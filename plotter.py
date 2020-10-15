import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")


# Лінійні графіки любого типу за розподілом по днях
def mega_lin_sca_plot_builder(types_data, data, kind):
    # Наводимо красу
    plt.rcParams["figure.figsize"] = (13, 6)
    lbl = ' / '.join([str(elem) for elem in types_data])  # підпис для осі y
    lay = 0

    # Параметр накладання графіків
    if len(types_data) > 1:
        lay = bool(int(input("Overlay plots?\n0 - No\n1 - Yes\n")))

    for i in types_data:
        if kind == "lin":
            plt.plot(data["Datetime"], data[i], label=i + " distribution")
            plt.xlabel('Datetime')
            plt.legend()

        elif kind == "sca":
            plt.scatter(data["Datetime"], data[i], label=i + " distribution", alpha=0.75)
            plt.xlabel('Datetime')
            plt.legend()

        # Формуємо графіки віносно накладання
        if lay:
            plt.ylabel(lbl)
        elif not lay:
            plt.ylabel(i)
            plt.show()
    if lay:
        plt.show()


# Секторні діаграми не для всіх типів даних
def pie_plot_builder(types_data, data):
    plt.rcParams["figure.figsize"] = (12, 12)
    for i in types_data:
        cnt = data[i].value_counts()
        plt.pie(cnt, autopct='%1.1f%%', startangle=0)
        plt.legend(labels=cnt.index)
        plt.title(i)
        plt.show()


# Гістограми без накладання відносно кількості даних
def his_plot_builder(types_data, data):
    plt.rcParams["figure.figsize"] = (12, 6)
    for i in types_data:
        plt.hist(data[i], label=i + " distribution", rwidth=0.9)
        plt.xlabel(i)
        plt.ylabel("Amount of values")
        plt.legend()
        plt.show()


# Запитуємо у користувача влстивості графіків
def plot_options(plot_data):
    print("Choose type of plot:")
    option = int(input("1 - Linear\n2 - Pie\n3 - Scatter\n4 - Histogram\n"))
    print("Choose the necessary data for plots:")
    if option == 1:
        kind = "lin"
        types_data = list(map(str, input(
            "Temperature / Dew Point / Humidity / "
            "Wind Speed / Wind Gust / Pressure - distribution by datetime\n").split(" / ")))
        mega_lin_sca_plot_builder(types_data, plot_data, kind)

    if option == 2:
        types_data = list(map(str, input(
            "Temperature / Dew Point / Humidity / Wind / "
            "Wind Speed / Wind Gust / Pressure / Condition\n").split(" / ")))
        pie_plot_builder(types_data, plot_data)

    if option == 3:
        kind = "sca"
        types_data = list(map(str, input(
            "Temperature / Dew Point / Humidity / "
            "Wind Speed / Wind Gust / Pressure - distribution by datetime\n").split(" / ")))
        mega_lin_sca_plot_builder(types_data, plot_data, kind)

    if option == 4:
        types_data = list(map(str, input(
            "Temperature / Dew Point / Humidity / "
            "Wind Speed / Wind Gust / Pressure - distribution by datetime\n").split(" / ")))
        his_plot_builder(types_data, plot_data)
