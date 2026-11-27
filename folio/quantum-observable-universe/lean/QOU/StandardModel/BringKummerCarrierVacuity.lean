/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under CC BY 4.0 as described in the repository LICENSE.
-/
import QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant

/-!
# The `qou-txc1` part (c) carrier is satisfied by a constant

Bean `qou-txc1`.  `BringKummerSU5EmbeddingHypothesis K` is documented as a zero-instance
Rule-13a carrier for "the degree-3 Kummer pushforward `W₃ = π_* 𝓛` on Bring's curve produces
the block embedding `S(U(3) × U(2)) ↪ SU(5)` with `α² = 1/36`".  Its fields mention neither
Bring's curve nor the pushforward: they ask for a scalar `α` with `α² = 1/36` and the `3/8`
trace ratio at `α`, which `traceRatio_5bar_oplus_10_eq_three_eighths_iff` already supplies at
`α = 1/6`.  `bringKummerCarrier_satisfied` builds the term (a `def`, **not** an `instance`), so
the class records no open content.

What part (c) actually asks is that Bring's curve supplies the flavour fundamental `W`
(`Λ³W ≅ 𝟙`, not self-dual) of `FlavouredQuantumObservableUniverse`, which that structure
currently postulates (bean `qou-j3w6`).  Given `V` and `W`, the embedding `S(U(V) × U(W*))` in
`SU(V ⊕ W*)` and its one-dimensional commutant are automatic (`HyperchargeUniqueness`), and
`α = ± 1/6` follows from one neutral lepton (`NeutralLeptonFixesCharges`,
`AnomalyFreeHyperchargeUniqueness`).

Caution from the χ = −6 thread (2026-11-27): on Bring's curve `H¹(M₀) ⊗ ℂ = 2W₄` with `W₄` the
irreducible 4-dimensional `A₅`-representation, and `A₅` has no 2-dimensional irreducible, so no
`A₅`-equivariant `3 ⊕ 2` splitting comes from `H¹`.
-/

namespace QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant

/-- The part (c) carrier is satisfied by the constant `α = 1/6`. -/
noncomputable def bringKummerCarrier_satisfied (K : Type*) [Field K] [CharZero K] :
    BringKummerSU5EmbeddingHypothesis K where
  commutantScale := 1 / 6
  commutantScale_sq := by norm_num
  traceRatio_eq_three_eighths := by
    rw [traceRatio_5bar_oplus_10_eq_three_eighths_iff]
    · norm_num
    · norm_num

end QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant
