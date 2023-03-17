
# main funktionen defineres øverst og indeholder resten af programmets definerede funktioner
def main():
    for i in range(10):
        print_besked1()
    print("\n")
    print_besked2()


# Nedenunder står de definerede funktioner der skal bruges af main funktionen
def print_besked1():
    print("Gud, Bæver, Danmark")

def print_besked2():
    print("Flere bæver til Danmark!")

# Til sidst kaldes main funktionen for at køre programmet
main()