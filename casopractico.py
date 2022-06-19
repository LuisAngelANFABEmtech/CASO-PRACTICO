from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

Usuarios=["emtech"]
Contraseñas=["caso1"]

while True:
  Usuario_entrada= input("ingrese su nombre de usuario: ")
  Contraseña_entrada=input("Ingrese su contraseña: ")
  
  if Usuario_entrada in Usuarios and Contraseña_entrada in Contraseñas:
    Access = True
    break
  else:
    print("Datos erroneos. Intenta nuevamente")
else: 
  print("Datos erroneos. Intenta nuevamente")
    
if Access:
  pass
  print("Acceso concedido. Bienvenido al analisis de productos")

#
#
#Analisis de productos más vendidos
contador = 0
total_ventas_productos = []
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador += 1
  formato = [producto[0], contador]
  total_ventas_productos.append(formato)
  contador = 0

  #ordenar productos por mayor cantidad de ventas 
  productos_más_vendidos = []
while total_ventas_productos:
  maximo = total_ventas_productos[0][1]
  lista_actual = total_ventas_productos[0]
  for venta_producto in total_ventas_productos:
    if venta_producto[1] > maximo:
      maximo = venta_producto[1]
      lista_actual = venta_producto
      
  productos_más_vendidos.append(lista_actual)
  total_ventas_productos.remove(lista_actual)

print(f'Estos son los cinco productos con mayores ventas: ', productos_más_vendidos[0:5])

#
#
#Analisis de busquedas de productos.
producto_busqueda=[]
contadorb=0
for producto in lifestore_products:
  for busqueda in lifestore_searches:
    if producto[0]==busqueda[1]:
      contadorb += 1
  formatob=[producto[0],contadorb]
  producto_busqueda.append(formatob)
  contadorb=0

#sesgo 10 principales.
lista_busquedas=[]
while producto_busqueda:
  maximob = producto_busqueda[0][1]
  lista_actualb = producto_busqueda[0]
  for orden_busqueda in producto_busqueda:
    if orden_busqueda[1] > maximob:
      maximob = orden_busqueda[1]
      lista_actualb = orden_busqueda

  lista_busquedas.append(lista_actualb)
  producto_busqueda.remove(lista_actualb)

print(f'Estos son los Diez productos con mayores busquedas: ', lista_busquedas[0:10])
      
#
#
#menores_ventas
contador = 0
total_ventas_productos = []
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador += 1
  formato = [producto[0], contador]
  total_ventas_productos.append(formato)
  contador = 0
  
#ordenar productos por menor cantidad de ventas 
productos_menos_ventas = []
while total_ventas_productos:
  minimo = total_ventas_productos[0][1]
  lista_actual = total_ventas_productos[0]
  for venta_producto in total_ventas_productos:
    if venta_producto[1] < minimo:
      minimo = venta_producto[1]
      lista_actual = venta_producto
      
  productos_menos_ventas.append(lista_actual)
  total_ventas_productos.remove(lista_actual)

print(f'Estos son los cinco productos con menores ventas: ', productos_menos_ventas[0:5])

#Menor cantidad de busquedas
producto_busqueda=[]
contadorb=0
for producto in lifestore_products:
  for busqueda in lifestore_searches:
    if producto[0]==busqueda[1]:
      contadorb += 1
  formatob=[producto[0],contadorb]
  producto_busqueda.append(formatob)
  contadorb=0

#filtro 10 menores.
lista_busquedas=[]
while producto_busqueda:
  minimo = producto_busqueda[0][1]
  lista_actualb = producto_busqueda[0]
  for orden_busqueda in producto_busqueda:
    if orden_busqueda[1] < minimo:
      minimo = orden_busqueda[1]
      lista_actualb = orden_busqueda

  lista_busquedas.append(lista_actualb)
  producto_busqueda.remove(lista_actualb)

print(f'Estos son los Diez productos con menor busqueda: ', lista_busquedas[0:10])     
      
  


      
      
      
  
    
  


  