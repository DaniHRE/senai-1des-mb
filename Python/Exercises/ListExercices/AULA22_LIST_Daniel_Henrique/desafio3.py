def sort(mainlist):
    for count in range(0, len(mainlist)-1):
        for countAux in range(len(mainlist)-1):
            if mainlist[countAux] > mainlist[countAux+1]:
                copy = mainlist[countAux]
                mainlist[countAux] = mainlist[countAux+1]
                mainlist[countAux+1] = copy
    print(f"Lista: {mainlist}")
    return mainlist


def main():
    list = []

    for i in range(1, 6):
        num = int(input(f"Digite o {i}º valor: "))
        list.append(num)

        print(f"Lista não organizada: {list}")

    newlist = sort(list)
    print(f"Lista Organizada: {newlist}")


if __name__ == "__main__":
    main()