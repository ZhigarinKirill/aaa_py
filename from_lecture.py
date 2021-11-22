import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):
    def __init__(self, name: str):
        self.name = name
        self._exp = 0

    @property
    @abstractmethod
    def exp(self):
        pass

    @classmethod
    @abstractmethod
    def inc_exp(self, value: int):
        pass


class EmojiMixin:
    emoji = {'grass': '🌿',
             'fire': '🔥',
             'water': '🌊',
             'electric': '⚡'}

    def __str__(self):
        return super().__str__().replace(self.poketype,
                                         self.emoji.get(self.poketype)
                                         )


class BasePokemon(AnimeMon):
    def __str__(self):
        return f'{self.name}/{self.poketype}'


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name: str, poketype: str):
        super().__init__(name)
        self.poketype = poketype

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value: int):
        if value <= 0:
            raise ValueError('xp must be positive')
        self._exp = value

    def inc_exp(self, value: int):
        self.exp += value


class Digimon(AnimeMon):
    def __init__(self, name: str):
        super().__init__(name)

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value: int):
        if value <= 0:
            raise ValueError('xp must be positive')
        self._exp = value

    def inc_exp(self, value: int):
        self.exp += value * 8


def train(animemon: AnimeMon):
    """"
        Train animemon using inc_exp method
    """
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for _ in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            animemon.inc_exp(step_size)


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
    train(bulbasaur)
    print(bulbasaur.exp)

    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
