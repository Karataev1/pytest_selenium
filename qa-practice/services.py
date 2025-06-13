import string
import random


class GenerateText:

    @staticmethod
    def generate_char(num: int) -> str:
        final_str = ''

        for i in range(num):
            rnd = random.randint(1, 26)
            final_str = final_str + string.ascii_lowercase[rnd-1]

        return final_str


    @staticmethod
    def get_invalid_characters() -> list:
        INVALID_CHARACTERS = list((string.punctuation.replace("-", "").replace("_", "")))
        result = [char + 'test' for char in INVALID_CHARACTERS]
        return result

