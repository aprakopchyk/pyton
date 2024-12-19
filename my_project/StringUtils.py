import random
import string

class StringUtils:
    @staticmethod
    def random_text_generation(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))