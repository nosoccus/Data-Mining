import matplotlib.pyplot as plt


# Лінійні графіки любого типу за розподілом по днях
def lin_plot_builder(types_data, data, lay):
    # Наводимо красу
    plt.rcParams["figure.figsize"] = (10, 5)
    lbl = ' and '.join([str(elem) for elem in types_data])  # підпис для осі y

    for i in types_data:
        plt.plot(data["Datetime"], data[i], label=i + " distribution")
        plt.xlabel('Datetime')
        plt.legend()

        if lay:
            plt.ylabel(lbl)
        elif not lay:
            plt.ylabel(i)
            plt.show()
    if lay:
        plt.show()


# Секторні діаграми не для всіх типів даних
def pie_plot_builder(types_data, data):
    plt.rcParams["figure.figsize"] = (8, 8)
    for i in types_data:
        cnt = data[i].value_counts()
        plt.pie(cnt, autopct='%1.1f%%', startangle=0)
        plt.legend(labels=cnt.index)
        plt.title(i)
        plt.show()


# Запитуємо у користувача влстивості графіків
def plot_options(plot_data):
    print("Choose type of plot:")
    option = int(input("1 - Simple\n2 - Pie\n3 - Scatter\n"))
    lay = 0  # опція накладання графіків
    if option == 1:
        print("Choose the necessary data for plots:")
        types_data = list(map(str, input(
            "Temperature / Dew Point / Humidity / "
            "Wind Speed / Wind Gust / Pressure - distribution by datetime\n").split(" and ")))
        if len(types_data) > 1:
            lay = bool(int(input("Overlay plots?\n0 - No\n1 - Yes\n")))
        lin_plot_builder(types_data, plot_data, lay)

    if option == 2:
        types_data = list(map(str, input(
            "Temperature / Dew Point / Humidity / Wind / "
            "Wind Speed / Wind Gust / Pressure / Condition\n").split(" and ")))
        pie_plot_builder(types_data, plot_data)
