def joules(richter):
    return (10**((1.5 * richter) + 4.8))


def tnt(richter):
    return (richter * (4.184 * (10**9)))


def programme(richter):
    title = ("Richter         Joules                  TNT")
    find = (title.find("T"))
    printingstatement = (str(richter) + ((16 - len(str(richter))) * " ") +
                         str(joules(richter)))
    printingstatement += ((find - len(printingstatement)) * " ")
    printingstatement += str(tnt(richter))
    print(printingstatement)


def main():
    print("Richter         Joules                  TNT")
    programme(1)
    programme(5)
    programme(9.1)
    programme(9.2)
    programme(9.2)
    richter = float(
        input("What is the Richter scale you want to investigate?"))
    print("")
    programme(richter)
