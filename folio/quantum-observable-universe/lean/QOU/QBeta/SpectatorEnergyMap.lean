import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Algebra.Module.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

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
   `log_cell_bounds`: for every `q > 1`, `2/q² < 2·e0(q)·log q < 2/q`.

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

end QOU.QBeta.SpectatorEnergyMap
