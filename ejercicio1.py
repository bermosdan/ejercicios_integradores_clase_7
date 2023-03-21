def maximo_comun_divisor(numero_1, numero_2):
    auxiliar=0
    while numero_2 != 0:
        auxiliar = numero_2
        numero_2 = numero_1 % numero_2
        numero_1 = auxiliar
    return numero_1

print("Maximo común divisor")
numero_1 = input("Ingrese primer valor: ")
numero_2 = input("Ingrese segundo valor: ")
mcd = maximo_comun_divisor(int(numero_1), int(numero_2))
print(f"El máximo común divisor de {numero_1} y {numero_2} es {mcd}")