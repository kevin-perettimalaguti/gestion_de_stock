from tkinter import *
from tkinter import ttk
# from class_py.product import Product
# from class_py.category import Category

# product = Product()
# category = Category()

class Interface:
    def __init__(self, database):
        self.database = database
        self.fenetre = Tk()
        self.fenetre.geometry("900x500")
        self.fenetre.title("Stockage store")
        self.create_widgets()

    def create_widgets(self):
        #======Ajouter un produit========#
        label_add_productt = Label(self.fenetre, text="Ajouter un produit", font=("Arial 13"), width=16, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_add_productt.place(x=470, y=50)

        # Name
        label_name_add = Label(self.fenetre, text="Nom", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_name_add.place(x=400, y=100)
        name_add = Entry(self.fenetre, width=10)
        name_add.place(x=400, y=130)

        # Description
        label_description_add = Label(self.fenetre, text="Description", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_description_add.place(x=490, y=100)
        description_add = Text(self.fenetre, height=1, width=10)
        description_add.place(x=490, y=130)

        # Price
        label_price_add = Label(self.fenetre, text="Prix", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_price_add.place(x=600, y=100)
        price_add = Entry(self.fenetre, width=10)
        price_add.place(x=600, y=130) 

        # Quantity
        label_quantity_add = Label(self.fenetre, text="Quantité", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_quantity_add.place(x=700, y=100)
        quantity_add = Entry(self.fenetre, width=10)
        quantity_add.place(x=700, y=130)

        # Category
        label_category_add = Label(self.fenetre, text="Categorie", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_category_add.place(x=800, y=100)
        category_add = ttk.Combobox(self.fenetre, width=5, font=("Arial 11"))
        category_add.place(x=800, y=130)

        bouton_add = Button(self.fenetre, text="Ajouter", command=None , width=6, font=("Arial", 11), height=1)
        bouton_add.place(x=630, y=45) 


        #======Modifier un produit======#
        label_add_productt_modif = Label(self.fenetre, text="Modifier un produit", font=("Arial 13"), width=16, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_add_productt_modif.place(x=470, y=200)

        # Name
        label_name_modif = Label(self.fenetre, text="Nom", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_name_modif.place(x=400, y=250)
        name_modif = Entry(self.fenetre, width=10)
        name_modif.place(x=400, y=280)

        # Description
        label_description_modif = Label(self.fenetre, text="Description", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_description_modif.place(x=490, y=250)
        description_modif = Text(self.fenetre, height=1, width=10)
        description_modif.place(x=490, y=280)

            # Price
        label_price_modif = Label(self.fenetre, text="Prix", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_price_modif.place(x=600, y=250)
        price_modif= Entry(self.fenetre, width=10)
        price_modif.place(x=600, y=280) 

        # Quantity
        label_quantity_modif = Label(self.fenetre, text="Quantité", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_quantity_modif.place(x=700, y=250)
        quantity_modif= Entry(self.fenetre, width=10)
        quantity_modif.place(x=700, y=280)

        # Category
        label_category_modif= Label(self.fenetre, text="Categorie", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_category_modif.place(x=800, y=250)
        category_modif = ttk.Combobox(self.fenetre, width=5, font=("Arial 11"))
        category_modif.place(x=800, y=280)

        bouton_modif = Button(self.fenetre, text="Valider", command=None , width=6, font=("Arial", 11), height=1)
        bouton_modif.place(x=640, y= 195) 
        # command=product.add_product()
 

        #=====Delete product=====#
        label_add_productt_add = Label(self.fenetre, text="Supprimer un produit", font=("Arial 13"), width=20, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_add_productt_add.place(x=470, y=340)

        #id
        id_product = ttk.Combobox(self.fenetre, width=5, font=("Arial 11"))
        id_product.place(x=425, y= 380)
        
        bouton_supp = Button(self.fenetre, text="Supprimer", command=None , width=8, font=("Arial", 11), height=1)
        bouton_supp.place(x=520, y= 375) 
 

        #=====Affichage de la base de donnée=====#
        board = ttk.Treeview(self.fenetre, columns=("id", "Nom", "Description", "Prix", "Quantité","id_categorie"), show="headings")

        # board.insert()

        # Configurer les colonnes
        board.heading("id", text="id")
        board.heading("Nom", text="Nom")
        board.heading("Description", text="Description")
        board.heading("Prix", text="Prix")
        board.heading("Quantité", text="Quantité")
        board.heading("id_categorie", text="id_categorie")
    
    def run(self):
        self.fenetre.mainloop()


