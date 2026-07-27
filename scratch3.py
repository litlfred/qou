import mpmath as mp
import sys
mp.mp.dps = 50

# Load canonical q0
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0

print("Q0:", Q0)
print("E0:", E0)

f_req = mp.exp(-mp.mpf("2.224566") / E0)
print("f_req exactly:", f_req)

# We want to represent f_req in terms of W_alg and geometric objects.
W_alg = mp.mpf("0.660673770417933908") # I need the exact W_alg

# Let's compute W_alg exactly.
def _qint(m, q):
    return mp.mpf(m) if q == 1 else (q ** m - q ** (-m)) / (q - q ** (-1))

def gate_qfact(n, q):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= _qint(k, q)
    return r

def _conjugate(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for r in lam if r > c) for c in range(m))

def _hooks(lam):
    lamp = _conjugate(lam)
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            hs.append((row - (j + 1)) + (lamp[j] - (i + 1)) + 1)
    return hs

def gate_qdim(lam, q):
    denom = mp.mpf(1)
    for hk in _hooks(lam):
        denom *= _qint(hk, q)
    return gate_qfact(sum(lam), q) / denom

W_alg_exact = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
print("W_alg exact:", W_alg_exact)

f_bring = mp.sqrt(Q0)/(Q0+1) - (Q0 - 1/Q0)*(0.5 - 0.001377/4)

trM = mp.mpf("1.006730454652734")
kappa = mp.mpf(3)/16

# Use PSLQ to find a relation between f_req, W_alg_exact, z0, z, h, trM, kappa
z0 = mp.sqrt(Q0) - 1/mp.sqrt(Q0)
z = mp.sqrt(Q0) / (Q0 + 1)
h = Q0 - 1/Q0

print("z0:", z0)
print("z:", z)
print("h:", h)
print("trM:", trM)

terms = [f_req, W_alg_exact, z0, z, h, kappa, mp.mpf(1)]
names = ["f_req", "W_alg", "z0", "z", "h", "kappa", "1"]

# We can use mpmath's pslq
# But f_req is unlikely to be linearly related.
# Maybe log(f_req), which is -B/E0.
# Or f_req / W_alg_exact as a rational function of q?
ratio = f_req / W_alg_exact
print("ratio f_req / W_alg:", ratio)

# Let's search for algebraic relations involving q.
print("PSLQ on ratio, 1, z0, z, h:")
res = mp.pslq([ratio, mp.mpf(1), z0, z, h, z0**2, h**2, z**2, kappa, trM], tol=1e-10)
print(res)

print("PSLQ on f_req, W_alg, W_alg*z0, W_alg*kappa, ...")
res2 = mp.pslq([f_req, W_alg_exact, W_alg_exact*z0, W_alg_exact*z, W_alg_exact*h, W_alg_exact*kappa, W_alg_exact*trM], tol=1e-8)
print(res2)

