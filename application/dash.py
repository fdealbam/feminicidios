import dash
import matplotlib.pyplot as plt 
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os

yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")



###############################
# DATABASES
############################### Abre archivos

defunciones15 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def15_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones16 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def16_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones17 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def17_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones18 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def18_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
defunciones19 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def19_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
                    )
#defunciones20 = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/def20_r_femeninas_tabla%20de%20datos.csv", encoding= "Latin-1", 
#                    )
def_tot15 =defunciones15.iloc[0]['Valor']
def15_tot =defunciones15.iloc[0]['Valor']
agr15_val = defunciones15.iloc[29]['Valor']
agr15_txt = defunciones15.iloc[29]['Variable']
agr215_val  = defunciones15.iloc[30]['Valor']
agr215_txt  = defunciones15.iloc[30]['Variable']
viofm15_val = defunciones15.iloc[19]['Valor']
viofm15_txt = defunciones15.iloc[19]['Variable']
lug115_val = defunciones15.iloc[10]['Valor']
lug115_txt = defunciones15.iloc[10]['Variable']
lug215_val = defunciones15.iloc[11]['Valor']
lug215_txt = defunciones15.iloc[11]['Variable']
aurb15_val = defunciones15.iloc[17]['Valor']
aurb15_txt = defunciones15.iloc[17]['Variable']
ent115_val = defunciones15.iloc[2]['Valor']
ent115_txt = defunciones15.iloc[2]['Variable']
ent215_val = defunciones15.iloc[3]['Valor']
ent215_txt = defunciones15.iloc[3]['Variable']
ent315_val = defunciones15.iloc[4]['Valor']
ent315_txt = defunciones15.iloc[4]['Variable']
eda115_val = defunciones15.iloc[21]['Valor']
eda115_txt = defunciones15.iloc[21]['Variable']
eda215_val = defunciones15.iloc[22]['Valor']
eda215_txt = defunciones15.iloc[22]['Variable']
eda315_val = defunciones15.iloc[23]['Valor']
eda315_txt = defunciones15.iloc[23]['Variable']
emba15_val = defunciones15.iloc[14]['Valor']
emba15_txt = defunciones15.iloc[14]['Variable']
esc115_val = defunciones15.iloc[6]['Valor']
esc115_txt = defunciones15.iloc[6]['Variable']
esc215_val = defunciones15.iloc[7]['Valor']
esc215_txt = defunciones15.iloc[7]['Variable']
esc315_val = defunciones15.iloc[8]['Valor']
esc315_txt = defunciones15.iloc[8]['Variable']

def16_tot   = defunciones16.iloc[0]['Valor']
agr16_val   = defunciones16.iloc[29]['Valor']
agr16_txt   = defunciones16.iloc[29]['Variable']
agr216_val  = defunciones16.iloc[30]['Valor']
agr216_txt  = defunciones16.iloc[30]['Variable']
viofm16_val = defunciones16.iloc[19]['Valor']
viofm16_txt = defunciones16.iloc[19]['Variable']
lug116_val  = defunciones16.iloc[10]['Valor']
lug116_txt  = defunciones16.iloc[10]['Variable']
lug216_val  = defunciones16.iloc[11]['Valor']
lug216_txt  = defunciones16.iloc[11]['Variable']
aurb16_val  = defunciones16.iloc[17]['Valor']
aurb16_txt  = defunciones16.iloc[17]['Variable']
ent116_val  = defunciones16.iloc[2]['Valor']
ent116_txt  = defunciones16.iloc[2]['Variable']
ent216_val  = defunciones16.iloc[3]['Valor']
ent216_txt  = defunciones16.iloc[3]['Variable']
ent316_val  = defunciones16.iloc[4]['Valor']
ent316_txt  = defunciones16.iloc[4]['Variable']
eda116_val  = defunciones16.iloc[21]['Valor']
eda116_txt  = defunciones16.iloc[21]['Variable']
eda216_val  = defunciones16.iloc[22]['Valor']
eda216_txt  = defunciones16.iloc[22]['Variable']
eda316_val  = defunciones16.iloc[23]['Valor']
eda316_txt  = defunciones16.iloc[23]['Variable']
emba16_val  = defunciones16.iloc[14]['Valor']
emba16_txt  = defunciones16.iloc[14]['Variable']
esc116_val  = defunciones16.iloc[6]['Valor']
esc116_txt  = defunciones16.iloc[6]['Variable']
esc216_val  = defunciones16.iloc[7]['Valor']
esc216_txt  = defunciones16.iloc[7]['Variable']
esc316_val  = defunciones16.iloc[8]['Valor']
esc316_txt  = defunciones16.iloc[8]['Variable']

def17_tot   = defunciones17.iloc[0]['Valor']
agr17_val   = defunciones17.iloc[29]['Valor']
agr17_txt   = defunciones17.iloc[29]['Variable']
agr217_val  = defunciones17.iloc[30]['Valor']
agr217_txt  = defunciones17.iloc[30]['Variable']
viofm17_val = defunciones17.iloc[19]['Valor']
viofm17_txt = defunciones17.iloc[19]['Variable']
lug117_val  = defunciones17.iloc[10]['Valor']
lug117_txt  = defunciones17.iloc[10]['Variable']
lug217_val  = defunciones17.iloc[11]['Valor']
lug217_txt  = defunciones17.iloc[11]['Variable']
aurb17_val  = defunciones17.iloc[17]['Valor']
aurb17_txt  = defunciones17.iloc[17]['Variable']
ent117_val  = defunciones17.iloc[2]['Valor']
ent117_txt  = defunciones17.iloc[2]['Variable']
ent217_val  = defunciones17.iloc[3]['Valor']
ent217_txt  = defunciones17.iloc[3]['Variable']
ent317_val  = defunciones17.iloc[4]['Valor']
ent317_txt  = defunciones17.iloc[4]['Variable']
eda117_val  = defunciones17.iloc[21]['Valor']
eda117_txt  = defunciones17.iloc[21]['Variable']
eda217_val  = defunciones17.iloc[22]['Valor']
eda217_txt  = defunciones17.iloc[22]['Variable']
eda317_val  = defunciones17.iloc[23]['Valor']
eda317_txt  = defunciones17.iloc[23]['Variable']
emba17_val  = defunciones17.iloc[14]['Valor']
emba17_txt  = defunciones17.iloc[14]['Variable']
esc117_val  = defunciones17.iloc[6]['Valor']
esc117_txt  = defunciones17.iloc[6]['Variable']
esc217_val  = defunciones17.iloc[7]['Valor']
esc217_txt  = defunciones17.iloc[7]['Variable']
esc317_val  = defunciones17.iloc[8]['Valor']
esc317_txt  = defunciones17.iloc[8]['Variable']

def18_tot   = defunciones18.iloc[0]['Valor']
agr18_val   = defunciones18.iloc[29]['Valor']
agr18_txt   = defunciones18.iloc[29]['Variable']
agr218_val  = defunciones18.iloc[30]['Valor']
agr218_txt  = defunciones18.iloc[30]['Variable']
viofm18_val = defunciones18.iloc[19]['Valor']
viofm18_txt = defunciones18.iloc[19]['Variable']
lug118_val  = defunciones18.iloc[10]['Valor']
lug118_txt  = defunciones18.iloc[10]['Variable']
lug218_val  = defunciones18.iloc[11]['Valor']
lug218_txt  = defunciones18.iloc[11]['Variable']
aurb18_val  = defunciones18.iloc[17]['Valor']
aurb18_txt  = defunciones18.iloc[17]['Variable']
ent118_val  = defunciones18.iloc[2]['Valor']
ent118_txt  = defunciones18.iloc[2]['Variable']
ent218_val  = defunciones18.iloc[3]['Valor']
ent218_txt  = defunciones18.iloc[3]['Variable']
ent318_val  = defunciones18.iloc[4]['Valor']
ent318_txt  = defunciones18.iloc[4]['Variable']
eda118_val  = defunciones18.iloc[21]['Valor']
eda118_txt  = defunciones18.iloc[21]['Variable']
eda218_val  = defunciones18.iloc[22]['Valor']
eda218_txt  = defunciones18.iloc[22]['Variable']
eda318_val  = defunciones18.iloc[23]['Valor']
eda318_txt  = defunciones18.iloc[23]['Variable']
emba18_val  = defunciones18.iloc[14]['Valor']
emba18_txt  = defunciones18.iloc[14]['Variable']
esc118_val  = defunciones18.iloc[6]['Valor']
esc118_txt  = defunciones18.iloc[6]['Variable']
esc218_val  = defunciones18.iloc[7]['Valor']
esc218_txt  = defunciones18.iloc[7]['Variable']
esc318_val  = defunciones18.iloc[8]['Valor']
esc318_txt  = defunciones18.iloc[8]['Variable']

def19_tot   = defunciones19.iloc[0]['Valor']
agr19_val   = defunciones19.iloc[29]['Valor']
agr19_txt   = defunciones19.iloc[29]['Variable']
agr219_val  = defunciones19.iloc[30]['Valor']
agr219_txt  = defunciones19.iloc[30]['Variable']
viofm19_val = defunciones19.iloc[19]['Valor']
viofm19_txt = defunciones19.iloc[19]['Variable']
lug119_val  = defunciones19.iloc[10]['Valor']
lug119_txt  = defunciones19.iloc[10]['Variable']
lug219_val  = defunciones19.iloc[11]['Valor']
lug219_txt  = defunciones19.iloc[11]['Variable']
aurb19_val  = defunciones19.iloc[17]['Valor']
aurb19_txt  = defunciones19.iloc[17]['Variable']
ent119_val  = defunciones19.iloc[2]['Valor']
ent119_txt  = defunciones19.iloc[2]['Variable']
ent219_val  = defunciones19.iloc[3]['Valor']
ent219_txt  = defunciones19.iloc[3]['Variable']
ent319_val  = defunciones19.iloc[4]['Valor']
ent319_txt  = defunciones19.iloc[4]['Variable']
eda119_val  = defunciones19.iloc[21]['Valor']
eda119_txt  = defunciones19.iloc[21]['Variable']
eda219_val  = defunciones19.iloc[22]['Valor']
eda219_txt  = defunciones19.iloc[22]['Variable']
eda319_val  = defunciones19.iloc[23]['Valor']
eda319_txt  = defunciones19.iloc[23]['Variable']
emba19_val  = defunciones19.iloc[14]['Valor']
emba19_txt  = defunciones19.iloc[14]['Variable']
esc119_val  = defunciones19.iloc[6]['Valor']
esc119_txt  = defunciones19.iloc[6]['Variable']
esc219_val  = defunciones19.iloc[7]['Valor']
esc219_txt  = defunciones19.iloc[7]['Variable']
esc319_val  = defunciones19.iloc[8]['Valor']
esc319_txt  = defunciones19.iloc[8]['Variable']

#os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")

delitos = pd.read_csv("https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/feminicidios2015_2021.csv?raw=true")
delitos.drop('Unnamed: 0',1, inplace=True)

delitos.groupby(['Año','Entidad','Tipo de delito'])['Enero', 
                 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre',
       'Noviembre', 'Diciembre'].sum().to_csv("00.csv",  header=True)

fem= pd.read_csv("00.csv")

############################################### separación de años

year15= fem[fem.Año == 2015]
year16= fem[fem.Año == 2016]
year17= fem[fem.Año == 2017]
year18= fem[fem.Año == 2018]
year19= fem[fem.Año == 2019]
year20= fem[fem.Año == 2020]
year21= fem[fem.Año == 2021]

############################################### Agregar suffix de años

y15 = year15.add_suffix('15')
y15.rename(columns ={'Año15': 'Año', 'Tipo de delito15': 'Tipo de delito', 'Unnamed: 015' : 'Unnamed: 0',
                            'Entidad15': 'Entidad'}, inplace = True)

y16 = year16.add_suffix('16')
y16.rename(columns ={'Año16': 'Año', 'Tipo de delito16': 'Tipo de delito', 'Unnamed: 016' : 'Unnamed: 0',
                            'Entidad16': 'Entidad'}, inplace = True)

y17 = year17.add_suffix('17')
y17.rename(columns ={'Año17': 'Año', 'Tipo de delito17': 'Tipo de delito', 'Unnamed: 017' : 'Unnamed: 0',
                            'Entidad17': 'Entidad'}, inplace = True)

y18= year18.add_suffix('18')
y18.rename(columns ={'Año18': 'Año', 'Tipo de delito18': 'Tipo de delito','Unnamed: 018' : 'Unnamed: 0',
                            'Entidad18': 'Entidad'}, inplace = True)

y19= year19.add_suffix('19')
y19.rename(columns ={'Año19': 'Año', 'Tipo de delito19': 'Tipo de delito', 'Unnamed: 019' : 'Unnamed: 0',
                            'Entidad19': 'Entidad'}, inplace = True)

y20= year20.add_suffix('20')
y20.rename(columns ={'Año20': 'Año', 'Tipo de delito20': 'Tipo de delito','Unnamed: 020' : 'Unnamed: 0',
                            'Entidad20': 'Entidad'}, inplace = True)

y21= year21.add_suffix('21')
y21.rename(columns ={'Año21': 'Año', 'Tipo de delito21': 'Tipo de delito','Unnamed: 021' : 'Unnamed: 0',
                            'Entidad21': 'Entidad'}, inplace = True)



############################################### Concat todos los años

fa = y15.merge(y16, on="Entidad",  how="inner")
fb = fa.merge(y17, on="Entidad",  how="inner")
fc = fb.merge(y18, on="Entidad",  how="inner")
fd = fc.merge(y19, on="Entidad",  how="inner")
fe = fd.merge(y20, on="Entidad",  how="inner")
ff = fe.merge(y21, on="Entidad",  how="inner")
                    
femi15_21 = ff[[
 'Entidad','Enero15','Febrero15','Marzo15','Abril15','Mayo15','Junio15',
 'Julio15','Agosto15','Septiembre15','Octubre15','Noviembre15','Diciembre15',
 
 'Enero16','Febrero16','Marzo16','Abril16','Mayo16','Junio16','Julio16',
 'Agosto16','Septiembre16','Octubre16','Noviembre16','Diciembre16',

 'Enero17','Febrero17','Marzo17','Abril17','Mayo17','Junio17','Julio17',
 'Agosto17','Septiembre17','Octubre17','Noviembre17','Diciembre17',
    
 'Enero18','Febrero18','Marzo18','Abril18','Mayo18','Junio18','Julio18',
 'Agosto18','Septiembre18','Octubre18','Noviembre18','Diciembre18',
 
 'Enero19','Febrero19','Marzo19','Abril19','Mayo19','Junio19','Julio19',
 'Agosto19','Septiembre19','Octubre19','Noviembre19','Diciembre19',

 'Enero20','Febrero20','Marzo20','Abril20','Mayo20','Junio20','Julio20',
 'Agosto20','Septiembre20','Octubre20','Noviembre20','Diciembre20',
    
 'Enero21','Febrero21'#,'Marzo21','Abril21','Mayo21','Junio21','Julio21',
# 'Agosto21','Septiembre21','Octubre21','Noviembre21','Diciembre21'
             ]]



##CRear columna de TOTAL ANUAL 
femi15_21['Total2015']= femi15_21[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               'Junio15', 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               'Noviembre15', 'Diciembre15',]].sum(axis=1)
femi15_21['Total2016']= femi15_21[[ 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16',
                               'Junio16', 'Julio16', 'Agosto16', 'Septiembre16', 'Octubre16',
                               'Noviembre16', 'Diciembre16',]].sum(axis=1)
femi15_21['Total2017']= femi15_21[[ 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17',
                               'Junio17', 'Julio17', 'Agosto17', 'Septiembre17', 'Octubre17',
                               'Noviembre17', 'Diciembre17',]].sum(axis=1)
femi15_21['Total2018']= femi15_21[[ 'Enero18', 'Febrero18', 'Marzo18', 'Abril18', 'Mayo18',
                               'Junio18', 'Julio18', 'Agosto18', 'Septiembre18', 'Octubre18',
                               'Noviembre18', 'Diciembre18',]].sum(axis=1)
femi15_21['Total2019']= femi15_21[[ 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19',
                               'Junio19', 'Julio19', 'Agosto19', 'Septiembre19', 'Octubre19',
                               'Noviembre19', 'Diciembre19',]].sum(axis=1)
femi15_21['Total2020']= femi15_21[[ 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20',
                               'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               'Noviembre20', 'Diciembre20',]].sum(axis=1)

femi15_21['Total2021']= femi15_21[[ 'Enero21','Febrero21'#, 'Marzo21', 'Abril21', 'Mayo21',
                                   #'Junio21','Julio21','Agosto21','Septiembre21','Octubre21',
                                   #'Noviembre21','Diciembre21'
                                  ]].sum(axis=1)


#identificadores
conf_2015= femi15_21.Total2015.sum()
conf_2016= femi15_21.Total2016.sum()
conf_2017= femi15_21.Total2017.sum()
conf_2018= femi15_21.Total2018.sum()
conf_2019= femi15_21.Total2019.sum()
conf_2020= femi15_21.Total2020.sum()
conf_2021= femi15_21.Total2021.sum()



################################################## PREPARA GRAFICA MENSUAL
pagra = ff[[
  'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15', 'Junio15', 'Julio15', 'Agosto15', 
    'Septiembre15', 'Octubre15', 'Noviembre15', 'Diciembre15',
 
 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16', 'Junio16', 'Julio16', 'Agosto16', 
    'Septiembre16', 'Octubre16', 'Noviembre16', 'Diciembre16',

 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17', 'Junio17', 'Julio17', 'Agosto17', 
    'Septiembre17', 'Octubre17', 'Noviembre17', 'Diciembre17', 
    'Enero18', 'Febrero18', 'Marzo18',    'Abril18', 'Mayo18', 'Junio18', 'Julio18', 'Agosto18',
    'Septiembre18', 'Octubre18', 'Noviembre18', 'Diciembre18',
 
 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19', 'Junio19', 'Julio19', 'Agosto19', 
    'Septiembre19', 'Octubre19', 'Noviembre19', 'Diciembre19',

 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20', 'Junio20', 'Julio20', 'Agosto20',
    'Septiembre20','Octubre20', 'Noviembre20', 'Diciembre20',

 'Enero21', 'Febrero21'#, 'Marzo21', 'Abril21', 'Mayo21', 'Junio21', 'Julio21', 'Agosto21',
  #  'Septiembre21','Octubre21','Noviembre21','Diciembre21'
            ]]


pagrafm = pagra.stb.subtotal()
pagrafm.to_csv("0000procesod.csv")
#Selecciona ultima columna (Totales)
other  = pd.read_csv('0000procesod.csv')
other_s = other.iloc[32]
other_b = pd.DataFrame(other_s)
other_b.to_csv('0000procesodi.csv')
vuelve_a_abrir = pd.read_csv('0000procesodi.csv')
##Elimina filas 0 a 4 
gra_mes = vuelve_a_abrir.drop([0])
#Renombra titulo de columna
gra_mes = gra_mes.rename(columns= {"Unnamed: 0": "Mes"})
gra_mes = gra_mes.rename(columns= {"32": "Total"})
gra_mes['Total'] = pd.to_numeric(gra_mes['Total'])


#Grafica mensual 
graf_meses = go.Figure()
graf_meses.add_trace(go.Bar(x=gra_mes['Mes'],y=gra_mes['Total'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))
graf_meses.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Acumulados mensuales',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    #width=1000,
    #height=400
    )





#- FILE JSON PARA ENTIDADES ------------------------------------------------------------------------------



################################################ SUMA TODOS LOS AÑOS ranking de municipios por estado (3edos)

#filtro de feminicidio
delitos.groupby(['Municipio','Entidad',])['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                                             'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre',
                                             'Noviembre', 'Diciembre'].sum().to_csv('0000procesofem.csv')

fem_filter1=pd.read_csv('0000procesofem.csv')
fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']] = fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']].astype(int)
    
fem_filter1['Total']=fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']].sum(1)



#- FILE MUNICIPIOS ------------------------------------------------------------------------------

fem_filter1.fillna(0, inplace=True) 
fem_filter1['Total']=fem_filter1['Total'].astype(int)


############################################### filtro para estados(4) e identifiación de mpios y abs feminicidios

# estado 1
estado1=fem_filter1[fem_filter1.Entidad=='México']
edo1orden=estado1[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo1mpio1=edo1orden.iloc[0]['Municipio']
edo1mpio1v=edo1orden.iloc[0]['Total']
#2
edo1mpio2=edo1orden.iloc[1]['Municipio']
edo1mpio2v=edo1orden.iloc[1]['Total']
#3
edo1mpio3=edo1orden.iloc[2]['Municipio']
edo1mpio3v=edo1orden.iloc[2]['Total']
#4
edo1mpio4=edo1orden.iloc[3]['Municipio']
edo1mpio4v=edo1orden.iloc[3]['Total']
#5
edo1mpio5=edo1orden.iloc[4]['Municipio']
edo1mpio5v=edo1orden.iloc[4]['Total']


# estado 2
estado2=fem_filter1[fem_filter1.Entidad=='Veracruz de Ignacio de la Llave']
edo2orden=estado2[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo2mpio1=edo2orden.iloc[0]['Municipio']
edo2mpio1v=edo2orden.iloc[0]['Total']
#2
edo2mpio2=edo2orden.iloc[1]['Municipio']
edo2mpio2v=edo2orden.iloc[1]['Total']
#3
edo2mpio3=edo2orden.iloc[2]['Municipio']
edo2mpio3v=edo2orden.iloc[2]['Total']
#4
edo2mpio4=edo2orden.iloc[3]['Municipio']
edo2mpio4v=edo2orden.iloc[3]['Total']
#5
edo2mpio5=edo2orden.iloc[4]['Municipio']
edo2mpio5v=edo2orden.iloc[4]['Total']


# estado 3
estado3=fem_filter1[fem_filter1.Entidad=='Ciudad de México']
edo3orden=estado3[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo3mpio1=edo3orden.iloc[0]['Municipio']
edo3mpio1v=edo3orden.iloc[0]['Total']
#2
edo3mpio2=edo3orden.iloc[1]['Municipio']
edo3mpio2v=edo3orden.iloc[1]['Total']
#3
edo3mpio3=edo3orden.iloc[2]['Municipio']
edo3mpio3v=edo3orden.iloc[2]['Total']
#4
edo3mpio4=edo3orden.iloc[3]['Municipio']
edo3mpio4v=edo3orden.iloc[3]['Total']
#5
edo3mpio5=edo3orden.iloc[4]['Municipio']
edo3mpio5v=edo3orden.iloc[4]['Total']


# estado 4
estado4=fem_filter1[fem_filter1.Entidad=='Jalisco']
edo4orden=estado4[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo4mpio1=edo4orden.iloc[0]['Municipio']
edo4mpio1v=edo4orden.iloc[0]['Total']
#2
edo4mpio2=edo4orden.iloc[1]['Municipio']
edo4mpio2v=edo4orden.iloc[1]['Total']
#3
edo4mpio3=edo4orden.iloc[2]['Municipio']
edo4mpio3v=edo4orden.iloc[2]['Total']
#4
edo4mpio4=edo4orden.iloc[3]['Municipio']
edo4mpio4v=edo4orden.iloc[3]['Total']
#5
edo4mpio5=edo4orden.iloc[4]['Municipio']
edo4mpio5v=edo4orden.iloc[4]['Total']



######################################################### tablas Ranking municipios
# tabla 1
patabla1 = {'Mpio' : [edo1mpio1,edo1mpio2,edo1mpio3,edo1mpio4,edo1mpio5],
            'Casos': [edo1mpio1v,edo1mpio2v,edo1mpio3v,edo1mpio4v,edo1mpio5v],}

patabla1a = pd.DataFrame (patabla1, columns = ['Mpio','Casos'])


############## tabla 2
patabla2 = {'Mpio'  : [edo2mpio1,edo2mpio2,edo2mpio3,edo2mpio4,edo2mpio5],
            'Casos' : [edo2mpio1v,edo2mpio2v,edo2mpio3v,edo2mpio4v,edo2mpio5v],}

patabla2a = pd.DataFrame (patabla2, columns = ['Mpio','Casos'])


############## tabla 3
patabla3 = {'Mpio'  : [edo3mpio1,edo3mpio2,edo3mpio3,edo3mpio4,edo3mpio5],
            'Casos' : [edo3mpio1v,edo3mpio2v,edo3mpio3v,edo3mpio4v,edo3mpio5v],}

patabla3a = pd.DataFrame (patabla3, columns = ['Mpio','Casos'])


############## tabla 4
patabla4 = {'Mpio'  : [edo4mpio1,edo4mpio2,edo4mpio3,edo4mpio4,edo4mpio5],
            'Casos' : [edo4mpio1v,edo4mpio2v,edo4mpio3v,edo4mpio4v,edo4mpio5v],}

patabla4a = pd.DataFrame (patabla4, columns = ['Mpio','Casos'])




######################################################### Graf. Tasas de feminicidios por entidad 2015-2020

junto1 = pd.read_csv('https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/POB_15_21.csv')
fem15_21 = femi15_21[['Entidad', 'Total2015', 'Total2016', 'Total2017',
       'Total2018', 'Total2019', 'Total2020', 'Total2021']]

junto15_21 = fem15_21.merge(junto1,right_on='NOM_ENT',left_on='Entidad')
junto15_21["Entidad"].replace('Veracruz de Ignacio de la Llave','Veracruz' , inplace=True)

junto15_21['Totfem1521']=junto15_21[['Total2015', 'Total2016', 'Total2017', 'Total2018','Total2019', 'Total2020', 'Total2021']].sum(1)
junto15_21['Totpob1521']=junto15_21[['POB15', 'POB16', 'POB17', 'POB18','POB19', 'POB20', 'POB21']].sum(1)
junto15_21['Tasa1521']=((junto15_21.Totfem1521/junto15_21.Totpob1521)*100000).round(2)

TasasFem15_21index=junto15_21[['Entidad','Totfem1521','Totpob1521','Tasa1521']].sort_values('Tasa1521',ascending=False)


######################################################### Grafica Totales

graf_tasafem = go.Figure()
graf_tasafem.add_trace(go.Bar(x=TasasFem15_21index['Entidad'],y=TasasFem15_21index['Tasa1521'],
                marker_color='sandybrown'  # cambiar nuemeritos de rgb
                ))

graf_tasafem.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    #title='Tasa feminicidio periodo 2015-2020',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Tasa cada 100 000 habitantes',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
#    width=2100,
#    height=600
    )


######################################################### Grafica Total

TasasTot15_21index=junto15_21[['Entidad','Totfem1521','Totpob1521','Tasa1521']].sort_values('Totfem1521',ascending=False)

graf_totfem = go.Figure()
graf_totfem.add_trace(go.Bar(x=TasasTot15_21index['Entidad'],y=TasasTot15_21index['Totfem1521'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))

graf_totfem.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    #title='Tasa feminicidio periodo 2015-2020',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Tasa cada 100 000 habitantes',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
 #   width=2100,
  #  height=600
    )


######################################################### MAPAS 3estados con más feminicidios

#concat2 = fem_filter1[fem_filter1.Entidad == "Veracruz de Ignacio de la Llave"]
#concat.plot("NOM_ENT", cmap= "Oranges", legend=True, k=5)
#plt.axis("off")
#plt.savefig("ver.png", dpi= 120)
#plt.show()


####################################

# A P P

####################################

########### Define your variables
mytitle=' '
tabtitle='Feminicidios'
sourceurl='https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published'


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. FLATLY], server=server)

body = html.Div([
# Cintillo 000
        dbc.Row(
           [
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width={'size': 1,  "offset": 1}),
               dbc.Col(html.H1("Feminicidios en México (2015-2020)"),
                        width={'offset' : 2}),
           ]),

#Cintillo 00    
    dbc.Row(
           [
               dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 4}), 
               dbc.Col(html.H6("Fuente: SENSNSP"),
                        width={'size': 3,  "offset":1 }),
            ]),
               
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
    
#cintillo 0
    
     dbc.Row(
           [
               dbc.Col(html.H1(["Casos ", 
                                dbc.Badge("anuales", color="info", className="mr-1")]),
                        width={'size': 8,  "offset":1 }),
            ]),

      html.Br(),
    
     dbc.Row(
           [
               dbc.Col(html.H5("2015")),
               dbc.Col(html.H5("2016")),
               dbc.Col(html.H5("2017")),
               dbc.Col(html.H5("2018")),
               dbc.Col(html.H5("2019")),
               dbc.Col(html.H5("2020")),
           ], justify= "start"),
    
#Cintillo 1
    dbc.Row(
           [
               dbc.Col(html.H1(conf_2015)),
               dbc.Col(html.H1(conf_2016)),
               dbc.Col(html.H1(conf_2017)),
               dbc.Col(html.H1(conf_2018)),
               dbc.Col(html.H1(conf_2019)),
               dbc.Col(html.H1(conf_2020)),
            ],justify= "start"),
    
# Cintillo 1.1
        dbc.Row([
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/mapa2015.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/mapa2016.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/mapa2017.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/mapa2018.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/mapa2019.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/mapa2020.jpeg?raw=true")),
           ]),
# Cintillo párrafos
       html.Br(),
    
#      dbc.Row([
#               dbc.Col(dbc.Container([
#                       html.P(
#                           "En 10 entidades se registraron 82.2% de feminicidios (338)"
#                           " en 2015: Jalisco (62), México (59), Ciudad de México (56),"
#                           "Veracruz (40), Chiapas (36), Sonora (24), Guanajuato (16),"
#                           "Coahuila (16), Morelos (15) y Sinaloa (14).",
#                    className="top",)
#                                ], fluid=True)
#                       
#                      ),
#        
#          dbc.Col(dbc.Jumbotron([
#                   dbc.Container([
#                       html.P(
#                           "En 10 entidades se registraron 71.5% de feminicidios (433)"
#                           " en 2016 : Oaxaca (67), Veracruz (58), México (56), Jalisco"
#                           "(48), Ciudad de México (46), Sinaloa (39), Chiapas (32), "
#                           "Sonora (30), Morelos (30) y Tabasco (27).",
#                    className="top")
#                                ], fluid=True)
#                                    ], fluid=True)
#                      ),
#          dbc.Col(
#                   dbc.Container([
#                       html.P(
#                           "En 10 entidades se registraron 68.3% de feminicidios (507)"
#                           " en 2017 : Veracruz (100), Sinaloa (82), México (70), Oaxaca"
#                           " (57), Nuevo León (43), Ciudad de México (37), Sonora (32),"
#                           " Michoacán (29), Chiapas (29) y Tabasco (28).",
#                    className="top")
#                                ], fluid=True)
#                                    )
#                      ,
#          dbc.Col(dbc.Jumbotron([
#                   dbc.Container([
#                       html.P(
#                           "En 10 entidades se registraron 63.6% de feminicidios (568)"
#                           " en 2018 : México (115), Veracruz (101), Nuevo León (79), "
#                           "Sinaloa (48), Chihuahua (44), Ciudad de México (43), Tabasco"
#                           " (40), Jalisco (33), Guerrero (33) y Puebla (32).",
#                    className="top")
#                                ], fluid=True)
#                                    ], fluid=True)
#                      ),
#          dbc.Col(dbc.Container([
#                       html.P(
#                           "En 10 entidades se registraron 66.4% de feminicidios (627)"
#                           " en 2019 : México (122), Veracruz (104), Ciudad de México "
#                           "(72), Nuevo León (67), Jalisco (62), Puebla (58), Morelos "
#                           "(39), Sonora (37), Sinaloa (37) y Chihuahua (29).",
#                    className="top")
#                                ], fluid=True)
#                      ),
#          dbc.Col(dbc.Jumbotron([
#                   dbc.Container([
#                       html.P(
#                           "En 10 entidades se registraron 65.8% de feminicidios (618)"
#                           " en 2020 : México (150), Veracruz (84), Nuevo León (67), "
#                           "Jalisco (66), Ciudad de México (64), Puebla (52), Oaxaca "
#                           "(38), Morelos (35), Sonora (31) y Baja California (31).",
#                    className="top")
#                                ], fluid=True)
#                                    ], fluid=True),
#                  
#                      ),
#      ]),
#                
    
       html.Br(),
#     dbc.Row(
#           [
#               dbc.Col(html.H1([dbc.Badge((def_tot15), className="ml-1",color="light"),
#                               "  "]),
#                       width={'size': 10,  "offset":1 }),
#            ]),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
   
       
#---------Grafica mensual
     dbc.Row(
           [
               dbc.Col(html.H1(["Casos ", 
                       dbc.Badge("mensuales", color="info", className="mr-1")]), 
                                       width={'size': 11,  "offset":1 })]),
       dbc.Row(
           [        
               dbc.Col(html.H5("(hasta febrero 2021)"),
                                       width={ 'size': 3, "offset":1 }),

            ]),
   
    dbc.Row(
        [
            dbc.Col(dcc.Graph(figure=graf_meses, config= "autosize")),
        ]),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
    
##Cintillo mapas y ranking

    #títulos
     dbc.Row(
           [
               dbc.Col(html.H1([dbc.Badge("Municipios", color="info", className="ml-1"), 
                               " en entidades con más casos acumulados ",]),
                       
                        width={'size': 10,  "offset":1 }),
            ]),
    html.Br(),
    html.Br(),
    
     dbc.Row(
           [
               dbc.Col(html.H3("México", ),
                       #width=1, 
                       lg={'size': 1,  "offset": 1, }
                      ),
               
               dbc.Col(html.H3("Veracruz"),
                        #width=1, 
                       lg={'size': 1,  "offset": 1, }
                      ),
               
               dbc.Col(html.H3("Ciudad de México"),
                       # width=1, 
                       lg={'size': 3,  "offset": 2, }
                      ),
                      
               dbc.Col(html.H3("Jalisco"),
                       # width=1, 
                       lg={'size': 1,  "offset": 1, }
                      ),
           ], #, justify= "end", 
    align= "center"),

    
    dbc.Row([
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/mx2.jpeg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/ver2.jpeg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/cdmx2.jpeg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/feminicidios/blob/main/application/static/jal2.jpeg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
           ], no_gutters=True),
       

    #################################################################  MUNICIPIOS ranking    

    dbc.Row([
               dbc.Col(dbc.Container([
                       html.P(
                           "Los 10 Municipios con mayor número de casos de feminicidios son:"
                           " Ecatepec de Morelos (56), Chimalhuacán (35), Nezahualcóyotl (31)"
                           ", Toluca (27), Naucalpan de Juárez (22), Ixtapaluca (22), Zumpango"
                           "(21), Tecámac (19), Cuautitlán Izcalli (19), y Valle de Chalco"
                           "Solidaridad (16).",
                    className="top",)
                                ], fluid=True)
                       
                      ),
          dbc.Col(dbc.Jumbotron([
                   dbc.Container([
                       html.P(
                           "Los 10 Municipios con mayor número de casos de feminicidios son:"
                           " Veracruz (49), Xalapa (42), Coatzacoalcos (25), Córdoba (24), "
                           "Poza Rica de Hidalgo (17), Tuxpan (13), Papantla (12), Tierra "
                           "Blanca (11), Minatitlán (11), y San Andrés Tuxtla (11).",
                    className="top")
                                ], fluid=True)
                                    ], fluid=True)
                      ),
          dbc.Col(
                   dbc.Container([
                       html.P(
                           "Los 10 Municipios con mayor número de casos de feminicidios son:"
                           " Iztapalapa (68), Gustavo A. Madero (37), Tlalpan (35), Cuauhtémoc"
                           "(34), Xochimilco (25), Miguel Hidalgo (19), Álvaro Obregón (17),"
                           " Tláhuac (16), Coyoacán (14), y Venustiano Carranza (14).",
                    className="top")
                                ], fluid=True)
                                    )
                      ,
          dbc.Col(dbc.Jumbotron([
                   dbc.Container([
                       html.P(
                           "Los 10 Municipios con mayor número de casos de feminicidios son:"
                           " Guadalajara (51), Tlajomulco de Zúñiga (38), Zapopan (34), "
                           "El Salto (24), Tonalá (17), Puerto Vallarta (10), Ocotlán (6),"
                           " Tequila (6), Mezquitic (6), y Ixtlahuacán de los Membrillos (6).",
                    className="top")
                                ], fluid=True)
                                    ], fluid=True)
                      ),
      ]),

#############################################  MUNICIPIOS ranking (OPCION  2)
#    dbc.Row([
#               dbc.Col(dbc.Container([
#                       html.P(
#                           "Ecatepec de Morelos (56)"
#                           "Chimalhuacán (35)"
#                           "Nezahualcóyotl (31)"
#                           "Toluca (27)"
#                           "Naucalpan de Juárez (22)"
#                           "Ixtapaluca (22)"
#                           "Zumpango (21)"
#                           "Tecámac (19)"
#                           "Cuautitlán Izcalli (19)"
#                           "Valle de Chalco Solidaridad (16)",
#                    className="top",)
#                                ],)
#                       
#                      ),
#          dbc.Col(dbc.Jumbotron([
#                   dbc.Container([
#                       html.P(
#                           "Veracruz (49)"
#                           "Xalapa (42)"
#                           "Coatzacoalcos (25)"
#                           "Córdoba (24)"
#                           "Poza Rica de Hidalgo (17)"
#                           "Tuxpan (13)"
#                           "Papantla (12)"
#                           "Tierra Blanca (11)"
#                           "Minatitlán (11)"
#                           "San Andrés Tuxtla (11)",
#                    className="top")
#                                ], )
#                                    ], )
#                      ),
#          dbc.Col(
#                   dbc.Container([
#                       html.P(
#                           "Iztapalapa (68)"
#                           "Gustavo A. Madero (37)"
#                           "Tlalpan (35)"
#                           "Cuauhtémoc (34)"
#                           "Xochimilco (25)"
#                           "Miguel Hidalgo (19)"
#                           "Álvaro Obregón (17)"
#                           "Tláhuac (16)"
#                           "Coyoacán (14)"
#                           "Venustiano Carranza (14)",
#                    className="top")
#                                ],)
#                                    )
#                      ,
#          dbc.Col(dbc.Jumbotron([
#                   dbc.Container([
#                       html.P(
#                           "Guadalajara (51)"
#                           "Tlajomulco de Zúñiga (38)"
#                           "Zapopan (34)"
#                           "El Salto (24)"
#                           "Tonalá (17)"
#                           "Puerto Vallarta (10)"
#                           "Ocotlán (6)"
#                           "Tequila (6)"
#                           "Mezquitic (6)"
#                           "Ixtlahuacán de los Membrillos (6)",
#                    className="top")
#                                ], )
#                                    ], )
#                      ),
#      ]),
#  
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
   
    
# Cintillo 3
     
       
#---------Grafica por entidad
     dbc.Row(
           [
               dbc.Col(html.H1([dbc.Badge("Comparativo", color="info", className="mr-1"),
                               " entre casos acumulados & tasas "]),
                       width={'size': 10,  "offset":1 }),
            ]),

      html.Br(),
    
    dbc.Row(
           [
               dbc.Col(html.H4("Total acumulado por entidad"),
                        width=2,lg={'size': 4,  "offset": 1, }),

               dbc.Col(html.H4("Tasa por entidad"),
                       width=1, lg={'size': 3,  "offset": 4, }),                     #size=12
               
            ], justify="end",),
   
    dbc.Row(
        [
            dbc.Col(dcc.Graph(figure=graf_totfem , config= "autosize")),
                   #lg={'size': 5,  "offset": 0,}),
            
            dbc.Col(dcc.Graph(figure= graf_tasafem, config= "autosize")),
                   #lg={'size': 5,  "offset": 1,}),
        ], justify="end", no_gutters=True,),

       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
    
    dbc.Row(
    [
        dbc.Col(html.H2([dbc.Alert("Perfil de Homicidios femeninos", color="primary",# className="alert-link",
                                  className="alert-heading"),
                        ]),width={'size': 10,  "offset":1 })]),
      dbc.Row(
           [
               dbc.Col(html.H5("2015")),
               dbc.Col(html.H5("2016")),
               dbc.Col(html.H5("2017")),
               dbc.Col(html.H5("2018")),
               dbc.Col(html.H5("2019")),
              # dbc.Col(html.H5("2020")),
           ], justify= "start"),
    
   

      
     dbc.Row(
           [
               dbc.Col(html.H1([" ", 
                                dbc.Badge((def15_tot),className="mb-0",color="light",),]),),
               dbc.Col(html.H1([" ", 
                                dbc.Badge((def16_tot),className="mb-0",color="light",),]),),
               dbc.Col(html.H1([" ", 
                                dbc.Badge((def17_tot),className="mb-0",color="light",),]),),
               dbc.Col(html.H1([" ", 
                                dbc.Badge((def18_tot),className="mb-0",color="light",),]),),
               dbc.Col(html.H1([" ", 
                                dbc.Badge((def19_tot),className="mb-0",color="light",),]),),
               #dbc.Col(html.H1([" ", 
               #                 dbc.Badge((def_tot20),className="mb-0",color="light",),]),),
            ]),
    html.Br(),
   



       dbc.Row([
        dbc.Col([dbc.Card(
            dbc.CardBody([
            
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr15_txt),": ", (agr15_val),"%",]),
            html.H6([ (agr215_txt),": ", (agr215_val),"%",]),
            html.Code("Violencia familiar:", className="card-text"), 
            html.H6([ (viofm15_txt),": ", (viofm15_val),"%",]),
            html.Code("Lugar donde ocurrió "),
            html.H6([ (lug115_txt),": ", (lug115_val),"%",]),
            html.H6([ (lug215_txt),": ", (lug215_val),"%",]),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("Entidades con más casos:"),
            html.H6([ (ent115_txt),": ", (ent115_val),"%",]),
            html.H6([ (ent215_txt),": ", (ent215_val),"%",]),
            html.H6([ (ent315_txt),": ", (ent315_val),"%",]),
            html.Code("Área urbana "),
            html.H6([ (aurb15_txt),": ", (aurb15_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la victima ", className="card-title"), 
            html.Hr(),
            html.Code("Grupos de edad con mayor incidencia"),
            html.H6([ (eda115_txt),": ", (eda115_val),"%",]),
            html.H6([ (eda215_txt),": ", (eda215_val),"%",]),
            html.H6([ (eda315_txt),": ", (eda315_val),"%",]),
            html.Code("Estado civil"),
            html.H6("Embarazada:"),
            html.H6([ (emba15_txt),": ", (emba15_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc115_txt),": ", (esc115_val),"%",]),
            html.H6([ (esc215_txt),": ", (esc215_val),"%",]),
            html.H6([ (esc315_txt),": ", (esc315_val),"%",]),

          
        ]
    ),
    style={"width": "10rem"},
),]),
        dbc.Col([dbc.Card(
            dbc.CardBody([
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr16_txt),": ", (agr16_val),"%",]),
            html.H6([ (agr216_txt),": ", (agr216_val),"%",]),
            html.Code("Violencia familiar:", className="card-text"), 
            html.H6([ (viofm16_txt),": ", (viofm16_val),"%",]),
            html.Code("Lugar donde ocurrió "),
            html.H6([ (lug116_txt),": ", (lug116_val),"%",]),
            html.H6([ (lug216_txt),": ", (lug216_val),"%",]),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("Entidades con más casos:"),
            html.H6([ (ent116_txt),": ", (ent116_val),"%",]),
            html.H6([ (ent216_txt),": ", (ent216_val),"%",]),
            html.H6([ (ent316_txt),": ", (ent316_val),"%",]),
            html.Code("Área urbana "),
            html.H6([ (aurb16_txt),": ", (aurb16_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la victima ", className="card-title"), 
            html.Hr(),
            html.Code("Grupos de edad con mayor incidencia"),
            html.H6([ (eda116_txt),": ", (eda116_val),"%",]),
            html.H6([ (eda216_txt),": ", (eda216_val),"%",]),
            html.H6([ (eda316_txt),": ", (eda316_val),"%",]),
            html.Code("Estado civil"),
            html.H6("Embarazada:"),
            html.H6([ (emba16_txt),": ", (emba16_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc116_txt),": ", (esc116_val),"%",]),
            html.H6([ (esc216_txt),": ", (esc216_val),"%",]),
            html.H6([ (esc316_txt),": ", (esc316_val),"%",]),
          
        ]
    ),
    style={"width": "10rem"},
),]),
         dbc.Col([dbc.Card(
            dbc.CardBody([
            
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr17_txt),": ", (agr17_val),"%",]),
            html.H6([ (agr217_txt),": ", (agr217_val),"%",]),
            html.Code("Violencia familiar:", className="card-text"), 
            html.H6([ (viofm17_txt),": ", (viofm17_val),"%",]),
            html.Code("Lugar donde ocurrió "),
            html.H6([ (lug117_txt),": ", (lug117_val),"%",]),
            html.H6([ (lug217_txt),": ", (lug217_val),"%",]),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("Entidades con más casos:"),
            html.H6([ (ent117_txt),": ", (ent117_val),"%",]),
            html.H6([ (ent217_txt),": ", (ent217_val),"%",]),
            html.H6([ (ent317_txt),": ", (ent317_val),"%",]),
            html.Code("Área urbana "),
            html.H6([ (aurb17_txt),": ", (aurb17_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la victima ", className="card-title"), 
            html.Hr(),
            html.Code("Grupos de edad con mayor incidencia"),
            html.H6([ (eda117_txt),": ", (eda117_val),"%",]),
            html.H6([ (eda217_txt),": ", (eda217_val),"%",]),
            html.H6([ (eda317_txt),": ", (eda317_val),"%",]),
            html.Code("Estado civil"),
            html.H6("Embarazada:"),
            html.H6([ (emba17_txt),": ", (emba17_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc117_txt),": ", (esc117_val),"%",]),
            html.H6([ (esc217_txt),": ", (esc217_val),"%",]),
            html.H6([ (esc317_txt),": ", (esc317_val),"%",]),
             
        ]
    ),
    style={"width": "10rem"},
),]),
         dbc.Col([dbc.Card(
            dbc.CardBody([
            
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr18_txt),": ", (agr18_val),"%",]),
            html.H6([ (agr218_txt),": ", (agr218_val),"%",]),
            html.Code("Violencia familiar:", className="card-text"), 
            html.H6([ (viofm18_txt),": ", (viofm18_val),"%",]),
            html.Code("Lugar donde ocurrió "),
            html.H6([ (lug118_txt),": ", (lug118_val),"%",]),
            html.H6([ (lug218_txt),": ", (lug218_val),"%",]),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("Entidades con más casos:"),
            html.H6([ (ent118_txt),": ", (ent118_val),"%",]),
            html.H6([ (ent218_txt),": ", (ent218_val),"%",]),
            html.H6([ (ent318_txt),": ", (ent318_val),"%",]),
            html.Code("Área urbana "),
            html.H6([ (aurb18_txt),": ", (aurb18_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la victima ", className="card-title"), 
            html.Hr(),
            html.Code("Grupos de edad con mayor incidencia"),
            html.H6([ (eda118_txt),": ", (eda118_val),"%",]),
            html.H6([ (eda218_txt),": ", (eda218_val),"%",]),
            html.H6([ (eda318_txt),": ", (eda318_val),"%",]),
            html.Code("Estado civil"),
            html.H6("Embarazada:"),
            html.H6([ (emba18_txt),": ", (emba18_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc118_txt),": ", (esc118_val),"%",]),
            html.H6([ (esc218_txt),": ", (esc218_val),"%",]),
            html.H6([ (esc318_txt),": ", (esc318_val),"%",]),
                        ]
    ),
    style={"width": "10rem"},
),]),
         dbc.Col([dbc.Card(
            dbc.CardBody([
            
            html.H4("Modus Operandi", className="card-title"),
            html.Hr(),
            html.Code("Parentesco con agresor", className="card-text"),
            html.H6([ (agr19_txt),": ", (agr19_val),"%",]),
            html.H6([ (agr219_txt),": ", (agr219_val),"%",]),
            html.Code("Violencia familiar:", className="card-text"), 
            html.H6([ (viofm19_txt)," ", (viofm19_val),"%",]),
            html.Code("Lugar donde ocurrió "),
            html.H6([ (lug119_txt),": ", (lug119_val),"%",]),
            html.H6([ (lug219_txt),": ", (lug219_val),"%",]),
            html.Hr(),
            html.H4("Mayor incidencia", className="card-title"),
            html.Hr(),
            html.Code("Entidades con más casos:"),
            html.H6([ (ent119_txt),": ", (ent119_val),"%",]),
            html.H6([ (ent219_txt),": ", (ent219_val),"%",]),
            html.H6([ (ent319_txt),": ", (ent319_val),"%",]),
            html.Code("Área urbana "),
            html.H6([ (aurb19_txt),": ", (aurb19_val),"%",]),
            html.Hr(),
            html.H4("Perfil de la victima ", className="card-title"), 
            html.Hr(),
            html.Code("Grupos de edad con mayor incidencia"),
            html.H6([ (eda119_txt),": ", (eda119_val),"%",]),
            html.H6([ (eda219_txt),": ", (eda219_val),"%",]),
            html.H6([ (eda319_txt),": ", (eda319_val),"%",]),
            html.Code("Estado civil"),
            html.H6("Embarazada:"),
            html.H6([ (emba19_txt),": ", (emba19_val),"%",]), 
            html.Code("Escolaridad"),
            html.H6([ (esc119_txt),": ", (esc119_val),"%",]),
            html.H6([ (esc219_txt),": ", (esc219_val),"%",]),
            html.H6([ (esc319_txt),": ", (esc319_val),"%",]),
                        ]
    ),
    style={"width": "10rem"},
),]),]),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),

# nuevo
    
    dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H4("Consideraciones generales "),
                html.P(
                    "Los feminicidios son un problema aún irresuelto y son tema central de la " 
                    "agenda de seguridad nacional. Su gravedad se observa "
                    "en los registros anuales y registros mensuales, que se presentan al "
                    "inicio de esta visualización."
                    "Existe mayor atención institucional al fenómeno y fuerte preocupación de la sociedad, " 
                    "lo que se evidencia en el hecho que todos seamos más vigilantes al respecto. "
                    "No obstante, aún hace falta más acción social, sobretodo, más intervención institucional "
                    "para diseñar estrategias efectivas de prevención y promover su denuncia. Es imperante "
                    "acabar con esta violencia de género. "
                    "El presente dashboard (tablero de datos) es un ejercicio institucional con el objeto de "
                    "informar a la sociedad. La información proviene del Secretariado Ejecutivo Nacional del Sistema Nacional de "
                    "Seguridad Pública (SENSNSP). El lector debe ser advertido que el período cubierto "
                    "es del mes de enero de 2015 hasta el mes de enero del 2021. "
                    "Ademas, esta dashboard seguramente puede ser completado con otras fuentes de información "
                    "gubernamental y por toda aquella información proveniente de organizaciones civiles que " 
                    "dan seguimiento al tema. En ningún caso, este contenido representa algún "
                    "posicionamiento partidista, personal o institucional, mucho menos opinión o postura alguna "
                    "sobre el fenómeno. ",
                    className="lead"),
                html.Br(),
                html.H5("Metodología "),
                html.P(
                    "Esta información fue tratada con el lenguaje de programación Python y varias de las librerías "
                    "más comunes (Dash, Choropleth, Pandas, Numpy, Geopandas, etc.), que nos ayudan a automatizar "
                    "la recurrencia (request) a la fuente de información y las operaciones necesarias para creargraficas "
                    "interactivas y mapas presentados. ",
                    className="lead"),
                    
            ], fluid=True,
        )
    ],
    fluid=True,
    ),    
    
        
    
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
    

    dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=4, lg={'size': 1,  "offset": 3, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
        
            ])


app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
