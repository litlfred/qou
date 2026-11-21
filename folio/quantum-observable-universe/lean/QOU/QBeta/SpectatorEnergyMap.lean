import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Algebra.Module.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# The ε → energy map from spectator invariance

Thread "Derive the n–p cell's E0 and ε→MeV map", 2026-11-21. Pre-registration:
`computations/probes/qbeta_energy_map/PREREGISTRATION.md`. Audit:
`docs/audits/2026-11-21-qbeta-energy-map-spectator.md`.

## The premise

**Spectator invariance (S).** An energy *difference* is unchanged when both states are multiplied
by one common positive factor: `Φ(λx) − Φ(λy) = Φ(x) − Φ(y)` for `λ, x, y > 0`. In the corpus a
common factor arises from the shared lepton factor (owner ruling 2026-11-21, "not one-sided
yet"), from an idle strand, and from the choice of global normalisation `[2]³`.

## What is proved

1. `log_spectatorInvariant`: every `c·log + d` satisfies S.
2. `eq_log_of_spectatorInvariant`: **S plus continuity on `(0, ∞)` forces `Φ = c·log + d`.**
   (Cauchy's equation for `t ↦ Φ(eᵗ) − Φ(1)`.)
3. `linear_not_spectatorInvariant`: the linear map `x ↦ c·x`, `c ≠ 0`, fails S.
4. `log_cell`: with the two weight-space traces equal to one value `t > 0` (the content of
   `NucleonWeightSpaceTraces.trace_word_eq`), K-weights `q^{±1}` and any normalisation `D > 0`,
   the log map gives `Φ(ε_n) − Φ(ε_p) = −2c·log q`. The word, its trace and `D` drop out.
   `log_cell_pos_iff`: the neutron side is the higher one iff `c < 0` (for `q > 1`).
5. `shared_factor_cancels` / `linear_shared_factor`: a common factor `f` leaves an S-map's cell
   unchanged and multiplies the linear cell by `f`.
6. E₀ (in units of `m_e`, `e0 q = 1/(q(q−1))`): `tower_ratio` (`E₀^full/E₀ = q²/(2q−1)`) and
   `log_cell_bounds`: for every `q > 1`, `2/q² < 2·e0(q)·log q < 2/q`;
   `log_cell_tower_lt_two`: with the tower-summed `E₀`, the log cell is `< 2·m_e` for every
   `q > 1`.

## What is NOT claimed

* That S is true. It is a premise, stated in the pre-registration.
* Any scale. S fixes the *form* of the map, never `c`. Which multiple of `E₀` is `|c|` is open.
* Which reading (`Q_β` or `m_n − m_p`) the cell is. No measured value appears in this file.
-/

namespace QOU.QBeta.SpectatorEnergyMap

open Real

/-- **Spectator invariance** of a map `Φ` from (positive) trace values to energies. -/
def SpectatorInvariant (Φ : ℝ → ℝ) : Prop :=
  ∀ l x y : ℝ, 0 < l → 0 < x → 0 < y → Φ (l * x) - Φ (l * y) = Φ x - Φ y

/-- Every logarithmic map is spectator invariant. -/
theorem log_spectatorInvariant (c d : ℝ) :
    SpectatorInvariant (fun x => c * Real.log x + d) := by
  intro l x y hl hx hy
  simp only
  rw [Real.log_mul hl.ne' hx.ne', Real.log_mul hl.ne' hy.ne']
  ring

/-- **Spectator invariance plus continuity forces the logarithm.** -/
theorem eq_log_of_spectatorInvariant (Φ : ℝ → ℝ) (hS : SpectatorInvariant Φ)
    (hc : ContinuousOn Φ (Set.Ioi 0)) :
    ∃ c d : ℝ, ∀ x : ℝ, 0 < x → Φ x = c * Real.log x + d := by
  -- `g t = Φ(eᵗ) − Φ 1` is additive and continuous.
  let g : ℝ →+ ℝ :=
    { toFun := fun t => Φ (Real.exp t) - Φ 1
      map_zero' := by simp
      map_add' := by
        intro s t
        have h := hS (Real.exp s) (Real.exp t) 1 (Real.exp_pos s) (Real.exp_pos t) one_pos
        rw [mul_one] at h
        simp only [Real.exp_add]
        linarith }
  have hg : Continuous g := by
    show Continuous fun t => Φ (Real.exp t) - Φ 1
    refine Continuous.sub ?_ continuous_const
    exact hc.comp_continuous Real.continuous_exp (fun t => Real.exp_pos t)
  let L := g.toRealLinearMap hg
  refine ⟨g 1, Φ 1, fun x hx => ?_⟩
  have hL : g (Real.log x) = Real.log x * g 1 := by
    have := L.map_smul (Real.log x) (1 : ℝ)
    simpa [L, smul_eq_mul] using this
  have hgx : g (Real.log x) = Φ x - Φ 1 := by
    show Φ (Real.exp (Real.log x)) - Φ 1 = Φ x - Φ 1
    rw [Real.exp_log hx]
  linarith [hL, hgx]

/-- The corpus's linear map `x ↦ c·x` is not spectator invariant unless `c = 0`. -/
theorem linear_not_spectatorInvariant (c : ℝ) (hc : c ≠ 0) :
    ¬ SpectatorInvariant (fun x => c * x) := by
  intro hS
  have h := hS 2 1 2 (by norm_num) one_pos (by norm_num)
  simp only at h
  apply hc
  linarith

/-! ## The ruled cell under a logarithmic map -/

/-- Proton component: `K`-weight `q`, common trace `t`, global normalisation `D`. -/
noncomputable def epsP (q t D : ℝ) : ℝ := q * t / D

/-- Neutron component: `K`-weight `q⁻¹`, the same trace `t` (`trace_word_eq`), the same `D`. -/
noncomputable def epsN (q t D : ℝ) : ℝ := q⁻¹ * t / D

theorem epsN_eq (q t D : ℝ) (hq : 0 < q) : epsN q t D = epsP q t D / q ^ 2 := by
  unfold epsN epsP
  field_simp

/-- **The log cell is `−2c·log q`, for every word, trace and normalisation.** -/
theorem log_cell (c d q t D : ℝ) (hq : 0 < q) (ht : 0 < t) (hD : 0 < D) :
    (c * Real.log (epsN q t D) + d) - (c * Real.log (epsP q t D) + d)
      = -2 * c * Real.log q := by
  have hP : 0 < epsP q t D := by unfold epsP; positivity
  rw [epsN_eq q t D hq, Real.log_div hP.ne' (by positivity), Real.log_pow]
  push_cast
  ring

/-- **Sign.** For `q > 1` the neutron side of the log cell is the higher one iff `c < 0`, i.e.
iff the map is decreasing (the free-energy form `−|c|·log`). -/
theorem log_cell_pos_iff (c d q t D : ℝ) (hq : 1 < q) (ht : 0 < t) (hD : 0 < D) :
    0 < (c * Real.log (epsN q t D) + d) - (c * Real.log (epsP q t D) + d) ↔ c < 0 := by
  rw [log_cell c d q t D (by linarith) ht hD]
  have hl : 0 < Real.log q := Real.log_pos hq
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    nlinarith
  · intro hc
    nlinarith

/-- A common factor leaves every spectator-invariant cell unchanged. -/
theorem shared_factor_cancels (Φ : ℝ → ℝ) (hS : SpectatorInvariant Φ) (f x y : ℝ)
    (hf : 0 < f) (hx : 0 < x) (hy : 0 < y) :
    Φ (f * x) - Φ (f * y) = Φ x - Φ y :=
  hS f x y hf hx hy

/-- Under the linear map a common factor rescales the cell by that factor. -/
theorem linear_shared_factor (c f x y : ℝ) :
    c * (f * x) - c * (f * y) = f * (c * x - c * y) := by
  ring

/-! ## The base `E₀`, in units of `m_e` -/

/-- `E₀ / m_e = 1/(q(q−1))` (`energy-scale-planck`). -/
noncomputable def e0 (q : ℝ) : ℝ := 1 / (q * (q - 1))

/-- `E₀^full / m_e = E₀/m_e / (1 − ℏ_q²)`, `ℏ_q = 1 − q⁻¹` (`qbeta_e0.tower_summed`). -/
noncomputable def e0Tower (q : ℝ) : ℝ := e0 q / (1 - (1 - q⁻¹) ^ 2)

/-- **The tower factor is `q²/(2q − 1)`.** -/
theorem tower_ratio (q : ℝ) (hq : 1 < q) : e0Tower q = e0 q * (q ^ 2 / (2 * q - 1)) := by
  unfold e0Tower
  have h1 : (2 * q - 1) ≠ 0 := by linarith
  have h0 : q ≠ 0 := by linarith
  have hT : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by field_simp; ring
  rw [hT]
  field_simp

/-- **Bounds on the log cell with `|c| = E₀`:** for every `q > 1`,
`2/q² < 2·(E₀/m_e)·log q < 2/q`. So the cell tends to `2·m_e` as `q → 1` and stays below it. -/
theorem log_cell_bounds (q : ℝ) (hq : 1 < q) :
    2 / q ^ 2 < 2 * e0 q * Real.log q ∧ 2 * e0 q * Real.log q < 2 / q := by
  have hq0 : 0 < q := by linarith
  have hq1 : 0 < q - 1 := by linarith
  have hup : Real.log q < q - 1 := by
    have := Real.log_lt_sub_one_of_pos hq0 (ne_of_gt hq)
    linarith
  have hlo : 1 - q⁻¹ < Real.log q := by
    have h := Real.log_lt_sub_one_of_pos (inv_pos.mpr hq0) (by
      intro h; have : q = 1 := by
        have := congrArg (·⁻¹) h; simpa using this
      linarith)
    rw [Real.log_inv] at h
    linarith
  have he : 2 * e0 q * Real.log q = 2 * Real.log q / (q * (q - 1)) := by
    unfold e0; ring
  have hden : 0 < q * (q - 1) := by positivity
  rw [he]
  constructor
  · rw [lt_div_iff₀ hden]
    have : 1 - q⁻¹ = (q - 1) / q := by field_simp
    rw [this] at hlo
    have h2 : 2 / q ^ 2 * (q * (q - 1)) = 2 * ((q - 1) / q) := by field_simp; ring
    rw [h2]
    linarith
  · rw [div_lt_iff₀ hden]
    have h2 : 2 / q * (q * (q - 1)) = 2 * (q - 1) := by field_simp
    rw [h2]
    linarith

/-- **With the tower-summed `E₀` the log cell stays below `2·m_e` for every `q > 1`.**
`2·(E₀^full/m_e)·log q < 2q/(2q−1) ≤ 2`. -/
theorem log_cell_tower_lt_two (q : ℝ) (hq : 1 < q) : 2 * e0Tower q * Real.log q < 2 := by
  have hb := (log_cell_bounds q hq).2
  have hq0 : 0 < q := by linarith
  have h21 : 0 < 2 * q - 1 := by linarith
  have hr : 0 < q ^ 2 / (2 * q - 1) := by positivity
  rw [tower_ratio q hq]
  have e : 2 * (e0 q * (q ^ 2 / (2 * q - 1))) * Real.log q
      = (2 * e0 q * Real.log q) * (q ^ 2 / (2 * q - 1)) := by ring
  rw [e]
  calc (2 * e0 q * Real.log q) * (q ^ 2 / (2 * q - 1))
      < 2 / q * (q ^ 2 / (2 * q - 1)) := mul_lt_mul_of_pos_right hb hr
    _ = 2 * q / (2 * q - 1) := by field_simp; ring
    _ ≤ 2 := by rw [div_le_iff₀ h21]; linarith

/-! ## The scale as a temperature (pre-registration addendum 1)

Route T: `def:quantum-temperature` gives `k_B T_q = ℏ_q = (q−1)/q` in natural units, and
`def:information-speed-of-light` converts mass to energy with `c_q² = 1/(q−1)²`. With the CAL-1
mass unit `m_e`, `k_B T_q` in units of `m_e` is `c_q²·ℏ_q`. Route D: the `β = ln q` dictionary
(`QBetaEnergyDictionary.energyOf`) reads energies as `−ln y / ln q`. -/

/-- **Route T: the thermal energy `m_e·c_q²·ℏ_q` is exactly `E₀`.** -/
theorem kT_eq_e0 (q : ℝ) (hq : 1 < q) : (1 / (q - 1)) ^ 2 * ((q - 1) / q) = e0 q := by
  unfold e0
  have h1 : q - 1 ≠ 0 := by linarith
  have h0 : q ≠ 0 := by linarith
  field_simp

/-- **Route T cell.** The free-energy map `E = −k_B T_q·log ε` gives `2·(E₀/m_e)·log q`. -/
theorem routeT_cell (q t D : ℝ) (hq : 1 < q) (ht : 0 < t) (hD : 0 < D) :
    (-(e0 q) * Real.log (epsN q t D)) - (-(e0 q) * Real.log (epsP q t D))
      = 2 * e0 q * Real.log q := by
  have := log_cell (-(e0 q)) 0 q t D (by linarith) ht hD
  simp only [add_zero] at this
  rw [this]; ring

/-- **Route D cell.** In the `β = ln q` dictionary's units the cell is exactly `2`. -/
theorem routeD_cell (q t D : ℝ) (hq : 1 < q) (ht : 0 < t) (hD : 0 < D) :
    (-Real.log (epsN q t D) / Real.log q) - (-Real.log (epsP q t D) / Real.log q) = 2 := by
  have hl : Real.log q ≠ 0 := (Real.log_pos hq).ne'
  have := log_cell (-1) 0 q t D (by linarith) ht hD
  simp only [add_zero, neg_one_mul] at this
  rw [← sub_div, this]
  field_simp
  ring

/-- **The two corpus temperatures disagree.** For `1 < q < 2` the dictionary's inverse temperature
`ln q` is strictly below `def:quantum-temperature`'s `β_q = 1/ℏ_q = q/(q−1)`. -/
theorem dictionary_beta_lt_quantum_beta (q : ℝ) (hq : 1 < q) (hq2 : q < 2) :
    Real.log q < q / (q - 1) := by
  have hq0 : 0 < q := by linarith
  have h1 : Real.log q < q - 1 := by
    have := Real.log_lt_sub_one_of_pos hq0 (ne_of_gt hq); linarith
  have h2 : 1 < q / (q - 1) := by
    rw [lt_div_iff₀ (by linarith)]; linarith
  linarith

/-! ## Reconciling the two temperatures (pre-registration addendum 2)

Both corpus readings use the same Boltzmann weight `y`. Equal weights fix only the product
`β·E`, so two inverse temperatures describe one Gibbs state in two energy units. -/

/-- **One weight, two units.** `e^{−β₁E₁} = e^{−β₂E₂}` iff `E₂ = (β₁/β₂)·E₁`. -/
theorem same_weight_iff (β₁ β₂ E₁ E₂ : ℝ) (h₂ : β₂ ≠ 0) :
    Real.exp (-β₁ * E₁) = Real.exp (-β₂ * E₂) ↔ E₂ = β₁ / β₂ * E₁ := by
  rw [Real.exp_eq_exp]
  constructor
  · intro h
    field_simp
    linarith
  · intro h
    rw [h]
    field_simp

/-- **The dictionary's energy unit in units of `m_e`.** With `β_D = ln q` and `β_q = 1/ℏ_q`, one
dictionary unit is `(β_D/β_q)` natural units, i.e. `ℏ_q·ln q·c_q² = (E₀/m_e)·ln q`. -/
theorem dictionary_unit (q : ℝ) (hq : 1 < q) :
    Real.log q / (1 / ((q - 1) / q)) * (1 / (q - 1)) ^ 2 = e0 q * Real.log q := by
  unfold e0
  have h1 : q - 1 ≠ 0 := by linarith
  have h0 : q ≠ 0 := by linarith
  field_simp

/-- **Reconciled: route D, converted to the natural unit, is route T.** -/
theorem routeD_converted_eq_routeT (q : ℝ) (hq : 1 < q) :
    2 * (Real.log q / (1 / ((q - 1) / q)) * (1 / (q - 1)) ^ 2) = 2 * e0 q * Real.log q := by
  rw [dictionary_unit q hq]
  ring

/-! ## S is not an extra axiom (owner: "should follow from QOU, no hidden symmetry axioms")

S follows from two things the corpus already has:
* **the trace is multiplicative on disjoint strand sets** (`markov-axioms-primitive`, derived
  there from the Markov axioms): for the convention-D quantum trace this is `trace_kron` below,
  since `K^{⊗(n+m)} = K^{⊗n} ⊗ K^{⊗m}` (K is grouplike) and `[2]^{n+m} = [2]^n·[2]^m`;
* **energy is additive over non-interacting parts.** In the corpus's own energy reading of the
  trace (`prop:beta-eq-ln-q-dictionary`, `E = −ln y / β`) this holds outright; and in general it
  is the statement that the energy generator `H = log_q K` is primitive because `K` is grouplike.

`spectator_of_additive`: an energy map additive over products is spectator invariant. So S is a
consequence, and together with continuity it is equivalent to additivity
(`eq_log_of_spectatorInvariant`). The one assumption left is that a continuous ε → energy map
exists at all, which is the question being asked. -/

/-- **Multiplicativity of the weighted trace on a disjoint (tensor) pair.**
`Tr((K₁ ⊗ K₂)(x ⊗ y)) = Tr(K₁ x)·Tr(K₂ y)`. -/
theorem trace_kron {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    (K₁ x : Matrix m m ℝ) (K₂ y : Matrix n n ℝ) :
    Matrix.trace (Matrix.kroneckerMap (· * ·) K₁ K₂ * Matrix.kroneckerMap (· * ·) x y)
      = Matrix.trace (K₁ * x) * Matrix.trace (K₂ * y) := by
  rw [← Matrix.mul_kronecker_mul, Matrix.trace_kronecker]

/-- **Additive energy ⇒ spectator invariance.** If `Φ(ab) = Φ(a) + Φ(b)` for positive trace values
(energy of non-interacting parts adds; trace multiplies), then `Φ` satisfies S. -/
theorem spectator_of_additive (Φ : ℝ → ℝ)
    (hA : ∀ a b : ℝ, 0 < a → 0 < b → Φ (a * b) = Φ a + Φ b) : SpectatorInvariant Φ := by
  intro l x y hl hx hy
  rw [hA l x hl hx, hA l y hl hy]
  ring

/-- **The grouplike weight has an additive exponent.** On a tensor pair of `K`-eigenvectors with
weights `q^i`, `q^j`, the weight is `q^(i+j)`: `log_q` of a grouplike element is primitive. -/
theorem grouplike_weight (q : ℝ) (hq : 0 < q) (i j : ℤ) :
    Real.log (q ^ i * q ^ j) = (i + j) * Real.log q := by
  rw [Real.log_mul (zpow_pos hq i).ne' (zpow_pos hq j).ne', Real.log_zpow, Real.log_zpow]
  ring

end QOU.QBeta.SpectatorEnergyMap
