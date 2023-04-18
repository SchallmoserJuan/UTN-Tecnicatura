// Hoisting
miFuncion(8,2)

// Funciones en JavaScript
function miFuncion(a,b) {
    console.log('Sumamos: '+ (a+b));
    return a + b;
}

// Llamada a la funcion
miFuncion(2,2);


let resultado = miFuncion(10,2);
console.log(resultado);


// Funcion de tipo expresión o anonima
let x = function(a,b){return a+b}
resultado = x(4,5) // al llamarla se pone la variable y los parentesis
console.log(resultado);



// Funciones de tipo self y invoking
(function(a,b){
    console.log('Ejecutando la función: '+ (a + b));
})(9,6)


console.log(typeof miFuncion);



// Cuantos argumentos se han definido en una funcion
function miFuncionDos(a,b) {
    console.log(arguments.length);
}
miFuncionDos(5,4,2)




// toString
var miFuncionTexto = miFuncionDos.toString() 
console.log(miFuncionTexto);





// Funciones Flecha
const sumarFuncionFlecha = (a,b) => a + b // const es una variable constante = no cambia
resultado = sumarFuncionFlecha(2,1)
console.log(resultado);





let sumar = function(a =  4,b = 2){

    console.log(arguments[0]); // muestra el parametro de a ->
    console.log(arguments[1]); // muestra el parametro de b ->
    console.log(arguments[2]); // muestra el parametro de c ->

    return a + b + arguments[2];
}

resultado = sumar(8,2,6) // Reasignacion de valores
console.log(resultado);



// Hoisting -> llamar a la función antes de ser creada o definida



// sumar todos los argumentos
let respuesta = sumarTodo(5,4,13,10,9)
console.log(respuesta); // Respuesta ->

function sumarTodo(){

    let suma = 0
    for (let i = 0; i < arguments.length; i++) {
        suma += arguments[i] // arguments es para arreglos
        
    }
    return suma;

}




// Tipos primitivos
let k = 10;
function cambiarValor(a){ // Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k);






const persona = {
    nombre: 'Juan',
    apellido: 'Schallmoser',
    edad: 22
}
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio'
    p1.apellido = 'Perez'
    p1.edad = 19
}

//llamdo
cambiarValorObjeto(persona)

console.log(persona);