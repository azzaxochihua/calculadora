# Dev 2 - Interfaz gráfica con Tkinter
import tkinter as tk

def create_ui(root, button_click):
    root.title("Calculadora V1.0")
    root.geometry("370x430")
    root.resizable(False, False)

    # Pantalla
    entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="solid", justify="right")
    entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10)

    # Botones
    buttons = [
        ("AC", 1, 0), ("C", 1, 1), ("%", 1, 2), ("/", 1, 3),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
        ("0", 5, 0), (".", 5, 1), ("=", 5, 2, 2)
    ]

    for btn in buttons:
        text = btn[0]
        row = btn[1]
        col = btn[2]
        colspan = btn[3] if len(btn) > 3 else 1

        tk.Button(
            root,
            text=text,
            width=6 if colspan == 1 else 14,
            height=2,
            font=("Arial", 14),
            command=lambda t=text: button_click(t)
        ).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

    return entry
