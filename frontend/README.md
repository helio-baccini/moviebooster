# Frontend - Locadora de Filmes

**Frontend** da aplicação **Locadora de Filmes**, criado com **HTML**, **CSS** e **JavaScript**, responsável por exibir a interface de reserva de filmes e se comunicar com a API Flask no backend.

---

## Estrutura de Diretórios

frontend/
index.html                    # Página principal da aplicação
script.js                     # Lógica de interação com o backend (fetch, DOM)
Static/estilo.css             # Estilos visuais da aplicação
Static/imagens/               # Imagens utilizadas na interface

---

## Funcionalidades

- Formulário para cadastro de reservas de filmes
- Lista de registros exibidos dinamicamente
- Botões de **editar** (ícone de lápis) e **excluir** (ícone de lixeira)
- Imagens de filmes
- Design responsivo para melhor visualização em diferentes dispositivos

---

## Integração com Backend

O arquivo `script.js` realiza chamadas à API backend (Flask) por meio de `fetch()` para os seguintes endpoints:

- `GET /api/registros`
- `POST /api/registros`
- `PUT /api/registros/<id>`
- `DELETE /api/registros/<id>`

---

## Como Executar

1. Garanta que o backend Flask esteja rodando, abra o arquivo iniciar_projeto.bat
2. O arquivo `index.html` irá abrir automaticamente, caso não abrir, precisará abrir manualmente clicando 2x no arquivo ou pelo navegador.
3. A interface será carregada e se comunicará com a API.
