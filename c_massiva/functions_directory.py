import os

def clearDirectory(user):
    path = "c_massiva/uploads/" + user + '/'

    for f in os.listdir(path):
        try:
            os.remove(os.path.join(path, f))
        except OSError:
            print("Erro ao deletar os arquivos %s " % path)
        else:
            print("Successfully ao deletar os arquivos %s " % path)

def createDirectory(user):
    path = "c_massiva/uploads/" + user + '/'

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)