from Chamaveis import Local, Barras
import vlc, os

B1 = Barras.BarraDupla
Local = Local.Local_dir(__file__)
Dir = os.listdir(Local)

B1()
print("《TOCADOR .MP3》".center(38,"="))
B1()
Mp3 = list(filter(lambda x: ".mp3" in x, Dir))

for a in range(len(Mp3)):
    print(f"[{1+a}] == {Mp3[a]}")
B1()

Escolha = int(input("Escolha: "))
path = (Local+Mp3[Escolha-1])
print(path)

Music = vlc.MediaPlayer(path)
Music.play()

B1()
Stop = input("Parar: ")
Music.stop() if Stop != "" else exit()