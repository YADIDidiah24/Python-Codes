# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from flask_bcrypt import Bcrypt
import mysql.connector
from PIL import Image
import base64
import io

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'sec_5#y2L"F4Q8z\n\xec]/key'
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yadidiah",
    database="real_estate_management_system"
)

cursor = db.cursor()

def login_required_for_agents(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if session.get('role') != 'agent':
            return redirect(url_for('index'))  
        return fn(*args, **kwargs)
    return wrapper


def login_for_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if session.get('role') != 'admin':
            return redirect(url_for('login'))  
        return fn(*args, **kwargs)
    return wrapper

def prepare_property_data_with_images(properties):
    property_data_with_images = []

    for property_data in properties:
        cursor.execute("SELECT image FROM properties WHERE PropertyID = %s", (property_data[0],))
        image = cursor.fetchone()

        if image and image[0]:
            binary_data = base64.b64decode(image[0])
            image_obj = Image.open(io.BytesIO(binary_data))
            buffered = io.BytesIO()
            image_obj.save(buffered, format="JPEG")
            encoded_img_data = base64.b64encode(buffered.getvalue())
            property_data_with_images.append((property_data, encoded_img_data.decode('utf-8')))
        else:
            property_data_with_images.append((property_data, None))

    return property_data_with_images


@app.route('/')
def index():
    cursor.execute("SELECT * FROM properties")
    properties = cursor.fetchall()
    property_data_with_images = prepare_property_data_with_images(properties)
    return render_template('index.html', properties=property_data_with_images)



@app.route('/agents')
def show_agents():
    cursor.execute("SELECT * FROM agents")
    agents = cursor.fetchall()
    return render_template('agents.html', agents=agents)


@app.route('/clients')
def show_clients():
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    return render_template('clients.html', clients=clients)


@app.route('/offices')
def show_offices():
    cursor.execute("SELECT * FROM offices")
    offices = cursor.fetchall()
    return render_template('offices.html', offices=offices)

@login_for_admin
@app.route('/transactions')
def show_transactions():
    cursor.execute('''SELECT
        t.TransactionID,
        t.TransactionDate AS DATE,
        CONCAT(c.FirstName, ' ', c.LastName) AS client,
        CONCAT(p.City, ', ', p.State) AS Location,
        CONCAT(a.FirstName, ' ', a.LastName) AS Agent,
        o.OfficeName AS Office,
        t.Price AS Price,
        t.PaymentType,
        p.Address AS Property,
        p.PropertyType AS type,
        CONCAT(p.Bedrooms, ', ', p.Bathrooms) AS BedsBaths,
        p.SquareFeet as size
    FROM
        transactions t
    INNER JOIN
        properties p ON t.PropertyID = p.PropertyID
    INNER JOIN
        agents a ON t.AgentID = a.AgentID
    INNER JOIN
        offices o ON a.OfficeID = o.OfficeID
    INNER JOIN
        clients c ON t.ClientID = c.ClientID;
    ''')
    transactions = cursor.fetchall()

    return render_template('transactions.html', transactions=transactions)



@app.route('/search_properties', methods=['GET'])
def search_properties():
    location = request.args.get('location')
    price_from = request.args.get('price_from')
    price_to = request.args.get('price_to')
    property_type = request.args.get('property_type')
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')
    square_feet = request.args.get('square_feet')

    query = "SELECT * FROM properties WHERE 1=1"
    params = []

    if location:
        query += " AND (City LIKE %s OR State LIKE %s OR ZIP LIKE %s)"
        params.extend(['%' + location + '%'] * 3)

    if price_from:
        query += " AND Price >= %s"
        params.append(price_from)

    if price_to:
        query += " AND Price <= %s"
        params.append(price_to)

    if property_type:
        query += " AND PropertyType LIKE %s"
        params.append('%' + property_type + '%')

    if bedrooms:
        query += " AND Bedrooms = %s"
        params.append(bedrooms)

    if bathrooms:
        query += " AND Bathrooms = %s"
        params.append(bathrooms)

    if square_feet:
        query += " AND SquareFeet >= %s"
        params.append(square_feet)

    cursor.execute(query, params)
    properties = cursor.fetchall()

    property_data_with_images = prepare_property_data_with_images(properties)

    return render_template('index.html', properties=property_data_with_images, location=location, price_from=price_from, price_to=price_to, property_type=property_type, bedrooms=bedrooms, bathrooms=bathrooms, square_feet=square_feet)


@app.route('/filter_properties_by_type/<property_type>', methods=['GET'])
def filter_properties_by_type(property_type):
    cursor.execute("SELECT * FROM properties WHERE PropertyType = %s", (property_type,))
    filtered_properties = cursor.fetchall()
    property_data_with_images = prepare_property_data_with_images(filtered_properties)
    return render_template('index.html', properties=property_data_with_images)


@app.route('/clear_filters', methods=['GET'])
def clear_filters():
    return redirect(url_for('index'))

REGISTRATION_PASSWORD = "RealEstate"

@app.route('/register', methods=['GET', 'POST'])
@login_for_admin
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        validation_password = request.form['validation_password']

        if validation_password != REGISTRATION_PASSWORD:
            return render_template('register.html', message='Invalid validation password')

        # Hash the password using Flask-Bcrypt
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)", (username, hashed_password, role))
            db.commit()
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            return render_template('register.html', message='Username already exists')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[2], password):
            session['username'] = username
            session['role'] = user[3]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

@app.route('/add_property', methods=['GET', 'POST'])
@login_for_admin
def add_property():
    if request.method == 'POST':
        property_type = request.form['property_type']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        price = request.form['price']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        square_feet = request.form['square_feet']
        description = request.form['description']
        
        # Handle image upload
        image = request.files['image']
        if image:
            image_data = image.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
        else:
            encoded_image = None
        
        try:
            cursor.execute(
                """INSERT INTO properties (PropertyType, Address, City, State, ZIP, Price, Bedrooms, Bathrooms, SquareFeet, Description, Image)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (property_type, address, city, state, zip_code, price, bedrooms, bathrooms, square_feet, description, encoded_image)
            )
            db.commit()
            return redirect(url_for('index'))
        except mysql.connector.Error as err:
            return render_template('add_property.html', message='Error adding property: ' + str(err))

    return render_template('add_property.html')

@app.route('/manage_properties/<int:property_id>', methods=['GET', 'POST'])
@login_required_for_agents
def manage_property(property_id):
    if request.method == 'POST':
        property_type = request.form.get('property_type')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip_code')
        price = request.form.get('price')
        bedrooms = request.form.get('bedrooms')
        bathrooms = request.form.get('bathrooms')
        square_feet = request.form.get('square_feet')
        description = request.form.get('description')
        image = request.files.get('image')

        update_query = "UPDATE properties SET "
        update_params = []

        if property_type:
            update_query += "PropertyType = %s, "
            update_params.append(property_type)

        if address:
            update_query += "Address = %s, "
            update_params.append(address)

        if city:
            update_query += "City = %s, "
            update_params.append(city)

        if state:
            update_query += "State = %s, "
            update_params.append(state)

        if zip_code:
            update_query += "ZIP = %s, "
            update_params.append(zip_code)

        if price:
            update_query += "Price = %s, "
            update_params.append(price)

        if bedrooms:
            update_query += "Bedrooms = %s, "
            update_params.append(bedrooms)

        if bathrooms:
            update_query += "Bathrooms = %s, "
            update_params.append(bathrooms)

        if square_feet:
            update_query += "SquareFeet = %s, "
            update_params.append(square_feet)

        if description:
            update_query += "Description = %s, "
            update_params.append(description)

        if image:
            image_data = image.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            update_query += "Image = %s, "
            update_params.append(encoded_image)

        if update_params:
            update_query = update_query.rstrip(', ') + " WHERE PropertyID = %s"
            update_params.append(property_id)

            try:
                cursor.execute(update_query, tuple(update_params))
                db.commit()
                return redirect(url_for('index'))
            except mysql.connector.Error as err:
                return render_template('manage_property.html', property_id=property_id, message='Error updating property: ' + str(err))
        else:
            return render_template('manage_property.html', property_id=property_id, message='No changes detected.')

    else:
        cursor.execute("SELECT * FROM properties WHERE PropertyID = %s", (property_id,))
        property_data = cursor.fetchone()
        if property_data:
            return render_template('manage_property.html', property=property_data)
        else:
            return redirect(url_for('index'))



@app.route('/delete_property/<int:property_id>', methods=['POST'])
@login_required_for_agents
def delete_property(property_id):
    try:
        cursor.execute("DELETE FROM properties WHERE PropertyID = %s", (property_id,))
        db.commit()
    except mysql.connector.Error as err:
        return redirect(url_for('index', message='Error deleting property: ' + str(err)))
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
