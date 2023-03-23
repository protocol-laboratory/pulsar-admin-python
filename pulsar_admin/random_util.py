import random
import uuid


class RandomUtil:
    @staticmethod
    def random_string():
        return str(uuid.uuid4())

    @staticmethod
    def random_int():
        return random.randint(-(2 ** 31), 2 ** 31 - 1)

    @staticmethod
    def random_long():
        return random.randint(-(2 ** 63), 2 ** 63 - 1)

    @staticmethod
    def random_positive_long():
        return random.randint(0, 2 ** 63 - 1)

    @staticmethod
    def random_positive_int():
        return random.randint(0, 2 ** 31 - 1)

    @staticmethod
    def random_negative_int():
        return random.randint(-(2 ** 31), -1)
