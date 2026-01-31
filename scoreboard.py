class Scoreboard:
    def __init__(self):
        self.usuario = 0
        self.computador = 0

    def inc_usuario(self):
        self.usuario += 1

    def inc_computador(self):
        self.computador += 1

    def __str__(self):
        return f"**** Final do campeonato! ****\nPlacar: Você {self.usuario} X {self.computador} Computador"

