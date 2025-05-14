import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.entrada = tk.Entry(master, width=25, borderwidth=5, font=("Arial", 16), justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        linha = 1
        coluna = 0
        for botao_texto in botoes:
            botao = tk.Button(master, text=botao_texto, padx=20, pady=20, font=("Arial", 14),
                              command=lambda texto=botao_texto: self.clicar_botao(texto))
            botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        # Configurar o redimensionamento das linhas e colunas
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

        self.operacao = None
        self.primeiro_valor = None

    def clicar_botao(self, texto):
        if texto == "=":
            self.calcular()
        elif texto == "C":
            self.limpar_entrada()
        elif texto in ['+', '-', '*', '/']:
            self.realizar_operacao(texto)
        else:
            self.entrada.insert(tk.END, texto)

    def limpar_entrada(self):
        self.entrada.delete(0, tk.END)
        self.operacao = None
        self.primeiro_valor = None

    def realizar_operacao(self, op):
        try:
            self.primeiro_valor = float(self.entrada.get())
            self.operacao = op
            self.entrada.delete(0, tk.END)
        except ValueError:
            self.entrada.insert(0, "Erro")

    def calcular(self):
        try:
            segundo_valor = float(self.entrada.get())
            resultado = 0
            if self.operacao == '+':
                resultado = self.primeiro_valor + segundo_valor
            elif self.operacao == '-':
                resultado = self.primeiro_valor - segundo_valor
            elif self.operacao == '*':
                resultado = self.primeiro_valor * segundo_valor
            elif self.operacao == '/':
                if segundo_valor == 0:
                    resultado = "Erro: Div por 0"
                else:
                    resultado = self.primeiro_valor / segundo_valor
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, resultado)
            self.operacao = None
            self.primeiro_valor = None
        except (ValueError, TypeError):
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Erro")

root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()