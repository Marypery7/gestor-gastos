gastos = [12, 8, 25, 15, 30]

# 1. Calcula el total
total = 0
for gasto in gastos:
    total += gasto
print(f"El gasto total es: {total}")

# 2. Calcula la media
media = total / len(gastos)
print(f"El gasto medio es: {media}")

# 3. Muestra los gastos mayores de 20
print("Gastos mayores de 20:")
for gasto in gastos:
    if gasto > 20:
        print(gasto)

