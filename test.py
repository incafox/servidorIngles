from tinydb import TinyDB, Query
User = Query()
db = TinyDB('users.json')
db.insert({
        'name': 'juan perez',
        'email': 'juan@gmail.com',
        'cursos': [{'activado': 'true'}, {'type': 'sudo'}]})
db.insert({
        'name': 'raul perez',
        'email': 'raul@gmail.com',
        'cursos': [{'activado': 'false'}, {'type': 'sudo'}]})
db.insert({
        'name': 'juan perez',
        'email': 'juan@gmail.com',
        'cursos': [{'activado': 'true'}, {'type': 'sudo'}]})
db.insert({
        'name': 'juan perez',
        'email': 'juan@gmail.com',
        'cursos': [{'activado': 'false'}, {'type': 'sudo'}]})

"""
db.insert_multiple([
        {'name': 'John', 'age': 22},
        {'name': 'John', 'age': 37}])"""


db.upsert({'name': 'Johndi', 'logged-in': True}, User.name == 'John')


o = db.search(User.name == 'juan perez')
print (o)

#k = db.get(User.name == 'John')
#print (k)
#borra todo
#db.purge_tables()
