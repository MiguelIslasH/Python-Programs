#Sistema 2x2
#a11X a12Y = b1
#a21X a22Y = b2

#definimos 2 funciones para encontrar el numero mayor entre los primeros coeficientes del sistema

def maximo(num1,num2):
	if(abs(num1)>abs(num2)):
		return num1
	else:
		return num2
def minimo(num1,num2):
	if(abs(num1)<abs(num2)):
		return num1
	else:
		return num2
#Creamos dos listas una donde almacenaremos nuestros coeficientes
#La otra la usaremos para acomodarlos y hacer mas fácil el trabajo
a=[]
aux=[]

#Agregamos a nuestra primera lista los coeficientes dados por el usuario
a.append(int(input("Introduce el primer coeficiente ")))
a.append(int(input("Introduce el segundo coeficiente ")))
a.append(int(input("Introduce el termino independiente ")))

a.append(int(input("Introduce el primer coeficiente ")))
a.append(int(input("Introduce el segundo coeficiente ")))
a.append(int(input("Introduce el termino independiente ")))

#Obtenemos el mayor y el menor sin tomar el signo para hacer una división
#Es por eso que en nuestras funciones tenemos la función abs()
#La cual nos regresa el valor absoluto de un numero

mayor = maximo(a[0],a[3])
menor = minimo(a[0],a[3])


#cambiar las listas
#Con esto acomodamos las listas
#Para tener el coeficiente menor siempre en a[0]

if (abs(a[0])>abs(a[3])):
	aux.extend([a[3],a[4],a[5]])
	a[3]=a[0]
	a[4]=a[1]
	a[5]=a[2]

	a[0]=aux[0]
	a[1]=aux[1]
	a[2]=aux[2]

#Con este multiplo sabremos como hacer la multiplicacion de la fila 1
#Con el signo negativo para que se cancele con la fila 2 y obtener el 0
multiplo = -(mayor/menor)

#multiplo*F1 + F2 -> F2

a[3] = a[0]*multiplo + a[3]
a[4]= a[1]*multiplo + a[4]
a[5] = a[2]*multiplo + a[5]

#condiciones para saber sobre las soluciones

#Esta primer condición nos determina que hay una unica solución

if(a[4]!=0):
	y = a[5]/a[4]
	x = (a[2]-a[1]*y)/a[0]
	print("\n\nUnica solución")
	print("y =",y)
	print("x =",x)

#Una segunda condición para saber si nuestro sistema no tiene solución
elif (a[4]==0 and a[5]!=0):
	print("No tiene solución")
  
#Si tenemos que en a[4] y en a[5] hay ceros significa una infinidad de soluciones

elif(a[4]==0 and a[5]==0):
	print("Tiene infinidad de soluciones: ")
#Aqui imprimimos una representación de la ecuación despejando X
if(a[0]>0):
	print("x = (",a[2],"",-a[1],"y)/",a[0])
else:
	print("x = (",-a[2],"",a[1],"y)/",-a[0])
