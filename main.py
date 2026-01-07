import pyttsx3

def abrir_site():
    pass

def decidir_ação(entrada):
    match entrada:
        case "que horas são":
            print("O horáro é: 18h28min")
        case "localização":
            print("Você está em Extrema, Minas Gerais")
        case "abrir o youtube":
            print("Abrindo o youtube...")
        case _:
            print("comando desconhecido")


'''
def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    print("Iniciando projeto Jarvis...")
    falar("Olá, senhor. O projeto Jarvis está online e funcional!")
'''

def main():
    entrada = input("Digite o comando: ").lower()
    #ler_texto(entrada)
    decidir_ação(entrada)

main()
