from tkinter import *
from tkinter import ttk, messagebox
from class_py.product import Product
from class_py.category import Category
from class_py.database import Database
class Interface:
    def __init__(self):
        self.database = Database("localhost", "root", "1478", "store")
        self.product = Product()
        self.category = Category()
        self.fenetre = Tk()
        self.fenetre.geometry("900x500")
        self.fenetre.title("Stockage store")
        self.widgets_add()
        self.widgets_modify()
        self.widgets_delete()
        self.widgets_display_database()

    def widgets_add(self):
        label_add_productt = Label(self.fenetre, text="Add product", font=("Arial 13"), width=16, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_add_productt.place(x=470, y=50)

        # Name
        label_name_add = Label(self.fenetre, text="Name", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
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
        label_price_add = Label(self.fenetre, text="Price", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_price_add.place(x=600, y=100)
        price_add = Entry(self.fenetre, width=10)
        price_add.place(x=600, y=130) 

        # Quantity
        label_quantity_add = Label(self.fenetre, text="Quantity", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_quantity_add.place(x=700, y=100)
        quantity_add = Entry(self.fenetre, width=10)
        quantity_add.place(x=700, y=130)

        # Category
        label_category_add = Label(self.fenetre, text="Category", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_category_add.place(x=800, y=100)
        category_add = ttk.Combobox(self.fenetre, width=5, font=("Arial 11"))
        category_add.place(x=800, y=130)
        return name_add, description_add, price_add, quantity_add, category_add
        # bouton_add = Button(self.fenetre, text="Ajouter", command=None , width=6, font=("Arial", 11), height=1)
        # bouton_add.place(x=630, y=45) 
    
    def add_product(self):
        name = self.widgets_add[0]
        description = self.widgets_add[1]
        price = self.widgets_add[2]
        quantity = self.widgets_add[3]
        category = self.widgets_add[4]
        
        if name is not None:
            self.product.add_product(name, description, price, quantity, category)            
        else:
            messagebox.showerror(f"Error, product not add")

    def widgets_modify(self):
        label_add_productt_modif = Label(self.fenetre, text="Modify product", font=("Arial 13"), width=16, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_add_productt_modif.place(x=470, y=200)

        # Name
        label_name_modif = Label(self.fenetre, text="Name", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
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
        label_price_modif = Label(self.fenetre, text="Price", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_price_modif.place(x=600, y=250)
        price_modif= Entry(self.fenetre, width=10)
        price_modif.place(x=600, y=280) 

        # Quantity
        label_quantity_modif = Label(self.fenetre, text="Quantity", font=("Arial 11"), width=10, height=1, padx=5, pady=1, relief="flat",
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

        # bouton_modif = Button(self.fenetre, text="Valider", command=None, width=6, font=("Arial", 11), height=1)
        # bouton_modif.place(x=640, y= 195) 
        # command=product.add_product()
        return name_modif, description_modif, price_modif, quantity_modif, category_modif   

    def widgets_delete(self):
        label_add_productt_add = Label(self.fenetre, text="Supprimer un produit", font=("Arial 13"), width=20, height=1, padx=5, pady=1, relief="flat",
                     anchor=NW)
        label_add_productt_add.place(x=470, y=340)

        #id
        id_product = ttk.Combobox(self.fenetre, width=5, font=("Arial 11"))
        id_product.place(x=425, y= 380)
        
        # bouton_supp = Button(self.fenetre, text="Supprimer", command=None , width=8, font=("Arial", 11), height=1)
        # bouton_supp.place(x=520, y= 375)
        return id_product
    
    def insert_product_on_board(self):
        for item in self.board.get_children():
            self.board.delete(item)
        
        products = self.product.display_all_product()
        for product in products:
            product_id, name, description, price, quantity, category_id = product

            category_name = self.get_category_name_from_id(category_id)

            self.board.insert("", 'end', values=(product_id, name, description, price, quantity, category_name, category_id))
            
    def get_category_name_from_id(self, category_id):
        categories = self.category.get_all_categories()
        for category in categories:
            if category[0] == category_id:
                return category[1]         
 

    def widgets_display_database(self):
        self.board = ttk.Treeview(self.fenetre)
        self.board['columns'] = ('ID', 'Name', 'Description', 'Price', 'Quantity', 'Category', 'Category ID')

        self.board.column("#0", width=0,)
        self.board.column("ID", width=40)
        self.board.column('Name', width=80)
        self.board.column("Description", width=120)
        self.board.column("Price", width=60)
        self.board.column("Quantity", width=60)
        self.board.column("Category", width=60)
        self.board.column("Category ID", width=80)

        # Create Headings
        self.board.heading("#0", text="", width=0)
        self.board.heading("ID", text="ID")
        self.board.heading("Name", text="Name")
        self.board.heading("Description", text="Description")
        self.board.heading("Price", text="Price")
        self.board.heading("Quantity", text="Quantity")
        self.board.heading("Category", text="Category")
        self.board.heading("Category ID", text="Category ID")

        self.board.pack(expand=True)
        
    def refresh_data(self):
        self.insert_product_on_board()
    
    def running(self):
        self.fenetre.mainloop()


