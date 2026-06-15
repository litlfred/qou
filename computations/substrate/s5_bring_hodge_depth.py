"""S₅-Hodge depth of the Bring prolongation operator `M` (keystone).

The keystone needs the depth `d` of the recurrence on the prolonged
periods `a_D⁽ⁿ⁾` (R = charpoly(M), an `d×d` operator). The naive bound is
`d ≤ 2g = 8`. This module fixes `d` a priori via representation theory.

Input (cited, Riera–Rodríguez 1992, *The period matrix of Bring's curve*):
the space of holomorphic differentials `H⁰(Ω)` of Bring's genus-4 curve is
an **irreducible 4-dimensional `S₅` representation** `W` (the standard rep
`(4,1)` or its sign-twist `(2,1,1,1)`; both give the same conclusion).

Consequence computed here:
  H¹ = H^{1,0} ⊕ H^{0,1} = W ⊕ conj(W) = 2·W   (W is real ⇒ conj W ≅ W),
so `W` occurs in `H¹` with **multiplicity 2**. Since the Gauss–Manin
operator `M` is `S₅`-equivariant, by Schur it acts as `id_W ⊗ B` with `B`
a 2×2 matrix on the multiplicity (Hodge) space. Hence the recurrence
**depth is `≤ 2`**, and Griffiths transversality (`∇F^p ⊂ F^{p-1}⊗Ω`)
couples the two Hodge lines, making `B` non-scalar ⇒ **depth exactly 2**.
So `R = charpoly(B)` is degree 2: two numbers.

Character data reused from the sibling probe
`probes/gap_a4_T4_schur_weyl_icosahedral_probe.py` (S₅/A₅ tables;
hand-built, standard).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
for _p in (str(_HERE.parent), str(_HERE)):  # computations/, substrate/
    if _p not in _sys.path:                  # idempotent: don't shadow on re-import
        _sys.path.insert(0, _p)
import _path_bridge as _bridge  # noqa: E402, F401

from fractions import Fraction  # noqa: E402

# S₅: 7 conjugacy classes  e, (12), (12)(34), (123), (123)(45), (1234), (12345).
S5_CLASS_SIZES = [1, 10, 15, 20, 20, 30, 24]   # |S₅| = 120
S5_ORDER = 120
# Sign character on the 7 classes (parity of each class representative).
S5_SGN = [1, -1, 1, 1, -1, -1, 1]
# Standard rep W = (4,1): χ(g) = (#fixed points) − 1.
CHI_W_41 = [4, 2, 0, 1, -1, 0, -1]
# Sign-twist W' = (2,1,1,1) = (4,1)⊗sgn.
CHI_W_2111 = [s * c for s, c in zip(S5_SGN, CHI_W_41)]


def inner(chi_a, chi_b) -> Fraction:
    """⟨χ_a, χ_b⟩_{S₅} = (1/|G|) Σ_classes |C|·χ_a(C)·χ_b(C) (real chars)."""
    tot = sum(sz * a * b for sz, a, b in zip(S5_CLASS_SIZES, chi_a, chi_b))
    return Fraction(tot, S5_ORDER)


def multiplicity_in_H1(chi_W) -> int:
    """Multiplicity of `W` in H¹ = 2·W. This is the recurrence-depth
    **upper bound** (depth ≤ multiplicity, by Schur). 'Depth exactly 2'
    additionally requires the Griffiths-transversality argument, which is
    NOT computed here — it is a theoretical input stated in the module
    docstring and workplan."""
    chi_H1 = [2 * x for x in chi_W]      # H¹ = W ⊕ conj W = 2W
    m = inner(chi_H1, chi_W)
    # A genuine multiplicity is a non-negative integer; a non-trivial
    # denominator would mean the character data is wrong/mismatched.
    assert m.denominator == 1, f"non-integer multiplicity {m} (bad character data)"
    return m.numerator


def _emit_witness() -> None:
    from witness_base import WitnessBuilder

    irred_41 = inner(CHI_W_41, CHI_W_41)        # = 1 (irreducible)
    irred_2111 = inner(CHI_W_2111, CHI_W_2111)  # = 1
    distinct = inner(CHI_W_41, CHI_W_2111)      # = 0 (distinct irreps)
    m_41 = multiplicity_in_H1(CHI_W_41)
    m_2111 = multiplicity_in_H1(CHI_W_2111)

    w = WitnessBuilder("s5-bring-hodge-depth", engine="python-fractions")
    w.set_audit_only(
        "docs/workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md"
    )
    w.add_data("W_41_irreducible_norm", str(irred_41))
    w.add_data("W_2111_irreducible_norm", str(irred_2111))
    w.add_data("W_41_vs_W_2111_inner", str(distinct))
    w.add_data("multiplicity_in_H1_via_41", m_41)
    w.add_data("multiplicity_in_H1_via_2111", m_2111)
    # Keep the witness strictly aligned with what is COMPUTED here.
    w.add_data("computed_conclusion",
               "H¹ = 2·W (multiplicity 2); M = id_W ⊗ B with B a 2×2 matrix "
               "(Schur) ⇒ recurrence depth ≤ 2")
    w.add_data("additional_argument_not_checked",
               "depth = 2 (not just ≤ 2) requires Griffiths transversality "
               "(∇F^p ⊂ F^{p−1}⊗Ω) ⇒ B non-scalar; this geometric input is "
               "stated in the workplan, NOT verified by this script")
    w.add_data("character_source",
               "probes/gap_a4_T4_schur_weyl_icosahedral_probe.py (S₅/A₅ tables)")

    w.add_assertion("W_41_irreducible", computed=int(irred_41 == 1), expected=1,
                    source="⟨χ_(4,1), χ_(4,1)⟩ = 1")
    w.add_assertion("W_2111_irreducible", computed=int(irred_2111 == 1),
                    expected=1, source="⟨χ_(2,1,1,1), χ_(2,1,1,1)⟩ = 1")
    w.add_assertion("multiplicity_in_H1_is_2",
                    computed=int(m_41 == 2 and m_2111 == 2), expected=1,
                    source="multiplicity of W in H¹ = 2W is 2 ⇒ depth ≤ 2")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    print("S₅-Hodge depth of the Bring prolongation operator")
    print(f"  ⟨W(4,1), W(4,1)⟩       = {inner(CHI_W_41, CHI_W_41)}  (1 ⇒ irreducible)")
    print(f"  ⟨W(2,1,1,1), …⟩        = {inner(CHI_W_2111, CHI_W_2111)}  (1 ⇒ irreducible)")
    print(f"  ⟨W(4,1), W(2,1,1,1)⟩   = {inner(CHI_W_41, CHI_W_2111)}  (0 ⇒ distinct)")
    print(f"  mult of W in H¹=2W : {multiplicity_in_H1(CHI_W_41)}  "
          f"(via 4,1)  /  {multiplicity_in_H1(CHI_W_2111)}  (via 2,1,1,1)  "
          f"⇒ depth ≤ 2 (computed)")
    print("  ⇒ M = id_W ⊗ B (2×2). depth = 2 needs Griffiths transversality "
          "(theoretical input, not checked here)")
    _emit_witness()
