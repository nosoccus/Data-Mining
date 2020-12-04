import pandas as pd
import geopandas as gpd
import openpyxl as pyxl
import plotter as plt


def group_date(df):
    df = df.set_index("zvit_date")
    # Згрупувати дані по ознаці “однакова дата”
    df_date = df.groupby(["zvit_date"]).sum()
    print("Grouped by date")
    print(df_date)
    return df_date


def group_area(df):
    # Вибрати дані по одній з областей України
    area = input("Choose area: ")
    df_area = df.loc[df["registration_area"] == area]
    new_df = group_date(df_area)
    print(f"Grouped by {area} area")
    print(new_df)
    return new_df, area


def merge_data(df_gpd, df_data, sh_option):
    if sh_option == 1:
        df_gpd = df_gpd.replace({"Chernihiv": "Чернігівська",
                           "Donets'k": "Донецька",
                           "Dnipropetrovs'k": "Дніпропетровська",
                           "Luhans'k": "Луганська",
                           "L'viv": "Львівська",
                           "Ivano-Frankivs'k": "Івано-Франківська",
                           "Odessa": "Одеська",
                           "Poltava": "Полтавська",
                           "Kiev": "Київська",
                           "Chernivtsi": "Чернівецька",
                           "Kharkiv": "Харківська",
                           "Kirovohrad": "Кіровоградська",
                           "Volyn": "Волинська",
                           "Rivne": "Рівненська",
                           "Transcarpathia": "Закарпатська",
                           "Zhytomyr": "Житомирська",
                           "Vinnytsya": "Вінницька",
                           "Mykolayiv": "Миколаївська",
                           "Kiev City": "м. Київ",
                           "Ternopil'": "Тернопільська",
                           "Cherkasy": "Черкаська",
                           "Kherson": "Херсонська",
                           "Khmel'nyts'kyy": "Хмельницька",
                           "Sumy": "Сумська",
                           "Zaporizhzhya": "Запорізька"})
        left = df_gpd.rename(columns={"NAME_1": "registration_area"})

    if sh_option == 2:
        df_data = df_data.replace({"м. Київ": "Київська"})
        left = df_gpd.rename(columns={"ADM1_UA": "registration_area"})

    df_data = df_data.groupby(["zvit_date", "registration_area"]).sum().reset_index()
    right = df_data.groupby("registration_area").sum()
    res = left.merge(right, how="left", on="registration_area")
    return res


def to_excel(data):
    name = input("Enter a filename:")
    area_stats = data.groupby("registration_area").sum()
    unique = data["registration_area"].unique()
    with pd.ExcelWriter(name) as writer:
        area_stats.to_excel(writer, sheet_name="Area_statistics")
        for area in unique:
            curr = data[data["registration_area"] == area].describe()
            curr.to_excel(writer, sheet_name=area)
    return name


if __name__ == '__main__':
    # Знімаємо обмеження по кількості стовбців
    pd.set_option('display.max_columns', None)

    # Парсимо CSV
    url = "https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_area_type_hosp_dynamics.csv"
    df_data = pd.read_csv(url, encoding='utf-8', parse_dates=True)
    df_compare = df_data.groupby(["zvit_date", "registration_area"]).sum().reset_index()
    # Зчитуємо Shapefile
    sh_option = int(input("Choose shapefile:\n1 - with Kyiv\n2 - only areas\n"))
    if sh_option == 1:
        df_gpd = gpd.read_file("zip://UKR_adm.zip!UKR_adm1.shp", encoding='utf-8')

    if sh_option == 2:
        df_gpd = gpd.read_file('zip://ukr_admbnda_adm1_q2_sspe_20171221.zip!ukr_admbnda_adm1_q2_sspe_20171221.shp', encoding='utf-8')

    while True:
        print("Main menu:")
        option = int(input("1 - group by date\n2 - group by area\n"
                           "3 - plot module\n4 - export to excel\n"))

        if option == 1:
            # Викликаємо функцію для групування даних лише по даті
            df_grouped = group_date(df_data)
            area = "Україна"

        if option == 2:
            # Викликаємо функцію для групування даних по даті і області
            df_grouped, area = group_area(df_data)
            area += " область"

        if option == 3:
            df_merged = merge_data(df_gpd, df_data, sh_option)
            # Викликаємо модуль для побудови графіків
            try:
                plt.plot_options(df_compare, df_grouped, df_merged, area)
            except NameError:
                raise Exception("Firstly group the data")

        if option == 4:
            print("Dataframe is written to", to_excel(df_data))
