class character():
    def _init_(self,name,job,age):
        self.name=name
        self.job=job
        self.age=age
        self.health=100
        delf.weapon=[]

class Fighter(character):
    def _init_(self,name,age):
        super()._init_(name,'Fighter',age)


class monster():
    def _init_(self,name):
        self.name=name

    def attack(self,other):
        pass

class dragon(monster):
    pass



rai = Fighter('Rai', 20)