from utilities import falar, decidir_acao


def main():
    print("Iniciando projeto Jarvis...")
    falar("Projeto Jarvis online e funcional!")
    rodando = True

    while rodando:
        entrada = input("Digite o comando: ").lower()
        rodando = decidir_acao(entrada)

if __name__ == "__main__":
    main()
