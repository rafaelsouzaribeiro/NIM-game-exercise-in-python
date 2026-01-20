from player import usuario_escolhe_jogada
from computer import computador_escolhe_jogada

vitorias_usuario = 0
vitorias_computador = 0

def partida():
    global vitorias_usuario, vitorias_computador
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    valor_cond=n % (m + 1) == 0

    if valor_cond:
        print("Você começa!\n")
        jogador = True
        
    if not valor_cond:
        print("Computador começa!\n")
        jogador = False

    while n > 0:
        if jogador:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            
            if jogada == 1:
                print("\nVocê tirou uma peça.")
            else:
                print(f"\nVocê tirou {jogada} peças.")
        else:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {jogada} peças.")
        
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        elif n > 1:
            print(f"Agora restam {n} peças no tabuleiro.\n")
        
        jogador = not jogador

    if jogador:
        print("Fim do jogo! O computador ganhou!\n")
        vitorias_computador += 1
    else:
        print("Fim do jogo! Você ganhou!\n")
        vitorias_usuario += 1
    print("**** Final do campeonato! ****\n")
    print(f"Placar: Você {vitorias_usuario} X {vitorias_computador} Computador")    

def campeonato():
    global vitorias_usuario, vitorias_computador
    
    print("\nVoce escolheu um campeonato!\n")
    
    vitorias_usuario = 0
    vitorias_computador = 0
    
    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****\n")
        partida()
    
