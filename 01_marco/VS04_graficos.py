# -*- coding: utf-8 -*-
import os, csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(BASE, "evidencias")

AZUL_UPT = "#16285C"
GRIS = "#9CA3AF"

# --- tipo de cambio ---
periodos, valores = [], []
with open(os.path.join(EV, "VS_series_bcrp.csv"), encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        periodos.append(row["periodo"])
        valores.append(float(row["valor"]))

# --- internet users por pais ---
paises = {}
with open(os.path.join(EV, "VS_series_banco_mundial.csv"), encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        if row["codigo"] == "IT.NET.USER.ZS":
            paises[row["pais"]] = float(row["valor"])

fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))

ax[0].plot(range(len(periodos)), valores, color=AZUL_UPT, linewidth=2)
ax[0].set_title("Tipo de cambio interbancario (S/ por US$)\nFuente: BCRP, serie PN01207PM", fontsize=10)
step = max(1, len(periodos)//8)
ax[0].set_xticks(range(0, len(periodos), step))
ax[0].set_xticklabels([periodos[i] for i in range(0, len(periodos), step)], rotation=45, ha="right", fontsize=8)
ax[0].grid(alpha=.3)

orden = sorted(paises.items(), key=lambda x: -x[1])
nombres = [p for p, v in orden]
vals = [v for p, v in orden]
colores = [AZUL_UPT if n == "Peru" else GRIS for n in nombres]
ax[1].bar(nombres, vals, color=colores)
ax[1].set_title("Personas que usan Internet, % de la poblacion (2024)\nFuente: Banco Mundial, WDI", fontsize=10)
ax[1].set_ylabel("%")
for i, v in enumerate(vals):
    ax[1].text(i, v + 0.8, f"{v:.1f}", ha="center", fontsize=8)
ax[1].set_ylim(0, 105)

plt.tight_layout()
out = os.path.join(BASE, "VS_contexto.png")
plt.savefig(out, dpi=150)
print("Guardado:", out)
