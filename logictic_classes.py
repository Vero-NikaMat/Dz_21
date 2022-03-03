from abc import abstractmethod

class Storage:

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage): #Склад. В нем хранится любое количество любых товаров.
            # Store не может быть заполнен если свободное место закончилось
    def __init__(self):
        self.items = {"печеньки" : 20, "пельмени" : 30, "собачки" : 10}
        self.capacity = 100


    def add(self, name, count):
        """увеличивает запас items с учетом лимита capacity"""
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name]= count
                is_found = True
        if is_found:
            print(f"{name} добавлен")

        else:
            print(f"Товар не добавлен, осталось только {self.get_free_space()} мест")


    def remove(self, name, count):
        """уменьшает запас items но не ниже 0"""
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count > 0:
                    self.items[key] = self.items[key] - count
                    print(f"Товар {name} удален со склада")
                    break
                else:
                    print(f"Товара {name} на складе сталось только {self.items[key] - count} штук")
            else:
                print(f"Товара {name.title()} нет на складе")

    def get_free_space(self):
        """вернуть количество свободных мест"""
        return self.capacity - sum(self.items.values())

    def get_items(self):
        """возвращает сожержание склада в словаре {товар: количество}"""
        return self.items

    def get_unique_items_count(self):
        """возвращает количество уникальных товаров"""
        return len(self.items.keys())


class Shop(Store): # Магазин. В нем хранится **не больше 5 разных товаров**.
            # Shop не может быть наполнен, если свободное место закончилось или в нем уже есть 5 разных товаров.
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self.limit = limit

    @property
    def get_limit(self):
        return self.limit

    def add(self, name, count):
        """увеличивает запас items с учетом лимита capacity"""
        if self.get_unique_items_count() < self.limit:
            super().add(name, count)
        else:
            print(f"Товар {name} не может быть добавлен")


class Request:
    def __init__(self, str):
        lst = self.stroka(str)
        self.from_ = lst[4]       # - откуда везем(строка)
        self.to = lst[6]        # to - куда везем(строка)
        self.amount = int(lst[1])
        self.product = lst[2]

    def stroka(self, str):
        return str.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"





