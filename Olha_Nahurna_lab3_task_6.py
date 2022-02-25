'''
My module
'''
class LogisticSystem:
    '''
    logistic system
    '''
    def __init__(self, vehicles: list):
        '''
        main atributes
        '''
        self.vehicles = vehicles
        self.list_of_orders = [41241241, 4124351224, 855488695]
    def placeOrder(self, order):
        '''
        Check if vehicles are free
        '''
        self.order = order
        numb_of_vehicles = len(self.vehicles)
        if numb_of_vehicles < 1:
            return print('There is no available vehicles')
        else:
            self.vehicles.pop(0)
            return self.order, len(self.vehicles)

    def trackOrder(self, orderld, order, my_items):
        '''
        return info about your order
        '''
        self.orderld = orderld
        if self.orderld not in self.list_of_orders:
            return 'No such order'
        else:
            return f"Your order #{self.orderld} is sent to {order.location.city}. Total price: {order.calculateAmount(my_items)} UAH."


class Order:
    '''
    information about order
    '''
    def __init__(self, user_name, city, postoffice, items, number_ld):
        '''
        main atributes
        '''
        self.number_ld = number_ld
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
    def __str__(self):
        '''
        your order number
        '''
        return f"Your order number is {self.number_ld}"
        
    def calculateAmount(self, my_items):
        '''
        count total price
        '''
        self.total_price = 0
        count = len(self.items)
        for elem in range(count):
            price = my_items[elem].price
            self.total_price += price
        return self.total_price

    def assignVehicle(self):
        '''
        assign vehicle
        '''
        if logSystem.vehicles:
            logSystem.vehicles = logSystem.vehicles.pop(0)
            return True
        else:
            return False

class Location:
    '''
    information about location
    '''
    def __init__(self, city, postoffice):
        '''
        main atributes
        '''
        self.city = city
        self.postoffice = postoffice

class Item:
    '''
    information about items
    '''
    def __init__(self, name, price):
        '''
        main atributes
        '''
        self.name = name
        self.price = price
    def __str__(self):
        '''
        your items
        '''
        return f'Your order:{self.name}, it costs: {self.price}'

class Vehicle:
    '''
    information about vehicles
    '''
    def __init__(self, vehicleNo, isAvailable=True):
        '''
        main atributes
        '''
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
info = logSystem.placeOrder(my_order)
print(logSystem.trackOrder(my_order.number_ld, my_order, my_items))
# "Your order #165488695 is sent to Lviv. Total price: 154 UAH."
number_ld = 41241241
my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
my_order2 = Order('Andrii', 'Odessa', 3, my_items2, number_ld)
print(my_order2.__str__())
info = logSystem.placeOrder(my_order2)
print(logSystem.trackOrder(my_order2.number_ld, my_order2, my_items2))

number_ld = 485932990
my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3, number_ld)
info = logSystem.placeOrder(my_order3)
print(logSystem.trackOrder(my_order3.number_ld, my_order3, my_items3))