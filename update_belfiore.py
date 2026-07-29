import pandas as pd

ISTAT_URL = "https://www.istat.it/storage/codici-unita-amministrative-territoriali/Elenco-comuni-italiani.csv"

def update_data():
    print("Scaricamento dati ISTAT in corso...")
    df = pd.read_csv(ISTAT_URL, sep=';', encoding='latin-1', dtype=str)

    column_mapping = {
        'Codice catasto': 'codice_belfiore',
        'Denominazione in italiano': 'nome',
        'Sigla automobilistica': 'provincia',
        'Denominazione Regione': 'regione',
        'Codice Comune formato alfanumerico': 'codice_istat'
    }

    df_clean = df[list(column_mapping.keys())].rename(columns=column_mapping)

    for col in df_clean.columns:
        df_clean[col] = df_clean[col].str.strip()

    df_clean = df_clean.sort_values(by='nome').reset_index(drop=True)

    df_clean.to_json("comuni_belfiore.json", orient="records", indent=2, force_ascii=False)
    df_clean.to_csv("comuni_belfiore.csv", index=False, encoding='utf-8')

    print(f"Completato! Elaborati {len(df_clean)} comuni.")

if __name__ == "__main__":
    update_data()