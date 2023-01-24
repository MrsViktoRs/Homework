with open('Cook-Book.txt', 'rt', encoding='utf-8') as file:
    Cook_book = {}
    for line in file:
        dish_name = line.strip()
        num_of_ingred = int(file.readline())
        ingredients = []
        for i in range(num_of_ingred):
            expl = file.readline().strip()
            ingredient_name, quantity, measure = expl.strip().split('|')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        Cook_book[dish_name] = ingredients


def get_shop_list_by_dishes(dishes, person_count):
    dict_one = {}
    for dish in dishes:
        if dish in Cook_book:
            for ingred in Cook_book[dish]:
                dict_two = {
                    'quantity': int(ingred['quantity']) * person_count,
                    'measure': ingred['measure']
                }
                dict_one[ingred['ingredient_name']] = dict_two
    return dict_one

