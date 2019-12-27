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
col_cursos = db["cursos"]

app = Flask(__name__) #create the Flask app
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app)

@app.route('/json-example')
def jsonexample():
    return 'Todo...'


"""==============="""
"""SECCION ALUMNO"""
"""==============="""

#CREA CUENTA
@app.route('/student-api-registerstudent', methods=['POST'])
def register_student():    
    userd = request.json['email']
    named = request.json['name']
    passw = request.json['password']
    #revisa server
    #print (request.json)
    if (col_student.find_one({"email": userd})):
        return "none"
    else:
        col_student.insert({"email": userd})
    


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


"""==============="""
"""SECCION MAESTRO"""
"""==============="""


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


@app.route('/instructor-api-registercurso', methods=['POST'])
def register_curso():  
    nombrecurso = request.json['nombrecurso']
    nombretutor = request.json['nombretutor']
    descripcion = request.json['descripcion']
    
    #revisa server
    #print (request.json)
    col_cursos.insert({ "nombrecurso": nombrecurso, "nombretutor": nombretutor, "descripcion":descripcion, "status": "false"})
    pass


"""==============="""
"""SECCION ADMIN"""
"""==============="""

@app.route('/login-admin', methods=['POST'])
def login_admin():
    userd = request.json['email']
    passw = request.json['password']
    #revisa server
    #print (request.json)
    temp = col_admin.find_one({"email": userd})
    try:
        user = temp['email']
        pasw = temp['clave']
        if (user == userd and pasw == passw):
            #retorna   
            return "yes"
    except:
        return "no"#db.col_admin.find_one({"email": userd})

#EL ALUMNO SE REGISTRA SOLO LUEGO EL ADMIN SE ENCARGA DE ACTIVARLO LUEGO DEL PAGO
@app.route('/admin-api-activatestudent', methods=['POST'])
def addstudent():
    pass

@app.route('/admin-api-activatecurso', methods=['POST'])
def activatecurso():
    pass

@app.route('/admin-api-eliminatecurso', methods=['POST'])
def eliminatecurso():
    pass

@app.route('/admin-api-blockstudent', methods=['POST'])
def blockstudent():
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