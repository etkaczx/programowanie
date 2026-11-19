import matplotlib.pyplot as plt
from .species import Prey, Predator


class Population:

    def __init__(self, population_data: dict, **kwargs):
        self.species = list(population_data)
        self._instances = []

        for species, count in population_data.items():
            for _ in range(count):
                creature = species(**kwargs)
                self._instances.append(creature)

        self.history = [self.n]

    def count(self, creatures):
        result = {}

        for s in self.species:
            counter = 0

            for c in creatures:
                if type(c) is s:
                    counter += 1

            result[s] = counter

        return result

    @property
    def n(self):
        return self.count(self._instances)

    def hunting(self):
        predators = []
        prey = []

        for c in self._instances:
            if isinstance(c, Predator):
                predators.append(c)

            if isinstance(c, Prey):
                prey.append(c)

        for predator, victim in zip(predators, prey):
            predator.hunt(victim)

    def natural_selection(self):

        # rozród
        newborns = []

        for c in self._instances:
            child = c.reproduce()

            if child:
                newborns.append(child)

        # polowanie
        self.hunting()

        # śmiertelność
        for c in self._instances:
            c.kill()

        # historia
        survivors = []

        for c in self._instances:
            if c.alive:
                survivors.append(c)

        current_population = survivors + newborns
        self.history.append(self.count(current_population))

        # aktualizacja zbioru
        self._instances = current_population

    def plot_history(self):
        colors = {
            "Prey": "#FFC0CB",
            "Predator": "#915F6D"
        }

        for s in self.species:
            values = []

            for h in self.history:
                values.append(h[s])

            plt.plot(values, label=s.__name__, color=colors.get(s.__name__, "pink"))

        plt.xlabel("Krok")
        plt.ylabel("Liczebność")
        plt.legend()
        plt.show()

    def plot_histogram(self, attr: str):
        values = []

        for c in self._instances:
            values.append(getattr(c, attr))

        plt.hist(values, color='#FFC0CB')
        plt.xlabel(attr)
        plt.show()
