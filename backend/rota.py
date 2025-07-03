from flask_openapi3 import APIBlueprint, Tag
from flask import request, jsonify
import uuid
from models import db, Pessoas, Filmes, Tasks
from pydantic import BaseModel

class RegistroPath(BaseModel):
    registro_id: str

# Criação do Blueprint para registros
registros_bp = APIBlueprint('registros', __name__, url_prefix="/api")
registro_tag = Tag(name="Registro", description="Operações de CRUD para registros de filmes")

# Rota para redirecionar a raiz da API para a documentação Swagger
# GET
@registros_bp.get("/registros", tags=[registro_tag])
def listar_registros():
    titulo_filtro = request.args.get("titulo", "")
    registros = []
    pessoas = Pessoas.query.all()
    filmes = Filmes.query.all()
    tasks = Tasks.query.all()

    for pessoa in pessoas:
        reg_id = pessoa.registro_id
        filme = next((f for f in filmes if f.registro_id == reg_id), None)
        task = next((t for t in tasks if t.registro_id == reg_id), None)
        if filme and task:
            if titulo_filtro.lower() in filme.titulo.lower():
                registros.append({
                    "registro_id": reg_id,
                    "nome": pessoa.nome,
                    "titulo": filme.titulo,
                    "data_lancamento": filme.data_lancamento,
                    "description": task.description
                })
    return jsonify(registros)

# Rota para redirecionar a raiz da API para a documentação Swagger
# POST
@registros_bp.post("/registros", tags=[registro_tag])
def criar_registro():
    dados = request.json
    reg_id = str(uuid.uuid4())
    titulo = dados.get("titulo", "").strip().lower()
    descricao = dados.get("description", "").strip().lower()

    if titulo in ["alugar", "reservar"]:
        return jsonify({"erro": "Este título de filme não pode ser 'Alugado' ou 'Reservado'."}), 400

    duplicado = db.session.query(Filmes, Tasks)\
        .join(Tasks, Filmes.registro_id == Tasks.registro_id)\
        .filter(Filmes.titulo.ilike(dados["titulo"]), Tasks.description.ilike(dados["description"]))\
        .first()
    if duplicado:
        return jsonify({"erro": "Este filme já está sendo alugado ou reservado!"}), 400

    pessoa = Pessoas(nome=dados["nome"], registro_id=reg_id)
    filme = Filmes(titulo=dados["titulo"], data_lancamento=dados["data_lancamento"], registro_id=reg_id)
    task = Tasks(description=dados["description"], registro_id=reg_id)
    db.session.add_all([pessoa, filme, task])
    db.session.commit()
    return jsonify({"mensagem": "Registro criado com sucesso."}), 201

# Rota para redirecionar a raiz da API para a documentação Swagger
# PUT
@registros_bp.put("/registros/<registro_id>", tags=[registro_tag])
def editar_registro(path: RegistroPath):
    registro_id = path.registro_id
    dados = request.json
    pessoa = Pessoas.query.filter_by(registro_id=registro_id).first()
    filme = Filmes.query.filter_by(registro_id=registro_id).first()
    task = Tasks.query.filter_by(registro_id=registro_id).first()
    if not (pessoa and filme and task):
        return jsonify({"erro": "Registro não encontrado."}), 404

    titulo_novo = dados.get("titulo", "").strip().lower()
    if titulo_novo in ["alugar", "reservar"]:
        return jsonify({"erro": "O título do filme não pode ser 'Alugar' ou 'Reservar'."}), 400

    duplicado = db.session.query(Filmes, Tasks)\
        .join(Tasks, Filmes.registro_id == Tasks.registro_id)\
        .filter(Filmes.titulo.ilike(dados["titulo"]), Tasks.description.ilike(dados["description"]), Filmes.registro_id != registro_id)\
        .first()
    if duplicado:
        return jsonify({"erro": "Já existe outro registro com o mesmo título e condição."}), 400

    pessoa.nome = dados["nome"]
    filme.titulo = dados["titulo"]
    filme.data_lancamento = dados["data_lancamento"]
    task.description = dados["description"]
    db.session.commit()
    return jsonify({"mensagem": "Registro atualizado com sucesso."})

# Rota para redirecionar a raiz da API para a documentação Swagger
# DELETE
@registros_bp.delete("/registros/<registro_id>", tags=[registro_tag])
def deletar_registro(path: RegistroPath):
    registro_id = path.registro_id
    pessoa = Pessoas.query.filter_by(registro_id=registro_id).first()
    filme = Filmes.query.filter_by(registro_id=registro_id).first()
    task = Tasks.query.filter_by(registro_id=registro_id).first()
    if not (pessoa and filme and task):
        return jsonify({"erro": "Registro não encontrado."}), 404

    db.session.delete(pessoa)
    db.session.delete(filme)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"mensagem": "Registro excluído com sucesso."})

