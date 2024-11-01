from cake import Cake
from constants import ABSTRACT_DECORATOR
from constants import SUGAR_DECORATOR
from constants import NUTS_DECORATOR

class AbstractDecorator(Cake):
    def __init__(self, cake: Cake):
        super().__init__(cake.get_price(), cake.get_name())
        self._cake = cake
    
    def __str__(self) -> str:
        return super().__str__() + ABSTRACT_DECORATOR + '\n'

class Sugar(AbstractDecorator):
    def __init__(self, cake: Cake):
        super().__init__(cake)
        super().set_name(SUGAR_DECORATOR)
    
    def __str__(self) -> str:
        return super().__str__() + super().get_name()

class Nuts(AbstractDecorator):
    def __init__(self, cake: Cake):
        super().__init__(cake)
        super().set_name(NUTS_DECORATOR)
    
    def __str__(self) -> str:
        return super().__str__() + super().get_name()