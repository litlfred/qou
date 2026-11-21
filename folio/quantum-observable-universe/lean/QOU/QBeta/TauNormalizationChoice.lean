import QOU.QBeta.ObservableComplexVolumeVsFullPotential

set_option autoImplicit false

/-!
# QOU.QBeta.TauNormalizationChoice — the A=1-vs-A=2 binary, machine-tracked

The `qou-pzzl` convention split, stated as mathematics instead of prose: the
bar-odd observable `S` is normalized two ways in the corpus —

* **full-potential** (`ArgUPhaseBranchSelection` / `NZBarEvenVolumeFace`):
  `S = Im Φ(u) = κ_shape·(Re²u − Im²u)`, `κ_shape = √3/2`;
* **complex-volume, integer-dressed** (`SDeformedVolumeChannel`):
  `S = A_ω · Im 𝔙(u) = A_ω·κ_pot·(Re²u − Im²u)`, `κ_pot = √3/4`.

Since `Φ = 2𝔙` exactly (`kappaFull_eq_two_mul_kappaCV`, sorry-free), the
full-potential convention IS the complex-volume convention with the integer
forced to `2` (`usesFullPotential_iff_A_two` below), so the split is a single
integer variable with candidate values `{2, A_ω}`. The exclusivity theorem
makes the pzzl statement "one is wrong" precise: two integer dressings of the
same nonvanishing channel force equal integers — so `A = 2` and `A = 3`
cannot both hold anywhere `Im 𝔙(u q) ≠ 0`.

## Honesty (§3b; anti-laundering)

Nothing here decides the binary. Which normalization the fibre→observable
(τ/archimedean) functor applies is the OPEN content of bean `qou-yh67`
(blocked on the `A_ω` internal derivation); no instance of either predicate
is fabricated, and no numerical `S` is wired. This file only replaces the
prose-tracked convention split with definitions the corpus can state
conditional theorems against.

## References

- [neumann-zagier1985] Neumann & Zagier, "Volumes of hyperbolic
  three-manifolds," Topology 24 (1985). https://doi.org/10.1016/0040-9383(85)90004-7
- [leitner2026] docs/audits/2026-08-02-pzzl-kappa-shape-vs-pot-S-normalization.md
-/

namespace QOU.QBeta.TauNormalizationChoice

open QOU.QBeta.ObservableComplexVolumeVsFullPotential

/-- The channel `S` carries the complex-volume normalization dressed by the
real factor `A`: `S q = A · Im 𝔙(u q)` at every substrate value. The open
question (qou-yh67) is WHICH `A` the τ-functor applies. -/
def UsesComplexVolumeNorm (A : ℝ) (S : ℝ → ℝ) (u : ℝ → ℂ) : Prop :=
  ∀ q, S q = A * imComplexVolume (u q)

/-- The channel `S` carries the full-potential normalization
`S q = Im Φ(u q)` (no dressing factor). -/
def UsesFullPotentialNorm (S : ℝ → ℝ) (u : ℝ → ℂ) : Prop :=
  ∀ q, S q = imFullPotential (u q)

/-- The full-potential convention IS the complex-volume convention with the
integer forced to `2` — the `qou-pzzl` "two conventions" are one integer
variable. Direct from `Φ = 2𝔙`. -/
theorem usesFullPotential_iff_A_two (S : ℝ → ℝ) (u : ℝ → ℂ) :
    UsesFullPotentialNorm S u ↔ UsesComplexVolumeNorm 2 S u := by
  unfold UsesFullPotentialNorm UsesComplexVolumeNorm
  constructor <;> intro h q <;>
    simpa [imFullPotential_eq_two_mul_imComplexVolume] using h q

/-- **Exclusivity.** Two dressings of the same channel with the same
deformation agree everywhere, so at any point where the channel's geometric
part does not vanish the dressing factors are equal. This is the precise
form of "one of the two conventions is wrong": `A = 2` (full potential) and
`A = 3` (the `A_ω` target) cannot both hold at a nonvanishing point. -/
theorem dressing_factor_unique {A A' : ℝ} {S : ℝ → ℝ} {u : ℝ → ℂ}
    (h : UsesComplexVolumeNorm A S u) (h' : UsesComplexVolumeNorm A' S u)
    {q : ℝ} (hq : imComplexVolume (u q) ≠ 0) : A = A' := by
  have := (h q).symm.trans (h' q)
  exact mul_right_cancel₀ hq this

/-- Application: the two live corpus conventions (`Φ`, i.e. `A = 2`, and the
`A_ω = 3` target) are incompatible on any channel with a nonvanishing point —
the reconciliation (`qou-pzzl`) must retire one, and which one is exactly the
open `qou-yh67` binary. -/
theorem full_potential_and_Aomega_three_incompatible {S : ℝ → ℝ} {u : ℝ → ℂ}
    (h2 : UsesFullPotentialNorm S u) (h3 : UsesComplexVolumeNorm 3 S u)
    {q : ℝ} (hq : imComplexVolume (u q) ≠ 0) : False := by
  have h2' : UsesComplexVolumeNorm 2 S u :=
    (usesFullPotential_iff_A_two S u).mp h2
  have : (2 : ℝ) = 3 := dressing_factor_unique h2' h3 hq
  norm_num at this

end QOU.QBeta.TauNormalizationChoice
