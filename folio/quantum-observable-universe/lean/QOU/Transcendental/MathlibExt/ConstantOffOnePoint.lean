import Mathlib.Analysis.Calculus.MeanValue

/-!
# A continuous function with vanishing derivative off one point is constant

Bean `qou-trns`. This is the last gap in the 5₂ transport, isolated as a
statement about real functions with no dilogarithm in it.

## Why the 5₂ lane needs exactly this

The transport `S(e^{iφ}) − S(1) = φ²` is proved by an envelope argument giving
`dS/dφ = 2φ`. That argument needs the implicit function theorem, hence a
non-vanishing discriminant — and `QOU/QBeta/FiveTwoDiscriminant.lean` proves the
discriminant **vanishes at one point of the arc**. So the derivative identity is
available on `[0,π]` minus a point, and `S` is continuous throughout.

That is precisely the hypothesis set below.

## Why it is not immediate from Mathlib

`constant_of_has_deriv_right_zero` requires the right derivative at **every**
point of `Ico a b`. Splitting at the bad point `c` works on `[a,c]` — where
`Ico a c` excludes `c` — but fails on `[c,b]`, whose `Ico c b` *contains* `c`.
The fix is to apply it on `[t,b]` for each `t > c` and then let `t → c⁺`,
using continuity. That is what `constant_of_hasDerivWithinAt_zero_off_point`
does.

The exceptional point may be an endpoint or lie outside `[a,b]` entirely; those
cases are subsumed, since then the hypothesis simply holds everywhere needed.
-/

namespace QOU.Archimedean

open Set Filter Topology

/-- **Continuous, and zero derivative off a single point, implies constant.**

`f` is continuous on `[a,b]` and has vanishing right derivative at every point of
`[a,b)` *except possibly one*. Then `f` is constant.

The excepted point costs nothing: on `[a,c]` the hypothesis already covers
`[a,c)`, and to the right of `c` one applies the standard result on `[t,b]` for
each `t > c` and passes to the limit. -/
theorem constant_of_hasDerivWithinAt_zero_off_point {f : ℝ → ℝ} {a b c : ℝ}
    (hcont : ContinuousOn f (Icc a b))
    (hderiv : ∀ x ∈ Ico a b, x ≠ c → HasDerivWithinAt f 0 (Ici x) x) :
    ∀ x ∈ Icc a b, f x = f a := by
  intro x hx
  rcases le_or_gt x c with hxc | hcx
  · -- left of the bad point: `Ico a x` misses `c`, so Mathlib applies directly
    refine constant_of_has_deriv_right_zero (hcont.mono (Icc_subset_Icc le_rfl hx.2)) ?_ x ?_
    · intro y hy
      exact hderiv y ⟨hy.1, lt_of_lt_of_le hy.2 hx.2⟩ (ne_of_lt (lt_of_lt_of_le hy.2 hxc))
    · exact ⟨hx.1, le_rfl⟩
  · -- right of it: constant on `(c, x]`, then continuity at `c` transfers the value
    have hac := le_or_gt a c
    rcases hac with hac | hca
    · -- `f` is constant on `[a,c]` by the first case
      have hcx' : c ∈ Icc a b := ⟨hac, le_trans (le_of_lt hcx) hx.2⟩
      have hleft : f c = f a := by
        refine constant_of_has_deriv_right_zero
          (hcont.mono (Icc_subset_Icc le_rfl hcx'.2)) ?_ c ⟨hac, le_rfl⟩
        intro y hy
        exact hderiv y ⟨hy.1, lt_of_lt_of_le hy.2 hcx'.2⟩ (ne_of_lt hy.2)
      -- and constant on `[t, x]` for every `t ∈ (c, x]`
      have hconst : ∀ t ∈ Ioc c x, f x = f t := by
        intro t ht
        refine (constant_of_has_deriv_right_zero
          (hcont.mono (Icc_subset_Icc (le_trans hac (le_of_lt ht.1)) hx.2)) ?_ x
          ⟨ht.2, le_rfl⟩)
        intro y hy
        exact hderiv y ⟨le_trans (le_trans hac (le_of_lt ht.1)) hy.1,
          lt_of_lt_of_le hy.2 hx.2⟩ (ne_of_gt (lt_of_lt_of_le ht.1 hy.1))
      -- let `t → c⁺`
      have h1 : Tendsto f (𝓝[>] c) (𝓝 (f x)) := by
        refine Tendsto.congr' ?_ tendsto_const_nhds
        filter_upwards [Ioc_mem_nhdsGT hcx] with t ht
        exact hconst t ht
      have hmem : Icc a b ∈ 𝓝[>] c := by
        filter_upwards [Ioc_mem_nhdsGT (lt_of_lt_of_le hcx hx.2)] with t ht
        exact ⟨le_trans hac (le_of_lt ht.1), ht.2⟩
      have h2 : Tendsto f (𝓝[>] c) (𝓝 (f c)) :=
        Filter.Tendsto.mono_left (hcont c hcx') (nhdsWithin_le_iff.mpr hmem)
      rw [tendsto_nhds_unique h1 h2, hleft]
    · -- the bad point is left of `a`: the hypothesis holds on all of `Ico a x`
      refine constant_of_has_deriv_right_zero (hcont.mono (Icc_subset_Icc le_rfl hx.2)) ?_ x ?_
      · intro y hy
        exact hderiv y ⟨hy.1, lt_of_lt_of_le hy.2 hx.2⟩
          (ne_of_gt (lt_of_lt_of_le hca hy.1))
      · exact ⟨hx.1, le_rfl⟩

end QOU.Archimedean
