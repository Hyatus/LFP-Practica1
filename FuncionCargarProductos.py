import easygui

def verificarCadena(lista,indice):
  contadorCorcheteAbierto = 0
  contadorCorcheteCerrado = 0
  contadorComillas = 0
  contadorPuntoComa = 0
  cadenaValida = False
  
  while lista[indice] != ")" and indice < len(lista):
   if lista[indice] == '[':
     contadorCorcheteAbierto +=1
   elif lista[indice] == ']':
     contadorCorcheteCerrado +=1
   elif lista[indice] == '"':
     contadorComillas +=1
   elif lista[indice] == ';':
     contadorPuntoComa +=1    
   indice += 1 

  if contadorCorcheteAbierto == contadorCorcheteCerrado:
      if contadorCorcheteAbierto == contadorPuntoComa:
        if contadorCorcheteAbierto == contadorComillas/2:
          cadenaValida = True
        else:
          print("\nCadena inválida revise que el nombre de cada producto empieze y termine con \"  ")
      else:
        print("\nCadena invalida revise que cada producto termine con ';' ")
  else:
    print("\nCadena invalida revise que los productos abran y cierren con '[' y ']'")


  if cadenaValida:
    return contadorCorcheteAbierto
  else:
    return -1

 # print("\nNúmero de [ : " + str(contadorCorcheteAbierto))
 # print("Número de ] : " + str(contadorCorcheteCerrado))
 # print("Número de “ : " + str(contadorComillas))
 # print("Número de ; :  " + str(contadorPuntoComa))


def agregarProducto(lista,c):
  c += 1
  nombreProducto = ""
  precioUnitario = ""
  cantidadUnidades = ""
  ganancia = 0.0
  elementosProducto = []
  listaAux = []

  #Captura el nombre del producto
  while lista[c] != '"' and c < len(lista):
    listaAux.append(lista[c])
    c += 1

  nombreProducto = nombreProducto.join(listaAux)  
  # print("Nombre del producto: " + nombreProducto)
  listaAux.clear()

  #Captura el precio Unitario
  c += 2
  while lista[c] != ',' and c < len(lista):
    listaAux.append(lista[c])
    c += 1

  precioUnitario = precioUnitario.join(listaAux)
  # print("Precio Unitario : " + precioUnitario)
  listaAux.clear()
  

  #Captura cantidad de Unidades 
  c += 1
  while lista[c] != ']' and c < len(lista):
    listaAux.append(lista[c])
    c += 1 
  
   
  cantidadUnidades = cantidadUnidades.join(listaAux)
  listaAux.clear()
  # print("Cantidad de Unidades : " + cantidadUnidades)

  c +=2 
  ganancia = float(cantidadUnidades) * float(precioUnitario)
  elementosProducto.append(nombreProducto)
  elementosProducto.append(float(precioUnitario))
  elementosProducto.append(int(cantidadUnidades))
  elementosProducto.append(round(ganancia,2))

  return elementosProducto,c


def cargarProductos():

  ruta_archivo = easygui.fileopenbox() 
  f = open (ruta_archivo,'r')
  texto = f.read()
  f.close()
  
  lista = texto.strip()
  lista2 = []
  lista_aux = []
  productosExtraidos = []
  mes = ""
  anio = ""

  #print(lista, end = "")
  for elemento in lista:
    elemento.strip()
    if elemento != " " and elemento != "\n":
      lista2.append(elemento)

  #print(lista2,end=" ")
 
  c = 0
  #Tomamos el nombre del mes
  while lista2[c] != ":" and c < len(lista2):
     lista_aux.append(lista2[c])
     c += 1
  # Unimos el nombre en una sola cadena
  mes = mes.join(lista_aux)
  lista_aux.clear()

  #Tomamos el Año 
  c+=1
  while lista2[c] != "=" and c < len(lista2):
     lista_aux.append(lista2[c])
     c += 1

  c+=1
  anio = anio.join(lista_aux)
  lista_aux.clear()

 # PROCESO PARA INGRESO DE PRODUCTOS
  if lista2[c] == '(' and lista2[-1] == ')':
   c +=1
   numeroProductos = verificarCadena(lista2,c)
  # print("\n ULTIMO CARACTER " +  lista2[c])
  if numeroProductos != -1:
    #c += 1
    for x in range(numeroProductos):
      listadeProductos = []
      listadeProductos,c = agregarProducto(lista2,c+1)
      productosExtraidos.append(listadeProductos)
      # print(listadeProductos)
  else:
    print("\nEntrada de archivo inválida revise que contenga el siguiente caracter : '(' y ')' ")


  #print("MES: " +  mes)
  #print("AÑO: " + anio)
  #print(productosExtraidos)
  return productosExtraidos,mes,anio
