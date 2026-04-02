import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/matches.csv")
groups = df.groupby("game_mode")["duration"].mean()
groups = groups / 60

mode_names = {
    1: "All Pick",
    3: "Random Draft",
    4: "Single Draft",
    13: "New Player",
    21: "Ranked All Pick",
    22: "Turbo",
    23: "Ranked All Pick (new)"
}

groups.index = groups.index.map(mode_names)

groups.plot(kind="bar")

plt.title("Длительность игры в зависимости от режима")
plt.xlabel("Название режима")
plt.ylabel("Время в минутах")
plt.show()