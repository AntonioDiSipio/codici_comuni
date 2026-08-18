# 🇮🇹 Codici Belfiore e ISTAT dei Comuni Italiani (Auto-Update)

Repository per la mappatura e la consultazione sempre aggiornata dei dati amministrativi, ISTAT e dei **Codici Belfiore (Catastali)** dei Comuni d'Italia.

I dati vengono estratti automaticamente dalla fonte ufficiale **ISTAT** (permalink in formato Excel) tramite uno script Python e mantenuti sincronizzati settimanalmente attraverso un workflow di **GitHub Actions**.

---

## 📅 Automazione e Fonte Dati

* **Frequenza di aggiornamento:** Ogni lunedì alle 04:00 UTC (tramite GitHub Actions `cron`).
* **Esecuzione manuale:** Abilitata tramite il pulsante `workflow_dispatch` nella scheda Actions.
* **Pagina Ufficiale ISTAT:** [ISTAT - Codici delle unità amministrative](https://www.istat.it/it/archivio/6777)
* **Permalink Diretto File XLSX:** `https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.xlsx`

---

## 📁 File Generati nel Repository

All'interno del repository sono disponibili due formati per la massima interoperabilità:

1. **`comuni_belfiore.json`**: Formato JSON strutturato, ideale per web app, API, script JavaScript o Python.
2. **`comuni_belfiore.csv`**: Formato CSV (codifica UTF-8), pronto per l'importazione in database (PostgreSQL/PostGIS, SQLite, MySQL) o software GIS (QGIS, ArcGIS).

---

## 🛠️ Struttura Dati

Ogni record contiene i seguenti campi:

```json
{
  "codice_belfiore": "A001",
  "nome": "Abano Terme",
  "provincia": "PD",
  "regione": "Veneto",
  "codice_istat": "028001"
}

_Ultimo controllo automatico: 2026-08-18 16:19:22 UTC_
