# Programming Assignment 3
NAME : Deirojel Martin M. Garcia

SECTION : 2ECE-A

SUBMITTED : September 15, 2024

.ipynb file is uploaded just incase .py file would not load

***

## Problem 1

Using knowledge obtained from the experiment and demonstrations:

  - Load the corresponding .csv file into a data frame named cars using pandas

  - Display the first five and last five rows of the resulting cars.

___

In this problem we are required to load a specific .csv file and print its first 5 rows and last 5 rows. 

We start with importing Pandas for data analysis

``` python
import pandas as pd
```

Next, we need to import the .csv file to be analyzed

``` python
cars = pd.read_csv("cars.csv")
```

Since we need to print the first five rows, we can use the function pd.head()

``` python
cars.head()
```

Same goes with the last five rows, we can use the function pd.tail()

``` python
cars.tail()
```

***

## Problem 2

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.
  - Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
  - Display the row that contains the ‘Model’ of ‘Mazda RX4’.
  - How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
  - Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
  Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

In this problem, we have to perform multiple tasks on the previous .csv given. 

___

First we need to import Pandas for data analysis

``` python
import pandas as pd
```

For question 1, we need print the first five odd numbered rows (1, 3, 5, 7, 9). We can use the function pd.iloc[] to use indeces to find and print.
``` python
cars.iloc[[1,3,5,7,9],:]
```
For question 2, we need to print display the row first five rows then its odd numbered columns. We can use pd.iloc[] again for this. :5 is for idicating that we need to use row 0 up to 4. For odd numbers I use 1::2 so we start at one and apply an incriment of 2.
``` python
cars.iloc[:5,1::2]
```
For question 3, we need to find how many cyl the car "Camaro Z28" has. With this we can use the function pd.loc[]. 

cars['Model']=='Camaro Z28' is where code looks for the row where 'Camaro Z28' is in the column named 'Model'. 

['Model','cyl'] specifies which columns to be printed.
``` python
cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
``` 
For question 4, we need to print how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']) Here we search for the rows that have the car models in the column "model'. 

['Model','cyl','gear'] Here we declare the columns to be printed 

``` python
cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']), ['Model','cyl','gear']]
```
[Changes within repository](https://github.com/DeiGarsya/PA-3/commits/main/)
