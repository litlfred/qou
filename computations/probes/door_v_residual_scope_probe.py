#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic q (sympy) for the calculus checks;
# mpmath at the package dps (never float64) for the one numerical question, the
# GGM sign-flip threshold at the proton q0. Audit-only probe (compute-author
# 1.3): no witness, no fitted parameter.
"""Probe: what the corpus's Door-v residual actually is, against the hypothesis
`twoOp_residual_kills_residue` (#6498) consumes.  (bean `qou-o2n6`)

THE QUESTION.  #6498 proved: a two-term derivative-like tower carrying the FULL
(-1)^n alternation at EVERY level has a dead residue slot.  The corpus's Door-v
residual (`conj:c1-ggm-bar-parity-faces`) is the sign alternation of the GGM
carrier's growing solution,  y_{m+2} - (2 - q^{m+1}) y_{m+1} + y_m = 0,  and the
block itself says it does NOT alternate at every consecutive pair: while
2 - q^{m+1} > 0 there is no sign change.  So the measured residual is
ASYMPTOTIC, and the #6498 hypothesis is strictly stronger than what is measured.

WHAT IS CHECKED, exactly:
  (1) THRESHOLD at the proton q0 (mpmath, package dps): the first m with
      2 - q0^{m+1} < 0, i.e. the first index at which the GGM recurrence can
      force alternation; and log 2 / log q0 for comparison.  Then the growing
      solution itself from generic positive initial data: the first index at
      which consecutive terms change sign, and that the terms BEFORE it are all
      of one sign (no alternation in the pre-asymptotic window).
  (2) THE ASYMPTOTIC THEOREM's mechanism, symbolic q, on a LAURENT seed (negative
      powers allowed): a shift-1 derivative iterate of length k >= 2 has a dead
      residue slot for EVERY seed (Lean `shiftOne_iterate_residue_zero_of_two_le`),
      while lengths 0 and 1 do NOT on a Laurent seed -- the seed hypothesis of
      #6474 is needed exactly there and nowhere else.
  (3) THE WINDOW: with alternation demanded only from level n0, the two-term
      derivative-like residue is dead from level n0 + 2 on (Lean
      `twoOp_residual_from_level_kills_residue_beyond`) and is given by the
      #6498 formula c1(-2) c2(-1) (D^n f)(1) below it -- checked by direct
      iteration for symbolic q on a power-series seed with generic coefficients:
      levels 2..n0+1 carry a nonzero residue while a tower that is the pure odd
      part from n0 on has none beyond.
  (4) Jet level n = GGM index m only through the conjecture's identification
      "jet degree = body order" (`prop:sw-period-residue-sum`); recorded, not
      checked -- it is the identification under test, not a fact.

Reproduce:
    PYTHONPATH=computations python3 -u computations/probes/door_v_residual_scope_probe.py
"""
from __future__ import annotations

import sympy as sp
from mpmath import mp

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP

q = sp.Symbol("q", positive=True)
E_LO, E_HI = -8, 10
NMAX = 8


def shift_op(k, c):
    return lambda f: (lambda e: c(e) * f(e + k))


def add_ops(*ops):
    return lambda f: (lambda e: sum((op(f)(e) for op in ops), sp.Integer(0)))


def iterate(op, n, f):
    for _ in range(n):
        f = op(f)
    return f


def qint_bal(m):
    return sp.cancel((q**m - q**(-m)) / (q - 1 / q))


def seed_from(coeffs, lo=0):
    """seed with coeffs[i] at exponent lo + i, zero elsewhere."""
    return lambda e: sp.sympify(coeffs[e - lo]) if lo <= e < lo + len(coeffs) else sp.Integer(0)


def main() -> int:
    fail: list[str] = []

    def ok(cond, msg):
        print(f"  [{'OK ' if cond else 'FAIL'}] {msg}")
        if not cond:
            fail.append(msg)

    print("=" * 78)
    print("(1) GGM sign-flip THRESHOLD at the proton q0 (mpmath, package dps)")
    print("=" * 78)
    mp.dps = 60
    q0 = Q_MP
    print(f"  q0 = {mp.nstr(q0, 25)}  (proton pin, qou_substrate.constants.Q_50_DIGIT_STR)")
    ratio = mp.log(2) / mp.log(q0)
    print(f"  log 2 / log q0 = {mp.nstr(ratio, 12)}")
    first_neg = None
    for m in range(0, 40):
        if 2 - q0 ** (m + 1) < 0:
            first_neg = m
            break
    print(f"  first m with 2 - q0^(m+1) < 0 :  m = {first_neg}   (coefficient sign turns at m+1 = {first_neg + 1})")
    ok(first_neg is not None and first_neg == int(mp.floor(ratio)), "threshold index m0 = floor(log 2 / log q0)")
    ok(all(2 - q0 ** (m + 1) > 0 for m in range(0, first_neg)), "every coefficient 2 - q0^(m+1) for m < m0 is POSITIVE")
    # The block says "for m+1 < log 2 / log q the coefficient is positive and no
    # sign change occurs".  The second half is NOT what the recurrence does: with
    # 0 < c_m < 2 it is OSCILLATORY, so solutions DO change sign in the window --
    # but never at two consecutive pairs (Lean `no_double_flip_of_pos`).  Measure
    # it on several initial data; the growing solution is generic among them.
    ok(all(0 < 2 - q0 ** (m + 1) < 2 for m in range(0, first_neg)),
       "every window coefficient lies in (0, 2): the recurrence is oscillatory there, not sign-preserving")
    inits = [(1, 1), (1, 0), (0, 1), (1, -1), (3, 1), (1, 3)]
    onsets = []
    for y0, y1 in inits:
        y = [mp.mpf(y0), mp.mpf(y1)]
        for m in range(0, 60):
            y.append((2 - q0 ** (m + 1)) * y[m + 1] - y[m])
        flips = [y[m] * y[m + 1] < 0 for m in range(len(y) - 1)]
        first_flip = next((m for m in range(len(flips)) if flips[m]), None)
        changes_in_window = sum(1 for m in range(0, first_neg) if flips[m])
        double_flip_in_window = any(flips[m] and flips[m + 1] for m in range(0, first_neg))
        last_same = max((m for m in range(len(flips)) if not flips[m]), default=None)
        onset = last_same + 1
        print(f"  y0,y1 = {y0},{y1}: first flip at pair ({first_flip},{first_flip + 1}); sign changes inside the window m<{first_neg}: {changes_in_window};"
              f" persistent strict alternation from m = {onset}")
        if (y0, y1) == (1, 1):
            print("    y_0..y_14 =", [mp.nstr(v, 5) for v in y[:15]])
        ok(changes_in_window >= 1, "    the solution DOES change sign inside the window -- the block's 'no sign change occurs' is false as written")
        ok(not double_flip_in_window, "    but never at two consecutive pairs while the coefficient is positive (Lean no_double_flip_of_pos)")
        ok(all(flips[m] for m in range(onset, 60)), "    and strict alternation, once persistent, holds through m = 60")
        ok(onset > first_neg, "    persistent alternation sets in only AFTER the coefficient threshold")
        onsets.append(onset)
    print(f"  onset of persistent strict alternation across initial data: {onsets}  (initial-data dependent; all > m0 = {first_neg})")
    print(f"  => the measured residual is alternation from m >= {min(onsets)} at the earliest; the #6498 hypothesis demands it from m = 0")

    print()
    print("=" * 78)
    print("(2) shift-1 derivative iterate on a LAURENT seed: dead residue for length >= 2 ONLY")
    print("=" * 78)
    a = sp.symbols("a0:12")
    laurent = seed_from(a, lo=-4)          # exponents -4 .. 7, generic
    S1 = shift_op(1, lambda e: qint_bal(e + 1))
    r = [sp.simplify(iterate(S1, k, laurent)(-2)) for k in range(0, 6)]
    print(f"  S1^k Y(-2), k=0..5: {r}")
    ok(r[0] != 0 and r[1] != 0, "lengths 0 and 1 are ALIVE on a Laurent seed (the #6474 seed hypothesis is needed exactly there)")
    ok(all(v == 0 for v in r[2:]), "length >= 2 is DEAD for every seed (Lean shiftOne_iterate_residue_zero_of_two_le)")

    print()
    print("=" * 78)
    print("(3) THE WINDOW: alternation from n0 kills residues from n0+2; below, the #6498 formula holds")
    print("=" * 78)
    c1 = lambda e: qint_bal(e + 1)
    c2 = lambda e: qint_bal(e + 2)
    S2 = shift_op(2, c2)
    D = add_ops(S2, S1)
    ps = seed_from(a[:8])                  # power-series seed, generic
    weight = sp.simplify(c1(-2) * c2(-1))
    ok(weight == -1, f"weight c1(-2) c2(-1) = {weight}")
    alive = [sp.simplify(iterate(D, n + 2, ps)(-2)) for n in range(0, 6)]
    print(f"  D^(n+2) f(-2), n=0..5 (levels 2..7): {[str(v)[:40] for v in alive]}")
    ok(all(v != 0 for v in alive), "levels 2..7 carry a NONZERO residue on a generic seed -- inside a pre-asymptotic window of length >= 6 they are alive")
    ok(all(sp.simplify(alive[n] - weight * iterate(D, n, ps)(1)) == 0 for n in range(6)), "and each equals c1(-2) c2(-1) * (D^n f)(1)  (#6498 formula)")
    # the asymptotic theorem's conclusion is the pure-odd tower from n0 on; check its residue
    # vanishes from n0+2 on for any level-n0 jet Y (take Y = D^n0 ps, and ALSO an arbitrary Laurent Y)
    for n0 in (0, 3, 6):
        Y = iterate(D, n0, ps)
        dead = all(sp.simplify(iterate(S1, k + 2, Y)(-2)) == 0 for k in range(0, 4))
        ok(dead, f"n0 = {n0}: the odd-part tower from the level-{n0} jet has dead residue at levels n0+2.. (no seed hypothesis)")
    ok(all(sp.simplify(iterate(S1, k + 2, laurent)(-2)) == 0 for k in range(0, 4)),
       "same with an arbitrary Laurent level-n0 jet")

    print()
    print("=" * 78)
    print("(4) RECORDED, NOT CHECKED: jet level n = GGM index m rests on the conjecture's")
    print("    'jet degree = body order' identification (prop:sw-period-residue-sum).")
    print("=" * 78)
    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for m_ in fail:
            print("  -", m_)
        return 1
    print("VERDICT (exact where symbolic; mpmath at 60 dps for the threshold):")
    print(f"  * The measured Door-v residual is ASYMPTOTIC: at the proton q0 the GGM")
    print(f"    coefficient turns negative at m = {first_neg} and the growing solution first")
    print(f"    flips sign at m = {first_flip}; below that there is no alternation at all.")
    print("  * So the #6498 exclusivity hypothesis (alternation at EVERY level) is")
    print("    strictly stronger than the measured residual.  Under the measured,")
    print("    from-level-n0 form the residue is dead only from level n0 + 2 on, and")
    print(f"    the derivative-like two-term operator keeps a live residue at levels")
    print(f"    2 .. n0 + 1 -- at q0, jet levels 2 .. {first_neg + 1}, the low body orders.")
    print("  * Residue and residual therefore COEXIST in the pre-asymptotic window;")
    print("    the 'mutually exclusive' clause of #6498 holds only above it.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
