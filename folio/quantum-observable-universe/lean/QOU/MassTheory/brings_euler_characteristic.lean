import Mathlib.Algebra.BigOperators.Fin
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.ArchimedeanUniverse.brings_euler_characteristic

Content block
[`lem:brings-euler-characteristic`](../../../quantum-observable-universe/brings-surface/brings-euler-characteristic.md):
*Bring's surface `Σ₄` has topological Euler characteristic
`χ_eu(Σ₄) = 2 − 2g(Σ₄) = 2 − 8 = −6`.  Equivalently, in the Hodge
decomposition of its Hochschild homology (HKR) one has `dim HH₀(Σ₄) = 2`
and `dim HH_{±1}(Σ₄) = 4`, and `−6` is the alternating sum
`∑_n (−1)^n dim HH_n(Σ₄)`.*

## Mathematical formalisation

1. **Complete-intersection adjunction derivation of `g(Σ₄) = 4` and `χ_eu(Σ₄) = −6`**:
   For a smooth complete-intersection curve `C = H₁ ∩ ⋯ ∩ H_{N−1} ⊂ ℙ^N` cut
   out by hypersurfaces of degrees `[d₁, …, d_{N−1}]`, Bézout's theorem gives
   `deg(C) = ∏ dᵢ` and the adjunction formula gives canonical twist
   `k_C = (∑ dᵢ) − (N + 1)`, canonical degree `deg K_C = k_C · deg(C)`,
   `2g(C) − 2 = deg K_C`, and `χ_eu(C) = deg T_C = −deg K_C = 2 − 2g(C)`.
   Instantiating `bringsCompleteIntersection` with `N = 4` (`ℙ⁴`) and power-sum
   multidegree `[1, 2, 3]` **derives** `deg(Σ₄) = 6`, `k_{Σ₄} = 1`,
   `deg K_{Σ₄} = 6`, `g(Σ₄) = 4`, and `χ_eu(Σ₄) = −6`.

2. **HKR Hodge decomposition and explicit vector-space `finrank`s**:
   From the genus-`g` curve Hodge diamond `(h^{0,0}, h^{1,0}, h^{0,1}, h^{1,1}) = (1, g, g, 1)`,
   the HKR decomposition `HH_n(Σ_g) ≅ ⨁_i H^i(Σ_g, Ω^{i+n})` (`n ∈ {−1, 0, 1}`
   indexed by `k : Fin 3` via `n = k − 1`) matches the explicit `K`-vector
   spaces `CurveHochschildSpace K g = (K^g, K^2, K^g)`, whose `Module.finrank K`
   alternating sum `∑_{n=−1}^1 (−1)^n dim_K HH_n(Σ_g)` equals `2 − 2g` for every
   `g : ℕ`, specialising to `(4, 2, 4)` and `−6` on Bring's surface.

3. **Backward-compatible context interface**:
   `BringsEulerCharacteristicContext` and its helper lemmas are preserved at
   the bottom of the module, equipped with `ofAdjunction` constructing the
   context directly from `bringsCompleteIntersection`.
-/

namespace QOU.ArchimedeanUniverse

/-- Data of a smooth 1-dimensional complete-intersection curve
    `C = H₁ ∩ ⋯ ∩ H_{N−1} ⊂ ℙ^N` of multidegree `degrees`. -/
structure SmoothCompleteIntersectionCurve where
  /-- Ambient projective dimension `N` of `ℙ^N`. -/
  ambientDim : ℕ
  /-- Degrees `[d₁, …, d_{N−1}]` of the defining homogeneous equations. -/
  degrees : List ℕ
  /-- Codimension `N − 1` cuts out a curve in `ℙ^N`. -/
  codim_eq : degrees.length + 1 = ambientDim
  /-- Every hypersurface degree is positive. -/
  pos_degrees : ∀ d ∈ degrees, 0 < d

namespace SmoothCompleteIntersectionCurve

/-- Bézout degree `deg(C) = ∏ᵢ dᵢ`. -/
def intersectionDegree (C : SmoothCompleteIntersectionCurve) : ℕ :=
  C.degrees.prod

/-- Adjunction canonical twist `k_C = (∑ᵢ dᵢ) − (N + 1)` in `K_C ≅ 𝒪_C(k_C)`. -/
def canonicalTwist (C : SmoothCompleteIntersectionCurve) : ℤ :=
  (C.degrees.sum : ℤ) - ((C.ambientDim : ℤ) + 1)

/-- Canonical bundle degree `deg K_C = k_C · deg(C)`. -/
def canonicalDegree (C : SmoothCompleteIntersectionCurve) : ℤ :=
  C.canonicalTwist * (C.intersectionDegree : ℤ)

/-- Tangent bundle degree `deg T_C = ∫_C c₁(T_C) = −deg K_C`. -/
def tangentDegree (C : SmoothCompleteIntersectionCurve) : ℤ :=
  -C.canonicalDegree

/-- Topological Euler characteristic `χ_eu(C) = −deg K_C`. -/
def topologicalEulerChar (C : SmoothCompleteIntersectionCurve) : ℤ :=
  -C.canonicalDegree

/-- Genus `g(C)` recovered from `2g(C) − 2 = deg K_C`. -/
def arithmeticGenus (C : SmoothCompleteIntersectionCurve) : ℕ :=
  ((C.canonicalDegree + 2) / 2).toNat

/-- General adjunction relation: whenever `deg K_C ≥ −2` is even,
    `2g(C) − 2 = deg K_C` and `χ_eu(C) = 2 − 2g(C)`. -/
-- Ref: [leitner2026] brings-surface/brings-euler-characteristic-proof.md
theorem adjunction_genus_and_euler (C : SmoothCompleteIntersectionCurve)
    (h_low : -2 ≤ C.canonicalDegree) (h_even : 2 ∣ C.canonicalDegree) :
    2 * (C.arithmeticGenus : ℤ) - 2 = C.canonicalDegree ∧
    C.topologicalEulerChar = 2 - 2 * (C.arithmeticGenus : ℤ) := by
  unfold arithmeticGenus topologicalEulerChar
  obtain ⟨m, hm⟩ := h_even
  omega

end SmoothCompleteIntersectionCurve

/-- **Bring's curve `Σ₄ ⊂ ℙ⁴`** as the smooth complete intersection of the first
    three homogeneous power sums of multidegree `(1, 2, 3)` in `ℙ⁴`. -/
-- Ref: [leitner2026] brings-surface/brings-surface-def.md
def bringsCompleteIntersection : SmoothCompleteIntersectionCurve where
  ambientDim := 4
  degrees := [1, 2, 3]
  codim_eq := rfl
  pos_degrees := by simp

/-- **Adjunction invariants of Bring's surface** derived from `(1, 2, 3)` in `ℙ⁴`:
    `deg(Σ₄) = 6`, canonical twist `k = 1`, `deg K_{Σ₄} = 6`, `g(Σ₄) = 4`,
    `χ_eu(Σ₄) = −6`, and `deg T_{Σ₄} = −6`. -/
-- Ref: [leitner2026] brings-surface/brings-euler-characteristic-proof.md
theorem brings_adjunction_invariants :
    bringsCompleteIntersection.intersectionDegree = 6 ∧
    bringsCompleteIntersection.canonicalTwist = 1 ∧
    bringsCompleteIntersection.canonicalDegree = 6 ∧
    bringsCompleteIntersection.arithmeticGenus = 4 ∧
    bringsCompleteIntersection.topologicalEulerChar = -6 ∧
    bringsCompleteIntersection.tangentDegree = -6 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp [bringsCompleteIntersection,
      SmoothCompleteIntersectionCurve.intersectionDegree,
      SmoothCompleteIntersectionCurve.canonicalTwist,
      SmoothCompleteIntersectionCurve.canonicalDegree,
      SmoothCompleteIntersectionCurve.arithmeticGenus,
      SmoothCompleteIntersectionCurve.topologicalEulerChar,
      SmoothCompleteIntersectionCurve.tangentDegree]

/-- Hodge diamond `h^{p,q}(Σ_g)` of a smooth projective curve of genus `g`:
    `(h^{0,0}, h^{1,0}, h^{0,1}, h^{1,1}) = (1, g, g, 1)`. -/
def curveHodgeNumber (g : ℕ) (p q : Fin 2) : ℕ :=
  match p.val, q.val with
  | 0, 0 => 1
  | 1, 0 => g
  | 0, 1 => g
  | _, _ => 1

/-- HKR Hodge sum for `dim HH_n(Σ_g) = ∑_i dim H^i(Σ_g, Ω^{i+n})` with
    `n = (k : ℤ) − 1 ∈ {−1, 0, 1}` indexed by `k : Fin 3`. -/
def hkrHochschildDim (g : ℕ) (k : Fin 3) : ℕ :=
  ∑ i : Fin 2, ∑ j : Fin 2,
    if (i : ℤ) + ((k : ℤ) - 1) = (j : ℤ) then curveHodgeNumber g j i else 0

/-- Dimension profile `(g, 2, g)` of `(HH_{-1}(Σ_g), HH_0(Σ_g), HH_1(Σ_g))`. -/
def hochschildRank (g : ℕ) : Fin 3 → ℕ
  | 0 => g
  | 1 => 2
  | 2 => g

/-- Explicit `K`-vector-space carrier `K^{dim HH_n(Σ_g)}` (`(K^g, K^2, K^g)`)
    for the Hochschild homology of a smooth curve of genus `g` in degrees
    `n = −1, 0, 1` (`k = 0, 1, 2 : Fin 3`). -/
abbrev CurveHochschildSpace (K : Type*) (g : ℕ) (k : Fin 3) : Type _ :=
  Fin (hochschildRank g k) → K

/-- `finrank` of the model space is its rank (Lean v4.35: `simp` no longer sees
through the `CurveHochschildSpace` abbreviation inside the module instance). -/
theorem finrank_curveHochschildSpace (K : Type*) [Field K] (g : ℕ) (k : Fin 3) :
    Module.finrank K (CurveHochschildSpace K g k) = hochschildRank g k :=
  Module.finrank_fin_fun K

/-- **HKR dimension identity**: for every `k : Fin 3` (`n = k − 1 ∈ {−1, 0, 1}`),
    `Module.finrank K (CurveHochschildSpace K g k)` equals the HKR Hodge sum
    `hkrHochschildDim g k` built from `(h^{0,0}, h^{1,0}, h^{0,1}, h^{1,1}) = (1, g, g, 1)`. -/
-- Ref: [leitner2026] brings-surface/brings-euler-characteristic-proof.md
theorem hkr_finrank_eq_hodge_sum (K : Type*) [Field K] (g : ℕ) (k : Fin 3) :
    Module.finrank K (CurveHochschildSpace K g k) = hkrHochschildDim g k := by
  rw [finrank_curveHochschildSpace]
  fin_cases k <;>
    simp [hochschildRank, hkrHochschildDim,
      curveHodgeNumber, Fin.sum_univ_two]

/-- Sign `(−1)^n` at Hochschild degree `n = (k : ℤ) − 1 ∈ {−1, 0, 1}`. -/
def hochschildDegreeSign (k : Fin 3) : ℤ :=
  (((-1 : ℤˣ) ^ ((k : ℤ) - 1) : ℤˣ) : ℤ)

/-- Alternating Hochschild Euler characteristic
    `∑_{n=−1}^1 (−1)^n · finrank_K HH_n(Σ_g)` over `Fin 3`. -/
noncomputable def hochschildEulerChar (K : Type*) [Field K] (g : ℕ) : ℤ :=
  ∑ k : Fin 3,
    hochschildDegreeSign k * (Module.finrank K (CurveHochschildSpace K g k) : ℤ)

/-- **HKR Euler-characteristic formula** for any genus `g`:
    `∑_{n=−1}^1 (−1)^n dim_K HH_n(Σ_g) = −g + 2 − g = 2 − 2g`. -/
-- Ref: [leitner2026] brings-surface/brings-euler-characteristic-proof.md
theorem hochschild_euler_eq_two_sub_two_genus (K : Type*) [Field K] (g : ℕ) :
    hochschildEulerChar K g = 2 - 2 * (g : ℤ) := by
  simp only [hochschildEulerChar, finrank_curveHochschildSpace]
  simp [hochschildDegreeSign,
    hochschildRank, Fin.sum_univ_three]
  ring

/-- **Lemma** ([`lem:brings-euler-characteristic`]):
    Bring's surface `Σ₄` (the smooth `(1, 2, 3)` complete intersection in `ℙ⁴`)
    has derived adjunction genus `g(Σ₄) = 4` and topological Euler
    characteristic `χ_eu(Σ₄) = 2 − 2g(Σ₄) = −6`; equivalently, in the HKR Hodge
    decomposition of its Hochschild homology over a field `K`,
    `dim_K HH_{-1}(Σ₄) = 4`, `dim_K HH_0(Σ₄) = 2`, `dim_K HH_1(Σ₄) = 4`, and
    the alternating Hochschild Euler sum equals `−6`. -/
-- Ref: [leitner2026] brings-surface/brings-euler-characteristic.md
theorem brings_euler_characteristic (K : Type*) [Field K] :
    let g := bringsCompleteIntersection.arithmeticGenus
    g = 4 ∧
    bringsCompleteIntersection.topologicalEulerChar = 2 - 2 * (g : ℤ) ∧
    bringsCompleteIntersection.topologicalEulerChar = -6 ∧
    Module.finrank K (CurveHochschildSpace K g 0) = 4 ∧
    Module.finrank K (CurveHochschildSpace K g 1) = 2 ∧
    Module.finrank K (CurveHochschildSpace K g 2) = 4 ∧
    hochschildEulerChar K g = -6 := by
  obtain ⟨_, _, _, hg4, hchi, _⟩ := brings_adjunction_invariants
  dsimp only
  refine ⟨hg4, ?_, hchi, ?_, ?_, ?_, ?_⟩
  · rw [hg4, hchi]
    norm_num
  · rw [finrank_curveHochschildSpace]; simp [hochschildRank, hg4]
  · rw [finrank_curveHochschildSpace]; simp [hochschildRank]
  · rw [finrank_curveHochschildSpace]; simp [hochschildRank, hg4]
  · rw [hochschild_euler_eq_two_sub_two_genus, hg4]
    norm_num

/-! ## Backward-compatible context interface -/

/-- Geometric context for the Euler-characteristic interface over a ground ring `R`. -/
class BringsEulerCharacteristicContext (R : Type*) [CommRing R] where
  /-- Substrate parameter `q₀ ∈ R`. -/
  q0 : R
  /-- Genus of Bring's surface. -/
  g : ℕ
  /-- `g(Σ₄) = 4`. -/
  genus_is_four : g = 4

namespace BringsEulerCharacteristicContext

/-- Canonical constructor populating `BringsEulerCharacteristicContext` from the
    derived `(1, 2, 3)` adjunction genus of `bringsCompleteIntersection`. -/
def ofAdjunction {R : Type*} [CommRing R] (q0 : R) :
    BringsEulerCharacteristicContext R where
  q0 := q0
  g := bringsCompleteIntersection.arithmeticGenus
  genus_is_four := brings_adjunction_invariants.2.2.2.1

variable {R : Type*} [CommRing R] [ctx : BringsEulerCharacteristicContext R]

/-- Topological Euler characteristic `2 − 2g`. -/
def chi_A : ℤ := 2 - 2 * (ctx.g : ℤ)

/-- Quantum dimension `dim_q 𝟙 = 1` of the monoidal unit. -/
def qdimUnit (_q : R) : R := 1

/-- Alternating super-trace `1·dim_q𝟙 − 2g·dim_q𝟙 + 1·dim_q𝟙` over `H^*(Σ_g)`. -/
def categoricalTrace (q : R) : R :=
  1 * qdimUnit q - (2 * (ctx.g : R)) * qdimUnit q + 1 * qdimUnit q

end BringsEulerCharacteristicContext

variable {R : Type*} [CommRing R]

/-- Alternating cohomology super-trace equals `2 − 2g` for every `q`. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/brings-euler-characteristic.md
theorem categorical_trace_eq_euler [ctx : BringsEulerCharacteristicContext R] (q : R) :
    BringsEulerCharacteristicContext.categoricalTrace (R := R) q = 2 - 2 * (ctx.g : R) := by
  unfold BringsEulerCharacteristicContext.categoricalTrace BringsEulerCharacteristicContext.qdimUnit
  ring

/-- `q`-independence of the alternating cohomology super-trace. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/brings-euler-characteristic.md
theorem categorical_trace_q_independent
    [ctx : BringsEulerCharacteristicContext R] (q q' : R) :
    BringsEulerCharacteristicContext.categoricalTrace (R := R) q
      = BringsEulerCharacteristicContext.categoricalTrace (R := R) q' := by
  rw [categorical_trace_eq_euler, categorical_trace_eq_euler]

/-- Alternating cohomology super-trace evaluates to `−6` at `g = 4`. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/brings-euler-characteristic.md
theorem categorical_trace_eq_neg_six
    [ctx : BringsEulerCharacteristicContext R] (q : R) :
    BringsEulerCharacteristicContext.categoricalTrace (R := R) q = -6 := by
  rw [categorical_trace_eq_euler, ctx.genus_is_four]
  norm_num

/-- Specialisation at `q₀` agrees with `chi_A = −6` in `R`. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/brings-euler-characteristic.md
theorem quantum_dimension_recovers_chi [ctx : BringsEulerCharacteristicContext R] :
    BringsEulerCharacteristicContext.categoricalTrace (R := R) ctx.q0
      = ((BringsEulerCharacteristicContext.chi_A (R := R) : ℤ) : R) := by
  have hchi : BringsEulerCharacteristicContext.chi_A (R := R) = -6 := by
    unfold BringsEulerCharacteristicContext.chi_A
    rw [ctx.genus_is_four]
    norm_num
  rw [categorical_trace_eq_neg_six, hchi]
  norm_num

end QOU.ArchimedeanUniverse
