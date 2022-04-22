from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




# @app.route('/admin')
# def welcome_admin():
#     return '<h1>Welcome, admin!</h1>'

# @app.route('/guest/<guest>')
# def welcome_guest(guest):
#     return '<h1>Welcome, %s!</h1>' % guest

# @app.route('/user/<name>')
# def welcome_user(name):
#     if name == 'admin':
#         return redirect(url_for('welcome_admin'))
#     else:
#         return redirect(url_for('welcome_guest', guest=name))


app.run(debug=True)
