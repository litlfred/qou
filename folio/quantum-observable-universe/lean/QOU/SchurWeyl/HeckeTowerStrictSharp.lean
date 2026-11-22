/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeInclInjective
import QOU.SchurWeyl.HeckeTowerStrict

/-!
# The sharp dimension of the tower image

Bean `qou-p8yg`, sharp half. `HeckeTowerStrict.heckeIncl_range_lt_top` shows the tower inclusion is
never onto using a dimension *inequality* and **no injectivity** — see that file, whose import list
is the evidence. This file consumes `heckeIncl_injective` to upgrade the inequality to the exact
value: the image of `H_m(q)` in `H_{m+1}(q)` has dimension exactly `(m+1)!`.

Split from `HeckeTowerStrict` deliberately. Keeping the two in one file would put
`heckeIncl_injective` in the import cone of the strictness statement and make the independence
claim unverifiable from the source; separating them lets the compiler carry it.

## Scope

`ℝ`, `q ≠ 0`, `NotRootOfUnity q` — inherited from `heckeIncl_injective`, whose step 2
(`compress_seminormalRep_heckeIncl`) is stated over `ℝ` with `qi = q⁻¹`. The strictness statement is
*not* confined to `ℝ`; only this sharpening is.

-- Ref: [leitner2026] beans qou-p8yg, qou-ejde.
-/

namespace QOU.SchurWeyl

open QOU.SchurWeyl.HeckeInclusion

/-- **The image has exactly the dimension of the level below.** This is where injectivity is
consumed: it upgrades the `≤` of `heckeIncl_range_lt_top` to an equality. -/
theorem finrank_range_heckeIncl {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Module.finrank ℝ (LinearMap.range (heckeIncl ℝ q q⁻¹ m).toLinearMap)
      = (m + 1).factorial := by
  haveI := finiteDimensional_hecke (K := ℝ) q q⁻¹ m
  rw [LinearMap.finrank_range_of_inj
      (f := (heckeIncl ℝ q q⁻¹ m).toLinearMap) (SeminormalRep.heckeIncl_injective hq0 hq2 m),
    finrank_hecke_eq_factorial q hq0 hq2 m]

end QOU.SchurWeyl
