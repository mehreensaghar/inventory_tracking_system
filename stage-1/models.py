from database import get_connection

def add_product(name, sku):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO Product (name, sku) VALUES (?, ?)", (name, sku))
    conn.commit()
    conn.close()

def record_stock_movement(sku, movement_type, quantity):
    conn=get_connection()
    cursor=conn.cursor()
    
    # Get product ID
    cursor.execute("SELECT id FROM Product WHERE sku = ?", (sku,))
    result=cursor.fetchone()
    
    if not result:
        print("Product not found.")
        return

    product_id=result[0]
    cursor.execute('''
        INSERT INTO StockMovement (product_id, type, quantity)
        VALUES (?, ?, ?)
    ''',(product_id,movement_type,quantity))

    conn.commit()
    conn.close()

def get_inventory():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''
        SELECT p.name, p.sku, 
            SUM(CASE WHEN s.type = 'stock_in' THEN s.quantity ELSE 0 END) -
            SUM(CASE WHEN s.type IN ('sale', 'manual_removal') THEN s.quantity ELSE 0 END)
        AS quantity
        FROM Product p
        LEFT JOIN StockMovement s ON p.id = s.product_id
        GROUP BY p.id;
    ''')
    
    rows =cursor.fetchall()
    conn.close()
    return rows

