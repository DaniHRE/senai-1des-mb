def areaCalc(base, altura):
    area = (base * altura)
    return area


if __name__ == "__main__":
    altura = int(input("Digite a altura: "))
    base = int(input("Digite a base: "))
    print(areaCalc(base, altura))
