"""Ring-mass energy readings of the corpus braid words, and U(1) = 3*lk (no fitting).

Ring mass (def:mass-identity): m(beta) = [2]^n q^{-2w} tr_D(beta) on n = 3 strands, with
tr_D = y3 * q^w + y21 * tr(rho21(beta)) (convention D, QOU.Nuclear.WeightSpaceMarkov).
Energy reading U = -q d/dq log m (thermodynamic sign).

Lean: QOU/Observations/RingMassLinkingNumber.lean and
QOU/Transcendental/MassTheory/RingMassLinkingNumber.lean prove the two-strand family
m(sigma1^n) = [3] q^-n + (-1)^n q^-3n with U(1) = 3k on T(2,2k) (lk = k) and 0 on knots.
This probe checks the same on three strands and reads the corpus words:
  electron  sigma1 sigma2 sigma1  (Hopf, lk 1)
  muon      (sigma1 sigma2^-1)^2  (4_1, knot)
  proton    (sigma1 sigma2^-1)^3  (Borromean, all lk 0)
It also reads the corpus volume chart of QOU.Core.MassInRing (m_mu/m_e = v/hbar^2), where the
volume v is constant in q. Nothing here is compared with a measured value.
"""
import sys
import mpmath as mp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / p))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 30
q0 = mp.mpf(Q_50_DIGIT_STR)
checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def gens(q):
    A = mp.matrix([[q, 1], [0, -1 / q]])
    B = mp.matrix([[-1 / q, 0], [1, q]])
    return {1: A, -1: mp.inverse(A), 2: B, -2: mp.inverse(B)}


def ring_mass(word, q):
    g = gens(q)
    M = mp.eye(2)
    w = 0
    for s in word:
        M = M * g[s]
        w += 1 if s > 0 else -1
    s2 = (q + 1 / q) ** 2
    tr = (1 - 2 / s2) * q**w + (M[0, 0] + M[1, 1]) / s2
    return (q + 1 / q) ** 3 * q ** (-2 * w) * tr


def U(f, q):
    return -q * mp.diff(lambda x: mp.log(f(x)), q)


WORDS = {
    "electron s1 s2 s1 (Hopf, lk 1)": ([1, 2, 1], 1),
    "muon (s1 s2^-1)^2 (4_1)": ([1, -2] * 2, 0),
    "proton (s1 s2^-1)^3 (Borromean)": ([1, -2] * 3, 0),
    "trefoil s1^3 s2 (knot)": ([1, 1, 1, 2], 0),
    "T(2,4) s1^4 s2 (lk 2)": ([1, 1, 1, 1, 2], 2),
    "T(2,6) s1^6 s2 (lk 3)": ([1] * 6 + [2], 3),
}

eps = mp.mpf(10) ** -15
one = mp.mpf(1)
print(f"{'word':36s} {'m(1)':>6s} {'U(1)':>8s} {'3*lk':>5s} {'m(q0)':>12s} {'U(q0)':>12s}")
rows = {}
for name, (word, lk) in WORDS.items():
    f = lambda x, w=word: ring_mass(w, x)
    u1 = U(f, one)
    uq = U(f, q0)
    rows[name] = uq
    print(f"{name:36s} {mp.nstr(f(one), 4):>6s} {mp.nstr(u1, 6):>8s} {3 * lk:>5d} "
          f"{mp.nstr(f(q0), 10):>12s} {mp.nstr(uq, 10):>12s}")
    check(f"U(1) = 3*lk for {name}", abs(u1 - 3 * lk) < eps)

# stabilisation invariance: s1 s2 s1 (3 strands) = Hopf on 2 strands = [4]/q^3
check("electron word = [4]/q^3",
      abs(ring_mass([1, 2, 1], q0) - (q0**3 + q0 + 1 / q0 + q0**-3) / q0**3) < eps)
# two-strand family formula, n = 4 stabilised
m24 = lambda x: (x**2 + 1 + x**-2) * x**-4 + x**-12
check("T(2,4): s1^4 s2 equals [3]q^-4 + q^-12", abs(ring_mass([1, 1, 1, 1, 2], q0) - m24(q0)) < eps)
# amphichirality of 4_1: m(1/q) = m(q), so U is odd in log q
fm = lambda x: ring_mass([1, -2] * 2, x)
check("4_1 ring mass is q <-> 1/q symmetric", abs(fm(q0) - fm(1 / q0)) < eps)

print()
print("-- volume chart (QOU.Core.MassInRing, units of m_e, v constant in q) --")
U_mu_vol = 2 / (q0 - 1)
check("U(v/hbar^2) = 2/(q-1)", abs(U(lambda x: 1 / (1 - 1 / x) ** 2, q0) - U_mu_vol) < eps)
print("U_mu (v/hbar^2, ratio to m_e)   ", mp.nstr(U_mu_vol, 12))
U_e = rows["electron s1 s2 s1 (Hopf, lk 1)"]
print("U_e  (ring, [4]/q^3)             ", mp.nstr(U_e, 12))
print("U_mu absolute (U_e + 2/(q-1))     ", mp.nstr(U_e + U_mu_vol, 12))
VOL41 = 2 * mp.clsin(2, mp.pi / 3)   # Vol(4_1), a constant of the ring F = Q(q, v)


def m_p_vol(x):
    h = x - 1 / x
    tr_bor = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)
    f_bor = tr_bor * (x**2 + 1 + x**-2) * (x + 1 / x) / x**3
    return 2 * (VOL41 / (1 - 1 / x) ** 2 * f_bor - 6)


print("U_p  (2(v/hbar^2 F_Bor - 6))      ", mp.nstr(U(m_p_vol, q0), 12))
print()
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
