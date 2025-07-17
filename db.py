import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@12345",
        database="sweet_shop" # Ensure this matches your database name
    )

def get_all_sweets(query='', sort_by='id'):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = f"SELECT * FROM sweets WHERE name LIKE %s OR category LIKE %s ORDER BY {sort_by}"
    like = f"%{query}%"
    cursor.execute(sql, (like, like))
    sweets = cursor.fetchall()
    cursor.close()
    conn.close()
    return sweets

def add_sweet(sweet):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO sweets (id, name, category, price, quantity) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (sweet['id'], sweet['name'], sweet['category'], sweet['price'], sweet['quantity']))
    conn.commit()
    cursor.close()
    conn.close()

def delete_sweet(sweet_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM sweets WHERE id = %s"
    cursor.execute(sql, (sweet_id,))
    conn.commit()
    cursor.close()
    conn.close()

def purchase_sweet(sweet_id, qty):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE sweets SET quantity = quantity - %s WHERE id = %s AND quantity >= %s"
    cursor.execute(sql, (qty, sweet_id, qty))
    conn.commit()
    cursor.close()
    conn.close()   

def restock_sweet(sweet_id, qty):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE sweets SET quantity = quantity + %s WHERE id = %s"
    cursor.execute(sql, (qty, sweet_id))
    conn.commit()
    cursor.close()
    conn.close()