# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_mcm(numbers):
    print(numbers)
    mat_factores = []
    factores_nocomunes = []
    factores_comunes = []

    for item in numbers:
        print(item)

        local_factor = descomponer(item)
        mat_factores.append(local_factor)

    sum_mat = []
    for f in mat_factores:
        sum_mat += f

    totales_factor = {factor: 0 for factor in set(sum_mat)}

    for item in mat_factores:
        repeticiones = {k: item.count(k) for k in set(item)}

        for key, value in repeticiones.items():
            if value > totales_factor[key]:
                totales_factor[key] = value

    print(totales_factor)
    mcm = 1
    for key, value in totales_factor.items():
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
            if numbers.count() <= 1:
                print("debes escoger mas de 1 numero.")
            else:
                acumFlag = False

        if numbers.count() == 10:
            print("Has llegado al limite de numeros.")
            acumFlag = False


    get_mcm(numbers)
