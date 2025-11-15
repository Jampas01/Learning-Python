#primeira interaçao com uma 'HUD'

import tkinter as tk
import random

def jogar(escolha_jogador):
    itens = ("pedra", "papel", "tesoura")
    computador = random.randint(0, 2)
    escolha_pc = itens[computador]

    if escolha_jogador == escolha_pc:
        resultado = "Empate!"
    elif (escolha_jogador == "pedra" and escolha_pc == "tesoura") or \
         (escolha_jogador == "papel" and escolha_pc == "pedra") or \
         (escolha_jogador == "tesoura" and escolha_pc == "papel"):
        resultado = "Você ganhou!"
    else:
        resultado = "Você perdeu!"

    label_resultado.config(text=f"Você escolheu: {escolha_jogador}\nComputador: {escolha_pc}\n{resultado}")

# 🟦 Janela
janela = tk.Tk()
janela.title("JO JEN PO")
janela.geometry("200x150")

# 🟩 Botões
tk.Button(janela, text="Pedra", width=20, command=lambda: jogar("pedra")).pack(pady=10)
tk.Button(janela, text="Papel", width=20, command=lambda: jogar("papel")).pack(pady=10)
tk.Button(janela, text="tesoura", width=20, command=lambda: jogar("tesoura")).pack(pady=10)

# 🟥 Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=20)

janela.mainloop()

