saldo = 1000
import tkinter as tk
def apo():
    global saldo
    monto = int(entrada.get())
    saldo -= monto
    if saldo < monto:
        ventana.config(bg="red")
        ventana.quit()
    else:    
        menu()
    
def menu():
    texto_ventana.place_forget()
    entrada.place_forget()
    boton_4.place_forget()
    boton_5.place_forget()
    texto_ventana.place(relx=0.5, rely=0.1, anchor="center")
    boton_1.place(relx=0.1, rely=0.6, anchor="center")
    boton_2.place(relx=0.9, rely=0.6, anchor="center")
    boton_3.place(relx=0.5, rely=0.9, anchor="center")
    if saldo <= 0:
        ventana.quit()
        
    
def retirar():
    entrada.place(relx=0.5, rely=0.3, anchor="center")
    texto_ventana.place_forget()
    boton_1.place_forget()
    boton_2.place_forget()
    boton_3.place_forget()
    boton_4.place(relx=0.5, rely=0.7, anchor="center")
        
        
    
def ver():
    texto_ventana.config(text=saldo)
    
def salir():
    ventana.quit()         
    
    

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.config(bg="blue")
texto_ventana = tk.Label(ventana, text="BBVA", font=("Arial", 8), fg="black")
boton_1 = tk.Button(ventana, text="ver saldo", command=ver)
boton_2 = tk.Button(ventana, text="retirar", command=retirar)
boton_3 = tk.Button(ventana, text="salir", command=salir)
entrada = tk.Entry(ventana, justify="center", font=("Arial", 8))
boton_4 = tk.Button(ventana, text="retirar", command=apo)
boton_5 = tk.Button(ventana, text="menú", command=menu)

boton_5.place(relx=0.5, rely=0.5, anchor="center")

#texto_ventana.place(relx=0.5, rely=0.1, anchor="center")
#boton_1.place(relx=0.3, rely=0.9, anchor="center")
#boton_2.place(relx=0.9, rely=0.7, anchor="center")
#boton_3.place(relx=0.5, rely=0.9, anchor="center")

ventana.mainloop()