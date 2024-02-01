from database import Database
database = Database()

class Category:
    def __init__(self, database):
        self.database = database

    def add_category(self, name):
        sql = "INSERT INTO category (name) VALUES (%s)"
        self.database.execute_sql(sql, (name,))
        database.base.commit()

    def delete_category(self, id):
        sql= "DELETE FROM category WHERE id = %s"
        self.database.execute_sql(sql, (id,))
        database.base.commit()

    def modify_category(self, id, new_name):
        sql= "UPDATE category SET name = %s WHERE id = %s"
        self.database.execute_sql(sql, (new_name, id))
        database.base.commit()

    def get_all_categories(self):
        sql = "SELECT * FROM category"
        return self.database.fetch_all(sql)