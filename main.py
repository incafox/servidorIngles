import flask
from flask import jsonify, Flask, request,render_template  #import main Flask class and request object
import pymongo
#from flask.ext.cors import CORS
from flask_cors import CORS, cross_origin

#BASE DE DATOS GENERAL PARA ALUMNOS (SOLO REGISTRO)

#BASE DE DATOS CURSOS - IMPORTANTE

from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/") #crea cliente
db = myclient["ilaof"]  #crea base de datos
col_admin = db["admin"]
col_student = db["student"]
col_instructor = db["instructor"]


app = Flask(__name__) #create the Flask app
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app)

@app.route('/json-example')
def jsonexample():
    return 'Todo...'


#LOGIN SECTION
@app.route('/login-student', methods=['POST'])
def login_student():    
    userd = request.json['email']
    passw = request.json['password']
    #revisa server
    #print (request.json)
    temp = col_student.find_one({"email": userd})
    try:
        user = temp['email']
        pasw = temp['clave']
        if (user == userd and pasw == passw):
            #retorna   
            return "yes"
    except:
        return "no"#db.col_admin.find_one({"email": userd})

@app.route('/login-instructor', methods=['POST'])
def login_instructor():  
    userd = request.json['email']
    passw = request.json['password']
    #revisa server
    #print (request.json)
    temp = col_instructor.find_one({"email": userd})
    try:
        user = temp['email']
        pasw = temp['clave']
        if (user == userd and pasw == passw):
            #retorna   
            return "yes"
    except:
        return "no"#db.col_admin.find_one({"email": userd})



@app.route('/login-admin', methods=['POST'])
def login_admin():
    userd = request.json['email']
    passw = request.json['password']
    #revisa server
    #print (request.json)
    temp = col_student.find_one({"email": userd})
    try:
        user = temp['email']
        pasw = temp['clave']
        if (user == userd and pasw == passw):
            #retorna   
            return "yes"
    except:
        return "no"#db.col_admin.find_one({"email": userd})


@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    name = request.json['name']
    passw = request.json['password']
    #GRABA EN BASE DE DATOS
    pass

#INSTRUCTOR
@app.route('/registrarcurso', methods=['POST'])
def registrar_curso():
    tutor = request.json['tutor']
    nombrecurso = request.json['name']
    descripcion = request.json['descripcion']
    db.collection.insert({""})
    return "registrado"
    """
    #GRABA EN BASE DE DATOS
    if ( db_cursos.search(Consulta.name == nombrecurso) ):
        return "existe"
    else : #si no existe 
        db_cursos.insert({
            'tutor': tutor,
            'nombrecurso': nombrecurso,
            'descripcion': descripcion })
        return "registrado"
		"""
#ALUMNO
#@app.route('/getcursos-student')
#def get_cursos_student():
#    return jsonify(db_cursos.all())




#PARA ALUMNOS
@app.route('/registrarcurso', methods=['POST'])
def registrarse_encurso():
    tutor = request.json['tutor']
    nombrecurso = request.json['name']
    descripcion = request.json['password']
    #GRABA EN BASE DE DATOS"
    pass


#PARA ALUMNOS
@app.route('/inscribirse', methods=['POST'])
def inscribirse():
    nombrecurso = request.json['name']
    descripcion = request.json['password']
    pass


#PARA MAESTRO
#retorna sus cursos
@app.route('/getcursos/<string:maestro>',)
def cursos_instructor(maestro):
    #GRABA EN BASE DE DATOS
    pass
    #return (db_alumnos_general.search(Consulta.name == maestro) )


#retorna sus alumnos
@app.route('/getcursos/<string:maestro>',)
def alumnosporcurso(maestro):
    #GRABA EN BASE DE DATOS
    pass
    #return (db_alumnos_general.search(Consulta.name == maestro) )

if __name__ == '__main__':
    app.run(debug=True, port=8000) #run app in debug mode on port 5000