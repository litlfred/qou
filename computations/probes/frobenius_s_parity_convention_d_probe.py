#!/usr/bin/env python3
"""Frobenius S-parity of Phi_1 under convention D (bean qou-fd2u).

prop:frobenius-s-classification assigned z the S-eigenvalue +1 because
z_C = 1/(q^{1/2} + q^{-1/2}) is invariant under q -> 1/q.  Convention D
(z = q^3/(q^2+1)) is canonical, and z_D is NOT invariant:

    z_D(1/q) = 1/(q (q^2+1)) = z_D(q) - h,   h = q - 1/q.        (*)

WHICH S.  Table 3 of the block maps uu=(1,0) -> (1,-h), dd -> uu, and FIXES
ud = (1,-h/2).  That is consistent only with the Kazhdan-Lusztig bar
involution  q -> 1/q, sigma -> sigma^{-1}  applied to the whole element
X = c sigma + d, coefficients barred too:

    bar(c sigma + d) = c(1/q) sigma + d(1/q) - c(1/q) h(q).

The q-fixed map (c, d) -> (c, d - c h) sends ud to (1, -3h/2), not to itself
(checked below), so it is not the S of Table 3.  On braids, bar is the mirror
sigma_i -> sigma_i^{-1}.  This probe takes S = bar.

WHAT (*) MEANS.  For the Markov functional tr(c sigma + d) = z c + d,
tr(bar X) = bar(tr X) for every X  iff  z(1/q) = z(q) - h(q).  So
  * convention D: tr IS bar-equivariant, and
        Phi_1(S beta; q0) = Phi_1(beta; 1/q0)      (evaluation flip);
  * convention C: z_C is bar-invariant but tr_C is NOT bar-equivariant.
In NEITHER convention is the raw Phi_1 an S-eigenvector at fixed q0.  Table 1's
"+1 (after Frobenius averaging)" is the S-even projection
Phi_1^+ = (Phi_1 + Phi_1 o S)/2, +1 by construction; the remainder
Phi_1^- = (Phi_1 - Phi_1 o S)/2 is a second S-odd channel.

This probe measures Phi_1^- against the chirality term h^2 Phi_3 at the proton
pin.  NO FLOAT64: sympy exact for identities, mpmath (dps 50) for numbers.
No witness is written: the results are identities plus a handful of values,
recorded in bean qou-fd2u.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(50)
from qou_substrate.constants import q_at  # noqa: E402

FAILS = []


def check(name, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- symbolic
qs = sp.symbols("q", positive=True)
hs = qs - 1 / qs
zD = qs**3 / (qs**2 + 1)
zC = sp.sqrt(qs) / (qs + 1)
print("SYMBOLIC (sympy, exact in Q(q))")
check("z_D(1/q) == 1/(q(q^2+1))",
      sp.simplify(zD.subs(qs, 1 / qs) - 1 / (qs * (qs**2 + 1))) == 0)
check("z_D(1/q) == z_D(q) - h", sp.simplify(zD.subs(qs, 1 / qs) - (zD - hs)) == 0)
check("z_C(1/q) == z_C(q)  (C is bar-invariant)",
      sp.simplify(zC.subs(qs, 1 / qs) - zC) == 0)
check("z_C(1/q) != z_C(q) - h  (C trace NOT bar-equivariant)",
      sp.simplify(zC.subs(qs, 1 / qs) - (zC - hs)) != 0)
check("z = q also satisfies z(1/q) = z - h",
      sp.simplify(1 / qs - (qs - hs)) == 0)

SYM_PRIM = {"uu": (sp.Integer(1), sp.Integer(0)),
            "dd": (sp.Integer(1), -hs),
            "ud": (sp.Integer(1), -hs / 2)}


def sbar(cd):
    c, d = cd
    cb, db = c.subs(qs, 1 / qs), d.subs(qs, 1 / qs)
    return (sp.simplify(cb), sp.simplify(db - cb * hs))


def same(u, v):
    return all(sp.simplify(x - y) == 0 for x, y in zip(u, v))


check("bar(uu) == dd", same(sbar(SYM_PRIM["uu"]), SYM_PRIM["dd"]))
check("bar(dd) == uu", same(sbar(SYM_PRIM["dd"]), SYM_PRIM["uu"]))
check("bar(ud) == ud", same(sbar(SYM_PRIM["ud"]), SYM_PRIM["ud"]))
qfix_d = SYM_PRIM["ud"][1] - SYM_PRIM["ud"][0] * hs
check("q-fixed map sends ud to (1,-3h/2), NOT ud  (so S must be bar)",
      sp.simplify(qfix_d + 3 * hs / 2) == 0)

# ---------------------------------------------------------------- numeric
Q0 = q_at(50)


def h(q):
    return q - 1 / q


def z_d(q):
    return q**3 / (q**2 + 1)


def prim(q):
    """Crossing values (c, d) at q.  Quark primitives from Table 3; nucleon and
    electron crossings from wedderburn_mass_table_convention_d.TBL."""
    H = h(q)
    return {("u", "u"): (mp.mpf(1), mp.mpf(0)), ("d", "d"): (mp.mpf(1), -H),
            ("u", "d"): (mp.mpf(1), -H / 2),
            ("p", "p"): (mp.mpf(1), mp.mpf(0)), ("n", "n"): (mp.mpf(1), -H),
            ("p", "n"): (mp.mpf(1), -H / 2), ("e", "e"): (mp.mpf(1), mp.mpf(0)),
            ("p", "e"): (mp.mpf(1), -H), ("n", "e"): (mp.mpf(0), mp.mpf(1))}


def cross(x, y, q, barred=False):
    if barred:
        cb, db = cross(x, y, 1 / q)
        return cb, db - cb * h(q)
    T = prim(q)
    return T[(x, y)] if (x, y) in T else T[(y, x)]


def chain_cd(chain, q):
    H = h(q)
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        a, b = a * (c * H + d) + b * c, a * c + b * d
    return a, b


def invariants(seq, q, z, barred=False):
    p1 = p2 = p3 = mp.mpf(0)
    for i in range(len(seq)):
        ch = [cross(seq[i], seq[j], q, barred) for j in range(i + 1, len(seq))]
        if not ch:
            continue
        c, d = chain_cd(ch, q)
        p1 += mp.log(abs(z * c + d))
        p2 += mp.log(abs(d * (c * h(q) + d) - c * c))
        p3 += mp.log(abs((c * q + d) / (-c / q + d)))
    return p1, p2, p3


print("\nNUMERIC (mpmath dps 50, proton pin)")
print(f"  q0          = {mp.nstr(Q0, 20)}")
print(f"  z_D(q0)     = {mp.nstr(z_d(Q0), 20)}")
print(f"  z_D(1/q0)   = {mp.nstr(z_d(1 / Q0), 20)}")
print(f"  z_D - h     = {mp.nstr(z_d(Q0) - h(Q0), 20)}")
check("(*) at q0: |z_D(1/q0) - (z_D - h)| < 1e-45",
      abs(z_d(1 / Q0) - (z_d(Q0) - h(Q0))) < mp.mpf(10) ** -45)

CASES = [
    ("proton  (quarks uud)", list("uud")),
    ("neutron (quarks udd)", list("udd")),
    ("2H nucleus (pn)", list("pn")),
    ("3He nucleus (ppn)", list("ppn")),
    ("4He nucleus (ppnn)", list("ppnn")),
    ("2H atom (e p n)", list("epn")),
    ("4He atom (e p e p n n)", list("epepnn")),
]
H0 = h(Q0)
print(f"\n  {'chain':<26}{'Phi1':>13}{'Phi1(S)':>13}{'Phi1^-':>13}"
      f"{'h^2 Phi3':>13}{'Phi2S-Phi2':>12}{'Phi3+Phi3S':>12}")
for name, seq in CASES:
    p1, p2, p3 = invariants(seq, Q0, z_d(Q0))
    s1, s2, s3 = invariants(seq, Q0, z_d(Q0), barred=True)
    f1, _, _ = invariants(seq, 1 / Q0, z_d(1 / Q0))
    odd = (p1 - s1) / 2
    print(f"  {name:<26}{mp.nstr(p1, 8):>13}{mp.nstr(s1, 8):>13}{mp.nstr(odd, 6):>13}"
          f"{mp.nstr(H0**2 * p3, 6):>13}{mp.nstr(s2 - p2, 3):>12}{mp.nstr(p3 + s3, 3):>12}")
    check(f"{name}: Phi_1(S beta; q0) == Phi_1(beta; 1/q0)",
          abs(s1 - f1) < mp.mpf(10) ** -40)

pp1, _, pp3 = invariants(list("uud"), Q0, z_d(Q0))
ps1, _, _ = invariants(list("uud"), Q0, z_d(Q0), barred=True)
nn1, _, _ = invariants(list("ddu"), Q0, z_d(Q0))
check("quark mirror: Phi_1 of S(uud) == Phi_1 of ddu",
      abs(ps1 - nn1) < mp.mpf(10) ** -40)
odd_p = (pp1 - ps1) / 2
print("\n  m(S beta) - m(beta) = -2 alpha (Phi1^- + h^2 Phi3)   [Phi2 S-even]")
print(f"    proton uud: Phi1^-        = {mp.nstr(odd_p, 15)}")
print(f"    proton uud: h^2 Phi3      = {mp.nstr(H0**2 * pp3, 15)}")
print(f"    ratio Phi1^- / (h^2 Phi3) = {mp.nstr(odd_p / (H0**2 * pp3), 10)}")

zc = mp.sqrt(Q0) / (Q0 + 1)
c1, _, _ = invariants(list("uud"), Q0, zc)
cs1, _, _ = invariants(list("uud"), Q0, zc, barred=True)
fc1, _, _ = invariants(list("uud"), 1 / Q0, mp.sqrt(1 / Q0) / (1 / Q0 + 1))
print(f"\n  CONTRAST, excised C, uud: Phi1 = {mp.nstr(c1, 10)},"
      f" Phi1(S) = {mp.nstr(cs1, 10)}, Phi1^- = {mp.nstr((c1 - cs1) / 2, 10)}")
check("C: Phi_1(S beta; q0) != Phi_1(beta; 1/q0)  (no evaluation flip)",
      abs(cs1 - fc1) > mp.mpf(10) ** -10)

print(f"\n{len(FAILS)} FAIL(S)" if FAILS else "\nALL CHECKS PASS")
sys.exit(1 if FAILS else 0)
