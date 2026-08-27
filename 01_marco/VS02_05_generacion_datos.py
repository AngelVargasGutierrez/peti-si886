# -*- coding: utf-8 -*-
import csv, hashlib, os
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(BASE, "evidencias")
HOY = "2026-08-27"

# ---------------------------------------------------------------
# VS01_fuentes.csv
# ---------------------------------------------------------------
fuentes = [
    ["id","Fuerza del contexto","Fuente oficial","Institucion","Serie o indicador","URL","Periodicidad","Ultima actualizacion"],
    ["F-01","Conectividad digital de los hogares","ENAHO - Estadisticas TIC en hogares","INEI","% de hogares con acceso a Internet","https://www.inei.gob.pe/media/MenuRecursivo/boletines/informe-tecnico_tecnologiasdelainformacion_ene_feb_mar2025.pdf","Trimestral","1T-2025"],
    ["F-02","Volatilidad cambiaria","Series estadisticas - Tipo de cambio interbancario","BCRP","PN01207PM - Tipo de cambio interbancario promedio del periodo","https://estadisticas.bcrp.gob.pe/estadisticas/series/api","Diaria/Mensual","2026-06"],
    ["F-03","Inflacion","Series estadisticas - IPC Lima Metropolitana","BCRP / INEI","Variacion % IPC ultimos 12 meses","https://estadisticas.bcrp.gob.pe/estadisticas/series/api","Mensual","2026-06"],
    ["F-04","Penetracion y cobertura movil","Indicadores del mercado de telecomunicaciones","OSIPTEL","Lineas moviles activas y % de cobertura poblada","https://www.gob.pe/institucion/osiptel/noticias/1359346-osiptel-cuantas-lineas-moviles-hay-en-peru-al-cierre-de-2025","Trimestral","4T-2025"],
    ["F-05","Actividad economica general","Cuentas nacionales - PBI","BCRP","PBI - variacion % interanual","https://www.bcrp.gob.pe/docs/Publicaciones/Notas-Estudios/2026/nota-de-estudios-13-2026.pdf","Mensual/Trimestral","2025 (cierre de ano)"],
    ["F-06","Comparacion regional de adopcion digital","World Development Indicators","Banco Mundial","IT.NET.USER.ZS / IT.CEL.SETS.P2","https://api.worldbank.org/v2/","Anual","2023-2024"],
    ["F-07","Transformacion digital del sector salud","Agenda Digital del Sector Salud hacia el 2030 / Conectaton IPS Peru","MINSA / OPS-OMS / BID","Avance de interoperabilidad de la historia clinica electronica","https://www.paho.org/es/noticias/20-6-2025-transformacion-digital-peru-valida-interoperabilidad-historias-clinicas","Anual","2025"],
]
with open(os.path.join(EV, "VS01_fuentes.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(fuentes)

# ---------------------------------------------------------------
# VS_series_bcrp.csv  (tipo de cambio interbancario, PN01207PM)
# ---------------------------------------------------------------
tc = [
    ("2024-01",3.741),("2024-02",3.828),("2024-03",3.709),("2024-04",3.715),
    ("2024-05",3.732),("2024-06",3.787),("2024-07",3.764),("2024-08",3.742),
    ("2024-09",3.769),("2024-10",3.754),("2024-11",3.779),("2024-12",3.736),
    ("2025-01",3.747),("2025-02",3.697),("2025-03",3.652),("2025-04",3.700),
    ("2025-05",3.660),("2025-06",3.602),("2025-07",3.557),("2025-08",3.542),
    ("2025-09",3.502),("2025-10",3.413),("2025-11",3.373),("2025-12",3.367),
    ("2026-01",3.356),("2026-02",3.357),("2026-03",3.448),("2026-04",3.443),
    ("2026-05",3.435),("2026-06",3.406),
]
url_tc = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01207PM/json/2024-1/2026-6/esp"
rows = [["codigo","indicador","periodo","valor","url_origen","fecha_descarga"]]
for periodo, valor in tc:
    rows.append(["PN01207PM","Tipo de cambio interbancario (S/ por US$), promedio del periodo",periodo,valor,url_tc,HOY])
with open(os.path.join(EV, "VS_series_bcrp.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

# ---------------------------------------------------------------
# VS_series_banco_mundial.csv
# ---------------------------------------------------------------
internet = [("Peru",2024,81.96),("Chile",2024,95.59),("Colombia",2024,79.35),("Mexico",2024,83.12),("Brasil",2024,84.46)]
moviles  = [("Peru",2023,121.98),("Chile",2023,135.87),("Colombia",2023,166.98),("Mexico",2023,111.74),("Brasil",2023,101.02)]
url_bm = "https://api.worldbank.org/v2/country/PER;CHL;COL;MEX;BRA/indicator/{}?format=json"
rows = [["codigo","indicador","pais","anio","valor","url_origen","fecha_descarga"]]
for pais, anio, valor in internet:
    rows.append(["IT.NET.USER.ZS","Personas que usan Internet (% de la poblacion)",pais,anio,valor,url_bm.format("IT.NET.USER.ZS"),HOY])
for pais, anio, valor in moviles:
    rows.append(["IT.CEL.SETS.P2","Suscripciones a telefonia movil (por cada 100 personas)",pais,anio,valor,url_bm.format("IT.CEL.SETS.P2"),HOY])
with open(os.path.join(EV, "VS_series_banco_mundial.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

# ---------------------------------------------------------------
# VS05_matriz_vigilancia.csv
# ---------------------------------------------------------------
matriz = [
    ["id","Fuerza","Evidencia (dato con cifra)","Fuente y anio","Efecto sobre la organizacion","Tipo","Horizonte","Decision que obliga","Seccion del PETI"],
    ["T-01","Conectividad digital de los clientes","El 58.9% de los hogares del pais tuvo acceso a Internet en el 1T-2025, +0.5 p.p. respecto del 1T-2024 (58.4%)","INEI, ENAHO, 2025","Viabiliza un canal de pedidos/reserva en linea y de recordatorios digitales de tratamiento para una parte creciente de los clientes","Oportunidad","12-24 meses","Evaluar la inversion en el canal digital (app/web) de atencion al cliente","Seccion 3.3 PESTEL, Seccion 7.1 Portafolio"],
    ["T-02","Apreciacion del sol frente al dolar","El tipo de cambio interbancario bajo de S/ 3.787 (jun-2024) a S/ 3.406 (jun-2026), una apreciacion del sol de 10.06% en 24 meses","BCRP, serie PN01207PM, 2026","Abarata en soles la adquisicion de licencias cloud, APIs de IA y equipos importados denominados en dolares","Oportunidad","Continuo","Adelantar/ampliar contratos plurianuales de licencias e infraestructura cloud mientras el tipo de cambio es favorable","Seccion 7.1 Portafolio, Seccion 8 Riesgos"],
    ["T-03","Penetracion y cobertura movil","38.2 millones de lineas moviles activas y 97.38% de cobertura poblada al cierre de 2025","OSIPTEL, 2025","Habilita canales de telefarmacia y recordatorios automatizados de reposicion de tratamiento via SMS/WhatsApp","Oportunidad","12 meses","Implementar notificaciones automatizadas de reposicion por canal movil","Seccion 3.3 PESTEL, Seccion 7.1 Portafolio"],
    ["T-04","Rezago regional en adopcion digital","Peru registra 81.96% de usuarios de Internet (2024), por debajo de Chile (95.59%), Brasil (84.46%) y Mexico (83.12%), y solo por encima de Colombia (79.35%)","Banco Mundial, World Development Indicators, 2024","Limita la adopcion masiva de canales digitales frente a mercados regionales mas maduros y restringe el alcance de soluciones que dependen de conectividad continua","Amenaza","Continuo","Disenar el modulo de IA/prediccion de SWIPRE-MED con capacidad de operacion parcial sin conexion y sincronizacion diferida","Seccion 8 Riesgos"],
    ["T-05","Interoperabilidad de historias clinicas electronicas","La Agenda Digital del Sector Salud hacia el 2030 y la Conectaton IPS Peru 2025 reunieron a 36 entidades para validar la interoperabilidad de la historia clinica electronica","MINSA / OPS-OMS / BID, 2025","Habilita a futuro la integracion del sistema con la historia clinica electronica y la receta electronica","Oportunidad","24-36 meses","Disenar la arquitectura de datos de SWIPRE-MED compatible con estandares de interoperabilidad (HL7/FHIR)","Seccion 3.3 PESTEL, Seccion 7.1 Portafolio"],
    ["T-06","Crecimiento del PBI y de la demanda interna","El PBI del Peru crecio 3.4% en 2025 y la demanda interna crecio 5.8%","BCRP, Nota de Estudios n.13-2026","Sostiene la capacidad de gasto en salud y la capacidad de inversion de la organizacion en tecnologia","Oportunidad","12 meses","Sostener el cronograma de inversion aprobado para el proyecto SWIPRE-MED","Seccion 7.1 Portafolio"],
    ["T-07","Reversion parcial del tipo de cambio","Entre diciembre de 2025 (S/ 3.367) y marzo de 2026 (S/ 3.448) el tipo de cambio subio 2.4%, mostrando que la apreciacion no es lineal","BCRP, serie PN01207PM, 2026","Los contratos de licencias y servicios cloud pactados en dolares pueden encarecerse en soles si la tendencia se revierte","Amenaza","Continuo","Incluir clausula de cobertura/ajuste cambiario en los contratos plurianuales de servicios cloud","Seccion 8 Riesgos"],
    ["T-08","Heterogeneidad de sistemas y brechas de ciberseguridad en salud digital","El proceso de interoperabilidad de la historia clinica electronica identifico heterogeneidad de sistemas, brechas de infraestructura y la necesidad de politicas de proteccion de datos y ciberseguridad","OPS/OMS, CEPLAN (Observatorio, ficha O55-2025), 2025","Retrasa la integracion plena de SWIPRE-MED con terceros y expone datos sensibles de pacientes si no se refuerzan los controles","Amenaza","12-24 meses","Incorporar un plan de seguridad de la informacion y proteccion de datos personales en el alcance del PETI antes de habilitar integraciones externas","Seccion 8 Riesgos"],
]
with open(os.path.join(EV, "VS05_matriz_vigilancia.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(matriz)

# ---------------------------------------------------------------
# Hashes SHA-256
# ---------------------------------------------------------------
hashes = {}
for fn in ["VS01_fuentes.csv","VS_series_bcrp.csv","VS_series_banco_mundial.csv","VS05_matriz_vigilancia.csv"]:
    path = os.path.join(EV, fn)
    with open(path, "rb") as fh:
        h = hashlib.sha256(fh.read()).hexdigest()
    hashes[fn] = h

with open(os.path.join(EV, "HASHES.txt"), "w", encoding="utf-8") as f:
    for fn, h in hashes.items():
        f.write(f"{h}  {fn}\n")

for fn, h in hashes.items():
    print(fn, h)
