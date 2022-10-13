#Estructura de datos#

#LISTAS#

#APPEND#
'''list.append(x)
Agrega un ítem al final de la lista.'''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
fruits.append("grape")
print(fruits)
'''


#EXTEND#
'''list.extend(iterable)
Extiende la lista agregándole todos los ítems del iterable.'''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
cars = ["Nissan", "BMW", "Audi"]
fruits.extend(cars)
print(fruits)
'''


#INSERT#
'''list.insert(i, x)
Inserta un ítem en una posición dada.
'''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
fruits.insert(1,"apple")
print(fruits)
'''


#REMOVE#
'''list.remove(x)
Quita el primer ítem de la lista cuyo valor sea x. '''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
fruits.remove("orange")
print(fruits)
'''


#POP#
'''list.pop([i])
Quita el ítem en la posición dada de la lista y lo retorna.'''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
fruits.pop(1)
print(fruits)
'''


#CLEAR#
'''list.clear()
Elimina todos los elementos de la lista.'''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
fruits.clear()
print(fruits)
'''


#INDEX#
'''list.index(x[, start[, end]])
Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. '''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
x = fruits.index("orange")
print(x)
'''


#COUNT#
'''list.count(x)
Retorna el número de veces que x aparece en la lista.'''
#ejemplo#
'''
fruits = ["orange", "peach", "lime"]
x = fruits.count("peach")
print(x)
'''


#SORT#
'''list.sort()
Ordena los elementos de la lista in situ.'''
#ejemplo#
'''
cars = ["Nissan", "BMW", "Audi"]
cars.sort()
print(cars)
'''


#REVERSE#
'''list.reverse()
Invierte los elementos de la lista in situ.'''
#ejemplo#
'''
cars = ["Nissan", "BMW", "Audi"]
cars.reverse()
print(cars)
'''


#COPY#
'''list.copy()
Retorna una copia superficial de la lista.'''
#ejemplo#
'''
cars = ["Nissan", "BMW", "Audi"]
mylist = cars.copy()
print(mylist)
'''


#USANDO LISTAS COMO TUPLAS#
'''
stack = [1,2,3]
stack.append(4)
stack.append(5)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)
'''


#USANDO LISTAS COMO TUPLAS#
'''
from collections import deque
queue = deque(["Brayan", "Stiven", "Oviedo", "Cadleron"])
queue.append("Raul")
queue.append("Gomez")
queue.popleft()
queue.popleft()
print(queue)
'''


#COMPRENSION DE LISTAS#
'''
squares = []
for x in range(8):
  squares.append(x**2)
print(squares)
'''
#squares = list(map(lambda x: x**2, range(8)))

#squares = [x**2 for x in range(8)]
'''
combs = []
for x in [1,2,3]:
  for y in [3,2,1]:
    if x != y:
      combs.append((x,y))
print(combs)
'''

#LISTAS POR COMPRENSION ANIDADAS#
'''
matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
]
print(matrix)

[[row[i]for row in matrix] for i in range(4)]

comp = []
for i in range(4):
  comp_row = []
  for row in matrix:
    comp_row.append(row[i])
  comp.append(comp_row)
print(comp)

list(zip(*matrix))
'''

#INSTRUCTIVO DEL#
'''
v_del = [-1, 1, 66.25, 333, 333, 1234.5]
del v_del[0]
print(v_del)

del v_del[2:4]
print(v_del)

del v_del[:]
print(v_del)
'''


#TUPLAS#

'''
portero = ("guantes", "guayos", "balon","guantes","balon")
print(len(portero))
'''
'''
datos = ("abc", 34, True, 40, "male")
print(datos)
'''
'''
portero = ("guantes", "guayos", "balon","guantes","balon")
print(type(portero))
'''

#CONJUNTOS#
'''
computador = {'teclado', 'mouse', 'pantalla', 'cpu', 'parlantes', 'mouse', 'teclado', 'cpu', 'parlantes'}
print(computador)
'''
'''
x = set('guanabana')
y = set('guayaba')
print(x)
print(y)

print(x - y)

print(x | y)

print(x & y)

print(x ^ y)

x = {x for x in 'guanabana' if x not in 'abc'}
print(x)
'''

#DICCIONARIO#
'''
per = {'brayan': 2004, 'edad': 17}
per['año_actual'] = 2022
print(per)

del per['edad']
per['años_vida'] = 18
print(per)

list(per)

sorted(per)

'año_actual' in per

'brayan' not in per
'''
'''
per = dict([('edad', 17), ('año_actual', 2022), ('brayan', 2004)])
print(per)
'''
'''
num = {x: x**2 for x in (2,4, 6)}
print(num)
'''
'''
num = dict(brayn=2004, edad=17, año_actual=2022)
print(num)
'''

#ITERACIONES#
'''
num = {'brayan': 'the pure', 'robin': 'the brave'}
for x, y in num.items():
  print(x, y)
'''
'''
for x, y in enumerate(['one', 'two', 'three']):
  print(x, y)
'''

preguntas = ['name', 'quest', 'favorite color']
respuestas = ['brayan', 'boulevard', 'black']
for x, y in zip(preguntas,respuestas):
  print('what is your {0}? It is {1}.'.format(x, y))