products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80), ("Апельсины", 12, 70)],
    "Овощи": [("Морковь", 20, 30), ("Картофель", 25, 40)],
    "Напитки": [("Сок", 5, 120), ("Вода", 30, 50)]
}


print("### Все товары по категориям:")
for category, items in products.items():
    print(f"{category}:")
    for name, quantity, price in items:
        print(f"- {name} — {quantity} шт., {price} руб.")
    print()


max_price = -1
most_expensive_item = None
most_expensive_category = None

for category, items in products.items():
    for name, quantity, price in items:
        if price > max_price:
            max_price = price
            most_expensive_item = (name, quantity, price)
            most_expensive_category = category

print("### Самый дорогой товар:")
if most_expensive_item:
    print(f"'{most_expensive_item[0]}' из категории '{most_expensive_category}' (цена: {most_expensive_item[2]} руб.)")
else:
    print("В магазине нет товаров.")
print()


max_total_quantity = -1
category_with_most_items = None

for category, items in products.items():
    total_quantity_in_category = sum(item[1] for item in items)
    if total_quantity_in_category > max_total_quantity:
        max_total_quantity = total_quantity_in_category
        category_with_most_items = category

print("### Категория с наибольшим количеством товаров:")
if category_with_most_items:
    print(f"'{category_with_most_items}' (всего: {max_total_quantity} шт.)")
else:
    print("В магазине нет товаров.")
print()


total_store_cost = 0

for category, items in products.items():
    for name, quantity, price in items:
        total_store_cost += quantity * price

print("### Общая стоимость всех товаров в магазине:")
print(f"{total_store_cost} руб.")
