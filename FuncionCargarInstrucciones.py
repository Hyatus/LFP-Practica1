import easygui

def armarPalabra(lista,i):
  clave = ""
  valor = ""
  lista_aux = []
  cadenaValida = False
  finalCadena = False
  # Obtenemos la clave
  while lista[i] != ":" and i < len(lista):
    lista_aux.append(lista[i])
    i += 1

  clave = clave.join(lista_aux)
  # print("Clave: " + clave)
  lista_aux.clear()
  
  i += 1
  if lista[i] == '"':
      i += 1
      while lista[i] != '"' and i < len(lista):
        lista_aux.append(lista[i])
        i += 1

      valor = valor.join(lista_aux)
      # print("Valor : " + valor)
      lista_aux.clear()

      #print("Valor del índice " + str(i))
      #print("Tamaño de la lista " + str(len(lista)-1))
      
      if i == len(lista)-1:
        print("Cadena inválida debe terminar con los caracteres '?>' ")
        return clave,valor,i,cadenaValida,finalCadena 
      else:  
        i += 1
      
      if lista[i] == ',' and i < len(lista)-3:
        cadenaValida = True
        return clave,valor,i,cadenaValida,finalCadena
      elif lista[i] == '?' and i < len(lista)-1:
        i += 1
        if lista[i] == '>':
          cadenaValida = True
          finalCadena = True
          return clave,valor,i,cadenaValida,finalCadena
      elif lista[i] == '?' and i == len(lista)-1:
          print("Cadena inválida debe terminar con el símbolo '>' ")
          return clave,valor,i,cadenaValida,finalCadena   
      elif lista[i] != '?' and lista[i] != ',' and i < len(lista):
          print("Cadena inválida a una de las instrucciones le hace falta el caracter ',' ")
          return clave,valor,i,cadenaValida,finalCadena   
      else:
          return clave,valor,i,cadenaValida,finalCadena     
  else:
      print('Instrucción inválida valor debe comenzar con el símbolo : " ')

 
def cargarInstrucciones():
  nombre = None
  grafica = None
  titulo = None
  tituloX = None
  tituloY = None
  instruccionesValidas = True
  FinalCadena = False
  
  
  ruta_archivo = easygui.fileopenbox() 
  f = open (ruta_archivo,'r')
  instrucciones = f.read()
  f.close()
  #print(instrucciones)
  lista_instrucciones = instrucciones.strip()
  listaInstrucciones = []
  
  for elemento in lista_instrucciones:
    elemento.strip()
    if elemento != " " and elemento != "\n" and elemento != 'Â':
      listaInstrucciones.append(elemento)

  #print(listaInstrucciones) 
  
  i = 0
  if listaInstrucciones[i] == '<':
    i += 1
    if listaInstrucciones[i] == '¿':
       i += 1
       while instruccionesValidas and i < len(listaInstrucciones) and not FinalCadena:
        clave = ""
        valor = ""
        clave, valor ,i , instruccionesValidas, FinalCadena = armarPalabra(listaInstrucciones,i)
        i += 1 
        clave = clave.lower()
        if clave == "nombre":
            nombre = valor
        elif clave == "grafica":
            grafica = valor
        elif clave == "titulo":
            titulo = valor
        elif clave == "titulox":
            tituloX = valor
        elif clave == "tituloy":
            tituloY = valor

       if not instruccionesValidas:
         print("ERROR: No se pudo cargar instrucciones debido a que son inválidas ")
         nombre = None
         grafica = None
         titulo = None
         tituloX = None
         tituloY = None
         return nombre,grafica,titulo,tituloX,tituloY,instruccionesValidas
       else:
          if nombre != None and grafica != None:
            #print("Nombre: " + nombre)
            #print("Grafica: " + grafica)
            #print("Titulo: " + titulo)
            #print("TituloX: " + tituloX)
            #print("TituloY: " + tituloY)
            return nombre,grafica,titulo,tituloX,tituloY,instruccionesValidas
          elif nombre == None:
              nombre = None
              grafica = None
              titulo = None
              tituloX = None
              tituloY = None
              instruccionesValidas = False
              print("ERROR: Instrucciones inválidas no se proporcionó un nombre para el reporte")
              return nombre,grafica,titulo,tituloX,tituloY,instruccionesValidas
          elif grafica == None:
            nombre = None
            grafica = None
            titulo = None
            tituloX = None
            tituloY = None
            instruccionesValidas = False
            print("ERROR: Instrucciones inválidas no se proporcionó el tipo de gráfica que se desea generar")    
            return nombre,grafica,titulo,tituloX,tituloY,instruccionesValidas    
    else:
         nombre = None
         grafica = None
         titulo = None
         tituloX = None
         tituloY = None    
         instruccionesValidas = False
         print("Intrucciones invalidas falta el caracter  '¿' ")
         return nombre,grafica,titulo,tituloX,tituloY,instruccionesValidas  
  else:
     print("Intrucciones invalidas debe empezar con '<' ")
     instruccionesValidas = False
     nombre = None
     grafica = None
     titulo = None
     tituloX = None
     tituloY = None  
     return nombre,grafica,titulo,tituloX,tituloY,instruccionesValidas
