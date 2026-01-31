class Game:
    def __init__(self):   
        self.n = int(input("Quantas peças? "))
        self.m = int(input("Limite de peças por jogada? "))
        print()
        self.jogador = (self.n % (self.m + 1)) == 0

        if self.jogador:
            print("Você começa!\n")
        else:
            print("Computador começa!\n")

    def computador_escolhe_jogada(n, m):
        if n <= m:
            return n
        else:
            optimal_move = n % (m + 1)
            if optimal_move == 0:
                return m
            else:
                return optimal_move

    def usuario_escolhe_jogada(n, m):
        while True:
            try:
                jogada = int(input(f"Quantas peças você vai tirar? "))
                if jogada < 1 or jogada > m:
                    print(f"Jogada inválida! Você deve tirar entre 1 e {m} peças.")
                elif jogada > n:
                    print(f"Você não pode tirar mais peças do que as disponíveis ({n}).")
                else:
                    return jogada
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")


