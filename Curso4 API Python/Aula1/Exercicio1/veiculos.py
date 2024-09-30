class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
        

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"        
        return f"{self.marca} {self.modelo} Status: {status}"