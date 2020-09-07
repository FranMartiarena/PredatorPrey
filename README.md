# Modelo Presa Depredador by Prittiao


## Metodologia
<br>
Esta simulacion se va a llevar a cabo atravez de un automata celular programado en python usando pygame, matplotlib y pandas.

Un automata celular es un conjunto de celulas que interactuan en un espacio segun un conjunto de reglas dadas. "Un juego de 0 jugadores".

Cada celula podra tener uno de tres estados: Presa, depredador, o territorio
En este caso, las celulas tendran geometria cuadrada y estaran ubicadas en un plano bidimensional, afectadas por los estados de sus celulas vecinas, en un area de Moore(radio 1).
El sistema sera un sistema cerrado y no del tipo toroideal, ya que lo ideal es que los depredadores puedan encerrar a las presas.
## Reglas
<br>
Dada una celula de posicion (x,y) dentro del plano, se evaluara su estado, el cual puede ser presa, depredador, o vacio(territorio).
Si la celula es presa, se calculara una probabilidad de muerte segun la cantidad de presas a su alrededor. Si sobrevive, la celula se queda en el mismo estado, si muere la celula estara vacia
y habra una probabilidad de que se transforme en un depredador.

Si la celula es depredador, esta tendra tambien una probabilidad de morir, pero estara presente en todo momento(No como en la presa, que dependera de la cantidad de depredadores a su alrededor).

Si la celula esta vacia, primero se evaluara si tiene algun depredador como vecino, si no es asi, y tiene solo presas, estas podran reproducirse con una probabilidad dada segun la cantidad de presas
apareciendo una nueva presa en el espacio vacio.
<br>
### Las reglas seran las siguientes(Pseudo-codigo):
<br>

![alt text](https://github.com/FranMartiarena/PredatorPrey/blob/master/pseudo.png?raw=true)

## Modificaciones
<br>
Si bien aplique estas reglas, lo hice de otra forma y con algunas modificaciones, como podran ver al ejecutar el codigo, le agregue al final de la simulacion una funcion que toma como parametros la cantidad de poblacion (presa  y depredador) y su generacion. De esta forma se podra ver graficamente como es la oscilacion de cantidad de individuos en el territorio.
<br>
<br>
![alt text](https://github.com/FranMartiarena/PredatorPrey/blob/master/Simulation.png?raw=true)

![alt text](https://github.com/FranMartiarena/PredatorPrey/blob/master/presa_depredadpr.png?raw=true)
