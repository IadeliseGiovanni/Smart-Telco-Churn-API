# 🚀 Smart Telco RAG & ETL System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![ETL](https://img.shields.io/badge/Data-Engineering_ETL-orange?logo=sqlite&logoColor=white)
![XGBoost](https://img.shields.io/badge/Model-XGBoost_Pipeline-darkorange?logo=xgboost&logoColor=white)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)
![Frontend](https://img.shields.io/badge/UI-Swagger_UI-blueviolet?logo=fastapi&logoColor=white)

---

## 📋 Panoramica del Progetto
Piattaforma integrata End-to-End di **Data Engineering** e **Machine Learning** per la predizione e la prevenzione del Customer Churn nel settore delle Telecomunicazioni. 

Il progetto unisce la gestione automatizzata dei flussi di dati (ETL su database relazionali) all'addestramento di modelli predittivi avanzati, esponendo il tutto tramite un'architettura **API-First**.

### 🖥️ Interfaccia API & Documentazione (Swagger UI)
<img width="1643" height="817" alt="Screenshot 2026-10-14 181815" src="https://github.com/user-attachments/assets/92e4974c-6251-4eb8-8ddb-e9450567103e" />


---

## 🔄 Flusso Operativo
1. **ETL Pipeline (`etl_pipeline.py`):** Estrazione dei dati grezzi, pulizia (gestione duplicati e valori nulli) e caricamento automatizzato in un database relazionale SQLite (`data/telco.db`).
2. **Machine Learning (`train_model.py`):** Estrazione dei dati dal DB, split stratificato e training di un modello di classificazione **XGBoost** serializzato in `models/churn_pipeline_v1.joblib`.
3. **Backend & API (`backend/api.py`):** Server asincrono sviluppato con **FastAPI** per l'inferenza in tempo reale e documentazione interattiva (Swagger UI).

---

## 🛠️ Stack Tecnologico
* **Core:** Python 3.10+, Pandas, NumPy
* **Data Engineering:** SQLAlchemy, SQLite, Pipeline ETL
* **Machine Learning:** Scikit-learn, XGBoost, Joblib
* **Backend:** FastAPI, Pydantic, Uvicorn
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
