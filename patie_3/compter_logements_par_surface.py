# =====================================================
# Auteur : Saleh BA-ZIGHIFAN
# Script : graphique_logements_simple.py
# Objectif : Créer un graphique clair avec valeurs au-dessus des barres
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------- Réglages ----------
DATA_PATH = "C:/Users/Saleh/Test_Saleh/data/BDD_TEST.csv"
RESULTS_DIR = "C:/Users/Saleh/Test_Saleh/patie_3/resultats"
PDF_PATH = os.path.join(RESULTS_DIR, "logements_par_surface.pdf")

# ---------- Lecture du fichier ----------
df = pd.read_csv(DATA_PATH)

# ---------- Nettoyage de la colonne ----------
def nettoyer_surface(s):
    s = (
        s.astype(str)
        .str.replace("\u00A0", " ", regex=False)
        .str.replace(",", ".", regex=False)
        .str.replace("m²", "", regex=False)
        .str.replace("m2", "", regex=False)
        .str.replace("'", "", regex=False)
        .str.replace(" ", "", regex=False)
    )
    return pd.to_numeric(s, errors="coerce")

colonne = "surface_reelle_bati"
df[colonne] = nettoyer_surface(df[colonne])

# ---------- Comptage ----------
plage = range(9, 15)
resultats = {m2: len(df[df[colonne] == m2]) for m2 in plage}

# ---------- Création du graphique ----------
os.makedirs(RESULTS_DIR, exist_ok=True)
fig, ax = plt.subplots(figsize=(8, 6))

# Couleurs bleu clair → foncé
couleurs = plt.cm.Blues([0.4 + i * 0.08 for i in range(len(resultats))])

bars = ax.bar(resultats.keys(), resultats.values(), color=couleurs, edgecolor="black", linewidth=1.2)
ax.set_title("Nombre de logements par surface (9 à 14 m²)", fontsize=15, fontweight="bold", color="#0d47a1")
ax.set_xlabel("Surface (m²)", fontsize=12)
ax.set_ylabel("Nombre de logements", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.5)

# Ajouter les valeurs au-dessus de chaque barre
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 30, f"{int(yval)}", ha="center", va="bottom",
            fontsize=10, fontweight="bold", color="#0d47a1")

# Signature en bas
plt.figtext(0.5, 0.02,
            "Rapport généré automatiquement par Saleh BA-ZIGHIFAN – Analyse des logements (9–14 m²)",
            ha="center", fontsize=9, color="#555")

# Sauvegarde en PDF
plt.tight_layout()
plt.savefig(PDF_PATH, dpi=300, bbox_inches="tight")
plt.close()

print("✅ PDF créé avec succès !")
print(f"📄 Enregistré dans : {PDF_PATH}")
