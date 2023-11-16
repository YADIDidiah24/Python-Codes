import mysql.connector
import PySimpleGUI as sg
from collections import deque



db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="yadidiah",
    database="restrauntmenu"
)

myCursor = db.cursor()
sg.theme('BrightColors')

def insert_meal(id,meal_name,meal_price,meal_type,meal_ingredients):
    
    query ="INSERT INTO meals(meal_id, name, price, type, ingredients) VALUES({}, '{}', {}, '{}', '{}')".format(id,meal_name,meal_price,meal_type,meal_ingredients)
    myCursor.execute(query)
    db.commit()
    print(myCursor.rowcount, "Record inserted successfully into meals table")
    
def delete_meal(id: int):
    
    query = "DELETE FROM meals WHERE meal_id={}".format(id)
    myCursor.execute(query)
    print(f"row with id: {id} is deleted from the table 'meals'")
    db.commit()
    
def update_meal(id,change,ans):
    query = f"UPDATE meals SET {change} = '{ans}' WHERE meal_id={id}"
    myCursor.execute(query)
    print(f"{change} has been changed for meal with id {id}")
    db.commit()

def filter_search(filters):
    query = "SELECT * FROM meals WHERE "
    filter_queries = [] 
    
    for key, value in filters.items():
        if value is not None and value != "":
            if isinstance(value, str):
                if value[0] =="<":
                    val = int(value[1:])
                    filter_queries.append(f"{key}<{val}")
                elif value[0] ==">":
                    val = int(value[1:])
                    filter_queries.append(f"{key}>{val}")
                elif value[0] =="=":
                    val = int(value[1:])
                    filter_queries.append(f"{key}={val}")
                else:
                    filter_queries.append(f"{key} LIKE '%{value}%'")
            else:
                filter_queries.append(f"{key}={value}")
    query += " AND ".join(filter_queries)
    myCursor.execute(query)
    data = myCursor.fetchall()
    return data

myCursor.execute('SELECT * FROM meals')
data = myCursor.fetchall()

meal_options = [row[0] for row in myCursor.fetchall()]
order_list = deque()
options = ['id', 'name', 'price','type','ingredients']
layout = [
        [[sg.Table(key="table",values=data, headings=[i[0] for i in myCursor.description], max_col_width=90, auto_size_columns=True, justification='left',row_height=35,enable_events=True)]],
        [sg.Text("Values")],


        [sg.Button("Insert Meal"),sg.Button("Delete Meal"),sg.Button("Update Meal",key="update"),sg.Button("Filter"),sg.Button('Enter',key="enter"),
        sg.Button("QUIT")],#sg.Button("Add Meals", key="add_meals")],
        [sg.Listbox(values=options,key="filter_box" ,size=(20, len(options)), select_mode='multiple',visible=False)],
        [sg.Text("Enter filter:", key ="filter", visible=False),sg.Input(key='filter_input', visible=False)],
        

        ]

window = sg.Window('Select your meals', layout, resizable=True)

#order_layout =  [   [sg.Text('Selected Meals:')],
#                    [sg.Table(values = order_list, headings=[i[0] for i in myCursor.description], key='-ORDER TABLE-')],
#                    [sg.Button('Submit Order'), sg.Button('Cancel')]
#]
# Create the add-to-order window



selected_row=0
# read the window for events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:   
        break
    if event == "table":
        try: 
            selected_row = values["table"][0]  # get the first (and only) selected row
            print("row is :",selected_row)
        except IndexError:
                pass


   # if event == "add_meals":
   #     order_window = sg.Window('Add Meal', order_layout)
   #     
   #     while True:
   #         event, values = order_window.read()
   #         order_list.append(selected_row)
   #         print("atdtdtdt: ",order_list)
   #        order_window['-ORDER TABLE-'].update(values=order_list)
   #         if event == sg.WIN_CLOSED or event == 'Cancel':
   #             break
           
            
                
   #         elif event == 'Submit Order':
   #             # Do something with the order list (e.g. calculate the total price)
   #             total_price = sum([meal['price'] for meal in order_list])
   #             # Display the total price in a message box
   #             sg.popup(f'Total price: {total_price}')
   #             # Clear the order list and the table in the add-to-order window
   #             order_list.clear()
   #             order_window['-ORDER TABLE-'].update(values=order_list)
   #         elif event == 'Cancel':
                # Clear the order list and the table in the add-to-order window
   #             order_list.clear()
   #             order_window['-ORDER TABLE-'].update(values=order_list)
   #             # Close the add-to-order window
   #             order_window.close()


    elif event == "Delete Meal":
        meal_id = sg.popup_get_text('Enter the ID of the meal you want to DELETE:')
        confirm_popup = sg.popup_ok_cancel('Are you sure you want to delete this record?', title='Delete Record')
        if confirm_popup == 'OK':
            # get the selected row ID
            
                # delete the row from the database
                delete_meal(meal_id)
                # refresh the table data
                myCursor.execute('SELECT * FROM meals')
                data = myCursor.fetchall()
                window.Element("table").update(values=data)
            

    elif event == 'Insert Meal':
        meal_id = sg.popup_get_text(message = 'Enter the meal id',title = "id")
        meal_name = sg.popup_get_text(message = 'Enter the meal name', title = "name")
        meal_price = sg.popup_get_text(message = 'Enter the meal price',title = "price")
        meal_type = sg.popup_get_text(message = 'Enter the meal type',title = "type")
        ingredients = sg.popup_get_text(message = 'Enter the Ingredients',title = "ingredients")
        insert_meal(meal_id,meal_name, meal_price, meal_type, ingredients)
        myCursor.execute('SELECT * FROM meals')
        data = myCursor.fetchall()
        window.Element("table").update(values=data)
    #elif event=='Delete Meal':
     #   meal_id = sg.popup_get_text('Enter the ID of the meal you want to delete:')
      #  delete_meal(meal_id)
       # data = myCursor.fetchall()
        #window.refresh()
        #print('Meal deleted successfully!')
        

    elif event=="update":
        meal_id = sg.popup_get_text('Enter the ID of the meal you want to update:')
        change = sg.popup_get_text('Enter what to change:')
        value = sg.popup_get_text('Enter the new changed value:')

        update_meal( meal_id,change,value)
        
        myCursor.execute('SELECT * FROM meals')
        data = myCursor.fetchall()
        window.Element("table").update(values=data)

    elif event=="Filter":
        window["filter_box"].update(visible=True)
        window["filter"].update(visible=True)
        window["filter_input"].update(visible=True)

        window["enter"].update(visible=True)
    if event== 'enter':
        list1 = values["filter_input"].split()
        dict_values={}
        for i in range(len(values["filter_box"])):
            dict_values[values["filter_box"][i]]=list1[i]
        

        data = filter_search(dict_values)
        if data:
            window["table"].update(values=data)
        else:
            print("No data found.")

                    

    elif event == 'QUIT':

        sg.popup('GOODBYE! 😁 ')
        break

window.close()
db.close()
