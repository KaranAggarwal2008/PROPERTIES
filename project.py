import pandas as pd
import plotly.express as px
dataFrames = pd.read_csv("data.csv")
framesInGraph = px.scatter(dataFrames, x="City", y="Price_range_per_sqft",color="Price_rise",
                   size_max=60)
framesInGraph.show()