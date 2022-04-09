import connect as conx
    
def listar(escolha):
    
    dic = {} 
    contador = 0 
    #SELECIONA UM PRODUTO EM ESPECIFICO DE ACORDO COM O FILTRO (QUE NO CASO É O NOME)
    if len(escolha) >= 2:
        for  registro in conx.Produtos.objects():
            if registro['NOME'] == escolha:
                dic[contador] = { "NOME": registro['NOME'], "DESCRICAO" : registro['DESCRICAO'], "VALOR" :registro['VALOR'] }
                contador +=1
    #PUXA A LISTA INTEIRA CASO NÃO TENHA NOME 
    else:
        for  registro in conx.Produtos.objects():
            dic[contador] = { "NOME": registro['NOME'], "DESCRICAO" : registro['DESCRICAO'], "VALOR" :registro['VALOR'] }
            contador +=1
    return dic
    
def tamanho():
    return len(conx.Produtos.objects())