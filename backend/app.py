from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from flask import send_from_directory
from swagger_ui import api_doc
import os
from models import db, Pessoas, Filmes, Tasks
from rota import registros_bp  # corrigido também

# Informações da API
info = Info(title="Locadora de Filmes API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Configurar caminho do swagger.json
swagger_json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "swagger.json"))

# Expor a documentação Swagger em /swagger/
api_doc(app, config_path=swagger_json_path, url_prefix='/swagger', title='Documentação Swagger')

# Banco de dados
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'instance', 'site.db'))
os.makedirs(os.path.dirname(db_path), exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco e rotas
db.init_app(app)
app.register_api(registros_bp)

# Criar tabelas
with app.app_context():
    db.create_all()

# Iniciar app em modo debug (apenas se executar diretamente este arquivo)
if __name__ == "__main__":
    app.run(debug=True)
