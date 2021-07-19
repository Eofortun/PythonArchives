try: 
    import androidhelper as android
except:
    import android

v = 10

droid = android.Android()
'''
@ essa função retorna 3 valores em forma de array
@ usando colchetes [1] é possivel obter o resultado
'''
print(type(droid.checkAirplaneMode()[1]))