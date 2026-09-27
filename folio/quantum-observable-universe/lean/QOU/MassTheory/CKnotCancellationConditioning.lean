/-
# The `C_knot` spread is measured in an ill-conditioned coordinate

The master binding magnitude is an **alternating** sum over Wedderburn blocks,

  `S(K) = Σ_λ t_λ(K)`,   `t_λ(K) = y_λ · χ^λ(β_K) · (−1)^{n(λ)} · f^λ`,

and the reported deficit is the ratio `C_knot(K) = B_AME(K) / (m_e · |S(K)|)`.  Because the sum is
alternating, `|S|` can sit far below the scale of its own summands, and then `C_knot` inherits that
cancellation as an amplification.  The controlling quantity is the **cancellation ratio**

  `κ(K) = |S(K)| / Σ_λ |t_λ(K)| ∈ [0, 1]`.

This file proves the two facts that make `κ` the right diagnostic, for a general finite alternating
sum (no substrate input, no `q₀`, no experimental number in the general lemmas):

* `perturbed_sum_dist_le` — a per-block **relative** perturbation of sup-norm `ε` moves the sum by at
  most `ε · Σ|t_λ|`.  Combined with `Σ|t_λ| = |S| / κ`, that is a relative move of up to `ε / κ`:
  `1/κ` is exactly the condition number of `|S|` in this coordinate.
* `exists_annihilating_perturbation` — the bound is **sharp**: a perturbation of sup-norm exactly `κ`
  drives the sum to `0`, hence `C_knot` to `+∞`.  So `C_knot` is not merely imprecise when `κ` is
  small; it is undetermined, sign included.

The measured `κ` (probe `c_knot_cancellation_conditioning_probe.py`, convention D, experimental proton
pin, 0-fit, exact mpmath) is `0.2911 (D) / 0.4137 (T) / 0.2944 (³He) / 0.0079548 (⁴He)`.  The concrete
lemmas below record the two consequences that matter:

* `he4_cancellation_below_one_percent` — `κ(⁴He) < 1/100`, so the reported `C_knot(⁴He) = 290.007` is
  the `1/κ ≈ 126×` amplification of a sub-percent cancellation, not `290×` of missing physics.  It is
  what dominates the headline cross-isotope spread `59.12×`.
* `mirror_pair_well_conditioned` — `κ(T) > 1/4` and `κ(³He) > 1/4`.  This is the **defensive** half:
  the T/³He mirror-pair exclusion `CKnotNonUniversal.no_level_only_closure` is stated at a pair of
  well-conditioned points, so nothing in this file weakens it.

## Scope (STRICT)

This is **scope-(a)** — a correction to the *interpretation* of the reported spread, resting on the
triangle inequality plus the measured `κ`.  It asserts **no** structural exclusion, proposes **no**
ansatz for the magnitude (per AGENTS.md there is no seventh per-block-weight ansatz here, and none is
implied — `κ` is a diagnostic of the *existing* formula), and closes nothing.  In particular it does
**not** show `C_knot` is universal; it is not.  The Δ_λ **magnitude** remains OPEN (bean `qou-3q7t`).

`B_AME` enters only through the diagnostic ratios, never inverted into a canonical weight (owner
directive: "Δ_λ from inverted CODATA = NOT ALLOWED").  `free_parameters = 0`; nothing wired.

Companion: `QOU/MassTheory/CKnotNonUniversal.lean`; probe
`computations/deltalambda/c_knot_cancellation_conditioning_probe.py`; PR #5406.
-/
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.MassTheory.CKnotCancellationConditioning

open Finset

variable {ι : Type*}

/-- **Conditioning bound for a relative per-block perturbation.**  If every block term `t i` is
perturbed multiplicatively, `t i ↦ t i · (1 + δ i)`, with sup-norm `‖δ‖_∞ ≤ ε`, then the total moves
by at most `ε · Σ|t i|`.

Dividing by `|Σ t i|` and writing `κ = |Σ t i| / Σ|t i|`, the *relative* move of the total is bounded
by `ε / κ`.  That is the precise sense in which `1/κ` is the condition number of the master binding
magnitude: for `⁴He`, `κ ≈ 0.008`, so a sub-percent per-block correction is amplified into an
order-one change in `|S|` and hence in `C_knot`. -/
theorem perturbed_sum_dist_le (s : Finset ι) (t δ : ι → ℝ) (ε : ℝ)
    (hδ : ∀ i ∈ s, |δ i| ≤ ε) :
    |∑ i ∈ s, t i * (1 + δ i) - ∑ i ∈ s, t i| ≤ ε * ∑ i ∈ s, |t i| := by
  have hrw : (∑ i ∈ s, t i * (1 + δ i)) - ∑ i ∈ s, t i = ∑ i ∈ s, t i * δ i := by
    rw [← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  rw [hrw, mul_sum]
  refine (Finset.abs_sum_le_sum_abs _ _).trans (Finset.sum_le_sum fun i hi => ?_)
  calc |t i * δ i| = |t i| * |δ i| := abs_mul _ _
    _ ≤ |t i| * ε := mul_le_mul_of_nonneg_left (hδ i hi) (abs_nonneg _)
    _ = ε * |t i| := mul_comm _ _

/-- **The conditioning bound is sharp: a perturbation of sup-norm exactly `κ` annihilates the sum.**

Take `δ i = -(S / T) · sign(t i)` with `S = Σ t i`, `T = Σ|t i|`.  Then `t i · δ i = -(S/T)·|t i|`, so
the perturbed total is `S - (S/T)·T = 0`, while `‖δ‖_∞ = |S|/T = κ`.

Consequence for the deficit ratio: when `κ` is small, `C_knot = B/(m_e·|S|)` is not merely
imprecise — a per-block relative correction of size `κ` sends `|S|` to `0` and `C_knot` to `+∞`, and
corrections slightly larger flip the sign of `S`.  So `C_knot(⁴He) = 290.007`, sitting at
`κ < 1/100`, carries essentially no information about the size of the missing per-block structure. -/
theorem exists_annihilating_perturbation (s : Finset ι) (t : ι → ℝ)
    (hT : 0 < ∑ i ∈ s, |t i|) :
    ∃ δ : ι → ℝ,
      (∀ i ∈ s, |δ i| ≤ |∑ i ∈ s, t i| / ∑ i ∈ s, |t i|) ∧
      ∑ i ∈ s, t i * (1 + δ i) = 0 := by
  set S : ℝ := ∑ i ∈ s, t i with hS
  set T : ℝ := ∑ i ∈ s, |t i| with hTdef
  refine ⟨fun i => -(S / T) * (if 0 ≤ t i then 1 else -1), fun i _ => ?_, ?_⟩
  · have h1 : |(if 0 ≤ t i then (1 : ℝ) else -1)| = 1 := by
      split_ifs <;> simp
    rw [abs_mul, h1, mul_one, abs_neg, abs_div, abs_of_pos hT]
  · have hkey : ∀ i ∈ s, t i * (1 + -(S / T) * (if 0 ≤ t i then (1 : ℝ) else -1))
        = t i - (S / T) * |t i| := by
      intro i _
      by_cases h : 0 ≤ t i
      · rw [if_pos h, abs_of_nonneg h]; ring
      · rw [if_neg h, abs_of_neg (lt_of_not_ge h)]; ring
    rw [Finset.sum_congr rfl hkey, Finset.sum_sub_distrib, ← mul_sum, ← hS, ← hTdef,
      div_mul_cancel₀ _ (ne_of_gt hT), sub_self]

/-! ### The measured cancellation ratios

Values from `c-knot-cancellation-conditioning.witness.json` (convention D, experimental proton pin,
`q₀ = 1.1099785827513808…`, exact mpmath at 50 dps, `free_parameters = 0`).  `S` here is the signed
master sum's magnitude and `T = Σ_λ |t_λ|` its absolute-term total; both are substrate-derived, with
no experimental input. -/

/-- `|S(⁴He)|` — magnitude of the master binding sum at `H₁₂` (77 partitions). -/
def absS_He4 : ℝ := 0.19093767

/-- `T(⁴He) = Σ_λ |t_λ|` — the absolute-term total at `H₁₂`. -/
def T_He4 : ℝ := 24.002872

/-- `|S(T)|` — magnitude of the master binding sum for the triton at `H₉`. -/
def absS_T : ℝ := 2.4751404

/-- `T(T) = Σ_λ |t_λ|` for the triton at `H₉`. -/
def T_T : ℝ := 5.9822922

/-- `|S(³He)|` — magnitude of the master binding sum for the helion at `H₉`. -/
def absS_He3 : ℝ := 3.0789913

/-- `T(³He) = Σ_λ |t_λ|` for the helion at `H₉`. -/
def T_He3 : ℝ := 10.459258

/-- **`⁴He` sits on a sub-percent cancellation:** `κ(⁴He) = |S| / Σ|t_λ| < 1/100`.

By `exists_annihilating_perturbation`, a per-block relative correction of sup-norm under `1%` sends
`S(⁴He)` to zero and `C_knot(⁴He)` to `+∞`.  The reported `C_knot(⁴He) = 290.007` — which is what
produces the headline cross-isotope spread `59.12×` — is therefore an amplified cancellation, not a
measurement of `290×` of missing physics. -/
theorem he4_cancellation_below_one_percent : absS_He4 / T_He4 < 1 / 100 := by
  unfold absS_He4 T_He4; norm_num

/-- **The mirror pair is well conditioned** — `κ(T) > 1/4` and `κ(³He) > 1/4`.

This is the defensive half of the conditioning analysis.  `CKnotNonUniversal.no_level_only_closure`
excludes the level-only rescale class using the `(B, S)` pairs of the triton and helion; both sit at
`κ` above a quarter, i.e. within a factor `4` of a perfectly conditioned sum.  So that scope-(b)
exclusion is **not** touched by anything proved here — the ill-conditioning is localised on `⁴He`. -/
theorem mirror_pair_well_conditioned :
    1 / 4 < absS_T / T_T ∧ 1 / 4 < absS_He3 / T_He3 := by
  constructor
  · unfold absS_T T_T; norm_num
  · unfold absS_He3 T_He3; norm_num

/-- **The ⁴He cancellation is two orders of magnitude sharper than the mirror pair's.**  `κ(T)` and
`κ(³He)` exceed `κ(⁴He)` by more than `25×`, so the four isotopes do not share a conditioning regime:
any statement that reads the cross-isotope `C_knot` spread as a uniform measurement of per-knot
variation is comparing one ill-conditioned point against three well-conditioned ones. -/
theorem he4_conditioning_regime_differs :
    25 * (absS_He4 / T_He4) < absS_T / T_T ∧ 25 * (absS_He4 / T_He4) < absS_He3 / T_He3 := by
  constructor
  · unfold absS_He4 T_He4 absS_T T_T; norm_num
  · unfold absS_He4 T_He4 absS_He3 T_He3; norm_num

end QOU.MassTheory.CKnotCancellationConditioning
