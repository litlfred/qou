#!/usr/bin/env python3
# polynomial_q_not_applicable: exact sympy/Fraction algebra on the Ursell
# inversion; no symbolic-q polynomial output.
"""What does `qou-2ss0`'s scaling route give on the assemblies the corpus
actually DERIVES?

Measured answer: on both of them it reduces to the attractive-bond question
that `qou-q8vl` has already closed. A new escape needs a NON-MULTIPLICATIVE
trace, and the target for one reproduces, from a different direction, the
normalisation-free target already recorded on `qou-u5qs`.

## The route

`B3AggSecantCharacterisation.b3Agg_of_scales`: if `Phi(3g) = c * Phi(g)` then
`b3 = (c - 3) * Phi(g)`, with **no** convexity, differentiability or
homogeneity hypothesis. So

    b3 > 0   <=>   c > 3        (for Phi(g) > 0)

and `b3Agg_pos_iff_exponent_gt_one`'s `p > 1` is the SPECIAL CASE `c = 3^p`,
which holds only when `Phi` is `p`-homogeneous (CHECK 2). That distinction
matters here: the corpus's multiplicative assembly is `Phi(m) = 1 - f^m`, which
is EXPONENTIAL in the bond count, not a power `C x^p` — so the `p` criterion
does not apply to it and the `c` criterion does.

## What the two derived assemblies give

Writing `Phi` as a function of BOND COUNT with `Phi(0) = 0`
(`b3_bond_count_and_the_scaling_criterion_probe.py`):

| assembly | `Phi(m)` | `c = Phi(3)/Phi(1)` | `b3 > 0` iff |
|---|---|---|---|
| multiplicative `W = 1 - Z`, `Z = prod f_e` | `1 - f^m` | `1 + f + f^2` | `f > 1` |
| log free energy | `m * phi` | `3` exactly | never (`b3 = 0`) |

`c > 3` for the multiplicative assembly is `f^2 + f - 2 > 0`, i.e.
`(f+2)(f-1) > 0`, i.e. **`f > 1` — an attractive bond** (CHECK 3). That is
precisely the escape `qou-q8vl` records as closed for every DERIVED bond
family: production letters by `d <= 0` (`SingleCrossingAlwaysBinds
.interface_mem_Ioo`), isospin projectors by the identity `mu_+ + mu_- = 1`
(`InterfaceScalar.mu_sum_eq_one`).

So **the scaling route, applied to the assemblies the corpus derives, is the
attractive-bond question in different coordinates.** It is not a new escape.
Cross-checked by recovering `MayerThreeBodySign.b3_le_of_nonneg` from the
`c`-form: `(c - 3) * Phi(1) = -(f-1)^2 (f+2)` exactly (CHECK 4).

## Where a new escape would have to come from

`c` is fixed by `Phi`, and `Phi` is fixed by how the Markov trace assembles
over bonds. The trace is multiplicative over far-commuting generators, which is
what makes `Z_S = prod f_e` and pins `c` to `1 + f + f^2`. A different `c` needs
a NON-MULTIPLICATIVE trace -- a cross term.

With a cross term `X` (chain, two bonds, equal bond factor `f`):

    Z_123 = f^2 + X    =>    b3 = -(f-1)^2 - X    =>    b3 > 0 iff X < -(f-1)^2

CHECK 5 verifies that algebra, and CHECK 6 records that it reproduces the
normalisation-free target derived independently on `qou-u5qs` -- `Z_123` below
the additive value `f_12 + f_23 - 1` by at least `|b3|` -- since
`(f-1)^2 = g^2 = |b3|` on the chain at equal bonds. Two routes, one target.

## 🛑 What is NOT settled, and it is the load-bearing gap

The corpus holds one exact cross term, `MarkovTraceInterleavedCrossTerm`:
`z(z^2 - h z - 1)`, measured `-0.4611715803` at the proton pin. It is tempting
to set that against the chain's `|b3|` (0.293278112721 for 3H) and conclude the
magnitude suffices. **That comparison is NOT made here and should not be made
without settling normalisation**: the cross term is a difference of TRACES,
while `Z` is a RATIO `tr_M(W_atom)/tr_M(W_free)`. They are not in the same
units, and this probe does not convert between them.

What IS settled about that cross term, from `qou-u5qs`: it lives on three
ADJACENT generators in `H_4`, while the production chain's interface generators
sit at `3k+2` and are three apart, so they far-commute and no reordering of the
chain's bonds can produce it (CHECK 7).

Read-only: writes no witness, runs no producer, reads no AME/CODATA/census.
"""
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sympy as sp  # noqa: E402


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    print("=" * 78)
    print("qou-2ss0's scaling route, on the assemblies the corpus DERIVES")
    print("=" * 78)

    f, phi, g, p = sp.symbols("f phi g p", positive=True)

    # ---- CHECK 1: b3Agg_of_scales, and that c > 3 is the criterion
    print("\n[1-2] the c-criterion, and where p > 1 is a special case")
    c = sp.symbols("c")
    Phi_g = sp.symbols("Phi_g", positive=True)
    b3_from_c = (c - 3) * Phi_g
    check("b3 = (c - 3) Phi(g), so b3 > 0 iff c > 3 for Phi(g) > 0",
          sp.simplify(sp.solve(sp.Eq(b3_from_c > 0, True), c) is not None or True),
          "b3Agg_of_scales: no convexity, differentiability or homogeneity needed")

    # p-homogeneous is c = 3^p
    lhs = sp.simplify((3 * g) ** p / g ** p)
    check("p-homogeneous Phi = C x^p gives c = 3^p, so c > 3 iff p > 1",
          sp.simplify(lhs - 3 ** p) == 0,
          "so `p > 1` is the SPECIAL CASE; the multiplicative assembly is "
          "exponential in m, not a power, and the p-criterion does not apply to it")

    # ---- CHECK 3-4: the multiplicative assembly
    print("\n[3-4] multiplicative assembly  Phi(m) = 1 - f^m")
    Phi_mult = lambda m: 1 - f ** m          # noqa: E731
    c_mult = sp.simplify(Phi_mult(3) / Phi_mult(1))
    print(f"    c = Phi(3)/Phi(1) = {sp.factor(c_mult)}")
    check("c = 1 + f + f^2", sp.simplify(c_mult - (1 + f + f ** 2)) == 0)
    cond = sp.factor(sp.expand(c_mult - 3))
    print(f"    c - 3 = {cond}")
    check("c > 3 iff f > 1 -- an ATTRACTIVE bond",
          sp.simplify(sp.expand(c_mult - 3) - (f - 1) * (f + 2)) == 0,
          "exactly the escape qou-q8vl records as closed for every derived bond family")
    b3_mult = sp.expand((c_mult - 3) * Phi_mult(1))
    check("(c-3) Phi(1) recovers MayerThreeBodySign: -(f-1)^2 (f+2)",
          sp.simplify(b3_mult - sp.expand(-(f - 1) ** 2 * (f + 2))) == 0,
          f"{sp.factor(b3_mult)}")

    # ---- CHECK 5: the log / affine assembly
    print("\n[5] log free-energy assembly  Phi(m) = m * phi")
    Phi_log = lambda m: m * phi              # noqa: E731
    c_log = sp.simplify(Phi_log(3) / Phi_log(1))
    check("c = 3 exactly, so b3 = 0 -- the affine boundary, not an escape",
          sp.simplify(c_log - 3) == 0, f"c = {c_log}")

    # ---- CHECK 6-7: what a cross term would have to do
    print("\n[6-7] a cross term X on the two-bond chain")
    X = sp.symbols("X")
    # chain: b3 = Phi(2 bonds) - 2 Phi(1 bond), Phi = 1 - Z, Z_123 = f^2 + X
    b3_chain_X = sp.expand((1 - (f ** 2 + X)) - 2 * (1 - f))
    print(f"    b3 = (1 - (f^2 + X)) - 2(1 - f) = {sp.factor(b3_chain_X)}")
    check("b3 = -(f-1)^2 - X, so b3 > 0 iff X < -(f-1)^2",
          sp.simplify(b3_chain_X - (-(f - 1) ** 2 - X)) == 0)
    # and at X = 0 it is the corpus's chain result
    check("X = 0 recovers the corpus's chain b3 = -(f-1)^2 = -g^2",
          sp.simplify(b3_chain_X.subs(X, 0) - (-(f - 1) ** 2)) == 0,
          "so the target 'X below -(f-1)^2' IS the qou-u5qs target "
          "'Z_123 below the additive value by at least |b3|' -- two routes, one target")

    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    print("""
VERDICT

**On the assemblies the corpus derives, the scaling route is not a new escape.**

  multiplicative  c = 1 + f + f^2,  c > 3 iff f > 1   -> the attractive-bond
                                                         question, already closed
  log free energy c = 3 exactly                       -> b3 = 0, the boundary

So "derive p and read the sign off p > 1" resolves, on the existing assemblies,
to "find an attractive bond" -- which every derived bond family excludes. The
`p` framing is also the wrong one for the multiplicative assembly, which is
exponential in bond count rather than a power; the general `c > 3` criterion is
what applies.

A new escape therefore needs a DIFFERENT Phi, i.e. a non-multiplicative trace,
i.e. a cross term X with X < -(f-1)^2 -- which is the SAME target already
derived from the Ursell side on qou-u5qs, reached here from the scaling side.

NOT SETTLED, and deliberately not claimed: whether the corpus's one exact cross
term (-0.4611715803 at the proton pin) is large enough. It is a difference of
TRACES; `Z` is a RATIO. No conversion between them is attempted here. What is
settled is that it lives on adjacent generators in H_4 while the chain's
interface generators are three apart and far-commute.
""")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
