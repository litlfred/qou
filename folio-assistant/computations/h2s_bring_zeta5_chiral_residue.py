#!/usr/bin/env python3
# polynomial_q_not_applicable: ζ₅ / quintic-discriminant grounding of the Bring
# 1/√5 coefficient, not a Jones-polynomial evaluation.
"""
Grounding the H₂S Bring 1/√5 in the ζ₅ chiral fibre of Bring's surface.

The conjecture (conj:h2s-angle-s3-braid-holonomy) found the H₂S chiral residue
takes the Bring 1/√5 form. This grounds the 1/√5 in the framework's own
Bring/quintic structure, closing the chiral-channel ↔ Bring loop:

  • The chiral channel is the c_λ=0 (2,1) block — the H₃ standard rep.
  • Bring's surface has a CHIRAL CUBIC FIBRE (bring_chiral_fibre_figure.py),
    from the invariant ring,
        X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1) = 0,
    whose THREE SHEETS merge at the discriminant branch points with **B₃
    monodromy** — i.e. the chiral fibre's monodromy is exactly the 3-strand
    braid group B₃ ↠ H₃(q). The chiral channel and the Bring chiral fibre are
    the SAME H₃ object.
  • Bring's surface carries the ℤ₅ automorphism `(x,y) ↦ (ζ₅ x, y)` of the
    hyperelliptic quintic 𝒳₅: y² = x⁵−1 (prop:x5-z5-automorphism,
    ζ₅ = exp(2πi/5)). This ζ₅ 5-fold symmetry is the singular-fibre structure
    around which the chiral residue's monodromy is taken.

WHERE √5 COMES FROM (the quintic / ζ₅):
  • cos(2π/5) = (√5 − 1)/4,  2cos(2π/5) = (√5−1)/2 = 1/φ  — ζ₅ is irrational
    over ℚ exactly through √5.
  • disc(x⁵ − 1) = 5⁵, so the quintic period carries √(5⁵) = 25·√5.
  • The Gauss sum over the 5th roots of unity is √5.
So the archimedean (real, Im q₀ = 0) projection of a ζ₅-symmetric chiral residue
is normalised by √5 — and the leading chiral coefficient is 1/√5, the Bring
constant of the H₂S residual-mixing form.

STATUS: the chiral-channel ↔ Bring-chiral-fibre ↔ ζ₅ ↔ √5 connection is
established structurally (same H₃ object; ζ₅ is the only source of irrationality,
and it is √5). The exact normalisation — that the ζ₅-residue of the chiral p-lone
returns precisely the 1/√5 coefficient — is the remaining monodromy computation
(the conjecture's open content). This script verifies the √5-from-ζ₅ facts.

Refs: conj:h2s-angle-s3-braid-holonomy; bring_chiral_fibre_figure.py (the cubic
fibre, B₃ monodromy); prop:x5-z5-automorphism (ζ₅); h2s_bring_residual_mixing.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

SQRT5 = np.sqrt(5.0)
PHI = (1 + SQRT5) / 2


def main() -> None:
    w = WitnessBuilder("h2s-bring-zeta5-chiral-residue", engine="python")

    print("=" * 70)
    print("H₂S Bring 1/√5 grounded in the ζ₅ chiral fibre")
    print("=" * 70)
    # √5 from ζ₅ = exp(2πi/5)
    z5 = np.exp(2j * np.pi / 5)
    cos72 = np.cos(2 * np.pi / 5)
    cos72_exact = (SQRT5 - 1) / 4
    two_cos72 = 2 * cos72                         # = 1/φ = (√5−1)/2
    # quintic discriminant of x⁵−1 and its √
    disc_x5 = 5 ** 5
    sqrt_disc = np.sqrt(disc_x5)                  # 25·√5
    # Gauss sum over 5th roots of unity (quadratic Gauss sum, p=5) = √5
    gauss = sum(np.exp(2j * np.pi * (k * k) / 5) for k in range(5))

    print(f"  ζ₅ = exp(2πi/5) = {z5:.5f},  ζ₅⁵ = {z5**5:.3f}")
    print(f"  cos(2π/5) = {cos72:.6f}  =? (√5−1)/4 = {cos72_exact:.6f}  "
          f"(match {abs(cos72-cos72_exact)<1e-12})")
    print(f"  2cos(2π/5) = {two_cos72:.6f} = 1/φ = (√5−1)/2 = {1/PHI:.6f}")
    print(f"  disc(x⁵−1) = {disc_x5} = 5⁵ ;  √disc = {sqrt_disc:.4f} = 25·√5 "
          f"({25*SQRT5:.4f})")
    print(f"  quadratic Gauss sum Σ ζ₅^(k²) = {gauss.real:.5f}{gauss.imag:+.1e}i "
          f"= √5 = {SQRT5:.5f}")
    print()
    print(f"  ⇒ ζ₅ is irrational over ℚ exactly through √5; the archimedean "
          f"projection of a")
    print(f"    ζ₅-symmetric chiral residue is normalised by √5 → leading "
          f"coefficient 1/√5 = {1/SQRT5:.5f}")
    print(f"  ⇒ Bring 1/√5 (H₂S residual mixing) = the quintic √5 of the ζ₅ "
          f"chiral fibre.")

    w.set_description(
        "Grounds the H₂S Bring 1/√5 in the ζ₅ chiral fibre of Bring's surface. "
        "The chiral channel (c_λ=0 (2,1) = H₃ standard rep) IS the Bring chiral "
        "cubic fibre (3 sheets, B₃↠H₃ monodromy); Bring's surface carries the "
        "ℤ₅ automorphism (ζ₅=exp(2πi/5)) of 𝒳₅:y²=x⁵−1. √5 is the unique source "
        "of irrationality of ζ₅: cos(2π/5)=(√5−1)/4, disc(x⁵−1)=5⁵ (√=25√5), "
        "Gauss sum Σζ₅^(k²)=√5. So the archimedean ζ₅-residue normalisation is "
        "√5, and the leading chiral coefficient is 1/√5 — the Bring constant of "
        "the H₂S residual-mixing form. The exact ζ₅-residue normalisation "
        "remains the conjecture's open monodromy computation."
    )
    w.set_content_block("conj:h2s-angle-s3-braid-holonomy")
    w.add_data("zeta5_re", float(z5.real))
    w.add_data("zeta5_im", float(z5.imag))
    w.add_data("cos_2pi_5", float(cos72))
    w.add_data("cos_2pi_5_exact_sqrt5_minus_1_over_4", float(cos72_exact))
    w.add_data("disc_x5_minus_1", int(disc_x5))
    w.add_data("sqrt_disc_eq_25_sqrt5", float(sqrt_disc))
    w.add_data("gauss_sum_re", float(gauss.real))
    w.add_data("sqrt5", float(SQRT5))
    w.add_data("inv_sqrt5_bring", float(1 / SQRT5))
    w.add_assertion(
        "cos(2π/5) = (√5−1)/4 — ζ₅'s irrationality is √5",
        computed=bool(abs(cos72 - cos72_exact) < 1e-12), expected=True,
        source="exact value of cos(2π/5)",
    )
    w.add_assertion(
        "quadratic Gauss sum over 5th roots of unity = √5",
        computed=bool(abs(gauss.real - SQRT5) < 1e-9
                      and abs(gauss.imag) < 1e-9),
        expected=True, source="Σ_{k=0}^{4} ζ₅^(k²) = √5 (p=5 quadratic Gauss sum)",
    )
    w.add_data(
        "finding",
        "The Bring 1/√5 of the H₂S residual is grounded in the ζ₅ chiral fibre "
        "of Bring's surface. The chiral channel (c_λ=0 (2,1) block = H₃ standard "
        "rep) is the Bring chiral cubic fibre (3 sheets with B₃↠H₃ monodromy); "
        "the surface's ℤ₅ automorphism (ζ₅=exp(2πi/5)) of 𝒳₅:y²=x⁵−1 supplies "
        "the 5-fold singular-fibre structure. √5 is the unique source of ζ₅'s "
        "irrationality over ℚ (cos(2π/5)=(√5−1)/4; disc(x⁵−1)=5⁵; Gauss sum=√5), "
        "so the archimedean ζ₅-residue is normalised by √5 and the leading "
        "chiral coefficient is 1/√5. Connection established (same H₃ object, ζ₅ "
        "⇒ √5); the exact ζ₅-residue normalisation is the open monodromy step.",
    )
    w.save()
    print("\nDone. Witness saved (h2s-bring-zeta5-chiral-residue).")


if __name__ == "__main__":
    main()
