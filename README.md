# RPG Character Generator

## Contexto da Aplicação

O **RPG Character Generator** é uma aplicação que permite aos usuários criar e gerenciar personagens para jogos de RPG. A aplicação fornece uma interface para definir atributos dos personagens, como raça, classe, nível e habilidades. O objetivo é facilitar a criação de personagens de forma rápida e intuitiva, permitindo que os jogadores se concentrem na narrativa e na jogabilidade.

## Stack

A aplicação é construída utilizando as seguintes tecnologias:

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework web moderno e rápido para construir APIs com Python.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interagir com o banco de dados.
- **Alembic**: Ferramenta de migração de banco de dados para SQLAlchemy.
- **SQLite**: Banco de dados leve utilizado para armazenar os dados dos personagens.
- **Pydantic**: Para validação de dados e definição de modelos.
- **pytest**: Para testes automatizados.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o seguinte instalado:

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## Como Rodar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu_usuario/rpg-character-generator.git
   cd rpg-character-generator
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:

   Certifique-se de que o arquivo de configuração do banco de dados está correto. O Alembic deve estar configurado para apontar para o seu banco de dados.

5. **Execute as migrações**:

   ```bash
   alembic upgrade head
   ```

6. **Inicie a aplicação**:

   ```bash
   uvicorn app.main:app --reload
   ```

   A aplicação estará disponível em `http://127.0.0.1:8000`.

7. **Acesse a documentação da API**:

   A documentação interativa da API pode ser acessada em `http://127.0.0.1:8000/docs`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
