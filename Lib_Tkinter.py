import tkinter as tk

window = tk.Tk()
window.title("Finestra di prova")
window.geometry("600x600")
window.resizable(True,True)
window.configure(background="red")

# Di seguito vanno i widget
etichetta = tk.Label(window, text="Etichetta di prova", fg="#FF0000", font=("Helvetica",10))
etichetta.grid(row=0, column=0, sticky="W", padx=10, pady=10)

def stampa_etichetta():
    text = "prova"
    text_output = tk.Label (window, text = text,fg="#ff0000",font = ("Helvetica",10))
    text_output.grid(row = 1, column=1, sticky="W")

# Di seguito definisco un pulsante
first_button = tk.Button(text = "Clicca", command= stampa_etichetta)
first_button.grid(row = 1,column=0,sticky="N")

def stampa_etichetta_input():
    testo = input_text.get()
    text_output1 = tk.Label(window,text = testo, fg="#FF0000", font=("Helvetica",10))
    text_output1.grid(row= 3,column = 0)

# Creazione del campo di input
input_text = tk.Entry(window)
input_text.grid(row=2,column=0,sticky="W")

second_button = tk.Button(window, text = "Clicca2!",command=stampa_etichetta_input)
second_button.grid(row=3,column=0,sticky="W")

if __name__ == "__main__":
    window.mainloop()