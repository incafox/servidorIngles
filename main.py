
import flask
from flask import jsonify, Flask, request,render_template  #import main Flask class and request object
from tinydb import TinyDB, Query
#from flask.ext.cors import CORS
from flask_cors import CORS, cross_origin

#BASE DE DATOS GENERAL PARA ALUMNOS (SOLO REGISTRO)
db_alumnos_general = TinyDB('alumnos.json')

#BASE DE DATOS CURSOS - IMPORTANTE
db_cursos = TinyDB('cursos.json')

Consulta = Query()

app = Flask(__name__) #create the Flask app
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app)

@app.route('/form-example')
def formexample():
    return 'gaaaa'

@app.route('/json-example')
def jsonexample():
    return 'Todo...'

@app.route('/login-dashboard', methods=['POST'])
def login_page():
    
    userd = request.json['username']
    passw = request.json['password']
    if ( db_alumnos_general.search(Consulta.name == userd)):
        pass
    #revisa server
    #print (request.json)
    return userd + passw


@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    name = request.json['name']
    passw = request.json['password']
    #GRABA EN BASE DE DATOS
    if ( db_alumnos_general.search(Consulta.name == email) ):
        pass
    else : #si no existe 
        db_alumnos_general.insert({
            'name': name,
            'email': email,
            'password': passw  })
    pass


@app.route('/registrarcurso', methods=['POST'])
def registrar_curso():
    tutor = request.json['tutor']
    nombrecurso = request.json['name']
    descripcion = request.json['password']
    #GRABA EN BASE DE DATOS
    if ( db_alumnos_general.search(Consulta.name == nombrecurso) ):
        return "existe"
    else : #si no existe 
        db_alumnos_general.insert({
            'tutor': tutor,
            'nombrecurso': nombrecurso,
            'descripcion': descripcion })
        return "registrado"
		

#PARA ALUMNOS
@app.route('/registrarcurso', methods=['POST'])
def registrarse_encurso():
    tutor = request.json['tutor']
    nombrecurso = request.json['name']
    descripcion = request.json['password']
    #GRABA EN BASE DE DATOS
    if ( db_alumnos_general.search(Consulta.name == nombrecurso) ):
        return "existe"
    else : #si no existe 
        db_alumnos_general.insert({
            'tutor': tutor,
            'nombrecurso': nombrecurso,
            'descripcion': descripcion })
        return "registrado"


#PARA MAESTRO
#retorna sus cursos
@app.route('/getcursos/<string:maestro>',)
def cursos_instructor(maestro):
    #GRABA EN BASE DE DATOS
    return (db_alumnos_general.search(Consulta.name == maestro) )


#retorna sus alumnos
@app.route('/getcursos/<string:maestro>',)
def alumnosporcurso(maestro):
    #GRABA EN BASE DE DATOS
    return (db_alumnos_general.search(Consulta.name == maestro) )


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000