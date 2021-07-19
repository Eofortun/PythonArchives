from functools import reduce

class Local:

    def __init__(self, Arquivo):
        self.Arquivo = Arquivo


    def Local_dir(self):#Retorna uma string com o caminho correto do arquivo

        #Parâmetro: __file__

        Local = self.Arquivo.split("/")
        Local.pop()
        Bar = "/"
        Bar += reduce(lambda x,y: x + y + "/", Local)

        return Bar

    def LocalLess(self):#Retorna uma string do path sem a barra

        #Parâmetro: __file__

        Local = self.Arquivo.split("/")
        Local.pop()
        Less = "/"
        Less += reduce(lambda x, y: x + y + "/", Local)
        Total = Less[:len(Less)-1]

        return Total


    def RelativePath(path):

        PathSlit = path.split('/')
        PathSlit.pop()

        new_path = ''
        for x in range(0, len(PathSlit)):
            new_path += PathSlit[x] + '/'

        return new_path


'''
caminho = __file__

print(caminho)
Local.RelativePath(caminho)
'''










'''
a = 'C:/Users/Krieg/Documents/Programs/Python/Curso-em-video/Curso-Python-master/New/PythonArchives'
path_mutado = Local_dir(a)
print(path_mutado)

new_path = ''

for x in range(1, len(path_mutado)):
    new_path += path_mutado[x]

print(new_path)
'''
