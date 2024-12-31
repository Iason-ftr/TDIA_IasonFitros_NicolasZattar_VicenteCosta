from lista_de_tarefas import ListaDeTarefas

class Utilizador:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.listas = {}

    # Método para adicionar uma nova lista de tarefas
    def adicionar_lista(self, nome_lista):
        if nome_lista not in self.listas:
            self.listas[nome_lista] = ListaDeTarefas()

    # Método para alterar a senha do utilizador
    def alterar_senha(self, nova_senha):
        self.senha = nova_senha

    # Método para salvar as credenciais do utilizador em um ficheiro
    def salvar_credenciais(self):
        with open("utilizadores.txt", "a") as file:
            file.write(f"{self.nome}:{self.senha}\n")