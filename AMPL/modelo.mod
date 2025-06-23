# Definición de conjuntos y parámetros
set NODES;
set PROHIBITED within {NODES, NODES};

param C {NODES, NODES};
param n := card(NODES);

# Parámetros opcionales para CATSPP-BC (inicio y fin fijos)
param start_node symbolic;
param end_node symbolic;

# Variables de decisión
var x {i in NODES, j in NODES} binary;
var u {i in NODES} >= 1, <= n;

# Función objetivo
minimize TotalCost:
    sum {i in NODES, j in NODES} C[i,j] * x[i,j];

# Restricciones de flujo
subject to OneSuccessor {i in NODES}:
    sum {j in NODES: j != i} x[i,j] = 1;

subject to OnePredecessor {j in NODES}:
    sum {i in NODES: i != j} x[i,j] = 1;

# Eliminación de subtours (MTZ)
subject to MTZ {i in NODES, j in NODES: i != j}:
    u[i] - u[j] + n * x[i,j] <= n - 1;

# Transiciones prohibidas
subject to NoArcs {i in NODES, j in NODES}:
    if (i,j) in PROHIBITED then x[i,j] = 0;

# Restricciones de inicio y fin (solo si corresponde CATSPP-BC)
subject to StartConstraint:
    sum {j in NODES: j != start_node} x[start_node,j] = 1;

subject to EndConstraint:
    sum {i in NODES: i != end_node} x[i,end_node] = 1;
