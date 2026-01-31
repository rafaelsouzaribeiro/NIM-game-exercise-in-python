from game import Game
from scoreboard import Scoreboard
from round import Round

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    modo = input("2 - para jogar um campeonato ")

    if modo == '1':
        print("\nVoce escolheu uma partida!\n")
        game = Game()
        round = Round(game.jogador, game.n, game.m, scoreboard=Scoreboard())
        round.play()
    elif modo == '2':
        print("\nVoce escolheu um campeonato!\n")
        sb = Scoreboard()
        for rodada in range(1, 4):
            print(f"**** Rodada {rodada} ****\n")
            game = Game()
            round = Round(game.jogador, game.n, game.m, scoreboard=sb)
            round.play()
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()