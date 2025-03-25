
from MagiaNumerica import MagiaNumerica 
class Lanzador:
    @staticmethod
    def ejecutar():
        numeros = [10, 15, 20, 10, 25, 30, 35, 40]
        magia = MagiaNumerica(numeros)
        lista_transformada = magia.realizar_magia()
        print("Lista transformada:", lista_transformada)
        es_valida = magia.verificar_suma(lista_transformada)
        print("¿La suma es válida?", es_valida)
