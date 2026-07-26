/-
  Figure-eight (4_1 = Higgs) Kashaev invariant and the volume-conjecture saddle.

  ⟨4_1⟩_N = Σ_{k=0}^{N-1} ∏_{j=1}^k (2 - 2·cos(2πj/N))     (real, root-of-unity)

  WHAT IS PROVABLE IN LEAN (sorry-free, below):
    * the object is well-defined and every term is ≥ 0 (cos ≤ 1);
    * ⟨4_1⟩_N ≥ 1 for N ≥ 1 (the k=0 empty product contributes 1) — the
      base fact that it does not vanish (a torus knot's Kashaev sum would not
      grow; this is the Lean-checkable floor of the "exponential growth → Vol"
      verification done numerically in figure_eight_kashaev_volume.py).

  CARRIED AS A CONDITIONAL CLASS (and, since 2026-07-26, DISCHARGED):
    * the asymptotic limit  lim_N (2π/N)·log⟨4_1⟩_N = Vol(4_1) = 2·Cl₂(π/3)
      is the Kashaev–Murakami–Murakami VOLUME CONJECTURE, proved for the
      figure-eight in the literature (Andersen–Hansen; Ohtsuki) and NOW ALSO
      machine-proved in-repo, sorry-free, by the saddle program's Riemann-sum
      squeeze (`FigureEightVolumeSqueeze.lean`, milestone qou-cpfn) — the
      class instance in `FigureEightVolumeLiterature.lean` carries the proof.
      It is the Re-face of the keystone (Re V(4_1)=Vol → m_μ/m_e). The
      Im-face CS(4_1)=0 is, by contrast, ELEMENTARY (amphichirality /
      self-duality) — see the bar-symmetry of the colored Jones in
      figure_eight_aj_operator.py.

  Archimedean (ℝ): uses Real.cos / Real.log (§7c — genuinely archimedean).

  -- Ref: [kashaev1997] https://doi.org/10.1007/BF01239527
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic
import QOU.Archimedean.ClausenFunctionMathlibFiller

namespace QOU.Knot.FigureEightVolume

open Real

/-- The k-fold Kashaev product ∏_{j=1}^k (2 - 2·cos(2πj/N)). -/
noncomputable def kashaevProd (N k : ℕ) : ℝ :=
  ∏ j ∈ Finset.Icc 1 k, (2 - 2 * Real.cos (2 * π * j / N))

/-- The figure-eight Kashaev invariant at the N-th root of unity. -/
noncomputable def kashaev (N : ℕ) : ℝ :=
  ∑ k ∈ Finset.range N, kashaevProd N k

/-- Each factor `2 - 2·cos x ≥ 0` (since `cos x ≤ 1`). -/
theorem factor_nonneg (x : ℝ) : 0 ≤ 2 - 2 * Real.cos x := by
  have h := Real.cos_le_one x; linarith

/-- The Kashaev product is non-negative. -/
theorem kashaevProd_nonneg (N k : ℕ) : 0 ≤ kashaevProd N k :=
  Finset.prod_nonneg (fun _ _ => factor_nonneg _)

/-- The empty (k = 0) product is 1. -/
@[simp] theorem kashaevProd_zero (N : ℕ) : kashaevProd N 0 = 1 := by
  simp [kashaevProd]

/-- **The Kashaev sum is ≥ 1 for N ≥ 1** — the non-vanishing floor (the k = 0
    term contributes 1; every other term is ≥ 0). A torus knot would have no
    such growth; this is the Lean-checkable base of "exponential growth ⇒
    nonzero volume rate". -/
theorem kashaev_ge_one (N : ℕ) (hN : 1 ≤ N) : 1 ≤ kashaev N := by
  have h0 : (0 : ℕ) ∈ Finset.range N := Finset.mem_range.mpr hN
  calc (1 : ℝ) = kashaevProd N 0 := (kashaevProd_zero N).symm
    _ ≤ ∑ k ∈ Finset.range N, kashaevProd N k :=
        Finset.single_le_sum (fun k _ => kashaevProd_nonneg N k) h0
    _ = kashaev N := rfl

/-- In particular the Kashaev sum is positive, so `log ⟨4_1⟩_N` is well-defined
    and non-negative for N ≥ 1. -/
theorem kashaev_pos (N : ℕ) (hN : 1 ≤ N) : 0 < kashaev N :=
  lt_of_lt_of_le one_pos (kashaev_ge_one N hN)

/-- The figure-eight hyperbolic volume constant, EXACT:
    `Vol(4_1) = 2·Cl₂(π/3) = 6·Λ(π/3) ≈ 2.0299` — twice the Clausen value at
    the Thurston ideal-tetrahedron angle (2 regular ideal tetrahedra of shape
    `e^{iπ/3}`, each of volume `Cl₂(π/3)`).

    STATEMENT-REPAIR NOTE (2026-07-26, bean qou-yf47). This was previously
    the truncated rational decimal `2.029883212819307250011597804990`, which
    differs from the transcendental `2·Cl₂(π/3)` by ≈ 1e-30 — making the
    conjectured limit `limit_eq_vol` AS THEN STATED mathematically false and
    undischargeable. The exact definition is the honest target of the
    E5 saddle/deviation program (`QOU/Knot/Clausen.lean` E5c bricks); the
    decimal is demoted to the approximation carrier `VOL_4_1_decimal`. -/
noncomputable def VOL_4_1 : ℝ := 2 * QOU.Archimedean.Cl_2 (π / 3)

/-- `VOL_4_1` agrees with the Clausen-filler volume carrier
    `Vol_figure_8 = 2·Cl₂(π/3)` definitionally. -/
theorem VOL_4_1_eq_vol_figure_8 : VOL_4_1 = QOU.Archimedean.Vol_figure_8 := rfl

/-- The 30-digit decimal approximation of `Vol(4_1)`, numerically witnessed by
    `computations/figure_eight_kashaev_volume.py`. This is an APPROXIMATION
    carrier only — `VOL_4_1 = 2·Cl₂(π/3)` is transcendental and differs from
    this rational by ≈ 1e-30; no formal identity between the two is claimed
    (that would need certified interval arithmetic on the `Cl₂` series). -/
noncomputable def VOL_4_1_decimal : ℝ := 2.029883212819307250011597804990

/-- **Volume conjecture for the figure-eight** (Kashaev–Murakami–Murakami),
    a PROVED theorem for `4_1` (Andersen–Hansen; Ohtsuki) whose saddle-point /
    Borel-resummation proof is not available in Mathlib. Carried as a §3b-cond
    conditional class: any downstream result may take `[VolumeConjecture41]`
    as an explicit hypothesis. Its single field is the limit identity — the
    Re-face of the keystone `Re V(4_1) = Vol(4_1) → m_μ/m_e`. -/
class VolumeConjecture41 : Prop where
  /-- (2π/N)·log ⟨4_1⟩_N → Vol(4_1) as N → ∞. -/
  limit_eq_vol :
    Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log (kashaev N))
      Filter.atTop (nhds VOL_4_1)

/-- Conditional on the (proved-in-the-literature) volume conjecture, the
    Kashaev root-of-unity saddle reproduces the figure-eight hyperbolic
    volume — the keystone Re-face, stated rigorously modulo the named class. -/
theorem saddle_eq_volume [h : VolumeConjecture41] :
    Filter.Tendsto (fun N : ℕ => (2 * π / (N : ℝ)) * Real.log (kashaev N))
      Filter.atTop (nhds VOL_4_1) :=
  h.limit_eq_vol

end QOU.Knot.FigureEightVolume
