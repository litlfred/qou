import mpmath
mpmath.mp.dps = 50

q = mpmath.mpf('1.1099785827513808075916690956107688798744991218736')
c3 = mpmath.mpf('0.574282408456938210355325492317822986877864197992923769911929007421252062369680371490919245')
c21 = mpmath.mpf('0.507837426746464228913988647035446059902640201389006093845946328320494447333550882672314545')
c111 = mpmath.mpf('-0.0168135971275242277025816353272635952329381678125553655184651322421379193189033333671192534')
target = (3*q**2 + 4 + 3/q**2)/4

# We want to find D3, D21, D111 natively in H3 such that c3*D3 + c21*D21 + c111*D111 = target
# Native quantities in H3: powers of [3]_q, [2]_q, q, and integers.
# Let's generate a list of native values for each partition.
# For (3): dim=1, dim_q=1, W=1/[3]_q
# For (2,1): dim=2, dim_q=[2]_q, W=[2]_q^2/[3]_q
# For (1,1,1): dim=1, dim_q=1, W=1/[3]_q

# Just use PSLQ on: target, and c3*x, c21*y, c111*z where x, y, z are simple algebraic numbers.
