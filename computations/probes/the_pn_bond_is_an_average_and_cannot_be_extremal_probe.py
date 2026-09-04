#!/usr/bin/env python3
"""The pn bond can never be the strongest: its Hecke letter is by definition a
CONVEX COMBINATION of the pp and nn letters, the two-strand trace is affine in
the offset, so `L_pp < L_pn < L_nn` is forced for every `q` and every
`delta in (0,2)`. Physics needs `pn` to be the extreme — it is the only
two-body system that binds — and no choice of `q` can deliver that.

WHERE THIS SITS
---------------
Bean `qou-mu1h`, split out of `qou-bygw` after
`the_all_pairs_closure_is_not_one_link_probe` §5 measured, at `A = 2` where no
ordering or arrangement convention is in play:

    2He (pp)  L = 0.489899  B = 2.0507 MeV   reality: UNBOUND (diproton)
    2H  (pn)  L = 0.676822  B = 2.8332 MeV   reality: BOUND, 2.22452 MeV
    2n  (nn)  L = 0.907262  B = 3.7978 MeV   reality: UNBOUND (dineutron)

That probe asked whether the inversion `nn > pn > pp` is a numerical accident
or structural. It is neither. It is DEFINITIONAL.

THE IDENTITY
------------
Under convention D the three interface letters are `sigma + d` with

    d_pp = 0,     d_nn = -h,     d_pn = -h(1 - delta/2)/2,   h = q - 1/q,

and the third is exactly the weighted average of the first two:

    d_pn = (1/2 + delta/4) * d_pp  +  (1/2 - delta/4) * d_nn,
    weights summing to 1, both non-negative iff |delta| <= 2.

Verified symbolically (`d_pn - combination` simplifies to `0`, sympy) and at
200 bits. This is not a coincidence of the offset values — it is what
"averaged interface" MEANS in `atom_braid_word_3A`, whose own docstring writes
the letter as `(1/2 + delta/4) sigma + (1/2 - delta/4) sigma^-1`. The pn bond
is defined as an average over crossing sign between the pp and nn bonds.

WHY THAT SETTLES THE ORDERING
-----------------------------
`the_canonical_mass_trace_factorises_over_the_chain_probe` proved the interface
law is affine: `tr_2(sigma + d) = z + d`, `z = q^3/(q^2+1)`. An affine map sends
a convex combination to the same convex combination, so `z + d_pn` lies
strictly between `z + d_nn` and `z + d_pp`. And `L = -log(z + d)` is strictly
DECREASING in `d`. Therefore

    d_nn < d_pn < d_pp        =>        L_pp < L_pn < L_nn

for every `q > 1` and every `delta in (0, 2)` — with no freedom anywhere. At
`q_0` the pn factor sits at `0.500344` of the way from nn to pp, and `delta`
would have to reach `2` before the convexity even breaks, which needs
`q = 3.4581` against `q_0 = 1.10998`. There is no tuning here: the pn bond is
pinned between the other two by the definition of the letter.

WHAT PHYSICS NEEDS
------------------
Of the three two-body systems exactly one binds, and it is `pn`. So a bond
constant that ranks binding strength must put `pn` at an EXTREME. A convex
combination is never an extreme. The model therefore cannot rank the two-body
systems correctly, for any `q`, by construction rather than by misfit.

THE CAVEAT, STATED BEFORE THE CONCLUSION
----------------------------------------
This arc's `L` carries no spin, and the real distinction IS a spin one: the
deuteron binds in the `3S1` triplet channel, and every `1S0` two-body system —
`pp`, `pn`, `nn` alike — is unbound. A spinless bond constant cannot be
expected to separate bound from unbound. So "the model gets 2He wrong" is not
by itself a finding, and this probe does not claim it is.

What does not follow from the absence of spin is the ORDER. Nothing about
lacking a spin channel requires the unbound `nn` system to be ranked above the
bound `pn` one. That ranking comes from the averaging convention, and it would
persist in a spin-resolved theory that kept the same interface letter.

WHERE THE CORPUS'S np PREFERENCE ACTUALLY LIVES
-----------------------------------------------
Not in the bond constants. `wigner-np-pairing` puts it in the self-conjugate
`(2,2) |- 4` partition, as a categorical Wigner energy
`Delta_(2,2) = m_e [3]_q [2]_q^2 = 6.2894 MeV` (reproduced here to check the
reading, not to re-derive the block). That is a level-4 object and there is no
`(2,2)` partition of `2`, so whatever np preference it supplies is unavailable
at `A = 2`, where the bond constants are the whole story. So there is no
contradiction between the two — and that is the problem, because it leaves the
two-body ordering with nothing to rescue it.

WHAT WOULD HAVE TO CHANGE
-------------------------
One of these, none of them taken here:
  * the pn interface stops being an average over crossing sign — some letter
    outside the segment `[d_nn, d_pp]`, i.e. `|delta| > 2` or a different
    convention entirely;
  * the bond constant stops being the thing that ranks binding, and a channel
    the two-body sector actually has carries the np preference;
  * the framework declares the bond constant channel-averaged, and says
    explicitly what it is averaged over — at `A = 2` the `1S0`/`3S1` split is
    the entire content.

WHAT IS NOT CLAIMED
-------------------
Not that the framework is wrong. Not that `wigner-np-pairing` or
`reeb-pn-magnitude-criticality` are wrong; they are read, not re-derived, and
neither is contradicted. Nothing about `A >= 3`, where other channels exist.
The claim is exactly: at `A = 2` the three bond constants come out in an order
the physics does not have, and that order is forced by the definition of the
pn letter rather than by any fitted or tunable quantity.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402
import sympy as sp  # noqa: E402

import _exact_trace_engine as E  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

ALPHA = mpfr(str(M_E_MEV)) / (E.Q * (E.Q - 1))
REAL = {"pp": ("2He  (Z=2,N=0)", "UNBOUND — no bound diproton", None),
        "pn": ("2H   (Z=1,N=1)", "BOUND, B = 2.22452 MeV", mpfr("2.22452")),
        "nn": ("2n   (Z=0,N=2)", "UNBOUND — no bound dineutron", None)}


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nengine: {E.BITS} bits, q from Q_50_DIGIT_STR")

    print("\n" + "=" * 74)
    print("§1  THE pn LETTER IS A CONVEX COMBINATION OF THE pp AND nn LETTERS")
    print("=" * 74)
    q, dl = sp.symbols("q delta", positive=True)
    h = q - 1 / q
    d_pn = -h * (1 - dl / 2) / 2
    w_pp, w_nn = sp.Rational(1, 2) + dl / 4, sp.Rational(1, 2) - dl / 4
    comb = w_pp * 0 + w_nn * (-h)
    resid = sp.simplify(d_pn - comb)
    wsum = sp.simplify(w_pp + w_nn)
    print(f"    d_pp = 0,   d_nn = -h,   d_pn = -h(1 - delta/2)/2")
    print(f"    claim: d_pn = (1/2 + delta/4) d_pp + (1/2 - delta/4) d_nn")
    print(f"      residual  d_pn - combination = {resid}")
    print(f"      weight sum                   = {wsum}")
    print(f"    both weights are non-negative iff |delta| <= 2.")
    check("d_pn is exactly the stated convex combination of d_pp and d_nn (sympy)",
          resid == 0 and wsum == 1)

    print("\n" + "=" * 74)
    print("§2  SO THE ORDERING IS FORCED, FOR EVERY q AND EVERY delta IN (0,2)")
    print("=" * 74)
    z = E.Q ** 3 / (E.Q ** 2 + 1)
    d = {"pp": E.ZERO, "pn": E.D_PN, "nn": -E.H}
    L = {k: -gmpy2.log(z + v) for k, v in d.items()}
    print(f"    {'bond':<6}{'d':>16}{'z + d':>16}{'L = -log(z+d)':>18}{'B = alpha L':>14}")
    for k in ("pp", "pn", "nn"):
        print(f"    {k:<6}{float(d[k]):16.9f}{float(z + d[k]):16.9f}"  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
              f"{float(L[k]):18.9f}{float(ALPHA * L[k]):14.4f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    frac = (z + d["pn"] - (z + d["nn"])) / ((z + d["pp"]) - (z + d["nn"]))
    print(f"\n    the pn factor sits at fraction {float(frac):.6f} of the way from nn to pp")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    check("tr_2 being affine in d, z + d_pn lies STRICTLY between z + d_nn and z + d_pp",
          (z + d["nn"]) < (z + d["pn"]) < (z + d["pp"]))
    check("L = -log(z+d) is decreasing in d, so L_pp < L_pn < L_nn is forced",
          L["pp"] < L["pn"] < L["nn"])
    dq = (q - 1) ** 2 * (1 - q ** -4) / 3
    # delta at q0 comes from the exact engine, not a sympy round-trip: it is the
    # quantity the whole convexity argument turns on, so it stays in mpfr.
    d0 = E.DELTA
    q_break = sp.nsolve(sp.Eq(dq, 2), q, 3.0)   # float64-ok: sympy mpf, a coarse diagnostic bound (>3), never fed back
    print(f"    delta(q0) = {float(d0):.8f};  delta reaches 2 only at q = {float(q_break):.4f}, "  # float64-ok: display only
          f"against q0 = {float(E.Q):.5f}")  # float64-ok: display only
    check("delta is nowhere near the value that would break convexity, so the ordering "
          "is not tunable by q", mpfr(0) < d0 < mpfr("0.01") and q_break > 3)

    print("\n" + "=" * 74)
    print("§3  WHAT PHYSICS HAS, AND WHAT THE MODEL CAN OFFER")
    print("=" * 74)
    print(f"    {'system':<18}{'bond':<6}{'B_model (MeV)':>15}   reality")
    for k in ("pp", "pn", "nn"):
        print(f"    {REAL[k][0]:<18}{k:<6}{float(ALPHA * L[k]):15.4f}   {REAL[k][1]}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    print(f"\n    exactly one of the three binds, and it is pn — so a constant that ranks")
    print(f"    binding must put pn at an EXTREME. A convex combination is never an")
    print(f"    extreme. The model cannot rank the two-body systems, for any q.")
    check("the one system that binds is assigned the MIDDLE bond constant",
          L["pp"] < L["pn"] < L["nn"] and REAL["pn"][2] is not None)
    over = ALPHA * L["pn"] / REAL["pn"][2]
    print(f"    and the one it does bind it overshoots: {float(ALPHA * L['pn']):.4f} vs "  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
          f"AME {float(REAL['pn'][2]):.5f} = {float(over):.4f}x")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    check("the deuteron itself is overshot by ~1.27x — the same defect seen a second way",
          mpfr("1.2") < over < mpfr("1.35"))

    print("\n" + "=" * 74)
    print("§4  WHERE THE CORPUS'S np PREFERENCE LIVES (a reading, not a re-derivation)")
    print("=" * 74)
    q2 = E.Q + 1 / E.Q
    q3 = E.Q ** 2 + 1 + 1 / E.Q ** 2
    wig = mpfr(str(M_E_MEV)) * q3 * q2 ** 2
    print(f"    wigner-np-pairing: Delta_(2,2) = m_e [3]_q [2]_q^2 = {float(wig):.4f} MeV")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    print(f"      [2]_q = {float(q2):.6f}   [3]_q = {float(q3):.6f}   block says ~6.29 MeV")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
    check("the block's 6.29 MeV is reproduced, so the reading of it is right",
          abs(wig - mpfr("6.29")) < mpfr("0.01"))
    print(f"    that is a (2,2) |- 4 object; there is no (2,2) partition of 2, so it")
    print(f"    supplies nothing at A = 2 — no contradiction with the bond constants,")
    print(f"    and nothing to rescue their ordering either.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "The pn interface letter of convention D is exactly the convex combination "
            "(1/2 + delta/4) d_pp + (1/2 - delta/4) d_nn of the pp and nn letters, "
            "verified symbolically and at 200 bits. Since the two-strand trace is affine "
            "in the offset and L = -log(z+d) is strictly decreasing in it, "
            "L_pp < L_pn < L_nn is forced for every q and every delta in (0,2); delta at "
            "q0 is 0.0014 and would have to reach 2 (q = 3.458) to break convexity. But "
            "of the three two-body systems only pn binds, so a binding-ranking constant "
            "must put pn at an extreme, and a convex combination never is. The inversion "
            "measured at A=2 is therefore definitional, not numerical and not tunable. "
            "The corpus's np preference lives in the (2,2)|-4 Wigner term (6.2894 MeV, "
            "reproduced), which has no analogue at A=2. Caveat recorded: this L has no "
            "spin, and the bound/unbound split is a spin effect; the ORDER is not.")
        for k in ("pp", "pn", "nn"):
            wb.add_data(f"d_{k}", f"{float(d[k]):.12f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
            wb.add_data(f"L_{k}", f"{float(L[k]):.12f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
            wb.add_data(f"B_{k}_MeV", f"{float(ALPHA * L[k]):.6f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
        wb.add_data("pn_fraction_between_nn_and_pp", f"{float(frac):.9f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
        wb.add_data("delta_at_q0", f"{d0:.10f}")
        wb.add_data("q_at_which_delta_reaches_2", f"{q_break:.6f}")
        wb.add_data("deuteron_overshoot", f"{float(over):.6f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
        wb.add_data("wigner_2_2_MeV", f"{float(wig):.6f}")  # float64-ok: display only — value computed in mpfr/mpf, floated for printing
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "This arc's L carries no spin. The deuteron binds in the 3S1 triplet channel "
            "and every 1S0 two-body system is unbound, so a spinless bond constant cannot "
            "separate bound from unbound and is not claimed to. The finding is the ORDER, "
            "which the absence of spin does not explain.")
        wb.add_caveat(
            "wigner-np-pairing and reeb-pn-magnitude-criticality are read, not "
            "re-derived, and neither is contradicted. Nothing here concerns A >= 3, "
            "where other channels exist.")
        wb.add_caveat(
            "The alpha = m_e/(q0(q0-1)) normalisation is the sibling's, taken as-is; the "
            "ordering conclusion is independent of it, since alpha > 0 is a common factor.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
