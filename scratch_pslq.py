import mpmath
mpmath.mp.dps = 100

q = mpmath.mpf('1.1099785827513808075916690956107688798744991218736')
c3 = mpmath.mpf('0.574282408456938210355325492317822986877864197992923769911929007421252062369680371490919245')
c21 = mpmath.mpf('0.507837426746464228913988647035446059902640201389006093845946328320494447333550882672314545')
c111 = mpmath.mpf('-0.0168135971275242277025816353272635952329381678125553655184651322421379193189033333671192534')

target = (3*q**2 + 4 + 3/q**2)/4

# H3 objects
dim_3 = mpmath.mpf(1)
dim_21 = mpmath.mpf(2)
dim_111 = mpmath.mpf(1)

dimq_3 = mpmath.mpf(1)
dimq_21 = q + 1/q
dimq_111 = mpmath.mpf(1)

# W_lambda
q3 = q**2 + 1 + 1/q**2
W_3 = 1/q3
W_21 = (q+1/q)**2 / q3
W_111 = 1/q3

# d_q
dq_3 = 1
dq_21 = (q+1/q)**2 - 1
dq_111 = 1

def q_integer(n): return (q**n - q**-n)/(q - 1/q)
qint3 = q_integer(3)

basis = [
    target,
    c3 * dim_3, c21 * dim_21, c111 * dim_111,
    c3 * dimq_3, c21 * dimq_21, c111 * dimq_111,
    c3 * dimq_3**2, c21 * dimq_21**2, c111 * dimq_111**2,
    c3 * W_3, c21 * W_21, c111 * W_111,
    c3 * dq_3, c21 * dq_21, c111 * dq_111,
    c3 * qint3, c21 * qint3, c111 * qint3,
]

# We need to remove duplicates and exact 0s to make PSLQ stable
filtered_basis = []
for i, b in enumerate(basis):
    if b > 1e-10: # keep only significant
        # check if linearly dependent with existing? PSLQ handles it if we don't have exact copies
        # wait, c3*dim_3 = c3*dimq_3 = c3*dq_3 = c3
        filtered_basis.append(b)

res = mpmath.pslq(filtered_basis, tol=1e-50, maxcoeff=1000)
print("PSLQ result (all positive):", res)

