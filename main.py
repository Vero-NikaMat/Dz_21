from logictic_classes import Store, Storage, Request, Shop

item1 = Store()
print(f"На складе свободных мест: {item1.get_free_space()}")
item1.add("зонт", 3)
print(f"На складе свободных мест: {item1.get_free_space()}")

if __name__ == '__main__':
    item = input("Привет, пользователь. Что желаете купить? ")
    count = input("Сколько? ")
    zakaz = Request(f"Доставить {count} {item} из склад в магазин")
    print(zakaz)
    zakaz_st = Store()
    shop = Shop()
    print(f"На {zakaz.from_} хранится:")
    for i, k in zakaz_st.get_items().items():
        print(k, i)
    if zakaz_st.get_items().get(zakaz.product, 0) < zakaz.amount:
        print('Не хватает на складе, попробуйте заказать меньше или другой продукт!')
    else:
        print('Нужное количество есть на складе!')
        zakaz_st.remove(name=zakaz.product, count=zakaz.amount)
        print(f'Курьер везет {zakaz.amount} {zakaz.product} со склад в магазин.')
        shop.add(name=zakaz.product, count=zakaz.amount)

    print(f"На {zakaz.from_} хранится:")
    for i, k in zakaz_st.get_items().items():
        print(k, i)

    print(f"На {zakaz.to} хранится:")
    for i, k in shop.get_items().items():
        print(k, i)







