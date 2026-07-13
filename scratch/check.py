import sympy as sp
w, x = sp.symbols('w x', real=True)
n = sp.Symbol('n', integer=True)
x_w = 1/(2*w) - 1
w_x = 1 / (2 * (x + 1))
dw_dx = sp.diff(w_x, x)
f = sp.Function('f')(w)
df_dw = sp.diff(f, w)
d2f_dw2 = sp.diff(df_dw, w)
dy_dx = df_dw * dw_dx
d2y_dx2 = d2f_dw2 * (dw_dx**2) + df_dw * sp.diff(dw_dx, x)
leg1 = (1 - x**2) * d2y_dx2
leg2 = -2 * x * dy_dx
print("leg1 term:", sp.simplify(leg1.subs(x, x_w)))
print("leg2 term:", sp.simplify(leg2.subs(x, x_w)))
