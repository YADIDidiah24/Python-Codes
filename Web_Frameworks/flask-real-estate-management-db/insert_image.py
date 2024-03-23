import mysql.connector
import base64
# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yadidiah",
    database="real_estate_management_system"
)

# Create a cursor object
cursor = connection.cursor()

# Read the image file
with open(r"media\p4.jpg", "rb") as image_file:
    image_data = image_file.read()

image_data = base64.b64encode(image_data)
# Update the image data for a specific property
update_query = "UPDATE properties SET image = %s WHERE PropertyID = %s"
property_id = 5  # Update this with the appropriate property ID

try:
    cursor.execute(update_query, (image_data, property_id))
    connection.commit()
    print("Image inserted successfully.")
except mysql.connector.Error as error:
    print("Error inserting image:", error)

# Close the cursor and connection
cursor.close()
connection.close()
