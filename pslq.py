import mpmath
mpmath.mp.dps = 15

B2 = 2.224566
Q = 2.277455
K = 1.0/32.0
E0 = 4.004
me = 0.51099895
pi = mpmath.pi

constants = [B2, Q, K, E0, me, pi, 1.0, B2/Q, B2*Q, B2-Q, Q-B2, B2/E0]

# Try to find integer relation
res = mpmath.pslq([B2, Q, K, 1.0])
print("PSLQ [B2, Q, K, 1]:", res)

res = mpmath.pslq([B2, Q, K, me, 1.0])
print("PSLQ [B2, Q, K, me, 1]:", res)

res = mpmath.pslq([B2, Q, K, E0, 1.0])
print("PSLQ [B2, Q, K, E0, 1]:", res)

res = mpmath.pslq([B2, Q, 1.0])
print("PSLQ [B2, Q, 1]:", res)

res = mpmath.pslq([B2/Q, K, 1.0])
print("PSLQ [B2/Q, K, 1]:", res)

res = mpmath.pslq([B2/Q, K**2, K, 1.0])
print("PSLQ [B2/Q, K^2, K, 1]:", res)
