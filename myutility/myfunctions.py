import pandas as pd
import numpy as np
import plotly.graph_objects as go
import ipywidgets as ipw
import plotly.express as px

histSize = {'width' : 370, 'height' : 370}

## différence en heures entre deux dates
def hour_delta(x, date1, date2): return (x[date1] - x[date2]) / np.timedelta64(1, 'h')

# différence en jours entre deux dates
def day_delta(x, date1, date2): return (x[date1] - x[date2]) / np.timedelta64(1, 'D')

def completeness(data, dtype=True):
    '''
    affiche les informations sur les variables du dataframe :
    complétude, cardinalité, type de données
    '''

    ## complétude des variables 
    count = data.count().rename('count')
    
    ## cardinalité des variables
    nunique = data.nunique().rename('nunique')
    
    ## type des variables
    dtypes = data.dtypes.rename('dtype')
    
    ## concatènation des séries
    out = pd.concat([count, nunique], axis=1)
    if dtype:
        out = pd.concat([out, dtypes], axis=1)
    return out

def lastOrder(dftmp):
    '''
    retourne seulement la dernière commande 
    pour chaque client
    '''
    
    ## regroupement par client
    cust_group = dftmp.groupby('customer_unique_id')
    
    ## index : dernière commande par client
    idx = cust_group['order_purchase_timestamp'].transform(max) == dftmp['order_purchase_timestamp']
    
    ## dataframe : dernière commande client
    dftmp_last = dftmp.loc[idx]
    
    ## suppression des doublons de clients
    dftmp_last = dftmp_last.drop_duplicates(subset='customer_unique_id')
    
    return dftmp_last


## fonction pour aligner plusieurs figures côte à côte
def hboxing(figlist, nb_h = 3):
    fig_out = []
    ## converti la list de figure en list de widgets figures
    for elt in figlist:
        fig_out.append(go.FigureWidget(elt))
        
    
    ## liste des hbox
    hboxlist = []
    
    ## créer une hbox toutes les nb_h figures
    for elt in range(0, len(fig_out), nb_h):
        tmpHBox = ipw.HBox(fig_out[elt:elt+nb_h])
        hboxlist.append(tmpHBox)
        
    
    return ipw.VBox(hboxlist)

def getFigR(df):
    fig = px.histogram(df, x='recency')
    fig.update_layout(xaxis_title_text='Recency (D)',
                      yaxis_title_text='',
                      **histSize)
    return fig

def getFigF(df):
    fig = px.histogram(df, x='n_orders', range_x=[0.5,4.5])
    fig.update_layout(xaxis_nticks=5,
                       xaxis_title_text='Frequency',
                       yaxis_title_text='',
                       title = 'Nb of Customers',
                        **histSize)
    return fig

def getFigM(df):
    fig = px.histogram(df, x='price_sum')
    fig.update_layout(xaxis_title_text='Monetary Value (Real)',
                   yaxis_title_text='',
                   **histSize,
                  )
    return fig



def firstOrder(dftmp):
    '''
    retourne seulement la première commande 
    pour chaque client
    '''
    
    # regroupement par client
    cust_group = dftmp.groupby('customer_unique_id')
    
    # index : dernière commande par client
    idx = cust_group['order_purchase_timestamp'].transform(min) == dftmp['order_purchase_timestamp']
    
    # dataframe : dernière commande client
    dftmp_first = dftmp.loc[idx]
    
    # suppression des doublons de clients
    dftmp_first = dftmp_first.drop_duplicates(subset='customer_unique_id')
    
    return dftmp_first


def dropTimeDuplicate(dftmp):
    '''
    supprime les commandes d'un même client, 
    effectuées au même moment (seconde près)
    '''
    # doublons même client, plusieurs commandes même temps
    subset_duplicate = ['customer_unique_id','order_purchase_timestamp']
    
    # classe les commandes selon client, temps d'achat
    sortedDf = dftmp.sort_values(by=subset_duplicate)
    
    # supprime les commandes : même client, même date seconde près
    sortedDf = sortedDf.drop_duplicates(subset=subset_duplicate, keep=False)
    
    return sortedDf


def firstQuantile(series, quantile):
    '''
    sélectionne les individues de la series 
    contenue dans le premier quantile 
    '''
    
    # index 95% des clients qui ont le moins dépensé
    cut = series.quantile(quantile)

    # sélection des 95% les moins dépensiés
    series = series[series < cut]
    
    return series

def dfFirstLastOrder(dftmp):
    '''
    retourne un dataframe avec 2 colonnes :
    temps 1ère commande ::: temps dernière commande
    '''
    
    # liste dates de première commande 
    first = dftmp.groupby('customer_unique_id')['order_purchase_timestamp'].min()
    first.rename('first_order', inplace=True)
    
    # liste dates de deuxième commande 
    last = dftmp.groupby('customer_unique_id')['order_purchase_timestamp'].max()
    last.rename('second_order', inplace=True)
    
    # concaténation 1er et 2nd commande
    output = pd.concat([first, last], axis=1)
    
    # T2 - T1 (en heure)
    order_timeFreqH = output.apply(lambda x : hour_delta(x, 'second_order',
                                     'first_order') , axis=1)
    
    # T2 - T1 (en jours)
    order_timeFreqD = output.apply(lambda x : day_delta(x, 'second_order',
                                     'first_order') , axis=1)
    
    # ajout des 'T2 - T1' au dataframe
    output['order_freq_H'] = order_timeFreqH
    output['order_freq_D'] = order_timeFreqD
    
    return output
