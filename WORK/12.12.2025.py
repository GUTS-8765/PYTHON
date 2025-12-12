products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80), ("Апельсины", 20, 70)],
    "Овощи": [("Морковь", 20, 30), ("Картофель", 30, 25)],
    "Напитки": [("Сок", 5, 120), ("Вода", 50, 20)]
}


print("--- Каталог товаров ---")
for category, items in products.items():
    print(f"{category}:")
    for name, count, price in items:
        print(f"  {name} — {count} шт., {price} руб.")
print("-" * 20)


max_price = 0
most_expensive_item = None
for items in products.values():
    for name, count, price in items:
        if price > max_price:
            max_price = price
            most_expensive_item = (name, count, price)

print(f"Самый дорогой товар: {most_expensive_item[0]} — {most_expensive_item[2]} руб.")
print("-" * 20)


max_total_count = 0
category_with_max_count = ""
for category, items in products.items():
    current_total_count = sum(item[1] for item in items)
    if current_total_count > max_total_count:
        max_total_count = current_total_count
        category_with_max_count = category

print(f"Категория с наибольшим запасом: {category_with_max_count} (всего {max_total_count} шт.)")
print("-" * 20)


total_store_cost = 0
for items in products.values():
    for name, count, price in items:
        total_store_cost += count * price

print(f"Общая стоимость всех товаров в магазине: {total_store_cost} руб.")
print("-" * 20)