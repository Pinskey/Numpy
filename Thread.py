# Thread con tkinter Reaktice
# 12:23 PM
# File python per testare i thread attraverso la libreria tkinter
# tk_windows_thread.py

import tkinter as tk
import time
import threading # Thread può essere usato per runnare in modo asincrono rispetto al resto dello script
                 # cioè runna in modo autonomo rispetto all' esecuzione dello script principale


def create_window(width, height, title, bg_color, font_size, font_family):
    # Creare la finestra principale
    root = tk.Tk()
    
    # Impostare le dimensioni della finestra
    root.geometry(f"{width}x{height}")
    
    # Impostare il titolo della finestra
    root.title(title)
    
    # Impostare il colore di sfondo della finestra
    root.configure(bg=bg_color)
    
    # Creare una label con dimensioni e font specificati
    font = (font_family, font_size)
    label = tk.Label(root, text="Questo è un testo colorato!", fg="#FF0000", bg=bg_color, font=font)
    label.pack(pady=20)
    
    # Creare un canvas per disegnare il cerchio
    canvas = tk.Canvas(root, width=800, height=800, bg=bg_color)
    canvas.pack(pady=20)
    
    # Disegnare il cerchio (LED)
    led = canvas.create_oval(1, 1, 800, 800, fill="green")
    
    def blink_led():
        while True:
            current_color = canvas.itemcget(led, "fill")
            new_color = "blue" if current_color == "red" else "red"
            canvas.itemconfig(led, fill=new_color)
            time.sleep(0.01)
    
    # Creare e avviare il thread per far lampeggiare il cerchio
    threading.Thread(target=blink_led, daemon=True).start()
    
    # Avviare il ciclo principale della finestra
    root.mainloop()

# Esempio di utilizzo
width = 1200
height = 1200
title = "Finestra con LED lampeggiante"
bg_color = "lightblue"
font_size = 16
font_family = "Helvetica"

create_window(width, height, title, bg_color, font_size, font_family)

