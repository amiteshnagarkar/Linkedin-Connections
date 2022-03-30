import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Connections.csv', skiprows=2)

#stores all company names
companyData = df.head(100)
#print(companyData)

#Count amount of occurence of each Company
#print(companyData.nunique['Company'](axis=2, dropna=True))

companyOccurence = pd.value_counts(df.Company)
companyName = pd.value_counts(df.Company).index

#gets company occurence values
size2 = []
for test1 in companyOccurence:
    size2.append(test1)
    #print(test1)
pass

#gets company names
size3 = []
for i in companyName:
    size3.append(i)
    #print(i)
pass


#scatter graph
fig = go.Figure(data=go.Scatter(
    x=size3,
    y=size2,
    mode='markers',
    marker=dict(size=size2,
                color= '#0b0040', opacity=1)
)     
)

fig.update_traces(marker=dict(
                              line=dict(width=10,
                                        color='#0b0040')),
                  selector=dict(mode='markers'))

fig.update_xaxes(ticklabelposition="inside top", title='Company Names', automargin=True)
fig.update_yaxes(ticklabelposition="inside top", title='Amount of Connections', automargin=True)

fig.update_layout(
    title={
        'text': "Cool Graph",
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})


#fig.show()
fig.write_html('plot.html' , auto_open=True)