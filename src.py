from rich import print
import sqlite3


escolha = input(
"Escolha uma das opções:\n[1] - Criar uma Tarefa\n\
[2] - Visualizar Tarefas\n[3] - Marcar Tarefa como concluída\n\
[4] - Excluir Tarefa\n[5] - Sair\n")

#Criar tarefa
def criar_tarefa():

    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    nova_tarefa = input("Escreva o nome da Tarefa:")

    cursor.execute("INSERT INTO Tarefas (nome, concluido) VALUES (?, ?)", (nova_tarefa, 0))
    conexao.commit()


#Visualizar tarefas
def visualizar_tarefas():
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM Tarefas")
    print(cursor.fetchall())


#Marcar tarefa como concluída1
def concluir():
    
    nome = input('Digite o nome da tarefa que deseja concluir: ')
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE Tarefas SET concluido = ? WHERE nome = ?",(1,nome))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Tarefa '{nome}' concluída!")
    else:
        print(f"Nenhuma tarefa encontrada com o nome '{nome}'.")


#Excluir tarefa
def excluir():
    pass

#Sair
def sair():
    print("Saindo...")
    exit()

opcoes = {'1': criar_tarefa, 
        '2': visualizar_tarefas, 
        '3': concluir,
        '4': excluir,
        '5': sair }

try:
    opcoes[escolha]()
except KeyError:
    print("Opção inválida. Tente novamente.")
