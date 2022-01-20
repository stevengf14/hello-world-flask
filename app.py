from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)

app.secret_key = 'My_secret_key'

@app.route('/')
def index():
    if 'username' in session:
        return f'User {session["username"]} have been logged'
    return 'User have not been logged'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Omit validation of user and password
        user = request.form['username']
        # add user to session
        session['username'] = user
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))

@app.route('/hello_world')
def hello_world():
    app.logger.info(f'Get the path {request.path}')
    return 'Hello World'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello {name.upper()}'

@app.route('/age/<int:age>')
def show_age(age):
    return f'Your age is: {age}'

@app.route('/name/<name>', methods=['GET','POST'])
def show_name(name):
    return render_template('show.html', name=name)

@app.route('/change_route')
def change_route():
    return redirect(url_for('show_name', name='Steven'))

@app.route('/out')
def out():
    return abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html', error=error), 404

#REST Representational state transfer
@app.route('/api/show/<name>', methods=['GET','POST'])
def show_json(name):
    values = {'name': name, 'method_http': request.method}
    return jsonify(values)

if __name__ == '__main__':
   app.run(debug = True)