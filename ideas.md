## Ejercicio 1 (Nivel Jr):
Imaginemos una concesionaria de autos y motos.
Crear un programa cuyo punto de entrada sea un index.js en donde, al ejecutarse, se visualiza lo siguiente por consola y se termina la ejecución:

    Marca: Peugeot // Modelo: 206 // Puertas: 4 // Precio: $200.000,00
    Marca: Honda // Modelo: Titan // Cilindrada: 125c // Precio: $60.000,00
    Marca: Peugeot // Modelo: 208 // Puertas: 5 // Precio: $250.000,00
    Marca: Yamaha // Modelo: YBR // Cilindrada: 160c // Precio: $80.500,50

    Vehículo más caro: Peugeot 208
    Vehículo más barato: Honda Titan
    Vehículo que contiene en el modelo la letra ‘Y’: Yamaha YBR $80.500,50

Ejercicio extra:
Vehículos ordenados por precio de mayor a menor:
Peugeot 208
Peugeot 206
Yamaha YBR
Honda Titan

La solución debe cumplir con los siguientes requisitos:
- La salida es por consola y exactamente como se requiere.
- Cargar la lista de autos en un único método. No hay ingreso por pantalla de ningún tipo.
- El algoritmo usado para la impresión no tiene que depender de la cantidad, modelo o tipo de autos

-----------------------------

## Ejercicio 2 (Nivel Trainee):
Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
Se pide imprimir el nombre, el apellido y el promedio.
Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".

-----------------------------

## Ejercicio 3 (Nivel Jr):
Una escuela tiene alumnos, cuyas características son:

*Nombre
*Apellido
*Nota Matematica
*Nota Lengua
*Nota geografía
*Promedio

-Los alumnos pueden dar exámenes.

La escuela también tiene profesores que tienen las siguientes características:

*Nombre
*Apellido
*Materia que enseña

-Los profesores toman exámenes y le dan al alumno una nota.

Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores y que el resultado sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).

-----------------------------

Cuestionario copado: http://www.etnassoft.com/2011/05/24/cuestionario-para-autoevaluar-nuestro-nivel-javascript/

-----------------------------

# Ejercicio 4 (Nivel Jr):
Crea un método que:⁠
· si recibe 0, devuelva 1.⁠
· si recibe 1, devuelva 0.⁠
⁠
No puedes usar condicionales con if, ternarias, operadores lógicos ni bitwise.
⁠
-----------------------------

# Ejercicio 5 (Nivel SSR):
Dados dos calendarios de dos personas diferentes, crear una función que devuelva el horario en que ambos estan libres para poder tener una reunión.
A tener en cuenta:
Cada persona indica su horario de ingreso y egreso, no pudiendo nunca tener una reunión antes de su ingreso ni despues de su egreso.
Todos los horarios informados estan en forma de Array.
Puede suponer que los calendarios estan ordenados.
El horario de final y inicio de la siguiente reunión puede ser el mismo.
La reunión debe tener un tiempo mínimo de 1 hora libre.

Ejemplo
Persona A:
Horario de trabajo: [8:00 - 17:00]
Día: [8:30 - 9:30] | [10:30 - 12:00] | [14:00 - 15:30] | [16:00 - 17:00]

Persona B:
Horario de trabajo: [7:00 - 16:00]
Día: [8:00 - 9:00] | [11:00 - 13:00] | [14:00 - 14.30]

RESULTADO:
Horas libres para ambos: [9.30 - 10.30] | [13:00 - 14:00] | [14:30 - 16:00]

-----------------------------

# Ejercicio 6 (Nivel Jr):
Escribe un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por el palabro “Fizz” y, a su vez, los múltiplos de 5 por “Buzz”. Para los caosos que, al tiempo, son múltiplos de 3 y 5, utiliza el combinado “FizzBuzz”

-----------------------------

# Ejercicio 7 (Nivel Jr):
Escribe una función que reciba por parámetros dos string (str1, str2) y devuelva la cantidad de veces que str2 se reputa en str1
Ejemplo: 
ababa, aba => 2

-----------------------------

# Ejercicio 8 (Nivel SSR):
Crea una función que reciba por parametro un string y devuelva ese mismo string con la ultima letra ubicada en la primera posición y en mayuscula.
Ejemplo:
Poroto => Oporot
Cangrejo => Ocangrej

-----------------------------

# Ejercicio 9 (Nivel SSR):
1) Crear un canvas en un HTML de tamaño 200 x 200.
2) Crear una función en JavaScript que partiendo del punto 100, 100 cree una linea que se mueva con las flechas del teclado.

-----------------------------

# Ejercicio 10 (Nivel SSR):
Crear una función que dado un array numerico  devuelva la primera y ultima posición donde un mismo numero se repite.
Ejemplo:
<br>
[1, 2, 10, 5, 7, 1, 2, 5, 8, 4, 10, 1, 2, 7, 6, 5]<br>
2 => 1 - 11<br>
5 => 3 - 14<br>
1 => 0 - 10<br>
10 => 2 - 10<br>

-----------------------------

# Ejercicio 11 (Nivel SSR - SR):
Crear una función que reciba como parámetro un string y devuelva otro string que cumpla con los siguientes puntos.<br>
A = @<br>
E = 3<br>
I = 1<br>
O = 0<br>
U = V<br>
Además, la letra siguiente a una vocal debe estar en mayúscula.<br>
<br>
Ejemplo:
|Imput       |   Output |
|--|--|
|Fernando    |   F3Rn@Nd0
|Luciano     |   LVC1@N0
|Yamila      |   Y@M1L@

-----------------------------
# Ejercicio 12 (Nivel Jr - SSR)
Crear una función que reciba dos números como parámetros y los multiplique sin utilizar el operador multiplicación. Tener en cuenta que los números pasados pueden ser positivos o negativos.

-----------------------------
# Ejercicio 13 (Nivel Jr).
Crear una función que devuelva el número más grande un arreglo iterando una sola vez por él.

-----------------------------
# Ejercicio 14 (Nivel Jr - SSR)
Iterando un arregla solo una vez escribir una función que elimine los undefinded, 0, null, false.

-----------------------------
# Ejercicio 15 (Nivel SSR - SR)
Escribir una función que aplane los arreglos en un nivel.
Ejemplo:
arr = [[1,2], [[3,4]],[1,[]]]
res = [1,2, [3,4],1, []]

-----------------------------
# Ejercicio 16 (Nivel SSR - SR)
Escrbibir una función que verifique si un string es un palindromo

-----------------------------
# Ejercicio 17 (Nivel SR +)
Pensemos en un telefono viejo. Si recordamos el teclado se veía algo así:

   	 1		 2		 3
			abc	   	def
			
	 4		 5		 6
	ghi    		jkl     	mno
	
 	 7		 8		 9
	pqrs   		tuv     	wxyz
	
		    	 0
       
Se solicite que creé un método, que reciba dos parámetros, un número (como string) y un arreglo de strings. El mismo debe determinar que palabras dentro del arreglo string se pueden formar con los numeros ingresados como primer parámetro.<br>
Ej:<br> 
number: "3662277"<br>
words : ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]<br>

Output: ["foo", "bar", "foobar", "emo", "cap", "car"]<br>




