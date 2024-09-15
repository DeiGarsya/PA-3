import pandas as pd
cars = pd.read_csv("cars.csv")
cars.iloc[:5,1::2]
cars.loc[cars['Model']=='Mazda RX4']
cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']), ['Model','cyl','gear']]
