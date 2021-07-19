try: 
    import androidhelper as android 
except: 
    import android
#import androidhelper    

droid = android.Android()
wifi_list = droid.wifiGetScanResults()
#stop_location = droid.stopLocating()
print("##"*20)
print("Lista dos wifi: ", wifi_list)

print(droid.wifiGetConnectionInfo())
#print(droid.cameraCapturePicture("0"))
#droid.vibrate(200)

#print(droid.getRunningPackages())
"""
if droid.setScreenBrightness(200) != None:
    droid.setScreenBrightness(200)
else:
    print("Erro")"""