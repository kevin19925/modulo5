from modulo5.retos.reto6.r6 import Auto

auto1 = Auto("marca1", "1", "2020", 20)
auto2 = Auto("marca2", "1", "2020", 10)  
print(f"Auto 1: {auto1.__dict__}")
print(f"Auto 2: {auto2.__dict__}")

Auto.comparar(auto1, auto2)  
mazda = Auto.auto_mazda()
Auto.mayor(auto1, auto2)  
toyota = Auto.auto_Toyota()
print(f"Auto Mazda: {mazda.__dict__}")
print(f"Auto toyota: {toyota.__dict__}")