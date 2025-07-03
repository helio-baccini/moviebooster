
# Projeto Flask - Locadora de Filmes

Este é um projeto básico de uma API e interface para uma **Locadora de Filmes**, desenvolvido em **Python Flask**, com integração ao **Swagger** para documentação da API e uso de **SQLite** como banco de dados local.

---

## Estrutura de Arquivos

app.py               # Arquivo principal que inicia a aplicação
models.py            # Modelos de dados (SQLAlchemy)
rota.py              # Rotas/Endpoints da API
schemas.py           # Schemas de validação e resposta
swagger.json         # Definição manual da documentação Swagger (caso necessário)
__init__.py          # Inicialização do módulo (pode configurar o app aqui também)
instance/site.db     # Banco de dados SQLite
__pycache__          # Arquivos compilados do Python (gerados automaticamente)

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.11+
- Virtualenv (opcional, mas recomendado)

### Instalação

1. Clone ou extraia o projeto em uma pasta local:
   ```bash
   git clone <repositorio> ou extraia o ZIP
   cd nome_da_pasta
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   python app.py
   ```

---

## Documentação da API (Swagger)

Após iniciar o servidor, acesse a pagina e clica no menu **API** da pagina index.html ou pode entrar pelo link **http://127.0.0.1:5000/swagger**, ambus entrarão na documentação do Swagger, 

Lá você verá a interface do Swagger com todos os endpoints da API.

## GET
1 - Na homepage, abre a aba **GET** em azul
2 - Clique em Try it out
3 - Clique em execute
-- No Response Body terá os registros cadastrados
   **Data lançamento**
   **Descrição**
   **Nome**
   **Registro_id**
   **Titulos**

## POST
1 - Na homepage, abre a aba **POST** em verde
2 - Clique em Try it out
3 - Clique em execute
-- No Response Body poderá cadastrar reservas
   **Data lançamento**     Ano do lançamento do filme
   **Descrição**           Alugar / Reservar    
   **Nome**                Nome da pessoa que deseja realizar o aluguel ou reserva          
   **Titulos**             Nome do filme

## DELETE
1 - Na homepage, abre a aba **DELETE** em vermelho
2 - Clique em Try it out
3 - Copie o registro_id conforme descrito na aba GET
4 - Clique em execute, o registro será deletado e ao atualizar a pagina index a reserva não aparecerá

## PUT
1 - Na homepage, abre a aba **PUT** em laranja
2 - Clique em Try it out
3 - Copie o registro_id conforme descrito na aba GET
4 -No campo Edite Value poderá fazer a alteração
5 Clique em execute e o registro será alterado
---

## Banco de Dados

- O banco de dados é um arquivo SQLite localizado em:

  instance/site.db

- É criado automaticamente na primeira execução.

---

## ✨ Funcionalidades

- Cadastrar registros com:
  - Nome do cliente
  - Título do filme
  - Ano de lançamento
  - Tipo de tarefa (Alugar/Reservar)
- Listar todos os registros
- Buscar registros
- Atualizar ou excluir
