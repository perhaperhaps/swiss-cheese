from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():

    user_input = ''

    if request.method == 'POST':

        # Retrieve user input from the form

        user_input = request.form.get('user_input', '')

        # Sanitize user input using Jinja's escape function

        sanitized_input = escape(user_input)

        # Display sanitized user input in the template

        return render_template('index.html', user_input=sanitized_input, display_script=True)

    return render_template('index.html', user_input=user_input, display_script=False)

if __name__ == '__main__':

    app.run(debug=True, port=5001)
