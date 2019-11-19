import pandas as pd

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# # Import the cars.csv data: cars
# cars = pd.read_csv('cars.csv')
#
# # Print out cars
# print(cars)

# cars = pd.read_csv('cars.csv', index_col = 0)
#
# # Print out country column as Pandas Series
# print(cars['cars_per_cap'])
#
# # Print out country column as Pandas DataFrame
# print(cars[['cars_per_cap']])
#
# # Print out DataFrame with country and drives_right columns
# print(cars[['cars_per_cap', 'country']])

# cars = pd.read_csv('cars.csv', index_col = 0)
#
# # Print out first 4 observations
# print(cars[0:4])
#
# # Print out fifth, sixth, and seventh observation
# print(cars[4:6])

# cars = pd.read_csv('cars.csv', index_col = 0)
#
# # Print out observation for Japan
# print(cars.iloc[2])
#
# # Print out observations for Australia and Egypt
# print(cars.loc[['AUS', 'EG']])