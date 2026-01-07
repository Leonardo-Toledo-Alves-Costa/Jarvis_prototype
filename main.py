import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    print("Iniciando projeto Jarvis...")
    falar("Olá, senhor. O projeto Jarvis está online e funcional!")
    

