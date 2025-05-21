

'''
+--------------------------------------------------+
|                    SpaceShip                     |
+--------------------------------------------------+
| - __armor: float = 50            @class-variable |
| - __life: float                                  |
+--------------------------------------------------+
| + __init__(life=100)                             |
| + blowup_animation(): None      [@static-method] |
| + get_armor(): float            [@class-method]  |
| + upgrade_10perc(): None        [@class-method]  |
| + life: float                   [@property]      |
| + life(value: float): None      [@setter]        |
+--------------------------------------------------+
'''

class EvilSpaceShip:

    __armor = 50

    def __init__(self, life=100):
        self.life = life

    # @staticmethod - blowup_animation [print('EvilSpaceShip blow up')]
    @staticmethod
    def blowup_animation(space_ship):
        print('EvilSpaceShip blow up')

    # @classmethod - get_armor -- returns the __armor value
    @classmethod
    def get_armor(cls):
        return cls.__armor
        # return EvilSpaceShip.__armor  # works but not recommended

    # @classmethod - upgrade_10perc(cls) [increase armor by 10%]
    @classmethod
    def upgrade_10perc(cls):
        cls.__armor *= 1.1

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, value):
        if value < 0:
            self.__life = 0
        else:
            self.__life = value


# __init__(self, life=100):
#   __life + getter/setter
# class variables: __armor = 50
# @classmethod - upgrade_10perc(cls) [increase armor by 10%]
# @staticmethod - blowup_animation [print('EvilSpaceShip blow up')]
# @classmethod - get_armor -- returns the __armor value

# create 2 evil-space-ship
# print the armor level
# call upgrade_10perc
# print the armor level
# call blowup_animation

evilship1 = EvilSpaceShip(90)
evilship1.life += 50
evilship2 = EvilSpaceShip(215)
evilship2.life -= 250

# print(evilship1.get_armor())  # works but bad practice
print(EvilSpaceShip.get_armor())
EvilSpaceShip.upgrade_10perc()
EvilSpaceShip.blowup_animation()

# -- Order:
# class variables
# __init__
# @classmethod
# @staticmethod
# instance-method