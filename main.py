from utilities import falar, decidir_acao, ouvir_mic


def main():
    print("Iniciando projeto Jarvis...")
    falar("Projeto Jarvis online e funcional!")

    rodando = True
    while rodando:
        entrada = ouvir_mic()

        if entrada:
            rodando = decidir_acao(entrada)

if __name__ == "__main__":
    main()
