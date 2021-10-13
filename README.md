# Assassin Game

Implementación del famoso juego [Assassin Game](<https://es.wikipedia.org/wiki/Asesino_(juego)>) en Python 3.9, para la materia de Programación II de la carrera de la Licenciatura En Ciencias de la Computación, UNR.

## Jugabilidad

Es un juego de rol que consiste en matarse entre jugadores hasta que quede uno solo vivo dentro de una cierta distancia.
Nuestro juego se divide en dos partes: el juego de los mayores de edad y el de los menores.
En cada turno se formaran parejas de jugadores que pelearan entre sí y ganará uno de ellos pasando a la siguiente ronda. Si en alguna ronda
un jugador dentro de una misma ciudad no consigue un oponente ira a buscar a su ciudad vecina dentro de una cierta distancia.
Cuando no sepuedan hacer mas peleas, es decir, cuando ya haya 1 persona en cada zona se dará por terminado el juego ganando así solo los jugadores que esten con vida.

## Ejecución

Se necesitan dos archivos para la ejecución del programa, uno que contenga jugadores con el siguiente formato:

```
nombre,edad,ciudad
```

y uno que contenga las distancias entre las ciudades con el siguiente formato:

```
ciudad1, ciudad2, distancia
```

Se ejecuta con el comando

```
$ python3 src/main.py ruta/del/archivo/jugadores ruta/del/archivo/distancias
```

El programa le pedira la distancia máxima que puede haber entre dos ciudades. Una vez ingresada, procederá a escribir en un archivo denominado 'output.txt' la información sobre cada eliminacion, que jugador mató a quien, y los ganadores, todo dividido por bloques de edad.

## Testing

El framework utilizado para testear es Pytest, los mismos se corren de la siguiente manera:

```
$ cd src
$ python3 -m pytest ../tests/
```
