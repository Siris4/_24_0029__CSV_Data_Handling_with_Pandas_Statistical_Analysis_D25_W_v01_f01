# TODO: Below shows all the code required just to do (import pandas\n pandas.read_csv("weather_data.csv"))         with Pandas:

#################################
# import csv

# with open ("C:/Users/guber/Desktop/CoDex - Code Index - GitHub for HDD/Python/100 Days of Code - Projects Code - in PyCharm/__Learning Only Files - Only Mini-Projects here__/Day 25 Start - CSV Files and Pandas/weather_data.csv") as weather_data:
    # list_weather_data = weather_data.readlines()
    # list_weather_data = csv.reader(weather_data)
    # print(f"list weather data: {list_weather_data}")
    # list weather data: <_csv.reader object at 0x0000016292285340>
    #this Object can be Looped through!

    # tempuratures = []  #integers only, only temps go into this list

    # next(list_weather_data)   # Skip the header row

    # for row in list_weather_data:
        # print(row)
        # if row[1].isdigit():
        #     temp = int(row[1])
        #     tempuratures.append(temp)
        # if row[1] != "temp":
        #     tempuratures.append(int(row[1]))

    # print(tempuratures)

##################################

import pandas

weather_data_file = pandas.read_csv("weather_data.csv")
print(weather_data_file)
'''
   day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny

Process finished with exit code 0
'''

print(type(weather_data_file))
#<class 'pandas.core.frame.DataFrame'>

print(weather_data_file["temp"])   #if you want to get ahold of a certain, then you call it by the header name "temp" for column 2, as shown here:
print(type(weather_data_file["temp"]))
#<class 'pandas.core.series.Series'>
'''
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
'''

weather_data_dictionary = weather_data_file.to_dict()    #converting DataFrame to a dictionary
print(weather_data_dictionary)
#{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

weather_data_list = weather_data_file["temp"].to_list()
print(weather_data_list)
# [12, 14, 15, 14, 21, 22, 24]
print(len(weather_data_list))


# to get average of a list
def average_value_of_data_series_list():
    return sum(weather_data_list) / len(weather_data_list)

print(average_value_of_data_series_list())

mean_temp = weather_data_file["temp"].mean()
print(f"Pandas Series.mean() function: {mean_temp}")

max_temp = weather_data_file["temp"].max()
print(max_temp)

print(weather_data_file["condition"])

print(weather_data_file.condition)

print(weather_data_file[weather_data_file.day == "Monday"])
#      day  temp condition
# 0  Monday    12     Sunny


print(weather_data_file.day == "Monday")   #where in that file, in the day column, is there a Monday?
'''
0     True
1    False
2    False
3    False
4    False
5    False
6    False
'''


print(weather_data_file[weather_data_file.day == "Monday"])
print(weather_data_file[weather_data_file.temp == max(weather_data_file.temp)])



