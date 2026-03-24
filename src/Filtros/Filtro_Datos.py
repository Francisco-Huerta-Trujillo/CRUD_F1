import pandas as pd
import numpy as np
import datetime as dt
import os

INPUT_FILE = r'C:/ProyectosPersonales/CRUD_F1/CRUD_F1/Datasets/drivers.csv'
OUTPUT_DIR = r'C:/ProyectosPersonales/CRUD_F1/CRUD_F1/UpdatedDatasets'
OUTPUT_FILE = 'drivers_limpios.csv'
ruta_salida = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

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
    'driverId' : 'ID',
    'number' : 'Number',
    'forename' : 'Forename',
    'surname' : 'Surname',
    'nationality' : 'Nationality'
}

''' Verifico que existan las columnas antes de renombrarlas
set() sirve para comparar conjuntos de nombres '''
columnas_en_csv = set(df.columns)
columnas_que_quiero = set(columnas_necesarias.keys())

if not columnas_que_quiero.issubset(columnas_en_csv):
    print("Las columnas en el csv no coinciden con las que busco")
    print(f"El csv tiene {list(df.columns)}")
    exit()

# Filtro lo que quiero y renombro
df = df[columnas_necesarias.keys()]
df = df.rename(columns=columnas_necesarias)

# 3 GENERACION DE TABLAS NORMALIZADAS
print("Preparando archivo csv...")
df = df.drop_duplicates(subset=['ID'])

# 4 EXPORTACION
print("Guardando archivo limpio...")
df.to_csv(ruta_salida, index=False, encoding='utf-8')

print("\n Proceso terminado")
print(f"Filas originales: {total_filas}")
print(f"Filas limpias: {len(df)}")
print(f"Archivo generado: {OUTPUT_FILE}")