class FileEditor():

    def __init__(self, filename):
        self.file_name = filename
        self.file_exist = self.fileExist()

        if self.file_exist == True:
            out = False
            while not out:
                action = input(
                    'Pulsar B para borrar y continuar escribiendo o pulsar W para continuar en la ultima línea: ').upper()
                if action == 'B':
                    self.writeFile()
                    out = True
                elif action == "W":
                    self.continueTyping()
                    out = True
                else:
                    print('No ha indroducido un comando valido')
        else:
            self.writeFile()
            
        self.printe()
            

    def fileExist(self):
        try:
            with open(self.file_name, 'r') as file:
                self.contenido = file.read()
            self.file_exist = True

        except FileNotFoundError:
            self.file_exist = False

        return self.file_exist

    def writeFile(self):
        with open(self.file_name, "w") as file:
            while True:
                text = input("Insertar texto (Vacio para salir): ") + "\n"
                if text == "\n":
                    break
                else:
                    file.write(text)


    def continueTyping(self):
        print(self.contenido)
        with open(self.file_name, "w") as file:
            file.write(self.contenido)
            while True:
                text = input("Insertar texto (Vacio para salir): ") + "\n"
                if text == "\n":
                    break
                else:
                    file.write(text)
                    
    def printe(self):
        with open(self.file_name, 'r') as file:
            self.contenido = file.read()
        print('\n Este es el contenido del archivo \n')
        print(self.contenido)
