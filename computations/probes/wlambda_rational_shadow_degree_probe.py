#!/usr/bin/env python3
"""
Probe — how many values would actually pin the `W_λ` candidate, and how many the
Σ(2,3,5) geometry can supply?

Companion to `QOU/BraidKnot/PolynomialShadowRigidity.lean`, which proves
(sorry-free) that a polynomial / rational shadow is determined by its values at
*all* roots of unity. That theorem is unconditional, but it consumes infinitely
many values. The interpolation probe `habiro_interpolation_wlambda.py` has five.
This probe measures the gap, so the Lean file's docstring table is CHECKED rather
than asserted.

## The candidate

    F_λ(q) = [mark λ]²_q / D(q)²,      D(q)² = Σ_{9 McKay nodes} [mark μ]²_q

with affine-Ê₈ marks `1,2,3,4,5,6,4,2,3`. Since `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`,
the `(q − q⁻¹)` factors cancel between numerator and denominator, leaving a ratio
of Laurent polynomials with integer coefficients:

    F_λ(q) = (q^m − q^{−m})² / Σ_μ (q^{m_μ} − q^{−m_μ})²

Clearing the pole at `q = 0` and reducing by the polynomial gcd gives a genuine
reduced rational function `N/D`, and a rational function of that shape is pinned
by `deg N + deg D + 1` values. That count is computed exactly below (sympy over
ℤ — no floats anywhere, nothing to serialize).

Both relevant objects are measured, because they are easy to conflate and were:
the 9-node McKay `F_λ` above, and the keystone's **n=5 vacuum row**
`S_0λ² = d_λ²/Σ_μ d_μ²` with `d_q = ([1]_q, [4]_q, [5]_q, [4]_q[3]_q/[2]_q)`.
They are different objects with different degrees — 31..41 and 25..33 values
respectively — against the same supply of 5.

## The supply side, which is fixed by the geometry

The Poincaré sphere Σ(2,3,5) has exactly three exceptional fibres
`(p₁,p₂,p₃) = (2,3,5)` and exactly two irreducible SU(2) flat connections
(`D(2,3,5) = 2`, Fintushel–Stern), with rotation numbers `ℓ_j^{(m)}`. Both
connections have `ℓ₂ = ℓ₃ = 1`, so orders 2 and 3 contribute ONE root each and
order 5 contributes TWO (the Galois pair) — four nontrivial roots, plus `q = 1`.
Five. This is not a computation budget; it is the whole of the fibre data.

## What this settles

Scope-(a), and it is a statement about the FIBRE DATA, not about the route: the
root-of-unity values available from Σ(2,3,5) fall short of elementary rational
rigidity by a wide, computed margin. So "rigidity ⇒ no fit" cannot be sourced
from the fibre data alone; it needs either many more independent values from some
other source, or a bridge to an object with values at ALL roots of unity — at
which point `PolynomialShadowRigidity.lean` supplies the rigidity outright and
Habiro's theorem is not required.

This refutes no route and excludes no ingredient. It also does NOT claim the
five known values are uninformative: they constrain, exactly as
`habiro_interpolation_wlambda.py` says. The claim is only that constraining is
not pinning, with the shortfall quantified.

NO WITNESS: exact integer polynomial arithmetic, reproduced by the printed table;
nothing here feeds production.

Bean qou-uqen.
"""
from __future__ import annotations

import sys

import sympy as sp

# affine-Ê₈ McKay marks (dims of the 2I irreps); Σ mark² = 120 = |2I|.
MARKS = [1, 2, 3, 4, 5, 6, 4, 2, 3]

# Σ(2,3,5): 3 exceptional fibres, 2 flat connections, ℓ₂ = ℓ₃ = 1 for both.
N_ROOTS_FROM_FIBRES = 4      # orders 2,3 give one root each; order 5 gives two
N_VALUES_AVAILABLE = N_ROOTS_FROM_FIBRES + 1     # + the classical point q = 1


def main() -> int:
    q = sp.symbols("q")

    def sq(m: int):
        """(q^m - q^-m)^2 — the numerator shape after the [n]_q pole cancels."""
        return (q ** m - q ** (-m)) ** 2

    D2 = sum(sq(m) for m in MARKS)

    print("W_lambda rational-shadow degree probe  (bean qou-uqen)\n")
    print("  F_lambda(q) = [mark]^2_q / D(q)^2 ,  D(q)^2 = sum over 9 McKay nodes")
    print(f"  marks = {MARKS}   (sum of squares = {sum(m * m for m in MARKS)} = |2I|)\n")
    print("Reduced rational function per distinct mark (exact, over Z):\n")
    print("| mark | deg num | deg den | values needed to pin |")
    print("| ---: | ------: | ------: | -------------------: |")

    needed = []
    for m in sorted(set(MARKS)):
        F = sp.cancel(sp.together(sq(m) / D2))
        num, den = sp.fraction(sp.cancel(sp.simplify(F)))
        pn, pd = sp.Poly(sp.expand(num), q), sp.Poly(sp.expand(den), q)
        g = sp.gcd(pn, pd)
        pn, pd = sp.div(pn, g)[0], sp.div(pd, g)[0]
        dn, dd = pn.degree(), pd.degree()
        k = dn + dd + 1
        needed.append(k)
        print(f"| {m:>4} | {dn:>7} | {dd:>7} | {k:>20} |")

    # ---- the OTHER object, so the two are never conflated again -------------
    # The keystone's n=5 vacuum row is NOT the 9-node McKay F_lambda above. It is
    # S_0lambda^2 = d_lambda^2 / sum_mu d_mu^2 with the four physical lambda |- 5
    # quantum dimensions. Different object, different degrees. Computed here
    # because an earlier revision of this probe's finding was quoted at the n=5
    # object using the McKay figures — a real mix-up, now impossible to repeat.
    def qint(n: int):
        return (q ** n - q ** (-n)) / (q - q ** (-1))

    d5 = {
        "[1]": sp.Integer(1),
        "[4]": qint(4),
        "[5]": qint(5),
        "[4][3]/[2]": qint(4) * qint(3) / qint(2),
    }
    S5 = sum(sp.together(v ** 2) for v in d5.values())

    print("\nThe n=5 vacuum row — a DIFFERENT object, listed so the two are not conflated:")
    print("  S_0lambda^2 = d_lambda^2 / sum_mu d_mu^2 ,  d_q = ([1],[4],[5],[4][3]/[2])\n")
    print("| lambda      | deg num | deg den | values needed to pin |")
    print("| ----------- | ------: | ------: | -------------------: |")
    needed5 = []
    for name, v in d5.items():
        F = sp.cancel(sp.together(v ** 2 / S5))
        num, den = sp.fraction(sp.cancel(sp.simplify(F)))
        pn, pd = sp.Poly(sp.expand(num), q), sp.Poly(sp.expand(den), q)
        g = sp.gcd(pn, pd)
        pn, pd = sp.div(pn, g)[0], sp.div(pd, g)[0]
        dn, dd = pn.degree(), pd.degree()
        needed5.append(dn + dd + 1)
        print(f"| {name:<11} | {dn:>7} | {dd:>7} | {dn + dd + 1:>20} |")
    print(f"\n  n=5 vacuum row needs {min(needed5)}..{max(needed5)} values; same supply of "
          f"{N_VALUES_AVAILABLE}"
          f"  -> shortfall {min(needed5) - N_VALUES_AVAILABLE}.."
          f"{max(needed5) - N_VALUES_AVAILABLE}")

    lo, hi = min(needed), max(needed)
    print(f"\n  values needed: {lo}..{hi}")
    print(f"  values the Sigma(2,3,5) fibre data can supply: {N_VALUES_AVAILABLE}")
    print(f"    ({N_ROOTS_FROM_FIBRES} nontrivial roots — orders 2,3 give one each and")
    print("     order 5 gives the Galois pair, since l_2 = l_3 = 1 for both flat")
    print("     connections — plus the classical point q = 1)")
    print(f"  shortfall: {lo - N_VALUES_AVAILABLE}..{hi - N_VALUES_AVAILABLE} further"
          " independent values\n")

    short = N_VALUES_AVAILABLE < lo
    print("## Verdict\n")
    if short:
        print("- The fibre data CONSTRAINS but cannot PIN the candidate, and the gap is")
        print("  structural rather than a computation backlog: the Poincare sphere has")
        print("  three exceptional fibres and two flat connections, so five is all there")
        print("  is. Elementary rigidity on the rational shadow needs an order of")
        print("  magnitude more.")
        print("- Consequence for the keystone's 'rigidity => no fit' claim: it cannot be")
        print("  sourced from the fibre data. Either ~26+ further independent values come")
        print("  from somewhere else, or one bridges to an object carrying values at ALL")
        print("  roots of unity — and then PolynomialShadowRigidity.lean gives the")
        print("  rigidity unconditionally, with no appeal to Habiro's theorem.")
        print("- Scope-(a): about what the fibre data can pin. Excludes no ingredient and")
        print("  refutes no route.")
    else:
        print("- The fibre data suffices to pin the candidate. This would be a surprise;")
        print("  re-derive the supply count before acting on it.")

    print("\n(no witness by design — exact integer polynomial arithmetic.)")
    # Non-zero if the shortfall unexpectedly vanishes, so it cannot pass silently.
    return 0 if short else 1


if __name__ == "__main__":
    sys.exit(main())
