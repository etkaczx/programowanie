"""Module with definitions of considered species"""
import random

class Creature:

    alive: bool = True

    def __init__(self, p_death: float, p_reproduce: float):
        self.p_death = p_death
        self.p_reproduce = p_reproduce

    def kill(self):
        """Kills the creature with probability p_death"""
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        """Returns new instance of Creature with probability p_reproduce (otherwise None)"""
        if self.alive and (random.random() < self.p_reproduce):
            return self.__class__(p_death=self.p_death, p_reproduce=self.p_reproduce)

        return None


    @property
    def p_death(self):
        return self.__p_death

    @p_death.setter
    def p_death(self, value):
        value = min(1.0, max(0.0, value))
        self.__p_death = value

    @property
    def p_reproduce(self):
        return self.__p_reproduce

    @p_reproduce.setter
    def p_reproduce(self, value):
        value = min(1.0, max(0.0, value))

        self.__p_reproduce = value


class Prey(Creature):
    def __init__(self, p_death: float, p_reproduce: float, p_hunt: float = 0.5):
        super().__init__(p_death, p_reproduce)
        self.p_hunt = p_hunt

    def reproduce(self):
        child = super().reproduce()
        if child:
            child.p_hunt = self.p_hunt
        return child


class Predator(Creature):

    p_death_hungry = 0.9

    def __init__(self, p_death: float, p_reproduce: float):
        super().__init__(p_death, p_reproduce)
        self.hungry = True

    def hunt(self, prey):
        """Hunt succeeds with probability prey.p_hunt"""
        if self.alive and prey.alive and random.random() < prey.p_hunt:
            prey.alive = False
            self.hungry = False

    def kill(self):
        """Death with p_death_hungry when the predator is hungry"""
        p = self.p_death_hungry if self.hungry else self.p_death
        if random.random() < p:
            self.alive = False