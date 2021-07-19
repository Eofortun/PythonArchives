def FindFiles(Local_file):
    import os, Local, Barras
    
    Atual_dir = Local.Local_dir(Local_file)    
    B1 = Barras.BarraDupla
    
    B1()
    print("《ARQUIVOS NO DIRETORIO》".center(40,"="))
    B1()
    
    Arquivos = os.listdir(Atual_dir)
    for x in range(len(Arquivos)):
        print(f"[{x}] = {Arquivos[x]}")
    B1()