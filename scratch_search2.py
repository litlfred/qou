import mpmath
mpmath.mp.dps = 50

q = mpmath.mpf('1.1099785827513808075916690956107688798744991218736')
c3 = mpmath.mpf('0.57428240845693821035532549231782298687786419799292')
c21 = mpmath.mpf('0.50783742674646422891398864703544605990264020138901')
c111 = mpmath.mpf('-0.016813597127524227702581635327263595232938167812555')

target = (3*q**2 + 4 + 3/q**2)/4
print("Target: ", target)
print("c3 + c21 + c111 =", c3+c21+c111)

# Check linear relations with coefficients in Q(q).
# We want to find A, B, C such that c3*A + c21*B + c111*C = target
# Where A, B, C are simple functions of q.
# Simple functions: 1, dim_q, (dim_q)^2, [n]_q, W_lambda, f_lambda

def q_integer(n):
    return (q**n - q**-n)/(q - 1/q)

q_int_2 = q_integer(2)
q_int_3 = q_integer(3)

print("q_int_2:", q_int_2)
print("q_int_3:", q_int_3)

# Could Delta_lambda be dimension in SU(4) divided by something?
# dim_SU4: [3] -> 20, [2,1] -> 20, [1,1,1] -> 4

# Or could Delta_lambda be [dim(lambda)]_q?
# [1]_q = 1
# [2]_q = q + 1/q

print("Target - (c3*1 + c21*q_int_2^2 + c111*1):", target - (c3 + c21*q_int_2**2 + c111))
print("Target - (c3*q_int_3 + c21*q_int_3 + c111*1):", target - (c3*q_int_3 + c21*q_int_3 + c111))

