import tkinter as tk

def somma(num1,num2):
    return num1+num2

def moltiplicazine(num1,num2):
    return num1*num2

def sottrazione(num1,num2):
    return num1-num2

def divisione(num1,num2):
    if num2 == 0:
        print("ERRORE, non si può dividere per 0")
    else:
        return num1/num2
    

window = tk.Tk()
window.title("calcolatrice")
window.geometry("200x200")
window.resizable(True,True)
window.configure(background="red")

altra_operazione = True
while(altra_operazione == True):
    scelta = True
    print("Quale operazione vuoi eseguire:\n1- Somma\n2- Moltiplicazione\n3- Sottrazione\n4- Divisione")
    scelta_operazione = int(input())
    print("Inserisci il primo numero per l'operazione:\n")
    numero1 = int(input())
    print("Inserisci il secondo numero per l'operazione:\n")
    numero2 = int(input())
    if scelta_operazione==1:
        print(f"La somma è: {somma(numero1,numero2)}")
    elif scelta_operazione == 2:
        print(f"La moltiplicazione è: {moltiplicazine(numero1,numero2)}")
    elif scelta_operazione == 3:
        print(f"La sottrazione è: {sottrazione(numero1,numero2)}")
    elif scelta_operazione == 4:
        print(f"La divisione è: {divisione(numero1,numero2)}")
    while(scelta == True):
        print("Vuoi effettuare un'altra operazione? (si/no)")
        nuova_operazione = input()
        if nuova_operazione.lower() == "si":
            altra_operazione = True
            scelta = False
        elif nuova_operazione.lower() == "no":
            altra_operazione = False
            scelta = False
        else:
            print("non è stata inserita una risposta valida")