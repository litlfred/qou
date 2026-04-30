import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Wedderburn Mass Formula — three-invariant atomic mass

For a neutral atom `(Z, N)` with `n_gen` Hecke-NF generators, the
mass decomposes as the sum of nucleon and electron rest masses plus
a Wedderburn-weighted binding term:

  `M(Z, N) = Z · m_p + N · m_n + Z · m_e + α · Σᵢ ln |V̂ᵢ^full|`

where the **full traced volume** per generator is the Wedderburn
sum

  `V̂ᵢ^full = w_sym · λᵢ^sym + w_std · V̂ᵢ^std + w_alt · λᵢ^alt`

and the Wedderburn–Markov weights at the baryon level `n = 3` are

  `w_sym = w_alt = 1 / [3]_q!`,
  `w_std = [2]_q² / [3]_q!`,    where `[3]_q! = (1+q+q²)(1+q)`.

The binding scale `α = m_e · 8G` (Catalan, `Vol(B_3) = 8G`).

LaTeX: `\label{prop:wedderburn-mass-formula}`

This file encodes the formula structurally as `wedderburnMass`, with
opaques only for genuinely empirical / Hoefsmit inputs (`m_p, m_n,
m_e, V_std, lambda_sym, lambda_alt`). The proven theorems are
structural identities that follow by `rfl` / `ring` from the
definition; the underlying Hoefsmit positivity / Catalan-volume
witnesses remain unproved (axiomatised with explicit `Ref:`).

## References
- [chenier2026] manuscript, particle-interactions/wedderburn-mass-formula
- [wedderburn1908] https://doi.org/10.1112/plms/s2-6.1.77
- [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
-/

namespace QOU.Interactions

open scoped BigOperators

/-! ## Inputs (opaque physical / Hoefsmit data) -/

/-- Proton rest mass (CODATA 2022, MeV/c²). -/
-- Ref: [codata2022] https://doi.org/10.1103/RevModPhys.97.025002
noncomputable def m_p : ℝ := 938.27208943

/-- Neutron rest mass (CODATA 2022, MeV/c²). -/
-- Ref: [codata2022] https://doi.org/10.1103/RevModPhys.97.025002
noncomputable def m_n : ℝ := 939.56542194

/-- Electron rest mass (CODATA 2022, MeV/c²). -/
-- Ref: [codata2022] https://doi.org/10.1103/RevModPhys.97.025002
noncomputable def m_e : ℝ := 0.51099895069

/-- Catalan's constant `G ≈ 0.91596...`. Wired as opaque pending
    Mathlib `Real.catalan` (not yet in the toolchain). -/
-- Ref: [chenier2026] manuscript, particle-interactions/wedderburn-mass-formula
opaque catalan_G : ℝ

/-- The number of Hecke NF generators contributing to the binding
    term for an atom. The proton at level `n = 3` has 6 NF basis
    elements; this is parameterised so heavier atoms can use larger
    bases. -/
-- Ref: [manuscript] particle-interactions/wedderburn-mass-formula
opaque numGenerators : ℕ

/-- Standard-representation traced volume `V̂ᵢ^std = z·aᵢ + bᵢ`
    of generator `i` for the chosen braid representative of
    `(Z, N)` at substrate `q`. Opaque because the integer
    coefficients `aᵢ, bᵢ` come from the Hoefsmit seminormal form. -/
-- Ref: [manuscript] particle-interactions/wedderburn-mass-formula
opaque V_std (Z N : ℕ) : ℕ → ℝ → ℝ

/-- Symmetric eigenvalue product `λᵢ^sym = ∏ⱼ (cⱼ q + dⱼ)`. -/
-- Ref: [manuscript] particle-interactions/wedderburn-mass-formula
opaque lambda_sym (Z N : ℕ) : ℕ → ℝ → ℝ

/-- Alternating eigenvalue product `λᵢ^alt = ∏ⱼ (-cⱼ q⁻¹ + dⱼ)`. -/
-- Ref: [manuscript] particle-interactions/wedderburn-mass-formula
opaque lambda_alt (Z N : ℕ) : ℕ → ℝ → ℝ

/-! ## Closed-form Wedderburn weights -/

/-- The `q`-integer `[2]_q = 1 + q`. -/
noncomputable def q_int_2 (q : ℝ) : ℝ := 1 + q

/-- The `q`-integer `[3]_q = 1 + q + q²`. -/
noncomputable def q_int_3 (q : ℝ) : ℝ := 1 + q + q^2

/-- The `q`-factorial `[3]_q! = [3]_q · [2]_q · [1]_q
    = (1 + q + q²)(1 + q)`. -/
noncomputable def q_fact_3 (q : ℝ) : ℝ := q_int_3 q * q_int_2 q

/-- Symmetric Wedderburn weight `w_sym = 1 / [3]_q!`. -/
noncomputable def w_sym (q : ℝ) : ℝ := 1 / q_fact_3 q

/-- Alternating Wedderburn weight `w_alt = 1 / [3]_q!`. -/
noncomputable def w_alt (q : ℝ) : ℝ := 1 / q_fact_3 q

/-- Standard Wedderburn weight `w_std = [2]_q² / [3]_q!`. -/
noncomputable def w_std (q : ℝ) : ℝ := (q_int_2 q)^2 / q_fact_3 q

/-- Binding scale `α = m_e · 8 G`. -/
noncomputable def alpha_bind : ℝ := m_e * 8 * catalan_G

/-! ## Formula -/

/-- Full Wedderburn-weighted traced volume per generator `i`:
    `V̂ᵢ^full = w_sym · λᵢ^sym + w_std · V̂ᵢ^std + w_alt · λᵢ^alt`. -/
noncomputable def V_full (Z N : ℕ) (i : ℕ) (q : ℝ) : ℝ :=
  w_sym q * lambda_sym Z N i q
  + w_std q * V_std Z N i q
  + w_alt q * lambda_alt Z N i q

/-- The three-invariant Wedderburn binding term
    `α · Σᵢ ln |V̂ᵢ^full|` summed over the chosen NF generators. -/
noncomputable def bindingTerm (Z N : ℕ) (q : ℝ) : ℝ :=
  alpha_bind * ∑ i ∈ Finset.range numGenerators, Real.log |V_full Z N i q|

/-- **Wedderburn neutral-atom mass.**
    `M(Z, N) = Z · m_p + N · m_n + Z · m_e
              + α · Σᵢ ln |V̂ᵢ^full|`. -/
noncomputable def wedderburnMass (Z N : ℕ) (q : ℝ) : ℝ :=
  (Z : ℝ) * m_p + (N : ℝ) * m_n + (Z : ℝ) * m_e + bindingTerm Z N q

/-! ## Theorems -/

/-- **Wedderburn mass formula (definitional expansion).** The mass
    splits canonically into nucleon, electron, and binding
    contributions. This is the structural content of
    `prop:wedderburn-mass-formula` — the only remaining empirical
    inputs are the Hoefsmit eigenvalues (`V_std`, `λ^sym`, `λ^alt`)
    and the rest masses (`m_p`, `m_n`, `m_e`); the Wedderburn
    weights are derived in closed form from `q`. -/
-- Ref: [manuscript] particle-interactions/wedderburn-mass-formula
-- Ref: [wedderburn1908] https://doi.org/10.1112/plms/s2-6.1.77
theorem wedderburnMass_split (Z N : ℕ) (q : ℝ) :
    wedderburnMass Z N q
      = (Z : ℝ) * m_p + (N : ℝ) * m_n + (Z : ℝ) * m_e
        + bindingTerm Z N q := by
  rfl

/-- **Wedderburn weight identity at the baryon level.** The three
    weights sum, with multiplicities `(1, 1, 1)` weighted by the
    representation dimensions `(1, [2]_q, 1) = (1, [2]_q, 1)`, to
    the obvious closed-form expression. Concretely:
    `w_sym + w_std + w_alt = (2 + [2]_q²) / [3]_q!`. -/
-- Ref: [manuscript] particle-interactions/wedderburn-mass-formula
theorem wedderburn_weights_sum (q : ℝ) (hq : q_fact_3 q ≠ 0) :
    w_sym q + w_std q + w_alt q
      = (2 + (q_int_2 q)^2) / q_fact_3 q := by
  unfold w_sym w_std w_alt
  field_simp
  ring

/-- **Zero-fitted-parameter property.** The Wedderburn weights are
    determined by `q` alone — they contain no free coupling
    constants. In particular, at any pinned `q`, the values of
    `w_sym, w_std, w_alt` are functions of `q` only (this is just
    the definitional content of the closed-form weights, but
    documenting it as a theorem records the no-parameter property
    asserted by `prop:wedderburn-mass-formula`). -/
-- Ref: [manuscript] particle-interactions/wedderburn-mass-formula
theorem wedderburn_weights_q_only (q₁ q₂ : ℝ) (hq : q₁ = q₂) :
    (w_sym q₁, w_std q₁, w_alt q₁) = (w_sym q₂, w_std q₂, w_alt q₂) := by
  rw [hq]

end QOU.Interactions
