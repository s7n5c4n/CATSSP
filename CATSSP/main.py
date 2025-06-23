import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Simulación de matriz de costos (reemplazar por lectura de .catsp real)
# -1 indica transición prohibida
C = np.array([
    [-1, 300, 200, 654],
    [305, -1, 963, 117],
    [952, 493, -1, 704],
    [678, 123, 951, -1]
])

n = C.shape[0]
nodos = list(range(n))

solucion = []
actual = 0
visitados = {actual}
solucion.append(actual)

while len(visitados) < n:
    costos_permitidos = [(j, C[actual, j]) for j in nodos if j not in visitados and C[actual, j] != -1]
    if not costos_permitidos:
        break
    siguiente = min(costos_permitidos, key=lambda x: x[1])[0]
    solucion.append(siguiente)
    visitados.add(siguiente)
    actual = siguiente

costo_total = 0
for i in range(len(solucion) - 1):
    costo_total += C[solucion[i], solucion[i+1]]

plt.figure(figsize=(6, 6))
puntos = np.random.rand(n, 2)
for i in range(n):
    plt.scatter(puntos[i, 0], puntos[i, 1], c='blue')
    plt.text(puntos[i, 0]+0.01, puntos[i, 1]+0.01, str(i), fontsize=12)
for i in range(len(solucion) - 1):
    plt.plot([puntos[solucion[i], 0], puntos[solucion[i+1], 0]],
             [puntos[solucion[i], 1], puntos[solucion[i+1], 1]], 'r-')
plt.title(f'Recorrido heurístico - Costo total: {costo_total}')
plt.show()

# Mostrar secuencia y costo
df_resultado = pd.DataFrame({'Posición': range(len(solucion)), 'Nodo': solucion})
print(df_resultado)
print(f"Costo total de la solución heurística: {costo_total}")
