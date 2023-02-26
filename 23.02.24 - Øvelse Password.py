# Get age
#age = int(input("Hvor gammel er du? "))
# Get password
#password = input("Hvad er dit password? ")

# Tjek alder og password for at give adgang
#if age >= 20 and password == "DankMemes69":
#    print("Adgang godkendt!")
#else:
#    print("Adgang benægtet. Alder eller password er forkert!")




# Get age
age = int(input("Hvor gammel er du? "))
# Tjek alder
if age < 20:
    print("Adgang nægtet! Alder for lav!")
# Tjek password og print adgangsstatus
elif input("Hvad er dit password? ") == "DankMemes69" and age >= 20:
    print("Adgang godkendt!")
else:
    print("Adgang nægtet! Password forkert!")
