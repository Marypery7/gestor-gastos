# mi_gestor_gastos_nivel3.py

def calcular_total(gastos):
    """Calcula y devuelve el total de los gastos."""
    total = 0
    for gasto in gastos:
        total += gasto
    return total

def mostrar_menu():
    print("\n=======================================")
    print("      MI GESTOR DE GASTOS - NIVEL 3    ")
    print("=======================================")
    print("1. Ver lista de gastos y análisis")
    print("2. Añadir un nuevo gasto")
    print("3. Salir")
    print("=======================================")

def analizar_gastos(gastos):
    # Proteger contra lista vacía
    if not gastos:
        print("\n⚠️ No hay gastos registrados en la lista.")
        return
        
    # 1. Usar la función calcular_total
    total = calcular_total(gastos)
    
    # 2. Calcula la media (evitando división por cero)
    cantidad = len(gastos)
    if cantidad > 0:
        media = total / cantidad
    else:
        media = 0.0
        
    # 3. Muestra los resultados principales
    print(f"\n--- ANÁLISIS DE GASTOS ---")
    print(f"Lista actual: {gastos}")
    print(f"Gasto total: {total:.2f} €")
    print(f"Gasto medio: {media:.2f} €")
    
    # 4. Permitir que la persona introduzca un límite para filtrar los gastos
    try:
        limite = float(input("\nIntroduce un límite en € para filtrar gastos superiores: "))
    except ValueError:
        print("❌ Valor no válido. Se usará por defecto el límite de 20.0 €.")
        limite = 20.0

    print(f"Gastos superiores a {limite:.2f} €:")
    hay_altos = False
    for gasto in gastos:
        if gasto > limite:
            print(f" - {gasto:.2f} €")
            hay_altos = True
    if not hay_altos:
        print(f" - Ningún gasto supera los {limite:.2f} €.")
        
    # 5. Compara el total con el presupuesto de 100 €
    presupuesto = 100.00
    print(f"\nPresupuesto semanal: {presupuesto:.2f} €")
    if total > presupuesto:
        exceso = total - presupuesto
        print(f"⚠️ ¡Atención! Has superado el presupuesto por {exceso:.2f} €.")
    else:
        ahorro = presupuesto - total
        print(f"✅ ¡Muy bien! Estás dentro del presupuesto. Te quedan {ahorro:.2f} €.")

def main():
    # Lista inicial de gastos (puedes probar a dejarla vacía [] si quieres probar el caso base)
    gastos = [12.0, 8.5, 25.0, 35.0]
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1":
            analizar_gastos(gastos)
        elif opcion == "2":
            try:
                nuevo_gasto = float(input("Introduce el importe del nuevo gasto (€): "))
                gastos.append(nuevo_gasto)
                print(f"✅ Gasto de {nuevo_gasto:.2f} € añadido correctamente.")
            except ValueError:
                print("❌ Error: Por favor, introduce un número válido.")
        elif opcion == "3":
            print("¡Gracias por usar el gestor de gastos! ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    main()
