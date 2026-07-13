import sympy as sp
w = sp.Symbol('w')
q = 1 + w
b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
hbar_q = (q - 1)/q
u_lad = b * hbar_q**2

print("u_lad:")
print(u_lad.series(w, 0, 8))

c2 = sp.Symbol('c2')
ladd = 1 + c2 * u_lad**2
print("ladd:")
print(ladd.series(w, 0, 8))

