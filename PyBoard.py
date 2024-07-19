from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageGrab, ImageTk
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from CTkColorPicker import *
import webbrowser

def main():
    ######################################### ---- GUI ---- ##########################################

    gui=ctk.CTk()
    gui.title("PyBoard")
    gui.configure(fg_color="#14181f")
    gui.resizable(False, False)

    larghezza_finestra=1050
    altezza_finestra=570
    larghezza_schermo=gui.winfo_screenwidth()
    altezza_schermo=gui.winfo_screenheight()
    x=(larghezza_schermo//2)-(larghezza_finestra//2)
    y=(altezza_schermo//2)-(altezza_finestra//2)
    gui.geometry(f"{larghezza_finestra}x{altezza_finestra}+{x}+{y}")
    gui.lift()

    ####################################### ---- FUNZIONI ---- #######################################
    global colore_sfondo_gomma
    colore_sfondo_gomma="white" 

    def carica_sfondo():
        file_path=filedialog.askopenfilename(filetypes=[("File di Immagini", "*.jpg; *.jpeg; *.png;")])
        if file_path:
            try:
                img=Image.open(file_path)
                img=img.resize((canvas.winfo_width(), canvas.winfo_height()))
                img=ImageTk.PhotoImage(img)
                canvas.create_image(0, 0, anchor=NW, image=img)
                canvas.image=img
            except Exception as e:
                print(f"{e}")

    def posizione(event):
        global x_attuale, y_attuale
        x_attuale=event.x
        y_attuale=event.y

    def disegna(event):
        global x_attuale, y_attuale, colore
        canvas.create_line((x_attuale, y_attuale, event.x, event.y), capstyle=ROUND, smooth=TRUE, width=calcola_valore_attuale(), fill=colore)
        x_attuale, y_attuale=event.x, event.y

    def show_color(colore_nuovo):
        global colore
        colore=colore_nuovo
        canvas.configure(cursor="hand2")

    def pulisci():
        def conferma_cancellazione():
            msg=CTkMessagebox(title="Conferma", bg_color="#14181f", fg_color="#28303e", button_text_color="white", button_color="#28303e", message="Sei sicuro di voler cancellare tutto?", icon="question", option_1="No", option_2="Si")
            risposta=msg.get()
            if risposta=='Si':
                canvas.delete('all')
                palette_di_colori()
            else:
                return
        conferma_cancellazione()

    def palette_di_colori():
        palette.delete('all')
        id=palette.create_rectangle((10, 10, 30, 30), fill="black")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
        id=palette.create_rectangle((10, 40, 30, 60), fill="gray")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))
        id=palette.create_rectangle((10, 70, 30, 90), fill="brown4")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))
        id=palette.create_rectangle((10, 100, 30, 120), fill="red")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
        id=palette.create_rectangle((10, 130, 30, 150), fill="orange")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
        id=palette.create_rectangle((10, 160, 30, 180), fill="yellow")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
        id=palette.create_rectangle((10, 190, 30, 210), fill="green")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('green'))
        id=palette.create_rectangle((10, 220, 30, 240), fill="blue")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
        id=palette.create_rectangle((10, 250, 30, 270), fill="purple")
        palette.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

    def salva_canvas():
        x=canvas.winfo_rootx()
        y=canvas.winfo_rooty()
        x1=x+canvas.winfo_width()
        y1=y+canvas.winfo_height()

        img=ImageGrab.grab().crop((x, y, x1, y1))
        file_path=filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("File PNG", "*.png"), ("Tutti i File", "*.*")])

        if file_path:
            img.save(file_path)

    def calcola_valore_attuale():
        return '{: .2f}'.format(valore_attuale.get())

    def slider_aggiornato(event):
        valore_slider.configure(text=calcola_valore_attuale())

    def inf():
        informazioni=ctk.CTk()
        informazioni.title("PyBoard - Informazioni")
        informazioni.configure(fg_color="#14181f")
        informazioni.resizable(False, False)
        informazioni.attributes("-topmost", True)

        larghezza_finestra=550
        altezza_finestra=320
        larghezza_schermo=gui.winfo_screenwidth()
        altezza_schermo=gui.winfo_screenheight()
        x=(larghezza_schermo//2)-(larghezza_finestra//2)
        y=(altezza_schermo//2)-(altezza_finestra//2)
        informazioni.geometry(f"{larghezza_finestra}x{altezza_finestra}+{x}+{y}")
        informazioni.lift()

        ctk.CTkLabel(informazioni, text="Informazioni Lavagna: ", font=("Leelawadee UI", 15, "bold")).place(x=5, y=5)
        ctk.CTkLabel(informazioni, text="Questo è un progetto open-source scritto interamente in Python, basato sullo", font=("Leelawadee UI", 15)).place(x=6, y=35)
        ctk.CTkLabel(informazioni, text="scopo di dimostrare l'efficacia di Python nello sviluppo di applicativi attraverso", font=("Leelawadee UI", 15)).place(x=7, y=59)
        ctk.CTkLabel(informazioni, text="l'utilizzo di librerie come Tkinter e CustomTkinter.", font=("Leelawadee UI", 15)).place(x=7, y=83)
        ctk.CTkLabel(informazioni, text="Informazioni Generali:", font=("Leelawadee UI", 15, "bold"), ).place(x=6, y=109)
        ctk.CTkLabel(informazioni, text="Developer: Piramide", font=("Leelawadee UI", 15), ).place(x=6, y=139)
        ctk.CTkLabel(informazioni, text="Versione App: 1.0 BETA", font=("Leelawadee UI", 15)).place(x=6, y=161)
        ctk.CTkButton(informazioni, text="GitHub", text_color="white", fg_color="#28303e", font=("Leelawadee UI", 13),
                      command=lambda: webbrowser.open("https://github.com/p1ramide")).place(x=10, y=280)
        
        informazioni.mainloop()

    def colore_sfondo():
        global colore_sfondo_gomma
        pick_color=AskColor(title="Scegli colore dello sfondo", button_color="#28303e", bg_color="#14181f", fg_color="#14181f")
        colore_sfondo_gomma=pick_color.get()
        canvas.configure(background=colore_sfondo_gomma)

    def gomma():
        global colore_sfondo_gomma
        if colore_sfondo_gomma is not None:
            show_color(colore_sfondo_gomma)
        else:
            show_color("white")
        canvas.configure(cursor="dotbox")

    ################################## ---- VARIABILI E BOTTONI ---- #################################

    global colore, canvas
    colore="black"

    ######################### ---- ZONA IN ALTO A SINISTRA ---- ##########################

    tasto_informazioni=ctk.CTkButton(gui, width=40, height=40, corner_radius=20, text_color="#d0d7e1",
                                       anchor="center", fg_color="#28303e", font=("Leelawadee UI", 20, "bold"),
                                       text="ⓘ", command=inf)
    tasto_informazioni.place(x=18, y=20)

    ############################## ---- ZONA AL CENTRO ---- ##############################

    ctk.CTkFrame(gui, width=61, height=310, border_width=5, border_color="#28303e", corner_radius=25,
                 fg_color="#14181f").place(x=20, y=120)

    palette=Canvas(gui, bg="#14181f", highlightthickness=0, width=36, height=280, bd=0)
    palette.place(x=30, y=135)

    canvas=Canvas(gui, width=930, height=500, highlightthickness=0, background="white", cursor="hand2")
    canvas.place(x=100, y=10)

    ######################### ---- ZONA IN BASSO A SINISTRA ---- #########################

    tasto_sfondo=ctk.CTkButton(gui, text="Sfondo", font=("Leelawadee UI", 13), width=80, text_color="white",
                                 fg_color="#28303e", command=colore_sfondo)
    tasto_sfondo.place(x=8, y=485)

    tasto_gomma=ctk.CTkButton(gui, text="Gomma", font=("Leelawadee UI", 13), width=80, text_color="white",
                                fg_color="#28303e", command=gomma)
    tasto_gomma.place(x=8, y=520)

    valore_attuale=tk.DoubleVar(value=1)
    slider = ctk.CTkSlider(gui, from_=1, to=100, command=slider_aggiornato, button_color="#0386ff",
                           variable=valore_attuale)
    slider.place(x=97, y=530)

    valore_slider=ctk.CTkLabel(gui, text=calcola_valore_attuale())
    valore_slider.place(x=95, y=546)

    ########################## ---- ZONA IN BASSO A DESTRA ---- ##########################

    tasto_cancellatutto=ctk.CTkButton(gui, text="Cancella Tutto", font=("Leelawadee UI", 13), text_color="white",
                                        fg_color="#28303e", hover_color="#b51f24", command=pulisci)
    tasto_cancellatutto.place(x=605, y=530)

    tasto_carica=ctk.CTkButton(gui, text="Carica Lavagna", text_color="white", fg_color="#28303e",
                                 font=("Leelawadee UI", 13), command=carica_sfondo)
    tasto_carica.place(x=750, y=530)

    tasto_salva=ctk.CTkButton(gui, text_color="white", fg_color="#28303e", font=("Leelawadee UI", 13),
                                text="Salva Lavagna", command=salva_canvas)
    tasto_salva.place(x=895, y=530)

    ##################################################################################################

    palette_di_colori()

    canvas.bind('<Button-1>', posizione)
    canvas.bind('<B1-Motion>', disegna)

    gui.mainloop()

if __name__ == "__main__":
    main()
