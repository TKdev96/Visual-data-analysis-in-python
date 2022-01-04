import csv

import matplotlib.pyplot as plt
"""Visual data analysis - Comparing the highest and lowest daily temperatures in Sitka and Death Valley"""


"""Import of modules: csv, matplotlib and datetime"""

from datetime import datetime

"""Assignment a csv file name to a variable"""
filename = 'sitka_weather_2014.csv' 

"""Opening a file as an alias"""
with open(filename) as f_obj:
    """Assignment a method csv_reader to variable and passed f_obj"""
    reader = csv.reader(f_obj)

    """Reading headers using the next method"""
    header_row = next(reader)
    """Create empty lists"""
    highs = []
    lows = []
    dates = []

    """Iteration in reader for date, high and low data"""
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d") #using datetime and strptime method to formatted date
            high = (int(row[1]))
            low = (int(row[3]))
        except ValueError: #In case there is no data, we return an error
            print(date, 'Brak danych.')
        else:
            dates.append(date)
            highs.append(high)    
            lows.append(low)

filename_2 = 'death_valley_2014.csv'
with open(filename_2) as f_obj_2:
    reader_2 = csv.reader(f_obj_2)
    header_row_2 = next(reader_2)

    highs_2 = []
    lows_2 = []
    dates_2 = []

    for row in reader_2:
        try:
            date_2 = datetime.strptime(row[0], "%Y-%m-%d")
            high_2 = (int(row[1]))
            low_2 = (int(row[3]))
        except ValueError:
            print(date, 'Brak danych.')
        else:
            dates_2.append(date_2)
            highs_2.append(high_2)    
            lows_2.append(low_2)



    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.6)
    plt.plot(dates, lows, c='blue', alpha=0.6)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.plot(dates_2, highs_2, c='green')
    plt.plot(dates_2, lows_2, c='yellow')
    plt.fill_between(dates_2, highs_2, lows_2, facecolor='green', alpha=0.1)
    plt.title("Najwyższa i najniższa temperatura dnia - 2014", fontsize=20)
    fig.autofmt_xdate()
    plt.ylabel('Temperatura (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()