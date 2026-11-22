import QOU.BraidsAndKnots.BondChiralitySixStrand.CaseGLeft
import QOU.BraidsAndKnots.BondChiralitySixStrand.CaseGRight
import QOU.BraidsAndKnots.BondChiralitySixStrand.CaseGpLeft
import QOU.BraidsAndKnots.BondChiralitySixStrand.CaseGpRight

/-!
# Bond chirality on six strands: the weight-space reduction and the four values

Level-2 Jimbo braiding on `(C²)^{⊗6}`, `h = q - q⁻¹`:
`Ř e₀₀ = q e₀₀`, `Ř e₀₁ = e₁₀`, `Ř e₁₀ = e₀₁ + h e₁₀`, `Ř e₁₁ = q e₁₁`; `σ⁻¹ = σ − h`.
A basis state is `s : Fin 64`; bit `j` of `s` is the spin on strand `j` (`false` = zero).
`gen64 q i` is `Ř` on strands `i, i + 1`; a word is the matrix product in list order.

**The functional (B1 of the six-strand arm of `mn_hydrogen_capture_chirality_probe`, draft PR
#8804 §43).** `F(O) = Σ_s T³(s) · W s s` over the states whose three proton strands carry two
zeros (`O₊`) or one zero (`O₋`), with `T³ = (#0 − #1)/2 = #0 − 3` over all six strands.
`S = F(O₊) + F(O₋)`. These are `Fp64`, `Fm64` below, defined on the full 64-dimensional space.

**Reduction.** `Ř` preserves `#0`, and `#0 = 3` has `T³ = 0`, so only the weight spaces
`#0 ∈ {1, 2, 4, 5}` (dimensions 6, 15, 15, 6) enter. `mul_Emb_eq` proves `M · E = E · M|_W` for
any `M` that maps the weight space `W` to itself; closure under each generator and injectivity
of the inclusion are checked by `decide`. So for every word, `F(O₊)` and `F(O₋)` on the full space
equal explicit sums of 15 weight-space diagonal entries each (`Fp_L_reduction`, `Fm_L_reduction`,
and the `R` versions for the proton on strands `3–5`).

**Values (generic field, `q ≠ 0`).** The four words of §43:
* `G` proton left, `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂σ₃⁻¹)³`: `S = −4q·h⁴`.
* `G` proton right, `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂σ₃⁻¹)³`: `S = (3q² + 1)h⁴/q`.
* `G′` (non-ruled comparison arm) proton left, `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂⁻¹σ₃)³`: `S = (q² + 1)(3q⁴ − 2q² + 1)h⁴/q`.
* `G′` (non-ruled comparison arm) proton right, `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂⁻¹σ₃)³`: `S = −(3q² + 1)q³h⁴`.
At `q = 1`, all four have `F(O₊) = 6` and `F(O₋) = −6`. (The `±3` of §43 belongs to the
four-strand capture words, `HydrogenCaptureWeightSpace`, not to these.)

**Ruled form and comparison arm.** Owner ruling 2026-11-22 (reading A plus right-hand closure,
`docs/coordination/owner-rulings.md`): the photon vertex at strands `(i, i+1)` is `σ_iσ_{i+1}⁻¹`,
the larger letter inverted, so the bond `G = (σ₂σ₃⁻¹)³` is the ruled form. `G′ = (σ₂⁻¹σ₃)³` is
proved only as the non-ruled comparison arm; it is not an alternative convention.

**What the theorems assume about closure.** None. `F(O±)` is a weighted sum of diagonal entries
of the open six-strand braid matrix, so no closure (left or right) enters any statement here.
The placement of the proton (strands `0–2` or `3–5`) enters only through the projector `O±` and
the word as written; in every word the bond is the rightmost factor, i.e. it acts first. Whether
the right-hand-closure rule ("a bond enters the newer nucleon") selects one of the two placements
is not decided in this file. `(σ₀σ₁⁻¹)³` is the γγ product of the photon
`1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`. No numerical value enters.
-/

namespace QOU.BraidsAndKnots.BondChiralitySixStrand

variable {R : Type*} [Field R]

/-- **The four values of §43, on the full space.** `S = F(O₊) + F(O₋)` for the bond `G`
(ruled form) and the bond `G′` (non-ruled comparison arm), proton on strands `0–2` and `3–5`. -/
theorem four_values (q : R) (hq : q ≠ 0) :
    Fp64 [0, 1, 2] (word64 q wGL) + Fm64 [0, 1, 2] (word64 q wGL) = -(4 * q * (q - q⁻¹) ^ 4) ∧
    Fp64 [3, 4, 5] (word64 q wGR) + Fm64 [3, 4, 5] (word64 q wGR)
      = (3 * q ^ 2 + 1) * (q - q⁻¹) ^ 4 / q ∧
    Fp64 [0, 1, 2] (word64 q wGpL) + Fm64 [0, 1, 2] (word64 q wGpL)
      = (q ^ 2 + 1) * (3 * q ^ 4 - 2 * q ^ 2 + 1) * (q - q⁻¹) ^ 4 / q ∧
    Fp64 [3, 4, 5] (word64 q wGpR) + Fm64 [3, 4, 5] (word64 q wGpR)
      = -((3 * q ^ 2 + 1) * q ^ 3 * (q - q⁻¹) ^ 4) :=
  ⟨S_GL q hq, S_GR q hq, S_GpL q hq, S_GpR q hq⟩

/-- **`q = 1`:** in all four configurations `F(O₊) = 6` and `F(O₋) = −6`. -/
theorem at_one :
    (Fp64 [0, 1, 2] (word64 (1 : R) wGL) = 6 ∧ Fm64 [0, 1, 2] (word64 (1 : R) wGL) = -6) ∧
    (Fp64 [3, 4, 5] (word64 (1 : R) wGR) = 6 ∧ Fm64 [3, 4, 5] (word64 (1 : R) wGR) = -6) ∧
    (Fp64 [0, 1, 2] (word64 (1 : R) wGpL) = 6 ∧ Fm64 [0, 1, 2] (word64 (1 : R) wGpL) = -6) ∧
    (Fp64 [3, 4, 5] (word64 (1 : R) wGpR) = 6 ∧ Fm64 [3, 4, 5] (word64 (1 : R) wGpR) = -6) :=
  ⟨⟨Fp_GL_at_one, Fm_GL_at_one⟩, ⟨Fp_GR_at_one, Fm_GR_at_one⟩,
    ⟨Fp_GpL_at_one, Fm_GpL_at_one⟩, ⟨Fp_GpR_at_one, Fm_GpR_at_one⟩⟩

end QOU.BraidsAndKnots.BondChiralitySixStrand
