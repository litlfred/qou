import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# Pinning a branch integer by the base point

Bean `qou-trns`. The 5₂ transport needs to know that a sum of logarithms equals a
logarithm of a product **on the nose**, not up to `2πi ℤ`. This file proves the
principle that forces the integer to be `0`, with no dilogarithm and no curve in
it.

## The statement the transport wants

`exp_eq_zero_of_continuousOn_of_exp_eq_one`: if `F : ℝ → ℂ` is continuous on
`[a,b]`, satisfies `exp (F y) = 1` throughout, and vanishes at `a`, then `F ≡ 0`.

The transport instantiates it at
`F φ := Σⱼ log (1 − e^{iφ} · yⱼ) − iφ` on `[0, π]`:

* `exp (F φ) = 1` is **exactly** the Vieta product `∏ⱼ (1 − x·yⱼ) = x`, which is
  already sorry-free in `QOU/QBeta/FiveTwoCyclotomicBloch.lean`
  (`prod_one_sub_x_mul`; the companion `prod_x_sub` gives the other factor).
* `F 0 = 0` is the base point `x = 1`, where every factor is `1 − yⱼ` and the
  product is `1`.
* Continuity is the one genuine analytic hypothesis. See the scoping note below —
  it is **not** the hypothesis the refuted argument used, and it is **not** the
  naive "no factor meets the cut" either. See "the arc ends on the cut".

## Why this had to be proved rather than waved at

The earlier argument for `k = 0` ran: the branch integer is integer-valued and
locally constant on a collision-free arc, hence constant; and it is `0` at the
base point. Two separate steps, and the first one was **false as stated** — the
arc is not collision-free. `QOU/QBeta/FiveTwoDiscriminant.lean` proves the
discriminant of the GGM curve vanishes at a point of `|x| = 1`.

The repair is that collisions are *harmless here*: at the collision the two
colliding roots are equal, so the two log-terms being permuted are identical and
their **sum** cannot notice the relabelling. What the sum really needs is that no
factor `1 − x·yⱼ` crosses the branch cut of `log` — a different hypothesis, and
the honest one. This file takes that hypothesis in its weakest usable form,
plain continuity of `F`, and gets `k = 0` in a single step: connectedness plus
the base point, with no appeal to local constancy.

So the division of labour is now explicit:

| ingredient | status |
|---|---|
| `exp (F φ) = 1` | Lean-proved (Vieta, #4658) |
| `F 0 = 0` | Lean-proved (same Vieta identity at `x = 1`) |
| `F` continuous on the arc | **open** — see below |
| continuity + the two above ⟹ `F ≡ 0` | **this file** |

## The arc ends on the cut — and that is why this lane keeps seeing `2π`

Route 20 (`computations/probes/qbeta_5two_route20_cut_avoidance_probe.py`,
7 gates) measured the open hypothesis rather than the conclusion, and the first
version of it **failed**. The obvious sufficient condition — no factor ever meets
`(−∞, 0]` — is false: at the endpoint `x = −1`,

    1 − x·y₁ = 1 − w₁ = −1.2469796…

sits exactly on the cut, where `w₁` is the largest root of `w³ − 2w² − w + 1` —
the level-7 ladder's own cubic. And `x = −1` is on the cut too. The transport arc
ends on the branch cut in two independent ways; it is structural, not bad luck.

Continuity survives because it forbids *crossing*, not *touching*. The contact is
transversal — the margin is exactly `w₁·(π − φ)`, measured over four orders of
magnitude — and one-sided: rising to `φ = π` the factor arrives from above, so
`arg → +π`, which is precisely where the principal branch is defined on the cut.
Left-limit meets value; `F` is continuous on `[0, π]`; `hcont` holds.

Traverse the same arc *downward* and the factor arrives from below, `arg → −π`,
while principal `Log` on the cut still returns `+π` — a genuine `2πi` jump. So
the transport's **orientation is load-bearing**, and only because of where the
principal branch is declared to sit. `qou-trns` records three separate spurious
`2π`s and calls them the most reliable false alarm in this work. This is their
mechanism.

Away from the endpoint the margin is comfortable: an interior minimum of `0.337`
at `φ/π = 0.542`, and `0.775` at the collision — the branch point is invisible to
it, which is exactly why the symmetric repair survives a collision that killed
the per-root argument.

**`hcont` is measured, not proved.** Proving it means showing from the curve that
no factor meets `(−∞, 0]` for `φ ∈ [0, π)`, plus the one-sided limit at the
endpoint. That is not written, and until it is, this lemma's hypothesis is an
assumption.

## Proof

`Complex.exp_eq_one_iff` puts every value of `F` in `2πi ℤ`, so `F` has zero real
part and its imaginary part lands in the discrete set `2π·ℤ`. A continuous real
function into `c·ℤ` is constant: if it took two distinct values `c·m < c·n`, the
intermediate value theorem would realise `c·m + c/2`, which is not a multiple of
`c` because `2(k − m) = 1` has no integer solution.

That is the whole argument. Nothing here is deep; the point is that it is stated
against the hypothesis the mathematics actually supplies.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.Archimedean

open Set

/-- Two integer multiples of `c ≠ 0` never differ by exactly `c/2`.

This is the entire arithmetic content of "a continuous function into `c·ℤ` cannot
move": the midpoint the intermediate value theorem hands back is not available. -/
theorem intMul_ne_intMul_add_half {c : ℝ} (hc : c ≠ 0) (k m : ℤ) :
    c * (k : ℝ) ≠ c * (m : ℝ) + c / 2 := by
  intro h
  have key : c * (2 * (k : ℝ) - 2 * (m : ℝ) - 1) = 0 := by linear_combination 2 * h
  have h0 : 2 * (k : ℝ) - 2 * (m : ℝ) - 1 = 0 := (mul_eq_zero.mp key).resolve_left hc
  have hz : (2 * k - 2 * m - 1 : ℤ) = 0 := by exact_mod_cast h0
  omega

/-- **A continuous real function valued in `c·ℤ` is constant**, for `c > 0`.

Stated with the base point on the left so that the conclusion pins the *value*,
not merely the constancy — that distinction is what the refuted 5₂ argument
collapsed. -/
theorem eq_of_continuousOn_intMul {f : ℝ → ℝ} {a b c x : ℝ}
    (hc : 0 < c) (hx : x ∈ Icc a b)
    (hcont : ContinuousOn f (Icc a b))
    (hval : ∀ y ∈ Icc a b, ∃ n : ℤ, f y = c * (n : ℝ)) :
    f x = f a := by
  obtain ⟨hax, hxb⟩ := hx
  have hsub : Icc a x ⊆ Icc a b := Icc_subset_Icc le_rfl hxb
  have hcont' : ContinuousOn f (Icc a x) := hcont.mono hsub
  obtain ⟨m, hm⟩ := hval a (hsub ⟨le_rfl, hax⟩)
  obtain ⟨n, hn⟩ := hval x (hsub ⟨hax, le_rfl⟩)
  by_contra hne
  have hne' : f a ≠ f x := fun h => hne h.symm
  rcases lt_or_gt_of_ne hne' with hlt | hgt
  · -- `f a < f x`, so `m + 1 ≤ n`, and `c·m + c/2` sits strictly inside
    have hmn : m < n := by
      have hR : (m : ℝ) < (n : ℝ) := by
        have h' : c * (m : ℝ) < c * (n : ℝ) := by rw [← hm, ← hn]; exact hlt
        exact lt_of_mul_lt_mul_left h' hc.le
      exact_mod_cast hR
    have hstep : (m : ℝ) + 1 ≤ (n : ℝ) := by exact_mod_cast hmn
    have hmul : c * ((m : ℝ) + 1) ≤ c * (n : ℝ) := mul_le_mul_of_nonneg_left hstep hc.le
    have hv : c * (m : ℝ) + c / 2 ∈ Icc (f a) (f x) := by
      constructor
      · rw [hm]; linarith
      · rw [hn]; nlinarith
    obtain ⟨t, ht, hft⟩ := intermediate_value_Icc hax hcont' hv
    obtain ⟨k, hk⟩ := hval t (hsub ht)
    exact intMul_ne_intMul_add_half (ne_of_gt hc) k m (hk.symm.trans hft)
  · -- `f x < f a`: the same step with the roles of the two endpoints swapped
    have hnm : n < m := by
      have hR : (n : ℝ) < (m : ℝ) := by
        have h' : c * (n : ℝ) < c * (m : ℝ) := by rw [← hm, ← hn]; exact hgt
        exact lt_of_mul_lt_mul_left h' hc.le
      exact_mod_cast hR
    have hstep : (n : ℝ) + 1 ≤ (m : ℝ) := by exact_mod_cast hnm
    have hmul : c * ((n : ℝ) + 1) ≤ c * (m : ℝ) := mul_le_mul_of_nonneg_left hstep hc.le
    have hv : c * (n : ℝ) + c / 2 ∈ Icc (f x) (f a) := by
      constructor
      · rw [hn]; linarith
      · rw [hm]; nlinarith
    obtain ⟨t, ht, hft⟩ := intermediate_value_Icc' hax hcont' hv
    obtain ⟨k, hk⟩ := hval t (hsub ht)
    exact intMul_ne_intMul_add_half (ne_of_gt hc) k n (hk.symm.trans hft)

/-- **The branch integer is pinned by the base point.**

If `F` is continuous on `[a,b]` with `exp (F y) = 1` throughout and `F a = 0`,
then `F` vanishes identically.

This is the 5₂ transport's `k = 0` step. `exp (F y) = 1` is what Vieta supplies;
`F a = 0` is the base point `x = 1`; continuity is the open hypothesis, and it is
the non-*crossing* condition, not the non-touching one — the arc's endpoint sits
on the cut (see the header). No local-constancy argument appears, and no
non-collision hypothesis is needed: the arc *does* carry a collision
(`FiveTwoDiscriminant.exists_unit_circle_disc_zero`) and it is irrelevant to a
symmetric sum. -/
theorem eq_zero_of_continuousOn_of_exp_eq_one {F : ℝ → ℂ} {a b x : ℝ}
    (hx : x ∈ Icc a b) (hcont : ContinuousOn F (Icc a b))
    (hexp : ∀ y ∈ Icc a b, Complex.exp (F y) = 1) (h0 : F a = 0) :
    F x = 0 := by
  -- `exp z = 1` puts `z` on the imaginary axis at a multiple of `2π`
  have hre : ∀ y ∈ Icc a b, (F y).re = 0 := by
    intro y hy
    obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp (hexp y hy)
    rw [hn]; simp
  have him : ∀ y ∈ Icc a b, ∃ n : ℤ, (F y).im = 2 * Real.pi * (n : ℝ) := by
    intro y hy
    obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp (hexp y hy)
    exact ⟨n, by rw [hn]; simp; ring⟩
  -- the imaginary part is a continuous function into `2π·ℤ`, hence constant
  have hcontIm : ContinuousOn (fun y => (F y).im) (Icc a b) :=
    Complex.continuous_im.comp_continuousOn hcont
  have hpi : (0 : ℝ) < 2 * Real.pi := by positivity
  have hconst : (F x).im = (F a).im :=
    eq_of_continuousOn_intMul hpi hx hcontIm him
  -- and the base point kills it
  apply Complex.ext
  · simpa using hre x hx
  · simpa [h0] using hconst

end QOU.Archimedean
