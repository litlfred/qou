"""Binding on the RING-valued mass (def:mass-identity), and beta decay in the same reading.

Ring mass (framing-corrected, braid-class invariant), PR #9789:
    m(beta) = [2]^n q^{-2w} tr_D(beta) = q^{-2w} T(beta),
where T is the unnormalised quantum trace on (C^2)^{(x)n} (R-matrix with sigma - sigma^-1 = h,
weight diag(q, q^-1)). T is a Laurent polynomial in q with integer coefficients, so every
number below is computed EXACTLY in Z[q, q^-1] and only evaluated at q0 at the end.

Two readings of binding, free word x = V(0)^3 per nucleon, atom = x + bond word K:
  (log)    B_log = E0 * ln(m_free / m_atom)
  (energy) U = -q d/dq ln m;  B_U = U_free - U_atom = q d/dq ln(m_atom / m_free),
           converted with the #9789 unit m_e / U_e (U_e = 3 - D[4]/[4]).

Structural fact checked here: every gamma-gamma vertex V(s) = sigma_s sigma_{s+1}^{-1} has writhe 0,
so free and atom words have equal writhe and equal strand count. The framing factor
[2]^n q^{-2w} therefore cancels in m_free / m_atom: the ring changes neither reading of binding
relative to the raw trace. (The ring matters for the electron, w = 3, not for gamma-gamma bonds.)

Measured values (m_e, AME, CODATA Q_beta) enter only in the comparison block.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / p))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50
q0 = mp.mpf(Q_50_DIGIT_STR)

# ---------------------------------------------------------------- exact Laurent polynomials
def padd(a, b, s=1):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + s * c
        if out[e] == 0:
            del out[e]
    return out


def pmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            out[e1 + e2] = out.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in out.items() if c}


ONE, QP, H = {0: 1}, {1: 1}, {1: 1, -1: -1}
NEG_H = {1: -1, -1: 1}


def peval(a, q):
    return mp.fsum(c * q ** e for e, c in a.items())


def pdlog(a, q):
    """q d/dq ln a at q."""
    return mp.fsum(c * e * q ** e for e, c in a.items()) / peval(a, q)


def _r(a, b):
    if a == b:
        return [((a, b), QP)]
    if (a, b) == (0, 1):
        return [((0, 1), H), ((1, 0), ONE)]
    return [((0, 1), ONE)]


def T(word, n):
    """Unnormalised quantum trace of a word [(s, inverse?)] on n strands, in Z[q, q^-1]."""
    tot = {}
    for st in itertools.product((0, 1), repeat=n):
        v = {st: ONE}
        for (s, inv) in word:
            out = {}
            for cur, c in v.items():
                a, b = cur[s], cur[s + 1]
                terms = _r(a, b) + ([((a, b), NEG_H)] if inv else [])
                for (a2, b2), k in terms:
                    ns = cur[:s] + (a2, b2) + cur[s + 2:]
                    out[ns] = padd(out.get(ns, {}), pmul(c, k))
            v = {k: c for k, c in out.items() if c}
        if st in v:
            w = st.count(0) - st.count(1)
            tot = padd(tot, pmul({w: 1}, v[st]))
    return tot


def writhe(word):
    return sum(-1 if inv else 1 for (_, inv) in word)


def ring_mass(word, n):
    return pmul({-2 * writhe(word): 1}, T(word, n))


def V(s):
    return [(s, False), (s + 1, True)]


# ---------------------------------------------------------------- checks
checks = []


def check(name, ok, detail=""):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""), flush=True)


eps = mp.mpf(10) ** -40
int4 = {3: 1, 1: 1, -1: 1, -3: 1}
# K0: the electron sigma0 sigma1 sigma0 on 3 strands has ring mass [4]/q^3 (#9789 massE_eq)
m_el = ring_mass([(0, False), (1, False), (0, False)], 3)
check("K0 electron ring mass = [4]/q^3 exactly", m_el == pmul(int4, {-3: 1}), str(sorted(m_el.items())))
# K0b: T / [2]^3 reproduces the convention-D trace tau_e = q^3 (q^4+1)/(q^2+1)^2
tau = peval(T([(0, False), (1, False), (0, False)], 3), q0) / (q0 + 1 / q0) ** 3
check("K0b T/[2]^n is the convention-D trace", abs(tau - q0**3 * (q0**4 + 1) / (q0**2 + 1) ** 2) < eps)

U_e = 3 - pdlog(int4, q0)          # = -q d ln([4]/q^3)
ME = mp.mpf("0.51099895069")       # MeV, comparison only (CAL-1 unit)
hbar = 1 - 1 / q0
E0 = ME / (q0 * (q0 - 1) * (1 - hbar ** 2))   # tower E0, as in the binding-ceiling probes

CASES = [  # (label, A, bond word as V indices); words from PRs #9622 / #9786 audits
    ("2H  V2V3 (cheapest merging, R1)", 2, [2, 3]),
    ("2H  V2V2V2 (junction-only, R2)", 2, [2, 2, 2]),
    ("2H  V2 (single vertex)", 2, [2]),
    ("3H  V2V3V4 (R1 analogue)", 3, [2, 3, 4]),
]
if "--a4" in sys.argv:   # 12 strands; the one A = 4 class that passes reading 3 at q0 (#9786)
    CASES.append(("4He V2V3V4V8 (only q0 passer)", 4, [2, 3, 4, 8]))
rows = []
for label, A, k in CASES:
    n = 3 * A
    x = [(s + 3 * a, i) for a in range(A) for (s, i) in V(0) * 3]
    K = [lt for s in k for lt in V(s)]
    assert writhe(x) == 0 and writhe(K) == 0
    mf, ma = ring_mass(x, n), ring_mass(x + K, n)
    tf, ta = T(x, n), T(x + K, n)
    r_ring = peval(ma, q0) / peval(mf, q0)
    r_raw = peval(ta, q0) / peval(tf, q0)
    B_log = -E0 * mp.log(r_ring)
    dU = pdlog(ma, q0) - pdlog(mf, q0)       # U_free - U_atom
    dU1 = pdlog(ma, mp.mpf(1)) - pdlog(mf, mp.mpf(1))
    rows.append((label, A, r_ring, B_log, dU, dU1, dU / U_e * ME))
    check(f"K1 {label}: framing cancels, ring ratio = raw ratio", abs(r_ring - r_raw) < eps)

print("\nU_e(q0) =", mp.nstr(U_e, 12), "  E0 =", mp.nstr(E0, 12), "MeV")
print(f"{'case':36s} {'-ln r':>12s} {'B_log MeV':>12s} {'dU(q0)':>12s} {'dU(1)':>8s} {'B_U MeV':>12s}")
for label, A, r, bl, du, du1, bu in rows:
    print(f"{label:36s} {mp.nstr(-mp.log(r), 10):>12s} {mp.nstr(bl, 10):>12s} "
          f"{mp.nstr(du, 10):>12s} {mp.nstr(du1, 6):>8s} {mp.nstr(bu, 10):>12s}")

# ---------------------------------------------------------------- beta decay in the energy reading
# #9789: U_n - U_p = +2 exactly, so Delta_np = (2 / U_e) m_e. Q_beta = Delta_np - m_e (nucleon, no binding).
d_np = 2 / U_e * ME
Qb = d_np - ME
print("\nbeta decay (energy reading): Delta_np =", mp.nstr(d_np, 10), "MeV, Q_beta = Delta_np - m_e =",
      mp.nstr(Qb, 10), "MeV  (CODATA 0.78233; comparison only)")
check("K2 Q_beta sign in the energy reading is negative (neutron stable)", Qb < 0, mp.nstr(Qb, 8))

print(f"\n{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
