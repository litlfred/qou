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

  ALGEBRAIC SOURCE (bean qou-28qh, phase 3): `kashaev N` is DEFINED as the
  archimedean reading of the single Habiro element
  `QCalculus.HabiroSeries.figureEight ∈ ℤ̂[q]` (= Σ_n (q;q)_n (q⁻¹;q⁻¹)_n),
  evaluated by the ring map `evalRoot` at `ζ_N = exp(2πi/N)`. Everything that
  does not need the embedding into ℂ (truncation, bar invariance, the
  per-N polynomial of TarskiSignKashaev, the q = 1 + h expansion) is proved
  about the Habiro element. The only transcendental input here is
  `ζ^j + ζ^{-j} = 2 cos(2πj/N)` (`kashaev_factor_eq`), which gives the
  cosine form `kashaev_eq_sum` used by the saddle program.

  -- Ref: [kashaev1997] https://doi.org/10.1007/BF01239527
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic
import MathlibExt.ClausenFunctionMathlibFiller
import QCalculus.HabiroCyclotomicSeries
import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots
import Mathlib.RingTheory.RootsOfUnity.Complex

namespace QOU.Knot.FigureEightVolume

open Real

/-- The k-fold Kashaev product ∏_{j=1}^k (2 - 2·cos(2πj/N)). -/
noncomputable def kashaevProd (N k : ℕ) : ℝ :=
  ∏ j ∈ Finset.Icc 1 k, (2 - 2 * Real.cos (2 * π * j / N))

/-! ### The Kashaev invariant as the archimedean reading of a Habiro element -/

section HabiroReading

open Polynomial Complex QCalculus.HabiroSeries

/-- `ζ_N = exp(2πi/N)`. -/
noncomputable def kashaevRoot (N : ℕ) : ℂ := Complex.exp (2 * Real.pi * I / N)

theorem aeval_kashaevRoot_cyclotomic {N : ℕ} (hN : N ≠ 0) :
    aeval (kashaevRoot N) (cyclotomic N ℤ) = 0 := by
  have h := (Complex.isPrimitiveRoot_exp N hN).isRoot_cyclotomic (Nat.pos_of_ne_zero hN)
  simpa [aeval_def, eval₂_eq_eval_map, IsRoot.def] using h

/-- One factor: `(1 - ζ^{-j})(1 - ζ^j) = 2 - 2 cos(2πj/N)`. -/
theorem kashaev_factor_eq (N j : ℕ) :
    (1 - (kashaevRoot N)⁻¹ ^ j) * (1 - kashaevRoot N ^ j) =
      ((2 - 2 * Real.cos (2 * Real.pi * j / N) : ℝ) : ℂ) := by
  have hj : kashaevRoot N ^ j = Complex.exp ((2 * Real.pi * j / N : ℝ) * I) := by
    rw [kashaevRoot, ← Complex.exp_nat_mul]; congr 1; push_cast; ring
  have hji : (kashaevRoot N)⁻¹ ^ j = Complex.exp (-(2 * Real.pi * j / N : ℝ) * I) := by
    rw [inv_pow, hj, ← Complex.exp_neg]; congr 1; ring
  have hprod : kashaevRoot N ^ j * (kashaevRoot N)⁻¹ ^ j = 1 := by
    rw [hj, hji, ← Complex.exp_add]; simp
  push_cast at hj hji ⊢
  rw [Complex.two_cos, ← hj, ← hji]
  linear_combination hprod

/-- The value of the Habiro element `figureEight` at `ζ_N` is the real cosine sum. -/
theorem evalRoot_figureEight_eq_sum {N : ℕ} (hN : N ≠ 0) :
    evalRoot hN (kashaevRoot N) (aeval_kashaevRoot_cyclotomic hN) (figureEight (R := ℤ)) =
      ((∑ k ∈ Finset.range N, kashaevProd N k : ℝ) : ℂ) := by
  rw [evalRoot_figureEight_field]
  push_cast
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [kashaevProd, poch, poch, ← Finset.prod_mul_distrib]
  push_cast
  have hIcc : Finset.Icc 1 k = Finset.Ico 1 (k + 1) := rfl
  rw [hIcc, Finset.prod_Ico_eq_prod_range, Nat.add_sub_cancel]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [kashaev_factor_eq]
  push_cast
  rw [add_comm (1 : ℂ) (i : ℂ)]

/-- **The figure-eight Kashaev invariant** `⟨4₁⟩_N`: the real part of the Habiro
    element `figureEight` evaluated at `ζ_N = exp(2πi/N)` (and `0` at `N = 0`). -/
noncomputable def kashaev (N : ℕ) : ℝ :=
  if hN : N = 0 then 0
  else (evalRoot hN (kashaevRoot N) (aeval_kashaevRoot_cyclotomic hN)
    (figureEight (R := ℤ))).re

/-- The cosine form `⟨4₁⟩_N = Σ_{k<N} ∏_{j=1}^{k} (2 - 2 cos(2πj/N))`. -/
theorem kashaev_eq_sum (N : ℕ) : kashaev N = ∑ k ∈ Finset.range N, kashaevProd N k := by
  by_cases hN : N = 0
  · subst hN; simp [kashaev]
  · rw [kashaev, dif_neg hN, evalRoot_figureEight_eq_sum hN, Complex.ofReal_re]

/-- The Habiro value is real and equals `⟨4₁⟩_N`. -/
theorem kashaev_eq_evalRoot {N : ℕ} (hN : N ≠ 0) :
    ((kashaev N : ℝ) : ℂ) =
      evalRoot hN (kashaevRoot N) (aeval_kashaevRoot_cyclotomic hN) (figureEight (R := ℤ)) := by
  rw [kashaev_eq_sum, evalRoot_figureEight_eq_sum hN]

end HabiroReading

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
    _ = kashaev N := (kashaev_eq_sum N).symm

/-- In particular the Kashaev sum is positive, so `log ⟨4_1⟩_N` is well-defined
    and non-negative for N ≥ 1. -/
theorem kashaev_pos (N : ℕ) (hN : 1 ≤ N) : 0 < kashaev N :=
  lt_of_lt_of_le one_pos (kashaev_ge_one N hN)

/-- The figure-eight hyperbolic volume constant, EXACT:
    `Vol(4_1) = 2·Cl₂(π/3) = 6·Λ(π/3) ≈ 2.0299` — twice the Clausen value at
    the Thurston ideal-tetrahedron angle (2 regular ideal tetrahedra of shape
    `e^{iπ/3}`, each of volume `Cl₂(π/3)`).

    STATEMENT-REPAIR NOTE (2026-07-26, bean qou-yf47). This was previously
    the rational decimal `2.029883212819307250011597804990` — which, as of the
    2026-08-30 correction below, is now known to have been not merely truncated
    but WRONG from its 21st significant figure. The note is left with the value
    it actually carried; a historical record that silently adopts a later
    correction stops being a record. -/
noncomputable def VOL_4_1 : ℝ := 2 * QOU.Archimedean.Cl_2 (π / 3)

/-- `VOL_4_1` agrees with the Clausen-filler volume carrier
    `Vol_figure_8 = 2·Cl₂(π/3)` definitionally. -/
theorem VOL_4_1_eq_vol_figure_8 : VOL_4_1 = QOU.Archimedean.Vol_figure_8 := rfl

/-- The 30-digit decimal approximation of `Vol(4_1)`. An APPROXIMATION carrier
    only — `VOL_4_1 = 2·Cl₂(π/3)` is transcendental; no formal identity between
    the two is claimed (that would need certified interval arithmetic on `Cl₂`).

    ⚠ **CORRECTED 2026-08-30 (bean `qou-f8lit`) — this literal was WRONG.**

It read `2.029883212819307250011597804990`, which is **wrong from the 21st significant
figure** (error `3.08e-20`) against the canonical
`2·Cl₂(π/3) = 2.0298832128193072500424051085490…`. Verified by three independent
routes: `2·Cl₂(π/3)`, `6·Λ(π/3)`, and `2·Im Li₂(e^{iπ/3})`.

**This is worse in kind than a truncation.** A truncated literal is correct but short;
this one presented 30 digits of which only 20 were right, and the extra digits invite
the trust that a short value would not get. `MassDerivation.vol_figure_eight` carries the
correct value at 24 digits, so the corpus disagreed with itself.

Nothing in Lean was unsound: `abs_VOL_4_1_sub_decimal_lt` bounds the gap by `1/10` and
`3.08e-20 < 1/10` comfortably, so the theorem held either way — which is exactly why a
coarse certified bound does not protect a decimal's digits.

Known family, partially drained: bean `qou-jgew` found **seven** wrong hand-typed
`Vol(4₁)` values in one session, and `docs/audits/2026-06-21-q0-clusterD-and-vol41-fixes.md`
fixed one `.py` probe. Those drains never reached this Lean carrier. **Still live:** six
`computations/` sites carry the sibling variant `2.0298832128193072500115970029`, one of
them a committed witness that needs a producer re-run. -/
noncomputable def VOL_4_1_decimal : ℝ := (2029883212819307250042405108549 : ℝ) / 10 ^ 30

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
