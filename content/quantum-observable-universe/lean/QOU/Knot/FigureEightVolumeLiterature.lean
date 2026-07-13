/-
  Figure-eight volume conjecture — the literature instance (G1 of the
  2026-07-12 Borel/alien-calculus utilization audit).

  `QOU.Knot.FigureEightVolume` carries the 4₁ volume conjecture as the
  conditional class `VolumeConjecture41` and its own header records that the
  statement is PROVED in the literature (Andersen–Hansen; Ohtsuki) by a
  saddle-point / Borel-resummation analysis not available in Mathlib. This
  file supplies that literature result as a CITED instance, so downstream
  `[VolumeConjecture41]`-conditional results fire — honestly: the `sorry`
  below is the queued Borel-resummation formalization (bean el8w /
  `QOU.Mathlib.Borel`), NOT an open mathematical question. Per the
  anti-laundering rule this is a citation, not a Lean proof; the derived
  status is `has_sorry` with a published reference, the repo's standard
  encoding of an established-in-the-literature theorem.

  Sorry-free content in this file: the well-definedness glue
  (`log_kashaev_nonneg`) making the sequence in the limit statement
  non-negative from the `kashaev_ge_one` floor.

  Archimedean (ℝ): inherits Real.log / Real.cos from FigureEightVolume (§7c).

  -- Ref: [andersen-hansen2006] https://doi.org/10.1142/S0218216506004555
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import QOU.Knot.FigureEightVolume

namespace QOU.Knot.FigureEightVolume

open Real

/-- `log ⟨4₁⟩_N ≥ 0` for `N ≥ 1` — sorry-free glue from the `kashaev_ge_one`
    floor: the sequence whose limit the volume conjecture asserts is
    non-negative termwise. -/
theorem log_kashaev_nonneg (N : ℕ) (hN : 1 ≤ N) : 0 ≤ Real.log (kashaev N) :=
  Real.log_nonneg (kashaev_ge_one N hN)

/-- **The literature instance of the figure-eight volume conjecture**
    (Kashaev–Murakami–Murakami statement; proved for `4₁` — Andersen–Hansen,
    Ohtsuki — via saddle-point / Borel-resummation analysis).

    STATUS (2026-07-13). The Borel-resummation UNIQUENESS half of that analysis
    is now formalized sorry-free in `QOU.Mathlib.Borel` (bean el8w): the
    Watson / Nevanlinna–Sokal theorem `watson_uniqueness_rhp_open` (open right
    half-plane) and `watson_uniqueness_sector` (sector-at-0), built on the
    Gevrey-1 ⇒ Borel-disc convergence and the regularity `borelSum_eq_tsum`.
    That engine does NOT by itself close the `sorry` below: `limit_eq_vol` is a
    concrete saddle-point ASYMPTOTIC of the explicit Kashaev sum — its EXISTENCE
    and VALUE (growth rate `= Vol(4₁)`) are the load-bearing Andersen–Hansen /
    Ohtsuki content, of which uniqueness is only one ingredient. So the `sorry`
    remains the cited established-in-the-literature theorem (per the
    anti-laundering rule a citation, not a Lean proof); wiring the general
    uniqueness engine to this specific series' saddle-point evaluation is a
    separate open formalization item, not an automatic consequence. Downstream
    results conditional on `[VolumeConjecture41]` remain conditional on this
    single cited declaration. -/
instance volumeConjecture41_of_literature : VolumeConjecture41 := by
  constructor
  -- Ref: [andersen-hansen2006] https://doi.org/10.1142/S0218216506004555
  sorry

/-- The keystone Re-face, now unconditional modulo the cited literature
    instance: the Kashaev root-of-unity saddle reproduces the figure-eight
    hyperbolic volume. -/
theorem kashaev_saddle_volume :
    Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log (kashaev N))
      Filter.atTop (nhds VOL_4_1) :=
  saddle_eq_volume

end QOU.Knot.FigureEightVolume
