/-
  The algebraic skeleton of the Dimofte-Garoufalidis 1-loop invariant.

  WHAT THIS IS FOR.  The multi-cusp extension of the DG 1-loop invariant was
  derived numerically in `computations/one_loop_torsion.py` and validated in
  `computations/probes/one_loop_multicusp_derivation_probe.py`
  (audit: `docs/audits/2026-08-07-one-loop-multicusp-derivation.md`).  Most of
  that evidence is measurement — triangulation invariance over randomised
  triangulations, the change-of-curve law against SnapPy's cusp shapes.  But
  three of the load-bearing steps are not measurements at all; they are algebra
  that was ASSERTED in prose.  They are proved here.

  1. `zeta_sum_eq_zero` — `ζ + ζ' + ζ'' = 0`.

  2. `edge_rows_sum_zero` — if every column of the edge matrices sums to `2`,
     the specialised edge rows sum to zero.  **No hypothesis about the number
     of cusps appears anywhere in the statement or the proof.**  That is the
     whole point: PR #4708 asserted that the column-sum identity is specific to
     one cusp and that this blocked the extension.  The identity was then
     measured to hold at every cusp number, and this theorem shows the step it
     feeds is likewise cusp-free.

  3. `det_basis_change` and friends — changing the integral basis of the row
     lattice multiplies the determinant by the determinant of the change of
     basis.  Unimodular changes therefore leave it fixed up to sign (so the
     invariant is well defined once the edge rows are a lattice BASIS), while
     rows generating a sublattice of index `k` scale it by `k`.  That is the
     failure mode a greedy independent SUBSET exhibits, with `k = 2` observed.

  4. `percusp_factor_absorbs` — the per-cusp factor `2^{(c-1)/2}` is exactly
     cancelled by the `2^c` between the superseded determinant and the DG
     invariant, FOR EVERY `c`.  This is the one claim in
     `docs/audits/2026-08-08-per-cusp-factor-dissolves.md` that is a theorem
     rather than a measurement: it says the two laws are indistinguishable on
     any data where `|τ_old| = 2^c |τ|` holds, which is why fitting the factor
     on such data confirmed nothing.

  WHAT THIS IS NOT.  Nothing here proves that the multi-cusp construction
  computes the adjoint torsion, or that it is a topological invariant.  Those
  remain numerical (and, at `c = 1`, a theorem of Garoufalidis-Yoon for
  two-bridge knots).  The shapes are free complex numbers here; no gluing
  equation is imposed.  What is formalised is the algebra those arguments run
  on, and in particular that steps 2 and 4 are cusp-number-free.

  -- Ref: [dimofte-garoufalidis-2013] arXiv:1202.6268, Defn 1.2, Defn 2.1, Sec 1.9
  -- Ref: [neumann-zagier1985] Volumes of hyperbolic three-manifolds, Topology 24
  -- Ref: [porti2015] §5.1, prop:change (change-of-curve law: the ratio of the
  --      torsions for two peripheral curves is ± the Jacobian of the change of
  --      local parameter; the cusp-shape form at the holonomy is the corollary
  --      that follows it)
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

open scoped BigOperators

namespace QOU.OneLoopEdgeLattice

/-! ### The shape triple -/

/-- `ζ = 1/z`. -/
noncomputable def zeta (z : ℂ) : ℂ := 1 / z

/-- `ζ' = 1/(1-z)`. -/
noncomputable def zetaP (z : ℂ) : ℂ := 1 / (1 - z)

/-- `ζ'' = 1/(z(z-1))`. -/
noncomputable def zetaPP (z : ℂ) : ℂ := 1 / (z * (z - 1))

/-- The identity that makes the edge rows degenerate: `ζ + ζ' + ζ'' = 0`. -/
theorem zeta_sum_eq_zero {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    zeta z + zetaP z + zetaPP z = 0 := by
  have h1 : z - 1 ≠ 0 := sub_ne_zero.mpr hz1
  have h2 : (1 : ℂ) - z ≠ 0 := sub_ne_zero.mpr (Ne.symm hz1)
  unfold zeta zetaP zetaPP
  field_simp
  ring

theorem zetaPP_eq {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    zetaPP z = -zeta z - zetaP z := by
  have := zeta_sum_eq_zero hz0 hz1
  linear_combination this

/-- The specialised row depends only on the Neumann-Zagier pair
`(a, b) = (G - G'', G' - G'')`.  This is why the relevant lattice lives in
`ℤ^{2N}` rather than `ℤ^{3N}`. -/
theorem nz_pair_reduction {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) (g g' g'' : ℤ) :
    (g : ℂ) * zeta z + (g' : ℂ) * zetaP z + (g'' : ℂ) * zetaPP z
      = ((g - g'' : ℤ) : ℂ) * zeta z + ((g' - g'' : ℤ) : ℂ) * zetaP z := by
  rw [zetaPP_eq hz0 hz1]
  push_cast
  ring

/-! ### The edge rows are degenerate at every cusp number -/

/-- **The structural fact behind the multi-cusp extension.**

If every column of the edge matrices sums to `2` — which holds at every cusp
number, because each tetrahedron has six edges in three opposite pairs, one pair
per shape type, and each is glued into exactly one edge class — then the
specialised edge rows sum to zero, hence have rank at most `N - 1`.

Note what is absent: there is no cusp number in this statement, and none in the
proof.  DG state the column-sum identity for one cusp ("every edge begins and
ends at the cusp"), and PR #4708 read that as a hypothesis and concluded the
`c ≥ 2` extension was blocked.  It is not a hypothesis. -/
theorem edge_rows_sum_zero {m n : ℕ} (G G' G'' : Fin m → Fin n → ℤ) (z : Fin n → ℂ)
    (hz0 : ∀ j, z j ≠ 0) (hz1 : ∀ j, z j ≠ 1)
    (hG : ∀ j, ∑ I, G I j = 2) (hG' : ∀ j, ∑ I, G' I j = 2)
    (hG'' : ∀ j, ∑ I, G'' I j = 2) (j : Fin n) :
    ∑ I, ((G I j : ℂ) * zeta (z j) + (G' I j : ℂ) * zetaP (z j)
          + (G'' I j : ℂ) * zetaPP (z j)) = 0 := by
  simp only [Finset.sum_add_distrib, ← Finset.sum_mul]
  have c1 : ∑ I, ((G I j : ℤ) : ℂ) = (2 : ℂ) := by
    rw [← Int.cast_sum, hG j]; norm_num
  have c2 : ∑ I, ((G' I j : ℤ) : ℂ) = (2 : ℂ) := by
    rw [← Int.cast_sum, hG' j]; norm_num
  have c3 : ∑ I, ((G'' I j : ℤ) : ℂ) = (2 : ℂ) := by
    rw [← Int.cast_sum, hG'' j]; norm_num
  rw [c1, c2, c3]
  have := zeta_sum_eq_zero (hz0 j) (hz1 j)
  linear_combination (2 : ℂ) * this

/-- Non-vacuity: the hypotheses of `edge_rows_sum_zero` are simultaneously
satisfiable, so the theorem is not vacuously true.  (They are not satisfiable at
`m = 0` — with no edges the column sums are `0`, not `2` — which is exactly the
degenerate reading a vacuity audit should rule out.) -/
theorem edge_rows_hypotheses_satisfiable :
    ∃ (G G' G'' : Fin 2 → Fin 1 → ℤ) (z : Fin 1 → ℂ),
      (∀ j, z j ≠ 0) ∧ (∀ j, z j ≠ 1) ∧
      (∀ j, ∑ I, G I j = 2) ∧ (∀ j, ∑ I, G' I j = 2) ∧ (∀ j, ∑ I, G'' I j = 2) :=
  ⟨fun _ _ => 1, fun _ _ => 1, fun _ _ => 1, fun _ => 2,
    by norm_num, by norm_num, by decide, by decide, by decide⟩

/-! ### Why the rows must be a lattice basis, not just independent -/

/-- Changing the integral basis of the row lattice multiplies the determinant by
the determinant of the change-of-basis matrix. -/
theorem det_basis_change {n : ℕ} (U : Matrix (Fin n) (Fin n) ℤ)
    (B : Matrix (Fin n) (Fin n) ℂ) :
    (U.map (fun k : ℤ => (k : ℂ)) * B).det = ((U.det : ℤ) : ℂ) * B.det := by
  rw [Matrix.det_mul]
  congr 1
  exact (RingHom.map_det (Int.castRingHom ℂ) U).symm

/-- A unimodular change of basis leaves the determinant fixed up to sign.  So
the 1-loop determinant is well defined — DG's `τ` carries an undetermined sign
anyway — once the edge rows are a lattice BASIS, e.g. a Hermite normal form. -/
theorem det_basis_change_unimodular {n : ℕ} (U : Matrix (Fin n) (Fin n) ℤ)
    (B : Matrix (Fin n) (Fin n) ℂ) (hU : U.det = 1 ∨ U.det = -1) :
    (U.map (fun k : ℤ => (k : ℂ)) * B).det = B.det ∨
    (U.map (fun k : ℤ => (k : ℂ)) * B).det = -B.det := by
  rcases hU with h | h <;> rw [det_basis_change, h] <;> simp

/-- Rows generating a SUBLATTICE of index `k` scale the determinant by `k`.

This is the failure mode.  An independent subset of the edge rows spans the
right complex subspace, so it looks correct, but need not generate the lattice;
the determinant is then off by the index.  Measured index: exactly `2`, on
`L5a1`, `L6a4` and `L7a1`, in roughly one randomised triangulation in thirty. -/
theorem det_sublattice_index {n : ℕ} (U : Matrix (Fin n) (Fin n) ℤ)
    (B : Matrix (Fin n) (Fin n) ℂ) (k : ℤ) (hU : U.det = k) :
    (U.map (fun k : ℤ => (k : ℂ)) * B).det = (k : ℂ) * B.det := by
  rw [det_basis_change, hU]

/-! ### The per-cusp factor is a reparametrization -/

/-- **The per-cusp factor `2^{(c-1)/2}` cancels identically.**

If the superseded determinant satisfies `|τ_old| = 2^c |τ|` — which holds on the
default triangulations of `4_1`, `L5a1` and `L6a4`, the three cases the factor
was fitted to — then

  `2^{(c-1)/2} · |τ_old|^{-1/2}  =  2^{-1/2} · |τ|^{-1/2}`

for **every** `c`.  So the law carrying a per-cusp factor and the law carrying
none are the same function on such data, and agreement at `c = 1, 2, 3`
distinguishes nothing.  This is the precise sense in which the "standard
per-cusp Gaussian-integration factor" was a reparametrization: it is exactly the
`c`-dependence needed to undo the `2^c`.

Stated for real `c` and any `t > 0`; the geometric content is `t = |τ|`. -/
theorem percusp_factor_absorbs {t c : ℝ} (ht : 0 < t) :
    (2 : ℝ) ^ ((c - 1) / 2) * ((2 : ℝ) ^ c * t) ^ (-(1 : ℝ) / 2)
      = (2 : ℝ) ^ (-(1 : ℝ) / 2) * t ^ (-(1 : ℝ) / 2) := by
  have h2 : (0 : ℝ) < 2 := by norm_num
  have hpc : (0 : ℝ) < (2 : ℝ) ^ c := Real.rpow_pos_of_pos h2 c
  have hx : (c - 1) / 2 + c * (-(1 : ℝ) / 2) = -(1 : ℝ) / 2 := by ring
  rw [Real.mul_rpow hpc.le ht.le, ← Real.rpow_mul h2.le, ← mul_assoc,
    ← Real.rpow_add h2, hx]

/-- The converse reading, which is what the measurement actually reports: with
the corrected invariant the constant is `2^{-1/2}` with no `c` in it, and the
`c = 1` calibration therefore determines every other cusp number. -/
theorem percusp_free_law {t c : ℝ} (ht : 0 < t) :
    (2 : ℝ) ^ (-(1 : ℝ) / 2) * t ^ (-(1 : ℝ) / 2)
      = (2 : ℝ) ^ ((c - 1) / 2) * ((2 : ℝ) ^ c * t) ^ (-(1 : ℝ) / 2) :=
  (percusp_factor_absorbs ht).symm

end QOU.OneLoopEdgeLattice
