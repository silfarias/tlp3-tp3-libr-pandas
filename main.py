import pandas as pd

# Leemos el archivo CSV que almacena las edades
def obtener_csv(name_file):
    data = pd.read_csv(name_file)
    df = data['edades'].tolist()
    return df
    

edades = obtener_csv('edades_alumnos.csv')
print(edades)

# Obtenemos frecuencia absoluta simple
def obtener_fi():
    fi = {} # Diccionario para almacenar las frecuenciass
    for i in edades:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    return fi


def analisis_estadistico(edades):
    fi = obtener_fi() # Almacenamos en la variable fi la funcion obtener_fi
    df = pd.DataFrame({'edad': range(18, 36)}) # Creamos el DataFrame con un rango de 18 a 35 para las edades
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