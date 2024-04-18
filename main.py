import pandas as pd

# Leemos el archivo CSV
def obtener_csv_como_lista(nombre_archivo): 
    with open(nombre_archivo, encoding='utf-8') as archivo:
        next(archivo) # Ignoramos la primera línea.
        edades = [] 
        for linea in archivo:
            edades.append(int(linea)) # Convertimos la edad a entero y lo agregamos a la lista
        return edades


# Obtenemos la lista de edades
edades = obtener_csv_como_lista('edades_alumnos.csv')

# Obtenemos frecuencia absoluta simple
def obtener_fi():
    fi = {} # Diccionario para almacenar las frecuencias
    for i in edades:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    return fi


def analisis_estadistico(edades):
    fi = obtener_fi() # Almacenamos en la variable fi la funcion obtener_fi
    df = pd.DataFrame({'edad': range(18, 36)}) # Creamos el DataFrame con un rango de 18 a 36 para las edades
    # Agregamos fi al DataFrame
    df['fi'] = df['edad'].map(fi).fillna(0).astype(int) # Si la edad no está en el diccionario se rellena con 0 y lo convertimos a entero.
    df['Fi'] = df['fi'].cumsum() # Calculamos frecuencia absoluta acumulada
    n = df['fi'].sum() # Calculamos la suma de frecuencias absolutas
    df['ri'] = (df['fi'] / n).round(4) # Calculamos frecuencia relativa simple
    df['Ri'] = (df['ri'].cumsum()).round(4) # Calculamos frecuencia relativa acumulada
    df['pi%'] = (df['ri'] * 100).round(4) # Calculamos frecuencia porcentual simple
    df['Pi%'] = (df['Ri'] * 100).round(4) # Calculamos frecuencia porcentual acumulada

    df.to_clipboard(index= False) # Guardamos en el portapapeles
    return df

print(analisis_estadistico(edades))