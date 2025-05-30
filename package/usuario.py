from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome: str, id_usuario: int):
        self.nome = nome
        self.id_usuario = id_usuario

    @abstractmethod
    def prazo_devolucao(self) -> int:
        """Retorna o prazo de devolução em dias."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome} (ID: {self.id_usuario})"

class Aluno(Usuario):
    def prazo_devolucao(self) -> int:
        return 7  # dias

class Professor(Usuario):
    def prazo_devolucao(self) -> int:
        return 14  # dias

