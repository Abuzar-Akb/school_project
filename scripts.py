import http.client
import urllib.parse
import json
from tkinter.messagebox import showinfo
from tkinter import *
from time import *


def stations():  # new window definition

    key = {'Ocp-Apim-Subscription-Key': 'a97597eb7db7471b94e741b544e39062'}

    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request(
        "GET", "/public-reisinformatie/api/v2/stations", headers=key)
    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    payloadObject = data['payload']
    station_dict = {}
    for station in payloadObject:
        station_dict.update({station["namen"]["lang"]: station["code"]})

    return station_dict


stations = stations()


def inputprompt():
    prompt = Tk()

    def clicked():
        naam = entry.get().capitalize()
        if naam in stations:
            print(stations[naam])

            vertrek_bord = Tk()

            # vertrektijden = Label(master=vertrek_bord, text='goed', height=2)

            key = {'Ocp-Apim-Subscription-Key': 'a97597eb7db7471b94e741b544e39062'}

            params = urllib.parse.urlencode({
                'maxJourneys': '25',
                'station': stations[naam]
            })
            conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
            conn.request(
                "GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)
            response = conn.getresponse()
            responsetext = response.read()
            data = json.loads(responsetext)
            payloadObject = data['payload']
            departuresList = payloadObject['departures']

            bord = Label(master=vertrek_bord,
                         text='Vetrek tijden',
                         background='gold',
                         font=('Helvetica', 16, 'bold '),
                         width=250,
                         height=300)

            # vertrektijdborden
            top_font = ("Helvetica", 25, "bold")
            klein = ('Helvetica', 10)
            front_text = "#002d72"  # Blauw
            back_text = "#ffffff"  # Blauw
            knop = ('Helvetica', 10)
            front_knop = "#ffffff"  # Wit
            back_knop = "#002d72"  # Blauw
            vertrek_bord.configure(height=600, width=500, background="#ffffff")
            vertrek_bord.title('Vertrekbord NS')

            y_as = 85

            Button(vertrek_bord, text=''+strftime("%H:%M"), foreground=front_knop, background=back_knop,
                   font=knop, height=(2), width=5, command=vertrek_bord.destroy).place(x=10, y=0)
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
                Label(vertrek_bord, text=item['actualDateTime'][11:16], font=klein,
                      anchor='w', foreground=front_text, background=back_text).place(x=10, y=y_as)
                Label(vertrek_bord, text=item['direction'], font=klein, anchor='w',
                      foreground=front_text, background=back_text).place(x=100, y=y_as)
                Label(vertrek_bord, text=item['plannedTrack'], font=klein,
                      anchor='w',  foreground=front_text, background=back_text).place(x=270, y=y_as)
                Label(vertrek_bord, text=item['product']["longCategoryName"], font=klein, anchor='w',
                      foreground=front_text, background=back_text).place(x=320, y=y_as)
                y_as += 20

            vertrektijden.pack()
        else:
            messagebox.showerror(
                'NS Automaat', 'U heeft geen geldig station ingevoerd. Probeer het opnieuw!')

    label = Label(master=prompt, text='Voer station naam in', height=2)
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

    vertrek_bord = Tk()

    bord = Label(master=vertrek_bord,
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
    vertrek_bord.configure(height=600, width=500, background="#ffffff")
    vertrek_bord.title('Vertrekbord NS')

    y_as = 85

    Button(vertrek_bord, text=''+strftime("%H:%M"), foreground=front_knop, background=back_knop,
           font=knop, height=(2), width=5, command=vertrek_bord.destroy).place(x=10, y=0)
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
        Label(vertrek_bord, text=item['actualDateTime'][11:16], font=klein,
              anchor='w', foreground=front_text, background=back_text).place(x=10, y=y_as)
        Label(vertrek_bord, text=item['direction'], font=klein, anchor='w',
              foreground=front_text, background=back_text).place(x=100, y=y_as)
        Label(vertrek_bord, text=item['plannedTrack'], font=klein,
              anchor='w',  foreground=front_text, background=back_text).place(x=270, y=y_as)
        Label(vertrek_bord, text=item['product']["longCategoryName"], font=klein, anchor='w',
              foreground=front_text, background=back_text).place(x=320, y=y_as)
        y_as += 20


# UI Baisscherm details:
top_text = ("Helvetica", 32, "bold")
background = "#fcc917"  # Geel
front_text = "#002d72"  # Blauw
back_text = "#fcc917"  # Blauw
front_knop = "#ffffff"  # Wit
back_knop = "#002d72"  # Blauw
knop = font = ("Helvetica", 20)

# UI Basisscherm:
root = Tk()
root.configure(background=background)
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
# root.overrideredirect(True)
# root.geometry('%dx%d+0+0' % (w, h))
root.geometry("1920x1080")
root.title('NS Automaat')


# Knoppen in UI
Label(root, text='Welkom bij NS', font=top_text,
      foreground=front_text, background=back_text).place(x=660, y=60)

actuele = Button(root, text='Actuele \n reisinformatie', foreground=front_knop,
                 background=back_knop, font=knop, command=new_winF, height=2, width=15).place(x=480, y=600)

station = Button(root, text='Station \n informatie', foreground=front_knop,
                 background=back_knop, font=knop, command=inputprompt, height=2, width=15).place(x=900, y=600)
namen = Label(root, text='Door: Abuzar, Fong, Bunjamin en Youssef',
              foreground=front_text, font=20, background=back_text).place(x=620, y=720)

logo = PhotoImage(file='logo.png')
logovester = Label(root,
                   image=logo,).place(x=570, y=200)

root.mainloop()

# label = Label(master=root,
#               text='Welcome bij NS',
#               background='gold',
#               font=('Helvetica', 16, 'bold '),
#               width=25,
#               height=10)


# button1 = Button(root,
#                  font=('Helvetica', 10, 'bold '),
#                  text='Actuele \nreisinformatie ',
#                  background='blue',
#                  foreground='white',
#                  width=15,
#                  height=2,
#                  command=new_winF)


# button2 = Button(root,
#                  font=('Helvetica', 10, 'bold '),
#                  text='Station \ninformatie',
#                  background='blue',
#                  foreground='white',
#                  width=15,
#                  height=2,
#                  command=inputprompt)

# label.pack()
# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)


# root.mainloop()
