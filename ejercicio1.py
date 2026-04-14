import re

def enrutamiento():

    n = int(input())
    rutas = []

    for _ in range(n):
        linea = input().split()
        ruta = linea[0]
        contenido = " ".join(linea[1:])
        rutas.append((ruta, contenido))

    m = int(input())
    transiciones = []

    for _ in range(m):
        transiciones.append(input().strip())

    resultados = []

    for transicion in transiciones:
        partes_transicion = transicion.split("/")
        encontrado = False

        for ruta_path, ruta_contenido in rutas:
            partes_ruta = ruta_path.split("/")

            if len(partes_ruta) != len(partes_transicion):
                continue
                
            parametros = {}
            coincide = True

            for parte_ruta, parte_transicion in zip(partes_ruta, partes_transicion):
                if parte_ruta.startswith(":"):
                    parametros[parte_ruta[1:]] = parte_transicion
                elif parte_ruta != parte_transicion:
                    coincide = False
                    break

            if coincide:
                contenido_limpio = re.sub(r'\s*\([^)]+\)', '', ruta_contenido).strip()

                if parametros:
                    contenido_limpio += " " + " ".join(parametros.values())
                
                resultados.append(contenido_limpio)
                encontrado = True
                break

        if not encontrado:
            resultados.append("404 Not Found")

    for resultado in resultados:
        print(resultado)

enrutamiento()
