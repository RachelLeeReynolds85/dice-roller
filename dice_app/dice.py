import pandas as pd
from tabulate import tabulate
from functools import reduce

def dice_calc(num_dice):

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

    df_combos["sum"] = df_combos.sum(axis=1)

    # print("ALL POSSIBLE COMBOS")
    # print(tabulate(df_combos, headers="keys", tablefmt="psql", showindex=False))

    possible_rolls = df_combos["sum"].value_counts().sort_index().index.to_list()
    ways_to_roll = df_combos["sum"].value_counts().sort_index().values

    exact_roll_prob = []
    exact_roll_percent = []
    for i in ways_to_roll:
        exact_roll_prob.append(i / sum(ways_to_roll))
        exact_roll_percent.append(f'{i / sum(ways_to_roll):.2%}')

    roll_or_higher_prob = []
    roll_or_higher_percent = []

    for i in range(1, len(exact_roll_prob) + 1):
        roll_or_higher_prob.append(sum(exact_roll_prob[:i]))
        roll_or_higher_percent.append(f'{sum(exact_roll_prob[:i]):.2%}')

    roll_or_higher_prob.reverse()
    roll_or_higher_percent.reverse()

    dice_df = pd.DataFrame(list(zip(possible_rolls, ways_to_roll, exact_roll_percent, roll_or_higher_percent)), columns = ['Roll Total', 'Ways to roll', 'Exact', 'Or higher'])

    # print("\nROLL PROBABILITIES")
    # print(tabulate(dice_df, headers="keys", tablefmt="psql", showindex=False))

    response = dice_df.to_json()

    return response


# For Testing Purposes
num_dice = {
    "d4": 1,
    "d6": 1,
    "d8": 1,
    "d10": 0,
    "d12": 0,
    "d20": 0,
    }
dice_calc(num_dice)

# num_dice = get_input()

# def get_input():
#     num_dice = {
#     "d4": 0,
#     "d6": 0,
#     "d8": 0,
#     "d10": 0,
#     "d12": 0,
#     "d20": 0,
#     }
    
#     add_dice = "y"
#     while add_dice == "y":
#         dice_type = input("""\nWhat type of dice to you want to add?
#         d4, d6, d8, d10, d12, d20? """)
#         num_type = int(input("How many do you want to add? "))
#         num_dice[dice_type] = num_type
#         add_dice = input("Continue adding dice? (y/n) ")
#     return num_dice


