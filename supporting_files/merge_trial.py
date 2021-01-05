import pandas as pd
from tabulate import tabulate
from functools import reduce

num_dice = {
    "d4": 0,
    "d6": 6,
    "d8": 0,
    "d10": 0,
    "d12": 0,
    "d20": 0,
    }

dice_faces = {
    "d4": [i for i in range(1, 5)],
    "d6": [i for i in range(1, 7)],
    "d8": [i for i in range(1, 9)],
    "d10": [i for i in range(1, 11)],
    "d12": [i for i in range(1, 13)],
    "d20": [i for i in range(1, 21)],
}

dice_names = ["d4", "d6", "d8", "d10", "d12", "d20"]

df_list = []
for dice_name in dice_names:
    if num_dice[dice_name]:
        for i in range(1, num_dice[dice_name] + 1):
            df_list.append(pd.DataFrame(dice_faces[dice_name], columns=[dice_name]).assign(foo=1))

df_combos = reduce(lambda left, right: pd.merge(left, right, on=['foo']), df_list).drop('foo', 1).dropna(axis=1)

print(tabulate(df_combos.head(), headers="keys", tablefmt="psql", showindex=False))