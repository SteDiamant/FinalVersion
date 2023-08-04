import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

from database import *
import sqlite3
def show_card_payments():
    st.markdown('--------')
    card_payments_sections = st.container()
    with card_payments_sections:
        conn=sqlite3.connect('app_database.db')
        st.title('New Card Payments')
        data=get_all_card_payments(conn)
        data=pd.DataFrame(data,columns=['id','pin_number','visa_count','mastercard_count','maestro_count','vpay_count','datetime'])
        date=st.selectbox('Select Date',data['datetime'].unique())
        pin_no=st.selectbox('Pin_No',('1','2','3','4','5','6','7'))
        st.write(data)
        c1,c2,c3,c4=st.columns(4)
        try:
            with c1:
                visa_count = st.number_input(label='Visa',min_value=0.0,step=1.0,key='visa',value=float(data['visa_count'].values[0]))
            with c2:
                mastercard_count = st.number_input(label='Mastercard',min_value=0.0,step=1.0,key='mastercard',value=float(data['mastercard_count'].values[0]))
            with c3:
                maestro_count = st.number_input(label='Maestro',min_value=0.0,step=1.0,key='maestro',value=float(data['maestro_count'].values[0]))
            with c4:
                vpay_count = st.number_input(label='Vpay',min_value=0.0,step=1.0,key='vpay',value=float(data['vpay_count'].values[0]))
            
            old_count=data['visa_count'].values[0]+data['mastercard_count'].values[0]+data['maestro_count'].values[0]+data['vpay_count'].values[0] 
            new_count=visa_count+mastercard_count+maestro_count+vpay_count
            st.write('Old Total:',str(old_count))
            st.write('New Total:',str(new_count))
        except:
            pass
        
        
        # Layout for buttons
        col1, col2 = st.columns(2)
        if col1.button(label='Update Card Payment'):
            update_card_payment(conn, pin_no, visa_count, mastercard_count, maestro_count, vpay_count, date)
            st.experimental_rerun()
        if col2.button(label='Delete Card Payment'):
            delete_card_payment(conn, date, pin_no)
            st.experimental_rerun()

def show_gift_cards():
    st.markdown('--------')
    gift_card_sections = st.container()
    with gift_card_sections:
        conn=sqlite3.connect('app_database.db')
        st.title('New Card Payments')
        data=get_all_gift_cards(conn)
        data=pd.DataFrame(data,columns=['id','description','source','amount','datetime'])
        date=st.selectbox('Select Date',data['datetime'].unique())
        st.write(data)
        new_description=st.text_area('Description')
        new_source=st.text_input('Source')
        try:
            new_amount=st.number_input(label='Amount',min_value=0.0,step=1.0,key='amount',value=float(data['amount'].values[0]))
        except:
            pass
        col1, col2 = st.columns(2)
        if col1.button(label='Update Gift Card'):
            update_gift_card(conn, new_description, new_source, new_amount, date)
            st.experimental_rerun()
        if col2.button(label='Delete Gift Card'):
            delete_gift_card(conn, date)
            st.experimental_rerun()

def show_vault_cash():
    st.markdown('--------')
    vault_cash_sections = st.container()
    with vault_cash_sections:
        conn=sqlite3.connect('app_database.db')
        st.title('Vault Cash')
        data=get_all_vault_cash(conn)
        data=pd.DataFrame(data,columns=['id','value','amount','datetime'])
        st.write(data)
        date=st.selectbox('Select Date',data['datetime'].unique())
        values = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
        value = st.selectbox('Select Value',values)
        new_amount=st.number_input(label='Amount',min_value=0.0,step=1.0,key='amount',value=float(data['amount'].values[0]))
        col1, col2 = st.columns(2)
        if col1.button(label='Update Vault Cash'):
            update_vault_cash(conn,value,new_amount,date)
            st.experimental_rerun()
        if col2.button(label='Delete Vault Cash'):
            delete_vault_cash(conn)
            st.experimental_rerun()

def show_invoice():
    st.markdown('--------')
    invoice_sections = st.container()
    with invoice_sections:
        conn=sqlite3.connect('app_database.db')
        st.title('Invoice')
        data=get_all_invoices(conn)
        data=pd.DataFrame(data,columns=['id','name','email','bussiness_name','bussiness_code','amount','description','datetime'])
        st.write(data)
        date=st.selectbox('Select Date',data['datetime'].unique())
        new_name=st.text_input('Name')
        new_email=st.text_input('Email')
        new_bussiness_name=st.text_input('Bussiness Name')
        new_bussiness_code=st.text_input('Bussiness Code')
        new_description=st.text_area('Description')
        try:
            new_amount=st.number_input(label='Amount',min_value=0.0,step=1.0,key='amount',value=float(data['amount'].values[0]))
        except ValueError:
            new_amount=0.0
            
        col1, col2 = st.columns(2)
        if col1.button(label='Update Invoice'):
            update_invoice(conn,new_name,new_email,new_bussiness_name,new_bussiness_code,new_amount,new_description,date)
            st.experimental_rerun()
        if col2.button(label='Delete Invoice'):
            delete_invoice(conn)
            st.experimental_rerun()     

def show_kassastrook():
    st.markdown('--------')
    kassastrook_sections = st.container()
    with kassastrook_sections:
        conn=sqlite3.connect('app_database.db')
        st.title('Kassastrook')
        data=get_all_kassastrook_data(conn)
        data=pd.DataFrame(data,columns=['id','kassstrook_code','code','amount','datetime'])
        st.write(data)
        try:    
            date=st.selectbox('Select Date',data['datetime'].unique())
            name=st.selectbox('Select Name',data['kassstrook_code'].unique())
            if data['amount'].values[0] == "":
                data['amount'].values[0]=0
                amount=st.number_input(label='Amount',min_value=0,step=1,key='amount',value=(data['amount'].values[0]))
        except:
            pass
        col1, col2 = st.columns(2)
        if col1.button(label='Update Kassastrook'):
            update_kassastrook_data(conn,amount,date,name)
            st.experimental_rerun()
        if col2.button(label='Delete Kassastrook'):
            delete_kassastrook_data(conn)
            st.experimental_rerun()

def show_external_puchases():
    st.markdown('--------')
    external_puchases_sections = st.container()
    with external_puchases_sections:
        conn=sqlite3.connect('app_database.db')
        st.title('External Puchases')
        data=get_all_external_purchases(conn)
        data=pd.DataFrame(data,columns=['id','amount','description','proof','datetime'])
        st.write(data)

        date=st.selectbox('Select Date',data['datetime'].unique())
        new_description=st.text_area('Description')
        file_contents = st.file_uploader(label='Proof', key='proof_migrations', type=['png', 'jpg', 'pdf'])
        new_amount = st.number_input(label='Amount', min_value=0.0, step=1.0, key='amount', value=float(data['amount'].values[0]))
        if file_contents is not None:
            # Correct usage for file-like objects returned by file_uploader
            new_proof = file_contents.read()
            # Process the file_contents or save it to disk, etc.
            new_amount=st.number_input(label='Amount',min_value=0.0,step=1.0,key='amount',value=float(data['amount'].values[0]))
           
    if st.button(label='Update External Puchases'):
        update_external_purchase(conn,new_amount,new_description,new_proof,date)
        st.experimental_rerun()
    if st.button(label='Delete External Puchases'):
        delete_external_purchase(conn)
        st.experimental_rerun()
def main():
    conn = sqlite3.connect('app_database.db')

    st.title("Kasopmaak")

    with st.form(key='Card Payments'):
        st.title('New Card Payments')
        pin_no=st.selectbox('Pin_No',('1','2','3','4','5','6','7'))
        c1,c2,c3,c4=st.columns(4)
        with c1:
            visa_count = st.number_input(label='Visa',min_value=0,step=1,key='visa')
        with c2:
            mastercard_count = st.number_input(label='Mastercard',min_value=0,step=1,key='mastercard')
        with c3:
            maestro_count = st.number_input(label='Maestro',min_value=0,step=1,key='maestro')
        with c4:
            vpay_count = st.number_input(label='Vpay',min_value=0,step=1,key='vpay')
            
        total=visa_count+mastercard_count+maestro_count+vpay_count
        st.write('Total:',str(total))
        if st.form_submit_button(label='submit_card_payments'):
            insert_card_payments(conn,pin_no,visa_count,mastercard_count,maestro_count,vpay_count)
            st.success('Data inserted successfully')
            conn.close()
    st.markdown("----------------------------------")
    with st.form(key='GiftCard'):
            st.title('New Gift Card')
            descrtption=st.text_area("Description")
            source=st.text_input("Source")
            amount=st.number_input("Amount")
            if st.form_submit_button(label='Submit_GiftCard'):
                insert_gift_card(conn,descrtption,source,amount)
                st.success('Gift Card Created!')
                conn.close()
    st.markdown("----------------------------------")
    with st.form(key="New Invoice"):
            st.title('New Invoice')
            name=st.text_input(label='Contact Person',key='name_invoice')
            email=st.text_input(label='Debiteur Email',key='email_invoice')

            placeholder_dict = {'CONCORDIA': ['CONC', 'CON DB', 'CONCO']}

            bussiness_name=st.text_input(label='Bussiness Name',key='bussiness_name_invoice')
            bussiness_code = st.text_input(label='Business Code',key='bussiness_code_invoice',placeholder=placeholder_dict.get(bussiness_name, 'XXXX'))

            amount=st.number_input("amount",key='amount_invoice')
            description=st.text_area("Description",key='description_invoice')
            if st.form_submit_button(label='Submit_Invoice'):
                insert_invoice(conn, name, email, bussiness_name, bussiness_code, amount, description)
                st.success('Invoice Created!')
                conn.close()
    st.markdown("----------------------------------")
    c1,c2=st.columns([1,1])
    with c1:
        with st.form(key='VaultCash'):
            # Values for cash
            values = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]

            # Initialize amounts list with zeros
            amounts = [0] * len(values)

            # Create Streamlit form
            st.header("Cash Calculator")
        
            # Insert amounts on the right-hand side
            for idx, amount in enumerate(amounts):
                amounts[idx] = st.number_input(f"Enter amount for {values[idx]}", value=amount)
                st.write(f"Total {values[idx] * amounts[idx]}")
                st.markdown("----------------------------------")
            if st.form_submit_button(label='Cash_count'):
                insert_vault_cash(conn,values,amounts)
                st.write("Total amount: ", str(sum(np.multiply(values, amounts))))
                conn.close()

    data = {
            'Kassastrook Code': ['Hoofdgerechten', 'Negerechten', 'Gebak', 'Kleine kaart', 'Dagschotels', 'Dranken-hoog', 'Frisdranken overig', 'Koffie', 'Cultuurkaarten', 'Dagschotelabonnementer', 'Omzet kadobonnen', 'Catering', 'Zaalhuur', 'EG Dranken Hoog', 'EG Dranken Laag', 'EG Koffie', 'EG Grote kaart', 'EG Kleine kaart', 'EG Dagschotels', 'EG Nagerechten', 'EG Gebak', 'REPR Dranken Hoog', 'REPR Dranken Laag', 'REPR Koffie', 'REPR Grote kaart', 'REPR Kleine kaart', 'REPR Dagschotels', 'REPR Nagerechten', 'REPR Gebak'],
            'Code': [8000, 8030, 8040, 8010, 8020, 8100, 8200, 8300, 4760, 2200, 2220, 8050, 8400, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            'Amount': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            }
    st.markdown("----------------------------------")
    with c2:
        
        with st.form(key='KassastrookForm'):
            st.header("Kassastrook")
            for index, kassastrook_code in enumerate(data['Kassastrook Code']):
                st.write(f"Kassastrook: {kassastrook_code} **{str(data['Code'][index])}**")
                # Collect the amount input for each kassastrook_code
                amount_input = st.text_input(f"Amount for {kassastrook_code}", value=str(data['Amount'][index]), key=f"amount_{index}")
                data['Amount'][index] = amount_input
                st.markdown("----------------------------------")


            # Print the updated data to verify user inputs
            
            if st.form_submit_button(label='Submit'):
                # After the for loop is completed, insert the data into the database
                for index, kassastrook_code in enumerate(data['Kassastrook Code']):
                    # Pass the appropriate arguments to the function
                    insert_kassastrook_data(conn, kassastrook_code, data['Code'][index], data['Amount'][index])

                # Display success message
                st.success("Kassastrook created!")
                conn.close()
    st.markdown("----------------------------------")
    with st.form(key='Migrations'):
            amount = st.number_input(label='Amount', min_value=0, step=1, key='migrations')
            description = st.text_area(label='Description', key='description_migrations')
            proof = st.file_uploader(label='Proof', key='proof_migrations', type=['png', 'jpg', 'pdf'])

            if st.form_submit_button(label='Submit'):
                # Insert data into the database
                insert_external_purchase(conn, amount, description, proof)

                # Display success message
                st.success("External Purchase recorded successfully!")
                # Close the SQLite connection when the app is closed or reloaded
                conn.close()


if __name__ == "__main__":
    main()