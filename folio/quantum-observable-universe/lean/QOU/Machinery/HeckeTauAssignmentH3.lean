/-
# Inhabiting the τ-assignment at the H3 rung — coker(N) ≅ the CW(3,1) isotypic model

The second half of the `TauRhoHodgeLift` module-side wall: the typed
obligation `TauAssignmentData` (merged #4092) is INHABITED here at the
concrete H3 rung (`descentH3σ₀ : DescentStructure (Fin 6)`), with the
provenance pinned by three non-degeneracy theorems rather than by fiat:

* **`tauAssignmentH3`** — the assignment `v ↦ (v₀ + i v₁, v₂ + i v₃,
  v₄ + i v₅, 0)` into the genus-4 `H^{1,0}` model `Fin 4 → ℂ`, with its
  ρ-partner `w ↦ (w₀ − i w₁, …, 0)` into `H^{0,1}`. The three
  functionals are exactly the duals of `coker N`: the nilpotent
  `N = σ − i` acts pairwise on the three descent pairs `(0,1), (2,3),
  (4,5)` of the H3 cell, its image on each pair is the line
  `(x, ix)`, and `v ↦ v(2p) + i·v(2p+1)` is the functional that kills
  that line — the T2 Burau-at-`i` Jordan pair, seen dually.
* **`tauAssignmentH3_toFun_apply_three`** — the fourth coordinate is
  identically `0`: the assignment populates ONLY a 3-dimensional
  subspace of the target. This matches T1 (Chevalley–Weil for the
  degree-4 cyclic cover Bring → E): the deck-multiplier-`i` isotypic
  part of `H^{1,0}` is 3-dimensional and the complementary character is
  1-dimensional; a local-monodromy datum populates the matching
  isotypic part and cannot see the complement.
* **`tauAssignmentH3_surjective`** — every vector of the 3-dimensional
  isotypic model is hit: the assignment is onto, not a partial or zero
  map.
* **`tauAssignmentH3_ker_le_range_monodromyN`** — the kernel is EXACTLY
  the image of the nilpotent (the ⊇ direction is the structure field
  `kills_nilpotent`): the assignment descends to a linear ISOMORPHISM
  `coker N ≅ (3-dim isotypic model)` — dimension 3 = the CW multiplicity.
  This is the promised "factors through the semisimple quotient"
  provenance, realized exactly, not merely satisfied.

The ρ-intertwining field `rho_compat` is the assignment-level image of
the T3 deck/reality exchange (`DeckRealityEquivariance`): conjugation
carries the assignment onto its `H^{0,1}` partner, matching
`monodromyN_star` (ρ exchanges the two Jordan structures).

HONESTY (STRICT): this inhabits the typed obligation at the CONCRETE
rank-3 rung with exact coker-provenance; the general-rank statement — a
naturality square tying the assignments across the Hecke tower
inclusions (ι₃₄ and beyond) to a single functor — is NOT proved here
and remains the open functorial content of `TauRhoHodgeLift`. The
inhabitation is non-degenerate by the three theorems above (a `toFun = 0`
inhabitation would satisfy the bare interface — cf.
`interface_alone_is_trivially_inhabitable` in `TauFunctorTargetSpec` —
and is exactly what the surjectivity + kernel-exactness theorems
exclude). Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/
import QOU.Machinery.HeckeMonodromyWeightFiltration
import Mathlib.Tactic.LinearCombination

namespace QOU.Machinery.HeckeGeneral

open Complex

/-- **The H3-rung τ-assignment**: the three coker(N)-dual functionals
`v ↦ v(2p) + i·v(2p+1)` on the descent pairs of the H3 cell, into the
3-dimensional deck-multiplier-`i` isotypic slot of the genus-4
`H^{1,0}` model, with the conjugate partner into `H^{0,1}`. -/
noncomputable def tauAssignmentH3 : TauAssignmentData descentH3σ₀ where
  toFun v := ![v 0 + I * v 1, v 2 + I * v 3, v 4 + I * v 5, 0]
  toFunBar w := ![w 0 - I * w 1, w 2 - I * w 3, w 4 - I * w 5, 0]
  map_add v v' := by
    funext u
    fin_cases u <;> simp [Pi.add_apply] <;> try ring
  kills_nilpotent v := by
    funext u
    fin_cases u <;>
      simp [monodromyN, mulStep, descentH3σ₀, Pi.sub_apply, Pi.smul_apply,
        smul_eq_mul] <;>
      first
      | linear_combination (v 1) * I_mul_I
      | linear_combination (v 3) * I_mul_I
      | linear_combination (v 5) * I_mul_I
  rho_compat v u := by
    fin_cases u <;>
      simp [Complex.star_def, Complex.conj_I] <;>
      try ring

/-- The fourth coordinate of the assignment is identically zero: the
local-monodromy datum populates only the 3-dimensional isotypic slot,
matching the Chevalley–Weil (3,1) split of the cover's `H^{1,0}`. -/
theorem tauAssignmentH3_toFun_apply_three (v : Fin 6 → ℂ) :
    tauAssignmentH3.toFun v 3 = 0 := rfl

/-- **Surjectivity onto the isotypic model**: every vector supported on
the 3-dimensional CW slot is hit — the inhabitation is not the trivial
one. -/
theorem tauAssignmentH3_surjective (c : Fin 3 → ℂ) :
    ∃ v : Fin 6 → ℂ, tauAssignmentH3.toFun v = ![c 0, c 1, c 2, 0] := by
  refine ⟨![c 0, 0, c 1, 0, c 2, 0], ?_⟩
  funext u
  fin_cases u <;> simp [tauAssignmentH3]

/-- **Kernel exactness**: a state killed by the assignment lies in the
image of the nilpotent. With the structure field `kills_nilpotent`
(the reverse inclusion), the assignment descends to an isomorphism
`coker N ≅ ℂ³` — the exact CW-multiplicity match, the promised
semisimple-quotient provenance. -/
theorem tauAssignmentH3_ker_le_range_monodromyN (v : Fin 6 → ℂ)
    (h : tauAssignmentH3.toFun v = 0) :
    ∃ w, monodromyN descentH3σ₀ w = v := by
  have h0 : v 0 + I * v 1 = 0 := by
    have := congrFun h 0
    simpa [tauAssignmentH3] using this
  have h1 : v 2 + I * v 3 = 0 := by
    have := congrFun h 1
    simpa [tauAssignmentH3] using this
  have h2 : v 4 + I * v 5 = 0 := by
    have := congrFun h 2
    simpa [tauAssignmentH3] using this
  refine ⟨![0, v 0, 0, v 2, 0, v 4], ?_⟩
  funext u
  fin_cases u <;>
    simp [monodromyN, mulStep, descentH3σ₀, Pi.sub_apply, Pi.smul_apply,
      smul_eq_mul] <;>
    first
    | linear_combination I * h0 - v 1 * I_mul_I
    | linear_combination I * h1 - v 3 * I_mul_I
    | linear_combination I * h2 - v 5 * I_mul_I

end QOU.Machinery.HeckeGeneral
