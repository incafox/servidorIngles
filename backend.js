// 0 a 18 niveles >> 4 modulos >> 4 clases >> dif actividades

// import express (after npm install express)
const express = require('express');
var MongoClient = require('mongodb').MongoClient

// MONGOOSE
let mongoose = require('mongoose');
const Schema = mongoose.Schema;

// getting-started.js

//const mongoose = require('mongoose');

//modelos

const instructorSchema = new mongoose.Schema({
  email: {type: String},
  clave: {type: String},
}, {collection: 'instructor'}); //buscan en ntal coleccion

var instructor = mongoose.model('instructor', instructorSchema);

const studentSchema = new mongoose.Schema({
  email: {type: String},
  clave: {type: String},
}, {collection: 'student'}); //buscan en ntal coleccion

var student = mongoose.model('student', studentSchema);

const adminSchema = new mongoose.Schema({
  email: {type: String},
  clave: {type: String},
}, {collection: 'admin'}); //buscan en ntal coleccion

var admin = mongoose.model('admin', adminSchema);
 
////====================
/////LOS ESQUEMAS FINALES
///=====================
//NOVEL >> MODULO >> CLASE


//actividad
//general nivel >> modulo >> clase

// "niveles" : [{modulo},{modulo} .... ]
// "modulo" : [{clase},{clase}, ... ]
// "clase" : [{actividad1},{actividad1}]  //una actidad por ahora
// "actividad" : varios tipos de actividades para cada pregunta
// "actividad" :{tipo : "ordenar", }

//plan solo un tipo de actividad, dicha actividad
//ya tendra todos los espacions necesatios
// ya en react haces un solo js para 
//  que interprete el json de acuerdo al tipo "switch"
//"actividad"   >> ESQUEMA 
const actividadSchema = new mongoose.Schema({
  tipo: {type: String},
  sentencia: {type: String},
  sentenciacorrecta :{type: String},
},); //buscan en ntal coleccion
var actividad = mongoose.model('actividad', actividadSchema);
//============

const claseSchema = new mongoose.Schema({
  nombre: {type: String},
  actividades: [actividadSchema]
},); //buscan en ntal coleccion
var clase = mongoose.model('clase', claseSchema);

const moduloSchema = new mongoose.Schema({
  nombre: {type: String},
  actividades: [claseSchema]
},); //buscan en ntal coleccion
var modulo = mongoose.model('modulo', moduloSchema);


const nivelSchema = new mongoose.Schema({
  nombre: {type: String},
  actividades: [claseSchema]
},); //buscan en ntal coleccion
var modulo = mongoose.model('nivel', nivelSchema);


//ESQUEMA CURSO
const cursoSchema = new mongoose.Schema({
  nombre: {type: String},
  instructor: {type : String},
  curricula: []
}, {collection: 'cursos'}); //buscan en ntal coleccion
var curso = mongoose.model('curso', cursoSchema);
//========================


//ESQUEMA USUARIO
const userSchema = new mongoose.Schema({
  email: {type: String},
  clave: {type: String},
  direccion: {type: String},
  fullname: {type: String},
  telefono: {type: String},
  tipo: {type: String},  //student, instructor, admin
  //cursos: [curso],
}, {collection: 'users'}); //buscan en ntal coleccion
var user = mongoose.model('user', userSchema);
//==========================
//==========================

async function run(user,pass, modelo) {
  await mongoose.connect('mongodb://localhost:27017/ilaof', { useNewUrlParser: true });
  //await mongoose.connection.dropDatabase();
  // const customerSchema = new mongoose.Schema({ name: String, age: Number, email: String });
  // const Customer = mongoose.model('Customer', customerSchema);
  /*
  const instructorSchema = new mongoose.Schema({
    email: {type: String},
    clave: {type: String},
  }, {collection: 'instructor'});
  var instructor = mongoose.model('instructor', instructorSchema);
  */
  //await instructor.create({ email: 'test-instructor@test.com', clave: '12345' });
  // Find all customers
  const docs = await modelo.find({email:user,clave:pass});
  console.log("resultados");
  console.log(docs);
  return docs;
  /*
  if (docs.length>0){
    return 'yes';
  }
  else{
    return 'no';
  }*/
}

 //run().catch(error => console.log(error.stack));

//module.exports = mongoose.model('Product', instructorSchema);

// create new express app and save it as "app"
const app = express();
var bodyParser = require('body-parser');
var Promise = require('promise');
var cors = require('cors');
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
    extended: true
}));

// server configuration
const PORT = 8080;

// create a route for the app
app.get('/mensaje', (req, res) => {
  res.send('aaeeaaaa');
});


app.post("/login-xxx", (req, res) => {
 var myData = req.body;
 myData.save()
 .then(item => {
 res.send("item saved to database");
 })
 .catch(err => {
 res.status(400).send("unable to save to database");
 });
});

app.post('/login-main',async function(req,res) {
  console.log('request =' + JSON.stringify(req.body))
  console.log(req.body);
  var user_name=req.body.email;
  var password=req.body.password;
  //console.log("username : " + user_name);
  //console.log("password : " + password);
  var temporal = { "email": user_name, "clave": password}
  mongoose.connect('mongodb://localhost:27017/ilaof', { useNewUrlParser: true });
  const docs = await user.find({"email":user_name});
  let temp = await docs;
  
  //res.send(temp);
  if (temp.length==0)
  {
    res.send("usuario no existe"); 
  }
  else
  {
    console.log(temp)
    console.log(temp[0].tipo)
      if (temp.clave===password)
      {
        /*
        switch (temp[0].tipo) {
          case "instructor":
            res.send("instructor");
            break;
          case "admin":
            res.send("admin");
            break;
          case "student":
            res.send("student");
          
            break;
          default:
            break;
        }*/
        res.send(temp[0].tipo)
      }
      else
      {
        res.send("fallido");
      }
  }
  
  /*
  if (final.length>0)
  {
    //console.log(final);
    res.send("instructor");
  }
  else
  {
    if (final2.length>0)
    {
        res.send("admin");
    }
    else{
      if (final3.length>0)
      {
        res.send("student");
      }
      else
      {
        res.send("noexiste");
      }
    }
    //res.send("no");
  }
  */




});




//*******************
//API -- ADMIN
//******************* 
app.post('/login-admin',async function(req,res){
  console.log('request =' + JSON.stringify(req.body))
    console.log(req.body);
    var user_name=req.body.email;
    var password=req.body.password;
    console.log("username : " + user_name);
    console.log("password : " + password);
    //res.send(user_name+ " -- "+password);
    //var temp = req.body;
    mongoose.connect('mongodb://localhost:27017/ilaof', { useNewUrlParser: true });
    //await instructor.create({ email: 'test-instructor@test.com', clave: '12345' });
    //await instructor.create({ email: 'test-instructor@test.com', clave: 'dafd' });
    const docs =instructor.find();
    console.log("resultados");
    const g =  run(user_name,password);
    let final = await g;
    console.log(g);
    if (String(final))
    {
      console.log(final);
      res.send("yes");
    }
    else
    {
      console.log(final);
      res.send("no");
    }
});


app.post('/admin-matricula', async function(req,res) {
	  var tipo=req.body.tipo;
    var email=req.body.email;
    var fullname = req.body.fullname;
    var telefono = req.body.telefono;
    var direccion = req.body.direccion;
    var password = req.body.clave;
    let temporal = {
      "email": email,
      "clave": password,
      "fullname": fullname,
      "telefono": telefono,
      "direccion": direccion,
      "tipo": tipo
    }

    mongoose.connect('mongodb://localhost:27017/ilaof', { useNewUrlParser: true });
    const docs = await user.find({email:email});
    let temp = await docs;
    if (temp.length>0){
      res.send("existe");
    }
    else{
      user.create(temporal);
      res.send("creado")
    }
});

app.post('/admin-get-students', async function(req,res) {
  
});

//activar cuenta de alumno
app.post('/admin-get-students', async function(req,res) {
});

//obtener lista de 
app.get('/admin-get-students', async function(req,res) {
});

//************************ 
//API -- INSTRUCTOR
//************************

app.post('/instructor-create-curso', async function(req,res) {
  var instructorx = req.body.instructor;
  var nombre_cursox = req.body.nombre_curso;
  //var password_confirm = req.body.descripcion;
  //var nombre_completo = req.body.fullname;
  
  await mongoose.connect('mongodb://localhost:27017/ilaof', { useNewUrlParser: true });
  const docs = await curso.find({nombre_curso: nombre_cursox, instructor: instructorx});// primero busca en la base de datos 
  let resultado = await docs;
  //TODO : inserta curso en base de datos
});

///asdasd
//{
//  "nombrecurso": "ingles nivel",
//  "curricula": [
//    {"type": "level", "name":"nivel 1"},
//    {"type": "module", "name":"module 1"},
//    {"type": "reorder-sentence", "sentence": "love cat i my"},
//    {"type": "", "sentence": "love cat i my"}
//  ]
//}

//misma funcion que base de datos >>> udpate >> si hay info, la actualiza, sino la crea
// curricula > NIVEL > MODULO> CLASE > EJERCICIOS, cada modulo tiene un examen final
app.post('/instructor-save-curse', async function(req,res) {
	  
});

//probablemente lo mas facil sea >>> update and e

//obtener lista de alumnos de un curso
app.get('/instructor-get-students', async function(req,res) {
});

//calificar a un alumno
app.post('/instructor-set-nota', async function(req,res) {
});

//
app.post('/student-get-info-curso', async function(req,res) {
});

//****************************
//API --- ESTUDIANTE
//**************************** 
app.post('/login-student',async function(req,res){
  console.log('request =' + JSON.stringify(req.body))
  console.log(req.body);
  //console.log(res)
  var user_name=req.body.email;
  var password=req.body.password;
  console.log("username : " + user_name);
  console.log("password : " + password);
  const docs = run(user_name, password, student);
  let final = await docs;
  console.log(final);
  if ( final.length>0 )
  {
    //console.log(final);
    res.send('yes');
  }
  else
  {
    //console.log(final);
    res.send('no');
  }
});

// > registrar cuenta
app.post('/student-register', async function(req,res) {
  //con 2 campos de clave y su clave repetida de confirmacion
});

//matricularse en curso
app.post('/student-matricularse', async function(req,res) {
});

//obtener informacion de un curso en especifico (un json sobre el avance del alumno)
app.post('/student-get-info-curso', async function(req,res) {
});

//obtiene info de lo que el estudiante ah avanzado hasta ahora
app.post('/student-get-info-curso', async function(req,res) {
});

// make the server listen to requests
app.listen(PORT, () => {
  console.log(`Server running at: http://localhost:${PORT}/`);
});
