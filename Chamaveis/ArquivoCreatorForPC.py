def standard(L, Tipo, Texto):
    # 1° parametro: Caminho onde vai ser salvo o arquivo
    # 2° parâmetro: Extensão do arquivo
    # 3° parâmetro: Texto que sera inserido

    import os
    from Chamaveis import Local

    B1 = lambda x=20: print("##" * x)

    B1()
    print("[♤Arquivo Creator♤]".center(38, "~"))
    B1()

    FuncPath = Local.Local.RelativePath(L)
    Arquivo = str(input(f"Nome do Arquivo{Tipo}: "))
    Diretorio = os.listdir(FuncPath)
    Extensão = FuncPath + Arquivo + Tipo
    Existe = list(filter(lambda x: (Arquivo + Tipo) == x, Diretorio))

    B1()
    if len(Existe) != 0:
        print("Arquivo já existe!")
        exit()
    else:
        Novo_Arquivo = open(Extensão, "w")
        print("Arquivo Criado!")
        B1()
        Adicional = str(input("Deseja adicionar o texto?[S/N]: ")).upper()
        if Adicional != "N":
            try:
                Novo_Arquivo.write(Texto)
                print("Procedimento concluido!")
            finally:
                Novo_Arquivo.close()
    B1()
    print("<Fim do Algoritmo!>".center(40, "="))
    B1()

# standard(__file__, ".txt", "sample")
