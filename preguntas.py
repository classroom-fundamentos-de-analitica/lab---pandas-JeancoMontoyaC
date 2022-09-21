"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")



def pregunta_01():
    filas,columnas=tbl0.shape
    return filas



def pregunta_02():
    filas,columnas=tbl0.shape
    return columnas



def pregunta_03():
    tbl00=tbl0.groupby("_c1").size()
    return tbl00



def pregunta_04():
    tbl00=tbl0.groupby("_c1").mean().pop("_c2")
    return tbl00




def pregunta_05():

    tbl00=tbl0.groupby("_c1").max().pop("_c2")
    return tbl00


def pregunta_06():
    tbl00 = tbl1['_c4'].unique()
    tbl00=sorted(map(lambda x: x.upper(),tbl00))
    return tbl00



def pregunta_07():
    tbl00=tbl0.groupby("_c1").sum().pop("_c2")
    return tbl00



def pregunta_08():
    sumas =list( tbl0.sum(numeric_only=True, axis=1))
    tbl00=tbl0.copy()
    tbl00["sumas"]=sumas
    return tbl00



def pregunta_09():
    years=list(map(lambda x:x.split("-")[0],list(tbl0["_c3"])))
    new=tbl0.copy()
    new["year"]=years
    return new


def pregunta_10():
    valores = list(tbl0[['_c1', '_c2']].groupby(['_c1'])['_c2'].apply(list))
    c2=[]
    for letra in valores:
        texto = ''
        for valor in sorted(letra):
            texto += str(valor)+":"  
        c2.append(texto[:-1])
    return pd.DataFrame({'_c2': c2}, index = pd.Series(['A', 'B', 'C', 'D', 'E'], name='_c1'))


def pregunta_11():
    lista = list(tbl1.groupby(['_c0'])['_c4'].apply(list))
    lista1 = list(tbl1['_c0'].unique())
    lista2 = []

    for i in lista:
        texto = ''
        for j in sorted(i):
            texto += str(j)+','
        lista2.append(texto[:-1])

    return pd.DataFrame({
        '_c0': lista1,
        '_c4': lista2
    })


def pregunta_12():
    c5a = tbl2.groupby(['_c0'])['_c5a'].apply(list).tolist()
    c5b = tbl2.groupby(['_c0'])['_c5b'].apply(list).tolist()
    c0 = tbl1['_c0'].unique().tolist()
    c5 = []
    for i in range(len(c5a)):
        x = []
        for j in range(len(c5a[i])):
            x.append(f'{c5a[i][j]}:{c5b[i][j]}')
        texto = ''
        for valor in sorted(x):
            texto += f'{valor},'
        c5.append(texto[:-1])
    return pd.DataFrame({
        '_c0': c0,
        '_c5': c5})


def pregunta_13():
    join = pd.merge(tbl0, tbl2, on='_c0', how='inner')
    lista = join[['_c1', '_c5b']].groupby(['_c1']).sum()
    serie = lista.squeeze()
    return serie
 
