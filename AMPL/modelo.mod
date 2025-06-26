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

# Restricciones de flujo (solo para TSP clásico - comentadas para CATSPP-BC)
# subject to OneSuccessor {i in NODES}:
#     sum {j in NODES: j != i} x[i,j] = 1;

# subject to OnePredecessor {j in NODES}:
#     sum {i in NODES: i != j} x[i,j] = 1;

# Eliminación de subtours para caminos (MTZ modificado)
subject to MTZ {i in NODES, j in NODES: i != j and j != start_node}:
    u[i] - u[j] + n * x[i,j] <= n - 1;

# Fijar valores de u para nodos especiales
subject to StartNodeOrder:
    u[start_node] = 1;

subject to EndNodeOrder:
    u[end_node] = n;

# Transiciones prohibidas
subject to NoArcs {i in NODES, j in NODES}:
    if (i,j) in PROHIBITED then x[i,j] = 0;

# Restricciones para CATSPP-BC (Camino desde start_node hasta end_node)
# El nodo inicial tiene exactamente un sucesor y ningún predecesor
subject to StartConstraint:
    sum {j in NODES: j != start_node} x[start_node,j] = 1;

subject to StartNoPredecessor:
    sum {i in NODES: i != start_node} x[i,start_node] = 0;

# El nodo final tiene exactamente un predecesor y ningún sucesor  
subject to EndConstraint:
    sum {i in NODES: i != end_node} x[i,end_node] = 1;

subject to EndNoSuccessor:
    sum {j in NODES: j != end_node} x[end_node,j] = 0;

# Para nodos intermedios, conservación de flujo (un predecesor y un sucesor)
subject to IntermediateNodes {k in NODES: k != start_node and k != end_node}:
    sum {i in NODES: i != k} x[i,k] = 1;

subject to IntermediateNodesOut {k in NODES: k != start_node and k != end_node}:
    sum {j in NODES: j != k} x[k,j] = 1;
