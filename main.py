# main.py - Integra todo el proyecto

import tkinter as tk
from ui_main import create_ui
from controller import CalculatorController

def main():
    root = tk.Tk()

    # Se crea la interfaz y el controlador
    controller = CalculatorController(None)
    entry = create_ui(root, controller.button_click)
    controller.entry = entry

    root.mainloop()

if __name__ == "__main__":
    main()
