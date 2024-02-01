from database import Database
database = Database()

class Category:
    def __init__(self):
        pass
    
    def add_category(self, name):
        sql = f"INSERT INTO product (name,description,price,quantity,id_category)" \
            "VALUES" \
                f"('{name}');" 
        database.request.execute(sql)
        database.base.commit()
    
    def modify_category(self, id_category, new_name):
        sql = "UPDATE category" \
            f"SET name = {new_name}," \
                f"WHERE id = {id_category};"
        database.request.execute(sql)
        database.base.commit()
        
    def remove_category(self, id_category):
        sql = "DELETE FROM product" \
            f"WHERE id = {id_category}"
        database.request.execute(sql)
        database.base.commit()