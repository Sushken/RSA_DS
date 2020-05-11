import math
from hashlib import sha1
from sympy import randprime


class RSA:

    def __init__(self, hash):
        self.m = hash  # хэш от входяшего файла
        print("m = ", self.m)

        len_of_bits = input("Enter the len of bits = ")
        p = q = 0
        while p == q:
            p = randprime((2 ** (int(len_of_bits) - 1)), (2 ** int(len_of_bits)))
            q = randprime((2 ** (int(len_of_bits) - 1)), (2 ** int(len_of_bits)))
        n = p * q
        phi = (p - 1) * (q - 1)

        e = 0
        while math.gcd(e, phi) != 1:
            e = randprime(2, phi - 1)
        print("e = ", e)

        d = modinv(e, phi)

        privkey = [d, n]
        pubkey = [e, n]
        s = self.cipher(self.m, privkey)
        print("cipher = ", s)
        dec = self.decipher(s, pubkey)
        print("decipher = ", dec)

    def cipher(self, m, priv_key):
        return pow(m, priv_key[0], priv_key[1])

    def decipher(self, s, pub_key):
        return pow(s, pub_key[0], pub_key[1])


def hash(text):
    hash_object = sha1(text.encode())
    hex_digest = hash_object.hexdigest()
    return int(hex_digest, 16)


def egcd(a, b):
    l, r = abs(a), abs(b)
    x, lx, y, ly = 0, 1, 1, 0
    while r:
        l, (q, r) = r, divmod(l, r)
        x, lx = lx - q * x, x
        y, ly = ly - q * y, y

    return l, -lx if a < 0 else lx, -ly if b < 0 else ly


def modinv(a, m):
    g, x, y = egcd(a, m)  # solving g = a * x + m * y
    assert g == a * x + m * y
    if g != 1:
        raise ValueError
    return x % m


if __name__ == '__main__':
    file = open("input.txt", 'r')
    text = file.read()
    RSA(hash(text))
