from game import partida, campeonato

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    modo = input("2 - para jogar um campeonato ")

    if modo == '1':
        print("\nVoce escolheu uma partida!\n")
        partida()
    elif modo == '2':
        campeonato()
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()