import Mathlib.Tactic

/-!
# The multiplicative assembly cannot produce a positive 3-body cumulant here

`he4_body_order_shortfall_location_probe.py` (2026-08-29) measured the model's
connected 3-body Ursell cumulant as **wrong-signed** against AME2020 — `−2.744`
against `+1.426` — under *all four* convention × bond-typing combinations it
tried. That is four data points, and the obvious readings were that the bond
typing is wrong, or that the arrangement freedom
(`QOU.MassTheory.ChainBondOrderDependence`) is contaminating it.

Neither. The sign is **forced**, and this file says by what.

## Setup

The model is `B(K) = B_AME(D) · W(K)/W(D)` with the multiplicative assembly
`W(K) = 1 − ∏_{i<j} f_ij` (`multiplicative_W`), and the Ursell inversion
`b₂ = B(D)`, `b₃ = B̄(3) − 3·b₂`. The normalisation `B_AME(D)/W(D)` is positive,
so it does not affect signs; work in `W`-units. Writing `fpn` for the deuteron's
bond factor and `P₃` for the product of bond factors over whatever edge set the
three-body system carries,

    b₂ = 1 − fpn,     b₃ = (1 − P₃) − 3·(1 − fpn) = 3·fpn − 2 − P₃.

## Result

`b3_le_of_nonneg` — since bond factors are positive, `P₃ ≥ 0`, hence

    b₃ ≤ 3·fpn − 2

and therefore `lt_of_b3_pos`: **a positive 3-body cumulant requires
`fpn > 2/3`.**

Three things this does *not* depend on, which is the whole point:

* **the edge set.** `P₃` enters only through `P₃ ≥ 0`. Whether the three-body
  system is a chain, a triangle, or any derived coordination graph, the bound is
  the same. So deriving the bond set — the repair `ChainBondOrderDependence`
  calls for, and the SU(4)-partition-shape route of bean `qou-h7mh` — **cannot
  fix the 3-body sign** while the assembly stays `1 − ∏f`.
* **the like-pair factors.** `f_pp` and `f_nn` appear only inside `P₃`.
* **the overall energy scale.** `b₃`'s sign is scale-free, so the `α` question
  (bean `qou-302y`, the interface scale being ~2.70× too large) is a *magnitude*
  question and cannot bear on this sign either.

## What it excludes

Scope **(b)**, invariant named: positivity of a product of positive bond
factors. It excludes **the multiplicative assembly `W = 1 − ∏f` as the source of
the three-body term, at any `fpn ≤ 2/3`** — for every edge set, every like-pair
typing, every convention, and every energy scale.

The framework's own derived `fpn` is below the threshold in all four
combinations the 2026-08-29 probe measured (convention D and the excised C,
under both the `probe2` and `chi` typings) — the largest of them being
`fpn = z_D = 0.6126880…` against `2/3 = 0.6666…`. `chi_typing_below_threshold`
records that comparison; the companion probe carries all four at 50 dps.

So the defect is located **upstream of any weight**: it is in the assembly, not
in the body-order coefficients `a_D^(n)`. A replacement must change the
functional form, not the edge set, the typing, or the scale. Equivalently, the
falsifiable target for any replacement is that it clear `fpn > 2/3` or abandon
`1 − ∏f`.

Stated over an ordered field per AGENTS.md §7c — the ordering is genuinely
needed, the content is the inequality. Nothing else archimedean appears.
-/

namespace QOU.MassTheory.MayerThreeBodySign

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The two-body Ursell cumulant in `W`-units: `b₂ = W(2) = 1 − fpn`. -/
def b2 (fpn : R) : R := 1 - fpn

/-- The connected three-body Ursell cumulant in `W`-units,
`b₃ = W(3) − 3·b₂` with `W(3) = 1 − P₃`. -/
def b3 (fpn P3 : R) : R := (1 - P3) - 3 * b2 fpn

omit [LinearOrder R] [IsStrictOrderedRing R] in
@[simp] theorem b3_eq (fpn P3 : R) : b3 fpn P3 = 3 * fpn - 2 - P3 := by
  unfold b3 b2; ring

/-- The product of bond factors is non-negative, so the three-body cumulant is
capped by a quantity depending on the **deuteron** factor alone. -/
theorem b3_le_of_nonneg {fpn P3 : R} (hP : 0 ≤ P3) :
    b3 fpn P3 ≤ 3 * fpn - 2 := by
  rw [b3_eq]; linarith

/-- **A positive three-body cumulant requires `fpn > 2/3`** — for any edge set,
any like-pair factors, and any energy scale. -/
theorem lt_of_b3_pos {fpn P3 : R} (hP : 0 ≤ P3) (h : 0 < b3 fpn P3) :
    2 / 3 < fpn := by
  have hle : b3 fpn P3 ≤ 3 * fpn - 2 := b3_le_of_nonneg hP
  have : 0 < 3 * fpn - 2 := lt_of_lt_of_le h hle
  linarith

/-- Contrapositive, in the form the measurement meets it: at or below the
threshold the cumulant is non-positive, and strictly negative once the bond
product is strictly positive. -/
theorem b3_neg_of_le {fpn P3 : R} (hP : 0 < P3) (h : fpn ≤ 2 / 3) :
    b3 fpn P3 < 0 := by
  rw [b3_eq]; linarith

/-- The *largest* of the four `fpn` values the 2026-08-29 probe measured is the
convention-D `chi` typing, `fpn = z_D = 0.6126880371…`. It is below the
threshold, so every one of the four is. -/
theorem chi_typing_below_threshold : (6126881 / 10000000 : ℚ) < 2 / 3 := by
  norm_num

end QOU.MassTheory.MayerThreeBodySign
