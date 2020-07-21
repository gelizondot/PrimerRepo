menu = print("""S. Suma
R. Restra
M. Multiplicacion
D. Division
A. Salir""")


let = input("Elija una opcion. ")


while let.upper() in "SRMDA":
    if let.upper() == "S":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        suma = num1 + num2
        print(f"la suma es {suma}")
    
    
    elif let.upper() == "R":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        resta = num1 - num2
        print(f"la resta es {resta}")
    
    elif let.upper() == "M":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        multi = num1 - num2
        print(f"la multiplicacion es {multi}")
    
    elif let.upper() == "D":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        division = num1 - num2
        print(f"la divison es: {division}")
    
else:
    print("salir")