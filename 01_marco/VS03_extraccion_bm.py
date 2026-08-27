import requests, pandas as pd
from datetime import date

DESDE_ANIO, HASTA_ANIO = date.today().year - 10, date.today().year

IND = {
    "IT.NET.USER.ZS":  "Personas que usan internet (% de la poblacion)",
    "IT.CEL.SETS.P2":  "Suscripciones a telefonia movil (por cada 100 personas)",
    "NY.GDP.PCAP.CD":  "PBI per capita (US$ a precios actuales)",
}
PAISES = "PER;CHL;COL;MEX;BRA"     # comparacion regional

frames = []
for cod, nombre in IND.items():
    url = (f"https://api.worldbank.org/v2/country/{PAISES}/indicator/{cod}"
           f"?format=json&date={DESDE_ANIO}:{HASTA_ANIO}&per_page=500")
    r = requests.get(url, timeout=30); r.raise_for_status()
    payload = r.json()
    if len(payload) < 2 or not payload[1]:
        print(f"SIN DATOS {cod}"); continue
    df = pd.DataFrame([{"pais": x["country"]["value"], "anio": int(x["date"]),
                        "valor": x["value"]} for x in payload[1]])
    df["indicador"] = nombre; df["codigo"] = cod; df["url_origen"] = url
    df["fecha_descarga"] = date.today().isoformat()
    frames.append(df)
    print(f"OK {cod}: {len(df)} observaciones")

bm = pd.concat(frames, ignore_index=True).dropna(subset=["valor"])
bm.to_csv("../evidencias/VS_series_banco_mundial.csv", index=False)

# Posicion del Peru frente a la region en el ultimo anio disponible
ult = bm.sort_values("anio").groupby(["indicador", "pais"]).last().reset_index()
print(ult.pivot(index="indicador", columns="pais", values="valor").round(1).to_string())
