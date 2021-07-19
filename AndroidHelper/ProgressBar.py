from Chamaveis import Local, All_files
try:
    import androidhelper as android
except:
    import android

Local_dir = Local.Local_dir(__file__)
Atual = All_files.FindFiles(__file__)
Show = All_files.ShowFiles

Show(Atual)
Entrada = int(input("Entrada: "))

droid = android.Android()
droid.webViewShow(Local_dir+Atual[Entrada])

for x in range(0,10):
    result = droid.waitForEvent('say').result
    droid.ttsSpeak(result['data'])
    

