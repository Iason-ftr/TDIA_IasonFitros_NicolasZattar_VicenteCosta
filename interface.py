from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QInputDialog, QMessageBox, QLineEdit, QTextEdit, QDialog, QDialogButtonBox
from datetime import datetime

from tarefa import Tarefa
from sistema_gestao_tarefas import SistemaGestaoTarefas
from relatorio import Relatorio

# Classe principal da aplicação
class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tarefas")
        self.setGeometry(400, 400, 600, 300)
        self.sistema = SistemaGestaoTarefas()
        self.utilizador_atual = None
        self.initUI()

    # Método para inicializar a interface do usuário
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_initial_buttons()
        self.create_post_login_buttons()
        self.show_initial_buttons()

    # Método para criar os botões iniciais (Login e Registrar)
    def create_initial_buttons(self):
        self.label = QLabel("Bem-vindo ao Gestor de Tarefas")
        self.layout.addWidget(self.label)

        self.login_button = QPushButton("Login")
        self.layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Registar")
        self.layout.addWidget(self.register_button)
        self.register_button.clicked.connect(self.register)

    # Método para criar os botões após login
    def create_post_login_buttons(self):
        self.add_task_button = QPushButton("Adicionar Tarefa")
        self.layout.addWidget(self.add_task_button)
        self.add_task_button.clicked.connect(self.add_task)

        self.remove_task_button = QPushButton("Remover Tarefa")
        self.layout.addWidget(self.remove_task_button)
        self.remove_task_button.clicked.connect(self.remove_task)

        self.change_status_button = QPushButton("Mudar Status da Tarefa")
        self.layout.addWidget(self.change_status_button)
        self.change_status_button.clicked.connect(self.change_task_status)

        self.change_category_button = QPushButton("Alterar Categoria")
        self.change_category_button.clicked.connect(self.change_task_category)
        self.layout.addWidget(self.change_category_button)

        self.filter_tasks_button = QPushButton("Filtrar Tarefas")
        self.layout.addWidget(self.filter_tasks_button)
        self.filter_tasks_button.clicked.connect(self.filter_tasks)

        self.show_tasks_button = QPushButton("Mostrar Tarefas")
        self.layout.addWidget(self.show_tasks_button)
        self.show_tasks_button.clicked.connect(self.show_tasks)

        self.generate_report_button = QPushButton("Gerar Relatório")
        self.layout.addWidget(self.generate_report_button)
        self.generate_report_button.clicked.connect(self.generate_report)

    # Método para mostrar os botões iniciais
    def show_initial_buttons(self):
        self.label.show()
        self.login_button.show()
        self.register_button.show()
        self.add_task_button.hide()
        self.remove_task_button.hide()
        self.change_status_button.hide()
        self.change_category_button.hide()
        self.filter_tasks_button.hide()
        self.show_tasks_button.hide()
        self.generate_report_button.hide()
        
    # Método para mostrar os botões após login
    def show_post_login_buttons(self):
        self.label.hide()
        self.login_button.hide()
        self.register_button.hide()
        self.add_task_button.show()
        self.remove_task_button.show()
        self.change_status_button.show()
        self.change_category_button.show()
        self.filter_tasks_button.show()
        self.show_tasks_button.show()
        self.generate_report_button.show()

    # Método para fazer login do utilizador
    def login(self):
        nome_utilizador, ok1 = QInputDialog.getText(self, "Login", "Nome do utilizador:")
        if ok1:
            senha_dialog = QInputDialog(self)
            senha_dialog.setWindowTitle("Login")
            senha_dialog.setLabelText("Senha:")
            senha_dialog.setTextEchoMode(QLineEdit.Password)
            senha_dialog.exec_()
            senha = senha_dialog.textValue()
            if self.sistema.login(nome_utilizador, senha):
                self.utilizador_atual = nome_utilizador
                QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
                self.show_post_login_buttons()
            else:
                QMessageBox.warning(self, "Erro", "Nome de utilizador ou senha incorretos.")

    # Método para registar um novo utilizador
    def register(self):
        nome_utilizador, ok1 = QInputDialog.getText(self, "Registar", "Nome do utilizador:")
        if ok1 and nome_utilizador:
            senha, ok2 = QInputDialog.getText(self, "Registar", "Senha:", QLineEdit.Password)
            if ok2 and senha:
                self.sistema.registrar_utilizador(nome_utilizador, senha)
                QMessageBox.information(self, "Sucesso", "Utilizador registado com sucesso!")

    # Método para adicionar uma tarefa
    def add_task(self):
        titulo, ok = QInputDialog.getText(self, 'Adicionar Tarefa', 'Nome da Tarefa:')
        if ok and titulo:
            descricao, ok = QInputDialog.getText(self, 'Adicionar Tarefa', 'Descrição da Tarefa:')
            if not ok:
                descricao = ""
            categoria, ok = QInputDialog.getText(self, 'Adicionar Tarefa', 'Categoria da Tarefa:')
            if not ok:
                categoria = "Sem Categoria"
            data_de_criacao = datetime.now().strftime("%d-%m-%Y")
            tarefa = Tarefa(titulo, descricao, data_de_criacao, "Pendente", categoria)
            self.sistema.adicionar_tarefa(tarefa)
            QMessageBox.information(self, 'Sucesso', 'Tarefa adicionada com sucesso!')

    # Método para remover uma tarefa
    def remove_task(self):
        titulo, ok = QInputDialog.getText(self, 'Remover Tarefa', 'Nome da Tarefa:')
        if ok and titulo:
            self.sistema.remover_tarefa(titulo)
            self.sistema.salvar_tarefas()
            QMessageBox.information(self, 'Sucesso', f'Tarefa "{titulo}" removida com sucesso!')

    # Método para mudar o status de uma tarefa
    def change_task_status(self):
        titulo, ok = QInputDialog.getText(self, 'Mudar Status', 'Nome da Tarefa:')
        if ok and titulo:
            tarefa = self.sistema.buscar_tarefa(titulo)
            if tarefa:
                tarefa.mudar_status()
                self.sistema.salvar_tarefas()
                QMessageBox.information(self, 'Sucesso', f'Status da tarefa "{titulo}" mudado para {tarefa.status}!')
            else:
                QMessageBox.warning(self, 'Erro', 'Tarefa não encontrada!')

    # Método para alterar a categoria de uma tarefa
    def change_task_category(self):
        titulo, ok = QInputDialog.getText(self, 'Alterar Categoria', 'Nome da Tarefa:')
        if ok and titulo:
            tarefa = self.sistema.buscar_tarefa(titulo)
            if tarefa:
                nova_categoria, ok = QInputDialog.getText(self, 'Alterar Categoria', 'Nova Categoria:')
                if ok and nova_categoria:
                    tarefa.categoria = nova_categoria
                    self.sistema.salvar_tarefas()
                    QMessageBox.information(self, 'Sucesso', f'Categoria da tarefa "{titulo}" alterada para {nova_categoria}!')
            else:
                QMessageBox.warning(self, 'Erro', 'Tarefa não encontrada!')

    # Método para filtrar tarefas por status
    def filter_tasks(self):
        if not self.utilizador_atual:
            QMessageBox.warning(self, "Erro", "Faça login primeiro para filtrar tarefas.")
            return

        status, ok = QInputDialog.getText(self, 'Filtrar Tarefas', 'Status (Pendente/Concluido):')
        if ok and status:
            tarefas = self.sistema.filtrar_tarefas(status)
            QMessageBox.information(self, 'Tarefas Filtradas', '\n'.join([str(tarefa) for tarefa in tarefas]))

    # Método para mostrar todas as tarefas
    def show_tasks(self):
        if not self.utilizador_atual:
            QMessageBox.warning(self, "Erro", "Faça login primeiro para ver as tarefas.")
            return

        tarefas = self.sistema.listar_tarefas()
        self.show_tasks_dialog(tarefas)

    # Método para gerar relatório
    def generate_report(self):
        if not self.utilizador_atual:
            QMessageBox.warning(self, "Erro", "Faça login primeiro para gerar um relatório.")
            return

        nome_arquivo, ok = QInputDialog.getText(self, 'Gerar Relatório', 'Nome do Arquivo:')
        if ok and nome_arquivo:
            nome_arquivo += ".txt"
            tarefas = self.sistema.listar_tarefas()
            Relatorio.gerar_relatorio(tarefas, nome_arquivo)
            QMessageBox.information(self, 'Sucesso', 'Relatório gerado com sucesso!')

    # Método para mostrar o diálogo de tarefas
    def show_tasks_dialog(self, tarefas):
        dialog = QDialog(self)
        dialog.setWindowTitle("Tarefas")
        dialog.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        tasks_display = QTextEdit()
        tasks_display.setReadOnly(True)
        tasks_display.setText('\n'.join([str(tarefa) for tarefa in tarefas]))
        layout.addWidget(tasks_display)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)

        dialog.setLayout(layout)
        dialog.exec_()