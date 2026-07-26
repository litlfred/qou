/-
  Figure-eight volume conjecture — the instance, now MACHINE-PROVED
  (2026-07-26, bean qou-f248; formerly G1 of the 2026-07-12 Borel/alien-
  calculus utilization audit).

  `QOU.Knot.FigureEightVolume` carries the 4₁ volume conjecture as the
  conditional class `VolumeConjecture41`. This file HISTORICALLY supplied the
  Andersen–Hansen / Ohtsuki literature result as a CITED `sorry` instance;
  as of 2026-07-26 the `sorry` is DISCHARGED: the saddle program (bricks
  E1–E5d, milestone qou-cpfn) proves the limit outright as
  `tendsto_log_kashaev_vol` in `FigureEightVolumeSqueeze.lean` — an
  elementary Riemann-sum squeeze against the Clausen primitive, with the
  exact transcendental target `VOL_4_1 = 2·Cl₂(π/3)` (qou-yf47 repair).
  The instance below is now a genuine sorry-free Lean proof; downstream
  `[VolumeConjecture41]`-conditional results are unconditional in-repo.

  Also here: the well-definedness glue (`log_kashaev_nonneg`) making the
  sequence in the limit statement non-negative from the `kashaev_ge_one`
  floor.

  Archimedean (ℝ): inherits Real.log / Real.cos from FigureEightVolume (§7c).

  -- Ref: [andersen-hansen2006] https://doi.org/10.1142/S0218216506004555
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import QOU.Knot.FigureEightVolumeSqueeze

namespace QOU.Knot.FigureEightVolume

open Real

/-- `log ⟨4₁⟩_N ≥ 0` for `N ≥ 1` — sorry-free glue from the `kashaev_ge_one`
    floor: the sequence whose limit the volume conjecture asserts is
    non-negative termwise. -/
theorem log_kashaev_nonneg (N : ℕ) (hN : 1 ≤ N) : 0 ≤ Real.log (kashaev N) :=
  Real.log_nonneg (kashaev_ge_one N hN)

/-- **The figure-eight volume conjecture, machine-proved** (Kashaev–Murakami–
    Murakami statement for `4₁`; proved in the literature by Andersen–Hansen /
    Ohtsuki, and proved HERE, sorry-free, by the saddle program's Riemann-sum
    squeeze `tendsto_log_kashaev_vol` — `FigureEightVolumeSqueeze.lean`).

    HISTORY. Until 2026-07-26 this instance was a cited `sorry` (the
    established-in-the-literature encoding), with two obstructions: (a) the
    saddle asymptotic was unformalized, and (b) `VOL_4_1` was a truncated
    rational decimal ≈ 1e-30 away from `2·Cl₂(π/3)`, making the statement
    literally false. (b) was repaired by bean qou-yf47 (exact
    `VOL_4_1 = 2·Cl₂(π/3)`); (a) was closed by bricks E1–E5d (milestone
    qou-cpfn): E5a log-bridge, E4/E5c Riemann-sum-vs-Clausen deviation with
    k-uniform master error `E(N) → 0`, the E2/E3 Cl₂ extremum at `5π/3`, and
    the E5d two-envelope squeeze. No Borel resummation was needed — the
    root-of-unity Kashaev sum for `4₁` admits this elementary route. -/
instance volumeConjecture41_of_literature : VolumeConjecture41 :=
  ⟨tendsto_log_kashaev_vol⟩

/-- The keystone Re-face, now fully unconditional and sorry-free: the Kashaev
    root-of-unity saddle reproduces the figure-eight hyperbolic volume. -/
theorem kashaev_saddle_volume :
    Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log (kashaev N))
      Filter.atTop (nhds VOL_4_1) :=
  saddle_eq_volume

end QOU.Knot.FigureEightVolume
