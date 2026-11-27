/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.Kaehler.Basic
import BraidKnotOctonion.PhiQTowerAlgebraicStratification

/-!
# The residual of pentagon ascension lives in a power of the diagonal ideal

`phi_q_tower_algebraic_stratification_of_regrouping` takes the residual subgroup `J`
as a parameter. This file instantiates it with the jet module of order `k`,
`(S ⊗ S) ⧸ I^(k+1)` with `I = ker (m : S ⊗ S → S)`: the residual subgroup is
`I^(k+1)`. For `k = 1` this is the first jet module `J¹(S) = (S ⊗ S) ⧸ I²`, which is
`QOU.LiftingDescent.jetModule R S` in `JetModuleSplitting.lean`; the quotient is
written out here, and the two types are definitionally equal.

**The jet order `k` is not the brane-tower level `n`.** The tower iterates first
jets, and `J¹(J¹(S))` is not `(S ⊗ S) ⧸ I³`. So `I^(k+1)` is a residual at jet
order `k` inside one jet module. It is not the tower-level residual `J_{n+1}` of
`prop:phi-q-tower-algebraic-stratification`. Which submodule that is remains open.

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


/-! ### Scalar strata

`Φ_q(‖V̂_S‖_F)` is a scalar: the Frobenius norm takes values in the ground ring `R`,
and so does every truncation of `Φ_q` (`QOU.BraidKnot.phiQTrunc`). The obvious way to
place a stratum in `S ⊗ S` is `algebraMap R (S ⊗ S)`. When `R → S` is injective, a
scalar lies in `I` only if it is zero. So for scalar strata, "the residual lies in
`I^(k+1)`" is the same as "the residual is zero". The jet residual adds nothing
over the vanishing form. Its content needs strata that are not scalars.
-/

/-- A scalar lies in the diagonal ideal `I = ker m` only if it is zero, when
`R → S` is injective. -/
theorem algebraMap_mem_kaehlerIdeal_iff (hinj : Function.Injective (algebraMap R S))
    (r : R) : algebraMap R (S ⊗[R] S) r ∈ KaehlerDifferential.ideal R S ↔ r = 0 := by
  rw [KaehlerDifferential.ideal, RingHom.mem_ker, AlgHom.commutes]
  constructor
  · intro h; exact hinj (by rw [h, map_zero])
  · rintro rfl; exact map_zero _

/-- **Scalar strata collapse the jet residual to the vanishing form.** If every
stratum and every correction is a scalar (the image of `R`), and `R → S` is
injective, then the regrouping hypothesis at any jet order `k` holds iff the
level-≥3 scalar sum equals the scalar correction sum exactly. -/
theorem scalar_regrouping_iff (hinj : Function.Injective (algebraMap R S)) (k : ℕ)
    (U : Finset ℕ) (g d : Finset ℕ → R) :
    (∑ T ∈ U.powerset.filter (fun T => ¬ T.card ≤ 2), algebraMap R (S ⊗[R] S) (g T)
        - ∑ T ∈ U.powerset.filter (fun T => T.card ≤ 2), algebraMap R (S ⊗[R] S) (d T)
        ∈ KaehlerDifferential.ideal R S ^ (k + 1))
      ↔ ∑ T ∈ U.powerset.filter (fun T => ¬ T.card ≤ 2), g T
          = ∑ T ∈ U.powerset.filter (fun T => T.card ≤ 2), d T := by
  simp only [← map_sum, ← map_sub]
  constructor
  · intro h
    have h1 := (algebraMap_mem_kaehlerIdeal_iff R S hinj _).mp
      (Ideal.pow_le_self (Nat.succ_ne_zero k) h)
    exact sub_eq_zero.mp h1
  · intro h
    rw [h, sub_self, map_zero]
    exact Ideal.zero_mem _

end QOU.LiftingDescent
