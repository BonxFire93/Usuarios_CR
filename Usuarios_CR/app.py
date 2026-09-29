from flask import Flask, render_template, request, redirect, url_for, abort
from usuario import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    usuarios = Usuario.get_all()
    return render_template('usuarios.html', todos_los_usuarios=usuarios)

@app.route('/crear_usuario', methods=['POST'])
def nuevo_usuario():
    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.save(datos)
    return redirect(url_for('index'))

@app.route('/formulario')
def formulario():
    return render_template('formulario_usuarios.html')


@app.route('/usuarios/<int:usuario_id>')
def ver_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        abort(404)
    return render_template('ver_usuario.html', usuario=usuario)


@app.route('/usuarios/editar/<int:usuario_id>')
def formulario_editar_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        abort(404)
    return render_template('editar_usuario.html', usuario=usuario)


@app.route('/usuarios/actualizar/<int:usuario_id>', methods=['POST'])
def actualizar_usuario(usuario_id):
    datos = {
        'id': usuario_id,
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.update(datos)
    return redirect(url_for('index'))


@app.route('/usuarios/borrar/<int:usuario_id>')
def borrar_usuario(usuario_id):
    Usuario.delete(usuario_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
