import streamlit as st
import pandas as pd

def display_file_uploader():
    """UI element to upload files."""
    uploaded_file = st.file_uploader("Επιλέξτε το αρχείο Excel", type=["xlsx"])
    return uploaded_file

def display_data(df):
    """Display data in a table."""
    st.write("Προεπισκόπηση δεδομένων:")
    st.dataframe(df.head(10))

def display_output_message(message):
    """Display a success or error message."""
    st.success(message)

def display_error_message(message):
    """Display an error message."""
    st.error(message)
