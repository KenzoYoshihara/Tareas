fecha=input("Introduza el dia de nacimiento\1n Introduzca el mes de nacimiento.")
dia = int(a)
mes = int(b)
a=1
if a<=31 and a>=1:
    print("El dia es correcto")
    if b<=12 and b>=1:
        print("El dia es correcto\n")
        if(b==3 and a<=21)or(b==4 and a<=20):
            print("El signo es Aries\n Es importante que definas situaciones y no sigas posponiendo las decisiones sentimentales, cuida tus palabras.")
        if(b==4 and a<=21)or(b==5 and a<=21):
            print("El signo es Tauro\n Para ti este es un momento de mucha importancia en tu paisaje sentimental debido al transito lunar existente.")
        if(b==5 and a<=22)or(b==6 and a<=21):
            print("El signo es Geminis\n Se inicia un ciclo lleno de posibilidades donde tu intuicion se afina y descubres cosas ocultas que tenia tu pareja.")
        if(b==6 and a<=22)or(b==7 and a<=22):
            print("El signo es Cancer\n Podras superar cualquier crisis con la fuerza radiante de tu voluntad si te han diagnosticado alguna dolencia.")
        if(b==7 and a<=23)or(b==8 and a<=23):
            print("El signo es Leo\n Despues que pasen los primeros momentos de una crisis te recuperas muy bien y te sentiras mejor que antes")
        if(b==8 and a<=24)or(b==9 and a<=23):
            print("EL signo es Virgo\n Todo es posible en este fin de semana. Un romance alejado regresa a tu vida. Entras en la etapa del amor.")
        if(b==9 and a<=24)or(b==10 and a<=23):
            print("El signo es Libra\n En pocos dias estaras viviendo una excitante aventura que te permitira disfrutar bien de tu vida pasional.")
        if(b==10 and a<=24)or(b==11 and a<=22):
            print("El signo es Escorpio\n Si tu trabajo es por comisiones, propinas o ingresos fuera de lo rutinario, vas a tener un buen ingreso en este dia.")
        if(b==11 and a<=23)or(b==12 and a<=21):
            print("El signo es Sagitario\n Tu nivel de comunicacion esta en un tono elevado y tendras mucho exito en el amor hablando abiertamente.")
        if(b==12 and a<=22)or(b==1 and a<=20):
            print("El signo es Capricornio\n Vende lo que no necesitas, sacale un mayor partido a tus talentos y no regales tu tiempo a gente que no lo valora.")
        if(b==1 and a<=21)or(b==2 and a<=20):
            print("El signo es Acuario\n SI estas desempleado no te inquietes y utiliza el tiempo libre para enviar cartas de ofertas a empleadores.")
        if(b==2 and a<=21)or(b==3 and a<=20):
            print("El signo es Piscis\n Te atreveras a realizar lo que hasta ahora considerabas prohibido, arriesgado o tabu. Empieza un tiempo intenso.")
        
    else:
        print("Error en el dia")
else:
    print("Error en el mes")
    
