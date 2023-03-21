def maximo_comun_divisor(numero_1, numero_2):
    auxiliar=0
    while numero_2 != 0:
        auxiliar = numero_2
        numero_2 = numero_1 % numero_2
        numero_1 = auxiliar
    return numero_1

def minimo_comun_multiplo(numero_1, numero_2):
    return (numero_1 * numero_2)/maximo_comun_divisor(numero_1, numero_2)

print("Mínimo común múltiplo")
numero_1 = input("Ingrese primer valor: ")
numero_2 = input("Ingrese segundo valor: ")
mcm = minimo_comun_multiplo(int(numero_1), int(numero_2))
print(f"El mínimo común múltiplo de {numero_1} y {numero_2} es {mcm}")