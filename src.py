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
    describe_tarefa = input("Escreva a descrição da Tarefa:")

    cursor.execute("INSERT INTO Tarefas (nome, describ, concluido) VALUES (?, ?, ?)",\
                    (nova_tarefa, describe_tarefa, 0))
    conexao.commit()
    conexao.close()


#Visualizar tarefas
def visualizar_tarefas():
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, describ, concluido FROM Tarefas")

    tarefas = cursor.fetchall()

    for tarefa in tarefas:
        nome, descricao, concluido = tarefa
        status = "Concluído" if concluido == 1 else "Pendente"
        print(f"Nome: {nome}, Descrição: {descricao}, Status: {status}")



    conexao.close()


#Marcar tarefa como concluída1
def concluir():
    
    nome = input('Digite o nome da tarefa que deseja concluir: ')
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE Tarefas SET concluido = ? WHERE nome = ?",\
                   (1,nome))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Tarefa '{nome}' concluída!")
    else:
        print(f"Nenhuma tarefa encontrada com o nome '{nome}'.")
    conexao.close()


#Excluir tarefa
def excluir():
  
    nome = input("Digite o nome da tarefa que deseja excluir: ")
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE nome = ?", (nome,))
    conexao.commit()
    conexao.close()

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
