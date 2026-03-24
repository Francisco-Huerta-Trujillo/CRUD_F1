import pandas as pd
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / '../../Datasets/races.csv'
OUTPUT_FILE = BASE_DIR / '../../UpdatedDatasets'
OUTPUT_FILE.mkdir(parents=True, exist_ok=True)
OUT_RACES = 'UpdatedRaces.csv'

# 1 CARGA DE DATOS
try:
    #"encoding='utf-8'" quiere decir que es la libreria universal de caracteres
    #"on_bad_lines='skip' quiere decir que salta lineas rotas si el archivo viene mal" 
    df = pd.read_csv(INPUT_FILE, encoding='utf-8', on_bad_lines='skip', index_col=False)
    total_filas = len(df)
except FileNotFoundError:
    print(f"No se encontro el archivo {INPUT_FILE}")
    exit()

# 2 SELECCION DE COLUMNAS
columnas_necesarias = {
    'raceId' : 'raceId',
    'round' : 'round',
    'circuitId' : 'circuitId',
    'name' : 'name',
    'date' : 'date'
}

columnas_en_csv = set(df.columns)
columnas_que_quiero = set(columnas_necesarias.keys())

if not columnas_que_quiero.issubset(columnas_en_csv):
    print("Las columnas en el csv no coinciden con las que busco")
    print(f"El csv tiene {list(df.columns)}")
    exit()


# Filtro lo que quiero y renombro
df = df[columnas_necesarias.keys()]
df = df.rename(columns=columnas_necesarias)

# 3 LIMPIEZA DE DATOS
print("Limpiando datos...")

# Convertir fechas
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Eliminar filas con datos críticos nulos
df = df.dropna(subset=['raceId', 'date', 'circuitId'])

# Eliminar duplicados
df = df.drop_duplicates(subset=['raceId'])

# 4 NORMALIZACION BASICA

# A) Tabla RACES
races_table = df.copy()

# B) Tabla CIRCUITS (solo IDs únicos por ahora)
circuits_table = df[['circuitId']].drop_duplicates().copy()

# 5 EXPORTACION
print("Guardando archivos limpios...")

# Crear carpeta si no existe
os.makedirs(OUTPUT_FILE, exist_ok=True)

# Exportar
races_table.to_csv(os.path.join(OUTPUT_FILE, OUT_RACES), index=False, encoding='utf-8')

print("\nProceso terminado")
print(f"Filas originales: {total_filas}")
print(f"Filas limpias: {len(df)}")
print(f"Archivo generado: {OUT_RACES}")
print(f"Races: {len(races_table)}")
print(f"Circuits únicos: {len(circuits_table)}")