import random # pragma: no cover
class War():
    def __init__(self, war1, war2):
        self.__war1 = war1
        self.__war2 = war2
    def hit(self, war1, war2):
        war2.set_health(war2.get_health()-war1.damage())
        print('{w1} атаковал {w2}. Здоровье {w2}: {health}'.format(w1=war1.get_name(), w2=war2.get_name(), health=war2.get_health()))
        if war2.get_health() <= 0:
            print(war1.get_name(), 'одержал победу')
            return False
        return True
    def start_war(self):
        war1 = self.__war1
        war2 = self.__war2

        while war1.get_health() > 0 and war2.get_health() > 0:
            attacking_war = random.choice([war1, war2])
            attacked_war = war2 if attacking_war == war1 else war1

            if not self.hit(attacking_war, attacked_war):
                break


class Warrior:

    def __init__(self, name):
        self.__name = name
        self.__health = 100

    def get_name(self):
        return self.__name



    def get_health(self):
        def decorate(func):
            health = func()
            if health < 0:
                return 0
            else:
                return health
        @decorate
        def real_health():
            return self.__health

        return real_health
    def set_health(self, health):
        self.__health = health
    def set_name(self, name):
        self.__name = name
    def __str__(self):
        return 'Состояние бойца {}:\nЗдоворовье - {}'.format(self.__name,self.__health)
class War1(Warrior):
    war_class = 'Белый пояс'
    counter = 0
    def __init__(self, name):
        super().__init__(name)
    def damage(self):
        self.counter += 1
        if self.counter > 4:
            self.counter = 0
        if self.counter == 4:
            print('Этот воин промахивается каждый 4 удар и сносит противнику всего 10 единиц здоровья!')
            damage = 10
            self.counter = 0
            return damage
        damage = 20
        return damage
class War2(Warrior):
    war_class = 'Желтый пояс'
    counter = 0
    def __init__(self, name): # pragma: no cover
        super().__init__(name)
    def damage(self):
        self.counter += 1
        if self.counter > 3:
            self.counter = 0
        if self.counter == 3:
            print('Каждый третий удар воина этого класса удвоенный!')
            damage = 40
            self.counter = 0
            return damage
        damage = 20
        return damage




