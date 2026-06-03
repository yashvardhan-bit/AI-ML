# class laptop:
#     storage_type="SSD"
#     @classmethod #decorator to make the method a class method
#     def get_storage_type(cls):
#         print("storage type is ",cls.storage_type)
#     @staticmethod #decorator to make the method a static method
#     def cal_discount(price,discount):
#         final_price=price-(discount/100)*price
#         print("final price is ",final_price)
# l1=laptop()
# laptop.get_storage_type()
# l1.get_storage_type()
# l1.cal_discount(1000,10)
# class product:
#     count=0 #class variable
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count+=1 #incrementing the count of products created
#     def get_info(self):
#         print(f"product name is {self.name} and price is Rs. {self.price}")
#     @classmethod
#     def get_count(cls):
#         print(f"total products createdd are{cls.count}")
#     @staticmethod
#     def cal_discounted_price(price,discount):
#         final_price=price-(discount/100)*price
#         print(f"final price after discount is Rs. {final_price}")
# p1=product("laptop",50000)
# p1.get_info()
# p2=product("mobile",20000)
# p3=product("tablet",15000)
# product.get_count()
# p1.cal_discounted_price(50000,10)
# p2.cal_discounted_price(p2.price,20)
'''1.Encapsulation'''
'''wrapping data and methods into single unit'''
