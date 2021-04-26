import plotly.express as px

# couleurs diagrammes circulaire
pieColor = px.colors.sequential.haline_r

# couleurs histogrammes
histColor={'marker_color':'rgb(158,202,225)'}

# couleurs diagrammes en baton
barColor={'marker_color':'rgb(158,202,225)', 'marker_line_color' : 'rgb(8,48,107)',
                  'marker_line_width': 1.3, 'opacity' : 0.6}

# taille des diagramme circulaires
pieSize =  {'width'   : 450,
            'height'  : 300,
            'margin_b': 0}

# taille des histogrammes
histSize = {'width'   : 400,
            'height'  : 400}
