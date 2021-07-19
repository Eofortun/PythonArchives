from Chamaveis import Local, Barras
import os

B1 = Barras.BarraDupla

Atual_dir = Local.Local_dir(__file__)
File_Txt = os.listdir(Atual_dir)
Txt_content = list(filter(lambda x: ".txt" in x, File_Txt))

B1()
for x in range(len(Txt_content)):    
    print(f"[{x}] = {Txt_content[x]}")
B1() 
Escolha = int(input("Escolha: "))

print(Atual_dir+Txt_content[Escolha])
File_Opened = open(Atual_dir+Txt_content[Escolha], "r")

#print(File_Opened.readlines()[0])

TextSample = "A LOT OF SYMBOLS @GYIBBJHĢFŔÝÚ" #File_Opened.readlines()[0]
#Lorem ipsum Dolor sit Amet"
#print(str(TextSample))
B1()
#print(codecs.encode())
B1()

#Codificando

Codec = 'iso2022_jp_2'
EncodeTXT = TextSample.encode(Codec)
print(f"Encode_{Codec}: \n", EncodeTXT)   

B1()

#Decodificando
DecodeTXT = EncodeTXT.decode(Codec)
print(f"Decode_{Codec}: \n", DecodeTXT)
B1()