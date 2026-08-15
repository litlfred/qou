/-
Copyright (c) 2026 litlfred. All rights reserved.

# Wiring FKV eq-22 into the strip-growth comparability shape

Option-1 brick of the FKV programme (owner-uploaded `library/arxiv-hep-th-0006156v1/0006156v1.pdf`,
Faddeev–Kashaev–Volkov 2001, [hep-th/0006156](https://arxiv.org/abs/hep-th/0006156)
§6). The audit `2026-07-31-fkv-phib-strip-growth-...` showed FKV **eq 22** (the
four-sector asymptotic of `e_b = phiBProd`) supplies the compact fundamental-domain
bound that `FaddeevStripGrowthBoxReduction` (#4424) promotes to a global one. This
file lands the **algebraic converter** that turns that global *ratio* bound into the
`FaddeevPhiStripGrowth.comparable` *shape* (`‖Φ‖ ≤ C‖Ψ‖ ∧ ‖Ψ‖ ≤ C‖Φ‖`), off the
reference's zeros.

The full wiring is:

```
FKV eq 22 (compact-domain ratio bound, cited)  ─┐
ratio Φ/Ψ periodic under ⟨ib, i/b⟩ (on main:    ├─ #4424 comparable_of_periodic_ballBound
  CyclicDilogPentagon.ratio_ib/ibinv_periodic)  ─┘        │
                                                          ▼
                                          global two-sided ratio bound
                                                          │  (this file)
                                                          ▼
                              ‖Φ z‖ ≤ C‖Ψ z‖ ∧ ‖Ψ z‖ ≤ C‖Φ z‖   (Ψ z ≠ 0)
```

**Scope (converter, not closure).** This is the last algebraic step, taken as a
standalone lemma over the *global ratio bound* (whatever supplies it). It gives the
comparability shape **where the reference `Ψ` is nonzero**; at `Ψ`'s discrete zero
lattice the upper bound `‖Φ‖ ≤ C‖Ψ‖` additionally needs `Φ` to vanish there — the
same-divisor input, which on the `phiBProd` side is already pinned (eq 21 /
`PhiBProdDivisor`). The remaining genuinely-open input stays FKV eq-22 itself (the
`Θ`-asymptotic, not formalized here — that is option 2). No fit; nothing wired to
production; the leg stays *stated*-conditional. Uses only on-`main`
`FaddeevStripGrowthBoxReduction`. Sorry-free.

-- Ref: [faddeev-kashaev-volkov-2001] https://arxiv.org/abs/hep-th/0006156 (§6, eq 22)
-/
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.LinearAlgebra.Basis.Basic
import QOU.QBeta.FaddeevStripGrowthBoxReduction

namespace QOU.QBeta.FaddeevStripGrowthFKV

open Module

/-- **Comparability shape from the compact ratio bound.** Let the ratio `Φ/Ψ` be
periodic under an `ℝ`-basis `bas` of `ℂ` and satisfy the two-sided bound
`‖Φ/Ψ‖ ≤ C`, `1/C ≤ ‖Φ/Ψ‖` on the closed fundamental ball (the FKV eq-22 input).
Then, wherever `Ψ z ≠ 0`, the `FaddeevPhiStripGrowth.comparable` shape holds:
`‖Φ z‖ ≤ C‖Ψ z‖` and `‖Ψ z‖ ≤ C‖Φ z‖`. The two-sided global ratio bound comes from
`FaddeevStripGrowthBoxReduction.comparable_of_periodic_ballBound`; this file adds the
`norm_div` conversion to the `Φ`/`Ψ` modulus inequalities. -/
theorem comparable_shape_of_periodic_ballBound
    {Φ Ψ : ℂ → ℂ} {bas : Basis (Fin 2) ℝ ℂ} {C : ℝ} (hC : 0 < C)
    (hper : ∀ (i : Fin 2) (z : ℂ), (Φ (z + bas i) / Ψ (z + bas i)) = Φ z / Ψ z)
    (hballU : ∀ w : ℂ, ‖w‖ ≤ ‖bas 0‖ + ‖bas 1‖ → ‖Φ w / Ψ w‖ ≤ C)
    (hballL : ∀ w : ℂ, ‖w‖ ≤ ‖bas 0‖ + ‖bas 1‖ → 1 / C ≤ ‖Φ w / Ψ w‖)
    {z : ℂ} (hΨ : Ψ z ≠ 0) :
    ‖Φ z‖ ≤ C * ‖Ψ z‖ ∧ ‖Ψ z‖ ≤ C * ‖Φ z‖ := by
  obtain ⟨hU, hL⟩ :=
    FaddeevStripGrowthBoxReduction.comparable_of_periodic_ballBound
      (r := fun z => Φ z / Ψ z) hper hballU hballL z
  rw [norm_div] at hU hL
  have hΨpos : 0 < ‖Ψ z‖ := norm_pos_iff.mpr hΨ
  refine ⟨(div_le_iff₀ hΨpos).mp hU, ?_⟩
  have hstep : 1 / C * ‖Ψ z‖ ≤ ‖Φ z‖ := (le_div_iff₀ hΨpos).mp hL
  have hmul := mul_le_mul_of_nonneg_left hstep hC.le
  rwa [← mul_assoc, mul_one_div, div_self hC.ne', one_mul] at hmul

end QOU.QBeta.FaddeevStripGrowthFKV
