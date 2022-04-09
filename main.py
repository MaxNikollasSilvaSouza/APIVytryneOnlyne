from flask import Flask, request
from flask.scaffold import F
import PostProduto as P
import GetProduto as G
import DeleteProduto as D
import PutProduto as A
import Login as L


#ESTE CÓDIGO MAIN É RESPONSÁVEL APENAS PELAS ROTAS E DIRECIONAMENTOS!

app = Flask(__name__)

#DEFINE A ROTA E O MÉTODO
@app.route("/", methods=['POST'])
def get_repository():
    try:
        produto = request.json
        dic = G.listar(produto['NOME'])
        print(dic)

        return dic
    except Exception as e:
       return str(e)
       
@app.route("/cadastrar", methods=['POST'])
def post_repository():
    try:
        produto = request.json
        P.salvar(produto['NOME'],produto['DESCRICAO'], produto['VALOR'],produto['CODIGO'],produto['CATEGORIA'],produto['IMAGEM'])
    
        return "Produto cadastrado!"
    except Exception as e:
       return str(e)

@app.route("/deletar", methods=['DELETE'])
def delete_repository():
    try:
        produto = request.json
        D.deletar(produto['CODIGO'])

        return "Produto deletado!"
    except Exception as e:
       return str(e)

@app.route("/atualizar", methods=['PUT'])
def atualizar_repository():
    try:
        produto = request.json
        A.atualizar(produto['NOME'],produto['DESCRICAO'], produto['VALOR'],produto['CODIGO'],produto['CATEGORIA'],produto['IMAGEM'])

        return "Produto atualizado!"
    except Exception as e:
       return str(e)

@app.route("/logar", methods=['POST'])
def logar_repository():
    try:
        usuario = request.json
        resultado = L.verificacao(usuario['EMAIL'],usuario['SENHA'])

        return resultado
    except Exception as e:
       return str(e)

@app.route("/deluser", methods=['POST'])
def del_user_repository():
    try:
        usuario = request.json
        resultado = L.deletar(usuario['EMAIL'],usuario['SENHA'])

        return resultado
    except Exception as e:
       return str(e)

@app.route("/salvaruser", methods=['POST'])
def salvar_user_repository():
    try:
        usuario = request.json
        resultado = L.salvar(usuario['EMAIL'],usuario['SENHA'])

        return resultado
    except Exception as e:
       return str(e)