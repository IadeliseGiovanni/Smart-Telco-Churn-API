# 🚀 Smart Telco RAG & ETL System

> Piattaforma integrata End-to-End di Data Engineering e Machine Learning per la predizione e la prevenzione del Customer Churn nel settore delle Telecomunicazioni.

---

## 📋 Panoramica del Progetto
Il progetto affronta una delle criticità economiche principali delle aziende Telco: la perdita di clienti (Churn). L'applicazione unisce le competenze di **Data Engineering** (gestione ed elaborazione dei flussi ETL su database relazionali) e di **Machine Learning** (addestramento di modelli predittivi avanzati con XGBoost), esponendo il tutto tramite un'architettura **API-First** ad alte performance.

### 🔄 Flusso Operativo:
1. **ETL Pipeline:** Estrazione, pulizia e strutturazione dei dati grezzi all'interno di un database relazionale SQLite (`data/telco.db`).
2. **Machine Learning:** Addestramento di un modello di classificazione **XGBoost** per stimare in tempo reale la probabilità di abbandono del cliente.
3. **Backend & API:** Esposizione del modello tramite un server asincrono sviluppato con **FastAPI** e documentazione interattiva (Swagger UI).

---

## 🛠️ Stack Tecnologico
* **Linguaggio Core:** Python 3.10+
* **Data Engineering & ETL:** Pandas, NumPy, SQLAlchemy, SQLite
* **Machine Learning:** Scikit-learn, XGBoost, Joblib
* **Backend & API:** FastAPI, Pydantic, Uvicorn
* **Version Control:** Git, GitHub

---

## 📂 Struttura del Repository
```plaintext
Smart-Telco-Rag/
│
├── 📂 backend/
│   └── api.py                  # Endpoint FastAPI per l'inferenza in tempo reale
├── 📂 data/
│   ├── processed/              # Dataset intermedi (Train/Test raw)
│   └── telco.db                # Database relazionale SQLite
├── 📂 models/
│   └── churn_pipeline_v1.joblib # Modello XGBoost pre-addestrato e serializzato
├── 📂 venv/                    # Ambiente virtuale Python (ignorato da Git)
├── etl_pipeline.py             # Script di estrazione, pulizia e popolamento database
├── train_model.py              # Script di training e salvataggio del modello XGBoost
└── README.md                   # Documentazione ufficiale del progetto
