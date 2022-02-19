import os

def generarReporte(productos):
    
    encabezado = '''
        <!DOCTYPE html>
        <html>
        <head>
	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	    <title>Reporte de Ventas</title>
        <link rel="stylesheet" type="text/css" href="estilo.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@500&family=Roboto:wght@700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body>
        <h1>Reporte Ventas generadas </h1>
        <h3>Nombre: Cristian Alexander Mejia Cahuec Carnet: 201807085</h3><br>
        <br>
        <br>
        <br>
        '''
    
    tabla = '''
            <table class="table table-hover">
            <thead>
            <tr>
            <th scope="col">#</th>
            <th scope="col">Producto</th>
            <th scope="col">Precio Unitario</th>
            <th scope="col">Unidades Vendidas</th>
            <th scope="col">Ganancias generadas</th>
            </tr>
            </thead>
            <tbody>
            '''
             
    final = ''' 
           </body>
           </html> 
            '''
    
    file = open('reporte.html',"w")
    file.write(encabezado)
    file.write(tabla)
    
    #Ordenar productos 
    productos.sort(key=tomarGanancia,reverse=True)
    
    for x in range(len(productos)):
        fila = f'''
                   <tr>
                   <th scope="row">{x}</th>
                   <td>{productos[x][0]}</td>
                   <td>{productos[x][1]}</td>
                   <td>{productos[x][2]}</td>
                   <td>Q.{productos[x][3]}</td>
                   </tr>
               '''
        file.write(fila)       
    
    finalTabla = '''
                    </tbody>
                    </table>
                 '''
                 
    masVendido = f"<h3>Producto mas vendido: {productos[0][0]}<h3>"
    ultimoprod = productos[-1][0]
    menosVendido = f"<h3>Producto menos vendido: {ultimoprod}<h3>"
                
    file.write(finalTabla)      
    file.write(masVendido)    
    file.write(menosVendido)   
    file.write(final)
    file.close()


def tomarGanancia(elemento):
    return elemento[3]    