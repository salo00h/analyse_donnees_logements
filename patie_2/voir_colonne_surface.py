# =====================================================
# Auteur : Saleh BA-ZIGHIFAN
# Script : voir_colonne_surface.py
# Objectif : Visualiser et analyser la colonne 'surface_reelle_bati'
# =====================================================

import pandas as pd
import os
from datetime import datetime

# ---------- Réglages ----------
DATA_PATH = "C:/Users/Saleh/Test_Saleh/data/BDD_TEST.csv"
RESULTS_DIR = "C:/Users/Saleh/Test_Saleh/patie_2/resultats"
EXCEL_PATH = os.path.join(RESULTS_DIR, "colonne_surface_brut.xlsx")
HTML_PATH = os.path.join(RESULTS_DIR, "colonne_surface_brut.html")

# ---------- Lecture du fichier CSV ----------
df = pd.read_csv(DATA_PATH)

# ---------- Vérification ----------
if "surface_reelle_bati" not in df.columns:
    raise KeyError("❌ Colonne 'surface_reelle_bati' introuvable dans le fichier CSV.")

# ---------- Extraire la colonne ----------
colonne_surface = df[["surface_reelle_bati"]].copy()

# ---------- Calculs des infos ----------
total_valeurs = len(colonne_surface)
valeurs_vides = colonne_surface["surface_reelle_bati"].isna().sum()
valeurs_valides = colonne_surface["surface_reelle_bati"].notna().sum()
pourcentage_vides = round((valeurs_vides / total_valeurs) * 100, 2)

# ---------- Sauvegarde Excel ----------
os.makedirs(RESULTS_DIR, exist_ok=True)
colonne_surface.to_excel(EXCEL_PATH, index=False)

print("✅ Colonne extraite avec succès !")
print(f"📂 Fichier Excel enregistré dans : {EXCEL_PATH}")

# ---------- Génération HTML ----------
date_gen = datetime.now().strftime("%d/%m/%Y à %H:%M")
table_html = colonne_surface.head(100).to_html(
    border=0,
    justify="center",
    classes="table table-hover",
    index=False
)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(f"""
    <html>
    <head>
        <meta charset='utf-8'>
        <title>Analyse de la colonne surface_reelle_bati</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, sans-serif;
                margin: 40px;
                background-color: #f4f6f8;
                color: #333;
            }}
            .card {{
                background: white; padding: 24px; border-radius: 12px;
                box-shadow: 0 4px 16px rgba(0,0,0,0.08); margin: auto; width: 80%;
            }}
            h1 {{ text-align: center; color: #0d6efd; margin-bottom: 10px; }}
            .kpi {{
                display: flex; gap: 18px; justify-content: center; flex-wrap: wrap;
                margin: 20px 0;
            }}
            .item {{
                background: #e9f2ff; border-radius: 10px; padding: 10px 14px;
                min-width: 200px; text-align: center; border: 1px solid #cfe2ff;
            }}
            th, td {{ border: 1px solid #ddd; padding: 8px 10px; text-align: center; }}
            th {{
                background-color: #0d6efd;
                color: white;
                font-weight: 600;
            }}
            tr:nth-child(even) {{ background-color: #f9fbff; }}
            footer {{
                text-align: center;
                margin-top: 20px;
                color: #555;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>📊 Analyse de la colonne « surface_reelle_bati »</h1>
            <p style="text-align:center; color:#555;">Généré le {date_gen}</p>

            <div class="kpi">
                <div class="item"><b>Total des lignes</b><br><span style="font-size:22px">{total_valeurs}</span></div>
                <div class="item"><b>Valeurs valides</b><br><span style="font-size:22px">{valeurs_valides}</span></div>
                <div class="item"><b>Valeurs manquantes (NaN)</b><br><span style="font-size:22px">{valeurs_vides}</span></div>
                <div class="item"><b>Taux de valeurs manquantes</b><br><span style="font-size:22px">{pourcentage_vides}%</span></div>
            </div>

            <h2 style="color:#0d6efd;">Aperçu des 100 premières lignes</h2>
            {table_html}
            <p style="text-align:center; color:#777;">Aperçu limité à 100 lignes pour lisibilité.</p>
        </div>
        <footer>
            ✅ Rapport généré automatiquement par <b>Saleh BA-ZIGHIFAN</b>
        </footer>
    </body>
    </html>
    """)

print(f"✅ Rapport HTML créé dans : {HTML_PATH}")
