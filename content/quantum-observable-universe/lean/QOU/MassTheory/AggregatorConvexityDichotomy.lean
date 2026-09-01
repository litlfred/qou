import Mathlib.Tactic
import Mathlib.Analysis.Convex.Function

/-!
# The 3-body cumulant sign is a convexity statement about the aggregator

Two assemblies have now been machine-checked to miss the measured 3-body Ursell
cumulant, in **opposite directions**:

* the multiplicative / Mayer assembly `W(K) = 1 − ∏ f_ij` gives `b₃ < 0`
  (`QOU.MassTheory.MayerThreeBodySign.b3_neg_of_le`, and the same sign in
  `QOU.MassTheory.Mu3SlotExclusion.thirdDiff_multiplicative`);
* the bond-functional additive assembly gives `b₃ = 0` **exactly**
  (`QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_ofBondFunctional`, and the
  4-body analogue `QOU.MassTheory.BodyOrderCumulant.fourthDiff_pairwise`);
* AME2020 requires `b₃ = +1.4262225 > 0`
  (`QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq`).

Read as two separate failures, the natural next move is to try a third assembly.
This file says that is the wrong move, because **both failures are the same
failure**, and names the one property that decides the sign.

## The statement

Write the binding of a symmetric `A`-body system as a function of its *total
bond weight*: `B(A) = Φ(m_A · g)` where `m_A` is the bond count and `g` the
common per-bond weight. The deuteron carries one bond and the three-body system
three, so with `Φ 0 = 0` the Ursell inversion `b₃ = B(3) − 3·B(2)` is

    b₃ = Φ(3g) − 3·Φ(g) =: b3Agg Φ g

which is a **secant comparison on the ray through the origin**, and nothing else.
Jensen at the two points `0` and `3g` with weights `(2/3, 1/3)` gives, with no
further hypotheses,

* `Φ` concave through the origin ⇒ `b₃ ≤ 0`  (`b3Agg_nonpos_of_concaveOn`)
* `Φ` convex through the origin  ⇒ `b₃ ≥ 0`  (`b3Agg_nonneg_of_convexOn`)

so the contrapositive `not_concaveOn_of_b3Agg_pos` is the result the programme
needs: **the measured positive `b₃` excludes every concave-through-the-origin
aggregator, for every bond weight and every bond set.**

## Why this subsumes both prior negatives

The additive assembly is `Φ = (a • ·)`, the boundary case — affine is concave, so
it saturates the bound at `b₃ = 0` exactly (`b3Agg_linear_eq_zero`, which
recovers `b3_eq_zero_ofBondFunctional`'s value independently and by a different
route; this is a numerical agreement, not a formal reduction of that theorem).

The multiplicative assembly with a common bond factor is `1 − f^n` in the bond
count, and its cumulant factors **exactly** (`wMult_b3_factor`):

    b₃ = (1 − f³) − 3(1 − f) = −(f − 1)²·(f + 2)

a negated perfect square times a positive factor. So on `f > −2` it is `≤ 0`
unconditionally and vanishes **only** at `f = 1`, i.e. only when the bonds do not
couple at all (`wMult_b3_eq_zero_iff`). That is strictly sharper than
`MayerThreeBodySign.b3_neg_of_le`, which needed the measured threshold
`f_pn ≤ 2/3` to conclude; in the equal-bond case no threshold is needed, and the
`(f − 1)²` says the negative sign is *second order* in the coupling, not an
artefact of where the measured `f_pn` happens to sit.

## Scope, and what this does NOT exclude

This is a **scope-(b) structural exclusion** in the sense of `AGENTS.md`
§"Before declaring refuted": the invariant is Jensen's inequality, cited and
proved here, and the excluded class is *concave-through-the-origin aggregators of
the total bond weight*.

It excludes nothing else, and in particular the convex branch is **open and
reachable** — `b3Agg_sq_pos` exhibits a convex `Φ` with `b₃ = 6 > 0`. The
programme's orientation therefore inverts: the aggregator must be **strictly
convex at small argument**, i.e. binding must be *superadditive* in bond count
rather than saturating in it. Two live constraints bound that search from the
other side and are not addressed here:

* saturation (`QOU.Mass.CoordinationSaturation`) needs `B/A` bounded, which for
  convex `Φ` through the origin means `Φ x / x` must be bounded — so `Φ` has to
  be strictly convex at small argument and asymptotically linear. That is a
  narrow but non-empty class (`x²/(1+x)` is in it); whether the framework's
  Hecke-side quantities produce such a `Φ` is exactly the open question.
* the connected 3-body sign is not the only target: `b₄ = +9.243387` must come
  out too, and **`b₄`'s sign is not decided by concavity** — `√·` is concave and
  yields a positive `b₄` — so `b₃` is the sharp discriminator of this family and
  `b₄` is not. Do not read a `b₄` agreement as evidence about the aggregator.

Reference for the cumulant conventions and the AME2020 inputs:
`docs/coordination/2026-08-29-bk-crossing-mass-binding-arc-reassessment.md`.
-/

namespace QOU.MassTheory.AggregatorConvexity

open Set

/-- The connected 3-body Ursell cumulant of a symmetric binding assembled as
`B(A) = Φ(m_A · g)` with bond counts `m_2 = 1`, `m_3 = 3` and `Φ 0 = 0`:

    b₃ = B(3) − 3·B(2) = Φ(3g) − 3·Φ(g).

A secant comparison on the ray through the origin. -/
noncomputable def b3Agg (Φ : ℝ → ℝ) (g : ℝ) : ℝ := Φ (3 * g) - 3 * Φ g

/-- **A concave aggregator through the origin cannot produce a positive 3-body
cumulant.** Jensen at `0` and `3g` with weights `(2/3, 1/3)`. No hypothesis on
the bond set enters: `g` is the common bond weight and `3` the three-body bond
count, and the argument is one secant comparison. -/
theorem b3Agg_nonpos_of_concaveOn {Φ : ℝ → ℝ}
    (hΦ : ConcaveOn ℝ (Ici (0 : ℝ)) Φ) (h0 : Φ 0 = 0) {g : ℝ} (hg : 0 ≤ g) :
    b3Agg Φ g ≤ 0 := by
  have h00 : (0 : ℝ) ∈ Ici (0 : ℝ) := by simp
  have h3g : (3 : ℝ) * g ∈ Ici (0 : ℝ) := by simp only [mem_Ici]; linarith
  have key := hΦ.2 h00 h3g (by norm_num : (0:ℝ) ≤ 2/3) (by norm_num : (0:ℝ) ≤ 1/3)
      (by norm_num : (2:ℝ)/3 + 1/3 = 1)
  simp only [smul_eq_mul, h0, mul_zero, zero_add] at key
  rw [show (1:ℝ)/3 * (3 * g) = g by ring] at key
  unfold b3Agg
  linarith

/-- **A convex aggregator through the origin cannot produce a negative one.**
The dual of `b3Agg_nonpos_of_concaveOn`, and the half that says the target sign
is reachable at all. -/
theorem b3Agg_nonneg_of_convexOn {Φ : ℝ → ℝ}
    (hΦ : ConvexOn ℝ (Ici (0 : ℝ)) Φ) (h0 : Φ 0 = 0) {g : ℝ} (hg : 0 ≤ g) :
    0 ≤ b3Agg Φ g := by
  have h00 : (0 : ℝ) ∈ Ici (0 : ℝ) := by simp
  have h3g : (3 : ℝ) * g ∈ Ici (0 : ℝ) := by simp only [mem_Ici]; linarith
  have key := hΦ.2 h00 h3g (by norm_num : (0:ℝ) ≤ 2/3) (by norm_num : (0:ℝ) ≤ 1/3)
      (by norm_num : (2:ℝ)/3 + 1/3 = 1)
  simp only [smul_eq_mul, h0, mul_zero, zero_add] at key
  rw [show (1:ℝ)/3 * (3 * g) = g by ring] at key
  unfold b3Agg
  linarith

/-- **The exclusion, as the programme uses it.** A strictly positive 3-body
cumulant — which is what AME2020 measures, `b₃ = +1.4262225` — refutes concavity
of the aggregator on `[0, ∞)`, whatever the bond weight and bond set. -/
theorem not_concaveOn_of_b3Agg_pos {Φ : ℝ → ℝ} (h0 : Φ 0 = 0) {g : ℝ}
    (hg : 0 ≤ g) (hpos : 0 < b3Agg Φ g) : ¬ ConcaveOn ℝ (Ici (0 : ℝ)) Φ := by
  intro hΦ
  exact absurd (b3Agg_nonpos_of_concaveOn hΦ h0 hg) (not_le.mpr hpos)

/-- **The additive assembly is the boundary case.** An affine-through-the-origin
aggregator — the bond-functional sum — saturates both bounds at `b₃ = 0`. This
reaches the value of `QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_ofBondFunctional`
by a different route; it is a numerical agreement, not a reduction of it. -/
theorem b3Agg_linear_eq_zero (a g : ℝ) : b3Agg (fun x => a * x) g = 0 := by
  unfold b3Agg; ring

/-- **Non-vacuity of the convex branch.** A strictly convex aggregator does reach
a positive cumulant, so `not_concaveOn_of_b3Agg_pos` is not excluding the target
along with the class. -/
theorem b3Agg_sq_pos : 0 < b3Agg (fun x => x ^ 2) 1 := by
  unfold b3Agg; norm_num

/-! ### The multiplicative assembly, exactly

With a common bond factor `f`, the Mayer weight of an `n`-bond system is
`1 − f^n`. -/

/-- The multiplicative (Mayer) weight of an `n`-bond system at common bond
factor `f`. -/
noncomputable def wMult (f : ℝ) (n : ℕ) : ℝ := 1 - f ^ n

/-- **The multiplicative 3-body cumulant factors as a negated perfect square.**
`(1 − f³) − 3(1 − f) = −(f − 1)²(f + 2)`. The sign is therefore *second order*
in the coupling `1 − f`, not a consequence of where the measured bond factor
sits. -/
theorem wMult_b3_factor (f : ℝ) :
    wMult f 3 - 3 * wMult f 1 = -((f - 1) ^ 2 * (f + 2)) := by
  unfold wMult; ring

/-- **Unconditional non-positivity in the equal-bond case.** No threshold on `f`
is needed beyond `f > −2`, which every genuine bond factor satisfies. This is
strictly sharper than `MayerThreeBodySign.b3_neg_of_le`, which concluded from the
measured `f_pn ≤ 2/3`. -/
theorem wMult_b3_nonpos {f : ℝ} (hf : -2 ≤ f) : wMult f 3 - 3 * wMult f 1 ≤ 0 := by
  rw [wMult_b3_factor]
  have hsq : 0 ≤ (f - 1) ^ 2 := sq_nonneg _
  nlinarith

/-- **And it vanishes only when the bonds do not couple.** On `f > −2` the
multiplicative cumulant is zero exactly at `f = 1`, i.e. exactly when every bond
factor is trivial. So within this assembly there is no tuning of `f` that
recovers a positive `b₃` — the boundary is the decoupled system. -/
theorem wMult_b3_eq_zero_iff {f : ℝ} (hf : -2 < f) :
    wMult f 3 - 3 * wMult f 1 = 0 ↔ f = 1 := by
  rw [wMult_b3_factor]
  constructor
  · intro h
    have hpos : 0 < f + 2 := by linarith
    have : (f - 1) ^ 2 = 0 := by
      rcases mul_eq_zero.mp (by linarith : (f - 1) ^ 2 * (f + 2) = 0) with h1 | h2
      · exact h1
      · exact absurd h2 (ne_of_gt hpos)
    have := pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this
    linarith
  · intro h; subst h; ring

end QOU.MassTheory.AggregatorConvexity
