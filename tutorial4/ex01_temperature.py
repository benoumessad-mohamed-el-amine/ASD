import numpy as np

T = np.array([
    [22, 25, 20],
    [24, 27, 21],
    [19, 20, 22],
    [25, 29, 28],
    [26, 30, 27],
    [21, 21, 23],
    [20, 26, 25],
])

cities = ["Alger", "Annaba", "Oran"]

print("Max per city:", T.max(axis=0))
print("Max per day:", T.max(axis=1))
print("Overall max:", T.max())

day_idx, city_idx = np.unravel_index(T.argmax(), T.shape)
print(f"Overall max at day {day_idx + 1}, city {cities[city_idx]}")

higher_alger_oran = np.maximum(T[:, 0], T[:, 2])
print("Higher between Alger and Oran per day:", higher_alger_oran)

averages = T.mean(axis=0).reshape(1, -1)
T_with_avg = np.vstack([T, averages])
print("Table with average row:\n", T_with_avg)

annaba_hottest = (T[:, 1] > T[:, 0]) & (T[:, 1] > T[:, 2])
print("Days where Annaba was hottest:", np.where(annaba_hottest)[0] + 1)

