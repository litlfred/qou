import sympy as sp
w = sp.Symbol('w')
q = 1 + w
z = sp.sqrt(q)/(1+q)
h = q - 1/q
alpha = (z - 1) * h / 2
print("alpha:", alpha.series(w, 0, 6))

cos_alpha = sp.cos(alpha)
print("cos(alpha):", cos_alpha.series(w, 0, 6))
