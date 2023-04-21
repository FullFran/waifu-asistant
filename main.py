import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia

'''
Primero vamos a definir un método para que convierta lo que le decimos en texto y nos escuche
'''

def escuchar():
    r=sr.Recognizer()
    '''
    Vamos a utilizar de speech_Recognition el módulo micrófono
    para que nos escuche lo que le decimos.
    '''
    with sr.Microphone() as source:
        print('Escuchando:')

        #Después de estos segundos sin escuchar nada
        #considerará que está completado.
        r.pause_threshold=0.7
        audio=r.listen(source)

        '''
        Ahora utilizamos el método try and catch para que 
        si no escucha bien lo que decimos tenga una excepción.
        '''
        try:
            print('Reconociendo...')
            Query=r.recognize_google(audio, language='es-ES')
            print('Has dicho: ', Query)

        except Exception as e:
            print(e)
            print('Dilo otra vez por favor.')
            return 'None'
        
        return Query


def decir(audio):
    engine=pyttsx3.init()

    voices=engine.getProperty('voices')
    #0=hombre 1=mujer
    engine.setProperty('voice',voices[0].id)

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)

    engine.say('<pitch middle="10">'+audio+'</pitch>')

    engine.runAndWait()

def saludar():
    decir('¡Hola!, soy tu asistente. ¿En qué puedo ayudarte?')





def diasemana():
    day=datetime.datetime.today().weekday()+1

    Day_dict= {1:'Lunes',2: 'Martes',
                3: 'Miércoles', 4: 'Jueves',
                5: 'Viernes', 6: 'Sábado',
                7: 'Domingo'}
    
    if day in Day_dict.keys():
        day_of_the_week=Day_dict[day]
        print(day_of_the_week)
        decir('Hoy es'+day_of_the_week)

def darhora():

    time=str(datetime.datetime.now())

    print(time)
    hour=time[11:13]
    min=time[14:16]
    decir('Son las '+hour+' y '+min+' minutos')

def actuar():

    saludar()

    while(True):

        query=escuchar().lower()
        #if 'mila' in query:
        if 'qué día es' in query:
            diasemana()
        elif 'qué hora es' in query:
            darhora()

        elif 'adiós' in query:
            decir('Adiós, espero volver a verte pronto.')
            exit()
        elif 'abrir youtube' in query:
            decir('Ahora mismo lo abro.')
            webbrowser.open('www.youtube.com')
if __name__ == '__main__':
    
    actuar()
