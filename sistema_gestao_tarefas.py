import os
from utilizador import Utilizador
from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas

# Classe que representa o sistema de gestão de tarefas
class SistemaGestaoTarefas:
    def __init__(self):
        self.utilizadores = {}
        self.utilizador_atual = None
        self.carregar_credenciais()

    # Método para carregar credenciais de utilizadores de um ficheiro
    def carregar_credenciais(self):
        if os.path.exists("utilizadores.txt"):
            with open("utilizadores.txt", "r") as file:
                for line in file:
                    nome_utilizador, senha = line.strip().split(":")
                    self.utilizadores[nome_utilizador] = Utilizador(nome_utilizador, senha)

    # Método para registrar um novo utilizador
    def registrar_utilizador(self, nome_utilizador, senha):
        if nome_utilizador not in self.utilizadores:
            self.utilizadores[nome_utilizador] = Utilizador(nome_utilizador, senha)
            self.salvar_credenciais()

    # Método para salvar credenciais de utilizadores em um ficheiro
    def salvar_credenciais(self):
        with open("utilizadores.txt", "w") as file:
            for nome_utilizador, utilizador in self.utilizadores.items():
                file.write(f"{nome_utilizador}:{utilizador.senha}\n")

    # Método para adicionar uma tarefa ao utilizador atual
    def adicionar_tarefa(self, tarefa):
        if self.utilizador_atual:
            if "default" not in self.utilizador_atual.listas:
                self.utilizador_atual.adicionar_lista("default")
            self.utilizador_atual.listas["default"].adicionar_tarefa(tarefa)
            self.salvar_tarefas()

    # Método para salvar tarefas em um ficheiro
    def salvar_tarefas(self):
        if self.utilizador_atual:
            with open(f"{self.utilizador_atual.nome}_lista_de_tarefas.txt", "w") as file:
                for lista in self.utilizador_atual.listas.values():
                    for tarefa in lista.tarefas:
                        file.write(f"{tarefa.titulo}:{tarefa.descricao}:{tarefa.data_de_criacao}:{tarefa.status}:{tarefa.categoria}\n")

    # Método para carregar tarefas de um ficheiro
    def carregar_tarefas(self):
        if self.utilizador_atual and os.path.exists(f"{self.utilizador_atual.nome}_lista_de_tarefas.txt"):
            with open(f"{self.utilizador_atual.nome}_lista_de_tarefas.txt", "r") as file:
                for line in file:
                    titulo, descricao, data_de_criacao, status, categoria = line.strip().split(":")
                    tarefa = Tarefa(titulo, descricao, data_de_criacao, status, categoria)
                    if "default" not in self.utilizador_atual.listas:
                        self.utilizador_atual.adicionar_lista("default")
                    self.utilizador_atual.listas["default"].adicionar_tarefa(tarefa)

    # Método para autenticar um utilizador
    def login(self, nome_utilizador, senha):
        if nome_utilizador in self.utilizadores and self.utilizadores[nome_utilizador].senha == senha:
            self.utilizador_atual = self.utilizadores[nome_utilizador]
            self.carregar_tarefas()  # Load tasks when the user logs in
            return True
        return False

    # Método para buscar uma tarefa pelo título
    def buscar_tarefa(self, titulo):
        if self.utilizador_atual:
            for lista in self.utilizador_atual.listas.values():
                tarefa = lista.buscar_tarefa(titulo)
                if tarefa:
                    return tarefa
        return None

    # Método para remover uma tarefa pelo título
    def remover_tarefa(self, titulo):
        if self.utilizador_atual:
            for lista in self.utilizador_atual.listas.values():
                lista.remover_tarefa(titulo)

    # Método para listar todas as tarefas do utilizador atual
    def listar_tarefas(self):
        if self.utilizador_atual:
            tarefas = []
            for lista in self.utilizador_atual.listas.values():
                tarefas.extend(lista.listar_tarefas())
            return tarefas

    # Método para filtrar tarefas por status
    def filtrar_tarefas(self, status):
        if self.utilizador_atual:
            tarefas_filtradas = []
            for lista in self.utilizador_atual.listas.values():
                tarefas_filtradas.extend([tarefa for tarefa in lista.listar_tarefas() if tarefa.status == status])
            return tarefas_filtradas