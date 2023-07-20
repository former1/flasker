from flask import Flask, render_template


#create a flask instance

app =Flask(__name__)

#create a route decorator
@app.route('/')
#def index():
#    return "hello world"

def index():
    first_name="John"
    stuff="this is bold text"
    favorite_pizza=["pepperoni","ananas","sucuk","karisik"]
    return render_template('index.html',
                           stuff=stuff,
                           favorite_pizza=favorite_pizza,
                           first_name=first_name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
