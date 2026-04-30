import json
def guardar_base_de_datos(lista_amigos): #carga datos guardados anteriormente 
    # Convertimos los objetos a diccionarios para que JSON los entienda
    datos_para_guardar = [usuario.__dict__ for usuario in lista_amigos]

def cargar_base_de_datos():
    try:
        with open("base_datos_scp.json", "r") as archivo:
            datos_cargados = json.load(archivo)
            
        # Convertimos los diccionarios de vuelta a objetos 
        lista_recuperada = []
        for d in datos_cargados:
            # Usamos los datos del JSON para crear un nuevo objeto
            nuevo = Info_people(d['id'], d['edad'], d['genero'])
            lista_recuperada.append(nuevo)
        
        print(">>> DATOS RECUPERADOS EXITOSAMENTE.")
        return lista_recuperada
    
    except FileNotFoundError:
        print(">>> NO SE ENCONTRÓ ARCHIVO PREVIO. INICIANDO DESDE CERO.")
        return []# si no se encuentra nada no hace nada 
            
class Info_people:
    def __init__(self,nombre,edad,genero): #la clase y sus condicionales
        self.id = nombre
        self.edad = edad
        self.genero = genero
    def presentación(self):
        print(f"nombre: \n {self.id} \n clase: \n{self.edad} \n riesgo: \n{self.genero}")
        
def buscar_scp(lista, nombre_buscado):
    for scp in lista:
        if scp.id == nombre_buscado:
            scp.presentación()
            return
    print("Entidad no encontrada.")
            
        
lista_amigos = []
lista_amigos = cargar_base_de_datos()
print("===============================")
print("==========contraseña===========")
f = input().lower()
if f == "/admin.acces.total.open": #sistema de seguridad
    print("bienvenido O5 Max")
    z = True
elif f == "revolucion de huevos franceses":
    print("bienvenido investigador")
    z = True
elif f == "class-guerrero":
    print("bienvenido guardia")
    z = True
elif f == "class-D-d-porque":
    print("bienvenido clase D")
    z = True        
else:
    print("localización enviada no escaparas")
    z = False    
    
while z:
    print("quieres salir?")
    j = input().lower()
    if j == "si":
        datos_para_guardar = [u.__dict__ for u in lista_amigos]
        with open("base_datos_scp.json", "w") as archivo:
            json.dump(datos_para_guardar, archivo, indent=4)
            print(">>> ARCHIVO ASEGURADO EN EL DISCO DURO.")#guarda los datos en el disco duro
            break  
    if j == "vaciar":
        lista_amigos = []#vacia la lista de lista_amigos
        continue
    if j == "lista":
        print("base de datos")
        for usuario in lista_amigos: #escanea toda la lista
            print(f"\n{usuario.id}")#imprime el nombre 
        continue    
            
    print("nombre del SCP?")
    k = input()
    print("clase?")
    l = input()
    print("peligro?")
    o = input() #peruntan nombre clase y peligro para guardarlo en una variable 
    usuario = Info_people(k,l,o)#guarda la información en la variable usuario
    lista_amigos.append(usuario)#añade los datos en la lista usuario
    print("quieres ver a tus SCPs?")
    h = input().lower()
    if h == "si":
        print("que SCP?")
        b = input()
        buscar_scp(lista_amigos,b)#esto busca en la variable lista_amigos según la entrada b
    else:
        continue
            