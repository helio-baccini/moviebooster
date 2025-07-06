#  Movie Booster
Sistema simples de **Reserva de Filmes**
API desenvolvido como projeto final Sprint: Desenvolvimento Full Stack Básico

## Tecnologias Utilizadas
   **Flask** como microframework web escrito em Python
   **SQLite** para banco de dados e armazenar informações
   **CRUD** para as operaçoes de Criar, Ler, Atualizar e Deletar registros
   **HTML/CSS** para a criação de pagina

---

## Estrutura do Projeto
   **app.py** Arquivo principal que inicializa a aplicação Flask
   **models.py** Define os modelos de dados com SQLAlchemy
   **instance/site.db** Banco de dados SQLite
   **static/estilo.css** Arquivo CSS para estilo das páginas
   **templates/index.html** Página HTML principal
   **templates/editar.html** Pagina HTML pra editar os dados cadastrados
   **requirements.txt** Lista de dependências
   **.venv/** Ambiente virtual Python

---

##  Funcionalidades

-  Cadastro, listagem, edição e exclusão de reservas de filmes
-  Filtro de busca por título (nome do filme)
-  API RESTful com documentação via **Swagger**, utilizando o **GET, POST, DELTE, PUT**
-  Integração com banco de dados **SQLite**
-  Front-end responsivo com HTML, CSS e JavaScript

---

##  Requisitos

- Python **3.10** ou superior
- `pip` instalado (normalmente já vem com o Python)

---

##  Como executar o projeto

###  Etapa 1: Back-end (API Flask)

1. **Clone ou descompacte o projeto**

2. Abra um terminal na pasta raiz do projeto (`MovieBooster`).

3. Crie e ative o ambiente virtual (opcional, mas recomendado).

3.1 Alternativa: você pode abrir o arquivo **inicio_projeto.bat**, ele criará um ambiente virtual temporário no windows e abrirá automaticamente a pagina index.html.

3.2 Caso ocorra erro do Windows Defener SmartScrim é porque o arquivo não é assinado por uma fonte reconhecida.
      Para continuar com segurança:
         - Clique em Mais informações (embaixo da mensagem).
         - Em seguida, clique no botão Executar assim mesmo.

4. Caso o index.html não abrir automaticamente, entre no  arquivo frontend e abra a pagina index.html.

5. O programa ira funcionar normalmente

###  Etapa 2: Front-end (HTML, CSS, JS)

1. Abra na pasta frontend

2. Abra o arquivo index.html 

---

## Apresentação do projeto
Link: https://youtu.be/zgTbkFzNSLA?si=Xkn11xdlMgCp8mfA
