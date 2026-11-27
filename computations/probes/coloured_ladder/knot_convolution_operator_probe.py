"""Knot convolution operator of 4_1: block scalars, root-of-unity value, growth (no fitting).

Lean: QOU/Observations/KnotConvolutionOperator.lean (habiroJ41, habiroJ41_at_root, habiroJ41_two)
and QOU/Transcendental/MassTheory/KnotConvolutionVolume.lean (growth_comp, growth_of_bounded).
The 4_1 operator acts on the colour-N block by J'_N(4_1; Q) (Habiro). At Q = zeta_N this is the
Kashaev invariant, whose growth (2 pi/N) log tends to Vol(4_1) (Andersen-Hansen, cited).
"""
import sys
import mpmath as mp

mp.mp.dps = 30
checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def habiro_j41(Q, N):
    s = 0
    for m in range(N):
        p = 1
        for j in range(m):
            p *= Q**N + Q**-N - Q**(j + 1) - Q**-(j + 1)
        s += p
    return s


def kashaev41(N):
    z = mp.expjpi(mp.mpf(2) / N)
    s = 0
    for m in range(N):
        p = 1
        for j in range(m):
            p *= (1 - z**(j + 1)) * (1 - z**-(j + 1))
        s += p
    return s


VOL41 = 2 * mp.clsin(2, mp.pi / 3)
for N in (3, 5, 8):
    z = mp.expjpi(mp.mpf(2) / N)
    check(f"N={N}: Habiro sum at zeta_N = Kashaev sum", abs(habiro_j41(z, N) - kashaev41(N)) < 1e-20)
q = mp.mpf("1.1099785827513808076")
ring41 = (q**2 + 1) * (q**8 - q**6 + q**4 - q**2 + 1) / q**5
check("ring mass of (s1 s2^-1)^2 = [2] * J'_2(4_1; Q=q^2)", abs(ring41 - (q + 1 / q) * habiro_j41(q**2, 2)) < 1e-20)

print()
print(f"{'N':>5s} {'(2pi/N) log K_N':>18s} {'minus (3pi/N) log N':>22s}")
for N in (10, 50, 200, 800):
    K = mp.re(kashaev41(N))
    g = 2 * mp.pi / N * mp.log(K)
    g1 = g - 3 * mp.pi / N * mp.log(N)
    print(f"{N:>5d} {mp.nstr(g, 10):>18s} {mp.nstr(g1, 10):>22s}")
print("Vol(4_1)", mp.nstr(VOL41, 12))
K = mp.re(kashaev41(800))
check("growth at N=800 (one-loop removed) within 1% of Vol(4_1)",
      abs(2 * mp.pi / 800 * mp.log(K) - 3 * mp.pi / 800 * mp.log(800) - VOL41) < 0.01 * VOL41)
print()
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
