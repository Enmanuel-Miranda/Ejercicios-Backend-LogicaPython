class Historia:
    # clase que inicia
    def __init__(self):
        #inicia el texto como un vacio que no se puede ver
        self.texto = ""

    def escribir(self, nuevo_texto):
        self.texto = self.texto + nuevo_texto
    
    def mostrar_texto(self):
        return self.texto


# Ejecutamos la clase para probarlo

instancia = Historia()
instancia.escribir("Gab riel")
instancia.escribir(", estoy aqui para aapoyarte")

print(instancia.mostrar_texto())

# para poder ejecutar esto lo qque debemos hacer es
# ejecutar con py class 

