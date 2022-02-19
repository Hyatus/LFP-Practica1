from FuncionCargarInstrucciones import *
from FuncionCargarProductos import *
from FuncionAnalisisdeDatos import *
from FuncionReportes import *
#Sintáctico utilizando pila 

def menuPrincipal():
    #Variables para la carga de Productos
    productExtraidos = []
    month = None
    year = None
    
    # Variables para la carga de Instrucciones 
    name = None
    graphic = None
    title = None
    titleX = None
    titleY = None
    validInstructions = False
    
    #Variables para el menú 
    cargaDeDatos = False
    cargaDeInstrucciones = False
    opcion = 0
    while(opcion != 5):
        print("\n███████ MENÚ PRINCIPAL ██████████")
        print("█OPCIONES:                      █")
        print("█1. Cargar Data                 █")
        print("█2. Cargar Instrucciones        █")
        print("█3. Analizar datos              █")
        print("█4. Generar Reportes            █")
        print("█5. Salir                       █")
        print("█████████████████████████████████")
        print(" ")
        opcion = int(input("Ingrese una de las opciones: "))
        print(" ")
        if opcion == 1:
           productExtraidos,month,year = cargarProductos()
           if len(productExtraidos) != 0 and month != None and year != None:
               print("DATOS CARGADOS CON ÉXITO! ")
               cargaDeDatos = True
           else:
               cargaDeDatos = False
               print("FALLÓ AL INTENTAR CARGAR DATOS! ")   
        elif opcion == 2:
             name,graphic,title,titleX,titleY,validInstructions = cargarInstrucciones()
             if validInstructions:
                cargaDeInstrucciones = True 
                print("CARGA DE INSTRUCCIONES REALIZADA CON ÉXITO! ")
             else:
                cargaDeInstrucciones = False
                print("FALLÓ LA CARGA DE INSTRUCCIONES")
        elif opcion == 3:
            if cargaDeDatos and cargaDeInstrucciones:
                print("Análisis de Datos")
                AnalizarData(productExtraidos,name,graphic,title,titleX,titleY)
            elif not cargaDeDatos:
                print("Debe cargar los datos primero para realizar el análisis")
            elif not cargaDeInstrucciones:
                print("Debe ingresar primero las instrucciones para realizar el análisis ")    
        elif opcion == 4:
            if cargaDeDatos and cargaDeInstrucciones:
                print("Generando Reporte...")
                generarReporte(productExtraidos)
            elif not cargaDeDatos:
                print("Debe cargar los datos primero para realizar el reporte")
            elif not cargaDeInstrucciones:
                print("Debe ingresar primero las instrucciones para realizar el reporte ")    
        elif opcion == 5: 
            print("Saliendo...")
        else:
            print("Ingrese una opción valida! ")
    
    print("HA SALIDO DE LA EJECUCIÓN DEL PROGRAMA CON ÉXITO ")




menuPrincipal()


