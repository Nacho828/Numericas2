class MagiaNumerica:
    def __init__(self, numeros):
        self.numeros = numeros

    def realizar_magia(self):
        # Eliminar duplicados
        lista_sin_duplicados = list(set(self.numeros))
        # Ordenar de mayor a menor
        lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
        # Eliminar números impares
        lista_pares = [num for num in lista_ordenada if num % 2 == 0]
        # Sumar los números restantes
        suma = sum(lista_pares)
        # Colocar la suma como el primer elemento
        lista_final = [suma] + lista_pares
        return lista_final

    def verificar_suma(self, lista):
        if len(lista) > 1:
            return lista[0] == sum(lista[1:])
        return False
