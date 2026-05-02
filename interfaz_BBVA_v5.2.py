saldo = 1000
import random as rd
import tkinter as tk
def invertir():
    global saldo
    rad = rd.randint(1,100)
    if rad <= 50:
        boton_agarra_pala.place_forget()
        boton_1.place_forget()
        boton_2.place_forget()
        boton_3.place_forget()
        boton_4.place_forget()
        boton_5.place_forget()
        boton_6.place_forget()
        boton_7.place_forget()
        boton_8.place_forget()
        boton_9.place_forget()
        boton_10.place_forget()
        boton_casino.place_forget()
        boton_invertir.place_forget()
        saldo=saldo*2
        texto_ventana.place(relx=0.5, rely=0.5, anchor="center")
        texto_ventana.config(text=f"se duplicó \n {saldo}")
        texto_ventana.config(bg="green")
        ventana.config(bg="green")
        ventana.after(2000, menu)
    if rad > 50:
        boton_agarra_pala.place_forget()
        boton_1.place_forget()
        boton_2.place_forget()
        boton_3.place_forget()
        boton_4.place_forget()
        boton_5.place_forget()
        boton_6.place_forget()
        boton_7.place_forget()
        boton_8.place_forget()
        boton_9.place_forget()
        boton_10.place_forget()
        boton_casino.place_forget()
        boton_invertir.place_forget()
        saldo=saldo/2
        texto_ventana.place(relx=0.5, rely=0.5, anchor="center")
        texto_ventana.config(text=f"se dividió \n {saldo}")
        texto_ventana.config(bg="red")
        ventana.config(bg="red")
        ventana.after(2000, menu)    
        
    
def casino_gano():
    global saldo
    rad = rd.randint(1,51)
    if rad <= 30:
        boton_agarra_pala.place_forget()
        boton_1.place_forget()
        boton_2.place_forget()
        boton_3.place_forget()
        boton_4.place_forget()
        boton_5.place_forget()
        boton_6.place_forget()
        boton_7.place_forget()
        boton_8.place_forget()
        boton_9.place_forget()
        boton_10.place_forget()
        boton_invertir.place_forget()
        boton_casino.place_forget()
        texto_ventana.place(relx=0.5, rely=0.5, anchor="center")
        texto_ventana.config(text="perdiste 50 varos")
        texto_ventana.config(bg="red")
        saldo -= 50
        ventana.config(bg="red")
        ventana.after(2000, menu)
    elif rad > 30:
        boton_agarra_pala.place_forget()
        boton_1.place_forget()
        boton_2.place_forget()
        boton_3.place_forget()
        boton_4.place_forget()
        boton_5.place_forget()
        boton_6.place_forget()
        boton_7.place_forget()
        boton_8.place_forget()
        boton_9.place_forget()
        boton_10.place_forget()
        boton_invertir.place_forget()
        boton_casino.place_forget()
        texto_ventana.place(relx=0.5, rely=0.5, anchor="center")
        texto_ventana.config(text="ganaste 100 varos")   
        texto_ventana.config(bg="green")
        saldo += 100
        ventana.config(bg="green")
        ventana.after(2000, menu)
        
def agarra_pala_2():
    boton_casino.place_forget()
    boton_1.place_forget()
    boton_2.place_forget()
    boton_3.place_forget()
    boton_4.place_forget()
    boton_5.place_forget()
    boton_6.place_forget()
    boton_7.place_forget()
    boton_8.place_forget()
    boton_9.place_forget()
    boton_10.place_forget()
    boton_invertir.place_forget()
    boton_agarra_pala.place_forget()
    agarra_pala()
    
def agarra_pala():
    global saldo
    if saldo > 100000:
        saldo = 999999999
        texto_ventana.config(text="saldo infinito")
        texto_ventana.place(relx=0.5, rely=0.5, anchor="center")
        boton_chamba.place_forget()
        ventana.after(2000, menu)
        
    elif saldo < 1000:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        saldo += 100
        texto_ventana.place(relx=0.5, rely=0.1, anchor="center")
        texto_ventana.config(text=saldo)
    elif saldo >= 1000:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        saldo += 100
        texto_ventana.place(relx=0.5, rely=0.1, anchor="center")
        texto_ventana.config(text=saldo)
        boton_5.place(relx=0.5, rely=0.9, anchor="center")
            
        
        
def buy():
    boton_invertir.place_forget()
    boton_casino.place_forget()
    boton_1.place_forget()
    boton_2.place_forget()
    boton_3.place_forget()
    boton_4.place_forget()
    boton_5.place_forget()
    boton_10.place_forget()
    boton_agarra_pala.place_forget()
    boton_6.place(relx=0.3, rely=0.3, anchor="center")
    boton_7.place(relx=0.6, rely=0.3, anchor="center")
    boton_8.place(relx=0.3, rely=0.6, anchor="center")
    boton_9.place(relx=0.6, rely=0.6, anchor="center")
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
def buy_1():
    global saldo
    saldo -= 300
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
    else:
        menu()     
def buy_2():
    global saldo
    saldo -= 600
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
        
    else:
        menu()     
def buy_3():
    global saldo
    saldo -= 1000
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
    else:
        menu()    
def buy_4():
    global saldo
    saldo -= 3000
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
    else:
        menu()    
             
    
    
def apo():
    boton_agarra_pala.place_forget()
    boton_casino.place_forget()
    boton_10.place_forget()
    global saldo
    h = entrada.get()
    if h == "/admin.acces.infinite.money":
        saldo = 999999999
        ventana.after(2000, menu)
        boton_4.place_forget()
    monto = int(entrada.get())
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
    elif saldo < monto:
        ventana.config(bg="red")
        ventana.after(2000)
        ventana.quit()
    else:  
        saldo -= monto 
        menu() 
    
def menu():
    boton_invertir.place(relx=0.9, rely=0.1, anchor="center")
    texto_ventana.config(bg="blue")
    boton_casino.place(relx=0.1, rely=0.1, anchor="center")
    ventana.config(bg="blue")
    boton_chamba.place_forget()
    boton_6.place_forget()
    boton_7.place_forget()
    boton_8.place_forget()
    boton_9.place_forget()
    texto_ventana.config(text="BBVA")
    entrada.place_forget()
    boton_4.place_forget()
    boton_5.place_forget()
    
    texto_ventana.place(relx=0.5, rely=0.1, anchor="center")
    boton_1.place(relx=0.1, rely=0.6, anchor="center")
    boton_2.place(relx=0.9, rely=0.6, anchor="center")
    boton_3.place(relx=0.5, rely=0.7, anchor="center")
    boton_10.place(relx=0.5, rely=0.5, anchor="center")
    boton_agarra_pala.place(relx=0.5, rely=0.9, anchor="center")
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
        
    
def retirar():
    boton_agarra_pala.place_forget()
    boton_invertir.place_forget()
    boton_casino.place_forget()
    boton_10.place_forget()
    entrada.place(relx=0.5, rely=0.3, anchor="center")
    texto_ventana.place_forget()
    boton_1.place_forget()
    boton_2.place_forget()
    boton_3.place_forget()
    boton_4.place(relx=0.5, rely=0.7, anchor="center")
    if saldo <= 0:
        boton_chamba.place(relx=0.5, rely=0.5, anchor="center")
        agarra_pala_2()
        
def ver():
    texto_ventana.config(text=saldo)
    #boton para ver 
    
def salir():
    ventana.quit()   
    #boton para salir
    
    

ventana = tk.Tk()
ventana.title("Banco BBVA")
ventana.geometry("1000x600")
ventana.config(bg="blue")
texto_ventana = tk.Label(ventana, text="BBVA", font=("Arial", 16), fg="white", bg="blue")
boton_1 = tk.Button(ventana, text="saldo", fg="gold", bg="black", command=ver)
boton_2 = tk.Button(ventana, text="retirar", fg="gold", bg="black", command=retirar)
boton_3 = tk.Button(ventana, text="salir", fg="red", command=salir)
entrada = tk.Entry(ventana, justify="center", font=("Arial", 8))
boton_4 = tk.Button(ventana, text="retirar", fg="gold", bg="black", command=apo)
boton_5 = tk.Button(ventana, text="menú", fg="gold", bg="black", command=menu)
boton_6 = tk.Button(ventana, text=f"lego\n $300", fg="gold", bg="black", command=buy_1)
boton_7 = tk.Button(ventana, text=f"agua fiji\n $600", fg="gold", bg="black", command=buy_2)
boton_8 = tk.Button(ventana, text=f"carro\n $1000", fg="gold", bg="black", command=buy_3)
boton_9 = tk.Button(ventana, text=f"compu\n $3000", fg="gold", bg="black", command=buy_4)
boton_10 = tk.Button(ventana, text="comprar", fg="gold", bg="black", command=buy)
boton_chamba =tk.Button(ventana, text="+ $100", fg="gold", bg="black", command=agarra_pala) 
boton_casino = tk.Button(ventana, text="arriesga", fg="gold", bg="black", command=casino_gano)
boton_invertir = tk.Button(ventana, text="invertir", fg="gold", bg="black", command=invertir)
boton_agarra_pala = tk.Button(ventana, text="chambear?", fg="gold", bg="black", command=agarra_pala_2)
#creamos todo de la interfaz 



boton_5.place(relx=0.5, rely=0.5, anchor="center")

#texto_ventana.place(relx=0.5, rely=0.1, anchor="center")
#boton_1.place(relx=0.3, rely=0.9, anchor="center")
#boton_2.place(relx=0.9, rely=0.7, anchor="center")
#boton_3.place(relx=0.5, rely=0.9, anchor="center")

ventana.mainloop()