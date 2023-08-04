
import sqlite3
from datetime import datetime
from io import BytesIO
# Initialize the SQLite database connection
conn = sqlite3.connect('app_database.db')
cursor = conn.cursor()

# Function to create the database tables
def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS card_payments (
                    id INTEGER PRIMARY KEY,
                    pin_number INTEGER,
                    visa_count INTEGER,
                    mastercard_count INTEGER,
                    maestro_count INTEGER,
                    vpay_count INTEGER,
                    datetime DATETIME)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS gift_cards (
                    id INTEGER PRIMARY KEY,
                    description TEXT,
                    source TEXT,
                    amount REAL,
                    datetime DATETIME)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS invoices (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    bussiness_name TEXT,
                    bussiness_code TEXT,
                    amount REAL,
                    description TEXT,
                    datetime DATETIME)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS vault_cash (
                    id INTEGER PRIMARY KEY,
                    value REAL,
                    amount INTEGER,
                    datetime DATETIME)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS kassastrook_data (
                    id INTEGER PRIMARY KEY,
                    kassastrook_code TEXT,
                    code INTEGER,
                    amount TEXT,
                    datetime DATETIME)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS external_purchases (
                    id INTEGER PRIMARY KEY,
                    amount INTEGER,
                    description TEXT,
                    proof BLOB,
                    datetime TEXT)''')
    conn.commit()

## Functions to interact with card payments database
def insert_card_payments(conn,pin_number,visa_count,mastercard_count,maestro_count,vpay_count):
    cursor = conn.cursor()
    current_datetime = datetime.now().strftime('%d-%m-%Y')
    cursor.execute("INSERT INTO card_payments (visa_count, pin_number, mastercard_count, maestro_count, vpay_count, datetime) VALUES (?, ?, ?, ?, ?, ?)",
                   (visa_count,pin_number, mastercard_count, maestro_count, vpay_count, current_datetime))
    conn.commit()
def delete_card_payment(conn,date,pin_no):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM card_payments WHERE datetime=? AND pin_number=?", (date, pin_no))
    conn.commit()
def update_card_payment(conn,pin_number,visa_count,mastercard_count,maestro_count,vpay_count,date):
    cursor = conn.cursor()
    cursor.execute("UPDATE card_payments SET visa_count=?, pin_number=?, mastercard_count=?, maestro_count=?, vpay_count=? WHERE pin_number=? AND datetime=?",
                   (visa_count,pin_number, mastercard_count, maestro_count, vpay_count, pin_number,date))
    conn.commit()
def get_all_card_payments(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM card_payments")
    rows = cursor.fetchall()
    return rows
def get_card_payment(conn,date):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM card_payments WHERE DATE=?", (date,))
    rows = cursor.fetchall()
    return rows

## Funtions to interact with gift cards database
def insert_gift_card(conn,description, source, amount):
    cursor=conn.cursor()
    current_datetime = datetime.now().strftime('%d-%m-%Y')
    cursor.execute("INSERT INTO gift_cards (description, source, amount, datetime) VALUES (?, ?, ?, ?)",
                   (description, source, amount, current_datetime))
    conn.commit()
def delete_gift_card(conn,date):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gift_cards WHERE datetime=?", (date,))
    conn.commit()
def update_gift_card(conn, description, source, amount, date):
    cursor = conn.cursor()
    cursor.execute("UPDATE gift_cards SET description=?, source=?, amount=? WHERE datetime=?",
                   (description, source, amount, date))
    conn.commit()
def get_all_gift_cards(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gift_cards")
    rows = cursor.fetchall()
    return rows
def get_gift_card(conn,card_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gift_cards WHERE id=?", (card_id,))
    rows = cursor.fetchall()
    return rows

## Functions to interact with invoices database
def insert_invoice(conn, name, email, bussiness_name, bussiness_code, amount, description):
    cursor = conn.cursor()
    current_datetime = datetime.now().strftime('%d-%m-%Y')
    cursor.execute("INSERT INTO invoices (name, email, bussiness_name, bussiness_code, amount, description, datetime) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (name, email, bussiness_name, bussiness_code, amount, description, current_datetime))
    conn.commit()
def delete_invoice(conn,invoice_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM invoices WHERE id=?", (invoice_id,))
    conn.commit()
def update_invoice(conn, name, email, bussiness_name, bussiness_code, amount, description,date):
    cursor = conn.cursor()
    cursor.execute("UPDATE invoices SET name=?, email=?, bussiness_name=?, bussiness_code=?, amount=?, description=? WHERE datetime=?",
                   (name,email,bussiness_name,bussiness_code,amount ,description, date))
    conn.commit()
def get_all_invoices(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invoices")
    rows = cursor.fetchall()
    return rows


## Functins to interact with vault cash database
def insert_vault_cash(conn, values, amounts):
    cursor = conn.cursor()
    current_datetime = datetime.now().strftime('%d-%m-%Y')

    for value, amount in zip(values, amounts):
        cursor.execute("INSERT INTO vault_cash (value, amount, datetime) VALUES (?, ?, ?)", (value, amount, current_datetime))
    conn.commit()
def delete_vault_cash(conn, vault_cash_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vault_cash WHERE id=?", (vault_cash_id,))
    conn.commit()
def update_vault_cash(conn, value, amount,date):
    cursor = conn.cursor()
    cursor.execute("UPDATE vault_cash SET amount=? WHERE datetime=? AND value=?",
                       (amount, date,  value))
    conn.commit()
def get_all_vault_cash(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vault_cash")
    rows = cursor.fetchall()
    return rows


## Funtions to interact with kassastrook database
def insert_kassastrook_data(conn,kassastrook_code, code, amount):
    cursor = conn.cursor()
    current_datetime = datetime.now().strftime('%d-%m-%Y')
    cursor.execute("INSERT INTO kassastrook_data (kassastrook_code, code, amount, datetime) VALUES (?, ?, ?, ?)",
                   (kassastrook_code, code, amount, current_datetime))
    conn.commit()
def delete_kassastrook_data(conn,kassastrook_data_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kassastrook_data WHERE id=?", (kassastrook_data_id,))
    conn.commit()
def update_kassastrook_data(conn,amount, date,kassastrook_code):
    cursor = conn.cursor()
    cursor.execute("UPDATE kassastrook_data SET amount=? WHERE datetime=? AND kassastrook_code=? ",
                   (amount,date,kassastrook_code))
    conn.commit()
def get_all_kassastrook_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kassastrook_data")
    rows = cursor.fetchall()
    return rows
def delete_kassastrook_data_by_kassastrook_code(conn,kassastrook_code):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kassastrook_data WHERE kassastrook_code=?", (kassastrook_code,))
    conn.commit()


## Functions to interact with external purchases database
def insert_external_purchase(conn, amount, description, proof):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor = conn.cursor()
    proof_bytes = BytesIO(proof.read())

    cursor.execute("INSERT INTO external_purchases (amount, description, proof, datetime) VALUES (?, ?, ?, ?)",
                   (amount, description, proof_bytes.getvalue(), current_datetime))
    conn.commit()
def delete_external_purchase(conn,external_purchase_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM external_purchases WHERE id=?", (external_purchase_id,))
    conn.commit()
def update_external_purchase(conn, amount, description, proof, date):
    cursor = conn.cursor()
    try:
        proof_bytes = BytesIO(proof.read())
    except:
        proof_bytes = None
    cursor.execute("UPDATE external_purchases SET amount=?, description=?, proof=? WHERE datetime=?",
                   (amount, description, proof_bytes.getvalue(), date))
    conn.commit()
def get_all_external_purchases(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM external_purchases")
    rows = cursor.fetchall()
    return rows
