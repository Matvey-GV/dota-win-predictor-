import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/matches.csv")
groups = df.groupby("radiant_win")["duration"].mean()

df["duration"].plot(kind="hist")

plt.title("Распределение длительности матчей")
plt.xlabel("Секунды")
plt.ylabel("Количество матчей")
plt.show()