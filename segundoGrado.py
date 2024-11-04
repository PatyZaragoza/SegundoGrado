#Autor: Patricia Zaragoza Palma
# Ingenieria en Sistemas Computacionales

import tkinter as tk
from tkinter import messagebox
import math

# Función para resolver la ecuación de segundo grado
def resolver_ecuacion():
    try:
        # Obtener los valores de a, b y c de la entrada
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
        
        # Calcular el discriminante
        discriminante = b**2 - 4*a*c
        
        # Determinar el tipo de solución según el discriminante
        if discriminante > 0:
            # Dos soluciones reales
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            resultado = f"Dos soluciones reales: x₁ = {x1}, x₂ = {x2}"
        elif discriminante == 0:
            # Una solución real
            x = -b / (2 * a)
            resultado = f"Una solución real: x = {x}"
        else:
            # Soluciones complejas
            real = -b / (2 * a)
            imag = math.sqrt(-discriminante) / (2 * a)
            resultado = f"Soluciones complejas: x₁ = {real} + {imag}i, x₂ = {real} - {imag}i"
        
        # Mostrar el resultado en la etiqueta de salida
        salida_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "El valor de 'a' no puede ser cero en una ecuación de segundo grado.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Resolución de Ecuaciones de Segundo Grado")

# Crear y colocar los elementos de la interfaz
etiqueta_a = tk.Label(ventana, text="Introduce el valor de a:")
etiqueta_a.pack()
entrada_a = tk.Entry(ventana)
entrada_a.pack()

etiqueta_b = tk.Label(ventana, text="Introduce el valor de b:")
etiqueta_b.pack()
entrada_b = tk.Entry(ventana)
entrada_b.pack()

etiqueta_c = tk.Label(ventana, text="Introduce el valor de c:")
etiqueta_c.pack()
entrada_c = tk.Entry(ventana)
entrada_c.pack()

boton_resolver = tk.Button(ventana, text="Resolver Ecuación", command=resolver_ecuacion)
boton_resolver.pack()

salida_resultado = tk.Label(ventana, text="Resultado:")
salida_resultado.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
