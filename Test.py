from Mundo_PC.DispositivoEntrada import DispositivoEntrada
from Mundo_PC.Monitor import Monitor
from Mundo_PC.Raton import Raton
from Mundo_PC.Teclado import Teclado
from Mundo_PC.computadora import Computadora
from Mundo_PC.orden import Orden

teclado1 = Teclado('HP','USB')
raton1 = Raton('ALienware', 'Bluethoot')
monitor1 = Monitor('HP',15)
computadora1 = Computadora('HP12443',monitor1,teclado1,raton1)

teclado2 = Teclado('Acer','USB')
raton2 = Raton('Hp', 'Bluethoot')
monitor2 = Monitor('Toshiba',30)
computadora2 = Computadora('Gamer',monitor2,teclado2,raton2)

teclado3 = Teclado('Think','USB')
raton3 = Raton('Hp', 'Bluethoot')
monitor3 = Monitor('Think',30)
computadora3 = Computadora('Lenovo',monitor3,teclado3,raton3)

computadoras1 = [computadora1,computadora2]
orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)