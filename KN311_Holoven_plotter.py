import matplotlib.pyplot as ultraplt
ultraplt.style.use("fivethirtyeight")


# Лінійні графіки любого типу за розподілом по днях
def mega_lin_sca_plot_builder(types_data, data, kind):
    # Наводимо красу
    ultraplt.rcParams["figure.figsize"] = (13, 6)
    lbl = ' / '.join([str(elem) for elem in types_data])  # підпис для осі y
    lay = 0

    # Параметр накладання графіків
    if len(types_data) > 1:
        lay = bool(int(input("Overlay plots?\n0 - No\n1 - Yes\n")))

    for i in types_data:
        if kind == "lin":
            ultraplt.plot(data["Datetime"], data[i], label=i + " distribution")
            ultraplt.xlabel('Datetime')
            ultraplt.legend()

        elif kind == "sca":
            ultraplt.scatter(data["Datetime"], data[i], label=i + " distribution", alpha=0.75)
            ultraplt.xlabel('Datetime')
            ultraplt.legend()

        # Формуємо графіки віносно накладання
        if lay:
            ultraplt.ylabel(lbl)
        elif not lay:
            ultraplt.ylabel(i)
            ultraplt.show()
    if lay:
        ultraplt.show()


# Секторні діаграми не для всіх типів даних
def pie_plot_builder(types_data, data):
    ultraplt.rcParams["figure.figsize"] = (12, 12)
    for i in types_data:
        cnt = data[i].value_counts()
        ultraplt.pie(cnt, autopct='%1.1f%%', startangle=0)
        ultraplt.legend(labels=cnt.index)
        ultraplt.title(i)
        ultraplt.show()


# Гістограми без накладання відносно кількості даних
def his_plot_builder(types_data, data):
    ultraplt.rcParams["figure.figsize"] = (12, 6)
    for i in types_data:
        ultraplt.hist(data[i], label=i + " distribution", rwidth=0.9)
        ultraplt.xlabel(i)
        ultraplt.ylabel("Amount of values")
        ultraplt.legend()
        ultraplt.show()


# Розподіл по будь-яки даних, поки що тільки з точковою діаграмою
def custom_plot_builder(data):
    ultraplt.rcParams["figure.figsize"] = (13, 6)
    cnt = int(input("How many plots? "))
    lay = 0
    if cnt > 1:
        lay = bool(int(input("Overlay plots?\n0 - No\n1 - Yes\n")))
    for i in range(cnt):
        x = input("Choose data for x: ")
        y = input("Choose data for y: ")
        ultraplt.scatter(data[x], data[y], label=x + " and " + y + " distribution")
        ultraplt.xlabel(x)
        ultraplt.xlabel(y)
        ultraplt.legend()
        if not lay:
            ultraplt.show()
    if lay:
        ultraplt.show()


# Запитуємо у користувача влстивості графіків
def plot_options(plot_data):
    print("Choose type of plot:")
    option = int(input("1 - Linear\n2 - Pie\n3 - Scatter\n4 - Histogram\n5 - Custom\n"))
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

    if option == 5:
        custom_plot_builder(plot_data)
