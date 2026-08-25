#!/usr/bin/env python3
"""
Habiro-ring WRT(S³/2I) q-series push — the residual keystone frontier.

The modular-category identification (`2026-06-22-keystone-modular-category-identification.md`)
located the residual open object as: the explicit Habiro-ring WRT invariant of the
Poincaré sphere S³/2I = Σ(2,3,5), evaluated at the substrate, vs the q-Plancherel
weights W_λ.

FORMULA (pinned from the literature, NOT guessed — Lawrence–Zagier 1999; Hikami,
"Quantum Invariant, Modular Form, and Lattice Points"; arXiv:1811.05376,
arXiv:2205.01282): the WRT invariant of Σ(2,3,5) is governed by the false theta

    Ψ(q) = Σ_{a∈{1,11,19,29}} Ψ̃_30^{(a)}(q),   Ψ̃_P^{(a)}(q) = Σ_{n≥0} ψ_{2P}^{(a)}(n) q^{n²/(4P)}

with P=30 (⇒ 4P=120), and ψ the ODD periodic function mod 60:

    χ(n) = +1  for n ≡ 1, 11, 19, 29   (mod 60)
    χ(n) = −1  for n ≡ 31, 41, 49, 59   (mod 60)   [ = 60 − {29,19,11,1}, the odd extension]
    χ(n) =  0  otherwise.

The support residues {1,11,19,29} are the icosahedral/E₈ data of Σ(2,3,5)
(P=30 = Coxeter number of E₈). Exponent q^{n²/120} (an overall q^{±1/120}
normalisation is convention-dependent and does not affect structure/ratios).

KEY REGIME FACT: Ψ(q) converges only for |q| < 1 (roots of unity on the boundary).
The substrate q₀ = 1.10998 is OUTSIDE (>1). Its BAR IMAGE 1/q₀ ≈ 0.901 is INSIDE.
So the type-correct evaluation uses the q↦q⁻¹ involution (ubiquitous in this corpus):
Ψ(1/q₀). This probe computes it and compares — type-correctly, no forcing — to the
W_λ-derived scalars.

DISCIPLINE: no fit to any target; report the value + structure; the bare Σ(2,3,5)
invariant is ONE number while W_λ is a λ-family ⇒ a direct equality is a type
mismatch and is NOT claimed.
"""
import sys
from pathlib import Path

from mpmath import mp, mpf, nstr

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0 = mpf("1.1099785955541805")
INV = 1 / Q0   # bar image, inside the unit disk


def chi60(n):
    r = n % 60
    if r in (1, 11, 19, 29):
        return 1
    if r in (31, 41, 49, 59):
        return -1
    return 0


def false_theta(q, nterms=4000):
    """Ψ(q) = Σ_{n≥0} χ(n) q^{n²/120}; converges for |q|<1.

    Uses `mp.fsum` over the term list (not a running `+=`) to avoid
    intermediate-rounding precision loss in the high-precision mpf sum."""
    terms = [chi60(n) * q ** (mpf(n * n) / 120) for n in range(nterms) if chi60(n)]
    return mp.fsum(terms)


def weight32_theta(q, nterms=4000):
    """The weight-3/2 partner Θ(q)=Σ n·χ(n) q^{n²/120} (Eichler-integral source)."""
    terms = [chi60(n) * n * q ** (mpf(n * n) / 120) for n in range(nterms) if chi60(n)]
    return mp.fsum(terms)


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def q_factorial(m):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def d_q(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h)
    return q_factorial(sum(lam)) / den


def main():
    print(f"q_0 = {Q0}  (>1, growth regime, OUTSIDE unit disk)")
    print(f"1/q_0 = {nstr(INV,12)}  (bar image, INSIDE unit disk)\n")

    # convergence check: |q|<1 needed
    psi = false_theta(INV)
    theta = weight32_theta(INV)
    # tail estimate
    psi_short = false_theta(INV, 1200)
    print("Lawrence–Zagier false theta of Σ(2,3,5), evaluated at the bar image 1/q_0:")
    print(f"  Ψ(1/q_0)          = {nstr(psi, 20)}")
    print(f"  Ψ(1/q_0) [1200 t] = {nstr(psi_short, 20)}   (tail |Δ| = {nstr(abs(psi-psi_short),4)})")
    print(f"  Θ_{{3/2}}(1/q_0)    = {nstr(theta, 20)}   (weight-3/2 partner)")
    print()

    # also at a root-of-unity-adjacent small q for a structural sanity value
    for qq in ("0.5", "0.9", "0.99"):
        print(f"  Ψ({qq}) = {nstr(false_theta(mpf(qq)), 14)}")
    print()

    # W_λ-derived scalars at q_0 (n=5)
    PARTS = [(5,), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1)]
    D2 = mp.fsum(d_q(l) ** 2 for l in PARTS)
    nfac = q_factorial(5)
    print("W_λ-derived scalars at q_0 (n=5):")
    print(f"  [5]_q!          = {nstr(nfac,14)}")
    print(f"  D² = Σ d_q²     = {nstr(D2,14)}")
    print(f"  d_q(3,1,1)      = {nstr(d_q((3,1,1)),14)}  (electron)")
    print(f"  d_q(3,2)        = {nstr(d_q((3,2)),14)}  (muon)")
    print()

    print("Type-correct assessment (NO forcing):")
    print(f"  • Ψ(1/q_0) ≈ {nstr(psi,8)} is ONE manifold invariant; W_λ is a λ-FAMILY.")
    print( "    A direct Ψ = W_λ equality is a type mismatch and is NOT asserted.")
    print( "  • The link is STRUCTURAL: the support residues {1,11,19,29 mod 60} are the")
    print( "    icosahedral/E₈ data (P=30=h(E₈)) — the SAME icosahedral input that the")
    print( "    A₅ ⊂ SO(3) fibre map and the W_λ blocks carry. The bare Σ(2,3,5) invariant")
    print( "    selects that modular data; the λ-RESOLVED weights need the WRT TQFT with")
    print( "    λ-COLOURED insertions (colored invariants / S-matrix), not the closed-manifold")
    print( "    number computed here.")
    print( "  • REGIME bridge: the substrate q_0>1 (growth) and the WRT series |q|<1 (rotation)")
    print( "    are joined by the q↦q⁻¹ bar involution (q_0 ↔ 1/q_0), which is the same bar")
    print( "    structure the whole c_k / Reeb-phase corpus runs on. The Habiro ring is the")
    print( "    object that makes BOTH sides one element (root-of-unity AND generic).")
    print("\nWRT q-series PUSH COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
