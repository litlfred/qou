import sympy
q = sympy.Symbol('q')
q_inv = 1/q
def q_int(n): return (q**n - q**(-n))/(q - q**(-1))
def q_fact(n): return sympy.prod(q_int(i) for i in range(1, n+1))

h = q - q_inv
sigma_alt = 1 - h*q_inv
# we want X_exact(q) = X_baseline(q) * (1 + O(h^2 / [4]_q!))
# The exact coupling is the trace of the 2-vertex weak insertion on H_4
p4_trace = 1 / q_fact(4)

print("P4 Trace:", sympy.simplify(p4_trace))
print("Correction term:", sympy.simplify((1 - sigma_alt) * p4_trace))
