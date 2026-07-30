from flask import Flask, render_template, request, redirect
from usuario import Usuario

app = Flask(__name__)

@app.route('/') #dirección de la ruta principal
def index(): 
    usuario = Usuario.get_all() 
    return render_template('usuarios.html', todo_los_usuarios = usuario)

@app.route('/crear_usuario', methods=['POST']) #dirección de la ruta para crear un nuevo usuario, no olvidarse del método POST
def nuevo_usuario():
    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.save(datos)
    return redirect('/') #redirecciona a la ruta principal

@app.route('/formulario') #dirección de la ruta para mostrar el formulario de creación de usuario
def formulario():
    return render_template('formulario_usuarios.html') #renderiza el template formulario.html

if __name__ == '__main__':
    app.run(debug = True)