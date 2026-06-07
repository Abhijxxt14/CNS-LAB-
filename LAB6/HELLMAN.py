
q = 157      # shared prime
p = 5        # primitive root

XA = 15      # private key of A
XB = 27      # private key of B

YA = pow(p, XA, q)
YB = pow(p, XB, q)

KA = pow(YB, XA, q)
KB = pow(YA, XB, q)

print("\nDiffie-Hellman")
print("YA =", YA)
print("YB =", YB)
print("Shared Key at A =", KA)
print("Shared Key at B =", KB)
