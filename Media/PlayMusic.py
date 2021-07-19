from Chamaveis import Local, Barras
import os
try:
    import androidhelper
except:
    import android

B1 = Barras.BarraDupla
B1()
print("《PLAY MUSIC》".center(40,"="))
B1()

Local = Local.Local_dir(__file__)

Music = os.listdir(Local)
Mp3_verifier = list(filter(lambda x: ".mp3" in str(x), Music))


Array = []
for x in range(len(Mp3_verifier)):
    print(f"[{x}] = {Mp3_verifier[x]}")
    Array.append(Mp3_verifier[x])

B1()
Escolha = int(input("Escolha: "))    

#Ligar Musica
droid = androidhelper.Android()
Xpath = Local+str(Array[Escolha])
droid.mediaPlay(Xpath)

B1()

#Fechar arquivo
Close = str(input("Fechar: "))
if Close != "":
    droid.mediaPlayClose()