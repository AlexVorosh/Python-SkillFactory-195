import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
print(orders)


"""1. Какой номер самого дорого заказа за июль?"""

max_price = 0
max_order = ''
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1. Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')


"""2. Какой номер заказа с самым большим количеством товаров?"""

max_quantity = 0
max_order = ''

for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    quantity = orders_data['quantity']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'2. Номер заказа с самым большим количеством товаров: {max_order}, колличество: {max_quantity}')


"""3. В какой день в июле было сделано больше всего заказов?"""

date_dict = {}

for order_num, order_data in orders.items():
    date = order_data['date']
    date_dict[date] = date_dict.get(date,0) + 1

for date in sorted(date_dict):
    max_value = max(date_dict.values())
    if date_dict[date] == max_value:
        print(f"3. Больше всего заказов было сделано {date}: {date_dict[date]}")


"""4. Какой пользователь сделал самое большое количество заказов за июль?"""

max_orders = 0
user_dict = {}

for order_num, order_date in orders.items():
    user_id = order_date['user_id']
    user_dict[user_id] = user_dict.get('user_id', 0) + 1
    orders_2 = user_dict.get(user_id)
    if orders_2 > max_orders:
        max_orders = orders_2

print(f"4. Самое большое кол-во заказов за июль у пользователя под номером: {user_id}, кол-во заказов: {max_orders}")


"""5. У какого пользователя самая большая суммарная стоимость заказов за июль?"""

user_dict = {}
max_price = 0

for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + orders_data['price']
    all_price = user_dict.get(user_id)
    if all_price > max_price:
        max_price = all_price

print(f"5. Пользователь {user_id} имеет самую большую суммарную стоимость заказов за июль: {max_price}")


"""6. Какая средняя стоимость заказа была в июле?"""

price_sum = 0
price_count = 0

for order_num, orders_data in orders.items():
    price_sum += orders_data['price']
    price_count = len(orders)

print(f"6. Средняя стоимость заказа в июле: {price_sum//price_count}")


"""7. Какая средняя стоимость товаров в июле?"""

sum_all = 0
count = 0

for order_num, orders_data in orders.items():
    sum_all += orders_data['price']
    count += orders_data['quantity']

print(f"7. Средняя стоимость товара в июле: {sum_all//count}")