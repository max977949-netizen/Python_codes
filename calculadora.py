import math

yes = input("quieres calcular algo?: ")
if yes == "si":
    num1 = int(input("número: "))
    nume = input("numerador: ")
    num2 = int(input("número 2: "))
    
if nume == "+":
    print(num1,"+",num2,"=",num1 + num2) 

if nume == "-":
    print(num1,"-",num2,"=",num1 - num2)   

if nume == "×":
    print(num1,"×",num2,"=",num1 * num2)
    
if nume == "÷":
    if num2 == 0:
        print("operación no valida")
    else:
        print(num1,"÷",num2,"=",num1 / num2)
    
if nume == "^":
    print(num1,"elevado a la",num2,"=",num1 ** num2)
    
if nume == "√":
    result = math.sqrt(num1)
    
    print("la raiz cuadrada de",num1,"es",result)  
    
if nume == "%":
    pors = (num1 * num2) / 100
    
    print("el",num1,"porciento de",num2,"=",pors)    
    