print("Funciones vercion 2")
print("Medina Zubia Nicolas")

# Zona de listas, tuplas, set y diccionario
celulares=["Samsung","IPhone 11","Chafa"]
tuplaautos=("Chevrolet","Ford","Ram","Porche","Mazda")
setjoyeria={"Cartier","Maestros Joyeros"}
print("")
DiccCanciones = {
  "Visita": "Enjambre",
  "La Gloria Eres Tu": "Luis Miguel",
  "Serenata frente al mar": "Daniel, Me estas matando",
  "La People II": "Peso Pluma",
}
print(DiccCanciones)
for x in DiccCanciones:
  print(x)


# zona de Funciones
 
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)

def vertupla(Carros):
    for unauto in Carros:
        print(unauto)

def verset(Joyas):
    for unajoya in Joyas:
        print(unajoya)


# Llamada a funciones

print("")
print("-- Imprime celulares --")
print("")
verlista(celulares)

print("")
print("-- Imprime autos --")
print("")
vertupla(tuplaautos)

print("")
print("-- Imprime Joyas --")
print("")
vertupla(setjoyeria)