# =====================================================
# Auteur : Saleh BA-ZIGHIFAN
# Script : analyse_generale.py
# Objectif : Faire une analyse générale du fichier CSV
# =====================================================

import pandas as pd
from datetime import datetime

# 1️⃣ Lecture du fichier CSV
df = pd.read_csv("C:/Users/Saleh/Test_Saleh/data/BDD_TEST.csv")

# 2️⃣ Informations générales
print("=== ANALYSE GÉNÉRALE DU FICHIER ===")
print("Nombre total de lignes :", len(df))
print("Nombre de colonnes :", len(df.columns))
print("\nNoms des colonnes :", list(df.columns))

# 3️⃣ Aperçu des premières lignes
print("\nAperçu des 5 premières lignes :")
print(df.head())

# 4️⃣ Types de données et valeurs manquantes
print("\n=== INFORMATIONS TECHNIQUES ===")
print(df.info())
print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())

# 5️⃣ Statistiques descriptives
print("\n=== STATISTIQUES DESCRIPTIVES ===")
print(df.describe())

print("\n✅ Analyse générale terminée avec succès.")

# ==========================================
# 🔹 SAUVEGARDE DU RAPPORT HTML DANS /results
# ==========================================

# Création du tableau HTML bien formaté
stats_html = df.describe().to_html(
    border=0,
    justify="center",
    classes="table table-hover"
)

# Date actuelle
date_gen = datetime.now().strftime("%d/%m/%Y à %H:%M")

# Chemin de sauvegarde
output_path = "C:/Users/Saleh/Test_Saleh/patie_1/resultats/statistiques.html"

# Création du fichier HTML complet avec style élégant
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"""
    <html>
    <head>
        <meta charset='utf-8'>
        <title>Rapport d'analyse - Saleh BA-ZIGHIFAN</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, sans-serif;
                margin: 40px;
                background-color: #f4f6f8;
                color: #333;
            }}
            h1 {{
                text-align: center;
                color: #0056b3;
                margin-bottom: 10px;
            }}
            h2 {{
                color: #007bff;
                border-bottom: 2px solid #007bff;
                padding-bottom: 5px;
                width: 80%;
                margin: 30px auto 10px;
            }}
            .info {{
                text-align: center;
                background-color: #e9ecef;
                border-radius: 10px;
                padding: 15px;
                width: 70%;
                margin: 0 auto 30px;
                box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
            }}
            table {{
                border-collapse: collapse;
                margin: auto;
                width: 85%;
                font-size: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                background-color: white;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 10px 12px;
                text-align: center;
            }}
            th {{
                background-color: #007bff;
                color: white;
                font-weight: 600;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            footer {{
                text-align: center;
                margin-top: 40px;
                font-size: 14px;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <h1>📊 Rapport d'analyse générale du fichier CSV</h1>
        <div class='info'>
            <p><strong>Date de génération :</strong> {date_gen}</p>
            <p><strong>Nombre total de lignes :</strong> {len(df)}</p>
            <p><strong>Nombre de colonnes :</strong> {len(df.columns)}</p>
            <p><strong>Colonnes :</strong> {', '.join(df.columns)}</p>
        </div>
        <h2>Statistiques descriptives</h2>
        {stats_html}
        <footer>
            ✅ Rapport généré automatiquement par <strong>Saleh BA-ZIGHIFAN</strong><br>
            © 2025 - Analyse de données professionnelle
        </footer>
    </body>
    </html>
    """)

print(f"\n✅ Rapport HTML professionnel créé avec succès dans : {output_path}")
