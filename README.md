# Resolução de Questões para Teste Prático de Estágio

Este repositório contém as resoluções de questões propostas para o teste prático de seleção para vagas de estágio. As soluções foram implementadas em **Python** como linguagem de programação, utilizando o **Poetry** como gerenciador de dependências e **Docker** como ambiente de execução

## Requisitos

Os requisitos para o projeto são:

- [Docker](https://www.docker.com/) - Ambiente de execução
- [Python](https://www.python.org/) - Linguagem de programação **v3.12.4**
- [Poetry](https://python-poetry.org/) - Gerenciador de dependêndias
- [Pytest](https://docs.pytest.org/en/stable/) - Framework de testes para Python
- [Pytest-cov](https://pypi.org/project/pytest-cov/) - Plugin para o pytest
- [Ruff](https://docs.astral.sh/ruff/) - Linter e formatador python
- [Taskipy](https://github.com/taskipy/taskipy) - Biblioteca Python para execução de tarefas

## Instruções para Execução

Para facilitar a execução e garantir a consistência do ambiente, as resoluções foram preparadas para serem executadas dentro de um container Docker. Siga os passos abaixo para configurar e rodar o ambiente:

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/leopoldocouto/teste_pratico_target_sistemas.git
    cd teste_pratico_target_sistemas
    ```

2. **Construa a imagem Docker**:

    No diretório raiz do projeto, execute o comando abaixo para construir a imagem Docker:

    ```bash
    docker build -t "teste_pratico_leopoldo_couto" .
    ```

3. **Docker instalando as dependências**:

    Dentro do container, as dependências serão gerenciadas pelo Poetry. O poetry instala todas as dependências listadas no arquivo `pyproject.toml`, executando<br><br>

4. **Execute as soluções**:

    Após a instalação das dependências, você pode executar os scripts de solução das questões. Por exemplo, para rodar todos os testes:

    ```bash
    docker run teste_pratico_leopoldo_couto
    ```

    Para rodar teste da questão 1:
    ```bash
    docker run teste_pratico_leopoldo_couto pytest -vv tests/test_questao1.py
    ```

    Substitua `questao_1.py` pelo nome do arquivo correspondente à questão que deseja executar.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

>teste_pratico_target_sistemas/ 
│ 
├── teste_pratico_target_sistemas # Diretório com as resoluções das questões
│ └── questao1.py
│ └── questao2.py
│ └── questao3.py
│ └── questao4.py
│ └── questao5.py
├── tests # Diretório com os testes das resoluções das questões
│ └── test_questao1.py
│ └── test_questao2.py
│ └── test_questao3.py
│ └── test_questao4.py
│ └── test_questao5.py
├── .gitignore  # Arquivos e pastas ignorados pelo Git
├── .pythonversion  # Arquivos com a versão usado do Python
├── Dockerfile # Dockerfile com as instruções para construir a imagem 
├── README.md # Documentação do projeto 
├── poetry.lock # Arquivo de configuração do Poetry e dependências 
└── pyproject.toml # Arquivo de configuração do Poetry e dependências 

Este README.md fornece instruções claras sobre como o avaliador deve configurar o ambiente, instalar as dependências e executar as soluções das questões utilizando Docker e Poetry.
