import random
import string
from abc import ABC, abstractmethod


class GeneratePasswordAbstract(ABC):

    @abstractmethod
    def generate_password(self, length=8):
        pass


class NumericPasswordGenerator(GeneratePasswordAbstract):
    letters = string.digits

    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


class LetterPasswordGenerator(GeneratePasswordAbstract):
    letters = string.ascii_letters

    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


class MixedPasswordGenerator(GeneratePasswordAbstract):
    letters = string.ascii_letters + string.digits

    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


if __name__ == '__main__':
    generator = MixedPasswordGenerator()
    print(generator.generate_password())
