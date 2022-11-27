# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_mcm(numbers):
    print(numbers)
    for item in numbers:
        print(item)
        print(descomponer(item))


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
            acumFlag = False

    get_mcm(numbers)
