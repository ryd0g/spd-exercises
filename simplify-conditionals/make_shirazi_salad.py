# by Kami Bigdely
# Consolidate conditional expressions

def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)

def make_shirazi_salad(ingredients):
    ingredients_list = ['cucumber', 'tomato', 'onion', 'lemon juice']
    for i in ingredients_list:
        if i not in ingredients_list:
            print('Ingredient not found')
            return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
