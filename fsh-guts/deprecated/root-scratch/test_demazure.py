import sympy as sp
x1, x2 = sp.symbols('x1 x2')
f = x1**2 * x2
s_f = f.subs({x1: x2, x2: x1}, simultaneous=True)
print("s_f:", s_f)
num = x1 * f - x2 * s_f
print("num:", num)
ans = sp.simplify(num / (x1 - x2))
print("ans:", ans)
