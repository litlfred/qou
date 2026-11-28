/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MassTheory.EmPhotonPairWeights

/-!
# Candidate rules for joining two photon vertices (bean `qou-l4t2`)

A two-loop vertex pair is two photon vertices `v`, `w` on one fermion loop. Each
vertex is a convention-D generator `σ` (`σ² = hσ + 1`) with bar image `σ⁻¹`. This
module evaluates four candidate joining rules, none of which is adopted here:

| rule | join of `v`, `w` | at one position | at two positions |
|---|---|---|---|
| plain product | `v w` | `hσ + 1` (`plain_same`) | `στ` |
| bar-Hermitian | `v̄ w` | `1` (`barHerm_same`) | `σ⁻¹τ` |
| bar-even | `(v + v̄)(w + w̄)` | `[2]_q² = 4 + h²` | `(2σ − h)(2τ − h)` (`barEven_eq`) |
| bar-odd, signed | `−(v − v̄)(w − w̄)` | `−h²` | `−h²` (`barOdd_eq`) |

The bar-odd rule is Form B's four-topology sum (`barOdd_eq_vertexPair`). The bar-even
rule, less the singlet, is the θ-graph's `[3]_q`.

`barOdd_eq` holds at **any** two positions, so only that rule gives a scalar there.
The other three depend on the positions; their moments depend on the moment data
`m(σ)`, `m(τ)`, `m(στ)`, and so on (`barEven_expand` writes the bar-even one out).
That is a structural reason the skein chain (`vertexPair_chain`,
`moment_vertexPair_chain`) exists only for the bar-odd rule. It is not a proof that
the bar-odd rule is the physical one. No measured value enters this file.
-/

set_option autoImplicit false

namespace QOU.MassTheory
namespace EmPhotonJoinRules

open EmVertexPairScalarChain EmThetaClassicalThree

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Plain product at one position: `σσ = hσ + 1`. -/
theorem plain_same {h : R} (g : HeckeGen (A := A) h) :
    g.σ * g.σ = algebraMap R A h * g.σ + 1 := by
  rw [← pow_two]; exact g.quad

/-- Bar-Hermitian join at one position: `σ⁻¹σ = 1`. -/
theorem barHerm_same {h : R} (g : HeckeGen (A := A) h) : g.σinv * g.σ = 1 := g.inv_mul

/-- Bar-even join at any two positions: `(σ + σ⁻¹)(τ + τ⁻¹) = (2σ − h)(2τ − h)`. -/
theorem barEven_eq {h : R} (g g' : HeckeGen (A := A) h) :
    (g.σ + g.σinv) * (g'.σ + g'.σinv)
      = (2 * g.σ - algebraMap R A h) * (2 * g'.σ - algebraMap R A h) := by
  rw [sum_eq_two_sigma_sub, sum_eq_two_sigma_sub]

/-- The bar-even join written out: `4στ − 2h(σ + τ) + h²`. -/
theorem barEven_expand {h : R} (g g' : HeckeGen (A := A) h) :
    (g.σ + g.σinv) * (g'.σ + g'.σinv)
      = 4 * (g.σ * g'.σ) - 2 * (algebraMap R A h * (g.σ + g'.σ))
          + algebraMap R A (h ^ 2) := by
  rw [barEven_eq]
  have hc : Commute (algebraMap R A h) g.σ := Algebra.commutes h g.σ
  calc (2 * g.σ - algebraMap R A h) * (2 * g'.σ - algebraMap R A h)
      = 4 * (g.σ * g'.σ) - 2 * (g.σ * algebraMap R A h)
          - 2 * (algebraMap R A h * g'.σ) + algebraMap R A h * algebraMap R A h := by
        noncomm_ring
    _ = _ := by rw [← hc.eq, map_pow, pow_two]; noncomm_ring

/-- Bar-even join at one position: `[2]_q² = 4 + h²`. -/
theorem barEven_same {h : R} (g : HeckeGen (A := A) h) :
    (g.σ + g.σinv) * (g.σ + g.σinv) = algebraMap R A (4 + h ^ 2) := by
  rw [← unsignedPair_eq_two_sq g]; unfold unsignedPair; noncomm_ring

/-- The signed bar-odd join is Form B's four-topology vertex pair. -/
theorem barOdd_eq_vertexPair {h : R} (g g' : HeckeGen (A := A) h) :
    -((g.σ - g.σinv) * (g'.σ - g'.σinv)) = vertexPair g g' := by
  unfold vertexPair; rw [four_topology_eq_neg_skein_product]

/-- The signed bar-odd join is `−h²` at any two positions. -/
theorem barOdd_eq {h : R} (g g' : HeckeGen (A := A) h) :
    -((g.σ - g.σinv) * (g'.σ - g'.σinv)) = algebraMap R A (-h ^ 2) := by
  rw [barOdd_eq_vertexPair, vertexPair_eq_neg_hsq]

end EmPhotonJoinRules
end QOU.MassTheory
