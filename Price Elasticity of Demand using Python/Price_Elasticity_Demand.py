import pandas as pd 

data = pd.DataFrame(
    {
    "Demand": [20,30,40,50,60],
    "Price": [2000,1500,1000,500,100]
    }
)



data["% Change in Demand"] = data["Demand"].pct_change()
data["% Change in Price"] = data["Price"].pct_change()


data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]

print(data)

