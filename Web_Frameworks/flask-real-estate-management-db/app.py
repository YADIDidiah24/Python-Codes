
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from PIL import Image
import base64
import io
app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yadidiah",
    database="real_estate_management_system"
)

cursor = db.cursor()

@app.route('/')
def index():
    # Fetch all properties from the database
    cursor.execute("SELECT * FROM properties")
    properties = cursor.fetchall()
    
    # Prepare a list to store tuples of (property_data, image_data)
    property_data_with_images = []
    
    # Iterate through each property
    for property_data in properties:
        # Fetch image data for the property
        cursor.execute("SELECT image FROM properties WHERE PropertyID = %s", (property_data[0],))
        image = cursor.fetchone()
        
        # If there's an image, decode it
        if image and image[0]:
            binary_data = base64.b64decode(image[0])
            # Convert binary data to image
            image_obj = Image.open(io.BytesIO(binary_data))
            # Convert image back to binary and encode as base64
            buffered = io.BytesIO()
            image_obj.save(buffered, format="JPEG")
            encoded_img_data = base64.b64encode(buffered.getvalue())
            property_data_with_images.append((property_data, encoded_img_data.decode('utf-8')))
        else:
            # If no image is found, append None
            property_data_with_images.append((property_data, None))

    return render_template('index.html', properties=property_data_with_images)
# Add routes for other types of data (clients, offices, transactions)

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


@app.route('/add_property', methods=['POST'])
def add_property():
    if request.method == 'POST':
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        property_type = request.form['property_type']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        square_feet = request.form['square_feet']
        price = request.form['price']
        image_file = request.files['image']

        # Insert property into the database
        cursor.execute("INSERT INTO Properties (Address, City, State, ZIP, PropertyType, Bedrooms, Bathrooms, SquareFeet, Price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (address, city, state, zipcode, property_type, bedrooms, bathrooms, square_feet, price))
        db.commit()

        # Get the last inserted property ID
        property_id = cursor.lastrowid

        # Save image data to PropertyImages table
        if image_file:
            image_data = image_file.read()
            cursor.execute("UPDATE Properties SET image = %s WHERE PropertyID = %s", (image_data, property_id))
            db.commit()

        return redirect(url_for('index'))

@app.route('/delete_property/<int:property_id>', methods=['POST'])
def delete_property(property_id):
    # Delete property from the database
    cursor.execute("DELETE FROM Properties WHERE PropertyID = %s", (property_id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
