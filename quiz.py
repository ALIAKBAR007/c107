from statistics import mean
import pandas as pd
import plotly.graph_objects as no
file = pd.read_csv("c107.csv")
studentData= file.loc[file['student_id']=='TRL_987']
analysis=studentData.groupby("level")["attempt"].mean()
fig= no.Figure(no.Bar(
    x = analysis,
    y = ["level 1","level 2","level 3","level 4",],
    orientation='h'
))
fig.show()
print(analysis)