from Chamaveis import Local
try: 
    import androidhelper as android 
except: 
    import android

droid = android.Android()
path = Local.Local_dir(__file__)
print("path: ",path)
droid.recorderStartVideo(path+"a.mp4", 0.5, 1)