import pandas as pd
import numpy as np
import random

# Fijamos una semilla para que, cada vez que corras el código, salgan los mismos números
np.random.seed(42)
num_registros = 500

# Creamos la estructura base (como una tabla de Excel vacía)
df = pd.DataFrame()

# Creamos una lista de números del 1 al 500 para identificar a cada estudiante
df['id_estudiante'] = range(1, num_registros + 1)

# Generamos edades aleatorias entre 17 y 25 años
edades = np.random.randint(17, 26, size=num_registros).tolist()
# Aquí metemos "ruido": elegimos 10 posiciones al azar y ponemos edades ilógicas (5, 85, 99)
for i in range(10): 
    edades[random.randint(0, 499)] = random.choice([5, 85, 99])

df['edad'] = edades

# Creamos notas promedio entre 1.0 y 5.0, redondeadas a dos decimales
df['promedio'] = np.round(np.random.uniform(1.0, 5.0, num_registros), 2)

# Simulamos olvidos en la base de datos: borramos el promedio de 15 estudiantes (valores nulos)
for _ in range(15):
    df.loc[random.randint(0, 499), 'promedio'] = np.nan

# Generamos porcentajes de asistencia entre 40 y 100
df['asistencia_pct'] = np.random.randint(40, 101, size=num_registros)

# Creamos ingresos familiares promedio de 1.5 millones
ingresos = np.random.normal(1500000, 500000, num_registros).astype(int)
# Metemos otros valores atípicos: 5 estudiantes con ingresos exagerados de 50 millones
for i in range(5): 
    ingresos[random.randint(0, 499)] = 50000000 
    
df['ingreso_mensual'] = ingresos

# Asignamos becas de forma aleatoria: el 30% tiene y el 70% no
df['tiene_beca'] = np.random.choice(['Si', 'No'], size=num_registros, p=[0.3, 0.7])

# Definimos una lógica para decidir quién abandona la escuela
def calcular_abandono(row):
    score = 0
    # Si no tiene nota o es muy baja, suma puntos de riesgo
    if pd.isna(row['promedio']) or row['promedio'] < 3.0:
        score += 2
    # Si falta mucho a clases, suma más riesgo
    if row['asistencia_pct'] < 70:
        score += 2
    # Si no tiene apoyo económico (beca), suma un punto de riesgo
    if row['tiene_beca'] == 'No':
        score += 1
        
    # Si acumuló mucho riesgo, tiene 80% de probabilidad de irse; si no, solo 10%
    if score >= 3:
        return np.random.choice(['Si', 'No'], p=[0.8, 0.2])
    else:
        return np.random.choice(['Si', 'No'], p=[0.1, 0.9])

# Aplicamos la lógica anterior a cada fila de nuestra tabla
df['abandono'] = df.apply(calcular_abandono, axis=1)

# Guardamos todo nuestro trabajo en un archivo CSV llamado igual que en la tarea
nombre_archivo = "dataset_abandono_escolar.csv"
df.to_csv(nombre_archivo, index=False, encoding='utf-8')

# --- BLOQUE DE IMPRESIÓN EN CONSOLA ---
# Esto solo sirve para que tú (o el profe) vean un resumen bonito al terminar
print(f"✅ ¡Dataset generado con éxito!: {nombre_archivo}")

print("\n" + "="*50)
print("       📊 REPORTE DE GENERACIÓN DE DATOS")
print("="*50)

print(f"✅ Archivo guardado: {nombre_archivo}")
print(f"👥 Total de registros: {len(df)}")
print("-"*50)

# Revisamos cuántos huecos vacíos (nulos) quedaron en cada columna
print("🔍 Verificación de Calidad (Valores Nulos):")
nulos = df.isnull().sum()
for col, cant in nulos.items():
    estado = "❌" if cant > 0 else "✅"
    print(f"   {estado} {col.ljust(15)}: {cant} nulos")

print("-"*50)

# Contamos cuántos estudiantes abandonaron y cuántos no
print("📈 Distribución de la Variable de Salida (Abandono):")
conteo = df['abandono'].value_counts()
for label, total in conteo.items():
    porcentaje = (total / len(df)) * 100
    print(f"   - {label}: {total} ({porcentaje:.1f}%)")

# Mostramos las primeras 5 filas para verificar que todo se ve bien
print("-"*50)
print("📋 Vista previa de los primeros 5 registros:")
print(df.head().to_string(index=False))
print("="*50 + "\n")