# gg_two_orientations — results (bean qou-a1hh, hypothesis only; nothing wired)

Words in {V, B} with V = σ₀σ₁⁻¹, B = V̄ = σ₀⁻¹σ₁, on 3 strands, lengths m = 1..6
(126 words). Reading 3 alone at levels 1-3, proton pin, mpmath 70 dps.

## Check T0 (pre-registered): PASS
Pure powers V^m and B^m pass iff 3 | m, matching gg_symmetry.

## Main result
| m | words | pass alone |
|---|---|---|
| 1 | 2 | 0 |
| 2 | 4 | 0 |
| 3 | 8 | **8** |
| 4 | 16 | 0 |
| 5 | 32 | 0 |
| 6 | 64 | **64** |

Pass-alone depends only on the number of vertices (3 | m), not on orientation.
So with both orientations allowed there are 8 three-vertex nucleon candidates, not 1.

Three-vertex words (level-3 χ_(2,1); one-photon level-2 sign dR):

| word | χ_(2,1) | dR |
|---|---|---|
| VVV | 1.99418581297996 | +0.00351714385882 |
| VVB | 2.13302885826185 | +0.00741626948117 |
| VBV | 2.13302885826185 | −0.0804724083125 |
| VBB | 2.13302885826185 | −0.0804724083125 |
| BVV | 2.13302885826185 | +0.0991462281542 |
| BVB | 2.13302885826185 | +0.0991462281542 |
| BBV | 2.13302885826185 | +0.0112575503605 |
| BBB | 1.99418581297996 | −0.00433330572292 |

Level 3 (conjugation-invariant) sees two classes only: pure (VVV, BBB) and mixed
(the other six). Level 2 splits further; several pairs coincide (VBV=VBB, BVV=BVB).

Outcome (i) as pre-registered: mixed words pass alone. The one-orientation vertex in
`QOU/Mass/GammaGammaWordSelection.lean` is what made every γγ nucleon a power of V.
Whether the γγ definition should admit V̄ is an owner decision (definition change).
Any reading of V/B as u/d flavour is a hypothesis, scope (a).
