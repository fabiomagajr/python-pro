import json
from flask import Flask, jsonify, request
app = Flask(__name__)

str_API='/api/v1/'

ARQUIVO_JSON='usuarios.json'

def carregar_usuarios():
    try:
        with open(ARQUIVO_JSON,'r',encoding='utf-8')as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
def salvar_usuarios(usuarios):
    with open(ARQUIVO_JSON,'w',encoding='utf=8')as f:
        json.dump(usuarios,f,indent=4,ensure_ascii=False)

@app.route(str_API)
def home():
    return jsonify({'Mensagem':'API OK!'})

@app.route(str_API+'usuarios',methods=['GET'])
def get_usuarios():
    return jsonify(carregar_usuarios())

@app.route(str_API+'usuario/<int:id>',methods=['GET'])
def get_usuario(id):
    usuarios=carregar_usuarios()
    usuario=next((u for u in usuarios if u["id"]==id),None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro":"Usuário não encontrado"}),404

@app.route(str_API+'usuarios',methods=['POST'])
def add_usuarios():
    usuarios=carregar_usuarios()
    dados = request.get_json()
    if not dados or "nome" not in dados or "idade" not in dados:
        return jsonify({"erro":"Dados inválidos"}),400
    
    novo_usuario = {
        "id":usuarios[-1]["id"]+1 if usuarios else 1,
        "nome": dados["nome"],
        "idade": dados["idade"]
    }
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    return jsonify(novo_usuario),201

@app.route(str_API+'usuarios/<int:id>',methods=['PUT'])
def update_usuario(id):
    usuarios=carregar_usuarios()
    dados=request.get_json()
    usuario = next((u for u in usuarios if u["id"]==id),None)
    
    if not usuario:
        return jsonify({"erro":"Usuário não encontrado"}),404
    
    if "nome" in dados:
        usuario["nome"] = dados["nome"]
    if "idade" in dados:
        usuario["idade"]=dados["idade"]
        
    salvar_usuarios(usuarios)
    return jsonify(usuario)

@app.route(str_API+'usuarios/<int:id>',methods=['DELETE'])
def delete_usuario(id):
    usuarios=carregar_usuarios()
    usuario=next((u for u in usuarios if u["id"]==id),None)
    
    if not usuario:
        return jsonify({"erro":"Usuário não encontrado"}),404
    
    usuarios.remove(usuario)
    salvar_usuarios(usuarios)
    return jsonify({"mensagem":"Usuário removido com sucesso"}),200


if __name__ == '__main__':
    app.run(debug=True)