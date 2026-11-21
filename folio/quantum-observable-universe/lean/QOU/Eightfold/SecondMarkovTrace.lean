/-
  A second Markov trace at rank 3, beside convention D.

  Owner decision (2026-11-15, issue #7895): keep convention D (rank 2) for mass
  and add a second Markov trace at rank N = 3 on the same Hecke tower for colour
  and flavour.  `OcneanuRankFamily.markovParam_three` specified the rank-3
  Markov parameter and said "nothing here builds such a trace".  This file
  builds it at the level of the `MarkovTraceTower` abstraction, for every rank:

  * `towerAtRank N` — a `MarkovTraceTower q` with `z = z_N` and Hopf trace
    `tr(σ₁²) = h·z_N + 1` (the Markov axiom applied to `σ² = hσ + 1`).
  * `towerAtRank_two_eq_canonical` — at `N = 2` it IS the production instance
    `markovTraceTower_canonical` (convention D), field by field.
  * `colourTower` — the rank-3 member: `z = q⁵/(q⁴+q²+1)`, Hopf trace
    `(q⁶+q²+1)/(q⁴+q²+1)`.
  * `colour_ne_mass` — the two traces are different (rank is recoverable from
    `z`), so the second trace is genuinely a second trace, not a retuning.
  * `TwoTraces` — the pair (mass, colour) on the same `q`, the shape the
    eightfold chapter needs.  The colour member carries the alternating
    channel: `weylDimAlt 3 = 1`, while `weylDimAlt 2 = 0`.

  The towers are `def`s, not instances, so two of them can live on the same
  `q` without a typeclass clash.  This is a construction at the level of the
  abstraction (z and the Hopf trace); the full rank-3 trace on every `H_n`
  element is the weights of `computations/y_lambda_su_n.py` at `N = 3`, which
  this file does not re-derive.
-/
import QOU.Braiding.HnMarkovTrace
import QOU.Eightfold.OcneanuRankFamily
import QOU.Eightfold.RowCapObstruction

namespace QOU.Eightfold.SecondMarkovTrace

open QOU.Braiding QOU.Eightfold.OcneanuRankFamily

/-- The rank-`N` Markov-trace tower: Markov parameter `z_N`, Hopf trace
`h·z_N + 1`. -/
noncomputable def towerAtRank (q : ℝ) (hq : 1 < q) (N : ℕ) (hN : 1 ≤ N) :
    MarkovTraceTower q where
  z := markovParam N q
  z_pos := lt_trans (heckeCoeff_pos hq) (markovParam_gt_hecke hq hN)
  trM_sigma1_sq := fun _ => heckeCoeff q * markovParam N q + 1
  trM_sigma1_sq_stabilises := fun _ _ _ _ => rfl

/-- **At rank 2 the tower is convention D**, i.e. the production instance. -/
theorem towerAtRank_two_eq_canonical (q : ℝ) (hq : 1 < q) :
    towerAtRank q hq 2 (by norm_num) = markovTraceTower_canonical q hq := by
  have h0 : q ≠ 0 := q_ne_zero hq
  have hs : q ^ 2 + 1 ≠ 0 := by positivity
  have hz := markovParam_two hq
  have htr : heckeCoeff q * markovParam 2 q + 1 = (q ^ 4 + 1) / (q ^ 2 + 1) := by
    rw [hz, heckeCoeff]
    field_simp
    ring
  unfold towerAtRank markovTraceTower_canonical
  congr 1
  funext _
  exact htr

/-- The colour tower: the rank-3 member. -/
noncomputable def colourTower (q : ℝ) (hq : 1 < q) : MarkovTraceTower q :=
  towerAtRank q hq 3 (by norm_num)

theorem colourTower_z (q : ℝ) (hq : 1 < q) :
    (colourTower q hq).z = q ^ 5 / (q ^ 4 + q ^ 2 + 1) :=
  markovParam_three hq

/-- The colour tower's Hopf trace `tr(σ₁²) = (q⁶+q²+1)/(q⁴+q²+1)`. -/
theorem colourTower_hopf (q : ℝ) (hq : 1 < q) (n : ℕ) :
    (colourTower q hq).trM_sigma1_sq n = (q ^ 6 + q ^ 2 + 1) / (q ^ 4 + q ^ 2 + 1) := by
  have h0 : q ≠ 0 := q_ne_zero hq
  have hs : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  show heckeCoeff q * markovParam 3 q + 1 = _
  rw [markovParam_three hq, heckeCoeff]
  field_simp
  ring

/-- **The colour trace is not the mass trace**: their Markov parameters differ. -/
theorem colour_ne_mass (q : ℝ) (hq : 1 < q) :
    (colourTower q hq).z ≠ (markovTraceTower_canonical q hq).z := by
  intro h
  have h2 : (markovTraceTower_canonical q hq).z = markovParam 2 q :=
    (markovParam_two hq).symm
  have := markovParam_injective hq (by norm_num : 1 ≤ 3) (by norm_num : 1 ≤ 2)
    (h.trans h2)
  omega

/-- **Two traces on one tower**: mass (convention D) and colour (rank 3). -/
structure TwoTraces (q : ℝ) where
  mass : MarkovTraceTower q
  colour : MarkovTraceTower q
  distinct : colour.z ≠ mass.z

/-- The pair the owner chose: D for mass, rank 3 for colour. -/
noncomputable def massAndColour (q : ℝ) (hq : 1 < q) : TwoTraces q where
  mass := markovTraceTower_canonical q hq
  colour := colourTower q hq
  distinct := colour_ne_mass q hq

/-- The colour member is the one that carries the alternating channel
`Λ³(ℂ^N)`: one-dimensional at `N = 3`, absent at `N = 2`. -/
theorem alternating_channel_rank :
    QOU.Eightfold.RowCapObstruction.weylDimAlt 3 = 1 ∧
      QOU.Eightfold.RowCapObstruction.weylDimAlt 2 = 0 := by
  decide

end QOU.Eightfold.SecondMarkovTrace
