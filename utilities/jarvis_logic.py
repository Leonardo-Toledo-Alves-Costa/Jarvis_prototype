import pyttsx3
import geocoder
import webbrowser
from datetime import datetime

def decidir_acao(entrada):

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
        case e if "abrir" in e:
            for site in sites:
                if site in e:
                    falar(f"Abrindo o site {site}")
                    abrir_site(site)
                    return True
            falar("Site fora da base de dados")
            return True
        case e if "sair" in e or 'desligar' in e:
            falar("Finalizando projeto Jarvis")
            return False
        case _:
            print("comando desconhecido")
            return True
        

def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(texto)
    engine.runAndWait()

def buscar_localizacao():
    ip = geocoder.ip('me')
    if ip.city and ip.state:
        return f"{ip.city}, {ip.state}"
    return "Não foi possível encontrar a sua localização"

sites = {
        'youtube': 'https://www.youtube.com',
        'sigaa': 'https://sigaa.unifei.edu.br/sigaa/public/home.jsf',
        'google': 'https://www.google.com/?client=safari&zx=1767909682901&no_sw_cr=1'
    }

def abrir_site(site):
    url = sites.get(site)

    try:
        if url:
            webbrowser.open(url)
        else:
            falar(f"Desculpe, esse site não está em nosso banco de dados")
    except webbrowser.Error:
        falar(f"Não foi possível abrir o site {site} por conta de um erro")
    