# Lexical_analyzer
Lexical analyzer designed in Language Translators II class (compilers) for the following particular grammar:


## Grammar
**Grammar name:** C2  


**Library management**
* <palabra reservada> <nombre de librería>


**Declaration of variables or constants**
* <Tipo de dato> nombreVariable;
* const <tipo_de_dato> nombreVariable = <valor>

**Declaration of functions**
* <tipo_de_dato | nulo > función <nombre función>([<tipo variable> <variable>,]0..n | nulo)  
{  
    …  
    regresa <variable | numero | constante | nulo>  
}

**Comments**
* //    one line
* /* ……… */   many lines

**Instruction completion**  
'\n'

**Main declaration**  
principal()
{

}

**Data entry declaration to read a data from the keyboard**  
<variable> = leer()

**Data output declaration**  
imprime(\<variable\> | \<constante\> | \<numero\> | \<funcion\>)

**Reseverd words**  
libreria, const, nulo, regresa, principal

**Data types**  
entero, flotante, caracter, cadena, booleano

**Iterative commands**  
para(<inicialización>; <condición>; <incremento>) { … }  
mientras(<condición>){ … }  
hacer { … } mientras(\<condición\>)

**Selective commands**  
si(<condición>) { … }  
sino(<condición>) { …}  
finalmente { … }  
determina(<variable>) {
	siEs <valor|variable>: …
	enDefecto: ...
}

**Assignment operations**  
=, +=, -=, *=, /=, %=

**Logical operation**  
==, !=, \>, \<, \>=, \<=, &, |, !

**Mathematical operations**  
\+, \-, \*, \/, %, \*\*

**Production rules**

S ::=  [\<comentarios\>]* \<librerias\> [  [\<comentarios\>]* | \<funcion\> | \<constante\>]*   [<comentarios\>]* \<main\>  [\<comentarios\>]*  
\<comentarios\> ::= '//' \<palabra\>* | '/\*' \<palabra\>* '\*/'  
\<palabra\> ::= \<caracter\>\<palabra\> | 'ʎ'  
\<caracter\>::= [A..Z] | [a..z] | [0..9] | [‘!’,’#’,’$’,’%’,’&’,’/’] 
	
Grammar was defined in Spanish by agreement of the class.
