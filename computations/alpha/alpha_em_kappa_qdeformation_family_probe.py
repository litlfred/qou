#!/usr/bin/env python3
"""Enumerate the q-deformation family of the CS Gram determinant ratio kappa.

`prop:em-coupling-chern-simons` predicts 1/alpha_EM with a Gram-determinant
ratio `kappa = det G_cl / det G_q` and is explicit that its own construction is
underdetermined:

    "The Gram matrix is dimensionally ambiguous. The choice of basis for the
     rank-2 sublattice and the explicit form of s_i, ell, c_i in the
     q-deformed setting are not fixed."

The shipped producer (`meson_em_sinh_closed_form._alpha_em_inv_derived`) fixes
them one way and gets kappa = 1.7216, leaving a -467 ppb residual; the block
records that an exact match needs kappa ~ 1.9153, an 11.2% gap.

The `.md` names two candidate causes and excludes one (the truncation, worth
11.07 ppb against a 468 ppb gap), leaving "a wrong Gram-determinant
identification of kappa" -- but nothing has tested WHICH identification.

That is testable rather than open-ended, because the ambiguity is FINITE.  The
Gram entries are built from four composite quantities, and the instruction
"replace m,n with [m]_q,[n]_q" has exactly two natural readings for each --
deform the composite, or deform its constituents:

  s  self-linking (m-1)(n-1)   : ([m]_q-1)([n]_q-1)         vs [m-1]_q[n-1]_q
  l  linking |m1 n2 - m2 n1|   : |[m1]_q[n2]_q-[m2]_q[n1]_q| vs [17]_q
  c  crossing product m n      : [m]_q[n]_q                  vs [m n]_q
  CS pi^2(m^2-1)(n^2-1)/(12mn) : q-deformed                  vs left classical

16 combinations, of which the producer is one.  This is a structural prune in
the sense of AGENTS.md "Formalize-first probe discipline": a finite,
structurally-motivated family, enumerated rather than searched.  Its caveat
applies -- the probe is cheap and decisive, so it is run rather than formalised.

IT IS NOT A FIT.  No parameter is tuned; 16 fixed readings are evaluated and
reported.  A reading is reported as landing only if it independently reaches
the window, and "none lands" is the informative outcome: it would mean the
whole `[m]_q` substitution family cannot supply the needed kappa, promoting the
block's own alternative hypothesis -- "the entire ansatz uses the wrong
decomposition" -- from speculation to a measured conclusion.

The basis choice for the rank-2 sublattice is the block's OTHER named
ambiguity, and it is NOT a source of freedom at all: a Gram matrix transforms by
congruence G -> B^T G B, det picks up (det B)^2, and that factor is the SAME on
both sides of the ratio, so it cancels.  kappa is basis-independent for ANY
invertible B -- unimodular, non-unimodular, or irrational.  Proved sorry-free in
`QOU/Archimedean/GramDetRatioCongruence.lean` and checked numerically below to
60 digits.  (I first wrote the opposite here, that det G is not invariant.  It
is the ratio that is invariant, and the block lists the basis as an open
ambiguity on the same mistaken reading.)

So the two named ambiguities reduce to one, and this probe enumerates it
exhaustively.  What a null result does NOT exclude is a DIFFERENT pairing --
different matrix entries, not a different reading of these ones -- which is the
block's own third alternative ("the entire ansatz uses the wrong
decomposition").

Precision: mpmath end to end at 50 dps, no float64 anywhere (AGENTS.md
"PROBES ARE NOT EXEMPT").

Run:  python3 -u computations/alpha/alpha_em_kappa_qdeformation_family_probe.py
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# The corpus precision entry point rather than a bare `mp.dps` assignment --
# idempotent, and what `never_raises_dps_audit.py` looks for.
set_compute_dps()

Q = Q_MP

# CODATA-2022, as quoted by the block itself.  Read, not derived.
CODATA_ALPHA_INV = mp.mpf("137.035999177")
CODATA_ALPHA_INV_ERR = mp.mpf("0.000000021")

# The two force-carrier torus knots, T_{m,n}.
KNOTS = ((2, 9), (3, 5))


def q_int(k, q):
    """[k]_q, matching `meson_em_sinh_closed_form.q_int` exactly."""
    return (q**k - q ** (-k)) / (q - 1 / q)


def cs_classical(m, n):
    """CS(T_{m,n}) = pi^2 (m^2-1)(n^2-1) / (12 m n), integer m, n."""
    m, n = mp.mpf(m), mp.mpf(n)
    return mp.pi**2 * (m**2 - 1) * (n**2 - 1) / (12 * m * n)


def cs_deformed(m, n, q):
    """Same expression with m,n -> [m]_q,[n]_q."""
    qm, qn = q_int(m, q), q_int(n, q)
    return mp.pi**2 * (qm**2 - 1) * (qn**2 - 1) / (12 * qm * qn)


def gram_det(q, *, s_mode, l_mode, c_mode, cs_mode, classical):
    """det of the 2x2 CS Gram matrix under one reading of the four composites.

    `classical=True` builds the undeformed matrix (all modes ignored, which is
    why det_cl is identical across the family and only det_q moves).
    """
    if classical:
        cs = [cs_classical(m, n) for m, n in KNOTS]
        s = [mp.mpf((m - 1) * (n - 1)) for m, n in KNOTS]
        c = [mp.mpf(m * n) for m, n in KNOTS]
        ell = mp.mpf(abs(KNOTS[0][0] * KNOTS[1][1] - KNOTS[1][0] * KNOTS[0][1]))
    else:
        if cs_mode == "deformed":
            cs = [cs_deformed(m, n, q) for m, n in KNOTS]
        else:
            cs = [cs_classical(m, n) for m, n in KNOTS]

        if s_mode == "constituents":          # ([m]_q - 1)([n]_q - 1)
            s = [(q_int(m, q) - 1) * (q_int(n, q) - 1) for m, n in KNOTS]
        else:                                  # [m-1]_q [n-1]_q
            s = [q_int(m - 1, q) * q_int(n - 1, q) for m, n in KNOTS]

        if c_mode == "constituents":           # [m]_q [n]_q
            c = [q_int(m, q) * q_int(n, q) for m, n in KNOTS]
        else:                                  # [m n]_q
            c = [q_int(m * n, q) for m, n in KNOTS]

        if l_mode == "constituents":           # |[m1]_q[n2]_q - [m2]_q[n1]_q|
            ell = abs(q_int(KNOTS[0][0], q) * q_int(KNOTS[1][1], q)
                      - q_int(KNOTS[1][0], q) * q_int(KNOTS[0][1], q))
        else:                                  # [17]_q
            ell = q_int(abs(KNOTS[0][0] * KNOTS[1][1]
                            - KNOTS[1][0] * KNOTS[0][1]), q)

    g11 = cs[0] + mp.pi**2 * s[0] ** 2 / c[0] ** 2
    g22 = cs[1] + mp.pi**2 * s[1] ** 2 / c[1] ** 2
    g12 = mp.pi**2 * ell**2 / (c[0] * c[1])
    return g11 * g22 - g12**2


def _gram_matrix(q, *, classical):
    """The shipped reading's 2x2 matrix itself, for the basis-invariance check.

    Only the shipped q-reading is needed here: the invariance is a fact about
    congruence, not about which reading built the entries.
    """
    if classical:
        cs = [cs_classical(m, n) for m, n in KNOTS]
        s = [mp.mpf((m - 1) * (n - 1)) for m, n in KNOTS]
        c = [mp.mpf(m * n) for m, n in KNOTS]
        ell = mp.mpf(abs(KNOTS[0][0] * KNOTS[1][1] - KNOTS[1][0] * KNOTS[0][1]))
    else:
        cs = [cs_deformed(m, n, q) for m, n in KNOTS]
        s = [(q_int(m, q) - 1) * (q_int(n, q) - 1) for m, n in KNOTS]
        c = [q_int(m, q) * q_int(n, q) for m, n in KNOTS]
        ell = abs(q_int(KNOTS[0][0], q) * q_int(KNOTS[1][1], q)
                  - q_int(KNOTS[1][0], q) * q_int(KNOTS[0][1], q))
    g11 = cs[0] + mp.pi**2 * s[0] ** 2 / c[0] ** 2
    g22 = cs[1] + mp.pi**2 * s[1] ** 2 / c[1] ** 2
    g12 = mp.pi**2 * ell**2 / (c[0] * c[1])
    return mp.matrix([[g11, g12], [g12, g22]])


def alpha_inv(q, kappa):
    """The block's live resummed form at a given kappa."""
    bare = q * q_int(9, q) * q_int(10, q)
    cs_sum = cs_classical(2, 9) + cs_classical(3, 5)
    hbar_q_sq = (1 - 1 / q) ** 2
    delta = cs_sum * (q_int(2, q) / 2) * hbar_q_sq / bare
    return bare * (1 + delta / (1 - delta * kappa))


def kappa_for_target(q, target):
    """Invert the resummed form for kappa.  Used ONLY to report what the data
    would require -- never as an input to any reading."""
    bare = q * q_int(9, q) * q_int(10, q)
    cs_sum = cs_classical(2, 9) + cs_classical(3, 5)
    delta = cs_sum * (q_int(2, q) / 2) * (1 - 1 / q) ** 2 / bare
    r = target / bare - 1                       # = delta/(1 - delta*kappa)
    return (1 - delta / r) / delta


def ppb(x, ref):
    return (x / ref - 1) * mp.mpf(10) ** 9


def main() -> int:
    q = Q
    print(f"q0 (proton pin)     : {mp.nstr(q, 20)}")
    print(f"CODATA-2022 1/alpha : {mp.nstr(CODATA_ALPHA_INV, 15)}"
          f"  (+/- {mp.nstr(CODATA_ALPHA_INV_ERR, 3)})")

    kappa_needed = kappa_for_target(q, CODATA_ALPHA_INV)
    lo = kappa_for_target(q, CODATA_ALPHA_INV * (1 - mp.mpf(100) / 10**9))
    hi = kappa_for_target(q, CODATA_ALPHA_INV * (1 + mp.mpf(100) / 10**9))
    k_lo, k_hi = (lo, hi) if lo < hi else (hi, lo)
    print(f"kappa for exact match : {mp.nstr(kappa_needed, 12)}")
    print(f"|err| < 100 ppb window: [{mp.nstr(k_lo, 10)}, {mp.nstr(k_hi, 10)}]"
          f"   width {mp.nstr(k_hi - k_lo, 6)}")

    det_cl = gram_det(q, s_mode=None, l_mode=None, c_mode=None, cs_mode=None,
                      classical=True)
    print(f"det G_cl              : {mp.nstr(det_cl, 15)}")

    # Basis invariance, numerically -- the companion to the Lean proof in
    # QOU/Archimedean/GramDetRatioCongruence.lean.  Three deliberately
    # different B: unimodular, non-unimodular (index 2), and irrational.
    det_q0 = gram_det(q, s_mode="constituents", l_mode="constituents",
                      c_mode="constituents", cs_mode="deformed",
                      classical=False)
    g_cl = _gram_matrix(q, classical=True)
    g_q = _gram_matrix(q, classical=False)
    k0 = det_cl / det_q0
    print("basis-invariance check (kappa under a common congruence B):")
    for name, B in (
        ("unimodular  [[1,1],[0,1]]", mp.matrix([[1, 1], [0, 1]])),
        ("index-2     [[2,0],[0,1]]", mp.matrix([[2, 0], [0, 1]])),
        ("irrational  [[pi,1],[1,e]]", mp.matrix([[mp.pi, 1], [1, mp.e]])),
    ):
        kb = mp.det(B.T * g_cl * B) / mp.det(B.T * g_q * B)
        print(f"  {name:26s} -> {mp.nstr(kb, 20)}  "
              f"rel-diff {mp.nstr(abs(kb - k0) / k0, 4)}")
    print()

    modes = list(itertools.product(
        ("constituents", "composite"),   # s
        ("constituents", "composite"),   # l
        ("constituents", "composite"),   # c
        ("deformed", "classical"),       # CS
    ))

    print(f"{'s':>13} {'l':>13} {'c':>13} {'CS':>10} "
          f"{'kappa':>14} {'1/alpha':>18} {'ppb':>12}  in?")
    print("-" * 100)

    rows, landed = [], []
    for s_m, l_m, c_m, cs_m in modes:
        det_q = gram_det(q, s_mode=s_m, l_mode=l_m, c_mode=c_m, cs_mode=cs_m,
                         classical=False)
        if det_q == 0:
            print(f"{s_m:>13} {l_m:>13} {c_m:>13} {cs_m:>10} "
                  f"{'SINGULAR det_q':>14}")
            continue
        kappa = det_cl / det_q
        a = alpha_inv(q, kappa)
        err = ppb(a, CODATA_ALPHA_INV)
        inside = k_lo <= kappa <= k_hi
        is_shipped = (s_m, l_m, c_m, cs_m) == ("constituents", "constituents",
                                               "constituents", "deformed")
        mark = "YES" if inside else ""
        tag = "  <- shipped" if is_shipped else ""
        print(f"{s_m:>13} {l_m:>13} {c_m:>13} {cs_m:>10} "
              f"{mp.nstr(kappa, 10):>14} {mp.nstr(a, 13):>18} "
              f"{mp.nstr(err, 7):>12}  {mark}{tag}")
        rows.append((s_m, l_m, c_m, cs_m, kappa, a, err))
        if inside:
            landed.append((s_m, l_m, c_m, cs_m, kappa, err))

    print("-" * 100)

    # Cross-check: the shipped reading must reproduce the producer exactly.
    from meson_em_sinh_closed_form import _alpha_em_inv_derived  # noqa: E402
    shipped = [r for r in rows
               if (r[0], r[1], r[2], r[3])
               == ("constituents", "constituents", "constituents", "deformed")]
    if shipped:
        mine = shipped[0][5]
        theirs = _alpha_em_inv_derived(q)
        rel = abs(mine - theirs) / theirs
        ok = rel < mp.mpf(10) ** -40
        print(f"\ncross-check vs shipped producer: rel diff "
              f"{mp.nstr(rel, 4)}  -> {'MATCH' if ok else 'MISMATCH'}")
        if not ok:
            print("  the enumeration does not reproduce the producer; every "
                  "row above is about this script, not the corpus.")
            return 1

    ks = sorted(r[4] for r in rows)
    print(f"\nreadings evaluated : {len(rows)}")
    print(f"kappa range        : [{mp.nstr(ks[0], 10)}, {mp.nstr(ks[-1], 10)}]")
    print(f"needed             : {mp.nstr(kappa_needed, 10)}")
    print(f"landing in window  : {len(landed)}")

    if landed:
        print("\nreadings that land:")
        for s_m, l_m, c_m, cs_m, kappa, err in landed:
            print(f"  s={s_m} l={l_m} c={c_m} CS={cs_m}  "
                  f"kappa={mp.nstr(kappa, 10)}  {mp.nstr(err, 6)} ppb")
    else:
        above = sum(1 for r in rows if r[4] > k_hi)
        below = sum(1 for r in rows if r[4] < k_lo)
        print("\nNONE of the readings lands.")
        print(f"  {below} fall below the window, {above} above.")
        print("  Scope: a scope-(a) negative in the AGENTS.md sense -- the")
        print("  [m]_q substitution family, ALONE, does not supply the kappa")
        print("  the block needs.  Since the basis choice is proved not to")
        print("  move kappa (see the basis check above), this exhausts BOTH")
        print("  ambiguities the block names.  It does NOT exclude a")
        print("  Gram-determinant kappa in general: a different PAIRING --")
        print("  different entries, not a different reading of these -- is")
        print("  untouched, and is the block's own remaining alternative.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
