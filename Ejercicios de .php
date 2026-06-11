//Ejercicio 1

<?php

echo "## Contador de Pares e Impares 1 al 50 ##\n";

$pares = 0;
$impares = 0;

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 === 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Cantidad de pares: " . $pares . "\n";
echo "Cantidad de impares: " . $impares . "\n";
?>

//Ejercicio 2

<?php
echo "## Tabla de multiplicar del 8 ##\n\n";

for ($i = 1; $i <= 10; $i++) {
    echo "8 x " . $i . " = " . (8 * $i) . "\n";
}
?>

//Ejercicio 3

<?php

echo "## Juego: Adivina el Numero ##\n\n";

$numeroSecreto = 7; 
$intento = 1;
$contador = 0;

while ($intento !== $numeroSecreto) {
    $contador++;

    echo "Intento #" . $contador . ": Probando el numero " . $intento . "\n";

    if ($intento !== $numeroSecreto) {
        $intento++;
    }
}

echo "\n Adivinaste El numero secreto era: " . $numeroSecreto . "\n";
echo "Numero total de intentos: " . $contador . "\n";
?>

//Ejercicio 4

<?php
echo "## Suma de impares 1 al 100 ##\n\n";

$suma = 0;

for ($i = 1; $i <= 100; $i++) {
    if ($i % 2 !== 0) {
        $suma += $i;
    }
}

echo "La suma de los impares del 1 al 100 es: " . $suma . "\n";
?>

//Ejercicio 5

<?php
echo "## Verificacion licencia de conducir ##\n\n";

$edad = 20; 

if ($edad >= 18 && $edad <= 65) {
    echo "Con la edad de $edad años, CUMPLE los requisitos. \n";
} else {
    echo "Con la edad de $edad años, NO CUMPLE los requisitos. \n";
}
?>


//Ejercicio 6

<?php
echo "## Cuadrado 5x5 con # ##\n\n";

$lado = 5;

for ($fila = 1; $fila <= $lado; $fila++) {
    for ($columna = 1; $columna <= $lado; $columna++) {
        echo "#";
    }
    echo "\n";
}
?>

//Ejercicio 7

<?php
echo "## Clasificacion de un numero ##\n\n";

$numero = -3; 

if ($numero > 0) {
    echo "El numero $numero es POSITIVO.\n";
} else if ($numero < 0) {
    echo "El numero $numero es NEGATIVO.\n";
} else {
    echo "El numero es CERO.\n";
}
?>

//Ejercicio 8

<?php
echo "## Mar y Tierra 1 al 30 ##\n\n";

for ($i = 1; $i <= 30; $i++) {
    if ($i % 3 === 0 && $i % 5 === 0) {
        echo "MarTierra\n";
    } else if ($i % 3 === 0) {
        echo "Mar\n";
    } else if ($i % 5 === 0) {
        echo "Tierra\n";
    } else {
        echo $i . "\n";
    }
}
?>

//Ejercicio 9

<?php
echo "## Clasificación de temperatura ##\n\n";
$temperatura = 20; 

if ($temperatura < 10) {
    echo "Fria\n";
} else if ($temperatura <= 25) {
    echo "Templada\n";
} else {
    echo "Calurosa\n";
}
?>

//Ejercicio 10

<?php

echo "## Cuenta regresiva de Año Nuevo ##\n\n";

for ($i = 10; $i >= 1; $i--) {
    echo $i . "\n";
}

echo "Feliz Año Nuevo \n";
?>


