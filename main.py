import pyttsx3
from datetime import datetime
import webbrowser
import geocoder

def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(texto)
    engine.runAndWait()

def abrir_site(site):
    sites = {
        'youtube': 'https://www.youtube.com',
        'sigaa': 'https://sigaa.unifei.edu.br/sigaa/public/home.jsf',
        'google': 'https://www.google.com/?client=safari&zx=1767909682901&no_sw_cr=1'
    }
    url = sites.get(site)

    try:
        if url:
            webbrowser.open(url)
        else:
            falar(f"Desculpe, esse site não está em nosso banco de dados")
    except webbrowser.Error:
        falar(f"Não foi possível abrir o site {site} por conta de um erro")
    
def buscar_localizacao():
    ip = geocoder.ip('me')
    if ip.city and ip.state:
        return f"{ip.city}, {ip.state}"
    return "Não foi possível encontrar a sua localização"
    

def decidir_ação(entrada):

    match entrada:
        case e if "horas" in e or 'horario' in e:
            agora = datetime.now().strftime('%H:%M')
            print(f"Agora são {agora}")
            falar(f"Agora são {agora}")
            return True
        case e if "localização" in e or 'onde' in e:
            loc = buscar_localizacao()
            print(f"A sua localização atual é {loc}")
            falar(f"A sua localização atual é {loc}")
            return True
        case e if "youtube" in e:
            print("Abrindo o youtube...")
            falar("Abrindo o youtube...")
            abrir_site("youtube")
            return True
        case e if "sigaa" in e:
            print("Abrindo o sigaa...")
            falar("Abrindo o sigaa...")
            abrir_site("sigaa")
            return True
        case e if "google" in e:
            print("Abrindo o google...")
            falar("Abrindo o google...")
            abrir_site("google")
            return True
        case e if "sair" in e or 'desligar' in e:
            falar("Finalizando projeto Jarvis")
            return False
        case _:
            print("comando desconhecido")
            return True


def main():
    print("Iniciando projeto Jarvis...")
    falar("Projeto Jarvis online e funcional!")
    rodando = True

    while rodando:
        entrada = input("Digite o comando: ").lower()
        rodando = decidir_ação(entrada)

main()
