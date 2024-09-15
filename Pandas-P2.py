import pandas as pd
cars = pd.read_csv("cars.csv")
cars.iloc[[1,3,5,7,9],:]
cars.loc[cars['Model']=='Mazda RX4']
cars.loc[cars['Model']=='Camaro Z28',['cyl']]
cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic'])]