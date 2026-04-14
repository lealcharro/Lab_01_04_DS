from collections import defaultdict

def cliente_mas_fiel():
    #N:# socios, M:# terminales, S:# transacciones  
    N, M, S = map(int, input().split())

    #Mapear cada terminal a su socio
    terminal_a_socio = {}
    socios = set()
    for _ in range(M):
        socio, terminal = map(int, input().split())
        terminal_a_socio[terminal] = socio
        socios.add(socio)

    #Contar transacciones usando defaultdict
    compras = defaultdict(lambda: defaultdict(int))
    for _ in range(S):
        #p:cliente, t:terminal 
        p, t = map(int, input().split())
        
        #Sólo procesamos si el terminal le pertenece a un socio
        if t in terminal_a_socio:
            socio = terminal_a_socio[t]
            compras[socio][p] += 1

    #Determinar el cliente más fiel por socio
    tabla_socio_cliente_fiel = {}
    for socio in socios:
        clientes_del_socio = compras[socio]
        
        #Si el socio no tuvo transacciones, le asignamos -1
        if not clientes_del_socio:
            tabla_socio_cliente_fiel[socio] = -1
            continue
            
        #Sino encontramos al cliente con más compras.
        #En caso de empate, el de menor ID de clientes usando un negativo en la tupla
        mejor_cliente = max(
            clientes_del_socio.keys(), 
            key=lambda c: (clientes_del_socio[c], -c)
        )
        
        tabla_socio_cliente_fiel[socio] = mejor_cliente

    for (socio, cliente_fiel) in tabla_socio_cliente_fiel.items():
        print(socio, cliente_fiel)

cliente_mas_fiel()