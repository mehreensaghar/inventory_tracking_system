import sqlite3

def get_connection():
    conn=sqlite3.connect('inventory.db')
    return conn

def init_db():
    conn=get_connection()
    cursor=conn.cursor()
    
    #Create Product table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Product(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sku TEXT UNIQUE NOT NULL);
    ''')

    #Create StockMovement table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS StockMovement (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            type TEXT CHECK(type IN ('stock_in', 'sale', 'manual_removal')),
            quantity INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(product_id) REFERENCES Product(id)
        );
    ''')

    conn.commit()
    conn.close()

