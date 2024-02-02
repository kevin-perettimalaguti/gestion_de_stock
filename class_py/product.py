from class_py.database import Database

class Product:
    def __init__(self):
        self.database = Database("localhost", "root", "1478", "store")             
        
    def add_product(self, name, description, price, quantity, id_category):
        sql = f"INSERT INTO product (name, description, price, quantity, id_category)" \
              f" VALUES ('{name}', '{description}', {price}, {quantity}, {id_category});" 
        self.database.execute_sql(sql)        
        
    def remove_product(self, id_product):
        self.database.execute_sql(f"DELETE FROM product WHERE id = {id_product};")        
        
    def modify_product(self, id_product, new_name, new_description, new_price, new_quantity, new_id_category):
        sql = f"UPDATE product" \
              f" SET " \
              f" name = '{new_name}'," \
              f" description = '{new_description}'," \
              f" price = {new_price}," \
              f" quantity = {new_quantity}," \
              f" id_category = {new_id_category}" \
              f" WHERE id = {id_product};"
        self.database.execute_sql(sql)

    def get_all_products(self):
        sql = "SELECT * FROM product"
        return self.database.fetch_all(sql)
    
    def fetch_all_products(self):
        sql = "SELECT * FROM product"
        self.database.cursor.execute(sql)
        return self.database.cursor.fetchall()
      
   
        
    
    
    
        
                    

        