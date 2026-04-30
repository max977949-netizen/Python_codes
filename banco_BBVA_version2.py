saldo = 1000
import tkinter as tk
def buy():
    boton_1.place_forget()
    boton_2.place_forget()
    boton_3.place_forget()
    boton_4.place_forget()
    boton_5.place_forget()
    boton_10.place_forget()
    boton_6.place(relx=0.3, rely=0.3, anchor="center")
    boton_7.place(relx=0.6, rely=0.3, anchor="center")
    boton_8.place(relx=0.3, rely=0.6, anchor="center")
    boton_9.place(relx=0.6, rely=0.6, anchor="center")
    if saldo <= 0:
        ventana.config(bg="red")
        ventana.after(2000)
        ventana.quit()
def buy_1():
    global saldo
    saldo -= 100
    menu() 
def buy_2():
    global saldo
    saldo -= 300
    menu()  
def buy_3():
    global saldo
    saldo -= 600
    menu()  
def buy_4():
    global saldo
    saldo -= 800
    menu()           
    
    
def apo():
    boton_10.place_forget()
    global saldo
    monto = int(entrada.get())
    if saldo <= 0:
        ventana.config(bg="red")
        ventana.after(2000)
        ventana.quit()
    elif saldo < monto:
        ventana.config(bg="red")
        ventana.after(2000)
        ventana.quit()
    else:  
        saldo -= monto  
        menu()
    
def menu():
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
    if saldo <= 0:
        ventana.config(bg="red")
        ventana.after(2000)
        ventana.quit()
        
    
def retirar():
    boton_10.place_forget()
    entrada.place(relx=0.5, rely=0.3, anchor="center")
    texto_ventana.place_forget()
    boton_1.place_forget()
    boton_2.place_forget()
    boton_3.place_forget()
    boton_4.place(relx=0.5, rely=0.7, anchor="center")
    if saldo <= 0:
        ventana.config(bg="red")
        ventana.after(2000)
        ventana.quit()
        
def ver():
    texto_ventana.config(text=saldo)
    
def salir():
    ventana.quit()         
    
    

ventana = tk.Tk()
ventana.title("Banco BBVA")
ventana.geometry("1000x600")
ventana.config(bg="blue")
texto_ventana = tk.Label(ventana, text="BBVA", font=("Arial", 16), fg="white", bg="blue")
boton_1 = tk.Button(ventana, text="saldo", fg="gold", bg="black", command=ver)
boton_2 = tk.Button(ventana, text="retirar", fg="gold", bg="black", command=retirar)
boton_3 = tk.Button(ventana, text="salir", fg="red", command=salir)
entrada = tk.Entry(ventana, justify="center", font=("Arial", 8))
boton_4 = tk.Button(ventana, text="retirar", command=apo)
boton_5 = tk.Button(ventana, text="menú", command=menu)
boton_6 = tk.Button(ventana, text="lego", fg="gold", bg="black", command=buy_1)
boton_7 = tk.Button(ventana, text="agua fiji", fg="gold", bg="black", command=buy_2)
boton_8 = tk.Button(ventana, text="carro", fg="gold", bg="black", command=buy_3)
boton_9 = tk.Button(ventana, text="compu", fg="gold", bg="black", command=buy_4)
boton_10 = tk.Button(ventana, text="comprar", fg="gold", bg="black", command=buy)

boton_5.place(relx=0.5, rely=0.5, anchor="center")

#texto_ventana.place(relx=0.5, rely=0.1, anchor="center")
#boton_1.place(relx=0.3, rely=0.9, anchor="center")
#boton_2.place(relx=0.9, rely=0.7, anchor="center")
#boton_3.place(relx=0.5, rely=0.9, anchor="center")

ventana.mainloop()