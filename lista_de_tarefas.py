from tarefa import Tarefa

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    # Método para adicionar uma nova tarefa
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    # Método para remover uma tarefa existente
    def remover_tarefa(self, titulo):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.titulo != titulo]

    # Método para listar todas as tarefas
    def listar_tarefas(self):
        return self.tarefas

    # Método para buscar uma tarefa pelo título
    def buscar_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                return tarefa
        return None