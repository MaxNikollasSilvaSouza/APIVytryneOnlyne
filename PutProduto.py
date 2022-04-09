import connect as conx
#FUNÇÃO DE ATUALIZAR VALORES
def atualizar(name, desc,valor,code,categ,img):
    conx.Produtos.objects(CODIGO = code).update_one(NOME = name)
    conx.Produtos.objects(CODIGO = code).update_one(DESCRICAO = desc)
    conx.Produtos.objects(CODIGO = code).update_one(VALOR = valor)
    #conx.Colecao.objects(CODIGO = code).update_one(CODIGO = code)  NÃO TEM COMO ALTERAR O NOME PQ O NOME É O IDENTIFICADOR PRINCIPAL
    conx.Produtos.objects(CODIGO = code).update_one(CATEGORIA = categ)
    conx.Produtos.objects(CODIGO = code).update_one(IMAGEM = img)