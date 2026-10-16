# 💰 Gestor de Gastos en Python (`mi_gestor_gastos`)

Este proyecto consiste en una aplicación interactiva desarrollada en Python para la gestión y control de presupuestos personales. Evoluciona gradualmente desde conceptos básicos de programación hasta una arquitectura modular con interfaz interactiva en terminal.

---

## 🚀 Niveles del Proyecto

### 📌 Nivel 1: Operaciones Básicas (`mi_gestor_gastos.py`)
- Cálculo automático de gasto total y gasto medio a partir de una lista fija de datos.
- Filtrado dinámico de gastos superiores a un umbral determinado (20 €).
- Conceptos clave: Listas, bucles `for`, condicionales `if`.

### 📌 Nivel 2: Control de Presupuesto y Funciones (`mi_gestor_gastos_nivel2.py`)
- Modularización del código mediante funciones reutilizables (`calcular_total`, `calcular_promedio`, `filtrar_gastos`).
- Evaluación de límites presupuestarios (presupuesto semanal de 100 €).
- Alertas dinámicas sobre exceso o margen de presupuesto disponible.

### 📌 Nivel 3: Sistema Interactivo Completo (`mi_gestor_gastos_nivel3.py`)
- Menú de navegación interactivo con bucle `while`.
- Entrada dinámica de gastos por parte del usuario con validación mediante bloques `try/except`.
- Control de excepciones para evitar errores de división por cero en listas vacías.
- Umbral de filtrado personalizado por el usuario.

---

## 💻 Requisitos e Instalación

Para ejecutar este proyecto de forma local:

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Marypery7/gestor-gastos.git](https://github.com/Marypery7/gestor-gastos.git)
