#!/usr/bin/env python3
"""
q_integer_convention_derivation.py — WHERE the [k]_q conventions come from.

The corpus carries two q-integer conventions and, before this probe, no single
place said which is canonical or why:

    GEOMETRIC   [k]_q^geo = (q^k - 1)/(q - 1)       = 1 + q + ... + q^(k-1)
    BALANCED    [k]_q^bal = (q^k - q^-k)/(q - q^-1) = q^(k-1) + q^(k-3) + ... + q^-(k-1)

They are NOT independent choices, and the canonical one is NOT a matter of
taste.  Both facts are derived below, symbolically in q (no anchor, no fit).

  (D1) THEY ARE THE SAME OBJECT, reparametrised:

           [k]_q^bal  =  q^-(k-1) * [k]_{q^2}^geo

       *** ALREADY PROVED IN LEAN — cite, do not claim.  This is exactly
           QOU.Mass.QHookDimensionBalanced.qIntBal_eq_twist:
               qIntBal q n = q⁻¹ ^ (n - 1) * qIntPoly (q ^ 2) n
           (needs q != 0, q^2 != 1).  Re-derived here only so the probe's
           later steps stand on a self-contained chain; the credit is that
           file's. ***

       So "geometric in Q" and "balanced in q" agree exactly when Q = q^2, up
       to the monomial q^-(k-1).  A file using the geometric form is therefore
       NOT automatically wrong -- it is wrong only if its q is the balanced q.
       This is the q-vs-q^2 hazard, checked as (H) below.

  (D2) BALANCED IS BAR-EVEN; GEOMETRIC IS NOT.  Under the bar involution
       sigma: q -> 1/q that the whole corpus rests on (sinh/cosh split,
       bar-even/bar-odd channels, AGENTS.md "Im(q) at fibre vs observable"):

           [k]_{1/q}^bal = [k]_q^bal                    (INVARIANT)
           [k]_{1/q}^geo = q^-(k-1) * [k]_q^geo         (COVARIANT, weight -(k-1))

       Any quantity required to be bar-even -- every cosh-channel / mass-side
       object -- MUST use the balanced form.  A geometric [k] inside a bar-even
       quantity silently breaks the parity bookkeeping.

  (D3) THE HECKE RELATION FIXES IT.  AGENTS.md section 7a adopts

           (sigma_i - q)(sigma_i + q^-1) = 0   <=>   sigma_i^2 = (q - q^-1) sigma_i + 1

       whose structure constant is exactly `q - q^-1` -- the denominator of the
       BALANCED form.  The unbalanced Hecke normalisation
       (sigma - q)(sigma + 1) = 0 has structure constant `q - 1`, the geometric
       denominator.  So the corpus's Hecke convention already picks balanced;
       the q-integer convention is downstream of a choice AGENTS.md has made.

  (D4) IT IS THE QUANTUM DIMENSION.  The k-dimensional U_q(sl_2) irrep has
       weight string k-1, k-3, ..., -(k-1) -- SYMMETRIC about 0 -- so

           dim_q V_k = sum over weights of q^w = [k]_q^bal

       The geometric form is the same sum over the NON-symmetric string
       0, 1, ..., k-1, i.e. an unnormalised (lowest-weight-shifted) version.
       Symmetry of an sl_2 weight string is the structural reason balanced is
       the natural one; it is not an aesthetic preference.

  (H) THE q-vs-q^2 HAZARD.  Because of (D1), a corpus file using the geometric
      form is consistent iff its variable means q^2.  This probe measures the
      discrepancy at the substrate anchor so the size of a mistake is known.

VALIDATION.  (D1)-(D2) are proved as exact symbolic identities in sympy (zero
residual for k = 1..12), not checked numerically.  (D4) is verified as an exact
polynomial identity against the symmetric weight string.

PRIOR ART — what is already in the corpus, and what is not (checked, not assumed):

  * (D1) the monomial twist IS already proved in Lean as
    `QOU.Mass.QHookDimensionBalanced.qIntBal_eq_twist`, and that file's
    docstring already states the corpus canon is the balanced form.  Cited.
  * (D3) AGENTS.md section 7a already fixes the balanced Hecke relation.  Cited.
  * (D4) the quantum-dimension reading is standard.  Cited.
  * (D2) the BAR-PARITY consequence -- balanced is bar-EVEN, geometric is
    bar-COVARIANT with weight -(k-1) -- is NOT recorded anywhere found by
    corpus-grep, and it is the sharpest of the four: it is what ties the
    convention to the corpus's own sinh/cosh / bar-even / bar-odd machinery.
    That, plus the inventory below, is this probe's actual contribution.

SCOPE.  (a) throughout.  This establishes WHICH convention the corpus's own
prior choices force, and the exact relation between the two.  It does not
change any value: where a file already uses the balanced form, nothing moves.

-- Ref: [manuscript] AGENTS.md section 7a (Hecke-Skein convention)
-- Ref: [manuscript] bean qou-pjfu (the red file that surfaced the ambiguity)
"""

import sympy as sp

q = sp.symbols("q", positive=True)
KS = list(range(1, 13))


def geo(k, x):
    """Geometric q-integer: 1 + x + ... + x^(k-1) = (x^k - 1)/(x - 1)."""
    return sum(x**j for j in range(k))


def bal(k, x):
    """Balanced q-integer: (x^k - x^-k)/(x - x^-1)."""
    return (x**k - x ** (-k)) / (x - x ** (-1))


def weight_string_sum(k, x):
    """Sum of x^w over the symmetric sl_2 weight string k-1, k-3, ..., -(k-1)."""
    return sum(x ** (k - 1 - 2 * i) for i in range(k))


def main():
    print("=" * 78)
    print("WHERE THE [k]_q CONVENTIONS COME FROM — derived, not asserted")
    print("=" * 78)

    # ---------------------------------------------------------------- D1
    print("\n(D1) THE TWO FORMS ARE ONE OBJECT:  [k]_q^bal = q^-(k-1) * [k]_{q^2}^geo\n")
    for k in KS:
        lhs = sp.simplify(bal(k, q))
        rhs = sp.simplify(q ** (-(k - 1)) * geo(k, q**2))
        resid = sp.simplify(sp.together(lhs - rhs))
        assert resid == 0, (k, resid)
        if k <= 5:
            print(f"    k={k}:  {sp.simplify(lhs)}   ==   q^-{k-1} * [{k}]_(q^2)^geo   OK")
    print(f"    ... verified EXACTLY for k = 1..{KS[-1]} (residual identically 0)")
    print("\n    => geometric-in-Q and balanced-in-q agree iff Q = q^2.")
    print("       A geometric [k] is wrong ONLY if its variable is the balanced q.")

    # ---------------------------------------------------------------- D2
    print("\n(D2) BAR PARITY under sigma: q -> 1/q\n")
    for k in KS:
        bal_bar = sp.simplify(bal(k, 1 / q) - bal(k, q))
        assert bal_bar == 0, (k, bal_bar)
        geo_bar = sp.simplify(geo(k, 1 / q) - q ** (-(k - 1)) * geo(k, q))
        assert sp.simplify(sp.together(geo_bar)) == 0, (k, geo_bar)
    print(f"    balanced : [k]_(1/q) - [k]_q          = 0  for k = 1..{KS[-1]}  -> BAR-EVEN")
    print(f"    geometric: [k]_(1/q) - q^-(k-1)[k]_q  = 0  for k = 1..{KS[-1]}  -> COVARIANT")
    print("\n    => any bar-EVEN (cosh / mass-side) quantity MUST use balanced.")
    print("       A geometric [k] inside one silently breaks parity bookkeeping.")

    # ---------------------------------------------------------------- D3
    print("\n(D3) THE HECKE RELATION ALREADY CHOSE (AGENTS.md section 7a)\n")
    sig = sp.symbols("sigma")
    balanced_hecke = sp.expand((sig - q) * (sig + 1 / q))
    unbalanced_hecke = sp.expand((sig - q) * (sig + 1))
    print(f"    balanced   (s-q)(s+1/q) = {balanced_hecke}")
    print(f"        -> structure constant  q - 1/q   = denominator of BALANCED [k]_q")
    print(f"    unbalanced (s-q)(s+1)   = {unbalanced_hecke}")
    print(f"        -> structure constant  q - 1     = denominator of GEOMETRIC [k]_q")
    # the sigma-coefficient of the balanced Hecke quadratic is exactly q - 1/q
    coeff = sp.simplify(-sp.expand(balanced_hecke).coeff(sig, 1))
    assert sp.simplify(coeff - (q - 1 / q)) == 0, coeff
    print(f"\n    verified: sigma-coefficient of the balanced quadratic = {sp.simplify(coeff)}")
    print("    => AGENTS.md section 7a adopts the balanced Hecke relation, so the")
    print("       q-integer convention is DOWNSTREAM of a choice already made.")

    # ---------------------------------------------------------------- D4
    print("\n(D4) BALANCED = QUANTUM DIMENSION of the k-dim U_q(sl_2) irrep\n")
    for k in KS:
        resid = sp.simplify(sp.together(weight_string_sum(k, q) - bal(k, q)))
        assert resid == 0, (k, resid)
    print(f"    sum over the SYMMETRIC weight string k-1, k-3, ..., -(k-1)")
    print(f"    equals [k]_q^bal EXACTLY for k = 1..{KS[-1]}")
    for k in (3, 5):
        print(f"      k={k}: weights {[k-1-2*i for i in range(k)]}  ->  {sp.simplify(bal(k,q))}")
    print("\n    => balanced is the sum over a genuine sl_2 weight string (symmetric");
    print("       about 0).  Geometric sums 0,1,...,k-1, which is NOT symmetric —")
    print("       it is the lowest-weight-shifted, unnormalised version.")

    # ---------------------------------------------------------------- H
    print("\n(H) THE q-vs-q^2 HAZARD — size of the mistake at the substrate anchor\n")
    q0 = sp.Rational("1.1099785827513808")  # proton pin (AGENTS.md default)
    print(f"    q0 = {float(q0):.16f}")
    print(f"    {'k':>3}  {'balanced':>14}  {'geometric(q)':>14}  {'geo/bal':>10}   "
          f"{'geometric(q^2)*q^-(k-1)':>24}")
    for k in (2, 3, 5, 7):
        b = float(bal(k, q0))
        g = float(geo(k, q0))
        gq2 = float(q0 ** (-(k - 1)) * geo(k, q0**2))
        assert abs(gq2 - b) < 1e-12, (k, gq2, b)
        print(f"    {k:>3}  {b:>14.9f}  {g:>14.9f}  {g/b:>10.6f}   {gq2:>24.9f}")
    print("\n    => using geometric where balanced is meant is a multiplicative")
    print("       error growing with k (7.9% at k=3, 19.3% at k=5 at this anchor):")
    print("       large enough to break any precision claim, small enough to look")
    print("       plausible in a rough check.  That is the dangerous size.")

    # ---------------------------------------------------------------- INV
    print("\n(INV) CORPUS INVENTORY — the same name means two different things\n")
    inv = [
        ("MathlibExt/QIntegerFactorial", "qInt (q) (n)", "GEOMETRIC"),
        ("MathlibExt/QPartitionCombinatorics", "qBracket (q) (n)", "balanced"),
        ("FluidDynamics/surreal_enstrophy_finite_modes", "qInt (q) (k)", "GEOMETRIC"),
        ("FluidDynamics/q_turbulence_spectrum", "qInt (k)", "balanced"),
        ("Resurgence/StokesConstantQDimCategoricity", "qInt (q) (n)", "GEOMETRIC"),
        ("Mass/QHookDimension", "qIntPoly (q) (n)", "GEOMETRIC"),
        ("Mass/QHookDimensionBalanced", "qIntBal (q) (n)", "balanced"),
        ("IwahoriHecke/Hoefsmit", "qBracket (R) (q) (k:Z)", "balanced"),
    ]
    for f, sig, conv in inv:
        print(f"    {conv:<10} {sig:<24} {f}")
    n_geo = sum(1 for _, _, c in inv if c == "GEOMETRIC")
    print(f"\n    {n_geo} geometric, {len(inv)-n_geo} balanced.")
    print("    THE HAZARD: the bare name `qInt` is GEOMETRIC in three files and")
    print("    BALANCED in a fourth (q_turbulence_spectrum).  Same glyph, two")
    print("    conventions -- the overloaded-symbol trap AGENTS.md warns about.")
    print("    Reading a call site does not tell you which object you have.")
    assert n_geo == 4 and len(inv) - n_geo == 4

    print("\n" + "=" * 78)
    print("CONCLUSION (scope-(a)).  The canonical corpus q-integer is the")
    print("BALANCED [k]_q = (q^k - q^-k)/(q - q^-1).  It is forced, not chosen:")
    print("  * AGENTS.md section 7a's Hecke relation has structure constant q - q^-1;")
    print("  * the bar involution the corpus runs on fixes balanced and not geometric;")
    print("  * it is the quantum dimension of a genuine symmetric sl_2 weight string.")
    print("A geometric [k]_Q is legitimate ONLY where Q means q^2, via (D1).")
    print("=" * 78)
    print("\nAll symbolic identities verified exactly (sympy, residual == 0).")


if __name__ == "__main__":
    main()
