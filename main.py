cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
	for line in f:
		key = line.strip()
		temp_list = []
		for i in range(int(f.readline().strip())):
			value = f.readline().strip()
			split_value = value.split(' | ')
			temp_dict = {'ingredient_name': split_value[0],
			'quantity': int(split_value[1]), 'measure': split_value[2]}
			temp_list.append(temp_dict)
		f.readline()
		cook_book[key] = temp_list
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
	shop_list = {}
	for i in dishes:
		if i in cook_book:
			for item in cook_book[i]:
				if item['ingredient_name'] not in shop_list:
					shop_list[item['ingredient_name']] = {'measure': item['measure'], 'quantity': item['quantity']*person_count}
				else:
					shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
		else: print('Блюда нет в книге')
	return(shop_list)

z=get_shop_list_by_dishes(['Омлет','Фахитос'], 2)
print(z)

