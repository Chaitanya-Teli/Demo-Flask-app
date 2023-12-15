from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form submission
        username = request.form['username']
        password = request.form['password']

        
        print(f"Username: {username}, Password: {password}")

    # Render the HTML template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
