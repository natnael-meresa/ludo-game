import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()
        
    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    
    def add(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (part, customer, retailer, price))
        self.conn.commit()
    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()
    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?", (part, customer, retailer, price, id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()
#db = Database('store.db')
#db.add("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
#db.add("Asus Mobo", "Mike Henry", "Microcenter", "360")
#db.add("500w PSU", "Karen Johnson", "Newegg", "80")
#db.add("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
#db.add("8GB DDR4 Ram", "Alberrt Kingston", "Microcenter", "260")
#db.add("500w PSU", "Karen Johnson", "Newegg", "80")
#db.add("2GB DDR4 Ram", "Alberrt Kingston", "Microcenter", "100")


    
        
