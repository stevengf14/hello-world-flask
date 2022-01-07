from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)

@app.route('/')
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

if __name__ == '__main__':
   app.run(debug = True)