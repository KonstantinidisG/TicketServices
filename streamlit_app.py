import streamlit as st
from backend.data_validation import load_data, save_temp_data
from backend.file_processing import validate_date, create_final_file
from frontend.components.ui_elements import display_file_uploader, display_data, display_output_message, display_error_message
import os

temp_file = "temp_data.xlsx"

def main():
    st.title("Επεξεργασία Αρχείων Excel")

    uploaded_file = display_file_uploader()
    if uploaded_file:
        try:
            df = load_data(uploaded_file)
            display_data(df)
            
            if st.button("Αποθήκευση Προσωρινών Δεδομένων"):
                save_temp_data(df)
                display_output_message("Τα δεδομένα αποθηκεύτηκαν προσωρινά.")
            
            output_file = st.text_input("Δώστε όνομα αρχείου εξόδου (π.χ. output.xlsx):")
            if st.button("Δημιουργία Τελικού Αρχείου"):
                if output_file:
                    create_final_file(df, output_file)
                    display_output_message("Το αρχείο εξόδου δημιουργήθηκε.")
                else:
                    display_error_message("Παρακαλώ εισάγετε όνομα αρχείου εξόδου.")
        except Exception as e:
            display_error_message(f"Σφάλμα: {str(e)}")

if __name__ == "__main__":
    main()