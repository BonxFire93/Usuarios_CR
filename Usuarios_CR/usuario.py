from mysqlconnection import connectToMySQL
class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM usuarios;'
        resultados_query = connectToMySQL('esquema_usuarios').query_db(query)
        lista_usuarios = []
        for usuario in resultados_query or []:
            lista_usuarios.append(cls(usuario))
        return lista_usuarios

    @classmethod
    def get_by_id(cls, usuario_id):
        query = 'SELECT * FROM usuarios WHERE id = %(id)s;'
        resultados = connectToMySQL('esquema_usuarios').query_db(query, {'id': usuario_id})
        if not resultados:
            return None
        return cls(resultados[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());'
        return connectToMySQL('esquema_usuarios').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = '''UPDATE usuarios
                   SET nombre = %(nombre)s, apellido = %(apellido)s,
                       email = %(email)s, updated_at = NOW()
                   WHERE id = %(id)s;'''
        return connectToMySQL('esquema_usuarios').query_db(query, data)

    @classmethod
    def delete(cls, usuario_id):
        query = 'DELETE FROM usuarios WHERE id = %(id)s;'
        return connectToMySQL('esquema_usuarios').query_db(query, {'id': usuario_id})
