/-
# The bar-odd channel is rank one: there is no bar-odd object to choose

Bean `qou-fi93`; probe `computations/barparity/bar_parity_rank_one_probe.py`.

`qou-fi93` measured that every counting object the framework defines is
*exactly* bar-even — `[n]_q`, `d_q(λ)`, the Plancherel measure `d_q²/D²`,
`Σ_λ y_λ` — and recorded a scope-(b) exclusion: the colour-curve asymmetry
cannot reach a number density through any of them.  Its sibling note then
exhibited `qⁿ − q⁻ⁿ = [n]_q·(q − q⁻¹)` as a bar-*odd* object carrying a
counting integer, and immediately flagged the weakness of doing so:

> `qⁿ − q⁻ⁿ` **is not SELECTED, only exhibited.**  It is the obvious bar-odd
> companion to `[n]_q`.  Choosing it *because* it has the wanted parity would
> be selection against the target, which §NO FITTING forbids.

This file removes that objection, by proving there is nothing to select.

## The structure theorem

Write `IsBarEven f` for `f q⁻¹ = f q` and `IsBarOdd f` for `f q⁻¹ = −f q`,
as properties of a function of the modulus.  Then (`isBarOdd_iff`):

    f is bar-odd  ↔  f = (q − q⁻¹) · g  for a bar-even g.

So the bar-odd functions are the image of the bar-even ones under
multiplication by the single generator `q − q⁻¹`, and `div_skein_barEven`
inverts it.  The bar-odd channel is a **free rank-one module** over the
bar-even part.  `qⁿ − q⁻ⁿ` is not one candidate among many: *every* bar-odd
object factors through the same generator, and the generator is itself the
`n = 1` member of the family (`skein_eq_qPowOdd_one`).

## What the generator is

`q − q⁻¹` is not a new object either.  It is the Hecke structure constant —
`σᵢ² = (q − q⁻¹)σᵢ + 1`, equivalently the skein coefficient in
`L₊ − L₋ = (q − q⁻¹)L₀` (AGENTS.md §7a).  Hence the name `skein` below.

## Why the counting measures are bar-even

Not an absence of bar-odd structure: `IsBarOdd.div_barOdd` says a ratio of
two bar-odd functions is bar-even, and `[n]_q` is exactly such a ratio.  The
same factor appears twice and cancels.  `IsBarOdd.eq_zero_of_inv_self` is the
one place the characteristic is used: a bar-odd function must vanish at a
fixed point of the bar (`q⁻¹ = q`, i.e. `q² = 1`), which is precisely where
the generator vanishes.

## What this does NOT prove

No number density, no `η`, no coupling between the colour geometry and a
counting measure.  `qou-fi93`'s scope-(b) exclusion stands and its residual
gap is untouched: this settles *which* object carries bar-odd content, not
whether that content reaches an observable.  In particular the 7.878 %
colour-curve asymmetry is nowhere in this file.

Generic over a `Field`; no anchor, no `ℝ`, per §7c.  Every evaluation at `q₀`
lives in the probe.

-- Ref: [manuscript] `def:crossing-energy`, AGENTS.md §7a (Hecke-Skein
--      convention), bean `qou-fi93`
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic.LinearCombination

namespace QOU.Observations.BarParityRankOne

variable {K : Type*} [Field K]

/-- A function of the modulus is **bar-even** when the bar involution
`q ↦ q⁻¹` leaves it unchanged. -/
def IsBarEven (f : K → K) : Prop := ∀ q : K, q ≠ 0 → f q⁻¹ = f q

/-- A function of the modulus is **bar-odd** when the bar involution negates
it. -/
def IsBarOdd (f : K → K) : Prop := ∀ q : K, q ≠ 0 → f q⁻¹ = -f q

/-- The **skein coefficient** `q − q⁻¹`: the Hecke structure constant in
`σᵢ² = (q − q⁻¹)σᵢ + 1`, equivalently the coefficient in the skein relation
`L₊ − L₋ = (q − q⁻¹)L₀`. -/
def skein : K → K := fun q => q - q⁻¹

/-- The generator is itself bar-odd. -/
theorem skein_barOdd : IsBarOdd (skein : K → K) := by
  intro q _
  simp only [skein, inv_inv]
  ring

/-! ### The ℤ/2 grading -/

theorem IsBarEven.mul {f g : K → K} (hf : IsBarEven f) (hg : IsBarEven g) :
    IsBarEven (fun q => f q * g q) := by
  intro q hq; simp only []; rw [hf q hq, hg q hq]

theorem IsBarOdd.mul_barOdd {f g : K → K} (hf : IsBarOdd f) (hg : IsBarOdd g) :
    IsBarEven (fun q => f q * g q) := by
  intro q hq; simp only []; rw [hf q hq, hg q hq, neg_mul_neg]

theorem IsBarEven.mul_barOdd {f g : K → K} (hf : IsBarEven f) (hg : IsBarOdd g) :
    IsBarOdd (fun q => f q * g q) := by
  intro q hq; simp only []; rw [hf q hq, hg q hq, mul_neg]

/-- **The mechanism `qou-fi93` measured.**  A ratio of two bar-odd functions
is bar-even — the two sign flips cancel.  This is *why* `[n]_q =
(qⁿ − q⁻ⁿ)/(q − q⁻¹)` carries no bar-odd content: not an absence of
structure, but the same factor divided out twice. -/
theorem IsBarOdd.div_barOdd {f g : K → K} (hf : IsBarOdd f) (hg : IsBarOdd g) :
    IsBarEven (fun q => f q / g q) := by
  intro q hq; simp only []; rw [hf q hq, hg q hq, neg_div_neg_eq]

/-- Dividing any bar-odd function by the generator lands in the bar-even
part.  No hypothesis on `q² ≠ 1` is needed: where the generator vanishes the
bar has a fixed point, so both sides of the bar-even equation are literally
the same expression. -/
theorem div_skein_barEven {f : K → K} (hf : IsBarOdd f) :
    IsBarEven (fun q => f q / skein q) :=
  hf.div_barOdd skein_barOdd

/-- Multiplying any bar-even function by the generator lands in the bar-odd
part. -/
theorem skein_mul_barOdd {g : K → K} (hg : IsBarEven g) :
    IsBarOdd (fun q => skein q * g q) :=
  by
  intro q hq
  simp only []
  rw [skein_barOdd q hq, hg q hq, neg_mul]

/-! ### Vanishing at the fixed points of the bar -/

/-- A bar-odd function vanishes wherever the bar has a fixed point, i.e. at
`q⁻¹ = q` (`q² = 1`).  This is the only place the characteristic enters. -/
theorem IsBarOdd.eq_zero_of_inv_self {f : K → K} (hf : IsBarOdd f)
    (h2 : (2 : K) ≠ 0) {q : K} (hq : q ≠ 0) (h : q⁻¹ = q) : f q = 0 := by
  have hfq : f q = -f q := by
    have hb := hf q hq
    rwa [h] at hb
  have : (2 : K) * f q = 0 := by linear_combination hfq
  rcases mul_eq_zero.mp this with h2' | hf0
  · exact absurd h2' h2
  · exact hf0

/-- The generator vanishes exactly at the fixed points of the bar. -/
theorem skein_eq_zero_iff {q : K} : skein q = 0 ↔ q⁻¹ = q := by
  constructor
  · intro h
    simp only [skein] at h
    exact (sub_eq_zero.mp h).symm
  · intro h
    simp only [skein, h, sub_self]

/-! ### The rank-one theorem -/

/-- **The bar-odd channel is free of rank one over the bar-even part**, with
the skein coefficient `q − q⁻¹` as generator.

A function is bar-odd **iff** it is the generator times a bar-even function.
So there is no *choice* of bar-odd object: every one factors through the same
`q − q⁻¹`.  This is what turns `qou-fi93`'s `qⁿ − q⁻ⁿ` from an exhibited
candidate into the only shape available. -/
theorem isBarOdd_iff (h2 : (2 : K) ≠ 0) (f : K → K) :
    IsBarOdd f ↔
      ∃ g : K → K, IsBarEven g ∧ ∀ q : K, q ≠ 0 → f q = skein q * g q := by
  constructor
  · intro hf
    refine ⟨fun q => f q / skein q, div_skein_barEven hf, ?_⟩
    intro q hq
    by_cases hs : skein q = 0
    · have hfix : q⁻¹ = q := skein_eq_zero_iff.mp hs
      rw [hf.eq_zero_of_inv_self h2 hq hfix, hs, zero_mul]
    · exact (mul_div_cancel₀ (f q) hs).symm
  · rintro ⟨g, hg, hfg⟩ q hq
    have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
    rw [hfg q⁻¹ hqi, hfg q hq, skein_barOdd q hq, hg q hq, neg_mul]

/-! ### The worked instance: `qⁿ − q⁻ⁿ` and `[n]_q` -/

/-- The undivided object `qⁿ − q⁻ⁿ`. -/
def qPowOdd (n : ℕ) : K → K := fun q => q ^ n - (q ^ n)⁻¹

/-- The symmetric q-integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`. -/
def qIntSym (n : ℕ) : K → K := fun q => qPowOdd n q / skein q

theorem qPowOdd_barOdd (n : ℕ) : IsBarOdd (qPowOdd n : K → K) := by
  intro q _
  simp only [qPowOdd, inv_pow, inv_inv]
  ring

/-- `[n]_q` is bar-even, and the proof is the mechanism rather than a
computation: it is a ratio of two bar-odd objects. -/
theorem qIntSym_barEven (n : ℕ) : IsBarEven (qIntSym n : K → K) :=
  div_skein_barEven (qPowOdd_barOdd n)

/-- The generator is the `n = 1` member of its own family. -/
theorem skein_eq_qPowOdd_one : (skein : K → K) = qPowOdd 1 := by
  funext q
  simp only [skein, qPowOdd, pow_one]

/-- `qⁿ − q⁻ⁿ = (q − q⁻¹)·[n]_q`, holding at the fixed points of the bar too
(both sides vanish there). -/
theorem qPowOdd_eq_skein_mul_qIntSym (h2 : (2 : K) ≠ 0) (n : ℕ) {q : K}
    (hq : q ≠ 0) : qPowOdd n q = skein q * qIntSym n q := by
  by_cases hs : skein q = 0
  · have hfix : q⁻¹ = q := skein_eq_zero_iff.mp hs
    rw [(qPowOdd_barOdd n).eq_zero_of_inv_self h2 hq hfix, hs, zero_mul]
  · exact (mul_div_cancel₀ (qPowOdd n q) hs).symm

/-- **The answer to `qou-fi93`'s residual.**  Any bar-odd function agrees
with `qⁿ − q⁻ⁿ` up to a bar-even factor, wherever the latter is nonzero —
because both are the same generator times a bar-even function.  So `qⁿ − q⁻ⁿ`
is not selected: it is representative of the whole channel. -/
theorem barOdd_div_qPowOdd_barEven {f : K → K} (hf : IsBarOdd f) (n : ℕ) :
    IsBarEven (fun q => f q / qPowOdd n q) :=
  hf.div_barOdd (qPowOdd_barOdd n)

end QOU.Observations.BarParityRankOne
