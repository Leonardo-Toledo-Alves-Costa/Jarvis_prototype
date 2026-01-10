import speech_recognition as sr
from .jarvis_logic import falar

def ouvir_mic():
    rec = sr.Recognizer()

    falar('Por favor, diga o comando desejado')

    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        print("Ouvindo...")

        try:
            audio = rec.listen(source)
            texto = rec.recognize_google(audio, language="pt-BR")
            print(f"O áudio dito foi {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            falar("Não foi possível criar a conexão com o google.")
            return ""
