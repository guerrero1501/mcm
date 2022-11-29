# This is a sample Python script.
from collections import Counter


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_mcm(numbers):
    print("Numeros ingresados: ", numbers)
    mat_factores = []

    for item in numbers:
        local_factor = descomponer(item)
        mat_factores.append(local_factor)

    sum_mat = []
    for f in mat_factores:
        sum_mat += f

    totales_factor_mcm = {factor: 0 for factor in set(sum_mat)}

#para mcm
    for item in mat_factores:
        repeticiones = {k: item.count(k) for k in set(item)}

        for key, value in repeticiones.items():
            if value > totales_factor_mcm[key]:
                totales_factor_mcm[key] = value
#fin mcm

#para mcd
    dupe_counter = Counter((n for a in mat_factores for n in a))
    no_com = {num: count for num, count in dupe_counter.items() if count == len(mat_factores)}
    print("no se repiten en todos los factores: ", no_com)
    #fin mcd
    print(totales_factor_mcm)
    mcm = 1
    for key, value in totales_factor_mcm.items():
        mcm *= pow(key, value)

    print('El minimo comun multiplo es: ', mcm)


def descomponer(n):
    primos = []

    for i in range(2, n + 1):
        while n % i == 0:
            primos.append(i)
            n = n / i
    return primos


if __name__ == '__main__':
    acumFlag = True
    numbers = []

    while acumFlag:
        numberClient = input("Agrega numeros de 3 digitos o mas para saber el MCM y el MCD. \n")
        numbers.append(int(numberClient))
        flag = input("Presiona cualquier tecla para continuar o (f) para finalizar\n")
        if flag == "f" or flag == "F":
            if len(numbers) <= 1:
                print("debes escoger mas de 1 numero.")
            else:
                acumFlag = False

        if len(numbers) == 10:
            print("Has llegado al limite de numeros.")
            acumFlag = False

    get_mcm(numbers)
