/-
Copyright (c) 2026 litlfred. All rights reserved.

# Constructing `FaddeevPhiStripGrowth` from the FKV eq-22 compact bound

Capstone of the Faddeev–Volkov A_ω uniqueness leg's strip-growth input. On main,
`FaddeevPhiStripGrowth b Φ` (the "`Φ` is comparable in modulus to `phiBProd`"
class) is consumed by the uniqueness capstone
(`FaddeevStripGrowthUniqueness.faddeevPhi_proportional_of_stripGrowth`), but for a
*second* solution it is carried as an **opaque axiom** — the physical
Faddeev–Kashaev asymptotic content that the shift equations alone do not pin
(elliptic freedom).

This file removes the opacity: it exhibits a **constructor** that *derives* the
class from three **named, literature-pinned** inputs, rather than assuming it
wholesale. It composes the box-reduction chain now fully on main:

```
FKV eq 22 (compact-domain two-sided ratio bound, hballU/hballL)  ─┐
ratio Φ/phiBProd periodic under ⟨ib, i/b⟩ (hper; on main:         ├─ #4431
  CyclicDilogPentagon.ratio_ib/ibinv_periodic give this)         ─┘  comparable_shape_of_periodic_ballBound
                                                                         │  (off phiBProd's zeros)
same divisor: Φ vanishes where phiBProd does (hDiv)  ────────────────────┤  (at phiBProd's zeros)
                                                                         ▼
                                              FaddeevPhiStripGrowth b Φ
```

**Scope (reduction, not closure).** The three hypotheses are exactly the physical
inputs (FKV eq-22 + the same-divisor matching); they remain *axioms for a second
solution*. What changes is that `FaddeevPhiStripGrowth` is no longer an opaque
black box — it is now
`strip-growth ⟸ (FKV compact ratio bound) + periodicity + same-divisor`, each a
cited or on-`main`-shaped input. This is the honest strengthening: the opaque
class field becomes a derivation from more primitive, literature-backed pieces.
No fit; nothing wired; the leg stays *stated*-conditional (per
"conditional-proved ≠ premise-established"). Uses only on-`main`
`FaddeevStripGrowthFKV` (hence #4424 box reduction) + `FaddeevPhiStripGrowth`.
Sorry-free.

-- Ref: [faddeev-kashaev-volkov2000] https://arxiv.org/abs/hep-th/0006156 (§6, eqs 21-22)
-/
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.LinearAlgebra.Basis.Basic
import QOU.QBeta.FaddeevStripGrowthFKV
import QOU.QBeta.FaddeevPhiStripGrowth

namespace QOU.QBeta.FaddeevStripGrowthConstructor

open Module
open QOU.MathlibExt.PhiBProd

/-- **`FaddeevPhiStripGrowth` from the FKV eq-22 compact bound + same-divisor.**
Given
* `hper` — the ratio `Φ/phiBProd` is periodic under both vectors of an `ℝ`-basis
  `bas` of `ℂ` (the shift-prefactor cancellation; on main
  `CyclicDilogPentagon.ratio_ib_periodic` / `ratio_ibinv_periodic`),
* `hballU`, `hballL` — the two-sided FKV eq-22 ratio bound on the closed
  fundamental ball (`‖Φ/phiBProd‖ ≤ C` and `1/C ≤ ‖Φ/phiBProd‖`),
* `hDiv` — the same-divisor input in the direction that matters here: `Φ`
  vanishes wherever `phiBProd b` does,

the class `FaddeevPhiStripGrowth b Φ` holds. Off `phiBProd`'s zeros the bound is
`FaddeevStripGrowthFKV.comparable_shape_of_periodic_ballBound` (via the #4424 box
reduction); at a zero `z` both sides collapse to `0` using `hDiv`. This *derives*
the previously-opaque strip-growth axiom from three literature-pinned inputs. -/
theorem stripGrowth_of_periodic_fkvBound {b : ℂ} {Φ : ℂ → ℂ}
    {bas : Basis (Fin 2) ℝ ℂ} {C : ℝ} (hC : 0 < C)
    (hper : ∀ (i : Fin 2) (z : ℂ),
      (Φ (z + bas i) / phiBProd b (z + bas i)) = Φ z / phiBProd b z)
    (hballU : ∀ w : ℂ, ‖w‖ ≤ ‖bas 0‖ + ‖bas 1‖ → ‖Φ w / phiBProd b w‖ ≤ C)
    (hballL : ∀ w : ℂ, ‖w‖ ≤ ‖bas 0‖ + ‖bas 1‖ → 1 / C ≤ ‖Φ w / phiBProd b w‖)
    (hDiv : ∀ z : ℂ, phiBProd b z = 0 → Φ z = 0) :
    FaddeevPhiStripGrowth b Φ := by
  refine ⟨C, hC, fun z => ?_⟩
  by_cases hz : phiBProd b z = 0
  · -- at a zero of `phiBProd`, `Φ z = 0` too (same divisor); both bounds are `0 ≤ 0`.
    rw [hz, hDiv z hz]
    simp
  · -- off the zeros, this is exactly the #4431 converter (which runs the #4424 box
    -- reduction on the FKV compact bound).
    exact FaddeevStripGrowthFKV.comparable_shape_of_periodic_ballBound
      hC hper hballU hballL hz

end QOU.QBeta.FaddeevStripGrowthConstructor
