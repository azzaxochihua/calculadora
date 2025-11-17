# Dev 3 - Controlador: maneja la interacción entre UI y lógica

from evaluator import evaluate_expression

class CalculatorController:
    def __init__(self, entry):
        self.entry = entry
        self.expression = ""

    def button_click(self, value):
        if value == "=":
            self.evaluate()
        elif value == "AC":  # limpiar todo
            self.expression = ""
            self.update_entry()
        elif value == "C":  # borrar último carácter
            self.expression = self.expression[:-1]
            self.update_entry()
        else:
            self.expression += value
            self.update_entry()

    def update_entry(self):
        self.entry.delete(0, "end")
        self.entry.insert("end", self.expression)

    def evaluate(self):
        try:
            result = evaluate_expression(self.expression)
            self.expression = str(result)
            self.update_entry()
        except Exception:
            self.expression = ""
            self.entry.delete(0, "end")
            self.entry.insert("end", "Error")
