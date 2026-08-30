# Definición del tamaño de la matriz
numero_filas = 3
numero_columnas = 3

def imprimir_matriz(matriz):
    print("\nLos valores finales de la matriz son:")
    for fila in matriz:
        for valor in fila:
            print(valor, end=" ")
        print()  # salto de línea al terminar cada fila

def capturar_valores(matriz):
    for f in range(numero_filas):
        for c in range(numero_columnas):
            matriz[f][c] = int(input(f"Ingrese el valor de la posición [{f}][{c}]: "))

def main():
    matriz = [[0] * numero_columnas for _ in range(numero_filas)]
    print("Actividad 04 - Matriz Bidimensional en Python (MxN)")
    capturar_valores(matriz)
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()

