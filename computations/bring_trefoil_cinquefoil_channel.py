#!/usr/bin/env python3
# polynomial_q_not_applicable: torus-knot genus combinatorics + ζ₅ Gauss-sum
# grounding of the Bring 1/√5; not a Jones-polynomial evaluation.
"""
The trefoil + cinquefoil channel in Bring's genus-4 Seifert fibre Σ₄.

Ties together the geometry behind the H₂S Bring 1/√5 (the open content of
conj:h2s-angle-s3-braid-holonomy). The earlier ζ₅ grounding
(h2s_bring_zeta5_chiral_residue.py) showed √5 is the unique irrationality of
ζ₅; this script makes the *embedding* geometry explicit and provable:

  THE CONFLATION CORRECTED — two DISTINCT torus knots, not one fibre:
    • 3-fold = chiral channel.  The color-tube cubic (3 roots r,g,b) fibres
      Bring's surface; its branch monodromy is B₃ ↠ H₃.  This is the TREFOIL
      T_{2,3} (Seifert genus 1) — the c_λ=0 (2,1) chirality cell.
    • 5-fold = the √5.  S₅=Aut(B) contains a cyclic ℤ₅; the hyperelliptic
      quintic 𝒳₅:y²=x⁵−1 is EMBEDDED (not a cover) by x = the first Lagrange
      resolvent w₁ of that ℤ₅⊂S₅, its 5 branch points one ℤ₅-orbit
      {1,ζ₅,…,ζ₅⁴}.  This is the CINQUEFOIL T_{2,5} (Seifert genus 2).

  Both embed in Σ₄ (genus 1 and 2, ≤ 4 = g(Σ₄)); they are distinct; the
  ambient S₅ links them.  The complete embeddable list is
  {(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)} (Seifert genus (m−1)(n−1)/2 ≤ 4).

  WHERE √5 ENTERS:  the quadratic Gauss sum over the cinquefoil's ℤ₅-orbit,
  g = Σ_{k=0}^{4} ζ₅^{k²},  satisfies  g² = 5  (p=5 ≡ 1 mod 4 ⇒ g = +√5).
  This is the unique source of ζ₅'s irrationality over ℚ; the w₁ resolvent
  carries it.  So the H₂S chiral residue's only available irrational scale on
  this configuration is √5, and its Bring constant is 1/√5.

STATUS: the discrete scaffold (two distinct torus knots both embedding in Σ₄,
linked by S₅; the ℤ₅-orbit Gauss sum g²=5) is fully provable and is formalised
sorry-free in the Lean sibling except for the classical g²=5 (cited). The exact
ζ₅-residue monodromy returning *precisely* 1/√5 is the conjecture's open content.

Refs: prop:bring-trefoil-cinquefoil-channel; prop:torus-embeddable-complete;
prop:x5-z5-automorphism; def:hyperelliptic-quintic; rem:chirality-trefoil;
conj:h2s-angle-s3-braid-holonomy; washington1997 (quadratic Gauss sum).
"""
from __future__ import annotations

import sys
from math import gcd
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

SQRT5 = np.sqrt(5.0)
BRINGS_GENUS = 4


def torus_knot_genus(m: int, n: int) -> int:
    """Seifert genus of the torus knot T_{m,n}: g = (m-1)(n-1)/2."""
    return (m - 1) * (n - 1) // 2


def embeddable_pairs() -> list[tuple[int, int]]:
    """Complete list of coprime (m,n), 1<m<n, with Seifert genus ≤ 4."""
    out = []
    for m in range(2, 12):
        for n in range(m + 1, 30):
            if gcd(m, n) == 1 and torus_knot_genus(m, n) <= BRINGS_GENUS:
                out.append((m, n))
    return out


def main() -> None:
    w = WitnessBuilder("bring-trefoil-cinquefoil-channel", engine="python")

    print("=" * 72)
    print("The trefoil + cinquefoil channel in Bring's Σ₄  (H₂S 1/√5 geometry)")
    print("=" * 72)

    g_tref = torus_knot_genus(2, 3)        # chiral channel
    g_cinq = torus_knot_genus(2, 5)        # ζ₅ carrier
    pairs = embeddable_pairs()

    print(f"  chiral channel  = trefoil   T_(2,3) : Seifert genus {g_tref}")
    print(f"  ζ₅ carrier      = cinquefoil T_(2,5) : Seifert genus {g_cinq}")
    print(f"  Bring fibre Σ₄  : genus {BRINGS_GENUS}")
    print(f"  both embed (g ≤ {BRINGS_GENUS}): "
          f"{g_tref <= BRINGS_GENUS and g_cinq <= BRINGS_GENUS}")
    print(f"  distinct knots (g differ): {g_tref != g_cinq}")
    print(f"  complete embeddable list: {pairs}")
    print()

    # The 3-fold (color-tube cubic) vs 5-fold (ζ₅ quintic) counts
    color_tube_roots = 3          # cubic — (r,g,b)
    quintic_branch_points = 5     # ℤ₅-orbit {1,ζ₅,…,ζ₅⁴}

    # ζ₅ and the quadratic Gauss sum over its orbit
    z5 = np.exp(2j * np.pi / 5)
    gauss = sum(z5 ** (k * k) for k in range(5))          # Σ ζ₅^{k²}
    gauss_sq = gauss ** 2
    inv_sqrt5 = 1.0 / SQRT5

    print(f"  ζ₅ = exp(2πi/5) = {z5:.6f},  ζ₅⁵ = {z5**5:.3f}")
    print(f"  Gauss sum g = Σ_(k=0..4) ζ₅^(k²) = {gauss.real:.6f}"
          f"{gauss.imag:+.1e}i")
    print(f"            g  =? √5 = {SQRT5:.6f}   (Δ={abs(gauss.real-SQRT5):.2e})")
    print(f"            g² =? 5  : {gauss_sq.real:.6f}{gauss_sq.imag:+.1e}i")
    print(f"  Bring constant 1/√5 = {inv_sqrt5:.6f}")
    print()
    print("  ⇒ chiral channel (trefoil) and ζ₅ (cinquefoil) are two distinct")
    print("    torus knots in the SAME Σ₄, linked by Aut(B)=S₅; the quintic")
    print("    embeds via the w₁ resolvent of ℤ₅⊂S₅, which carries √5 (g²=5).")

    w.set_description(
        "Ties the H₂S Bring 1/√5 geometry together: the chiral channel is the "
        "trefoil T_(2,3) (Seifert genus 1, the color-tube cubic's B₃↠H₃ "
        "monodromy) and the ζ₅ carrier is the cinquefoil T_(2,5) (genus 2, the "
        "hyperelliptic quintic 𝒳₅:y²=x⁵−1 embedded via the first Lagrange "
        "resolvent w₁ of ℤ₅⊂S₅). Both embed in Bring's Σ₄ (genus ≤ 4), they are "
        "distinct, and the ambient Aut(B)=S₅ links them — two torus knots in one "
        "Σ₄, NOT one fibre with two symmetries (corrects the earlier conflation). "
        "The quadratic Gauss sum over the cinquefoil's ℤ₅-orbit, g=Σζ₅^(k²), "
        "satisfies g²=5 (p=5≡1 mod 4 ⇒ g=√5) — the unique source of ζ₅'s "
        "irrationality, carried by w₁; so the H₂S chiral residue's irrational "
        "scale is √5 and its Bring constant is 1/√5. Exact ζ₅-residue "
        "normalisation = 1/√5 remains the conjecture's open monodromy step."
    )
    w.set_content_block("prop:bring-trefoil-cinquefoil-channel")
    w.add_data("g_trefoil_chiral_channel", int(g_tref))
    w.add_data("g_cinquefoil_zeta5", int(g_cinq))
    w.add_data("brings_genus_sigma4", int(BRINGS_GENUS))
    w.add_data("embeddable_pairs", [list(p) for p in pairs])
    w.add_data("color_tube_cubic_roots", int(color_tube_roots))
    w.add_data("quintic_branch_points", int(quintic_branch_points))
    w.add_data("zeta5_re", float(z5.real))
    w.add_data("zeta5_im", float(z5.imag))
    w.add_data("gauss_sum", float(gauss.real))
    w.add_data("gauss_sum_sq", float(gauss_sq.real))
    w.add_data("sqrt5", float(SQRT5))
    w.add_data("inv_sqrt5_bring", float(inv_sqrt5))

    w.add_assertion(
        "chiral channel = trefoil T_(2,3) has Seifert genus 1",
        computed=int(g_tref), expected=1, source="g=(m-1)(n-1)/2",
    )
    w.add_assertion(
        "ζ₅ carrier = cinquefoil T_(2,5) has Seifert genus 2",
        computed=int(g_cinq), expected=2, source="g=(m-1)(n-1)/2",
    )
    w.add_assertion(
        "both embed in Σ₄ (genus ≤ 4)",
        computed=bool(g_tref <= BRINGS_GENUS and g_cinq <= BRINGS_GENUS),
        expected=True, source="Seifert genus ≤ g(Σ₄)=4",
    )
    w.add_assertion(
        "trefoil and cinquefoil are distinct (genera differ)",
        computed=bool(g_tref != g_cinq), expected=True,
        source="1 ≠ 2",
    )
    w.add_assertion(
        "complete embeddable list = {(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)}",
        computed=pairs,
        expected=[(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)],
        source="coprime 1<m<n, (m-1)(n-1)≤8",
    )
    w.add_assertion(
        "quadratic Gauss sum over ℤ₅-orbit squares to 5 (g²=5)",
        computed=bool(abs(gauss_sq.real - 5.0) < 1e-9
                      and abs(gauss_sq.imag) < 1e-9),
        expected=True, source="g=Σζ₅^(k²), p=5≡1 mod 4 ⇒ g²=5",
    )
    w.add_assertion(
        "Gauss sum g = +√5 (archimedean projection)",
        computed=bool(abs(gauss.real - SQRT5) < 1e-9),
        expected=True, source="g=√5 for p=5≡1 mod 4",
    )
    w.add_data(
        "finding",
        "The H₂S Bring 1/√5 geometry: the chiral channel is the trefoil T_(2,3) "
        "(genus 1) and the ζ₅ carrier is the cinquefoil T_(2,5) (genus 2); both "
        "embed in Bring's Σ₄ (genus ≤ 4), they are distinct, and Aut(B)=S₅ links "
        "them — two torus knots in one Σ₄. The quintic embeds via the w₁ Lagrange "
        "resolvent of ℤ₅⊂S₅; the ℤ₅-orbit Gauss sum satisfies g²=5 (g=√5), the "
        "unique irrationality of ζ₅. So the chiral residue's irrational scale is "
        "√5 and the Bring constant is 1/√5. The exact ζ₅-residue normalisation "
        "(=1/√5) is the conjecture's open monodromy computation.",
    )
    w.save()
    print("\nDone. Witness saved (bring-trefoil-cinquefoil-channel).")


if __name__ == "__main__":
    main()
