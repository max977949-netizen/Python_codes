import random
saldo = int(input("¿Cuánto dinero tienes?: "))
ret = 0
w = ""
s = ""
c = ""
i = "impuesto"
impu = 0
q = ""
h = ""
while True:
    val = random.randint(1,50)
    vel = random.randint(80,116) / 100
    vil = random.randint(100,200)
    if saldo >= 10000:
        print("lo siento Pero se detecto lavado de dinero, solo te quedarás con 9999 pesos y el SAT se quedará con el resto")
        saldo = 9999
        
    if val < 10:
        print("felicidades... le debes",vil,"pesos al SAT")
        saldo=saldo-vil
        print("Te quedan",saldo,"pesos") 
        
    if saldo < 0:
        saldo=0       
        
    if saldo <= 0:
        h = True
        
    if saldo > 0:
        h = False        
        
    while h:
        q = input("¿De verdad quieres chambear?: ")
        if q == "si":
            print("felicidades ahora estás en la asombrosa chamba digital")
            
        if q == "no":
            break
               
        w = input("di chambear para chambear: ")
        if w == "chambear":
            while True:
                d = input("pon 1 para ganar un peso: ")
                if d == "1":
                    saldo=saldo+1
                
                if d == "10":
                    saldo=saldo+10 
            
                if d == "100":
                    saldo=saldo+100
                    
                if d == "1000":
                    saldo=saldo+1000    
                    
                if d == "salir":
                    break
            
                if saldo >= 1000:
                    break         
             
    
        if saldo >= 1000:
            break
            
        q = input("¿quieres seguir chambeando?: ")
        if q == "no":
            h = False
            
        else:
            h = True         
        
        
    s = input("que acción quieres hacer? 1 ver saldo. 2 comprar. 3 retirar. 4 salir: ")
    if s == "1":
        print("te quedan",round(saldo,2),"pesos")
        
    if s == i :
        print("felicidades... le debes",vil,"pesos al SAT")
        saldo=saldo-vil
        print("Te quedan",saldo,"pesos")           
        
    if s == "2":
        c = input("1.-lego 100 pesos. 2.-agua figi 300 pesos. 3.-carro del año 600 pesos. 4.-compu gamer 1000 pesos: ") 
        if c == "1":
            saldo=saldo-(100*vel)
            print("lego comprado ")
        
        if c == "2":
            saldo=saldo-(300*vel)
            print("agua comprada ")
            
        if c == "3":
            saldo=saldo-(600*vel)
            print("carro comprado ")
            
        if c == "4":
            saldo=saldo-(1000*vel)
            print("compu gamer comprada ")
    
    if s == "3":
        ret = int(input("¿Cuánto quieres retirar?: "))
        saldo=saldo-ret
        print("has retirado",ret,"peso te quedan",saldo,"pesos")
        
    if s == "4":
        print("saliendo")
        break
        
    if w == "salir":
        print("saliendo")
        break 
        
    q = input("¿quieres chambear?: ")    
    if q == "si":
        h = True   
        
    else:
        h = False  
            