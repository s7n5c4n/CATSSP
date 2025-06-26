import numpy as np

def cargar_instancia_catspp_penalizacion(path_archivo, penalizacion):
    matriz = []
    leyendo_matriz = False
    dimension = None

    with open(path_archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea.startswith("DIMENSION"):
                dimension = int(linea.split()[-1])
            if linea == "EDGE_WEIGHT_SECTION":
                leyendo_matriz = True
                continue
            if linea == "EOF":
                break
            if leyendo_matriz:
                fila = [float(x) for x in linea.split()]
                matriz.append(fila)

    matriz = np.array(matriz)

    if dimension is not None and matriz.shape[0] > dimension:
        matriz = matriz[:dimension, :dimension]

    matriz[matriz == -1] = penalizacion

    return matriz

def cargar_tour(path_archivo):
    secuencia = []
    bks = None
    leyendo_secuencia = False

    with open(path_archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if "Length =" in linea:
                bks = float(linea.split('=')[1].strip())
            if linea == "TOUR_SECTION":
                leyendo_secuencia = True
                continue
            if linea == "-1" or linea == "EOF":
                break
            if leyendo_secuencia:
                nodo = int(linea) - 1  # Ajuste de índices
                secuencia.append(nodo)

    return secuencia, bks

# Cálculo de costo
def calcular_costo(matriz_costos, secuencia):
    costo = 0
    for i in range(len(secuencia) - 1):
        costo += matriz_costos[secuencia[i], secuencia[i + 1]]
    return costo

# Búsqueda del valor de penalización correcto
def buscar_penalizacion(path_tsp, path_tour, lista_valores):
    secuencia, bks = cargar_tour(path_tour)

    for penalizacion in lista_valores:
        matriz = cargar_instancia_catspp_penalizacion(path_tsp, penalizacion)
        costo = calcular_costo(matriz, secuencia)

        print(f"Probando penalización = {penalizacion:.0f} | Costo calculado = {costo} | BKS = {bks}")

        if abs(costo - bks) < 1e-6:
            print(f"Penalización correcta encontrada: {penalizacion}")
            break
    else:
        print("No se encontró un valor que coincida exactamente.")

path_tsp = "data/CGL/cgl_17.tsp"
path_tour = "data/TOURS/CGL/cgl_17.4422.tour"

valores_a_probar = [999999, 1000000, 5000000, 9999999, 10000000, 20000000]

buscar_penalizacion(path_tsp, path_tour, valores_a_probar)
