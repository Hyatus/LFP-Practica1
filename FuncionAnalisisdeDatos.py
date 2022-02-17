import matplotlib.pyplot as plt
import numpy as np

def AnalizarData(productos,name,graphic,title,titleX,titleY):
    print("Analizando...")
    
    ejeX = [] 
    ejeY = []
    sumaTotal = 0.0
    porcentajes = []
    for x in range(len(productos)-1):
        ejeX.append(productos[x][0])
        ejeY.append(productos[x][3])
        
    
    #El método que se va a utilizar va a retornar 2 cosas 
    graphic = graphic.lower()
    if graphic == "Generando gráfica de Barras... ":
        fig, ax = plt.subplots()
        ax.bar(ejeX,ejeY)
        ax.set_ylabel(titleY)
        ax.set_xlabel(titleX)
        plt.title(title, 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})
        plt.savefig(name+'.png')
        plt.show()
    elif graphic == "lineas":
        print("Generando gráfico de Líneas... ")
        xpoints = np.array(ejeX)
        ypoints = np.array(ejeY)
        plt.xlabel(titleX)
        plt.ylabel(titleY)
        plt.title(title, 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})
        plt.plot(xpoints, ypoints)
        plt.savefig(name+'.png')
        plt.show()
        
    elif graphic == "pie":       
        print("Generando gráfica de Pie... ") 
        for x in range(len(productos)-1):
            sumaTotal += productos[x][3]
        
        for x in range(len(productos)-1):
            porcentaje = float(productos[x][3]/sumaTotal)*100
            porcentajes.append(round(porcentaje,2))  
       
        plt.pie(porcentajes, labels=ejeX, autopct="%0.1f %%")
        plt.axis("equal")
        plt.title(title, 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})
        plt.savefig(name+'.png')
        plt.show()
        
    
        
        
    
        
        