# Biblioteca Virtual - Projeto Livre OO (FGA/UnB 2025)

Este e um projeto desenvolvido para a disciplina de **Orientacao a Objetos**, como parte do **Projeto Livre** do semestre 01/2025.

---

## Objetivo

Simular uma **biblioteca virtual**, utilizando conceitos de Programacao Orientada a Objetos em Python. O sistema permite que usuarios (alunos e professores) realizem emprestimos de livros com prazos de devolucao distintos, controle de disponibilidade e armazenamento persistente.

---

##  Estrutura do Projeto

```
 projeto_biblioteca_virtual
    main.py
    README.md
    diagramas/
       diagrama_classes.png
       diagrama_casos_de_uso.png
      package/
       __init__.py
       usuario.py
       livro.py
       emprestimo.py
       biblioteca.py
```

---

##  Classes e Conceitos Usados

- **Heranca**: `Aluno` e `Professor` herdam de `Usuario`
- **Polimorfismo**: metodo `prazo_devolucao()` varia conforme o tipo de usuario
- **Composicao forte**: `Biblioteca` contem `Livros`, `Usuarios` e `Emprestimos`
- **Associacao fraca**: `Emprestimo` associa `Usuario` e `Livro`
- **Encapsulamento completo**
- **Serializacao de objetos**: com `pickle`

---

##  Casos de Uso

Veja o diagrama abaixo para entender como o sistema se comporta. (Disponivel em `/diagramas/diagrama_casos_de_uso.png`)

---
##  Como Executar

1. Clone o repositorio:
   ```bash
   git clone https://github.com/seu-usuario/biblioteca-virtual.git
   cd biblioteca-virtual
   ```

2. Execute o sistema:
   ```bash
   python main.py
   ```

3. O programa ira:
   - Criar usuarios e livros
   - Realizar emprestimos
   - Exibir prazos de devolucao
   - Salvar os dados em `biblioteca.pkl`

---

##  Serializacao

Os dados da biblioteca (livros, usuarios, emprestimos) sao salvos automaticamente no arquivo `biblioteca.pkl`.

---

##  Observacoes

Este projeto foi desenvolvido individualmente, conforme o edital do Projeto Livre da disciplina de POO da FGA/UnB. Diagramas de classes e casos de uso incluidos.
