import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.Tactic.FinCases

/-!
# QOU.StandardModel.ColourHeckeRegularHost — the colour action cannot live on the
regular three-strand Hecke carrier (a Hecke-compatibility obstruction)

The colour conjecture `conj:sm-colour-stabilizer-action` records, as its
surviving open content, an action of the colour algebra `𝔰𝔲(3) = ker(ev_e)`
(8-dimensional by the corpus gate) on *the framework's own three-strand Hecke
state space*, **compatible with its braid/Hecke structure** — "not merely some
faithful module somewhere."

The abstract class `QOU.StandardModel.ColourStabilizerAction` asks only for an
injective **linear** map `g →ₗ End V`. That is tautologically satisfiable for
any `V` with `finrank V ≥ 3` (since `8 ≤ 3² = 9`); the octonion base module
already witnesses it (`OctonionColourActionBaseModule`), and so would *any*
6-dimensional `V`. So instantiating the weak class on the Hecke carrier closes
nothing — the genuine content is **Hecke-compatibility**.

The framework's own three-strand state space is the **6-dimensional regular
carrier** `H₃(q)` implemented in `QOU.Mathlib.HeckeAlgebra` as
`H3Carrier = ℚ⁶`, with the two braid generators acting by left multiplication
`H3.mulSigma1`, `H3.mulSigma2`. Modelling it here as `Fin 6 → ℚ` (the same
basis `{1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁}`, positions `0..5`), the generators are
the matrices `L₁ = mulSigma1`, `L₂ = mulSigma2` (formulas copied verbatim from
`HeckeAlgebra.lean`, reproduced self-contained so this file verifies against
Mathlib alone).

**Result (this file, sorry-free).** "Hecke-compatible" in the Schur–Weyl sense
means the colour action **commutes with the Hecke action** `L₁, L₂`. On the
regular carrier this is *structurally impossible* for an 8-dimensional colour
algebra:

* `evAtOne_injective` — the centralizer of the regular Hecke action injects into
  `V` by evaluation at the cyclic vector `1 = e₀` (the six words
  `1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁` applied to `e₀` are the standard basis, so a
  centralizing `T` is determined by `T e₀`).
* `finrank_heckeCentralizer_le_six` — hence `finrank (centralizer) ≤ 6`.
* `no_heckeCompatible_colour_action_on_regularH3` — no injective linear
  `Φ : g →ₗ End V` with every `Φ x` commuting with `L₁, L₂` exists when
  `finrank g = 8`, since it would force `8 ≤ 6`.

This is a **scope-(b) structural exclusion** (per AGENTS.md "Before declaring
refuted"), cited to a *proved dimension invariant* — `finrank(End_{H₃}(H₃)) =
finrank H₃ = 6 < 8`. It is scoped to the **regular carrier** with the
**centralizer** reading of compatibility; it does **not** exclude the colour
action on the larger Schur–Weyl tensor host `(ℂ³)^{⊗3}` (dim 27), where the
Hecke centralizer is the DV–Todorov diagonal `𝔰𝔲(3)` itself. That positive
construction is the genuine remaining open derivation (see the conjecture's
`authorNotes`).

Applies to `𝔰𝔲(3) = ker(ev_e)` via the corpus gate `finrank (su3 e) = 8`
(`QOU.MathlibExt.OctonionSU3Stabilizer`): substitute `g := ↥(su3 e)`.

Base ring ℚ; exact rational linear algebra, nothing archimedean.
-/

namespace QOU.StandardModel.ColourHeckeRegularHost

open Matrix Module

/-- The framework's 6-dimensional regular three-strand Hecke state space,
`H3Carrier = ℚ⁶` (basis `{1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁}` at positions `0..5`),
modelled as `Fin 6 → ℚ`. -/
abbrev V : Type := Fin 6 → ℚ

/-- Hecke off-diagonal weight `d = q − q⁻¹` (the coefficient in
`σ_i² = (q − q⁻¹)σ_i + 1`). -/
def d (q : ℚ) : ℚ := q - q⁻¹

/-- Matrix of **left-multiplication by `σ₁`** on the regular carrier, copied
from `QOU.Mathlib.HeckeAlgebra.H3.mulSigma1`. Row `i` = coefficients of the
`i`-th output coordinate:
`(x₁, x₀+d·x₁, x₃, x₂+d·x₃, x₅, x₄+d·x₅)`. -/
def M1 (q : ℚ) : Matrix (Fin 6) (Fin 6) ℚ :=
  !![0, 1, 0, 0, 0, 0;
     1, d q, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 0;
     0, 0, 1, d q, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 1, d q]

/-- Matrix of **left-multiplication by `σ₂`** on the regular carrier, copied
from `QOU.Mathlib.HeckeAlgebra.H3.mulSigma2`. Output
`(x₂, x₄, x₀+d·x₂, x₅, x₁+d·x₄, x₃+d·x₅)`. -/
def M2 (q : ℚ) : Matrix (Fin 6) (Fin 6) ℚ :=
  !![0, 0, 1, 0, 0, 0;
     0, 0, 0, 0, 1, 0;
     1, 0, d q, 0, 0, 0;
     0, 0, 0, 0, 0, 1;
     0, 1, 0, 0, d q, 0;
     0, 0, 0, 1, 0, d q]

/-- Left-multiplication by `σ₁` as an endomorphism of the state space. -/
noncomputable def L1 (q : ℚ) : Module.End ℚ V := Matrix.toLin' (M1 q)

/-- Left-multiplication by `σ₂` as an endomorphism of the state space. -/
noncomputable def L2 (q : ℚ) : Module.End ℚ V := Matrix.toLin' (M2 q)

/-- The **Hecke centralizer**: endomorphisms of the state space commuting with
both regular Hecke generators — the target of a Hecke-compatible colour action
(Schur–Weyl reading). A submodule as the intersection of the two commuting
kernels. -/
noncomputable def heckeCentralizer (q : ℚ) : Submodule ℚ (Module.End ℚ V) :=
  LinearMap.ker (LinearMap.mulRight ℚ (L1 q) - LinearMap.mulLeft ℚ (L1 q)) ⊓
  LinearMap.ker (LinearMap.mulRight ℚ (L2 q) - LinearMap.mulLeft ℚ (L2 q))

/-- Membership unfolds to the two commuting relations `T * Lᵢ = Lᵢ * T`. -/
theorem mem_heckeCentralizer_iff (q : ℚ) (T : Module.End ℚ V) :
    T ∈ heckeCentralizer q ↔ T * L1 q = L1 q * T ∧ T * L2 q = L2 q * T := by
  simp only [heckeCentralizer, Submodule.mem_inf, LinearMap.mem_ker,
    LinearMap.sub_apply, LinearMap.mulRight_apply, LinearMap.mulLeft_apply,
    sub_eq_zero]

/-! ### The cyclic vector and the five word steps

`e₀ = 1` is a cyclic vector for the regular action: the six basis words
`1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁` are `L`-words applied to `e₀`. We only need the
five generator steps that reach `e₁,…,e₅`; each is a column read-off of `M₁/M₂`
that is `d`-free (the `q`-dependent diagonal entries multiply zero). -/

/-- Standard basis vector `eᵢ` of the state space (`= Pi.basisFun ℚ (Fin 6) i`). -/
def sb (k : Fin 6) : V := Pi.single k 1

theorem sb_eq_basisFun (k : Fin 6) : sb k = Pi.basisFun ℚ (Fin 6) k := by
  simp [sb, Pi.basisFun_apply]

/-- `σ₁ · 1 = σ₁`: `L₁ e₀ = e₁`. -/
theorem L1_sb0 (q : ℚ) : L1 q (sb 0) = sb 1 := by
  funext i; fin_cases i <;>
    simp [L1, M1, sb, d, Matrix.toLin'_apply, Matrix.mulVec]

/-- `σ₂ · 1 = σ₂`: `L₂ e₀ = e₂`. -/
theorem L2_sb0 (q : ℚ) : L2 q (sb 0) = sb 2 := by
  funext i; fin_cases i <;>
    simp [L2, M2, sb, d, Matrix.toLin'_apply, Matrix.mulVec]

/-- `σ₁ · σ₂ = σ₁σ₂`: `L₁ e₂ = e₃`. -/
theorem L1_sb2 (q : ℚ) : L1 q (sb 2) = sb 3 := by
  funext i; fin_cases i <;>
    simp [L1, M1, sb, d, Matrix.toLin'_apply, Matrix.mulVec]

/-- `σ₂ · σ₁ = σ₂σ₁`: `L₂ e₁ = e₄`. -/
theorem L2_sb1 (q : ℚ) : L2 q (sb 1) = sb 4 := by
  funext i; fin_cases i <;>
    simp [L2, M2, sb, d, Matrix.toLin'_apply, Matrix.mulVec]

/-- `σ₁ · σ₂σ₁ = σ₁σ₂σ₁`: `L₁ e₄ = e₅`. -/
theorem L1_sb4 (q : ℚ) : L1 q (sb 4) = sb 5 := by
  funext i; fin_cases i <;>
    simp [L1, M1, sb, d, Matrix.toLin'_apply, Matrix.mulVec]

/-! ### Evaluation at the cyclic vector is injective on the centralizer -/

/-- Evaluation-at-`e₀` on the Hecke centralizer, `T ↦ T e₀`, as a linear map. -/
noncomputable def evAtOne (q : ℚ) : heckeCentralizer q →ₗ[ℚ] V :=
  (LinearMap.applyₗ (sb 0)).comp (heckeCentralizer q).subtype

@[simp] theorem evAtOne_apply (q : ℚ) (T : heckeCentralizer q) :
    evAtOne q T = (T : Module.End ℚ V) (sb 0) := rfl

/-- **A centralizing endomorphism is determined by its value on the cyclic
vector.** If `T` commutes with `L₁, L₂` and kills `e₀`, then `T = 0`: it kills
each basis word `eₖ = (L-word) e₀`, and those span `V`. -/
theorem centralizing_eval_zero_eq_zero (q : ℚ) (T : Module.End ℚ V)
    (hc1 : T * L1 q = L1 q * T) (hc2 : T * L2 q = L2 q * T)
    (hker : T (sb 0) = 0) : T = 0 := by
  -- `T` kills each standard basis vector `eₖ`, reached from `e₀` by a word.
  -- `e₁ = L₁ e₀`:
  have e1 : T (sb 1) = 0 := by
    have h := LinearMap.congr_fun hc1 (sb 0)
    rw [Module.End.mul_apply, Module.End.mul_apply, L1_sb0, hker, map_zero] at h
    exact h
  -- `e₂ = L₂ e₀`:
  have e2 : T (sb 2) = 0 := by
    have h := LinearMap.congr_fun hc2 (sb 0)
    rw [Module.End.mul_apply, Module.End.mul_apply, L2_sb0, hker, map_zero] at h
    exact h
  -- `e₃ = L₁ e₂`:
  have e3 : T (sb 3) = 0 := by
    have h := LinearMap.congr_fun hc1 (sb 2)
    rw [Module.End.mul_apply, Module.End.mul_apply, L1_sb2, e2, map_zero] at h
    exact h
  -- `e₄ = L₂ e₁`:
  have e4 : T (sb 4) = 0 := by
    have h := LinearMap.congr_fun hc2 (sb 1)
    rw [Module.End.mul_apply, Module.End.mul_apply, L2_sb1, e1, map_zero] at h
    exact h
  -- `e₅ = L₁ e₄`:
  have e5 : T (sb 5) = 0 := by
    have h := LinearMap.congr_fun hc1 (sb 4)
    rw [Module.End.mul_apply, Module.End.mul_apply, L1_sb4, e4, map_zero] at h
    exact h
  have key : ∀ k : Fin 6, T (sb k) = 0 := by
    intro k
    fin_cases k
    · exact hker
    · exact e1
    · exact e2
    · exact e3
    · exact e4
    · exact e5
  -- `T` vanishes on the standard basis, hence `T = 0`.
  apply (Pi.basisFun ℚ (Fin 6)).ext
  intro i
  rw [← sb_eq_basisFun]
  simpa using key i

/-- **Evaluation at the cyclic vector is injective on the Hecke centralizer.**
Two centralizing endomorphisms agreeing at `e₀` agree everywhere. -/
theorem evAtOne_injective (q : ℚ) : Function.Injective (evAtOne q) := by
  intro a b hab
  -- The difference `a - b` is centralizing and kills `e₀`, hence is `0`.
  obtain ⟨ha1, ha2⟩ := (mem_heckeCentralizer_iff q _).1 a.property
  obtain ⟨hb1, hb2⟩ := (mem_heckeCentralizer_iff q _).1 b.property
  have hdiff : ((a : Module.End ℚ V) - b) = 0 := by
    refine centralizing_eval_zero_eq_zero q _ ?_ ?_ ?_
    · rw [sub_mul, mul_sub, ha1, hb1]
    · rw [sub_mul, mul_sub, ha2, hb2]
    · have h : (a : Module.End ℚ V) (sb 0) = (b : Module.End ℚ V) (sb 0) := by
        simpa only [evAtOne_apply] using hab
      simp [LinearMap.sub_apply, h]
  exact Subtype.ext (sub_eq_zero.1 hdiff)

/-! ### The dimension obstruction -/

/-- `finrank V = 6` (the regular carrier is 6-dimensional). -/
theorem finrank_V : finrank ℚ V = 6 := by
  simp [V]

/-- **The Hecke centralizer on the regular carrier is at most 6-dimensional.**
`finrank(End_{H₃}(H₃)) ≤ finrank H₃ = 6`. -/
theorem finrank_heckeCentralizer_le_six (q : ℚ) :
    finrank ℚ (heckeCentralizer q) ≤ 6 := by
  have h := LinearMap.finrank_le_finrank_of_injective (evAtOne_injective q)
  rwa [finrank_V] at h

/-- **G3 colour-action obstruction (scope-(b) structural exclusion).** No
faithful colour action of an 8-dimensional colour algebra `g` on the framework's
own 6-dimensional regular three-strand Hecke state space can be **Hecke-
compatible** (commute with both braid generators `L₁, L₂`): such a `Φ` would
land in the Hecke centralizer, whose dimension is `≤ 6 < 8`.

The invariant cited is the proved `finrank_heckeCentralizer_le_six`. Applies to
`𝔰𝔲(3) = ker(ev_e)` via the corpus gate `finrank (su3 e) = 8`. It does **not**
exclude the colour action on the Schur–Weyl tensor host `(ℂ³)^{⊗3}`. -/
theorem no_heckeCompatible_colour_action_on_regularH3
    (q : ℚ) (g : Type*) [AddCommGroup g] [Module ℚ g] [FiniteDimensional ℚ g]
    (h8 : finrank ℚ g = 8)
    (Φ : g →ₗ[ℚ] Module.End ℚ V) (hinj : Function.Injective Φ)
    (hcomm : ∀ x, Φ x * L1 q = L1 q * Φ x ∧ Φ x * L2 q = L2 q * Φ x) :
    False := by
  have hmem : ∀ x, Φ x ∈ heckeCentralizer q := fun x =>
    (mem_heckeCentralizer_iff q _).2 (hcomm x)
  set Φ' : g →ₗ[ℚ] heckeCentralizer q :=
    LinearMap.codRestrict (heckeCentralizer q) Φ hmem with hΦ'
  have hinj' : Function.Injective Φ' := by
    intro a b hab
    apply hinj
    have := congrArg (Subtype.val) hab
    simpa [hΦ', LinearMap.codRestrict] using this
  have hle : finrank ℚ g ≤ finrank ℚ (heckeCentralizer q) :=
    LinearMap.finrank_le_finrank_of_injective hinj'
  have h6 := finrank_heckeCentralizer_le_six q
  rw [h8] at hle
  omega

end QOU.StandardModel.ColourHeckeRegularHost
