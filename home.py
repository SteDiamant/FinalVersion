import streamlit as st
import pandas as pd
import numpy as np
from Daily_Count import main as daily_count
from logInPage import main as authenticate
from Daily_Count import show_external_puchases,show_kassastrook,show_card_payments,show_gift_cards,show_vault_cash,show_invoice

st.set_page_config(
    page_title="Sam-Sam App",
    page_icon="imgs\logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
def sidebar_menu():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page", ["Home", "Daily Count"])
    if page == "home":
        st.write("Welcome to the home page"	)
    elif page == "Daily Count":
        if st.session_state["authentication_status"]:
            daily_count()
        else:
            pass
    

def main():
    status=authenticate()
    radio_style = """
                        <style>
                        /* Cutted edges effect */
                        .radio-button input[type="radio"] + label {
                        border-radius: 5px;
                        border: 2px solid #4CAF50;
                        padding: 10px;
                        margin-right: 10px;
                        }

                        /* Highlight selected radio button */
                        .radio-button input[type="radio"]:checked + label {
                        background-color: #4CAF50;
                        color: white;
                        }

                        /* Align text to the center of the label */
                        .radio-button label {
                        display: inline-block;
                        text-align: center;
                        }

                        /* Remove outline on focus */
                        .radio-button input[type="radio"]:focus + label {
                        outline: none;
                        }
                        </style>
                        """


    if status:
        sidebar_menu()
        #st.markdown(radio_style, unsafe_allow_html=True)
        choice = st.radio("Choose Database to Interact With",['card_payments','gift_cards','invoices','vault_cash','kassastrook_data','external_purchase'],horizontal=True)
        if choice == 'card_payments':
            show_card_payments()
        elif choice == 'gift_cards':
            show_gift_cards()
        elif choice == 'invoices':
            show_invoice()
        elif choice == 'vault_cash':
            show_vault_cash()
        elif choice == 'kassastrook_data':
            show_kassastrook()
        elif choice == 'external_purchase':
            show_external_puchases()

if __name__ == "__main__":
    main()