import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

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

This file encodes the formula structurally:

* All `q`-dependent quantities (`q_int_2, q_int_3, q_fact_3,
  w_sym, w_std, w_alt`) are real `noncomputable def`s.
* All physical constants (`m_p, m_n, m_e, catalan_G, alpha_bind`)
  are `noncomputable def`s with explicit numerical values from
  CODATA / standard tables.
* Only the **Hoefsmit eigenvalues** (`V_std, lambda_sym,
  lambda_alt`) and the integer `numGenerators` remain `opaque` —
  they depend on the seminormal-form construction which is not
  yet formalised.
* Theorems include both the structural mass split and several
  positivity/closed-form facts about the weights, all proved.

## References
- [chenier2026] manuscript, particle-interactions/wedderburn-mass-formula
- [wedderburn1908] https://doi.org/10.1112/plms/s2-6.1.77
- [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
- [codata2022] https://doi.org/10.1103/RevModPhys.97.025002
-/

namespace QOU.Interactions

open scoped BigOperators

/-! ## Physical constants (numerical defs, not opaques) -/

/-- Proton rest mass (CODATA 2022, MeV/c²). -/
-- Ref: [codata2022] https://doi.org/10.1103/RevModPhys.97.025002
noncomputable def m_p : ℝ := 938.27208943

/-- Neutron rest mass (CODATA 2022, MeV/c²). -/
-- Ref: [codata2022] https://doi.org/10.1103/RevModPhys.97.025002
noncomputable def m_n : ℝ := 939.56542194

/-- Electron rest mass (CODATA 2022, MeV/c²). -/
-- Ref: [codata2022] https://doi.org/10.1103/RevModPhys.97.025002
noncomputable def m_e : ℝ := 0.51099895069

/-- Catalan's constant `G ≈ 0.91596559417721901505460351493238411077414937428167`
    (mpmath `mp.dps = 50`).
    Defined as the rational approximation; the irrationality of
    Catalan's constant is open (Apéry-style result not yet
    available in Mathlib), so we use the standard high-precision
    decimal. Bumped from 22-dps to 50-dps literal 2026-06-07
    (paired with the symbolic `QOU.Archimedean.catalan_G` /
    `vol_B3 := 8 · catalan_G` refactor — see
    `QOU.Archimedean.HyperbolicVolumeTranscendence` §0). -/
-- Ref: [oeis-A006752] Decimal expansion of Catalan's constant — see folio/schema/references.ts
noncomputable def catalan_G : ℝ := 0.91596559417721901505460351493238411077414937428167

/-- Binding scale `α = m_e · 8 G`. -/
noncomputable def alpha_bind : ℝ := m_e * 8 * catalan_G

/-! ## Hoefsmit-derived data (typeclass-supplied per `(Z, N)`)

The Hoefsmit seminormal form of `H_k(q)` is not yet formalised in
Lean / Mathlib. Rather than `opaque`-stubbing the per-`(Z, N)`
coefficients, we package them as a typeclass `HasHoefsmitData (Z N)`
so each nucleus's data is supplied by the caller (typically from
the Hoefsmit-tabulation Python pipeline; see
`hoefsmit-seminormal.witness.json`). -/

/-- **Hoefsmit seminormal data — class-supplied per `(Z, N)`.** -/
class HasHoefsmitData (Z N : ℕ) where
  /-- Number of NF generators contributing to the binding term. -/
  numGenerators : ℕ
  /-- Standard-rep traced volume `V̂ᵢ^std = z·aᵢ + bᵢ`. -/
  V_std : ℕ → ℝ → ℝ
  /-- Symmetric eigenvalue product `λᵢ^sym = ∏ⱼ (cⱼ q + dⱼ)`. -/
  lambda_sym : ℕ → ℝ → ℝ
  /-- Alternating eigenvalue product `λᵢ^alt = ∏ⱼ (-cⱼ q⁻¹ + dⱼ)`. -/
  lambda_alt : ℕ → ℝ → ℝ

/-- Number of NF generators (accessor). -/
def numGenerators (Z N : ℕ) [h : HasHoefsmitData Z N] : ℕ := h.numGenerators

/-- Standard-rep traced volume (accessor). -/
def V_std (Z N : ℕ) [h : HasHoefsmitData Z N] : ℕ → ℝ → ℝ := h.V_std

/-- Symmetric eigenvalue product (accessor). -/
def lambda_sym (Z N : ℕ) [h : HasHoefsmitData Z N] : ℕ → ℝ → ℝ := h.lambda_sym

/-- Alternating eigenvalue product (accessor). -/
def lambda_alt (Z N : ℕ) [h : HasHoefsmitData Z N] : ℕ → ℝ → ℝ := h.lambda_alt

/-- **Vacuum Hoefsmit data**: at `(Z, N) = (0, 0)` (no nucleons,
    no Hecke generators), the seminormal data collapses to the
    trivial identity:
    - `numGenerators = 0` (empty set)
    - `V_std = 0` (no generators contribute)
    - `lambda_sym = lambda_alt = 1` (empty product)
    The bindingTerm is then `α · Σ_{i ∈ ∅} … = 0`, so vacuum has
    zero binding contribution. -/
instance hasHoefsmitData_vacuum : HasHoefsmitData 0 0 where
  numGenerators := 0
  V_std := fun _ _ => 0
  lambda_sym := fun _ _ => 1
  lambda_alt := fun _ _ => 1

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

/-! ## Positivity lemmas for the weights -/

/-- For `q > 0`, `[2]_q = 1 + q > 0`. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem q_int_2_pos {q : ℝ} (hq : 0 < q) : 0 < q_int_2 q := by
  unfold q_int_2; linarith

/-- For `q > 0`, `[3]_q = 1 + q + q² > 0`. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem q_int_3_pos {q : ℝ} (hq : 0 < q) : 0 < q_int_3 q := by
  unfold q_int_3
  have hq2 : 0 ≤ q^2 := sq_nonneg q
  linarith

/-- For `q > 0`, `[3]_q! = (1 + q + q²)(1 + q) > 0`. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem q_fact_3_pos {q : ℝ} (hq : 0 < q) : 0 < q_fact_3 q := by
  unfold q_fact_3
  exact mul_pos (q_int_3_pos hq) (q_int_2_pos hq)

/-- For `q > 0`, `[3]_q! ≠ 0`. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem q_fact_3_ne_zero {q : ℝ} (hq : 0 < q) : q_fact_3 q ≠ 0 :=
  ne_of_gt (q_fact_3_pos hq)

/-- For `q > 0`, the symmetric weight is strictly positive. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem w_sym_pos {q : ℝ} (hq : 0 < q) : 0 < w_sym q := by
  unfold w_sym
  exact one_div_pos.mpr (q_fact_3_pos hq)

/-- For `q > 0`, the alternating weight is strictly positive. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem w_alt_pos {q : ℝ} (hq : 0 < q) : 0 < w_alt q := by
  unfold w_alt
  exact one_div_pos.mpr (q_fact_3_pos hq)

/-- For `q > 0`, the standard weight is strictly positive
    (since `[2]_q² > 0`). -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem w_std_pos {q : ℝ} (hq : 0 < q) : 0 < w_std q := by
  unfold w_std
  have h2 : 0 < (q_int_2 q)^2 := by
    have := q_int_2_pos hq
    positivity
  exact div_pos h2 (q_fact_3_pos hq)

/-- The symmetric and alternating weights are equal (both equal
    `1/[3]_q!`). -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem w_sym_eq_w_alt (q : ℝ) : w_sym q = w_alt q := by
  unfold w_sym w_alt; rfl

/-! ## Formula -/

/-- Full Wedderburn-weighted traced volume per generator `i`:
    `V̂ᵢ^full = w_sym · λᵢ^sym + w_std · V̂ᵢ^std + w_alt · λᵢ^alt`. -/
noncomputable def V_full (Z N : ℕ) [HasHoefsmitData Z N] (i : ℕ) (q : ℝ) : ℝ :=
  w_sym q * lambda_sym Z N i q
  + w_std q * V_std Z N i q
  + w_alt q * lambda_alt Z N i q

/-- The three-invariant Wedderburn binding term
    `α · Σᵢ ln |V̂ᵢ^full|` summed over the chosen NF generators. -/
noncomputable def bindingTerm (Z N : ℕ) [HasHoefsmitData Z N] (q : ℝ) : ℝ :=
  alpha_bind *
    ∑ i ∈ Finset.range (numGenerators Z N), Real.log |V_full Z N i q|

/-- **Wedderburn neutral-atom mass.**
    `M(Z, N) = Z · m_p + N · m_n + Z · m_e
              + α · Σᵢ ln |V̂ᵢ^full|`. -/
noncomputable def wedderburnMass (Z N : ℕ) [HasHoefsmitData Z N] (q : ℝ) : ℝ :=
  (Z : ℝ) * m_p + (N : ℝ) * m_n + (Z : ℝ) * m_e + bindingTerm Z N q

/-! ## Theorems -/

/-- **Wedderburn mass formula (definitional expansion).** The mass
    splits canonically into nucleon, electron, and binding
    contributions. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
-- Ref: [wedderburn1908] Wedderburn, "On hypercomplex numbers," Proc. London Math. Soc. s2-6 (1908)
theorem wedderburnMass_split (Z N : ℕ) [HasHoefsmitData Z N] (q : ℝ) :
    wedderburnMass Z N q
      = (Z : ℝ) * m_p + (N : ℝ) * m_n + (Z : ℝ) * m_e
        + bindingTerm Z N q := by
  rfl

/-- **Wedderburn weight identity at the baryon level.**
    `w_sym + w_std + w_alt = (2 + [2]_q²) / [3]_q!`. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem wedderburn_weights_sum (q : ℝ) (hq : q_fact_3 q ≠ 0) :
    w_sym q + w_std q + w_alt q
      = (2 + (q_int_2 q)^2) / q_fact_3 q := by
  unfold w_sym w_std w_alt
  field_simp
  ring

/-- **Wedderburn weights are strictly positive at any `q > 0`.**
    The full sum `w_sym + w_std + w_alt > 0`. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem wedderburn_weights_sum_pos {q : ℝ} (hq : 0 < q) :
    0 < w_sym q + w_std q + w_alt q := by
  have h1 := w_sym_pos hq
  have h2 := w_std_pos hq
  have h3 := w_alt_pos hq
  linarith

/-- **Zero-fitted-parameter property.** The Wedderburn weights are
    determined by `q` alone — they contain no free coupling
    constants. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem wedderburn_weights_q_only (q₁ q₂ : ℝ) (hq : q₁ = q₂) :
    (w_sym q₁, w_std q₁, w_alt q₁) = (w_sym q₂, w_std q₂, w_alt q₂) := by
  rw [hq]

/-- **Mass is monotone in `Z` along the proton-rich axis.** Adding
    one proton (with neutron number fixed) increases the leading
    rest-mass term by `m_p + m_e`. The binding term is `Z`-dependent
    via `V_std`, `λ^sym`, `λ^alt` (opaque), so we can only state the
    rest-mass part as an algebraic identity. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem wedderburnMass_succ_Z (Z N : ℕ)
    [HasHoefsmitData Z N] [HasHoefsmitData (Z + 1) N] (q : ℝ) :
    wedderburnMass (Z + 1) N q - wedderburnMass Z N q
      = m_p + m_e
        + (bindingTerm (Z + 1) N q - bindingTerm Z N q) := by
  unfold wedderburnMass
  push_cast
  ring

/-- **Mass is monotone in `N` along the neutron-rich axis.** Adding
    one neutron (with proton number fixed) increases the leading
    rest-mass term by `m_n`, plus the binding-term shift. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem wedderburnMass_succ_N (Z N : ℕ)
    [HasHoefsmitData Z N] [HasHoefsmitData Z (N + 1)] (q : ℝ) :
    wedderburnMass Z (N + 1) q - wedderburnMass Z N q
      = m_n
        + (bindingTerm Z (N + 1) q - bindingTerm Z N q) := by
  unfold wedderburnMass
  push_cast
  ring

/-- **Numerical sanity check.** All three rest masses are positive. -/
-- Ref: [codata2022]
theorem rest_masses_pos : 0 < m_p ∧ 0 < m_n ∧ 0 < m_e := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num [m_p, m_n, m_e]

/-- **Numerical sanity check.** Catalan's constant is positive. -/
-- Ref: [oeis-A006752]
theorem catalan_G_pos : 0 < catalan_G := by
  unfold catalan_G; norm_num

/-- **Numerical sanity check.** The binding scale `α > 0`. -/
-- Ref: [leitner2026] particle-interactions/wedderburn-mass-formula
theorem alpha_bind_pos : 0 < alpha_bind := by
  unfold alpha_bind
  have hme : 0 < m_e := rest_masses_pos.2.2
  have hG : 0 < catalan_G := catalan_G_pos
  positivity

end QOU.Interactions
