import mpmath
mpmath.mp.dps = 50

q = mpmath.mpf('1.1099785827513808075916690956107688798744991218736')

# we know tr(beta_Bor) = y3 * x3 + y21 * x21 + y111 * x111 = 0.998558
# but wait, I can compute chi_21 exactly!
# y3 = q^3 / [3]! (wait, W3 = 1/[3]_q. y3 = ?)
# from y_lambda Wenzl weight formula:
# y_lambda = (q-1/q)^n / (something)
