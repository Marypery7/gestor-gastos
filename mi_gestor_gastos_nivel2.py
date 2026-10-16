# mi_gestor_gastos_nivel2.py

def analizar_gastos(lista_gastos):
    # 1. Calcula el total con un bucle
    total = 0
    for gasto in lista_gastos:
        total += gasto
    
    # 2. Calcula la media
    cantidad = len(lista_gastos)
    media = total / cantidad if cantidad > 0 else 0
    
    # 3. Muestra los resultados principales
    print(f"--- ANÁLISIS DE GASTOS ---")
    print(f"Lista de gastos: {lista_gastos}")
    print(f"Gasto total: {total} €")
    print(f"Gasto medio: {media} €")
    
    # 4. Utiliza una condición para mostrar los gastos superiores a 20 €
    print("\nGastos superiores a 20 €:")
    hay_altos = False
    for gasto in lista_gastos:
        if gasto > 20:
            print(f" - {gasto} €")
            hay_altos = True
    if not hay_altos:
        print(" - Ningún gasto supera los 20 €.")
        
    # 5. Compara el total con el presupuesto de 100 €
    presupuesto = 100
    print(f"\nPresupuesto semanal: {presupuesto} €")
    if total > presupuesto:
        exceso = total - presupuesto
        print(f"⚠️ ¡Atención! Has superado el presupuesto por {exceso} €.")
    else:
        ahorro = presupuesto - total
        print(f"✅ ¡Muy bien! Estás dentro del presupuesto. Te quedan {ahorro} €.")

def main():
    # Define una lista de cinco gastos (o más)
    mis_gastos = [12, 8, 25, 15, 30]
    
    # Llama a la función organizadora
    analizar_gastos(mis_gastos)

if __name__ == "__main__":
    main()
