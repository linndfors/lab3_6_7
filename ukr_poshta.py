'''
My module
'''
class LogisticSystem:
    def __init__(self, vehicles: list):
        # це наш список машин
        self.vehicles = vehicles
        self.list_of_orders = [41241241, 4124351224, 855488695]
    def placeOrder(self, order):
        # перевіряє чи є вільні машини
        self.order = order
        # кількість машин
        numb_of_vehicles = len(self.vehicles)
        # якщо кількість машин менша ніж 1, то помилка
        if numb_of_vehicles < 1:
            return 'There is no available vehicles'
        else:
            # якщо ні, то викидаємо зі списку наявних машин першу і повертаємо номер замовлення
            self.vehicles.pop(0)
            return self.order, len(self.vehicles)

    def trackOrder(self, orderld):
        # повертає повідомлення про ваше замовлення
        self.orderld = orderld
        if self.orderld not in self.list_of_orders:
            return 'Failed numberld'
        else:
            return f"Your order #{self.orderld} is sent to {my_order.location.city}. Total price: {my_order.calculateAmount()} UAH."


class Order:

    def __init__(self, user_name, city, postoffice, items, number_ld):
        # self.orderId = random.randint(100000000, 999999998)
        self.number_ld = number_ld
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
    def __str__(self):
        return f"Your order number is {self.number_ld}"
        
    def calculateAmount(self):
        # рахує суцільну ціну за предмети
        self.total_price = 0
        for elem in range(len(self.items)):
            price = my_items[elem].price
            self.total_price += price
        return self.total_price

    def assignVehicle(self):
        pass
        # призначає машину
        # if logSystem.vehicles:
        #     logSystem.vehicles = logSystem.vehicles.pop(0)
        #     return True
        # else:
        #     return False

class Location:
    def __init__(self, city, postoffice):
        self.city = city
        self.postoffice = postoffice

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        # поки не ясно що має повертати
        return f'Your order:{self.name}, it costs: {self.price}'

class Vehicle:
    def __init__(self, vehicleNo, isAvailable=True):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

number_ld = 855488695
vehicle_list = []
# призначаємо змінній об'єкт класу, а саме список з двох машин
vehicles = [Vehicle(1), Vehicle(2)]
# пердаємо список об'єкту класа logisticsystem
logSystem = LogisticSystem(vehicles)
# список з предметів та їхньої ціни
my_items = [Item('book',110), Item('chupachups',44)]
my_order = Order(user_name='Oleg', city='Lviv', postoffice=53, items=my_items, number_ld = 855488695)
# print(my_order.__str__())
# "Your order number is 165488695."
info = logSystem.placeOrder(my_order)
print(logSystem.trackOrder(my_order.number_ld))
# "Your order #165488695 is sent to Lviv. Total price: 154 UAH."
