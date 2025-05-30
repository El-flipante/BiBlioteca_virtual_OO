import pickle
from pathlib import Path

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def realizar_emprestimo(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        livro = next((l for l in self.livros if l.isbn == isbn), None)

        if usuario and livro:
            from .emprestimo import Emprestimo
            emprestimo = Emprestimo(usuario, livro)
            self.emprestimos.append(emprestimo)
            return emprestimo
        else:
            raise ValueError("Usuário ou livro não encontrado.")

    def salvar_dados(self, arquivo='biblioteca.pkl'):
        with open(arquivo, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def carregar_dados(arquivo='biblioteca.pkl'):
        if Path(arquivo).exists():
            with open(arquivo, 'rb') as f:
                return pickle.load(f)
        return Biblioteca()

