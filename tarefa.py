# Classe que representa uma tarefa
class Tarefa:
    def __init__(self, titulo, descricao, data_de_criacao, status="Pendente", categoria=None):
        self.titulo = titulo
        self.descricao = descricao
        self.data_de_criacao = data_de_criacao
        self.status = status
        self.categoria = categoria

    # Método para mudar o status da tarefa
    def mudar_status(self):
        if self.status == "Pendente":
            self.status = "Concluido"
        else:
            self.status = "Pendente"

    # Método para representar a tarefa como string
    def __str__(self):
        return (f"Título: {self.titulo}\n"
                f"Descrição: {self.descricao}\n"
                f"Categoria: {self.categoria}\n"
                f"Status: {self.status}\n"
                f"Data de Criação: {self.data_de_criacao}\n")