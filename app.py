from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template("froyo_form.html")

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    return render_template("froyo_results.html", **request.args)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return render_template("favorites_form.html")

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    return render_template("favorites_results.html", **request.args)

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return render_template("secret_message_form.html")

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    return render_template("secret_message_results.html", message=sort_letters(request.form.get("message")))

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template("calculator_form.html")

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    op = request.args.get("operation")
    n1 = int(request.args.get("operand1"))
    n2 = int(request.args.get("operand2"))
    res = 0
    if op == "add":
        res = n1 + n2
    elif op == "subtract":
        res = n1 - n2
    elif op == "multiply":
        res = n1 * n2
    elif op == "divide":
        res = n1 / n2
    args = {**request.args, "result": res}
    return render_template("calculator_results.html", **args)



# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    compliment_count = int(request.args.get("num_compliments"))
    context = {
        "wants_compliments": request.args.get("wants_compliments") == "yes",
        "compliment_list": random.sample(list_of_compliments, compliment_count),
        "users_name": request.args.get("users_name")
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
