// -- Ejercicio 1

console.log("Ejercicio 1");
let numero = 18;
if (numero % 2 == 0){
    console.log('${numero} es un número par');
}else{
    console.log('${numero} es un número impar');
}

// -- Ejercicio 2

console.log("Ejercicio 2");
let suma = 0;
for (let i = 1; i <= 50; i++){
    suma += i;
    console.log("La suma de los números del 1 al 50 es", suma);
}

// -- Ejercicio 3

console.log("Ejercicio 3");
let dia = 7;
switch (dia){
    case 1 : console.log("Lunes");
    break;
    case 2 : console.log("Martes");
    break;
    case 3 : console.log("Miércoles");
    break;
    case 4 : console.log("Jueves");
    break;
    case 5 : console.log("Viernes");
    break;
    case 6 : console.log("Sabado");
    break;
    case 7 : console.log("Domingo");
    break;
    default : console.log("No es un día de la semana");
    break;
}

// -- Ejercicio 4

console.log("Ejercicio 4");
let contador = 10;
while (contador > 0){
    console.log(contador);
    contador--;
}
console.log("Explota Dramaticamente!💥");

// -- Ejercicio 5

console.log("Ejercicio 5");
let letra = "E";
let l = letra.toLowerCase();
if (l == "a" || l == "e" || l == "i" || l == "o" || l == "u"){
    console.log(`"${letra}" es una VOCAL`);
}else if (l >= "a" && l <= "z"){
    console.log(`"${letra}" es una CONSONANTE`);
}else{
    console.log(`"${letra}" no es una letra`);
}

// -- Ejercicio 6

console.log("Ejercicio 6");
for (let i = 1; i <= 100; i++){
    if (i % 3 == 0 && i % 5 === 0)
        console.log("FizzBuzz");
    else if (i % 3 == 0)
        console.log("Fizz");
    else if (i % 5 == 0)
        console.log("Buzz");
    else
        console.log(i);
}

// -- Ejercicio 7

console.log("Ejercicio 7");
let num1 = 10, num2 = 4, operador = "/";
switch (operador){
    case "+": console.log('${num1} + ${num2} = ${num1 + num2}');
    break;
    case "-": console.log('${num1} - ${num2} = ${num1 - num2}');
    break;
    case "*": console.log('${num1} * ${num2} = ${num1 * num2}');
    break;
    case "/": console.log('${num1} / ${num2} = ${num1 / num2}');
    break;
        if (num2 === 0) console.log("EUGH ESTA MAL... PORQUE VRGAS ESTA MAL SI METI TODO BIEN... ESTA MAL EN ALGO...PERO EN QUE CHINGADOS?...EN ALGOOO NI MODO");
    else console.log('${num1} / ${num2} = ${num1 / num2}');
    break;
    default: console.log("Operador no reconocido");
}

// -- Ejercicio 8

console.log("Ejercicio 8");
let num = 7, resultado = 1;
for (let i = n; i >= 1; i--){
    resultado *= i;
}
console.log(`${num}! = ${resultado}`);

// -- Ejercicio 9

console.log("Ejercicio 9");
let num = 37, esPrimo = true;
if (num < 2 ){
    esPrimo = false;
}else{
    for (let i = 2; i <= Math.floor(num/2); i++){
        if (num % i == 0){
            esPrimo = false;
            break;
        }
    }
}
console.log('${num} ${esPrimo ? "es" : "no es"} primo');

// -- Ejercicio 10

console.log("Ejercicio 10");
for (let fila = 1; fila <= 5; fila++) {
    let linea = "";
    for (let col = 1; col <= 5; col++) {
        linea += "*";
        console.log(linea);
    }
}

// -- Ejercicio 11

console.log("Ejercicio 11");
let a = 0, b= 1;
for (let i = 0; i < 15; i++){
    console.log(a);
    let temp = a + b;
    a = b;
    b = temp;
}

// -- Ejercicio 12

console.log("Ejercicio 12");
let collatz = 27, pasos = 0;
console.log(collatz);
while (collatz !==1){
    collatz = (collatz % 2 === 0 ) ? collatz / 2 : collatz * 3 + 1;
    console.log(collatz);
    pasos++;
}
console.log(`LLegamos a 1 en ${pasos}`);

// -- Ejercicio 13

console.log("Ejercicio 13");
let perfecto = 28, sumaDivisores = 0;
for (let i = 1; i < perfecto; i++){
    if (perfecto % i === 0) sumaDivisores += i;
}
if (sumaDivisores === perfecto){
    console.log('${perfecto} ES un numero perfecto (suma disivisores = ${sumaDivisores})');
}else{
    console.log('${perfecto} NO es un numero perfecto (suma disivisores = ${sumaDivisores})');
}


// -- Ejercicio 14

console.log("Ejercicio 14");
let decimal = 42, binario = "", temp = decimal;
while (temp > 0){
    binario = (temp % 2) + binario;
    temp = Math.floor(temp / 2);
}
if (decimal === 0) binario = "0";
console.log('${decimal} en binario es ${binario}');

// -- Ejercicio 15

console.log("Ejercicio 15");
let filas = 8;
for (let i = 1; i <= filas; i++){
    let linea = "";
    for (let j = 1; j <= i; j++){
        linea += j + "";
    }
    console.log(linea.trim());
}