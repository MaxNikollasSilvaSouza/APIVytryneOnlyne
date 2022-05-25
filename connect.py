from typing_extensions import Required
import mongoengine
from mongoengine import *
from mongoengine.connection import connect
from mongoengine.document import Document

#Conexão com o banco
mongoengine.connect(host = "mongodb+srv://teste1234:teste1234@testeezops.nsik1.mongodb.net/?retryWrites=true&w=majority")

#DOCUMENTO
class Produtos(Document):
    NOME = mongoengine.StringField()
    DESCRICAO = mongoengine.StringField()
    VALOR = mongoengine.FloatField()
    CODIGO = mongoengine.StringField()    
    CATEGORIA = mongoengine.StringField()       
    IMAGEM = mongoengine.StringField()

class Usuario(Document):
    EMAIL = mongoengine.StringField()
    SENHA = mongoengine.StringField()
