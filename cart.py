# class Product():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f"{self.name}, {self.price}"



# class Cart():
#     def __init__(self):
#         self.items = []
#         self.total = 0
#         self.count = 0

    

#     def add_item(self, item):
#         for i in self.items:
#             if item.name == i.name:
#                 i.quantity += 1
#                 self.total += item.price
#                 return
#         self.total += item.price
#         self.items.append(item)
#         self.items[-1].quantity = 1
#     def remove_item(self, item):
#         for i in self.items:
#             if item.name == i.name:
#                 if i.quantity == 1:
#                     self.total -= item.price
#                     self.items.remove(item)
#                 else: 
#                     i.quantity -= 1
#                     self.total -= item.price
#                 return
#             else:
#                 print("item not found")

    
    
    
#     def __str__(self):
#         return f"{self.items}"

# cart = Cart()
# p1 = Product('X', 1000)
# p2 = Product('Y', 2000)
# p3 = Product('Z', 3000)

# cart.add_item(p1)
# print(cart.total)
# cart.add_item(p1)
# print(cart.total)
# cart.add_item(p2)
# print(cart.total)
# cart.remove_item(p1)
# print(cart.total)
# cart.remove_item(p1)
# print(cart.total)
# print(cart.items[0].quantity)
# # print(cart.items[1].quantity)



class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 1
    
    def __str__(self):
        return f"{self.name}, {self.price}"

class Cart():
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, item):
        for i in self.items:
            if item.name == i.name:
                i.quantity += 1
                self.total += item.price
                return
        self.total += item.price
        self.items.append(item)
    
    def remove_item(self, item):
        for i in self.items:
            if item.name == i.name:
                if i.quantity == 1:
                    self.total -= item.price
                    self.items.remove(i)
                else: 
                    i.quantity -= 1
                    self.total -= item.price
                return
            else:
                print("item not found")
    def __str__(self):
        return f"{self.items}"
    