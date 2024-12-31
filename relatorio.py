# Classe para gerar relatórios de tarefas
class Relatorio():
    @staticmethod
    def gerar_relatorio(lista_tarefas, nome_arquivo):
        with open(nome_arquivo, "w") as file:
            for tarefa in lista_tarefas:
                file.write(str(tarefa) + "\n")