# Demo-Flask-app

This Python script utilizes the Flask web framework to create a simple web application with a form for user input. The application has a single route ('/') that handles both GET and POST requests. When a user visits the page, they are presented with an HTML form containing fields for a username and password. The form uses the POST method to send data to the server.

In the Flask app's Python code, the index function checks if the request method is POST. If it is, it retrieves the username and password from the form submission using request.form. The data is then printed for demonstration purposes, but you can replace the print statement with any logic you want to perform with the submitted data.

The HTML template ('index.html') includes a basic form structure with styling using CSS. The form has two input fields for the username and password, and a submit button. The styling is simple, providing a clean and centered layout. The Flask app is run with debugging enabled when the script is executed directly.

In summary, this script creates a web application using Flask, with a form for user input. The server-side logic captures and prints the submitted data when the form is submitted. The HTML template provides a visually pleasing and responsive interface for users to enter their information.
