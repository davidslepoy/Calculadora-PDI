import cv2
import numpy as np
import matplotlib.pyplot as plt

""""
1. Cargar la imagen img_calculadora.tif.
"""

img = cv2.imread('img_calculadora.tif', cv2.IMREAD_GRAYSCALE)
plt.figure(), plt.imshow(img, cmap='gray'), plt.show(block=False) 

"""_
2. Determinar las dimensiones de img_calculadora.tif.
"""

img.shape ## Retorna (1134,1360) lo que quiere decir que tiene 1134 filas y 1360 columnas

"""
3. Determinar el valor máximo y mínimo de nivel de gris de img_calculadora.tif.
"""

img.min() ## Devuelve el minimo que es 12
img.max() ## Devuelve el maximo que es 255

"""
4. Buscar todos los valores de nivel de gris que tiene img_calculadora.tif ¿Cuántos
son?
"""

valores = np.unique(img) ##Esta linea de codigo devuelve todos los valores una unica vez a pesar de que se repitan
len(np.unique(img)) ## Retorna cuantos elementos distintos hay, en total hay 244

"""
5. ¿Cuál es el valor de nivel de gris con mayor repetitividad en img_calculadora.tif?
¿Y el menor? (Tener en cuenta que pueden ser más de uno).
"""

matriz = np.array(img)
conteos = np.unique(matriz, return_counts=True) ##Imprime cuantas veces aparece cada valor en la matriz
minimo,maximo = [],[]
for i in range(len(conteos)):
    if conteos[i] == conteos.max():
        maximo.append(int(valores[i]))
    elif conteos[i] == conteos.min():
        minimo.append(int(valores[i]))
print(f"Valores que más se repiten: {maximo}")##Imprime los valores que más se repite. En este caso es 71
print(f"Valores que menos se repiten: {minimo}")##Imprime los valores que menos se repite. En este caso es 12,13,14

"""
6. Recortar de img_calculadora.tif las teclas SIN, COS y TAN. 
Mostrar los recortes en una nueva figura utilizando subplots (un subplot para cada tecla recortada).
"""

##Creamos una nueva variable para la imagen para no generar defectos en la imagen original
imagen_prueba = img.copy()
plt.imshow(imagen_prueba, cmap='gray')
plt.show()
## Recortamos COS, SIN y TAN de forma manual
SIN = imagen_prueba[330:440,730:880]
COS = imagen_prueba[330:440,950:1100]
TAN = imagen_prueba[330:440,1180:1330]
##Graficamos los 3 recortes

plt.subplot(321)
h = plt.imshow(SIN, cmap='gray')
plt.colorbar(h)
plt.title('SIN')
plt.subplot(322)
h = plt.imshow(COS, cmap='gray')
plt.colorbar(h)
plt.title('COS')
plt.subplot(323)
h = plt.imshow(TAN, cmap='gray')
plt.colorbar(h)
plt.title('TAN')
plt.show()
"""
7. Pegar los recortes del punto anterior en la imagen original img_calculadora.tif pero
de manera que las teclas queden ordenadas en la calculadora de la forma TAN COS
SIN.
"""
## Creamos una nueva imagen copiando la original para podes hacer los cambios
variable = imagen_prueba.copy() 
variable[330:440,730:880] = TAN
variable[330:440,1180:1330] = SIN
plt.imshow(variable, cmap='gray')
plt.show()

"""
8. Tomando como base la imagen original img_calculadora.tif, recortar la tecla
ENTER y pegarla en el lugar de la tecla SIN (tener en cuenta que ambas teclas
tienen diferentes tamaños).

"""
## Creamos denuevo la imagen para que no haya colisiones
imagen_nueva = img.copy()

##Sacamos el lugar en el que esta el 'enter' de forma manual y la visualizamos
enter = imagen_nueva[540:660,60:430]
plt.imshow(enter, cmap='gray')
plt.show()

##Vemos las dimensiones del 'enter' y del 'SIN'
enter.shape##(120,370)
SIN1 = imagen_nueva[330:440,730:880]
SIN1.shape##(110,150)

##Creamos la variable para pasar el tamañp del enter al de sin y visualizamos
enter_sin = cv2.resize(enter,(150,110))
enter_sin.shape
plt.figure(), plt.imshow(enter_sin, cmap='gray'), plt.show(block=False)
##Reeplazamos la region del sin con el enter re dimensionado y visualizamos
imagen_nueva[330:440,730:880] = enter_sin
plt.imshow(imagen_nueva, cmap='gray')
plt.show()

"""
9. Recortar las teclas 4, 5, 6, 7, 8 y 9 de la calculadora y pintar sus etiquetas numéricas
de gris (valor = 170). Luego, pegar el recorte pintado en la imagen original.
"""
##Por cada numero de los requeridos en el punto 9 buscamos las 'x' e 'y' de forma manual para despues transformalas
imagen_final_antes = img.copy()
imagen_final_despues = imagen_final_antes.copy()

##Guardamos en una variable con su nombre con su respectivo valor en la matriz conseguido de forma manual
cuatro= imagen_final_despues[1000:1110,310:500]
cinco = imagen_final_despues[1000:1110,580:780]
seis = imagen_final_despues[1000:1110,860:1050]
siete = imagen_final_despues[770:890,310:510]
ocho = imagen_final_despues[770:890,580:780]
nueve = imagen_final_despues[770:890,860:1050]

##Pintamos sus etiquetas numericas en un valor 170, seleccionamos un valor superior a 90 para modificar unicamente
## los colores claros de la parte del boton de los numeros
cuatro[cuatro>90]=170
cinco[cinco>90]=170
seis[seis>90]=170
siete[siete>90]=170
ocho[ocho>90]=170
nueve[nueve>90]=170

##Graficamos la calculadora antes y despues de ser modificada
plt.subplot(221)
h = plt.imshow(imagen_final_antes,cmap='gray')
plt.colorbar(h)
plt.title('imagen_antes')
plt.subplot(222)
h = plt.imshow(imagen_final_despues,cmap='gray')
plt.colorbar(h)
plt.title('imagen_despues')
plt.show()
