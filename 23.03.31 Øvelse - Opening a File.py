"""
filnavn = "testfil.txt"

minfil = open(filnavn, "w")


a = 69
minfil.write("yes\n")
minfil.write("123\n")
minfil.write(f"Tallet er {a}\n")

minfil.close()

minfil
"""

"""
# Opgave 1
minfil = open("Things.txt", "w")
minfil.write("Baever\n"
             "Banan\n"
             "Sverige")
minfil.close
"""

"""
# Opgave 2
minFil = open("Things.txt", "r")
filIndhold = minFil.read()
minFil.close()
print(filIndhold)
"""


# Opgave 3
fil3 = open("number_list.txt", "w")
filTal = 0
for i in range(100):
    filTal += 1
    fil3.write(f"{str(filTal)}\n")
fil3.close()


"""
# Opgave 4
# Åbner og viser indholdet
fil3 = open("number_list.txt", "r")
filIndhold = fil3.read()
fil3.close()
print(filIndhold)
"""

