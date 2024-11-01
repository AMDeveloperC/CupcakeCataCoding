from abstract_decorator import AbstractDecorator
from abstract_decorator import Sugar
from abstract_decorator import Nuts
from cake import Cake

cake = Nuts(Sugar(Cake(2.50, "Cupcake")))
print(cake)