import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = (13, 6)

color_maps = {"active_confirm": "Reds", "new_death": "Greys", "new_confirm": "Oranges", "new_susp": "Blues", "new_recover": "Greens"}


# Лінійний та точковий графік
def lin_sca_plot_builder(data, kind, area):
    # Вибираємо потрібні дані
    types_data = list(map(str, input(
        "new_susp / new_confirm / active_confirm "
        "/ new_death / new_recover\n").split(" / ")))

    lay = 0

    # Параметр накладання графіків
    if len(types_data) > 1:
        lay = bool(int(input("Overlay plots?\n0 - No\n1 - Yes\n")))

    for i in types_data:
        if kind == "lin":
            plt.plot(data.index, data[i], label=i)

        elif kind == "sca":
            plt.scatter(data.index, data[i], label=i, alpha=0.75)

        plt.xlabel('Date')
        plt.ylabel("People")
        plt.legend()
        plt.title(area)
        # Формуємо графіки віносно накладання
        if not lay:
            plt.show()
    if lay:
        plt.show()


# Графіки по мапі України
def map_plot_builder(map_df):
    # Вибираємо потрібні дані
    types_data = list(map(str, input(
        "new_susp / new_confirm / active_confirm "
        "/ new_death / new_recover\n").split(" / ")))

    for i in types_data:
        map_df.plot(cmap=color_maps[i], column=i, edgecolor="0.5", figsize=(12.0, 8.0),
                    missing_kwds={"color": "lightgrey", "hatch": "//"})
        v_min, v_max = map_df[i].min(), map_df[i].max()
        sm = plt.cm.ScalarMappable(cmap=color_maps[i],
                                   norm=plt.Normalize(vmin=v_min, vmax=v_max))
        plt.colorbar(sm)
        plt.title("Ukraine COVID-19 " + i)
        plt.axis("off")
    plt.show()


def compare_plot(data):
    print(data)
    types_area = list(map(str, input("Enter areas, please: ").split(" / ")))
    n = len(types_area)
    area_list = []
    for i in range(n):
        area_list.append(data[data["registration_area"] == types_area[i]])
    print(area_list)
    # Львівська / Київська
    prop = input("Enter property, please: ")

    ax = area_list[0].plot(x="zvit_date", y=prop, label=types_area[0])

    for i in range(1, n):
        area_list[i].plot(x="zvit_date", y=prop, label=types_area[i], ax=ax)
    plt.xlabel('Date')
    plt.legend()
    plt.ylabel(prop)
    plt.show()


# Запитуємо у користувача влстивості графіків
def plot_options(plot_compare, plot_data, plot_map, area):
    print(area)
    print("Choose type of plot:")
    option = int(input("1 - Linear\n2 - Scatter\n3 - Map\n4 - Compare\n"))
    if option == 1:
        kind = "lin"
        lin_sca_plot_builder(plot_data, kind, area)

    if option == 2:
        kind = "sca"
        lin_sca_plot_builder(plot_data, kind, area)

    if option == 3:
        map_plot_builder(plot_map)

    if option == 4:
        compare_plot(plot_compare)