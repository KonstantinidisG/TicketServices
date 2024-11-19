import pandas as pd
import numpy as np
import os
import re
from datetime import datetime
import openpyxl

temp_file = "temp_data.xlsx"

def load_data(input_file):
    """Load data from input file or temporary file."""
    if os.path.exists(temp_file):
        df = pd.read_excel(temp_file)
        print("Φόρτωση δεδομένων από το προσωρινό αρχείο.")
    else:
        df = pd.read_excel(input_file)
        if df.shape[1] == 9:
            df['Νέα Στήλη 10'] = np.nan
            df['Νέα Στήλη 11'] = np.nan
            df['Νέα Στήλη 12'] = pd.Series(dtype='object')
            df['Νέα Στήλη 13'] = None
            df['Νέα Στήλη 14'] = None
            df['Νέα Στήλη 15'] = None
        df.to_excel(temp_file, index=False)
        print("Δημιουργία προσωρινού αρχείου για αποθήκευση προόδου.")
    return df

def save_temp_data(df):
    """Save progress in temporary file."""
    df.to_excel(temp_file, index=False)