import http.client
import urllib.parse
import json
from tkinter.messagebox import showinfo
from tkinter import *
from time import *

namen = ['utrecht', 'amsterdam']


def inputprompt():
    prompt = Tk()

    def clicked():
        naam = entry.get()
        if naam in namen:
            label["text"] = 'goed'

    label = Label(master=prompt, text='Hello World', height=2)
    label.pack()

    button = Button(master=prompt, text='Druk hier',
                    command=clicked, )
    button.pack(pady=10)

    entry = Entry(master=prompt)
    entry.pack(padx=10, pady=10)


def new_winF():  # new window definition
    # get api data
    key = {'Ocp-Apim-Subscription-Key': 'a97597eb7db7471b94e741b544e39062'}

    params = urllib.parse.urlencode({
        'maxJourneys': '25',
        'station': 'Ut'
    })
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request(
        "GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)
    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    vertrek_tijden = Tk()

    bord = Label(master=vertrek_tijden,
                 text='Vetrek tijden',
                 background='gold',
                 font=('Helvetica', 16, 'bold '),
                 width=250,
                 height=300)

    payloadObject = data['payload']
    departuresList = payloadObject['departures']

# vertrektijdborden
    top_font = ("Helvetica", 25, "bold")
    klein = ('Helvetica', 10)
    front_text = "#002d72"  # Blauw
    back_text = "#ffffff"  # Blauw
    knop = ('Helvetica', 10)
    front_knop = "#ffffff"  # Wit
    back_knop = "#002d72"  # Blauw
    vertrek_bord = Tk()
    vertrek_bord.configure(height=600, width=500, background="#ffffff")
    vertrek_bord.title('Vertrekbord NS')

    y_as = 85

    Button(vertrek_bord, text=''+strftime("%H:%M"), foreground=front_knop, background=back_knop,
           font=knop, height=(2), width=5, command=vertrek_bord.destroy).place(x=5, y=0)
    Label(vertrek_bord, text='Vertrek Tijden', font=top_font,
          foreground=front_text, background=back_text).place(x=85, y=0)

    Label(vertrek_bord, text='tijd', font=('Helvetica', 10, 'bold'),
          foreground=front_text, background=back_text).place(x=5, y=65)
    Label(vertrek_bord, text='naar', font=('Helvetica', 10, 'bold'),
          foreground=front_text, background=back_text).place(x=100, y=65)
    Label(vertrek_bord, text='spoor', font=('Helvetica', 10, 'bold'),
          foreground=front_text, background=back_text).place(x=270, y=65)
    Label(vertrek_bord, text='treinsoort', font=('Helvetica', 10, 'bold'),
          foreground=front_text, background=back_text).place(x=320, y=65)
#     Label(vertrek_bord, text='opmerkingen', font=('Helvetica', 10, 'bold'),
#           foreground=front_text, background=back_text).place(x=320, y=65)

    for item in departuresList:
        Label(vertrek_bord, text=item['actualDateTime'], font=klein,
              anchor='w', foreground=front_text, background=back_text).place(x=5, y=y_as)
        Label(vertrek_bord, text=item['direction'], font=klein, anchor='w',
              foreground=front_text, background=back_text).place(x=100, y=y_as)
        Label(vertrek_bord, text=item['plannedTrack'], font=klein,
              anchor='w',  foreground=front_text, background=back_text).place(x=270, y=y_as)
        Label(vertrek_bord, text=item['product']["longCategoryName"], font=klein, anchor='w',
              foreground=front_text, background=back_text).place(x=320, y=y_as)
        y_as += 20


# styling buttons
root = Tk()
label = Label(master=root,
              text='Welcome bij NS',
              background='gold',
              font=('Helvetica', 16, 'bold '),
              width=25,
              height=3)


button1 = Button(root,
                 font=('Helvetica', 10, 'bold '),
                 text='Actuele \nreisinformatie ',
                 background='blue',
                 foreground='white',
                 width=15,
                 height=2,
                 command=new_winF)


button2 = Button(root,
                 font=('Helvetica', 10, 'bold '),
                 text='Station \ninformatie',
                 background='blue',
                 foreground='white',
                 width=15,
                 height=2,
                 command=inputprompt)

label.pack()
button1.pack(side=LEFT, padx=15)
button2.pack(side=RIGHT, padx=15)


root.mainloop()
