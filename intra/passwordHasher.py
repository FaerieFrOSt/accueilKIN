from django.contrib.auth.hashers import SHA1PasswordHasher
from django.utils.crypto import constant_time_compare
import hashlib
from base64 import urlsafe_b64encode as encode_b
import os

class   ZeroSHA1PasswordHasher(SHA1PasswordHasher):
    
    def encode(self, password, salt):
        res = super(ZeroSHA1PasswordHasher, self).encode(password, salt)
        salt = os.urandom(4)
        h = hashlib.sha1(password)
        h.update(salt)
        return res + "!" + encode_b(h.digest() + salt)
    
    def verify(self, password, encoded):
        tmp = encoded.split('!', 1)
        algorithm, salt, hash = tmp[0].split('$', 2)
        assert algorithm == self.algorithm
        encoded2 = self.encode(password, salt)
        return constant_time_compare(encoded, encoded2)
