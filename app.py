from flask import Flask, request
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
    return f'Your name is: {name}'

if __name__ == '__main__':
   app.run(debug = True)