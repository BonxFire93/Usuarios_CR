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
        for elemento in resultados_query:
            lista_usuarios.append(cls(elemento))
        return lista_usuarios

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());'
        return connectToMySQL('esquema_usuarios').query_db(query, data)