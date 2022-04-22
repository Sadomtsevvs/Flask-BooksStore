from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/submitbook', methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']
    return 'Book name is %s and author is %s' %(name, author)
    # return render_template('addbook.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username: str):
    return render_template('profile.html', username=username.capitalize(), isActive=True)

@app.route('/books')
def books():
    books = [{
    'name': 'Book '+str(i),
    'author': 'Author '+str(i),
    'cover': 'https://bukovero.com/wp-content/uploads/2016/07/Harry_Potter_and_the_Cursed_Child_Special_Rehearsal_Edition_Book_Cover.jpg'
    } for i in range(1, 6)]   
    return render_template('books.html', books=books)


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
