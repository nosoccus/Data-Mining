import pandas as superpd
import KN311_Holoven_plotter as megaplt


# Приводимо дату в нормальний формат
def date_fix(x):
    return str(x.replace(".", " ") + " 2019")


# Приводимо відсотки в дроби
def rate_to_float(x):
    return float(x.strip("%")) / 100


# Замінюємо кому на крапку для float
def comma_to_float(x):
    return float(x.replace(",", "."))


# Приводимо швидкість в число
def speed_to_int(x):
    return int(x.strip(" mph"))


# Приводимо дані до int
def to_int(x):
    return int(x)


# Знімаємо обмеження по кількості стовбців
superpd.set_option('display.max_columns', None)

# Зчитуємо дані в датафрейм з csv та форматуємо їх
df_data = superpd.read_csv('values.csv', sep=';',
                           converters={
                               'day/month': date_fix,
                               'Temperature': to_int,
                               'Dew Point': to_int,
                               'Humidity': rate_to_float,
                               'Pressure': comma_to_float,
                               'Wind Speed': speed_to_int,
                               'Wind Gust': speed_to_int,
                               'Precip.': to_int,
                               'Precip Accum': to_int,
                           }, parse_dates=True)

# Приводимо Time в 24-формат
df_data['Time'] = superpd.to_datetime(df_data['Time']).dt.strftime('%H:%M')

# Якщо є пусті стовбці, то видаляємо
df_data = df_data.loc[:, (df_data != 0).any(axis=0)]

# Створюємо об'єднанням нове поле datetime для зручності
df_data['Datetime'] = superpd.to_datetime(df_data['day/month'] + " " + df_data['Time'])
df_data['day/month'] = superpd.to_datetime(df_data['day/month'])

# Робимо day/month індексним стовбцем
df_data = df_data.set_index(["day/month"])

# print(df_data)

# Викликаємо модуль для побудови класів
megaplt.plot_options(df_data)
