from Chamaveis import Barras, Local, All_files
try:
    import androidhelper as android

except:
    import android 

B1 = Barras.BarraDupla

droid = android.Android()
Atual_dir = Local.Local_dir(__file__)

Find = All_files.FindFiles
Show = All_files.ShowFiles

Show(Find(__file__))
#print("Atual_dir: ", Atual_dir)

#droid.dialogSetMultiChoiceItems(Find[0])


droid.addOptionsMenuItem("Silly","silly",None,"star_on")
droid.addOptionsMenuItem("Sensible","sensible","I bet.","star_off") 
droid.addOptionsMenuItem("Off","off",None,"ic_menu_revert") 
print("Hit menu to see extra options.") 
print("Will timeout in 10 seconds if you hit nothing.") 
while True: # Wait for events from the menu. 
    response = droid.eventWait(10000).result 
    if response == None: 
        break 
        print(response)
    if response["name"]=="off":
        break 
print("And done.")