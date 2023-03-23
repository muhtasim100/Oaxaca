import json
import pandas as pd
import plotly
import plotly.express as px

from . import db

color_scheme = ["#4BA6B9", "#FFFFFF", "#B3B3B3", "#6F6F6F", "#3B3636", "#464646"]


def dishes_graph():
    result = db.session.execute("SELECT FoodItem.FoodName, SUM(OrderItem.Quantity) " +
"FROM OrderItem INNER JOIN FoodItem on FoodItem.FoodID = OrderItem.FoodID " +
"GROUP BY FoodItem.FoodName;")
    
    food_names = []
    food_quantities = []
    for row in result:
        food_names.append(row[0])
        food_quantities.append(row[1])

    df = pd.DataFrame({
      'Name': food_names,
      'Quantity': food_quantities
    })


    fig = px.pie(df, values="Quantity", names="Name", color_discrete_sequence=color_scheme)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family='Sans-Regular, sans-serif',
            size=24,
            color='#000000'
        ),
        legend=dict(orientation="h",
                    yanchor="bottom",
                    y=-0.6,
                    xanchor="center",
                    x=0.5),
        width=500,
        height=400,
        autosize=True
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
