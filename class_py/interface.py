import tkinter as tk
from tkinter import ttk, messagebox
from class_py.database import Database
from class_py.product import Product
from class_py.category import Category

class Interface:
    def __init__(self):
        self.database = Database("localhost", "root", "1478", "store")
        self.product = Product()
        self.category = Category()
        self.fenetre = tk.Tk()
        self.fenetre.title("Storage stock")
        self.insert_data_on_board()
        self.configure_widgets()        

    def configure_widgets(self):
        self.configure_product_management()
        self.configure_category_management()

    def insert_data_on_board(self):
        self.board = ttk.Treeview(self.fenetre)
        self.board['columns'] = ('ID', 'Name', 'Description', 'Price', 'Quantity', 'Category', 'Category ID')

        self.configure_columns_and_headings()
        
        self.refresh_button = tk.Button(self.fenetre, text="Refresh", command=self.refresh_data)
        self.refresh_button.pack(side=tk.RIGHT, anchor=tk.N)

        self.board.pack(fill=tk.BOTH, expand=True)

    def configure_columns_and_headings(self):
        columns = [
            ("#0", 0, tk.W, ""),
            ("ID", 40, tk.CENTER, "ID"),
            ("Name", 80, tk.CENTER, "Name"),
            ("Description", 120, tk.CENTER, "Description"),
            ("Price", 60, tk.CENTER, "Price"),
            ("Quantity", 60, tk.CENTER, "Quantity"),
            ("Category", 60, tk.CENTER, "Category"),
            ("Category ID", 80, tk.CENTER, "Category ID")
        ]

        for col, width, anchor, heading in columns:
            self.board.column(col, width=width, anchor=anchor)
            self.board.heading(col, text=heading, anchor=anchor)

    def configure_product_management(self):
        data_frame = tk.Frame(self.fenetre)
        data_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        labels_entries = [
            ("Name:", 0, 0),
            ("Description:", 1, 0),
            ("Price:", 2, 0),
            ("Quantity:", 3, 0),
            ("Category:", 4, 0)
        ]

        for label, row, col in labels_entries:
            tk.Label(data_frame, text=label).grid(row=row, column=col, sticky=tk.W)

        self.name_entry = tk.Entry(data_frame)
        self.description_entry = tk.Entry(data_frame)
        self.price_entry = tk.Entry(data_frame)
        self.quantity_entry = tk.Entry(data_frame)
        self.category_combobox = ttk.Entry(data_frame)

        entries = [
            (self.name_entry, 0, 1),
            (self.description_entry, 1, 1),
            (self.price_entry, 2, 1),
            (self.quantity_entry, 3, 1),
            (self.category_combobox, 4, 1)
        ]

        for entry, row, col in entries:
            entry.grid(row=row, column=col)

        buttons = [
            ("Add Product", self.add_product, 5, 0),
            ("Modify Product", self.modify_product, 5, 1),
            ("Delete Product", self.remove_product, 5, 2)
        ]

        for text, command, row, col in buttons:
            tk.Button(data_frame, text=text, command=command).grid(row=row, column=col, pady=5)

    def configure_category_management(self):
        fill_management_data = tk.Frame(self.fenetre)
        fill_management_data.pack(side=tk.RIGHT, padx=10, pady=10)

        labels_entries = [
            ("Category Name:", 0, 0),
            ("Category ID (for modify/delete):", 1, 0)
        ]

        for label, row, col in labels_entries:
            tk.Label(fill_management_data, text=label).grid(row=row, column=col, sticky=tk.W)

        self.category_name_entry = tk.Entry(fill_management_data)
        self.category_id_entry = tk.Entry(fill_management_data)

        entries = [
            (self.category_name_entry, 0, 1),
            (self.category_id_entry, 1, 1)
        ]

        for entry, row, col in entries:
            entry.grid(row=row, column=col)

        buttons = [
            ("Add Category", self.add_category, 2, 0),
            ("Modify Category", self.modify_category, 2, 1),
            ("Delete Category", self.remove_category, 2, 2)
        ]

        for text, command, row, col in buttons:
            tk.Button(fill_management_data, text=text, command=command).grid(row=row, column=col, pady=5)

    def populate_product_tree(self):
        for item in self.board.get_children():
            self.board.delete(item)

        products = self.product.fetch_all_products()
        for product in products:
            product_id, name, description, price, quantity, category_id = product

            category_name = self.get_category_name_from_id(category_id)

            self.board.insert("", 'end', values=(product_id, name, description, price, quantity, category_name, category_id))

    def fill_category_combobox(self):
        categories = self.category.get_all_categories()
        category_names = [category[1] for category in categories]
        self.category_combobox['values'] = category_names

    def get_category_id_from_name(self, category_name):
        categories = self.category.get_all_categories()
        for category in categories:
            if category[1] == category_name:
                return category[0]

    def add_product(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        category_name = self.category_combobox.get()

        id_category = self.get_category_id_from_name(category_name)

        if id_category is not None:
            self.product.add_product(name, description, price, quantity, id_category)
            self.populate_product_tree()
        else:
            messagebox.showerror("Error", "Category not found")

    def remove_product(self):
        selected_item = self.board.selection()
        if selected_item:
            product_id = self.board.item(selected_item)['values'][0]
            self.product.remove_product(product_id)
            self.populate_product_tree()
        else:
            pass

    def modify_product(self):
        selected_item = self.board.selection()
        if selected_item:
            product_id = self.board.item(selected_item)['values'][0]

            new_name = self.name_entry.get()
            new_description = self.description_entry.get()
            new_price = self.price_entry.get()
            new_quantity = self.quantity_entry.get()
            new_id_category = self.category_combobox.get()

            self.product.modify_product(product_id, new_name, new_description, new_price, new_quantity, new_id_category)
            self.populate_product_tree()
        else:
            pass

    def add_category(self):
        category_name = self.category_name_entry.get()
        self.category.add_category(category_name)
        self.fill_category_combobox()

    def remove_category(self):
        category_id = self.category_id_entry.get()
        self.category.delete_category(category_id)
        self.fill_category_combobox()

    def modify_category(self):
        category_id = self.category_id_entry.get()
        new_name = self.category_name_entry.get()
        self.category.modify_category(category_id, new_name)
        self.fill_category_combobox()

    def refresh_data(self):
        self.populate_product_tree()

    def get_category_name_from_id(self, category_id):
        categories = self.category.get_all_categories()
        for category in categories:
            if category[0] == category_id:
                return category[1]

    def running(self):
        self.fenetre.geometry("700x500")
        self.fenetre.mainloop()