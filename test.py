import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/matches.csv")
groups = df.groupby("game_mode")["duration"].mean()

groups.plot(kind="bar")

plt.title("Длительность игры в зависимости от режима")
plt.xlabel("Название режима")
plt.ylabel("Время")
plt.show()