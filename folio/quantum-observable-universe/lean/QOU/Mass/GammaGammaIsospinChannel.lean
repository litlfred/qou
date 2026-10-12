import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Module
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The γγ bond combined with the isospin projectors

Owner ask (2026-10-11, "try 1"): combine the γγ-selected interface bond `G` (bean
`qou-ales`, `G = (σ₂σ₃⁻¹)³` on `H₆`) with the isospin projectors
`P₊ = s•(σ + q⁻¹)`, `P₋ = s•(q − σ)`, `s = (q + q⁻¹)⁻¹`, of the interface generator
(bean `qou-kj4v`; `QOU.QBeta.InterfaceScalar.proj_add_eq_one`).

The corpus fixes no composition rule, so the probe
`computations/probes/gamma_gamma_isospin_channel_probe.py` computes six. This file proves
the two **structural** facts that hold for whole families of them, independently of any
number:

* **Composition C1 (`W·G·P_T` against `W`) obeys a sum rule.** The two channel ratios add
  up to the bare γγ ratio, `μ₊ + μ₋ = μ_G` (`channel_ratio_sum`). Because `μ_G − 1` is
  tiny (step 10: `μ_G − 1 = h⁴·c(q)`, `0 < c ≤ 1`), the physical sign pattern — `T = 1`
  unbound (`μ₊ > 1`) *and* `T = 0` bound (`0 < μ₋ < 1`) — is only reachable with
  `μ₋ < μ_G − 1`, i.e. a deuteron bound by **more than** `α·log(1/(μ_G − 1))`
  (`signPattern_forces_deuteron_floor`). That is a cost, not a closure: it says what the
  pattern would require of the `T = 0` channel, with no input from nature.
* **Compositions C4/C5 (channel-relative, against `W·P_T`) average to the bare ratio.**
  `μ_G = w₊·μ₊ʳᵉˡ + w₋·μ₋ʳᵉˡ` with `w₊ + w₋ = 1` (`relative_channel_average`), so whenever the
  weights are positive and `μ_G > 1`, **at least one** channel is unbound
  (`some_channel_unbound_of_bare_unbound`).

Both are linear algebra over a generic ring / ordered field (§7c); `ℝ` enters only where
`Real.log` does. Nothing here asserts a value of any trace.

## What the probe measured (recorded for context; not used by any proof)

`computations/probes/gamma-gamma-isospin-channel-probe.witness.json`, exact over `ℚ(q)`,
convention D, proton pin, selected vertex `V1`, `B = 𝔈₀^full·log(|tr_free|/|tr_atom|)`:

* C1–C3 (against `W`): every channel bound, `T = 1` at ≈ 1.2 MeV, `T = 0` at ≈ 5.8 MeV.
  The C1 sum rule holds exactly; at `μ_G(pn) = 1.000611` the floor above is ≈ 31 MeV.
* C4, C6 (against `W·P_T`, bond after / around the projector): `T = 1` bound, `T = 0`
  unbound — the inverted pattern.
* C5 (`W·P_T·G` against `W·P_T`): `T = 1` unbound (pp −17.4 keV, nn −10.0 keV), `T = 0`
  bound (pn +20.2 keV, np +35.1 keV).
* In **no** composition containing `G` is `pp = nn`: the response stays one-body (step 11),
  so `pp = np` and `nn = pn` exactly for `V1`, and charge independence would need the
  proton and neutron right-responses to coincide, which they do not.

C4 and C5 differ only in the order of `P_T` and `G`; nothing in the corpus fixes it, and
choosing C5 because its signs match nature would be selection against the target.
-/

namespace QOU.Mass.GammaGammaIsospinChannel

section Linear

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- The projectors are complementary — restated here (the same identity as
`QOU.QBeta.InterfaceScalar.proj_add_eq_one`) so this file depends on Mathlib only. -/
theorem proj_add_eq_one (σ : A) (q qi s : R) (hs : s * (q + qi) = 1) :
    s • (σ + qi • (1 : A)) + s • (q • (1 : A) - σ) = 1 := by
  have expand : s • (σ + qi • (1 : A)) + s • (q • (1 : A) - σ)
      = (s * (q + qi)) • (1 : A) := by
    module
  rw [expand, hs, one_smul]

/-- **C1 at the operator level.** Right-multiplying the bonded word by the two projectors
and adding gives back the bonded word: `X·P₊ + X·P₋ = X` for every `X`. -/
theorem bonded_word_splits (X σ : A) (q qi s : R) (hs : s * (q + qi) = 1) :
    X * (s • (σ + qi • (1 : A))) + X * (s • (q • (1 : A) - σ)) = X := by
  rw [← mul_add, proj_add_eq_one σ q qi s hs, mul_one]

/-- **C1 at the trace level.** For any `R`-linear trace, the two projected bonded traces
add up to the bare bonded trace. -/
theorem trace_splits (tr : A →ₗ[R] R) (X σ : A) (q qi s : R) (hs : s * (q + qi) = 1) :
    tr (X * (s • (σ + qi • (1 : A)))) + tr (X * (s • (q • (1 : A) - σ))) = tr X := by
  rw [← map_add, bonded_word_splits X σ q qi s hs]

end Linear

section Ratios

variable {F : Type*} [Field F]

/-- **The C1 sum rule.** Dividing `trace_splits` by the free trace: the `T = 1` and `T = 0`
ratios of composition C1 sum to the bare γγ ratio `μ_G = tr(W·G)/tr(W)`. -/
theorem channel_ratio_sum (tPlus tMinus tG tW : F) (hsplit : tPlus + tMinus = tG) :
    tPlus / tW + tMinus / tW = tG / tW := by
  rw [← add_div, hsplit]

/-- **The C4/C5 average.** With channel weights `w_T = tr(W·P_T)/tr(W)` and relative ratios
`μ_Tʳᵉˡ = tr(W·G·P_T)/tr(W·P_T)`, the bare ratio is their weighted sum. -/
theorem relative_channel_average (tPlus tMinus tWPlus tWMinus tW : F)
    (hWp : tWPlus ≠ 0) (hWm : tWMinus ≠ 0) :
    (tWPlus / tW) * (tPlus / tWPlus) + (tWMinus / tW) * (tMinus / tWMinus)
      = (tPlus + tMinus) / tW := by
  field_simp

end Ratios

section Order

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- In a sum rule `μ₊ + μ₋ = μ_G`, the `T = 1` channel is unbound and the `T = 0` channel
has positive ratio only if `μ₋ < μ_G − 1`. -/
theorem minus_lt_of_signPattern (μp μm μG : F) (hsum : μp + μm = μG) (hp : 1 < μp) :
    μm < μG - 1 := by
  linarith

/-- Contrapositive: if the `T = 0` ratio is at least `μ_G − 1`, the `T = 1` channel is
bound or marginal (`μ₊ ≤ 1`). -/
theorem plus_le_one_of_minus_ge (μp μm μG : F) (hsum : μp + μm = μG) (hm : μG - 1 ≤ μm) :
    μp ≤ 1 := by
  linarith

/-- **At least one relative channel is unbound.** A convex combination with positive
weights that exceeds `1` has a term exceeding `1`. -/
theorem some_channel_unbound_of_bare_unbound (wp wm μp μm μG : F)
    (hwp : 0 < wp) (hwm : 0 < wm) (hw : wp + wm = 1) (havg : wp * μp + wm * μm = μG)
    (hG : 1 < μG) : 1 < μp ∨ 1 < μm := by
  by_contra h
  push_neg at h
  obtain ⟨hp, hm⟩ := h
  have : wp * μp + wm * μm ≤ wp * 1 + wm * 1 := by
    have h1 : wp * μp ≤ wp * 1 := mul_le_mul_of_nonneg_left hp (le_of_lt hwp)
    have h2 : wm * μm ≤ wm * 1 := mul_le_mul_of_nonneg_left hm (le_of_lt hwm)
    linarith
  linarith

end Order

section Binding

/-- **The deuteron floor forced by the C1 sign pattern.** Under the live law
`B = −α·log μ` with `α > 0`: if `μ₊ + μ₋ = μ_G`, the `T = 1` channel is unbound
(`μ₊ > 1`) and the `T = 0` ratio is positive, then the `T = 0` binding exceeds
`α·log(1/(μ_G − 1))`. With `μ_G − 1 = h⁴·c(q)` of order `10⁻³` at the anchor, this is a
deuteron bound by several `α`, which is what the pattern costs under C1. -/
theorem signPattern_forces_deuteron_floor (α μp μm μG : ℝ) (hα : 0 < α)
    (hsum : μp + μm = μG) (hp : 1 < μp) (hm : 0 < μm) :
    α * Real.log (1 / (μG - 1)) < -α * Real.log μm := by
  have hlt : μm < μG - 1 := minus_lt_of_signPattern μp μm μG hsum hp
  have hG1 : 0 < μG - 1 := lt_trans hm hlt
  have hlog : Real.log μm < Real.log (μG - 1) := Real.log_lt_log hm hlt
  rw [one_div, Real.log_inv]
  nlinarith

/-- The same floor stated against a ceiling on the bare deviation: if `μ_G − 1 ≤ ε`,
the C1 sign pattern forces `B_{T=0} > α·log(1/ε)`. -/
theorem signPattern_forces_deuteron_floor_of_le (α μp μm μG ε : ℝ) (hα : 0 < α)
    (hsum : μp + μm = μG) (hp : 1 < μp) (hm : 0 < μm) (hε : μG - 1 ≤ ε) :
    α * Real.log (1 / ε) < -α * Real.log μm := by
  have hlt : μm < μG - 1 := minus_lt_of_signPattern μp μm μG hsum hp
  have hG1 : 0 < μG - 1 := lt_trans hm hlt
  have hmε : μm < ε := lt_of_lt_of_le hlt hε
  have hlog : Real.log μm < Real.log ε := Real.log_lt_log hm hmε
  rw [one_div, Real.log_inv]
  nlinarith

end Binding

end QOU.Mass.GammaGammaIsospinChannel
