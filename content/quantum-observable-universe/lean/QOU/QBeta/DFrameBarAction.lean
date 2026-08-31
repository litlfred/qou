/-
# The bar action on the Q_β traced volume: affine under C, multiplicative under D

Formalises bean `qou-cds1` Steps 6-8 (PRs #6149, #6172), established symbolically in
`computations/qbeta/qbeta_d_frame_bridge_generic_z.py` and
`computations/qbeta/qbeta_d_frame_bar_action_on_traced_volume.py`.

The content: the Q_β bridge phase `α = (z-1)h/2` is a re-centring of the Markov
traced volume `V̂ = z·h + 1`, and the bar involution `q ↦ q⁻¹` acts on `V̂` as an
**affine reflection** in convention C but as a **multiplicative scaling** in
convention D. That difference — not any change in the phase formula — is why the
cos-resummation of `prop:q-beta-cos-resummation` is convention-C-specific: its
stated justification is that bar sends `α ↦ -α`, which holds under C and fails
under D.

Everything is algebraic: stated over a generic `Field K` per AGENTS.md §7c, with
no `ℝ` and no `Real.sqrt`. Convention C is carried in the square-root variable
`u` (so `q = u^2`), which keeps it in the same generic setting.

The hypotheses are genuine, not bookkeeping. `q ≠ 0` and `q^2 + 1 ≠ 0` are both
needed — over a field where `-1` is a square (`ℂ` at `q = i`) the denominators
vanish — and `CharZero` is needed because the phase divides by `2`.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.CharZero.Defs

namespace QOU.QBeta.DFrame

variable {K : Type*} [Field K]

/-- `h = q - q⁻¹`, the substrate difference. Convention-free. -/
def hq (q : K) : K := q - q⁻¹

/-- The convention-D Markov parameter `z_D = q³/(q²+1)` (owner ruling 2026-08-15 R1). -/
noncomputable def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- The convention-C Markov parameter in the square-root variable `u`, where
`q = u^2`: `z_C = √q/(q+1) = u/(u²+1)`. Carried in `u` so the statement stays
algebraic — no `Real.sqrt`, no `ℝ`. -/
noncomputable def zC (u : K) : K := u / (u ^ 2 + 1)

/-- `h` in the square-root variable: `h = q - q⁻¹ = u² - (u²)⁻¹`. -/
def hu (u : K) : K := u ^ 2 - (u ^ 2)⁻¹

/-- The Markov traced volume of the pp transfer matrix, `V̂ = z·h + 1`
(`beta-decay-transfer-matrix-proof.md`: `V̂ = z·M₁₁ + M₂₁` with `T_pp = [[h,1],[1,0]]`).
Carried with `z` FREE — a convention enters only when `z` is instantiated. -/
def tracedVolume (z h : K) : K := z * h + 1

/-- The Q_β bridge phase `α = (z-1)h/2`, again with `z` free. -/
def bridgePhase (z h : K) : K := (z - 1) * h / 2

/-- Helper: `q ≠ 0` and `q² + 1 ≠ 0` give `(q⁻¹)² + 1 ≠ 0`, since
`(q⁻¹)² + 1 = (q² + 1)/q²`. -/
theorem comm_ne_zero {q : K} (h2 : q ^ 2 + 1 ≠ 0) : (1 : K) + q ^ 2 ≠ 0 := by
  rwa [add_comm] at h2

/-- `2 ≠ 0` in a characteristic-zero field. Needed because the bridge phase and
the invariant's closed form both divide by `2`; in characteristic 2 neither is
even well posed. -/
theorem two_ne_zero_cz [CharZero K] : (2 : K) ≠ 0 := by
  norm_num

theorem inv_sq_add_one_ne_zero {q : K} (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (q⁻¹) ^ 2 + 1 ≠ 0 := by
  have hrw : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by
    field_simp; ring
  rw [hrw]
  exact div_ne_zero h2 (pow_ne_zero 2 hq0)

/-! ## Step 6 — the phase is a re-centred traced volume, generically in `z` -/

/-- `α = (V̂ - 1 - h)/2`. A ring identity holding for EVERY `z`: the phase is the
traced volume re-centred on `1` and shifted by `h`. No hypothesis on `z` is used,
which is exactly why the phase FORMULA is convention-independent. -/
theorem bridgePhase_eq_recentred_tracedVolume (z h : K) :
    bridgePhase z h = (tracedVolume z h - 1 - h) / 2 := by
  unfold bridgePhase tracedVolume; ring

/-! ## The bar involution `q ↦ q⁻¹` on the pieces -/

/-- `h` is bar-ODD: `h(q⁻¹) = -h(q)`. -/
theorem hq_bar (q : K) : hq q⁻¹ = - hq q := by
  unfold hq
  rcases eq_or_ne q 0 with rfl | hq0
  · simp
  · field_simp
    ring

/-- `z_D` is a bar-EIGENVECTOR of weight `-4`: `z_D(q⁻¹) = z_D(q)/q⁴`. -/
theorem zD_bar (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    zD q⁻¹ = zD q / q ^ 4 := by
  have h2' := inv_sq_add_one_ne_zero hq0 h2
  have hc := comm_ne_zero h2
  have hc' := comm_ne_zero h2'
  unfold zD
  rw [div_div, div_eq_div_iff h2' (mul_ne_zero h2 (pow_ne_zero 4 hq0))]
  field_simp
  ring

/-! ## Step 7 — the two conventions give two DIFFERENT group actions -/

/-- Convention D, closed form: `V̂_D = (q⁴+1)/(q²+1)`. -/
theorem tracedVolume_D (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    tracedVolume (zD q) (hq q) = (q ^ 4 + 1) / (q ^ 2 + 1) := by
  have hc := comm_ne_zero h2
  unfold tracedVolume zD hq
  field_simp
  ring

/-- **Convention D: the bar action is MULTIPLICATIVE**, a weight `-2` eigenvector:
`V̂(q⁻¹) = V̂(q)/q²`. Bar SCALES the traced volume; it has no fixed point. -/
theorem tracedVolume_D_bar (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    tracedVolume (zD q⁻¹) (hq q⁻¹) = tracedVolume (zD q) (hq q) / q ^ 2 := by
  have h2' := inv_sq_add_one_ne_zero hq0 h2
  have hc := comm_ne_zero h2
  have hc' := comm_ne_zero h2'
  rw [tracedVolume_D q hq0 h2, tracedVolume_D q⁻¹ (inv_ne_zero hq0) h2']
  rw [div_div, div_eq_div_iff h2' (mul_ne_zero h2 (pow_ne_zero 2 hq0))]
  field_simp
  ring

/-- **Convention C: the bar action is an AFFINE REFLECTION** with fixed point `1`:
`V̂(u⁻¹) = 2 - V̂(u)`. Contrast `tracedVolume_D_bar` — the same object, a different
group action. That contrast is the whole content of Step 7. -/
theorem tracedVolume_C_bar (u : K) (hu0 : u ≠ 0) (h2 : u ^ 2 + 1 ≠ 0) :
    tracedVolume (zC u⁻¹) (hu u⁻¹) = 2 - tracedVolume (zC u) (hu u) := by
  have h2' := inv_sq_add_one_ne_zero hu0 h2
  have hc := comm_ne_zero h2
  have hc' := comm_ne_zero h2'
  unfold tracedVolume zC hu
  field_simp
  ring

/-! ## Step 8 — what each action's INVARIANT is -/

/-- **The convention-D bar-invariant is `V̂/q`** — the unique `q`-power rescaling
fixed by bar, since the action carries weight `-2`. -/
theorem tracedVolume_D_invariant (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    tracedVolume (zD q⁻¹) (hq q⁻¹) / q⁻¹ = tracedVolume (zD q) (hq q) / q := by
  rw [tracedVolume_D_bar q hq0 h2]
  field_simp

/-- Closed form for the D invariant:
`V̂_D/q = ([2]_q + h²·z_D/q²)/2`, with `[2]_q = q + q⁻¹` the quantum integer.
It is manifestly **not constant in `q`** — the content of Step 8: under D there
is no fixed centre for a resummation to be built around. -/
theorem tracedVolume_D_invariant_closed_form [CharZero K] (q : K) (hq0 : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) :
    tracedVolume (zD q) (hq q) / q
      = ((q + q⁻¹) + (hq q) ^ 2 * zD q / q ^ 2) / 2 := by
  have hc := comm_ne_zero h2
  have h2K := two_ne_zero_cz (K := K)
  rw [tracedVolume_D q hq0 h2]
  unfold hq zD
  field_simp
  ring

/-! ## The consequence for the resummation -/

/-- **Convention C: the phase is bar-ODD**, `α(u⁻¹) + α(u) = 0`. This is precisely
the hypothesis `prop:q-beta-cos-resummation` states as its justification — "the bar
involution maps `α ↦ -α`, so the resummation must be even in `α`". -/
theorem bridgePhase_C_bar_odd (u : K) (hu0 : u ≠ 0) (h2 : u ^ 2 + 1 ≠ 0) :
    bridgePhase (zC u⁻¹) (hu u⁻¹) + bridgePhase (zC u) (hu u) = 0 := by
  have h2' := inv_sq_add_one_ne_zero hu0 h2
  have hc := comm_ne_zero h2
  have hc' := comm_ne_zero h2'
  unfold bridgePhase zC hu
  field_simp
  ring

/-- **Convention D: the phase is NOT bar-odd.** The defect is exactly
`(q-1)²(q+1)²/(2q²)`. -/
theorem bridgePhase_D_bar_defect [CharZero K] (q : K) (hq0 : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) :
    bridgePhase (zD q⁻¹) (hq q⁻¹) + bridgePhase (zD q) (hq q)
      = (q - 1) ^ 2 * (q + 1) ^ 2 / (2 * q ^ 2) := by
  have h2' := inv_sq_add_one_ne_zero hq0 h2
  have hc := comm_ne_zero h2
  have hc' := comm_ne_zero h2'
  unfold bridgePhase zD hq
  field_simp
  ring

/-- The defect vanishes only at `q = ±1`, never on the substrate where `q > 1`.
So the bar-oddness convention C enjoys is genuinely **unavailable** under D — not
merely unproved — and the cos-resummation's stated justification fails with it. -/
theorem bridgePhase_D_not_bar_odd [CharZero K] (q : K) (hq0 : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) (h1 : q - 1 ≠ 0) (h1' : q + 1 ≠ 0) :
    bridgePhase (zD q⁻¹) (hq q⁻¹) + bridgePhase (zD q) (hq q) ≠ 0 := by
  rw [bridgePhase_D_bar_defect q hq0 h2]
  exact div_ne_zero (mul_ne_zero (pow_ne_zero 2 h1) (pow_ne_zero 2 h1'))
    (mul_ne_zero (two_ne_zero_cz (K := K)) (pow_ne_zero 2 hq0))

end QOU.QBeta.DFrame
