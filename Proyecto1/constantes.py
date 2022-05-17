
#Características de la ventana
width = 600
height = 800
size = (width, height)
background = (91,203,60)
black = (0, 0, 0)
red = (255,0,0)

#Tamaño de los objetos
road = int(width/1.6) #Definimos el tamaño que tendrá el road/carretera sobre la que se desplazan los autos.
y_line = int(width/80) #Definimos el tamaño de la línea amarilla que divide los carriles
carril_derecho = width/2 + road/4 #Ubicación derecha
carril_izquierdo = width/2 - road/4 #Ubicación izquierda

#Velocida de movimiento del auto enemigo
velocidad_enemigo = 1


#Posición del auto
auto_carril_izquierdo = (carril_izquierdo, height*0.2)
auto_carril_derecho = (carril_derecho, height*0.2)
