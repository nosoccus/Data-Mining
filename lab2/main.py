import pandas as pd
import plotter as plt


if __name__ == '__main__':
    # Знімаємо обмеження по кількості стовбців
    pd.set_option('display.max_columns', None)

    # Парсимо CSV
    url = "https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_area_type_hosp_dynamics.csv"
    df = pd.read_csv(url, encoding='utf-8', parse_dates=True, index_col="zvit_date")
    print(df)
    print(df.info(), "\n")

    # Вибрати дані по одній з областей України
    area = input("Виберіть область: ")
    df_lviv = df.loc[df["registration_area"] == area]

    # Згрупувати дані по ознаці “однакова дата”
    df_date = df_lviv.groupby(["zvit_date"]).sum()
    print(df_date)
    print(df_date.info(), "\n")
    # Викликаємо модуль для побудови графіків
    plt.plot_options(df_date)

