from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_busines import Laptop_Business

laptop_pepito = Laptop("Lenovo", "17", 32)
# laptop_maria = Laptop_Gaming("Lenovo", "17", 32, 600)
laptop_juanito = Laptop_Gaming("MST", "17", 4, "RTX 8GB")
print(laptop_juanito.realizar_diagnostico_sistema())
# print(f" gamin {laptop_maria.costo}")

print("pc negocio ")
laptop_kevin=Laptop_Business("dell", "intel i3", 8,"200 gb","3 h")
print(laptop_kevin.realizar_diagnostico_sistema())