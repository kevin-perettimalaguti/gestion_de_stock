from database import Database
database = Database()

class Product():
    def __init__(self, database):
        self.database = database               
        
    def add_product(self, name, description, price, quantity, id_category):
        sql = f"INSERT INTO product (name,description,price,quantity,id_category)" \
            "VALUES" \
                f"('{name}','{description}',{price},{quantity},{id_category});" 
        self.database.execute_sql(sql)
        database.base.commit()
        
    def remove_product(self, id_product):
        self.database.execute_slq(f"DELETE FROM product WHERE id = {id_product};")
        database.base.commit()
        
    def modify_product(self, id_product, new_name, new_description, new_price, new_quantity, new_id_category):
        sql = "UPDATE product" \
            f"SET" \
            f"name = {new_name}," \
            f"description = {new_description}," \
            f"price = {new_price}," \
            f"quantity = {new_quantity}," \
            f"id_category = {new_id_category}," \
            f"WHERE id = {id_product}"
        self.database.excute.sql(sql(id_product, new_name, new_description,new_price, new_quantity, new_id_category))
        database.base.commit()
        
    def display_all_product(self):
        sql = "SELECT product.id, product.name, product.description, product.price, product.quantity, product.id_category category.nom AS nom_category " \
          "FROM product " \
          "LEFT JOIN category ON product.id_category = category.id;"
        self.database.request.execute(sql)
        all_product = self.database.request.fetchall()
        for row in all_product:
            print(f"{row[0]} {row[1]} | Prix: {row[2]} | Quantité : {row[3]} | Catégory : {row[4]}")
        return all_product       
   
        
    # def modify_price(self, id_product, new_price):
    #     sql = f"UPDATE product" \
    #         f"SET price = {new_price}" \
    #             f"WHERE id = {id_product};"
    #     self.database.request.execute(sql)
    #     self.database.base.commit()
        
    # def modify_quantity(self, id_product, new_quantity):
    #     sql = f"UPDATE product" \
    #         f"SET quantity = {new_quantity}" \
    #             f"WHERE id = {id_product};"
    #     self.request.execute(sql)
    #     self.base.commit()
    
    
        
                    

        