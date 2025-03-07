from rich.table import  Table
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print
import sqlite3



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
    cursor.execute("SELECT id, nome, describ, concluido FROM Tarefas")

    tarefas = cursor.fetchall()

    console = Console()

    tabela = Table(title="Tarefas")
    tabela.add_column("ID", justify="left", style="cyan", no_wrap=True)
    tabela.add_column("Nome", justify="left", style="cyan", no_wrap=True)
    tabela.add_column("Descrição", justify="left", style="cyan", no_wrap=True)
    tabela.add_column("Status", justify="left", style="cyan", no_wrap=True)


    for tarefa in tarefas:
        id, nome, descricao, concluido = tarefa
        
        if concluido == 1:
            status = "[green]Concluído :white_check_mark:[/green]"
            tabela.add_row(str(id), nome, descricao, status)
            
        else:
            status = "[red]Pendente...[/red]"
            tabela.add_row(str(id), nome, descricao, status)

    console.print(tabela)
    
    conexao.close()


#Marcar tarefa como concluída
def concluir():
    
    id = input('Digite o id da tarefa que deseja concluir: ')
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE Tarefas SET concluido = ? WHERE id = ?",\
                   (1,id))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Tarefa '{id}' concluída!")
    else:
        print(f"Nenhuma tarefa encontrada com o nome '{id}'.")
    
    visualizar_tarefas()
    print("\n")
    conexao.close()


#Excluir tarefa
def excluir():
  
    visualizar_tarefas()
    print("\n")
    id = input("Digite o id da tarefa que deseja excluir: ")
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id,))
    if cursor.rowcount > 0:
        print(f"Tarefa '{id}' excluida!\n")
    else:
        print(f"Nenhuma tarefa encontrada com o nome '{id}'.\n")
    
    conexao.commit()
    visualizar_tarefas()

    conexao.close()

#Sair
def sair():
    print("Saindo...")
    exit()



def criar_base():
    conexao = sqlite3.connect('tarefas.db')
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tarefas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    nome VARCHAR(80),
    describ VARCHAR (200),
    concluido BOOLEAN DEFAULT 0
    )
    """)
    
    conexao.commit()


def menu():


    print("[bold] Escolha uma das opções:\n[1] - Criar uma Tarefa\n\
[2] - Visualizar Tarefas\n[3] - Marcar Tarefa como concluída\n\
[4] - Excluir Tarefa\n[5] - Sair\n[/]")
    
    escolha = input("")


    opcoes = {'1': criar_tarefa,
            '2': visualizar_tarefas, 
            '3': concluir,
            '4': excluir,
            '5': sair }

    try:
        opcoes[escolha]()
    except KeyError:
        print("Opção inválida. Tente novamente.")



def apresentacao():
   
    console = Console()
    titulo = 'Bem-vindo(a) ao Gerenciador de Tarefas!'
    # Cria um texto com o título, centralizado e com tamanho grande
    texto_titulo = Text(titulo, justify="center", style="bold magenta")
    
    # Cria um painel com o título
    painel = Panel(
        texto_titulo,
        title="Gerenciador de Tarefas",
        title_align="center",
        border_style="green"
    )
    
    # Imprime o painel no console
    console.print(painel)
    print('\n')


def clean():
    Console().clear()


# TODO permitir multiplas adições, exclusões, conclusões de uma vez
# TODO Resetar o indice das tarefas pos exclusão das mesmas