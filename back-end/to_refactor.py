import pandas as pd
from datetime import datetime

def convert_excel(input_file, output_file):
    # Διάβασμα του αρχείου εισόδου με τις 9 στήλες
    try:
        df = pd.read_excel(input_file)
    except Exception as e:
        print("Σφάλμα κατά το διάβασμα του αρχείου:", e)
        return

    # Έλεγχος για τον αριθμό στηλών
    if df.shape[1] != 9:
        print("Το αρχείο εισόδου δεν έχει 9 στήλες.")
        return
    
    # Εμφάνιση ονομάτων στηλών για έλεγχο
    print("Ονόματα στηλών:", df.columns)
    
    # Δημιουργία των νέων στηλών για τις οποίες ο χρήστης θα εισάγει δεδομένα
    df['Νέα Στήλη 10'] = ""
    df['Νέα Στήλη 11'] = ""
    df['Νέα Στήλη 12'] = ""

    # Προσθήκη της Στήλης 13 και των κενών στηλών 14 και 15
    df['Νέα Στήλη 13'] = ""
    df['Νέα Στήλη 14'] = ""
    df['Νέα Στήλη 15'] = None

    while True:
        date_input = input("Δώσε ημερομηνία (μορφή DD/MM/YYYY): ")
        try:
            date_object = datetime.strptime(date_input, "%d/%m/%Y")
            formatted_date = date_object.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Λάθος μορφή ημερομηνίας! Παρακαλώ χρησιμοποίησε τη μορφή DD/MM/YYYY.")
            
    value_column_15 = input("Bάλε τη μεθεπόμενη ημέρα της περιόδου: ")
    df['Νέα Στήλη 15'] = value_column_15
    
    # Επανάληψη για κάθε γραμμή του αρχείου
    for index, row in df.iterrows():
        try:
            # Αν γνωρίζουμε το όνομα της δεύτερης στήλης
            print(f"\nΓραμμή {index+1} - Τιμή στη 2η στήλη: {row['Στήλη_2']}")
            col2_value = row['Στήλη_2']
        except KeyError:
            # Αν δεν γνωρίζουμε το όνομα της δεύτερης στήλης, χρησιμοποιούμε την iloc
            col2_value = row.iloc[1]
            print(f"\nΓραμμή {index+1} - Τιμή στη 2η στήλη: {col2_value}")

        # Ζήτηση από τον χρήστη να εισάγει τιμές για τις Νέα Στήλη 10, Νέα Στήλη 11, και Νέα Στήλη 12
        value_column_10 = input("Δώσε την τιμή για τη Νέα Στήλη 10: ")
        value_column_11 = input("Δώσε την τιμή για τη Νέα Στήλη 11: ")
        value_column_12 = input("Δώσε την τιμή για τη Νέα Στήλη 12: ")

        # Ενημέρωση του DataFrame με τις τιμές του χρήστη
        df.at[index, 'Νέα Στήλη 10'] = value_column_10
        df.at[index, 'Νέα Στήλη 11'] = value_column_11
        df.at[index, 'Νέα Στήλη 12'] = value_column_12

        # Υπολογισμός της τιμής για τη στήλη 13
        col13_value = f"{str(col2_value)[:15]} {str(df.at[index, 'Νέα Στήλη 15'])} {value_column_11}"
        df.at[index, 'Νέα Στήλη 13'] = col13_value

        # Τοποθέτηση της κοινής ημερομηνίας σε όλες τις γραμμές στη στήλη Νέα Στήλη Ημερομηνία
        df.at[index, 'Νέα Στήλη 14'] = formatted_date

        # Έλεγχος των 5-6-7 χαρακτήρων της στήλης 5 για να ορίσουμε τον κωδικό στη στήλη 8
        col5_value = str(df.at[index, 'Unnamed: 4'])
        prefix = col5_value[4:7]  # Παίρνουμε τους πρώτους 5-6-7 χαρακτήρες
        
        # Αποδόσεις κωδικών ανάλογα με τους πρώτους 3 χαρακτήρες
        if prefix == "017":
            df.at[index, 'Στήλη_8'] = "38-03-001"
        elif prefix == "701":
            df.at[index, 'Στήλη_8'] = "38-03-002"
        elif prefix == "016":
            df.at[index, 'Στήλη_8'] = "38-03-002"
        elif prefix == "087":
            df.at[index, 'Στήλη_8'] = "38-03-002"
        elif prefix == "011":
            df.at[index, 'Στήλη_8'] = "38-03-004"
        elif prefix == "026":
            df.at[index, 'Στήλη_8'] = "38-03-005"
        elif prefix == "014":
            df.at[index, 'Στήλη_8'] = "38-03-026"
        else:
            df.at[index, 'Στήλη_8'] = "38-03-001"


    # Εξαγωγή στο νέο αρχείο με τις 15 στήλες
    try:
        df.to_excel(output_file, index=False)
        print("Το αρχείο εξόδου δημιουργήθηκε με επιτυχία:", output_file)
    except Exception as e:
        print("Σφάλμα κατά την αποθήκευση του αρχείου:", e)

# Παράδειγμα χρήσης:
input_file = 'eisodos.xlsx'    # Αντικατάστησε το με το όνομα του αρχείου εισόδου
output_file = 'eksodos.xlsx'    # Αντικατάστησε το με το όνομα του αρχείου εξόδου
convert_excel(input_file, output_file)
