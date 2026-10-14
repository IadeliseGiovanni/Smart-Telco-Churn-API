import os
import joblib
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score
from xgboost import XGBClassifier

# Percorsi
DB_PATH = "sqlite:///data/telco.db"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

def train_churn_model():
    print("🚀 #START: Caricamento dati dal database SQL per il Training...")
    
    # 1. Estrazione dati dal database SQLite creato con l'ETL
    engine = create_engine(DB_PATH)
    df = pd.read_sql("SELECT * FROM customers", engine)
    print(f"📊 Dataset caricato dal DB: {df.shape[0]} righe, {df.shape[1]} columns.")

    # 2. Preparazione Feature e Target (Churn Value)
    if 'Churn Value' not in df.columns:
        print("❌ Errore: Colonna target 'Churn Value' non trovata nel database.")
        return

    # Scegliamo alcune feature chiave per semplicità e robustezza
    # (Gestiamo le categoriche convertendole in indicatori numerici)
    feature_cols = ['Tenure Months', 'Monthly Charges', 'Total Charges']
    
    # Pulizia e conversione forzata in numerico
    for col in feature_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    X = df[feature_cols]
    y = df['Churn Value'].astype(int)

    # 3. Train/Test Split Stratificato
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"🔀 Dati suddivisi: {X_train.shape[0]} training set, {X_test.shape[0]} test set.")

    # 4. Training del modello XGBoost
    print("🤖 #TRAINING: Addestramento del modello XGBoost in corso...")
    model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        random_state=42,
        eval_metric='logloss'
    )
    model.fit(X_train, y_train)

    # 5. Valutazione Rapida
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]
    
    f1 = f1_score(y_test, preds)
    roc_auc = roc_auc_score(y_test, probs)
    
    print(f"📈 Metriche sul Test Set -> F1-Score: {f1:.4f} | ROC-AUC: {roc_auc:.4f}")

    # 6. Salvataggio del Modello (Artifact)
    model_path = os.path.join(MODEL_DIR, "churn_pipeline_v1.joblib")
    joblib.dump(model, model_path)
    print(f"💾 Modello salvato con successo in: {model_path}")
    print("🎉 Processo di Training completato!")

if __name__ == "__main__":
    train_churn_model()