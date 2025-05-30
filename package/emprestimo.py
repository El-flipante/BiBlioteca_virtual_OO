from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, usuario, livro):
        if not livro.disponivel:
            raise ValueError("Livro indisponível para empréstimo.")

        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + timedelta(days=usuario.prazo_devolucao())

        livro.emprestar()

    def devolver_livro(self):
        self.livro.devolver()

    def __str__(self):
        return (
            f"{self.usuario.nome} emprestou '{self.livro.titulo}' em {self.data_emprestimo.strftime('%d/%m/%Y')}.\n"
            f"Devolver até: {self.data_devolucao.strftime('%d/%m/%Y')}."
        )
