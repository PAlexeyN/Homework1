cook_book = {}
with open('recipes.txt', encoding='utf-8') as src_file:
    last_key = ''
    for line in src_file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            last_key = line
        elif line and '|' in line:
            name, qt, msure = line.split(" | ")
            cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))
 
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:  
        if dish_name in line:
            for ings in line[dish_name]:  
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count
 
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list

d = {}
for i in range(1, 3):
    name = f'{i}.txt'
    with open(name, 'r', encoding='utf-8') as f:
        d[name] = [x for x in f.read().splitlines() if x]
 
with open('final_file.txt', 'w', encoding='utf-8') as file:
    for k, v in sorted(d.items(), key=lambda x: -len([x[1]])):
        file.write(k + '\n')
        file.write(str(len(v)) + '\n')
        file.write('\n'.join(v))
        file.write('\n')