from class_py.interface import Interface
from class_py.database import Database

db = Database()
stock_store = Interface(db)
stock_store.run()

# if __name__ == "__main__":
#     db = DatabaseConnect('localhost', 'root', 'Teddy2212!', 'store')
#     gui = Interface(db)
#     gui.run()