import io
import sys
import pandas as pd
import requests

# Permalink esatto ISTAT
ISTAT_URL = "https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.xlsx"

def update_data():
    print("Scaricamento file XLSX da ISTAT...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(ISTAT_URL, headers=headers, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"ERRORE CRITICO nel download: {e}")
        sys.exit(1)

    print("Download completato. Elaborazione dati con Pandas...")
    
    # Legge il file Excel mantenendo i valori come stringhe
    df = pd.read_excel(io.BytesIO(response.content), dtype=str)

    # Mappatura esatta basata sulle colonne del file ISTAT
    column_mapping = {
        'Codice Catastale del Comune': 'codice_belfiore',
        'Denominazione in italiano': 'nome',
        'Sigla automobilistica': 'provincia',
        'Denominazione Regione': 'regione',
        'Codice Comune formato alfanumerico': 'codice_istat'
    }

    # Verifica presenza delle colonne necessarie
    missing_cols = [col for col in column_mapping.keys() if col not in df.columns]
    if missing_cols:
        print(f"ERRORE: Colonne mancanti nel file ISTAT: {missing_cols}")
        print("Colonne trovate:", df.columns.tolist())
        sys.exit(1)

    # Selezione e rinomina
    df_clean = df[list(column_mapping.keys())].rename(columns=column_mapping)

    # Pulizia spazi bianchi
    for col in df_clean.columns:
        df_clean[col] = df_clean[col].astype(str).str.strip()

    # Ordina alfabeticamente per nome Comune
    df_clean = df_clean.sort_values(by='nome').reset_index(drop=True)

    # Salvataggio JSON e CSV
    df_clean.to_json("comuni_belfiore.json", orient="records", indent=2, force_ascii=False)
    df_clean.to_csv("comuni_belfiore.csv", index=False, encoding='utf-8')

    print(f"Completato! Generati file con {len(df_clean)} comuni.")

if __name__ == "__main__":
    update_data()