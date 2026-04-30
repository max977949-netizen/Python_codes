import random
rps = ["piedra","papel","tijeras"]

while True:
    lol = random.choice(rps)
    lo = input("¿piedra, papel o tijeras?: ")
    
    if lo == "tijeras" and lol == "piedra":
        print("perdistes")
        print(lol," aplasta tijeras")
        
        
    if lo == lol:
        print("empate")
        
    if lo == "piedra" and lol == "tijeras":
        print("ganaste")
        break
        
    if lo == "papel" and lol == "piedra":
        print("ganaste")
        break
        
    if lo == "tijeras" and lol == "papel":
        print("ganaste")
        break
        
    if lo == "papel" and lol == "tijeras":
        print("perdistes")
        
    if lo == "piedra" and lol == "papel":
        print("perdiste")    
    
            