import os
import pandas as pd
from sqlalchemy import create_engine

# Percorsi delle cartelle e dei file
RAW_DATA_PATH = r"C:\Users\user\Desktop\Progetti Tech\Customer-Churn-Prediction-System\data\raw\Telco_customer_churn.csv"  # Modifica se necessario con il percorso del tuo CSV
PROCESSED_DIR = "data/processed"
DB_PATH = "data/telco.db"

os.makedirs(PROCESSED_DIR,exist_ok=True)
os.makedirs("data", exist_ok=True)

def run_etl():
    print("🚀 #START: Inizio Pipeline ETL (Extract, Transform, Load)")
    
    # 1. EXTRACT (Estrazione del dataset grezzo)
    if not os.path.exists(RAW_DATA_PATH):
        print(f"❌ Errore: File non trovato al percorso {RAW_DATA_PATH}. Controlla il percorso del CSV.")
        return
    
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"📥 Dati estratti con successo: {df.shape[0]} righe, {df.shape[1]} colonne.")

    # 2. TRANSFORM (Pulizia e Data Engineering di base)
    print("🛠️ #TRANSFORM: Pulizia e trasformazione dei dati...")
    
    # Pulizia nomi colonne (rimozione spazi)
    df.columns = df.columns.str.strip()
    
    # Conversione Total Charges in numerico (gestendo eventuali spazi vuoti come NaN)
    if 'Total Charges' in df.columns:
        df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
        # Riempimento dei valori mancanti per i clienti "neonati" (Tenure = 0)
        df['Total Charges'] = df['Total Charges'].fillna(0.0)

    # Rimozione duplicati se presenti
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"🧹 Rimossi {initial_rows - len(df)} record duplicati.")

    # Salvataggio dei dati processati in formato CSV intermedio (Train/Test raw split)
    train_df = df.sample(frac=0.8, random_state=42)
    test_df = df.drop(train_df.index)
    
    train_df.to_csv(os.path.join(PROCESSED_DIR, "train_raw.csv"), index=False)
    test_df.to_csv(os.path.join(PROCESSED_DIR, "test_raw.csv"), index=False)
    print(f"💾 Dataset intermedi salvati in {PROCESSED_DIR}/")

    # 3. LOAD (Caricamento nel Database Relazionale SQL)
    print(f"🗄️ #LOAD: Scrittura dei dati nel database SQLite ({DB_PATH})...")
    engine = create_engine(f"sqlite:///{DB_PATH}")
    
    # Salvataggio della tabella principale dei clienti
    df.to_sql("customers", engine, if_exists="replace", index=False)
    print("✅ Tabella 'customers' creata e popolata con successo nel database SQL!")
    print("🎉 Pipeline ETL completata senza errori!")

if __name__ == "__main__":
    run_etl()