from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/index')
def index():

    titulo="IEVN-1003 - PWA"
    listado=["Opera1","Opera2","Opera3","Opera4"]

    return render_template('index.html', titulo=titulo, listado=listado)


@app.route('/operas',methods=['GET','POST'])
def operas():

    if request.method == 'POST':
        x1=request.form.get('n1')
        x2=request.form.get('n2')
        resultado=int(x1)+int(x2)
        return render_template('operas.html', resultado=resultado)

    return render_template('operas.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/user/<string:user>')
def user(user):
    return "Hello"+ user

@app.route('/number/<int:num>')
def number(num):
    return "Number: {}".format(num)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "User ID: {} Name: {}".format(id, username)

@app.route('/suma/<float:a>/<float:b>')
def func(a, b):
    return "La suma de {}".format(a + b)

@app.route('/prueba')
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
    <p>Esta es una prueba de retorno de HTML en Flask.</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
    '''

# @app.route('/index')
# def index():
#     return '<h1>Welcome to the index page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)