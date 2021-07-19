import os
print("Nome do sistema:",os.name)
print("Grupo de processos:", len(os.getgroups()))
print("Login: ",os.getlogin())
#print(getpass.getuser())
print(os.getpgid(0))