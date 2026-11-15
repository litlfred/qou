/-
# The bar-even coefficient `g₂` is an **affine image of the measured binding**, magnified by `1/h²`

The deuteron bar-even binding coefficient is *defined* (Magnus/E_unit route, `#4158`,
`eunit_magnus_order2_probe.py`) as

```
g₂ = (E_AME / E⁺ − 1) / h²,   E⁺ = E_rot / (1 − t),
```

where `E_rot` (the first-order rotational energy `μ₀ ℏ_q [j]_q[j+1]_q`), the bar-odd impurity
`t = (v−v⁻¹)/[2]_v`, and `h = q−q⁻¹` are **pure theory** (functions of the substrate `q₀` alone),
and `E_AME` is the **measured** deuteron binding. The residual `r = g₂ − 1 ≈ +0.87%` is the object
the `g₂` chase tried to derive as a "geometric quantum-dilog amplitude."

This file makes precise, as an exact `Field` identity (§7c: generic `R`; the archimedean numbers are
downstream), the structural fact that ends that chase:

**`g₂` is an *affine* function of the measured binding `E_AME`**, with slope `1/(E⁺·h²)`. A *relative*
perturbation `δ` of the binding (`E_AME ↦ E_AME(1+δ)`) moves `g₂` by exactly `δ·E_AME/(E⁺·h²)` — the
**amplification factor** `E_AME/(E⁺·h²) ≈ 23.9` at `q₀`. Equivalently, to pin `r = g₂−1` to a relative
precision `ε` one must predict `E_AME` to `ε·r·h²·E⁺/E_AME` — numerically `≈ 36 ppm` for `ε = 10%`,
i.e. `~2500×` tighter than the framework's current first-order binding accuracy (`−9.21%`).

**Consequence.** `r` is not a special-function puzzle separable from the deuteron binding: deriving it
is *equivalent to* predicting `B(deuteron)` to `~36 ppm`. The `g₂ ≈ 1` leading term is genuinely
derived (`g2_leading = 1`, real coloring); the residual `r` is the still-open Δ_λ binding closure,
viewed through a `1/h²` magnifier — which is exactly why every categorical amplitude reproduces the
leading `1` but none pins `r`, and why fitting a single `~0.9%` (really `~36 ppm`) target is
information-starved (§2e).

This file does not derive `r`; it machine-checks the affine/amplification structure that reframes it.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.MassTheory.BindingResidual

variable {R : Type*} [Field R]

/-- The bar-even coefficient as a function of the (measured) binding `E`, given the pure-theory
frame energy `Ep = E⁺` and unit `h²` (`hsq`). Definition of `#4158`'s `g₂`. -/
def g2 (E Ep hsq : R) : R := (E / Ep - 1) / hsq

/-- **`g₂` is affine in the binding** `E`: `g₂ = E · (1/(Ep·hsq)) − 1/hsq`. The slope is
`1/(Ep·hsq)`; there is no higher-order dependence on `E`. -/
theorem g2_affine (E Ep hsq : R) (hEp : Ep ≠ 0) (hh : hsq ≠ 0) :
    g2 E Ep hsq = E * (1 / (Ep * hsq)) - 1 / hsq := by
  unfold g2
  field_simp

/-- **The amplification identity.** A *relative* perturbation `δ` of the measured binding
(`E ↦ E·(1+δ)`) shifts `g₂` by exactly `δ · E / (Ep · hsq)`. The coefficient
`E/(Ep·hsq)` is the amplification factor (`≈ 23.9` at `q₀`): the `1/h²` magnifies the binding's
relative error into `g₂`. -/
theorem g2_amplification (E Ep hsq δ : R) (hEp : Ep ≠ 0) (hh : hsq ≠ 0) :
    g2 (E * (1 + δ)) Ep hsq - g2 E Ep hsq = δ * E / (Ep * hsq) := by
  unfold g2
  field_simp
  ring

/-- **`r = g₂ − 1` inherits the same amplification** (subtracting the constant `1` does not change the
sensitivity): the residual moves by `δ·E/(Ep·hsq)` under a relative binding perturbation `δ`. So
resolving `r` to absolute precision `η` requires the binding to relative precision
`η·Ep·hsq/E`. -/
theorem r_amplification (E Ep hsq δ : R) (hEp : Ep ≠ 0) (hh : hsq ≠ 0) :
    (g2 (E * (1 + δ)) Ep hsq - 1) - (g2 E Ep hsq - 1) = δ * E / (Ep * hsq) := by
  rw [show (g2 (E * (1 + δ)) Ep hsq - 1) - (g2 E Ep hsq - 1)
        = g2 (E * (1 + δ)) Ep hsq - g2 E Ep hsq from by ring]
  exact g2_amplification E Ep hsq δ hEp hh

end QOU.MassTheory.BindingResidual
