import pandas as pd
import plotly.express as px
df = pd.read_csv("corona.csv")

fig = px.line(df, x="date", y="cases", color="country")
fig.show()