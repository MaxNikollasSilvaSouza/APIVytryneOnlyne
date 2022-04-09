import connect as conx

#DELETAR DOCUMENTO
def deletar(identificacao): 
    item = conx.Produtos.objects(CODIGO = identificacao)
    item.delete()