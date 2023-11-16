import sqlite3
import PySimpleGUI as sg

# create connection to the SQLite database
conn = sqlite3.connect('menu.db')

# create table for menu
conn.execute('''CREATE TABLE IF NOT EXISTS menu
             (meal_id INTEGER PRIMARY KEY,
             meal_name TEXT NOT NULL,
             meal_price REAL NOT NULL,
             meal_type TEXT NOT NULL,
             ingredients TEXT NOT NULL);''')

# close the connection


def insert_meal(id,meal_name,meal_price,meal_type,ingredients):
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()
    query ="INSERT INTO meals(meal_id, name, price, type, ingredients) VALUES({}, '{}', {}, '{}', '{}')".format(id,meal_name,meal_price,meal_type,ingredients)
    cursor.execute(query)
    conn.commit() #save changes
# function to insert a new meal in the menu
def add_meal(meal_name, meal_price, meal_type, ingredients):
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO menu (meal_name, meal_price, meal_type, ingredients) VALUES (?, ?, ?, ?)", (meal_name, meal_price, meal_type, ingredients))
    conn.commit()
    conn.close()

# function to list all meals in the menu
def list_meals():
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu")
    rows = cursor.fetchall()
    conn.close()
    return rows

# function to delete a meal from the menu and renumber the meal IDs
def delete_meal(meal_id):
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menu WHERE meal_id=?", (meal_id,))
    cursor.execute("SELECT meal_id FROM menu ORDER BY meal_id")
    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        cursor.execute("UPDATE menu SET meal_id=? WHERE meal_id=?", (i+1, row[0]))
    conn.commit()
    conn.close()

# function to update a meal in the menu
def update_meal(meal_id, meal_name, meal_price, meal_type, ingredients):
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE menu SET meal_name=?, meal_price=?, meal_type=?, ingredients=? WHERE meal_id=?", (meal_name, meal_price, meal_type, ingredients, meal_id))
    conn.commit()
    conn.close()

layout = [
    [sg.Text('Welcome to the Restaurant Menu!')],
    [sg.Button('Add Meal'), sg.Button('List Meals')], [sg.Button('Update Meal'), sg.Button('Delete Meal')],
    [sg.Button('Exit')],
    [sg.Text('')],
    [sg.Output(size=(100, 20))]
]

#create the PySimpleGUI window
window = sg.Window('Restaurant Menu', layout)

#start the event loop
while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Add Meal':
        meal_name = sg.popup_get_text('Enter the name of meal')
        meal_price = sg.popup_get_text('Enter the price of meal')
        meal_type = sg.popup_get_text('Enter the type of meal')
        ingredients = sg.popup_get_text('Enter the Ingredie')
        add_meal(meal_name, meal_price, meal_type, ingredients)
        print('Meal added successfully!')
    elif event == 'List Meals':
        rows = list_meals()
        print('{:<30} {:<30} {:<30} {:<30} {:<30}'.format('Meal ID', 'Meal Name', 'Price', 'Type', 'Ingredients'))
        for row in rows:
            print('{:<34} {:<34} {:<30} {:<30} {:<40}'.format(row[0], row[1], row[2], row[3], row[4]))
    elif event == 'Update Meal':
        meal_id = sg.popup_get_text('Enter the ID of the meal you want to update:')
        meal_name = sg.popup_get_text('Enter the new name of the meal:')
        meal_price = sg.popup_get_text('Enter the new price of the meal:')
        meal_type = sg.popup_get_text('Enter the new type of the meal:')
        ingredients = sg.popup_get_text('Enter the new ingredients of the meal:')
        update_meal(meal_id, meal_name, meal_price, meal_type, ingredients)
        print('Meal updated successfully!')
    elif event == 'Delete Meal':
        meal_id = sg.popup_get_text('Enter the ID of the meal you want to delete:')
        delete_meal(meal_id)
        print('Meal deleted successfully!')
#close the PySimpleGUI window

        add_meal(meal_name, meal_price, meal_type, ingredients)
        print('Meal added successfully!')
    elif event == 'List Meals':
        rows = list_meals()
        print('{:<10} {:<20} {:<10} {:<20} {:<20}'.format('Meal ID', 'Meal Name', 'Price', 'Type', 'Ingredients'))
        for row in rows:
            print('{:<10} {:<20} {:<10} {:<20} {:<20}'.format(row[0], row[1], row[2], row[3], row[4]))
    elif event == 'Update Meal':
        meal_id = sg.popup_get_text('Enter the ID of the meal you want to update:')
        meal_name = sg.popup_get_text('Enter the new name of the meal:')
        meal_price = sg.popup_get_text('Enter the new price of the meal:')
        meal_type = sg.popup_get_text('Enter the new type of the meal:')
        ingredients = sg.popup_get_text('Enter the new ingredients of the meal:')
        update_meal(meal_id, meal_name, meal_price, meal_type, ingredients)
        print('Meal updated successfully!')
    elif event == 'Delete Meal':
        meal_id = sg.popup_get_text('Enter the ID of the meal you want to delete:')
        delete_meal(meal_id)
        print('Meal deleted successfully!')

#close the PySimpleGUI window

window.close()
conn.close()