/-
# The multiplicative binding carries connected 4-body content — magnitude undershoots

Companion to
  computations/deltalambda/b4_multiplicative_cumulant_probe.py
  docs/audits/2026-08-02-option-e-b4-multiplicative-cumulant.md

## Context (Option-E / GAP-A-4, front 4 — the interface-operator / 4-body route)

The framework's canonical binding is the **multiplicative** interface form
(`binding_canonical.py`, `interface_4body_assembly_probe.py`)

    B(K) = E₀ · τ_vac · (1 − ∏ᵢ fᵢ),

with the product over the interface pair-factors `fᵢ` (pp = z, nn = z − h,
pn = z or z − h/2).  The connected 4-body Ursell cumulant is the 4th forward
finite difference of the binding sequence (`BodyOrderCumulant.fourthDiff`).

`BodyOrderCumulant.lean` proved the **additive** binding forms are *orthogonal*
to the 4-body channel: a 1-body-linear (`B_vol`) or 2-body-additive (`B_sym`)
binding has connected `b₄ = 0`.  This file records the complementary structural
fact for the **multiplicative** form: because `∏ᵢ fᵢ` is an exponential in the
pair count `C(A,2)`, the multiplicative binding is **not** pairwise-additive and
its 4-body cumulant is **generically nonzero** — the multiplicative route can
carry connected 4-body content the additive route structurally cannot.

The accompanying probe evaluates that cumulant 0-fit at the substrate `q₀` and
finds it reaches only **≈6.3 %** (production pn = z) / **≈36 %** (bar-invariant
pn = z − h/2) of the ⁴He AME target `b₄ ≈ 9.243 MeV`.  That magnitude
undershoot is a *scope-(a)* numerical result (the multiplicative connected
4-body cumulant, alone, undershoots); this file supplies only the structural
scaffolding that makes the extraction meaningful — the closed form, its two
sanity vanishings, and the bar-parity split of the pn factor (the I-par
refinement: the pn factor is bar-mixed, its retained-binding part is the
bar-even projection `z`).

Base ring: generic `[CommRing R]` (§7c) — pure polynomial identities in the
formal magnitudes `τ, f, z, h`; no ordering, no `Real`, no `q₀`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import QOU.MassTheory.BodyOrderCumulant

namespace QOU.MassTheory

variable {R : Type*} [CommRing R]

/-- The **symmetric-cluster multiplicative binding** table
`B(A) = τ^A · (1 − f^{C(A,2)})` for `A = 0,…,4`, with pair counts
`C(A,2) = 0,0,1,3,6`.  (0/1-body: no pairs ⇒ `1 − f^0 = 0` ⇒ `B = 0`.)  This is
the symmetric idealisation of the framework binding
`E₀ · τ_vac · (1 − ∏ f)`; the overall `E₀` scale is dropped (it cancels in the
fraction-of-target headline the probe reports). -/
def multBinding (τ f : R) : ℕ → R
  | 0 => 0
  | 1 => 0
  | 2 => τ ^ 2 * (1 - f ^ 1)
  | 3 => τ ^ 3 * (1 - f ^ 3)
  | 4 => τ ^ 4 * (1 - f ^ 6)
  | _ => 0

@[simp] theorem multBinding_zero (τ f : R) : multBinding τ f 0 = 0 := rfl
@[simp] theorem multBinding_one (τ f : R) : multBinding τ f 1 = 0 := rfl
@[simp] theorem multBinding_two (τ f : R) : multBinding τ f 2 = τ ^ 2 * (1 - f ^ 1) := rfl
@[simp] theorem multBinding_three (τ f : R) : multBinding τ f 3 = τ ^ 3 * (1 - f ^ 3) := rfl
@[simp] theorem multBinding_four (τ f : R) : multBinding τ f 4 = τ ^ 4 * (1 - f ^ 6) := rfl

/-- **Closed form of the multiplicative connected 4-body cumulant.**  The 4th
forward finite difference of the multiplicative binding sequence is
`τ⁴(1−f⁶) − 4τ³(1−f³) + 6τ²(1−f)`.  This is the quantity the probe evaluates
0-fit; the finite-difference extractor is the same `fourthDiff` proved in
`BodyOrderCumulant` to annihilate ≤2-body content, so this is genuinely the
*connected* 4-body part. -/
theorem multBinding_b4 (τ f : R) :
    fourthDiff (multBinding τ f)
      = τ ^ 4 * (1 - f ^ 6) - 4 * (τ ^ 3 * (1 - f ^ 3)) + 6 * (τ ^ 2 * (1 - f)) := by
  simp only [fourthDiff, multBinding_zero, multBinding_one, multBinding_two,
    multBinding_three, multBinding_four, pow_one]
  ring

/-- **No coupling ⇒ no connected cumulant.**  At `f = 1` every saturation factor
`1 − f^k` vanishes, so the multiplicative 4-body cumulant is `0`.  The connected
content is generated *entirely* by the coupling `f ≠ 1`; there is no spurious
4-body term from the extensive `τ^A` growth alone. -/
theorem multBinding_b4_at_f_one (τ : R) : fourthDiff (multBinding τ 1) = 0 := by
  rw [multBinding_b4]; ring

/-- **Pure-saturation cumulant** (drop the extensive `τ^A` growth, `τ = 1`).  The
connected 4-body part of `Bsat(A) = 1 − f^{C(A,2)}` is the explicit polynomial
`3 − 6f + 4f³ − f⁶`.  This is the "saturation ceiling" the probe's headline sits
against: it isolates how much connected 4-body content the *pair-count exponent*
`C(A,2)` alone supplies, independent of the (weak) `τ^A` growth. -/
theorem satBinding_b4 (f : R) :
    fourthDiff (multBinding 1 f) = 3 - 6 * f + 4 * f ^ 3 - f ^ 6 := by
  rw [multBinding_b4]; ring

/-- The pure-saturation cumulant also vanishes at `f = 1` (`3 − 6 + 4 − 1 = 0`):
a constant per-nucleon factor carries no connected 4-body content. -/
theorem satBinding_b4_at_f_one : fourthDiff (multBinding (1 : R) 1) = 0 := by
  rw [satBinding_b4]; ring

/-- **Non-vacuity / contrast with the additive route.**  Concretely at
`τ = 1, f = 0` the multiplicative 4-body cumulant is `3 ≠ 0`, whereas every
additive form (`fourthDiff_linear`, `fourthDiff_pairwise` in `BodyOrderCumulant`)
gives `0` identically.  So the multiplicative binding is the structurally
correct place to look for the missing ⁴He `b₄` — it is not orthogonal to the
4-body channel. -/
theorem multBinding_b4_nonvacuous : fourthDiff (multBinding (1 : ℤ) 0) = 3 := by
  rw [satBinding_b4]; ring

/-! ## Bar-parity of the pn interface factor (the I-par refinement)

`b4_connected_bar_parity_probe.py` establishes that the Markov `z` is **bar-even**
(`z(q) = z(q⁻¹)`) and the Hecke `h` is **bar-odd** (`h(q) = −h(q⁻¹)`).  Under the
bar involution `q ↦ q⁻¹` acting as `z ↦ z, h ↦ −h`, the pn pair factor
`z − h/2` is therefore **bar-mixed** — the original I-par phrasing "prove `b₄` is
bar-even" is too strong (it is FALSE for the multiplicative pn route, unlike the
writhe-determinant route of `B4CumulantBarEven` which is genuinely bar-even).

We record the split over a generic `CommRing`, using `2·(pn factor) = 2z − h` to
avoid division.  The bar-even projection of the pn factor is `z` (the pp/nn
Markov weight) and the bar-odd part is `−h/2` (the radiated Q_β-like channel). -/

/-- Twice the pn pair factor, `2·(z − h/2) = 2z − h`.  (Working with the doubled
form keeps everything over a generic `CommRing` — no division needed.) -/
def twoPnFactor (z h : R) : R := 2 * z - h

/-- The bar image of `twoPnFactor` under `z ↦ z, h ↦ −h`: `2z − (−h) = 2z + h`. -/
def twoPnFactorBar (z h : R) : R := 2 * z + h

/-- **The pn factor is bar-mixed** (I-par refined, not passed as stated): its bar
image differs from itself by `2h`, so it is bar-invariant iff `h = 0`. -/
theorem twoPnFactor_bar_mixed (z h : R) :
    twoPnFactorBar z h - twoPnFactor z h = 2 * h := by
  unfold twoPnFactor twoPnFactorBar; ring

/-- **Bar-even projection = the Markov weight `z`.**  The (doubled) bar-even
projection `½(f_pn + f_pn^bar)` of the pn factor is `2z`, i.e. the projection is
`z` — the retained binding part is exactly the pp/nn Markov weight, stripped of
the bar-odd `−h/2`. -/
theorem twoPnFactor_barEven_proj (z h : R) :
    twoPnFactor z h + twoPnFactorBar z h = 2 * (2 * z) := by
  unfold twoPnFactor twoPnFactorBar; ring

/-- **Bar-odd projection = `−h`.**  The (doubled) bar-odd projection
`½(f_pn − f_pn^bar)` of the pn factor is `−h`, i.e. the projection is `−h/2` —
the radiated (Q_β-like) channel, not retained binding. -/
theorem twoPnFactor_barOdd_proj (z h : R) :
    twoPnFactor z h - twoPnFactorBar z h = 2 * (-h) := by
  unfold twoPnFactor twoPnFactorBar; ring

end QOU.MassTheory
