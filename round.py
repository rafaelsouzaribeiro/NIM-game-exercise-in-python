from game import Game
from scoreboard import Scoreboard

class Round:
    def __init__(self, jogador, n, m, scoreboard=None):
        self.jogador = jogador
        self.n = n
        self.m = m
        self.scoreboard = scoreboard or Scoreboard()

    def play(self):
        while self.n > 0:
            if self.jogador:
                jogada = Game.usuario_escolhe_jogada(self.n, self.m)
                self.n -= jogada

                if jogada == 1:
                    print("\nVocê tirou uma peça.")
                else:
                    print(f"\nVocê tirou {jogada} peças.")
            else:
                jogada = Game.computador_escolhe_jogada(self.n, self.m)
                self.n -= jogada

                if jogada == 1:
                    print("O computador tirou uma peça.")
                else:
                    print(f"O computador tirou {jogada} peças.")

            if self.n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif self.n > 1:
                print(f"Agora restam {self.n} peças no tabuleiro.\n")

            self.jogador = not self.jogador

        if self.jogador:
            self.scoreboard.inc_computador()
            print(self.scoreboard)
            print("Fim do jogo! O computador ganhou!\n")
        else:
            self.scoreboard.inc_usuario()
            print(self.scoreboard)
            print("Fim do jogo! Você ganhou!\n")

        return self.scoreboard