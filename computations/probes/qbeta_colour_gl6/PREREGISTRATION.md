# Pre-registration: colour mixing with isospin inside one R-matrix (gl₆) (issue #8833, front 3)

Written and committed before the Lean file and probe are run. Follows
`qbeta_colour_factor` (commit dc9a8d6376), which proved that colour as a separate tensor
factor multiplies the ruled cell by F ≤ 1. Not excluded there: colour that mixes with isospin
inside one R-matrix. This probe tests that.

## Construction (no free parameter)

Each quark strand is C⁶ = C²(isospin) ⊗ C³(colour). The braid acts by the U_q(gl₆) Jimbo
R-matrix: R(e_i⊗e_i) = q e_i⊗e_i; for i < j, R(e_i⊗e_j) = e_j⊗e_i and
R(e_j⊗e_i) = e_i⊗e_j + h e_j⊗e_i (Hecke, eigenvalues q, −1/q). The nucleon word is the ruled
V³ = (σ₀σ₁⁻¹)³; V⁶ and V⁹ are reported too. The nucleon sectors are the ruled isospin sectors
(proton: one isospin-down quark; neutron: two). R preserves the multiset of basis labels, so
both the isospin and the colour weight are conserved and every sector below is invariant.

## The closed family (every member reported, none selected)

The gl₆ R depends on a total order of the six labels, which is not fixed by any ruling. So:

* **order:** isospin-major (label = 3t + c) or colour-major (label = 2c + t);
* **trace element:** the gl₆ quantum-trace element K₆ = diag(q⁵, q³, q, q⁻¹, q⁻³, q⁻⁵) in the
  chosen order (Tr K₆ = [6]), normalised by [6]³; or the isospin element K₂ ⊗ 1₃, normalised
  by (3[2])³. Both make an idle strand contribute 1 (premise N2 of the lepton normalisation);
* **colour treatment:** colour summed, or restricted to the colour-neutral weight (one quark
  of each colour).

2 × 2 × 2 = 8 members, each on V³, V⁶, V⁹. For each:
ε_p, ε_n, ε_flavour = ε_n − ε_p, and F = ε_flavour / ε_flavour^ruled. Compared with
F_required = 2.40397. The verdict uses V³.

## Lean first

`QOU/QBeta/GlNJimboHecke.lean`: over a generic field, each block of the gl_N Jimbo R (the
diagonal entry q, and the 2×2 block on {e_i⊗e_j, e_j⊗e_i}) satisfies the Hecke relation
X² = hX + 1, and the block's inverse is X − h.

## What this does NOT do

No member is selected by closeness to F_required. Nothing is mapped to MeV.

## Addendum (2026-11-21, after the first run): deriving the order and trace element

Owner direction via the coordinator: derive, do not choose. Written before the derivation
checks are run. The premises are those of the lepton normalisation (N1 agreement with D1,
N3 closure invariance), applied to the gl₆ braiding:

* **N3 fixes the trace element.** The Markov move needs the partial quantum trace of R over
  the last strand to be a scalar. Test, exactly, for K₆ (in the R's own order) and for
  K₂ ⊗ 1, in both orders. A trace element that fails is excluded.
* **N1 fixes the order.** D1 weighs the proton and neutron sectors by the isospin charge
  q^{±1}. For the lexicographic orders on C² ⊗ C³, K₆ restricted to isospin is q^{3(1−2t)}
  (isospin-major) or q^{(1−2t)} (colour-major) (Lean). Only the order that reproduces
  q^{±1} agrees with D1.

The verdict is whatever F the surviving member has, including F = 1. Reported either way.
