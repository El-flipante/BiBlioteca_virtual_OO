from package.biblioteca import Biblioteca
from package.usuario import Aluno, Professor
from package.livro import Livro

def main():
    # Carrega biblioteca salva (ou cria nova)
    biblioteca = Biblioteca.carregar_dados()

    # Criação de usuários
    aluno1 = Aluno("Carlos Silva", 1)
    professor1 = Professor("Dra. Helena Costa", 2)

    # Criação de livros
    livro1 = Livro("1984", "George Orwell", "123")
    livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "456")

    # Adiciona à biblioteca
    biblioteca.adicionar_usuario(aluno1)
    biblioteca.adicionar_usuario(professor1)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Realiza empréstimos
    emprestimo1 = biblioteca.realizar_emprestimo(1, "123")  # Carlos pega "1984"
    emprestimo2 = biblioteca.realizar_emprestimo(2, "456")  # Helena pega "O Pequeno Príncipe"

    # Exibe informações dos empréstimos
    print(emprestimo1)
    print(emprestimo2)

    # Salva estado da biblioteca
    biblioteca.salvar_dados()

if __name__ == "__main__":
    main()
