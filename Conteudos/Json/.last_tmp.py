def Creat_Json():
    
    from Chamaveis import ArquivoCreator as A
    from Chamaveis import Local, Barras
    import json, os
    
    B1 = Barras.BarraDupla
    
    B1()
    print("《CRIANDO JSON.PY》".center(38,"="))
    Nome_Json = str(input("Nome Json: "))
    texto = {Nome_Json:{}}
    
    #CRIANDO DADOS NO ARQUIVO.JSON
    Relé = True
    while Relé:
        B1()
        Topico = str(input("Topico: "))
        Texto = str(input("Conteúdo: "))
        texto[Nome_Json][Topico] = Texto
        B1()
        continuar = str(input("Deseja Atribuir algo mais[S/N]: ")).upper()
        if continuar == "N":
            Relé = False
    #/////
    B1()
    
    #Aficionado elementos no dicionario
    #texto["Json"]["b"] = "a"
    print(str(texto))
    
    #CRIANDO OS PARÂMETROS PARA CRIAÇÃO DO JSON
    Arquivo_Type = ".json"
    path = __file__
    
    Diretorio_atual = Local.Local_dir(path)
    Verifier_dir = os.listdir(Diretorio_atual)
    Arquivo_existe = list(filter(lambda X: (Nome_Json+Arquivo_Type) == X, Verifier_dir))
    
    B1()
    if len(Arquivo_existe) == 0:
        print()
        A.standard(Nome_Json, path, Arquivo_Type, str(texto))
        print()
        
    elif len(Arquivo_existe) != 0:
        print("Arquivo existe")
        
Creat_Json()