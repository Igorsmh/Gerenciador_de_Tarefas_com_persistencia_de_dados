from src import *



if __name__ == "__main__":
    clean()
    apresentacao()
    criar_base()
    while True:
        menu()
        input("Aperte ENTER para voltar ao menu...\n")
        clean()
