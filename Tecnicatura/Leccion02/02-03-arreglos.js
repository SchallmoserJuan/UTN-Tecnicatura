// Arreglos en Javascript

// Declarar un arreglo ->
const autos = ['Ferrari','Renault','BMW'];
console.log(autos);

// Recorrer elementos de un arreglo
console.log(autos[0])
console.log(autos[2])

//Ciclo for
for(let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i])
}

//Modificar elementos de un arreglo
autos[1] = 'Volvo'
