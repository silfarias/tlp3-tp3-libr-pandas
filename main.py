# lista_de_datos = [19,29,19,22,23,19,30,19,19,19,20,20,20,18,22,19,34,34,21,21,22,28,29,19,20,19,25,28,21,22]


def obtener_csv_como_lista(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as archivo:
        next(archivo)
        edades = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            edades.append(int(linea))
        return edades

def obtener_fi():
    edades = obtener_csv_como_lista('edades_alumnos.csv')
    fi = {}
    for i in edades:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    return fi

print(obtener_fi())




# def analisis_estadistico(lista_edades):
#     dicc = {}
#     data_frames = pd.read_csv('edades_alumnos.csv')