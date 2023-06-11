letra = input("Ingrese f/m para saber la mesa de votacion: ")
while letra.lower() != 'f' and letra.lower() != 'm':
    print("Error: Ingrese la letra 'f' o 'm' ")
    letra = input("Ingrese f/m para saber la mesa de votacion: ")
if letra.lower() == 'm':
    print("Votas en la mesa Masculina")
else:
    print("Votas en la mesa Femenina")

Ejercicio 9
for i in range(2):
    x = int(input(f"Ingrese el {i + 1}ro numero: "))
    if i == 0:
        n1 = x
    else:
        n2 = x
if n1 > n2:
    print("El primer numero es mayor")
else:
    print("El segundo numero es mayor")