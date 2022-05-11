class Monitor():
    contador_monitores = 0

    def __init__(self,marca,tamaño):
        Monitor.contador_monitores +=1
        self._id_monitores = Monitor.contador_monitores
        self._tamaño = tamaño
        self._marca = marca

    def __str__(self):
        return f'ID: {self._id_monitores}, Marca: {self._marca}, Tamaño: {self._tamaño}'

if __name__ == '__main__':
    monitor1 = Monitor('Alianware', 'Grande')
    print(monitor1)
    monitor2 = Monitor('HP', 'Grande')
    print(monitor2)