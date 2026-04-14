# Lab_01_04_DS
Resolución de Laboratorio Semana 2
Apellidos y Nombres: Chacón Roque Leonardo Alexander

## Problema 1

Diseñamos una función enrutamiento que realice las dos fases de análisis de la entrada:
La primera parte, guardar el dígito n que es el número de rutas, luego lee cada línea insertada en el terminal, la separan por espacios y dos variables: ruta (primer elemento de la línea) y el contenido (resto de elementos unidos por espacios), se agregan como tupla en la lista rutas.

    def enrutamiento():    
        n = int(input())
        rutas = []
        
        for _ in range(n):
            linea = input().split()
            ruta = linea[0]
            contenido = " ".join(linea[1:])
            rutas.append((ruta, contenido))

La segunda parte, guarda el dígito m que es el número de transiciones, leemos cada línea y la separamos por espacios, guardando estos elementos en una lista como un elemento de transiciones. Para cada transicion de transiciones, la separamos por el carácter slash y guardamos la lista en partes_transicion, suponemos que no hemos encontrado la dirección. 
    
        m = int(input())
        transiciones = []
        
        for _ in range(m):
            transiciones.append(input().strip())
    
        resultados = []
        
        for transicion in transiciones:
            partes_transicion = transicion.split("/")
            encontrado = False
        
Luego, para cada tupla (ruta , contenido) dentro de las tuplas de rutas, separamos la ruta por un slash en sus partes y verificamos si la cantidad de estas partes son iguales a la cantidad de elementos de partes_transicion, en el caso que no ocurra esto, continuamos a la siguiente tupla de las rutas
    
    for ruta_path, ruta_contenido in rutas:
        partes_ruta = ruta_path.split("/")

        if len(partes_ruta) != len(partes_transicion):
            continue
           
        parametros = {}
        coincide = True
        
En el caso que tengan la misma cantidad de elementos, partimos de que cada elemento de la ruta coincide con la transicion, por lo que para cada par de una parte de la ruta y la parte de una transición, verificamos si cada parte de la ruta comienza con el carácter dos puntos, en este caso guardamos la esta parte de la transición asociada a los parametros de los siguientes elementos de la parte de la ruta, sino verificamos si la parte de la ruta es la misma a la parte de la transición, en el caso de que no coincidan, cambiamos la variable coincide a falso y terminamos el bucle for.

        for parte_ruta, parte_transicion in zip(partes_ruta, partes_transicion):
            if parte_ruta.startswith(":"):
                parametros[parte_ruta[1:]] = parte_transicion
            elif parte_ruta != parte_transicion:
                coincide = False
                break
En el caso que coincidan,  eliminamos tanto los paréntesis como los elementos dentro de estos de la ruta del contenido, los separamos por sus espacios y en el caso de que tenga algún parámetro, agregamos estos valores de los parámetros separados por espacio. Finalmente, agregamos en resultados el contenido limpiado, cambiamos como verdadero a la variable encontrado y salimos del bucle for.

        if coincide:
            contenido_limpio = re.sub(r'\s*\([^)]+\)', '', ruta_contenido).strip()

            if parametros:
                contenido_limpio += " " + " ".join(parametros.values())
           
            resultados.append(contenido_limpio)
            encontrado = True
            break
En el caso que no se haya encontrado en esta combinatoria entre rutas y transiciones, agregamos que “404 Not Found” que significa que no encontramos la ruta.

    if not encontrado:
        resultados.append("404 Not Found")
Finalmente, escribimos el contenido de las rutas encontradas en el termina

    for resultado in resultados:
        print(resultado)
        
Pantalla de Salida

<img width="512" height="485" alt="image" src="https://github.com/user-attachments/assets/0c856c8b-0be1-44b8-b2eb-60af9350acad" />


## Problema 2

Usamos la biblioteca collections, de la que usamos defaultdict, que es un diccionario especializado que soluciona el problema de KeyError cuando quiere asignar al diccionario una llave inexistente.
from collections import defaultdict
Primero leemos y almacenamos el número de socios, número de terminales y número de transacciones y mapeamos cada terminal al socio correspondiente en un diccionario, y para que no se repitan los socios en un conjunto set().

    def cliente_mas_fiel():
        #N:# socios, M:# terminales, S:# transacciones  
        N, M, S = map(int, input().split())
    
    
        terminal_a_socio = {}
        socios = set()
        for _ in range(M):
            socio, terminal = map(int, input().split())
            terminal_a_socio[terminal] = socio
            socios.add(socio)
Después, usamos un diccionario especializado defaultdict compras que crea un diccionario anidado automático, se inicializan las claves faltantes como nuevos diccionarios vacíos y los valores de los valores como int(0). Luego mapea cada par cliente-terminal si el terminar le pertenece a un socio, y sumamos la compra un dígito.

        compras = defaultdict(lambda: defaultdict(int))
        for _ in range(S):
            p, t = map(int, input().split())
           
            if t in terminal_a_socio:
                socio = terminal_a_socio[t]
                compras[socio][p] += 1
A continuación buscamos el cliente más fiel para cada socio en un diccionario tabla_socio_cliente_fiel mediante dos opciones: Si el socio no tuvo transacciones, le asignamos -1, sino encontramos el cliente con más compras, y si existe empate ordenamos una tupla de valores negativos de los IDs de los clientes y buscamos el mayor, el cual sería el de menor valor de ID; Finalmente, almacenamos en el diccionario.

        tabla_socio_cliente_fiel = {}
        for socio in socios:
            clientes_del_socio = compras[socio]
           
            if not clientes_del_socio:
                tabla_socio_cliente_fiel[socio] = -1
                continue
               
            mejor_cliente = max(
                clientes_del_socio.keys(),
                key=lambda c: (clientes_del_socio[c], -c)
            )
           
            tabla_socio_cliente_fiel[socio] = mejor_cliente
Finalmente, mostramos el diccionario de la manera indicada en el ejemplo.

        for (socio, cliente_fiel) in tabla_socio_cliente_fiel.items():
            print(socio, cliente_fiel)
            
    cliente_mas_fiel()

Pantalla de Salida

<img width="324" height="537" alt="image" src="https://github.com/user-attachments/assets/b5703f97-9429-4fee-98a8-d71d1bddd408" />

