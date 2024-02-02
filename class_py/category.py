from class_py.database import Database


class Category:
    def __init__(self):
        self.database = Database("localhost", "root", "1478", "store")

    def add_category(self, name):
        sql = "INSERT INTO category (name) VALUES (%s)"
        self.database.execute_sql(sql, (name,))        

    def delete_category(self, id):
        sql= "DELETE FROM category WHERE id = %s"
        self.database.execute_sql(sql, (id,))        

    def modify_category(self, id, new_name):
        sql= "UPDATE category SET name = %s WHERE id = %s"
        self.database.execute_sql(sql, (new_name, id))        

    def get_all_categories(self):
        sql = "SELECT * FROM category"
        return self.database.fetch_all(sql)