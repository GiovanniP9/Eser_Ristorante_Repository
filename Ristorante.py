# classe Ristorante
class Ristorante:
    # Inizializza il ristorante
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}
    # Descrive il ristorante
    def descrivi_ristorante(self):
        print(f"Benvenuti al ristorante {self.nome}, che offre cucina {self.tipo_cucina}.")
    # Visualizza lo stato di apertura del ristorante
    def stato_apertura(self):
        if self.aperto: 
            print(f"Il ristorante {self.nome} è aperto ")
        else:
            print(f"Il ristorante {self.nome} è chiuso ")
    # Apre il ristorante
    def apri_ristorante(self):
        password = input("Inserisci la password per aprire il ristorante: ")
        if password == "maremma":# Se la password è corretta apre il ristorante
            self.aperto = True
            print(f"Il ristorante {self.nome} è stato aperto.")
    # Chiude il ristorante
    def chiudi_ristorante(self):
        password = input("Inserisci la password per chiudere il ristorante: ")
        if password == "maremma":# Se la password è corretta chiude il ristorante
            self.aperto = False
            print(f"Il ristorante {self.nome} è stato chiuso.")
        else:
            print("Password non corretta.")
    # Aggiunge un piatto al menu
    def aggiungi_al_menu(self,):
        # Inserisci la password per aggiornare il menu
        password = input("Inserisci la password per chiudere il ristorante: ")
        if password == "maremma": # Se la password è corretta
            piatto = input("Inserisci il nome del piatto da aggiungere: ")
            prezzo = float(input("Inserisci il prezzo del piatto da aggiungere: "))
            self.menu[piatto] = prezzo
        else:# Se la password non è corretta
            print("Password non corretta.")
    # Rimuove un piatto dal menu
    def rimuovi_dal_menu(self):
        # Inserisci la password per aggiornare il menu
        password = input("Inserisci la password per chiudere il ristorante: ")
        if password == "maremma":
            piatto = input("Inserisci il nome del piatto da rimuovere: ")
            if piatto in self.menu: # Se il piatto è presente nel menu
                del self.menu[piatto]
                print(f"Il piatto {piatto} è stato rimosso dal menu.")
            else:# Se il piatto non è presente nel menu
                print(f"Il piatto {piatto} non è presente nel menu.")
        else: 
            print("Password non corretta.")
    # Stampa il menu del ristorante
    def stampa_menu(self):
        print(f"Menu del ristorante {self.nome}:")
        for piatto, prezzo in self.menu.items():# Stampa nome e prezzo di ogni piatto nel menu
            print(f"{piatto}: {prezzo}")

# funzione principale per il menu del ristorante
def menu_ristorante():
    nome = "Fratelli Max 3"
    tipo_cucina = "Italiana"
    ristorante = Ristorante(nome, tipo_cucina)
    
    while True:
        print(" Menu Ristorante:")
        print("1. Descrizione Ristorante")
        print("2. Stato Apertura")
        print("3. Apri Ristorante")
        print("4. Chiudi Ristorante")
        print("5. Aggiungi Piatto al Menu")
        print("6. Rimuovi Piatto dal Menu")
        print("7. Stampa Menu")
        print("8. Esci")
        
        scelta = input("Inserisci il numero della opzione da eseguire: ")
        
        match scelta:
            case "1":
                ristorante.descrivi_ristorante()
            case "2":
                ristorante.stato_apertura()
            case "3":
                ristorante.apri_ristorante()
            case "4":
                ristorante.chiudi_ristorante()
            case "5":
                ristorante.aggiungi_al_menu()
            case "6":
                ristorante.rimuovi_dal_menu()
            case "7":
                ristorante.stampa_menu()
            case "8":
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida.")

menu_ristorante()