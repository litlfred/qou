import math
from itertools import product
import sympy as sp

B2 = 2.224566
Q = 2.277455
K = 1.0/32.0
E0 = 4.004
me = 0.51099895

constants = {
    'Q': Q,
    'K': K,
    'E0': E0,
    'me': me,
    'pi': math.pi,
    '1': 1.0,
    '2': 2.0,
}

# we want to find f(constants) = B2
print(f"Target B2 = {B2}")
print(f"Q*(1 - K) = {Q*(1 - K)}")
print(f"Q / (1 + K) = {Q/(1 + K)}")
print(f"Q * (1 - K + K**2) = {Q*(1 - K + K**2)}")

# Let's search algebraic forms: B2 = Q * (1 - c1*K - c2*K^2 ...) + c3 * me etc
