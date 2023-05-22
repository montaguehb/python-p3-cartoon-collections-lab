def roll_call_dwarves(dwarves):
    for index, n in enumerate(dwarves):
        print(f"{index + 1}. {n}")

def summon_captain_planet(captain):
    return([f"{n[0].upper()}{n[1:]}!"for n in captain])

def long_planeteer_calls(planeteer):
    for n in planeteer:
        if len(n) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    low_index = len(ingredients)
    for n in cheeses:
        if n in ingredients:
            low_index = ingredients.index(n)
    return ingredients[low_index] if low_index != len(ingredients) else None
find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"])