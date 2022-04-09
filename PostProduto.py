import connect as conx



#inserindo valores
def salvar(name, desc,valor,code,categ,img):
    
    try:
        #SALVANDO DOCUMENTO
        variavelqq = conx.Produtos(NOME = name, DESCRICAO =desc, VALOR = valor, CODIGO = code, CATEGORIA = categ, IMAGEM = img)
        variavelqq.save()
        print(variavelqq)
    except Exception as e:
        print(str(e))