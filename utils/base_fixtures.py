import random
import string


class BaseFixture:

    @staticmethod
    def get_valid_string(VALID_STR_RANGE=6):
        random_string = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase) for _ in range(VALID_STR_RANGE))
        return random_string
