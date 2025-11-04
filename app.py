from flask import Flask, render_template, request

import forms

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/alumnos', methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.email.data
    return render_template('alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em)

@app.route('/figuras', methods=['GET','POST'])
def figuras():
    form = forms.FiguraForm(request.form)
    area = ""
    figura = ""

    if request.method=='POST' and form.validate():
        figura = request.form.get('figura')
        valor1 = form.valor1.data
        valor2 = form.valor2.data

        if figura == 'triangulo':
            area = 0.5 * valor1 * valor2
        elif figura == 'rectangulo':
            area = valor1 * valor2
        elif figura == 'circulo':
            area = 3.1416 * valor1 * valor1
        elif figura == 'pentagono':
            area = (5 * valor1 * valor2) / 2

    return render_template('figuras.html', form=form, area=area, figura=figura)

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