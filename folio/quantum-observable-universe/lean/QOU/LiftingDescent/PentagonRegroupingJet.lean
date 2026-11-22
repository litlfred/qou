/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.Kaehler.Basic
import QOU.BraidKnot.PhiQTowerAlgebraicStratification

/-!
# The residual of pentagon ascension lives in a power of the diagonal ideal

`phi_q_tower_algebraic_stratification_of_regrouping` takes the residual subgroup `J`
as a parameter. This file fixes it using the first-order jet module adopted by
owner ruling 2026-11-22: `J¹(S) = (S ⊗ S) ⧸ I²`, with `I = ker (m : S ⊗ S → S)`
(`QOU.LiftingDescent.jetModule`, PR #9007). At jet order `k`, the residual
subgroup is `I^(k+1)`. For first order, `J = I²`, and the regrouping conclusion
says the mass equals the corrected low strata in `J¹(S)`.

The quotient is written out as `(S ⊗[R] S) ⧸ I ^ 2` rather than imported, so the
file does not depend on that PR. Its type is definitionally equal to `jetModule R S`.

Not proved here:
* that a stratum value lies in `S ⊗ S`, i.e. that `Φ_q(‖V̂_S‖_F)` is an element of
  the jet algebra;
* the hypothesis, i.e. that the `|S| ≥ 3` strata minus the correction lie in `I²`.
  That is pentagon ascension itself (bean `qou-hyqk`).
-/

namespace QOU.LiftingDescent

open TensorProduct QOU.BraidKnot

variable (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]

/-- **Stratification at jet order `k`.** If the level-≥3 strata, minus a correction
`δ` on the strata with `|S| ≤ 2`, lie in `I^(k+1)`, then the mass and the corrected
low strata agree in the `k`-th jet algebra `(S ⊗ S) ⧸ I^(k+1)`. -/
theorem stratification_in_jet_order (k : ℕ) (U : Finset ℕ) (f δ : Finset ℕ → S ⊗[R] S)
    (hreg : ∑ T ∈ U.powerset.filter (fun T => ¬ T.card ≤ 2), f T
        - ∑ T ∈ U.powerset.filter (fun T => T.card ≤ 2), δ T
        ∈ KaehlerDifferential.ideal R S ^ (k + 1)) :
    Ideal.Quotient.mk (KaehlerDifferential.ideal R S ^ (k + 1)) (∑ T ∈ U.powerset, f T)
      = Ideal.Quotient.mk (KaehlerDifferential.ideal R S ^ (k + 1))
          ((f ∅ + δ ∅) + ∑ T ∈ U.powersetCard 1, (f T + δ T)
            + ∑ T ∈ U.powersetCard 2, (f T + δ T)) := by
  rw [Ideal.Quotient.eq]
  exact phi_q_tower_algebraic_stratification_of_regrouping U f δ
    (KaehlerDifferential.ideal R S ^ (k + 1)).toAddSubgroup hreg

/-- **First-order case**: in `J¹(S) = (S ⊗ S) ⧸ I²`, the mass equals the corrected
strata with `|S| ≤ 2`, given that the regrouping residual lies in `I²`. -/
theorem stratification_in_first_jet (U : Finset ℕ) (f δ : Finset ℕ → S ⊗[R] S)
    (hreg : ∑ T ∈ U.powerset.filter (fun T => ¬ T.card ≤ 2), f T
        - ∑ T ∈ U.powerset.filter (fun T => T.card ≤ 2), δ T
        ∈ KaehlerDifferential.ideal R S ^ 2) :
    Ideal.Quotient.mk (KaehlerDifferential.ideal R S ^ 2) (∑ T ∈ U.powerset, f T)
      = Ideal.Quotient.mk (KaehlerDifferential.ideal R S ^ 2)
          ((f ∅ + δ ∅) + ∑ T ∈ U.powersetCard 1, (f T + δ T)
            + ∑ T ∈ U.powersetCard 2, (f T + δ T)) :=
  stratification_in_jet_order R S 1 U f δ hreg

/-- The jet filtration is monotone: a residual at jet order `k + 1` is also a
residual at order `k`. So the equality descends from `J^(k+1)` to `J^k`, and
down to order zero, where `I^1 = I` and the quotient is `S` via multiplication. -/
theorem jet_residual_mono (k : ℕ) :
    KaehlerDifferential.ideal R S ^ (k + 2) ≤ KaehlerDifferential.ideal R S ^ (k + 1) :=
  Ideal.pow_le_pow_right (by omega)

end QOU.LiftingDescent
