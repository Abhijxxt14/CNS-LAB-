# Experiment 6 : RSA and Diffie-Hellman

from math import gcd

# ---------- RSA ----------

p = 61
q = 53
e = 17

n = p * q
phi = (p - 1) * (q - 1)

for d in range(1, phi):
    if (e * d) % phi == 1:
        break

print("RSA")
print("n =", n)
print("phi =", phi)
print("Public Key (e,n) =", (e, n))
print("Private Key (d,n) =", (d, n))

m = 65  # message

c = pow(m, e, n)
print("Encrypted =", c)

m2 = pow(c, d, n)
print("Decrypted =", m2)

