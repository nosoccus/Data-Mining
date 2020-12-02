import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")


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
            plt.plot(data.index, data[i].cumsum(), label=i + " distribution")
            plt.xlabel('zvit_date')
            plt.legend()

        elif kind == "sca":
            plt.scatter(data.index, data[i], label=i + " distribution", alpha=0.75)
            plt.xlabel('zvit_date')
            plt.legend()

        # Формуємо графіки віносно накладання
        if lay:
            plt.ylabel(lbl)
        elif not lay:
            plt.ylabel(i)
            plt.show()
    if lay:
        plt.show()


def custom_plot_builder(data):
    plt.rcParams["figure.figsize"] = (13, 6)
    cnt = int(input("How many plots? "))
    lay = 0
    if cnt > 1:
        lay = bool(int(input("Overlay plots?\n0 - No\n1 - Yes\n")))
    for i in range(cnt):
        x = input("Choose data for x: ")
        y = input("Choose data for y: ")
        plt.scatter(data[x], data[y], label=x + " and " + y + " distribution")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.legend()
        if not lay:
            plt.show()
    if lay:
        plt.show()


# Запитуємо у користувача влстивості графіків
def plot_options(plot_data):
    print("Choose type of plot:")
    option = int(input("1 - Linear\n2 - Scatter\n3 - Custom\n"))
    print("Choose the necessary data for plots:")
    if option == 1:
        kind = "lin"
        types_data = list(map(str, input(
            "new_susp / new_confirm / active_confirm "
            "/ new_death / new_recover - distribution by datetime\n").split(" / ")))
        mega_lin_sca_plot_builder(types_data, plot_data, kind)

    if option == 2:
        kind = "sca"
        types_data = list(map(str, input(
            "new_susp / new_confirm / active_confirm "
            "/ new_death / new_recover - distribution by datetime\n").split(" / ")))
        mega_lin_sca_plot_builder(types_data, plot_data, kind)

    if option == 3:
        custom_plot_builder(plot_data)
