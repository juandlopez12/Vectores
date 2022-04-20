

lista_v = [int(elemento) for elemento in input().split()]
lista_u = [int(elemento) for elemento in input().split()]

resultado = 0
posicion = 0
for i in lista_v:
  
  producto= lista_v[posicion] * lista_u[posicion]
  resultado+=producto
  posicion+=1

print(resultado)