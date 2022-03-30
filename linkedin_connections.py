import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Connections.csv', skiprows=2)

#stores all company names
companyData = df.head(20)
#print(companyData)

#Count amount of occurence of each Company
#print(companyData.nunique['Company'](axis=2, dropna=True))

companyOccurence = pd.value_counts(companyData.Company)
companyName = pd.value_counts(companyData.Company).index

#gets company occurence values
for test1 in companyOccurence:
    print(test1)
pass

#gets company names
for i in companyName:
    print(i)
pass

#scatter graph
fig = go.Figure(data=go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))

fig.show()