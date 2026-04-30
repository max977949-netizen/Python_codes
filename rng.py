import random
intentos = 0
nombre = input("¿Como te llamas aventurero?: ")
while True:
    Blas = input("quieres empezar?: ")
    
    if Blas == "si":
    
        
        
        val = random.randint(1,100)
        if val > 96:
            print("obtuviste netherite")
            intentos=intentos+1
            print("felicidades",nombre," te tomo",intentos,"intentos encontrar netherite")
            break
            
        if val <= 81 and val >= 95:
            print("obtuviste diamante")
            intentos=intentos+1    
    
        if val <= 80 and val >= 51:
            print("obtuviste hierro")
            intentos=intentos+1
    
            
        if val <= 50 and val >= 11:
            print("obtuviste tierra")
            intentos=intentos+1
            
        if val <= 10:
            print("era una trampa + 5 intentos")
            intentos=intentos+5 
            
            
            
            
            
            
            
            
    
    if Blas == "netherite":
        print("obtuviste netherite")
        intentos=intentos+1
        print("felicidades",nombre," te tomo",intentos,"intentos encontrar netherite")
        break
                   
    
        
                    