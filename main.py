import pandas as pd
import numpy as np
import plotter as plt


# Приводимо дату в нормальний формат
def date_fix(x):
    return str(x.replace(".", " ") + " 2019")


# Приводимо відсотки в дроби
def rate_to_float(x):
    return float(x.strip("%")) / 100


# Замінюємо кому на крапку для float
def comma_to_float(x):
    return(float(x.replace(",", ".")))


# Приводимо швидкість в число
def speed_to_int(x):
    return int(x.strip(" mph"))


# Приводимо дані до int
def to_int(x):
    return int(x)


# Зчитуємо дані в dataframe з csv та форматуємо їх
data = pd.read_csv('values.csv', sep = ';',
                converters = {
                'day/month': date_fix,
                'Temperature': to_int,
                'Dew Point': to_int,
                'Humidity': rate_to_float,
                'Pressure': comma_to_float,
                'Wind Speed': speed_to_int,
                'Wind Gust': speed_to_int,
                'Precip.': to_int,
                'Precip Accum': to_int,
                }, parse_dates = True)

# Приводимо Time в 24-формат
data['Time'] = pd.to_datetime(data['Time']).dt.strftime('%H:%M')

# Якщо є пусті стовбці, то видаляємо
data = data.loc[:, (data != 0).any(axis = 0)]

# Створюємо об'єднанням нове поле datetime для зручності
data['Datetime'] = pd.to_datetime(data['day/month'] + " " + data['Time'])
data['day/month'] = pd.to_datetime(data['day/month'])

# Робимо day/month індексним стовбцем
data = data.set_index(["day/month"])

# print(data)
plt.plot_options(data)
