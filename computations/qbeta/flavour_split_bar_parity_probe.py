#!/usr/bin/env python3
"""The flavour-split baseline carries exactly ONE unit of framing -- a prune on its prefactor.

WHAT THIS ESTABLISHES
---------------------
`flavour_split_baseline_is_augmentation_trace_probe.py` identified the
`(q^2 - q^-2)` factor of `conj:flavor-split-habiro-derivation`'s baseline as the
Markov trace of the k = 2 crossing reversal at the augmentation, and left the
PREFACTOR `hbar_q^2/3` explicitly underived.  This probe measures one structural
constraint on that prefactor, under the bar involution `q -> 1/q`.

    X_baseline(1/q)  =  -q^2 * X_baseline(q)        neither bar-even nor bar-odd
    q * X_baseline   is  bar-ODD                     exactly one unit of framing
    w = 1 is the ONLY integer weight that does this

Since `q^2 - q^-2` is itself bar-odd, the condition on any prefactor C with
`X = C*(q^2-q^-2)` is `C(1/q) = q^2 * C(q)`.  The corpus's `hbar_q^2` meets it in
a way worth naming:

    q * hbar_q^2  =  (q-1)^2/q  =  -hbar_q * hbar_{1/q}

-- **the prefactor is 1/q times the BAR-NORM of hbar_q**, exactly.  That is the
sharpest positive statement here, and it is an identity rather than a derivation.

IT IS A PRUNE, NOT A DERIVATION -- SAID PLAINLY
-----------------------------------------------
Section 3 scans a 2044-monomial family in `hbar_q, h, [2]_q, [3]_q, z_D, (q-1),
q` (exponents in [-2,2], total degree <= 4) and reports how many satisfy the
parity condition.  The answer is 121 -- a 94 % prune that still leaves `hbar_q^2`
one survivor among many, and `q^-1` ALONE passes at degree 1 and is simpler.  So
parity narrows the search and does not close it.

The `/3` is UNTOUCHED: 3 is bar-invariant, so this argument says nothing about it
at all.  Where the 3 comes from is exactly as open as before.

AN HONEST NEGATIVE, WITH ITS AMBIGUITY UNRESOLVED
-------------------------------------------------
AGENTS.md's canonical cheat sheet calls `Q_beta` "the bar-odd sinh partner of the
bar-even cosh meson scale m_pi".  Measured against the published closed form
`Q_beta = m_e |q^2-2q-1|(q+1)/(2q^3)`, the literal reading FAILS: its bar ratio is
`-q^3(q^2+2q-1)/(q^2-2q-1)`, not a monomial in q, so NO integer framing weight
makes it bar-odd or bar-even.  The `cosh` half does check out -- `[2]_q` is
bar-even (section 5).

Three readings are consistent and THIS PROBE DOES NOT SEPARATE THEM:
  (i)   the description names a structural sector, not that expression;
  (ii)  the expression is the `z = 1` cell AGENTS.md's own 2026-09-05 scoping
        note retires as inadmissible under convention D, so the object being
        described is not this one;
  (iii) the description is wrong.
(ii) is the reading the corpus's own scoping note already supports, which is why
this is recorded as an observation and not filed as a defect.  Scope (a): a
measured negative about one expression, no invariant excluding a bar-odd Q_beta.

Lean: `QOU/Hecke/FlavourSplitBarParity.lean` (9 decls, lean-direct exit 0,
#print axioms clean).

Run: python3 computations/qbeta/flavour_split_bar_parity_probe.py
"""

from __future__ import annotations

import itertools
import sys

import sympy as sp
from mpmath import mp

mp.dps = 60

_q = sp.symbols("q", positive=True)


def bar(e):
    """The bar involution q -> 1/q."""
    return sp.simplify(sp.together(e.subs(_q, 1 / _q)))


HBAR = 1 - 1 / _q
H = _q - 1 / _q
T2 = _q + 1 / _q
T3 = _q**2 + 1 + _q**-2
Z_D = _q**3 / (_q**2 + 1)
SYM = _q**2 - _q**-2
X_BASELINE = (_q - 1) ** 2 * (1 - _q**-4) / 3
Q_BETA_SHAPE = (_q**2 - 2 * _q - 1) * (_q + 1) / (2 * _q**3)


def ratio(e):
    return sp.factor(sp.simplify(bar(e) / e))


def main() -> int:
    ok = True

    print("1. THE BASELINE IS NEITHER BAR-EVEN NOR BAR-ODD")
    r_x = ratio(X_BASELINE)
    r_sym = ratio(SYM)
    r_pre = ratio(HBAR**2)
    ok &= (r_x == -_q**2) and (r_sym == -1) and (r_pre == _q**2)
    print(f"   bar(q^2 - q^-2) / (q^2 - q^-2)      = {r_sym}      bar-ODD")
    print(f"   bar(hbar_q^2)   / hbar_q^2          = {r_pre}     the prefactor's twist")
    print(f"   bar(X_baseline) / X_baseline        = {r_x}    NEITHER")

    print()
    print("2. EXACTLY ONE UNIT OF FRAMING MAKES IT BAR-ODD, AND w = 1 IS UNIQUE")
    hits = []
    for w in range(-4, 5):
        e = _q**w * X_BASELINE
        if sp.simplify(bar(e) + e) == 0:
            hits.append(w)
        if sp.simplify(bar(e) - e) == 0:
            print(f"   w = {w}: bar-EVEN  (unexpected)")
    ok &= hits == [1]
    print(f"   integer weights w in [-4,4] with q^w * X_baseline bar-ODD: {hits}")
    print(f"   -> unique, w = 1: {'CONFIRMED' if hits == [1] else 'NOT CONFIRMED'}")
    qx = sp.factor(sp.simplify(_q * X_BASELINE))
    print(f"   q * X_baseline = {qx}")

    print()
    print("3. THE PREFACTOR IS 1/q TIMES THE BAR-NORM OF hbar_q  (exact)")
    barnorm = sp.simplify(-HBAR * bar(HBAR))
    e1 = sp.simplify(_q * HBAR**2 - barnorm)
    e2 = sp.simplify(bar(_q * HBAR**2) - _q * HBAR**2)
    ok &= (e1 == 0) and (e2 == 0)
    print(f"   -hbar_q * hbar_(1/q)        = {sp.factor(barnorm)}")
    print(f"   q * hbar_q^2 - that         = {e1}   {'EXACT' if e1 == 0 else 'MISMATCH'}")
    print(f"   q * hbar_q^2 is bar-EVEN    : {e2 == 0}")

    print()
    print("4. HOW MUCH DOES PARITY ACTUALLY PRUNE?  (it is NOT a derivation)")
    gens = {"hbar": HBAR, "h": H, "[2]_q": T2, "[3]_q": T3,
            "z_D": Z_D, "(q-1)": _q - 1, "q": _q}
    names = list(gens)
    total = 0
    survivors = []
    _surv_full = []
    for exps in itertools.product(range(-2, 3), repeat=len(names)):
        if sum(abs(e) for e in exps) > 4 or all(e == 0 for e in exps):
            continue
        total += 1
        C = sp.Integer(1)
        for n, e in zip(names, exps):
            C *= gens[n] ** e
        if sp.simplify(bar(C) / C - _q**2) == 0:
            lbl = "*".join(f"{n}^{e}" for n, e in zip(names, exps) if e)
            deg = sum(abs(e) for e in exps)
            survivors.append((deg, lbl))
            _surv_full.append((lbl, C, deg))
    survivors.sort()
    n_surv = len(survivors)
    ok &= (total == 2044) and (n_surv == 121)
    print(f"   scanned {total} monomials (|e| <= 2, total degree <= 4)")
    print(f"   satisfying bar(C)/C = q^2:  {n_surv}   ({100*(1-n_surv/total):.1f} % pruned)")
    print("   the four simplest survivors:")
    for deg, lbl in survivors[:4]:
        print(f"      deg {deg}: {lbl}")
    has_hbar2 = any(lbl == "hbar^2" for _, lbl in survivors)
    has_qinv = any(lbl == "q^-1" for _, lbl in survivors)
    ok &= has_hbar2 and has_qinv
    print(f"   hbar^2 survives: {has_hbar2}     q^-1 also survives (simpler): {has_qinv}")
    print("   -> PRUNE, NOT DERIVATION.  And 3 is bar-invariant, so the /3 is")
    print("      untouched by this argument entirely.")

    print()
    print("5. THE cosh HALF OF THE CHEAT SHEET'S SENTENCE CHECKS OUT")
    r_t2 = ratio(T2)
    ok &= r_t2 == 1
    print(f"   bar([2]_q)/[2]_q = {r_t2}    bar-EVEN, as 'the bar-even cosh meson scale'")

    print()
    print("6. THE sinh HALF DOES NOT -- honest negative, scope (a)")
    r_qb = ratio(Q_BETA_SHAPE)
    print(f"   bar(Q_beta)/Q_beta = {r_qb}")
    is_monomial = r_qb.is_Pow or r_qb.is_Number or r_qb == _q or r_qb == -_q
    qb_hits = [w for w in range(-4, 5)
               if sp.simplify(bar(_q**w * Q_BETA_SHAPE) + _q**w * Q_BETA_SHAPE) == 0
               or sp.simplify(bar(_q**w * Q_BETA_SHAPE) - _q**w * Q_BETA_SHAPE) == 0]
    ok &= (qb_hits == []) and (not is_monomial)
    print(f"   is that a monomial in q?  {is_monomial}")
    print(f"   integer w in [-4,4] making q^w Q_beta bar-odd OR bar-even: {qb_hits}")
    print("   -> the published closed form has NO integer framing weight at which")
    print("      it is bar-odd.  Three readings are consistent (see the docstring)")
    print("      and this probe separates NONE of them; (ii), that the expression")
    print("      is the retired z = 1 cell, is the one the corpus already supports.")

    print()
    print("7. A SECOND, INDEPENDENT INVARIANT: VANISHING ORDER AT q = 1")
    _e = sp.symbols("e", positive=True)

    def vorder(x):
        s = sp.simplify(x.subs(_q, 1 + _e))
        return sp.limit(sp.log(sp.Abs(s)) / sp.log(_e), _e, 0)

    o_R, o_X = vorder(SYM), vorder(X_BASELINE)
    o_hb2, o_qinv = vorder(HBAR**2), vorder(1 / _q)
    ok &= (o_R == 1) and (o_X == 3) and (o_hb2 == 2) and (o_qinv == 0)
    print(f"   q^2 - q^-2   order {o_R}      X_baseline   order {o_X}")
    print(f"   hbar_q^2     order {o_hb2}      q^-1         order {o_qinv}")
    print("   -> the corpus's baseline vanishes to order 3; with R at order 1 that")
    print("      forces a prefactor of order 2, which hbar_q^2 is and q^-1 is not.")
    order2 = sorted((d, l) for l, C, d in _surv_full if vorder(C) == 2)
    ok &= len(order2) == 32 and order2[0][1] == "hbar^2" and order2[0][0] == 2
    print(f"   parity AND order 2:  {len(order2)} of {total}  "
          f"({100*(1-len(order2)/total):.1f} % pruned)")
    print(f"   unique minimal-degree survivor: {order2[0][1]} (degree {order2[0][0]})")
    print("   🛑 BUT order 2 is read OFF THE CORPUS'S OWN EXPRESSION, not derived.")
    print("      It is a weaker form of the same hazard: selection against the")
    print("      corpus's answer rather than against the data.  Labelled, not hidden.")

    print()
    print("8. ONE HYPOTHESIS GIVES BOTH CONSTRAINTS  (Lean: barNorm_scaled_parity)")
    print("   If C = (1/q) * barNorm(f), barNorm(f)(q) := -f(q) f(1/q), then:")
    for lbl, f in (("f = hbar_q", HBAR), ("f = h", H), ("f = (q-1)", _q - 1)):
        C = sp.simplify(-f * bar(f) / _q)
        par = sp.simplify(bar(C) / C - _q**2) == 0
        o = vorder(C)
        print(f"   {lbl:12s}: C = {str(sp.factor(C)):22s} parity {par}, order {o}")
    inst = sp.simplify(-HBAR * bar(HBAR) / _q - HBAR**2)
    ok &= inst == 0
    print(f"   and at f = hbar_q the instance is EXACTLY hbar_q^2: {inst}  "
          f"{'EXACT' if inst == 0 else 'MISMATCH'}")
    degen = sp.simplify(-HBAR * bar(HBAR) / _q - (-(_q - 1) * bar(_q - 1) / _q))
    ok &= degen == 0
    print(f"   AND IT IS DEGENERATE: f = (q-1) gives the IDENTICAL prefactor "
          f"(difference {degen}).")
    print("   -> parity is automatic for EVERY f (proved in Lean, no hypothesis on f);")
    print("      order 2 follows whenever f vanishes at q = 1.  The hypothesis that")
    print("      the prefactor IS a bar-norm is NOT derived — and even granting it,")
    print("      it does not single out hbar_q, since (q-1) has the same bar-norm up")
    print("      to the 1/q.  It well-poses the search; it does not close it.")

    print()
    print("9. THE 3 DOES NOT q-DEFORM  (and this is NOT an accuracy argument)")
    tgt = mp.mpf("0.0013774698046076")
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP      # noqa: PLC0415
    q0 = Q_MP

    def at(e):
        return mp.mpf(str(sp.N(e.subs(_q, sp.Float(str(q0), 50)), 45)))

    core = HBAR**2 * SYM
    variants = [("plain 3 (the corpus's)", sp.Integer(3)),
                ("[3]_q = q^2 + 1 + q^-2", T3),
                ("[3]_q = q + 1 + q^-1", _q + 1 + 1 / _q)]
    for lbl, d in variants:
        v = at(core / d)
        print(f"   {lbl:26s} denom {mp.nstr(at(d), 10):>14s}  "
              f"delta {mp.nstr(v, 12):>16s}  rel {mp.nstr((v-tgt)/tgt, 6):>12s}")
    print("   -> the three denominators are DIFFERENT numbers, so the corpus's `3`")
    print("      is a plain rational and not a q-integer in disguise.  That is a")
    print("      statement about FORM.  The residual column is printed for the")
    print("      record and is explicitly NOT the argument: per NO-FITTING,")
    print("      accuracy is never a tie-breaker.  Where the 3 comes from is OPEN.")

    print()
    print("VERDICT:", "PASS -- the baseline is bar-odd after one unit of framing; the "
          "prefactor is 1/q times the bar-norm of hbar_q; parity + order prune to 32 "
          "of 2044 with hbar^2 minimal; and NOTHING here derives the 3"
          if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
