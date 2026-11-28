"""Readings of two candidate lepton word sets on the ring and coloured charts (no data).

Set A (least-trace ladder in the charge class, tau thread): e = Delta, mu = s1^2 s2^-1,
tau = s1^4 s2^-1. Set B (universality ladder, ruling 22:37Z): e = Delta, mu = Delta^3,
tau = Delta^5. Indices: s1 = sigma_0, s2 = sigma_1 of the tau thread.
Readings: PSL(2,Z) trace, linking sum (U(1) = 3 lk, #9805), ring mass m and U = -q d log m at q0,
coloured ring mass for N = 2..4 (#9819 conventions). Owner instruction (via tau thread): do NOT
compare with measured masses until the owner picks a set. No measured value appears here.
"""
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coloured_delta_ladder_probe import ring_mass  # noqa: E402  (runs its own checks on import)

Q0 = 1.1099785827513808
A = np.array([[1, 1], [0, 1]])
B = np.array([[1, 0], [-1, 1]])
G = {1: A, 2: B, -1: np.round(np.linalg.inv(A)).astype(int), -2: np.round(np.linalg.inv(B)).astype(int)}


def psl_trace(word):
    M = np.eye(2, dtype=int)
    for s in word:
        M = M @ G[s]
    return abs(int(np.trace(M)))


def U(N, word, q=Q0, h=1e-6):
    f = lambda x: np.log(abs(ring_mass(N, x, word)))
    return -q * (f(q + h) - f(q - h)) / (2 * h)


D = [1, 2, 1]
SETS = {
    "A least-trace": {"e": D, "mu": [1, 1, -2], "tau": [1, 1, 1, 1, -2]},
    "B universality": {"e": D, "mu": D * 3, "tau": D * 5},
}
checks = []
print()
for name, ws in SETS.items():
    print(f"== Set {name} ==")
    print(f"{'gen':>4s} {'|tr|':>5s} {'m2(q0)':>10s} {'U2(q0)':>9s} {'U2(1)':>7s} {'m3/m3e':>9s} {'m4/m4e':>9s}")
    base = {N: ring_mass(N, Q0, ws['e']) for N in (2, 3, 4)}
    for g, w in ws.items():
        tr = psl_trace(w)
        print(f"{g:>4s} {tr:>5d} {ring_mass(2, Q0, w):>10.5g} {U(2, w):>9.4f} {U(2, w, q=1.0):>7.3f} "
              f"{ring_mass(3, Q0, w) / base[3]:>9.4g} {ring_mass(4, Q0, w) / base[4]:>9.4g}")
    print()
checks.append(psl_trace(D) == 0)
checks.append(psl_trace([1, 1, -2]) == 4 and psl_trace([1, 1, 1, 1, -2]) == 6)
print(f"{sum(checks)}/{len(checks)} trace checks pass")
sys.exit(0 if all(checks) else 1)
