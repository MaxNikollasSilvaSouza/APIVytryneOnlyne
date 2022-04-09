import connect as conx

def verificacao(email, senha):
    
    #SELECIONA UM PRODUTO EM ESPECIFICO DE ACORDO COM O FILTRO (QUE NO CASO É O NOME)
    if len(email) >= 2 and len(senha) >=2:
        verificar = 'false'
        for  registro in conx.Usuario.objects():
            if registro['EMAIL'] == email and registro['SENHA'] == senha:
                verificar = 'true'
            else:
                verificar = 'false'
        
    return verificar

def salvar(email, senha):
    
    try:
        #SALVANDO DOCUMENTO
        variavelqq = conx.Usuario(EMAIL = email, SENHA =senha)
        variavelqq.save()
        return 'Usuario Salvo'
    except Exception as e:
        print(str(e))
        return str(e)

def deletar(email): 
    item = conx.Usuario.objects(EMAIL = email)
    item.delete()
    return 'Usuario Deletado com Sucesso'