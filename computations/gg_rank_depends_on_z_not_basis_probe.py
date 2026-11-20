#!/usr/bin/env python3
"""
gg_rank_depends_on_z_not_basis_probe — the <g,g> collapse to Temperley-Lieb is
caused by the VALUE of the Markov parameter z, not by the GB basis. At generic z
the pairing is non-degenerate; at the canonical convention-D z it has rank C_n.
And the convention-C parameter -- the sqrt(q) one -- is NON-degenerate.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Follows the tower walk (#6396),
which established rank <g,g> = C_n = dim TL_n at the canonical z.

## The two questions this answers

After the tower walk showed <g,g> = tr_M(T_v T_w) has rank C_n and therefore
factors through Temperley-Lieb, two routes out were proposed:

  (Q1) Can binding be sourced from a pairing that does NOT factor through TL?
  (Q2) Is the fix to work with v = sqrt(q), doing the GB in an algebra that
       projects onto H_n?

## Q2's second half is answered by pure algebra, before any measurement

**The GB basis cannot possibly be the cause, because the RANK OF A BILINEAR FORM
IS BASIS-INDEPENDENT.** Changing to normal forms computed in a larger algebra
that surjects onto `H_n` re-expresses the same form in a different basis; a
surjection induces the identical form on the quotient. So no choice of GB basis,
in any algebra projecting onto `H_n`, can change `rank <g,g>` by even one.

That is not an empirical claim and this probe does not need to test it -- but it
DOES test it, by conjugating the Gram with a random invertible change of basis
and checking the rank is unmoved. A demonstration is cheaper than an argument
when the reader is deciding whether to spend a tranche on the route.

## What actually controls the rank

The space of traces on `H_n(q)` is spanned by the irreducible characters, so any
trace is `tau = sum_lambda c_lambda chi^lambda`, and the form `tau(xy)` is
block-diagonal with block `lambda` scaled by `c_lambda`. Hence

    radical of tau(xy)  =  the sum of the blocks where c_lambda = 0.

For the Markov trace the `c_lambda` are the weights `y_lambda(q, z)`, so the
radical is controlled by which weights vanish -- and that is a question about
`z`, not about how the algebra is presented.

## The measurement

Rank of `G_{vw} = tr_M(T_v T_w)` at fixed `q0`, varying only `z`:

    z_D = q^3/(q^2+1)        canonical (owner ruling 2026-08-15)
    z_C = sqrt(q)/(q+1)      = 1/(v + 1/v) with v = sqrt(q)  [convention C]
    1/(q + 1/q)
    generic values

The finding, and it inverts the natural guess: **`z_C`, the `sqrt(q)` parameter,
gives a FULL-RANK pairing. The canonical `z_D` is the degenerate one.**

## Scope, and the tension it raises

Scope **(a)**: a measurement of what controls the rank. It does NOT propose
reverting the convention ruling and does NOT compute a binding energy.

But it does surface a tension that belongs in front of the owner: convention D is
canonical by the 2026-08-15 ruling, and convention D is exactly the `z` at which
the Frobenius pairing collapses onto Temperley-Lieb and becomes blind to the bulk
of the tower. The ruling was made on trace-convention grounds; this is a
different fact that bears on it, and the two have not been weighed together.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin. `float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import importlib.util as _ilu  # noqa: E402
# `comb`/`factorial` return exact arbitrary-precision `int`, never float
# (verified: type() is int; catalan cross-checked against an integer recurrence
# for k=1..14; factorial(170) is exact where f64 overflows). All four uses here
# are integer comparison or formatting -- `r == factorial(n)`, the C_n column --
# and no result of either ever enters float arithmetic. Same false positive the
# guard raised on gg_gram_tower_walk_probe.py.
from math import comb, factorial  # noqa: E402  # float64-ok: exact int, never float

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** -35


def _walk():
    """Reuse the tower walk's verified Hecke arithmetic (calibrated at n=3
    against `pyhecke.gram_matrix_mp` to 4.94e-51 inside that probe).

    DEPENDENCY: `gg_gram_tower_walk_probe.py`, which lands in PR #6396. This
    probe is deliberately NOT a second copy of that arithmetic -- duplicating a
    Hecke multiplication that took three bugs to get right would be the worse
    failure. If the sibling is absent, say so plainly and exit non-zero rather
    than failing with an opaque import error.
    """
    p = _Path(__file__).resolve().parent / "gg_gram_tower_walk_probe.py"
    if not p.exists():
        raise SystemExit(
            "gg_gram_tower_walk_probe.py not found next to this probe.\n"
            "It is the verified Hecke/Markov arithmetic this probe reuses and\n"
            "it lands in PR #6396. Rebase onto a main that carries #6396, or\n"
            "run this from that branch. Deliberately not duplicated here."
        )
    spec = _ilu.spec_from_file_location("_ggwalk", p)
    m = _ilu.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def catalan(k):
    return comb(2 * k, k) // (k + 1)


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    m = _walk()
    q0 = Q_MP
    h = q0 - 1 / q0
    v = mp.sqrt(q0)

    print("gg_rank_depends_on_z_not_basis_probe")
    print("=" * 78)
    print(f"q0 = {fmt(q0, 20)}   h = {fmt(h, 12)}   v = sqrt(q0) = {fmt(v, 12)}")
    print()

    # ---- 1. the basis cannot matter, and here is the demonstration ---------
    print("1. THE GB BASIS CANNOT BE THE CAUSE — rank is basis-independent")
    print("-" * 78)
    print("  A surjection from a larger algebra onto H_n induces the IDENTICAL")
    print("  form on the quotient, so normal forms computed there re-express the")
    print("  same pairing in a different basis.  Rank is invariant under change")
    print("  of basis, so no GB choice in any algebra projecting onto H_n can")
    print("  move rank <g,g> by even one.  Demonstrated rather than asserted:")
    zD = q0**3 / (q0**2 + 1)
    memo = {}
    basis, G = m.gram(4, h, zD, memo)
    r0, _, _ = m.rank_and_radical(G, TOL)
    d = len(basis)
    # A deterministic, definitely-invertible change of basis P (unit lower
    # triangular): G -> P^T G P.  No RNG, so this is reproducible.
    P = mp.matrix(d, d)
    for i in range(d):
        for j in range(d):
            P[i, j] = mp.mpf(1) if i == j else (mp.mpf(1) / (2 + i + 2 * j)
                                                if i > j else mp.mpf(0))
    Gm = mp.matrix(G)
    G2 = P.T * Gm * P
    r1, _, _ = m.rank_and_radical([[G2[i, j] for j in range(d)]
                                   for i in range(d)], TOL)
    print(f"    n = 4, rank in the GB normal-form basis      : {r0}")
    print(f"    n = 4, rank after a change of basis P^T G P  : {r1}")
    assert r0 == r1, "rank must be invariant under change of basis"
    print("    equal, as it must be.  => 'do the GB in a bigger algebra that")
    print("    projects onto H_n' CANNOT fix the degeneracy.  Whatever the fix")
    print("    is, it is not a basis.")
    print()

    # ---- 2. what does control it: z ----------------------------------------
    print("2. WHAT DOES CONTROL IT — the Markov parameter z")
    print("-" * 78)
    print("  Any trace on H_n(q) is tau = sum_lambda c_lambda chi^lambda, so")
    print("  tau(xy) is block-diagonal with block lambda scaled by c_lambda, and")
    print("  its radical is the sum of the blocks where c_lambda = 0.  For the")
    print("  Markov trace the c_lambda are the weights y_lambda(q, z): which")
    print("  blocks die is a question about z, not about the presentation.")
    print()
    CANDS = [
        ("z_D = q^3/(q^2+1)   [CANONICAL, conv D]", q0**3 / (q0**2 + 1)),
        ("z_C = sqrt(q)/(q+1) [conv C] = 1/(v+1/v)", mp.sqrt(q0) / (q0 + 1)),
        ("1/(v + 1/v),  v = sqrt(q)", 1 / (v + 1 / v)),
        ("1/(q + 1/q)", 1 / (q0 + 1 / q0)),
        ("generic 0.3", mp.mpf("0.3")),
        ("generic 0.7", mp.mpf("0.7")),
    ]
    NS = (3, 4, 5)
    print(f"{'z candidate':>42} {'value':>14} " +
          " ".join(f"{'n=' + str(n):>6}" for n in NS) + "   verdict")
    verdicts = {}
    for name, z in CANDS:
        ranks = []
        for n in NS:
            _b, Gz = m.gram(n, h, z, {})
            r, _, _ = m.rank_and_radical(Gz, TOL)
            ranks.append(r)
        full = all(r == factorial(n) for r, n in zip(ranks, NS))
        tl = all(r == catalan(n) for r, n in zip(ranks, NS))
        verdict = "FULL RANK" if full else ("= C_n (TL)" if tl else "mixed")
        verdicts[name] = verdict
        print(f"{name:>42} {fmt(z, 10):>14} " +
              " ".join(f"{r:>6}" for r in ranks) + f"   {verdict}")
    print(f"{'reference: n! ':>42} {'':>14} " +
          " ".join(f"{factorial(n):>6}" for n in NS))
    print(f"{'reference: C_n':>42} {'':>14} " +
          " ".join(f"{catalan(n):>6}" for n in NS))
    print()

    canon = verdicts["z_D = q^3/(q^2+1)   [CANONICAL, conv D]"]
    convc = verdicts["z_C = sqrt(q)/(q+1) [conv C] = 1/(v+1/v)"]
    assert canon == "= C_n (TL)", "canonical z_D must be the TL point"
    assert convc == "FULL RANK", "convention-C z must be non-degenerate"
    print("  => The canonical convention-D parameter is the DEGENERATE one, and")
    print("     the convention-C parameter -- the sqrt(q) one, 1/(v + 1/v) --")
    print("     is FULL RANK.  This inverts the natural guess, since 1/(v+1/v)")
    print("     is the classical Jones/TL loop normalisation and would be the")
    print("     obvious candidate for the TL point.  It is not.")
    print()

    # ---- 3. is z_D an approximation, or an exact special point? ------------
    print("3. IS z_D AN APPROXIMATION, OR AN EXACT SPECIAL POINT?")
    print("-" * 78)
    print("  z_D factors: q^3/(q^2+1) = q^2 * [1/(q + 1/q)] -- the BALANCED")
    print("  parameter times q^2.  So sweep the exponent in z = q^a/(q + 1/q)")
    print("  and see whether the degeneracy is a region or a point.")
    zbal = 1 / (q0 + 1 / q0)
    assert abs(q0**2 * zbal - q0**3 / (q0**2 + 1)) < mp.mpf(10) ** -40, \
        "q^2/(q+1/q) must equal q^3/(q^2+1)"
    print(f"    identity check |q^2/(q+1/q) - q^3/(q^2+1)| = "
          f"{fmt(abs(q0**2 * zbal - q0**3 / (q0**2 + 1)), 4)}")
    print()
    print(f"{'a':>6} {'z = q^a/(q+1/q)':>18} {'rank n=3':>10} {'rank n=4':>10}"
          f"   (full = 6 / 24)")
    degenerate_a = []
    for a in ("-2", "-1", "0", "0.5", "1", "1.5", "2", "2.5", "3"):
        av = mp.mpf(a)
        za = q0**av * zbal
        rs = []
        for n in (3, 4):
            _b, Gz = m.gram(n, h, za, {})
            r, _, _ = m.rank_and_radical(Gz, TOL)
            rs.append(r)
        deg = rs != [factorial(3), factorial(4)]
        if deg:
            degenerate_a.append(a)
        tag = "  <-- z_D CANONICAL" if a == "2" else ""
        print(f"{a:>6} {fmt(za, 10):>18} {rs[0]:>10} {rs[1]:>10}{tag}")
    print()
    print(f"  degenerate exponents in this sweep: {degenerate_a}")
    assert degenerate_a == ["2"], "only a = 2 should degenerate"
    print("  => AN ISOLATED POINT, not a region.  Half-integer exponents")
    print("     (0.5, 1.5, 2.5) are FULL RANK -- and so are the integers other")
    print("     than 2.  So the half-power is NOT what distinguishes them, and")
    print("     'z_C is full rank because it has a sqrt(q)' is the WRONG reading:")
    print("     z_C is full rank because it is not a = 2.")
    print()

    # ---- 4. is it structural in q, or an accident of the pin? --------------
    print("4. IS THE DEGENERACY STRUCTURAL IN q, OR AN ACCIDENT OF THE PIN?")
    print("-" * 78)
    print(f"{'q':>12} {'z = q^3/(q^2+1)':>18} {'rank n=3':>10} {'rank n=4':>10}")
    all_deg = True
    for qs in (Q_50_DIGIT_STR, "1.01", "1.5", "2", "3", "0.8"):
        qq = mp.mpf(qs)
        hh = qq - 1 / qq
        zz = qq**3 / (qq**2 + 1)
        rs = []
        for n in (3, 4):
            _b, Gz = m.gram(n, hh, zz, {})
            r, _, _ = m.rank_and_radical(Gz, TOL)
            rs.append(r)
        all_deg = all_deg and rs == [catalan(3), catalan(4)]
        lbl = "  <-- proton pin" if qs == Q_50_DIGIT_STR else ""
        print(f"{fmt(qq, 8):>12} {fmt(zz, 12):>18} {rs[0]:>10} {rs[1]:>10}{lbl}")
    assert all_deg, "z_D must be degenerate at every q, else it is pin-specific"
    print()
    print("  => rank = C_n at EVERY q tested, from 0.8 to 3.0.  The degeneracy is")
    print("     an ALGEBRAIC IDENTITY in q, not a coincidence at the pin.")
    print()
    print("  CONCLUSION.  z_D = q^3/(q^2+1) is not NEAR a Temperley-Lieb point --")
    print("  it IS the TL specialisation, exactly, for all q.  A first-order")
    print("  approximation to something else would not land on a measure-zero")
    print("  point at every q simultaneously, and would not be flanked by")
    print("  full-rank values at a = 1.5 and a = 2.5.  Choosing convention D is")
    print("  mathematically the same act as choosing to make the Frobenius")
    print("  pairing factor through Temperley-Lieb.")
    print()

    print("5. ANSWERS")
    print("-" * 78)
    print("  Q1: can binding be sourced from a pairing that does not factor")
    print("      through TL?")
    print("      YES, such pairings exist in abundance -- every generic z gives")
    print("      one, on the SAME algebra, SAME basis, SAME construction.  The")
    print("      TL collapse is not a structural feature of the Hecke tower or")
    print("      of the Markov trace; it is a property of one value of z.")
    print()
    print("  Q2: is the fix v = sqrt(q), with the GB done in an algebra that")
    print("      projects onto H_n?")
    print("      NO on both halves, though for different reasons:")
    print("      * the GB-in-a-larger-algebra part cannot be the mechanism at")
    print("        all, because rank is basis-independent (section 1);")
    print("      * and the sqrt(q) part does no work either.  Section 3 sweeps")
    print("        the exponent: HALF-INTEGER a (0.5, 1.5, 2.5) is full rank,")
    print("        and so is every integer except 2.  z_C is non-degenerate")
    print("        because it is not a = 2, NOT because it carries a sqrt(q).")
    print("        An intermediate reading of section 2 alone -- 'the sqrt(q)")
    print("        parameter is the non-degenerate one' -- is true but")
    print("        MISLEADING, and section 3 is what corrects it.")
    print()
    print("      What IS true: z_D is an isolated, q-independent special point.")
    print("      The fix, if one exists, is to move OFF that point -- and any")
    print("      other z will do, half-power or not.")
    print()

    print("THE TENSION THIS RAISES — for the owner, not for me to resolve")
    print("-" * 78)
    print("  Convention D is canonical by the owner ruling of 2026-08-15")
    print("  ('convention D is convention. excise convention C').  Convention D")
    print("  is also exactly the z at which the Frobenius pairing collapses onto")
    print("  Temperley-Lieb and goes blind to the bulk of the tower.")
    print()
    print("  These were decided on different grounds and have not been weighed")
    print("  together: the ruling settled a trace-convention question; this is a")
    print("  fact about the rank of the pairing.  Nothing here says the ruling is")
    print("  wrong -- D may well be right for the reasons it was chosen, and the")
    print("  <g,g> route may simply be the wrong route.  What is NOT tenable is")
    print("  pursuing an <g,g>/SDP binding derivation under convention D while")
    print("  treating the degeneracy as a numerical nuisance: it is exactly the")
    print("  convention.")
    print()
    print("WHAT THIS DOES NOT SAY")
    print("-" * 78)
    print("  * NOT that convention D is wrong, and NOT a proposal to revert to")
    print("    C.  C was excised for reasons this probe does not touch.")
    print("  * NOT that a full-rank pairing WOULD source the binding.  Only that")
    print("    the blindness objection does not apply to it.  Whether any such")
    print("    pairing reproduces AME is entirely unmeasured here.")
    print("  * NOT anything about which lambda-blocks die at z_D.  rank = C_n is")
    print("    strong evidence for the >=3-row (level-2 Wenzl) reading, but the")
    print("    per-block weights were not computed and that identification is")
    print("    inferred from the rank alone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
