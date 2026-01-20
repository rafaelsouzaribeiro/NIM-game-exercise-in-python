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