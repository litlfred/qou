import sympy
from sympy import nsimplify, pi

B2 = 2.224566
Q1 = 2.277455
Q2 = 2.277438
K = 1.0/32.0
E0 = 4.004
me = 0.51099895

print("Trying nsimplify on B2 / Q1")
print(nsimplify(B2 / Q1, tolerance=1e-5))

print("Trying nsimplify on B2 / Q2")
print(nsimplify(B2 / Q2, tolerance=1e-5))

print("Trying nsimplify on B2 - Q1 + something")
print(nsimplify(Q1 - B2, tolerance=1e-5))

print("What if B2 is Q * (1 - K^2 * something)?")
diff = Q1 - B2
print("diff = ", diff)
print(nsimplify(diff / K, tolerance=1e-5))
print(nsimplify(diff / (K**2), tolerance=1e-5))

print("Is there a relation B2 = Q * (1 - something * K)?")
print(nsimplify((Q1 - B2) / (Q1 * K), tolerance=1e-5))
