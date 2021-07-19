from Chamaveis import All_files, Local
#FindFiles, ShowFiles

Atual_dir = Local.Local_dir(__file__)
Find = All_files.FindFiles(__file__)
Show = All_files.ShowFiles
Show(Find)
#Escolha = int(input("Escolha: "))
Gravar = "GB18030"
#Arquivo = Find[Escolha]

Text = '=$%^&*'.encode(Gravar)
print(Text)
CodedText = Text.decode(Gravar)
print(CodedText)

"""
with open(Atual_dir+Arquivo, "r") as Planilha_file:
    Ler = Planilha_file.read()
    print("Original: ", type(Ler))
    print(f"Encode: {Ler.decode(Gravar)}")
"""