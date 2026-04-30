import random
val = random.randint(1,10)
vidas = 3
while True:
    
    num = int(input("numero del creeper: "))
    
    if num == val:
        print("ganaste")
        break
        
    if num < val:
        print("el valor es mayor")
        vidas=vidas-1
        print("te quedan",vidas,"vidas")   
        
    if num > val:
        print("el valor es menor")
        vidas=vidas-1
        print("te quedan",vidas,"vidas")  
    
    if vidas == 0:
         print("ya no tienes vidas") 
         print("el valor era",val)
         break