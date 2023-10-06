import PyPDF2
import pyttsx3

#convert pdf to mp3(audiobook)
voz = pyttsx3.init()
#to change voices
"""
voices = voz.getProperty('voices') 
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
"""
voz.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
#open the pdf and read it
libro = open("el-arte-de-prudencia.pdf", 'rb')
lector = PyPDF2.PdfReader(libro)
texto_total = ""

#verify number of pages of the pdf
#paginas = len(lector.pages) 
#print(paginas)

for x in lector.pages:
   texto = x.extract_text()
   texto_total += texto
    
libro.close()
    

voz.save_to_file(texto_total,'audiolibro2.mp3')  
voz.runAndWait()

    
    