# application_user/hashers.py
from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.crypto import constant_time_compare, get_random_string
import hashlib


class DummyPasswordHasher(BasePasswordHasher):
    algorithm = "dummy"

    def encode(self, password, salt):
        hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return f"{self.algorithm}${salt}${hash}"

    def verify(self, password, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        encoded_2 = self.encode(password, salt)
        return constant_time_compare(encoded, encoded_2)

    def safe_summary(self, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        return {
            "algorithm": algorithm,
            "salt": salt,
            "hash": hash,
        }

    def must_update(self, encoded):
        return False

    def harden_runtime(self, password, encoded):
        pass
