from Extended_Euclidean import extended_euclidean
from random import getrandbits
from Miller_Rabin import miller_rabin_test
from fast_modular_expo import fast_modular_exponentiation
def getBigRandomPrime(bits):

    while True:
        num = getrandbits(bits)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
                  241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
        if any(num % prime == 0 for prime in primes):
            continue
        if miller_rabin_test(num):
            return num

def key_generation(e):

    p = getBigRandomPrime(1000)
    q = getBigRandomPrime(1000)
    n = p*q 
    public_key = (n, e)

    varphi_n = (p-1) * (q-1)
    gcd, x, y = extended_euclidean(varphi_n, e)
    d = y % varphi_n
    private_key = d

    return public_key, private_key


def encryption(public_key, message):
    n, e = public_key
    encrypt_result = [str(fast_modular_exponentiation(ord(c), e, n)) for c in message]
    cipher_text = " ".join(encrypt_result)
    return cipher_text 

def decryption(private_key, n, ciphertext):
    d = private_key
    decrypt_result = [chr(fast_modular_exponentiation(int(c), d, n)) for c in cipher_text.split(' ')]
    plain_text = decrypt_result
    return ''.join(plain_text)

def chinese_remainder_decryption(p, q, c, d):
    
    dp = d % (p-1)
    dq = d % (q-1)
    
    mp = fast_modular_exponentiation(c, dp, p)
    mq = fast_modular_exponentiation(c, dq, q)

    gcd, yp, yq = extended_euclidean(p, q)
    n = p * q
    m = (((mp * yq * q) + (mq * yp * p)) %  n)
    return m


if __name__ == "__main__":
    # print(getBigRandomPrime(1000))
    public_key, private_key = key_generation(47)
    cipher_text = encryption(public_key=public_key, message="Zanan Master CHu")
    print(cipher_text.split())
    plain_text = decryption(private_key=private_key, n=public_key[0], ciphertext=cipher_text) 
    print(plain_text)
    # print(encryption(m=47, n=187, e=47))
    # print(chinese_remainder_decryption(p=100009, q=125658731, c=475, d=887))
    # print(chinese_remainder_decryption(p=463, q=547, c=7, d=1))
