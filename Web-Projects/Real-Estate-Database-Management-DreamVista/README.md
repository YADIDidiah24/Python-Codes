# Real Estate Database Management DreamVista



# app.py

This script contains the backend code for a Flask web application managing a real estate management system.

## Libraries and Configuration

The script imports necessary libraries such as Flask, render_template, request, redirect, url_for, session, bcrypt, mysql.connector, PIL, base64, and io. It also configures the Flask application, sets up a secret key, connects to the MySQL database, and initializes a cursor object.

## Decorators

- `login_required_for_agents`: Ensures that only agents can access certain routes.
- `login_for_admin`: Ensures that only admins can access certain routes.

## Routes and Functionality

- `/`: Renders the index page showing all properties.
- `/agents`: Renders a page showing all agents.
- `/clients`: Renders a page showing all clients.
- `/offices`: Renders a page showing all offices.
- `/transactions`: Renders a page showing all transactions.
- `/search_properties`: Searches properties based on various criteria.
- `/filter_properties_by_type/<property_type>`: Filters properties by a specific type.
- `/clear_filters`: Clears all filters.
- `/register`: Allows admins to register new users.
- `/login`: Handles user authentication and login.
- `/logout`: Logs the user out.
- `/add_property`: Allows admins to add new properties.
- `/manage_properties/<int:property_id>`: Allows agents to manage properties.
- `/delete_property/<int:property_id>`: Allows agents to delete properties.

## Property Data Handling

- `prepare_property_data_with_images`: Prepares property data along with images for rendering.

## Error Handling

The script includes error handling for database operations.

## Main Function

The `__main__` block starts the Flask application and runs it in debug mode.




# HTML Code Description

## Base HTML Structure

- **Document Type Declaration (DOCTYPE):**
  - Declares the document type and version of HTML being used.

- **Language Attribute:**
  - Specifies the language of the document, set to English (`en`).

- **Head Section:**
  - Contains metadata about the document and links to external resources.
  - Character set (`meta charset`) is set to UTF-8.
  - Viewport meta tag (`meta name="viewport"`) adjusts the page's viewport to the device's screen width.

- **Title Tag:**
  - Sets the title of the page using a block statement (`{% block title %}`) which can be overridden in child templates.
  - Default title is "DreamVista Homes 🏠🌟 - Find Your Perfect Property".

- **External CSS:**
  - Links to Bootstrap CSS (`bootstrap.min.css`) and a custom CSS file (`style.css`).

## Body Section

- **Header Section:**
  - Contains the site's navigation bar (`nav`) with branding and menu items.
  - Menu items include links to "Agents", "Clients", "Offices", "Transactions" (if the user is an admin), "Add Property" (if the user is an admin), "Logout" (if a user is logged in), "Login", "Sign Up", and "Contact".

- **Main Section:**
  - Contains the main content of each page, which will be populated by child templates.

- **Footer Section:**
  - Appears only on the home page (`request.path == '/'`).
  - Contains information about the project, menu links, and copyright information.
  - Menu links include "About", "Contact", "Privacy Policy", and "Terms of Use".

## Script Tags
- **JavaScript Libraries:**
  - Includes jQuery and Popper.js for Bootstrap functionality.

## Index HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Properties - Dream Homes".

- **Content Block:**
  - Contains the main content of the index page.
  - Displays a title "Find Your Perfect Property".
  - Includes a form for filtering properties based on location, price range, property type, bedrooms, bathrooms, and square feet.
  - If any filters are applied, provides a button to clear them.
  - Displays properties in cards if available, showing details like image, title, location, type, bedrooms, bathrooms, square feet, and price.
  - Provides buttons to manage and delete properties, with confirmation for deletion.
  - If no properties are found, displays an info alert indicating so.

## Agents HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Agents - Dream Homes".

- **Content Block:**
  - Contains the main content of the agents page.
  - Displays a title "Agents".
  - Includes a responsive table to display agent details.
  - The table has the following columns: "Agent ID", "Name", "Email", "Phone", and "Office ID".
  - Iterates over the list of agents to populate the table rows.
  - Alternates row classes for styling purposes: even-indexed rows have the class "even", and odd-indexed rows have the class "odd".

## Clients HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Clients - Dream Homes".

- **Content Block:**
  - Contains the main content of the clients page.
  - Displays a title "Clients".
  - Includes a responsive table to display client details.
  - The table has the following columns: "Client ID", "Name", "Email", and "Phone".
  - Iterates over the list of clients to populate the table rows.
  - Alternates row classes for styling purposes: even-indexed rows have the class "even", and odd-indexed rows have the class "odd".

## Offices HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Offices - Dream Homes".

- **Content Block:**
  - Contains the main content of the offices page.
  - Displays a title "Offices".
  - Includes a responsive table to display office details.
  - The table has the following columns: "Office ID", "Office Name", "Address", "City", "State", and "ZIP".
  - Iterates over the list of offices to populate the table rows.
  - Alternates row classes for styling purposes: even-indexed rows have the class "even", and odd-indexed rows have the class "odd".

## Add Property HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Add Property - Dream Homes".

- **Content Block:**
  - Contains the main content of the add property page.
  - Displays a title "Add Property".
  - Includes a form to add a new property with fields for:
    - **Address:** Text input field for the property's address, marked as required.
    - **City:** Text input field for the property's city, marked as required.
    - **State:** Text input field for the property's state, marked as required.
    - **ZIP Code:** Text input field for the property's ZIP code, marked as required.
    - **Property Type:** Text input field for the type of property, marked as required.
    - **Bedrooms:** Number input field for the number of bedrooms, marked as required.
    - **Bathrooms:** Number input field for the number of bathrooms, marked as required.
    - **Square Feet:** Number input field for the square footage of the property, marked as required.
    - **Price:** Number input field for the price of the property, marked as required.
    - **Image:** File input field for uploading an image of the property, accepts image files and is marked as required.
  - Submit button to add the property.

## Manage Properties HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Manage Property - Dream Homes".

- **Content Block:**
  - Contains the main content of the manage property page.
  - Displays a header "Manage Property".
  - Includes a form to manage and update property details:
    - **Property Type:** Text input field for the type of property, pre-filled with the current property type.
    - **Address:** Text input field for the property's address, pre-filled with the current address.
  - Submit button to save changes to the property.
  ## Login HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Login - Dream Homes".

- **Content Block:**
  - Contains the main content of the login page.
  - Displays a title "Login".
  - Includes a form to login with the following fields:
    - **Username:** Text input field for the username, marked as required.
    - **Password:** Password input field for the password, marked as required.
  - Submit button to login.
  - If there is a `message` variable provided (e.g., error message), it displays an alert with the message content.

## Register HTML

- **Template Inheritance:**
  - Extends `base.html`, inheriting its structure and content.

- **Title Block Override:**
  - Overrides the title block from the base template to set the title as "Register - Dream Homes".

- **Content Block:**
  - Contains the main content of the register page.
  - Displays a title "Register".
  - Includes a form to register a new user with the following fields:
    - **Username:** Text input field for the username, marked as required.
    - **Password:** Password input field for the password, marked as required.
    - **Role:** Dropdown select input for the user's role with options for "Admin", "Agent", and "Client".
    - **Validation Password:** Password input field for the validation password, marked as required.
  - Submit button to register.
  - If there is a `message` variable provided (e.g., error message), it displays an alert with the message content.

# The style.css file contains global styles for the website, including font choices, background colors, and container widths. It styles the header with a dark blue background, navigation with white text, and hover effects. Main content is styled with margins, form controls with border radius, and cards with a hover effect and box shadow. The footer has a dark blue background and white text, with customized alignment for responsiveness. Additionally, an 'about' class is defined for left-aligned text.


# Installation Instructions

```sh
To install and run the Django Marketplace project locally, follow these steps:



1. **Install dependencies**: 
   pip install Flask

2. **Run the development server**: 
   python app.py

```

  
## [Yadidiah Kanaparthi](https://github.com/YADIDidiah24)  @ 2024


