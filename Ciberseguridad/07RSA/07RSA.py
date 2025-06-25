import tkinter as tk
from tkinter import messagebox
from math import gcd

# ------------------ FUNCIONES DE CÁLCULO ------------------ #
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def cifrar():
    try:
        m = int(entry_mensaje.get())
        if m >= n:
            messagebox.showerror("Error", "El número a cifrar debe ser menor que n.")
            return
        c = pow(m, e, n)
        messagebox.showinfo("Cifrado", f"Mensaje cifrado: {c}")
    except:
        messagebox.showerror("Error", "Entrada inválida para cifrado.")

def abrir_descifrado():
    def descifrar():
        try:
            c = int(entry_cifrado.get())
            d_val = int(entry_d.get())
            m = pow(c, d_val, n)
            messagebox.showinfo("Descifrado", f"Mensaje original: {m}")
        except:
            messagebox.showerror("Error", "Entrada inválida para descifrado.")

    ventana_descifrado = tk.Toplevel()
    ventana_descifrado.title("Descifrar mensaje")

    # Centrar ventana descifrado
    ancho, alto = 300, 150
    x = (ventana_descifrado.winfo_screenwidth() - ancho) // 2
    y = (ventana_descifrado.winfo_screenheight() - alto) // 2
    ventana_descifrado.geometry(f"{ancho}x{alto}+{x}+{y}")
    ventana_descifrado.resizable(False, False)

    tk.Label(ventana_descifrado, text="Mensaje cifrado:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_cifrado = tk.Entry(ventana_descifrado)
    entry_cifrado.grid(row=0, column=1, padx=5)

    tk.Label(ventana_descifrado, text="d:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_d = tk.Entry(ventana_descifrado)
    entry_d.grid(row=1, column=1, padx=5)

    btn_descifrar = tk.Button(ventana_descifrado, text="Descifrar", width=20, command=descifrar)
    btn_descifrar.grid(row=2, column=0, columnspan=2, pady=10)

# ------------------ PARÁMETROS RSA ------------------ #
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
while gcd(e, phi) != 1:
    e += 2

d = modinv(e, phi)

# ------------------ VENTANA PRINCIPAL ------------------ #
ventana = tk.Tk()
ventana.title("Calculadora RSA")

# Centrar ventana principal
ancho_ventana, alto_ventana = 350, 300
x = (ventana.winfo_screenwidth() - ancho_ventana) // 2
y = (ventana.winfo_screenheight() - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
ventana.resizable(False, False)

# Crear layout ordenado con grid
info_frame = tk.Frame(ventana)
info_frame.pack(pady=10)

valores = [
    f"p = {p}",
    f"q = {q}",
    f"n = p × q = {n}",
    f"ϕ(n) = (p−1)×(q−1) = {phi}",
    f"e = {e}",
    f"d = {d}"
]

for i, texto in enumerate(valores):
    tk.Label(info_frame, text=texto, font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="w", padx=10, pady=2)

# Entrada para cifrado
entrada_frame = tk.Frame(ventana)
entrada_frame.pack(pady=10)

tk.Label(entrada_frame, text="Mensaje a cifrar (número):").grid(row=0, column=0, sticky="e", padx=5)
entry_mensaje = tk.Entry(entrada_frame)
entry_mensaje.grid(row=0, column=1, padx=5)

# Botones
boton_frame = tk.Frame(ventana)
boton_frame.pack(pady=10)

tk.Button(boton_frame, text="Cifrar", width=15, command=cifrar).grid(row=0, column=0, padx=5)
tk.Button(boton_frame, text="Ir a descifrado", width=15, command=abrir_descifrado).grid(row=0, column=1, padx=5)

ventana.mainloop()
