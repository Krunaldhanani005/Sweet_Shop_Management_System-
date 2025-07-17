from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_all_sweets, add_sweet, delete_sweet, purchase_sweet, restock_sweet
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key' 


@app.route('/')                                        #Displays a list of all sweets available in the shop.
def index():   
    query = request.args.get('q', '').lower()
    sort_by = request.args.get('sort', 'id')
    sweets = get_all_sweets(query, sort_by)
    return render_template('index.html', sweets=sweets, query=query, sort_by=sort_by)

@app.route('/add', methods=['POST'])                    #Adds a new sweet to the shop.
def add():
    sweet = {
        'id': request.form['id'],
        'name': request.form['name'],
        'category': request.form['category'],
        'price': float(request.form['price']),
        'quantity': int(request.form['quantity'])
    }
    try:                                                #Attempt to add the sweet to the database.
        add_sweet(sweet)
    except mysql.connector.IntegrityError:
        flash("ID should be unique!", "danger")
    return redirect(url_for('index'))

@app.route('/delete/<sweet_id>', methods=['POST'])      #Deletes a sweet from the shop.
def delete(sweet_id):
    delete_sweet(sweet_id)
    return redirect(url_for('index'))

@app.route('/purchase/<sweet_id>', methods=['POST'])    #Purchases a sweet from the shop.
def purchase(sweet_id):
    qty = int(request.form['qty'])
    purchase_sweet(sweet_id, qty)
    return redirect(url_for('index'))

@app.route('/restock/<sweet_id>', methods=['POST'])     #Restocks a sweet in the shop.
def restock(sweet_id):
    qty = int(request.form['qty'])
    restock_sweet(sweet_id, qty)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)