from rich import print
import sqlite3


escolha = input(
    "Escolha uma das opções:\n[1] - Criar uma Tarefa\n[2]\
    - Visualizar Tarefas\n[3] - Marcar Tarefa como concluída\n\
    [4] - Excluir Tarefa\n[5] - Sair\n")

#Criar tarefa
conexao = sqlite3.conect('Tarefas.db')
cursor = conexao.cursor()
nova_tarefa = input("Escreva o nome da Tarefa:")
execute("INSERT INTO Tarefas VALUES (?, ?, ?)", (1, nova_tarefa, 0))
conexao.comit()
#Visualizar tarefas

#Marcar tarefa como concluída
#Excluir tarefa
#Sair