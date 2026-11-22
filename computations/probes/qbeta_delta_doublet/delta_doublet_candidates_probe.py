#!/usr/bin/env python3
"""qou-99qc: Q_beta candidates from the four-strand left doublet, under convention D.

Bean qou-99qc (which element is Delta = n - p), epic qou-wxhi (issue #7939).

Pre-registered before any run (2026-11-15):
  * Candidates are taken as GIVEN from the four-strand doublet thread
    (branch claude/n4-left-flavour-doublet-2026-11-15, probe
    n4_left_doublet_flavour_probe.py): chirality = sigma_1 q-line; two flavour
    labels on that left line,
        label A: sigma_3 eigenlines,  X = P+(s1) P+(s3), Y = P+(s1) P-(s3);
        label B: J_4 eigenlines,      X = P+(s1) E_{J4=q^-2}, Y = P+(s1) E_{J4=q^4},
    J_4 = s3 s2 s1 s1 s2 s3; and the reading-3 passing gamma-gamma words of the
    SM thread (m = 3: 000, 111; m = 4: 0101, 1010, every V / Vb orientation).
  * For each (label, word W): p-state X W X, n-state Y W Y, Delta = Y W Y - X W X.
    |eps| is invariant under swapping which state is n, so the open n/p labelling
    does not enter.
  * eps = the ruled functional: Markov trace at z_D = q^3/(q^2+1), i.e.
    sum over two-row lambda |- 4 of y_lambda chi_lambda (three-row y_lambda = 0).
  * Reported per candidate: Q = |eps| E_0, residual vs CODATA, and the ladder
    factor F_required = Q_codata / Q. NOTHING IS SELECTED by residual or by F.
  * Reading 3 (chi_mu >= 0 on every block with y_mu > 0, at strand counts m = 3
    and 4) is reported for the p-state and n-state separately.
  * Calibration: the H_3 ruled base |h^2/2 - h z_D| E_0 = 0.444700408522 MeV
    must be reproduced from the same E_0 and z_D, or the run is void.

Exact over Q(q) (sympy), evaluated at the proton pin with mpmath at 60 dps.
No float arithmetic. No witness file (probe).
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gg_ntower"))
import gg_ntower_probe as g  # noqa: E402

mp.mp.dps = 60
q, K = g.q, g.K
Q0 = mp.mpf(g.Q_50_DIGIT_STR)
ME = mp.mpf("0.51099895069")            # CODATA 2022 m_e, MeV (string literal)
QB_CODATA = mp.mpf("0.78233341")       # m_n - m_p - m_e, MeV (as the corpus quotes it)
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(ME, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
SHAPES = g.two_row_shapes(4)           # (4,0), (3,1), (2,2)

ok = True


def check(name, cond):
    global ok
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    ok &= bool(cond)


def at_q0(f):
    return mp.mpf(str(sp.N(sp.sympify(f).subs(q, g.Q0_RAT), 80)))


def ks(x):
    return K.from_sympy(sp.cancel(sp.sympify(x)))


class Alg:
    """An element of H_4(q) seen through its two-row seminormal blocks."""

    def __init__(self, blocks):
        self.b = blocks

    def __mul__(self, o):
        return Alg({lam: self.b[lam] * o.b[lam] for lam in SHAPES})

    def __sub__(self, o):
        return Alg({lam: self.b[lam] - o.b[lam] for lam in SHAPES})

    def __add__(self, o):
        return Alg({lam: self.b[lam] + o.b[lam] for lam in SHAPES})

    def scale(self, c):
        return Alg({lam: self.b[lam] * ks(c) for lam in SHAPES})


def gen(i, e=1):
    return Alg({lam: g.rep(lam).letter(i, e) for lam in SHAPES})


ONE = Alg({lam: g.rep(lam).eye for lam in SHAPES})


def P_plus(i):
    return (gen(i) + ONE.scale(1 / q)).scale(1 / (q + 1 / q))


def P_minus(i):
    return (ONE.scale(q) - gen(i)).scale(1 / (q + 1 / q))


def spectral(X, lam_target, others):
    """Projector onto the lam_target eigenspace of X, given the full eigenvalue list."""
    P = ONE
    for mu in others:
        P = (P * (X - ONE.scale(mu))).scale(1 / (lam_target - mu))
    return P


def char(x, lam):
    return g.tr(x.b[lam])


def eps(x):
    return sp.cancel(sum(g.y_lambda(lam) * char(x, lam) for lam in SHAPES))


def level3_chars(x):
    out = {}
    for mu in g.two_row_shapes(3):
        acc = sp.Integer(0)
        for lam in SHAPES:
            R = g.rep(lam)
            s = sum(K.to_sympy(x.b[lam][i, i].element)
                    for i, T in enumerate(R.basis) if (3 - sum(T[:3]), sum(T[:3])) == mu)
            acc += g.y_lambda(lam) / g.y_lambda(mu) * s
        out[(3, mu)] = sp.cancel(acc)
    for lam in SHAPES:
        out[(4, lam)] = char(x, lam)
    return out


def reading3(x):
    """True iff every chi with y > 0 is >= 0 at q0 (levels 3 and 4)."""
    bad = []
    for key, f in level3_chars(x).items():
        v = at_q0(f)
        if v < -mp.mpf(10) ** -40:
            bad.append(f"{key[0]}:{key[1]}={mp.nstr(v, 6)}")
    return bad


def vertex(site, mirror):
    a, b = site, site + 1
    return gen(a, -1) * gen(b) if mirror else gen(a) * gen(b, -1)


def main():
    h = q - 1 / q
    zD = q**3 / (q**2 + 1)
    print("0. calibration")
    base = abs(at_q0(h**2 / 2 - h * zD)) * E0
    print(f"  H_3 ruled base = {mp.nstr(base, 15)} MeV")
    check("reproduces 0.444700408522", abs(base - mp.mpf("0.444700408522")) < mp.mpf("1e-11"))
    check("eps(1) = 1", sp.simplify(eps(ONE) - 1) == 0)
    check("eps(s3 x) = z_D eps(x) on x = s1 s2",
          sp.simplify(eps(gen(0) * gen(1) * gen(2)) - zD * eps(gen(0) * gen(1))) == 0)

    check("control: reading 3 rejects -1", bool(reading3(ONE.scale(-1))))
    check("control: reading 3 accepts 1", not reading3(ONE))
    J4 = gen(2) * gen(1) * gen(0) * gen(0) * gen(1) * gen(2)
    # J4 eigenvalues on two-row blocks of H_4: q^{2c(box 4)} = q^6, q^-2, q^4, q^0
    ev = [q**6, q**-2, q**4, sp.Integer(1)]
    Ea = spectral(J4, q**-2, [e for e in ev if e != q**-2])
    Eb = spectral(J4, q**4, [e for e in ev if e != q**4])
    PL = P_plus(0)
    labels = {
        "A": (PL * P_plus(2), PL * P_minus(2)),
        "B": (PL * Ea, PL * Eb),
    }
    for lab, (X, Y) in labels.items():
        check(f"label {lab}: X, Y idempotent, orthogonal, nonzero",
              all(M.b[lam].is_zero_matrix
                  for M in [(X * X - X), (Y * Y - Y), (X * Y), (Y * X)] for lam in SHAPES)
              and any(not X.b[lam].is_zero_matrix for lam in SHAPES)
              and any(not Y.b[lam].is_zero_matrix for lam in SHAPES))
        # both states inside sigma_1's left line: X (1 - P+(s1)) = 0
        check(f"label {lab}: X, Y on sigma_1's left line",
              all((X * (ONE - PL)).b[lam].is_zero_matrix and (Y * (ONE - PL)).b[lam].is_zero_matrix
                  for lam in SHAPES))

    patterns = {3: ["000", "111"], 4: ["0101", "1010"]}
    rows = []
    for m, pats in patterns.items():
        for pat in pats:
            for orient in itertools.product([0, 1], repeat=m):
                W = ONE
                for c, o in zip(pat, orient):
                    W = W * vertex(int(c), o)
                name = ".".join(("Vb" if o else "V") + c for c, o in zip(pat, orient))
                for lab, (X, Y) in labels.items():
                    p = X * W * X
                    n = Y * W * Y
                    d = sp.factor(sp.cancel(eps(n) - eps(p)))
                    v = abs(at_q0(d))
                    Qv = v * E0
                    rows.append({
                        "word": name, "label": lab, "eps_delta": d,
                        "Q": Qv,
                        "resid_pct": (Qv / QB_CODATA - 1) * 100 if Qv else None,
                        "F": QB_CODATA / Qv if Qv else None,
                        "r3_p": reading3(p), "r3_n": reading3(n),
                    })
    print("1. candidates: Delta = YWY - XWX, eps at z_D, Q = |eps| E_0")
    print(f"  {'word':20s} lab {'Q (MeV)':>14s} {'resid %':>10s} {'F_req':>10s}  reading3 p / n")
    for r in rows:
        if r["Q"] == 0:
            print(f"  {r['word']:20s} {r['label']}   eps(Delta) = 0 identically or at q0")
            continue
        r3 = ("pass" if not r["r3_p"] else "FAIL " + ",".join(r["r3_p"])) + " / " + \
             ("pass" if not r["r3_n"] else "FAIL " + ",".join(r["r3_n"]))
        print(f"  {r['word']:20s} {r['label']}  {mp.nstr(r['Q'], 10):>14s} "
              f"{mp.nstr(r['resid_pct'], 6):>10s} {mp.nstr(r['F'], 8):>10s}  {r3}")
    print("1b. range per label (post hoc summary, not a selection)")
    for lab in labels:
        qs = [r["Q"] for r in rows if r["label"] == lab]
        nz = [x for x in qs if x != 0]
        print(f"  label {lab}: {len(qs)} candidates, {len(qs) - len(nz)} with eps = 0, "
              f"Q in [{mp.nstr(min(nz), 8)}, {mp.nstr(max(nz), 8)}] MeV vs CODATA {QB_CODATA}")
    r3fail = [r for r in rows if r["r3_p"] or r["r3_n"]]
    print(f"  reading-3 failures among p/n states: {len(r3fail)}")
    print("2. distinct |eps(Delta)| values (exact)")
    seen = {}
    for r in rows:
        key = sp.factor(sp.Abs(r["eps_delta"])) if r["eps_delta"] != 0 else 0
        seen.setdefault(str(sp.factor(r["eps_delta"] ** 2)), []).append(f"{r['label']}:{r['word']}")
    for k, v in seen.items():
        print(f"  eps^2 = {k}\n     <- {len(v)} candidates, e.g. {v[:3]}")
    print("ALL PASS" if ok else "SOME FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
