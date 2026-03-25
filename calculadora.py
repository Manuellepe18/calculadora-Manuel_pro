import tkinter as tk

# Colores (modo oscuro)
COLOR_FONDO = "#636563"
COLOR_BOTON = "#3970CF"
COLOR_OPERADOR = "#839FE6"
COLOR_TEXTO = "#eff1ef"
COLOR_PANTALLA = "#3B3B41"

ventana = tk.Tk()
ventana.title("Calculadora ManuPro")
ventana.geometry("320x450")
ventana.configure(bg=COLOR_FONDO)

# Configuración responsive
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=4)
ventana.columnconfigure(0, weight=1)

# Pantalla
pantalla = tk.Entry(
    ventana,
    font=("Arial", 24),
    bd=0,
    bg=COLOR_PANTALLA,
    fg=COLOR_TEXTO,
    justify="right"
)
pantalla.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Funciones
def click_boton(valor):
    pantalla.insert(tk.END, valor)

def limpiar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Frame botones
frame = tk.Frame(ventana, bg=COLOR_FONDO)
frame.grid(row=1, column=0, sticky="nsew")

for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# Crear botones
def crear_boton(texto, fila, col, color_fondo, comando):
    boton = tk.Button(
        frame,
        text=texto,
        font=("Arial", 16, "bold"),
        bg=color_fondo,
        fg=COLOR_TEXTO,
        bd=0,
        activebackground="#555555",
        activeforeground=COLOR_TEXTO,
        command=comando
    )
    boton.grid(row=fila, column=col, sticky="nsew", padx=5, pady=5)

# Layout botones
botones = [
    ("C", 0, 0, COLOR_OPERADOR, limpiar),
    ("", 0, 1, COLOR_FONDO, None),
    ("", 0, 2, COLOR_FONDO, None),
    ("/", 0, 3, COLOR_OPERADOR, lambda: click_boton("/")),

    ("7", 1, 0, COLOR_BOTON, lambda: click_boton("7")),
    ("8", 1, 1, COLOR_BOTON, lambda: click_boton("8")),
    ("9", 1, 2, COLOR_BOTON, lambda: click_boton("9")),
    ("*", 1, 3, COLOR_OPERADOR, lambda: click_boton("*")),

    ("4", 2, 0, COLOR_BOTON, lambda: click_boton("4")),
    ("5", 2, 1, COLOR_BOTON, lambda: click_boton("5")),
    ("6", 2, 2, COLOR_BOTON, lambda: click_boton("6")),
    ("-", 2, 3, COLOR_OPERADOR, lambda: click_boton("-")),

    ("1", 3, 0, COLOR_BOTON, lambda: click_boton("1")),
    ("2", 3, 1, COLOR_BOTON, lambda: click_boton("2")),
    ("3", 3, 2, COLOR_BOTON, lambda: click_boton("3")),
    ("+", 3, 3, COLOR_OPERADOR, lambda: click_boton("+")),

    ("0", 4, 0, COLOR_BOTON, lambda: click_boton("0")),
    ("=", 4, 1, COLOR_OPERADOR, calcular),
]

# Crear botones en pantalla
for texto, fila, col, color, comando in botones:
    if texto != "":
        crear_boton(texto, fila, col, color, comando)

ventana.mainloop()