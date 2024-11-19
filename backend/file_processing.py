import pandas as pd
import numpy as np
import os
import re
from datetime import datetime

def validate_date(input_date):
    """Validate date format DD/MM/YYYY."""
    try:
        datetime.strptime(input_date, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def create_final_file(df, output_file):
    """Create the final Excel file."""
    new_columns = ["Στήλη 1", "Στήλη 2", "Στήλη 3", "Στήλη 4", "Στήλη 5", "Στήλη 6", "Στήλη 7"]
    new_df = pd.DataFrame(columns=new_columns)

    for index, row in df.iterrows():
        row1 = [
            row.iloc[13], "ΗΠΕΛ", "105", row.iloc[12], row.iloc[2], row.iloc[8], ""
        ]
        row2 = [
            row.iloc[13], "ΗΠΕΛ", "105", row.iloc[12], row.iloc[7], "", row.iloc[8]
        ]
        row3 = ["", "", "", "", "", "", ""]
        new_df = pd.concat([new_df, pd.DataFrame([row1, row2, row3], columns=new_columns)], ignore_index=True)

    new_df.to_excel(output_file, index=False)
    print(f"Το αρχείο εξόδου δημιουργήθηκε: {output_file}")