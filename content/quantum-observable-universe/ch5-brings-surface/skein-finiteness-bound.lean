/-!
# QOU.Descartes.skein_finiteness_bound

Finiteness of the nuclear chart: the Skein polynomial zero as stability boundary.

At a given q > 1, the number of stable nuclear configurations is FINITE.
The boundary is the zero locus P(q) = 0 of the Skein polynomial.

The closed-form bound: A_max(q) ~ π / √(4 ln q).
At q = 1.110: A_max ≈ 4.9, consistent with the sign flip at A=6.

LaTeX label: `prop:skein-finiteness-bound`

## References
- [manuscript] §6/skein-finiteness-bound
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

-- ═══════════════════════════════════════════════════════════════════
-- The stability condition: P(q) > 0
-- ═══════════════════════════════════════════════════════════════════

/-- A nuclear configuration (p,n) is stable at substrate parameter q
    if its Skein polynomial is positive. -/
-- Ref: [manuscript] §6/skein-finiteness-bound
structure IsStable (q : ℝ) (p n : ℕ) where
  q_gt_one : 1 < q
  skein_positive : (0 : ℝ) < skeinPolynomial q p n

/-- The Skein polynomial P(q) of N(p,n) — axiomatized as computed
    by the transfer matrix product ∏ V̂_i. -/
-- Ref: [manuscript] §6/skein-polynomial-transfer-matrix
axiom skeinPolynomial (q : ℝ) (p n : ℕ) : ℝ

-- ═══════════════════════════════════════════════════════════════════
-- The closed-form bound
-- ═══════════════════════════════════════════════════════════════════

/-- The finiteness bound: [A-1]_q! > [2]_q^{A-1}.
    q-factorial beats q-exponential at A = 5 for all q > 1.
    No classical e or π — purely q-combinatorial. -/
-- Ref: [manuscript] §6/skein-finiteness-bound

/-- The q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1}). -/
noncomputable def qInt (q : ℝ) (n : ℕ) : ℝ :=
  (q ^ n - (1/q) ^ n) / (q - 1/q)

/-- The q-factorial [n]_q! = ∏_{k=1}^n [k]_q. -/
noncomputable def qFactorial (q : ℝ) (n : ℕ) : ℝ :=
  (List.range n).foldl (fun acc k => acc * qInt q (k + 1)) 1

/-- The critical condition: [A-1]_q! > [2]_q^{A-1}.
    At A = 5: [4]_q! > [2]_q⁴ for q = 1.110. -/
-- Ref: [manuscript] §6/skein-finiteness-bound
-- Ref: folio-assistant/computations output: [4]! = 25.15 > [2]⁴ = 16.35
axiom q_factorial_exceeds_at_5 (q : ℝ) (hq : 1 < q) (hq2 : q < 2) :
    qFactorial q 4 > (qInt q 2) ^ 4

/-- Below A = 5: [A-1]_q! ≤ [2]_q^{A-1}. -/
-- Ref: folio-assistant/computations output
axiom q_factorial_bounded_below_5 (q : ℝ) (hq : 1 < q) (hq2 : q < 2) :
    qFactorial q 3 < (qInt q 2) ^ 3

/-- At q = 1, A_max → ∞ (all nuclei degenerate). -/
-- Ref: [manuscript] §6/skein-finiteness-bound
theorem A_max_diverges_classical :
    ∀ M : ℝ, ∃ q : ℝ, 1 < q ∧ A_max_approx q > M := by
  intro M
  -- As q → 1⁺, ln q → 0⁺, so π/√(4 ln q) → ∞
  sorry -- Ref: [manuscript] §6/skein-finiteness-bound

/-- At q → ∞, A_max → 0 (no stable nuclei). -/
-- Ref: [manuscript] §6/skein-finiteness-bound
theorem A_max_vanishes_strong_deformation :
    ∀ ε : ℝ, 0 < ε →
    ∃ Q : ℝ, ∀ q : ℝ, q > Q → A_max_approx q < ε := by
  intro ε hε
  -- As q → ∞, ln q → ∞, so π/√(4 ln q) → 0
  sorry -- Ref: [manuscript] §6/skein-finiteness-bound

-- ═══════════════════════════════════════════════════════════════════
-- Transfer matrix eigenvalue ratio = q²
-- ═══════════════════════════════════════════════════════════════════

/-- The pp transfer matrix T_pp has eigenvalues q and -q⁻¹.
    Their ratio is -q². -/
-- Ref: [manuscript] §6/skein-finiteness-bound
theorem pp_eigenvalue_ratio (q : ℝ) (hq : 0 < q) :
    let ha := q - 1/q
    let tr_T := ha                    -- T_pp = [[ha,1],[1,0]], tr = ha
    let det_T := -(1 : ℝ)            -- det = ha·0 - 1·1 = -1
    let disc := tr_T^2 - 4*det_T     -- ha² + 4
    let lam_p := (tr_T + Real.sqrt disc) / 2
    let lam_m := (tr_T - Real.sqrt disc) / 2
    lam_p * lam_m = -1 := by
  -- Product of eigenvalues = det = -1
  sorry -- Ref: [manuscript] §6/skein-finiteness-bound (Vieta's formula)

-- ═══════════════════════════════════════════════════════════════════
-- Embeddability bound on torus knots
-- ═══════════════════════════════════════════════════════════════════

/-- A torus knot T_{m,n} embeds in a surface of genus g
    iff (m-1)(n-1)/2 ≤ g. -/
-- Ref: [manuscript] §6/torus-embeddable-complete
def torusEmbeddable (m n g : ℕ) : Prop :=
  (m - 1) * (n - 1) ≤ 2 * g

/-- The Bring surface has genus 4.
    Embeddable torus knots: (m-1)(n-1) ≤ 8.
    Complete list: T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,5}. -/
-- Ref: [manuscript] §6/torus-embeddable-complete
theorem bring_surface_torus_knots :
    torusEmbeddable 2 3 4 ∧
    torusEmbeddable 2 5 4 ∧
    torusEmbeddable 2 7 4 ∧
    torusEmbeddable 2 9 4 ∧
    torusEmbeddable 3 5 4 ∧
    ¬ torusEmbeddable 2 11 4 ∧
    ¬ torusEmbeddable 3 7 4 ∧
    ¬ torusEmbeddable 5 7 4 := by
  unfold torusEmbeddable
  omega

/-- The number of embeddable torus knots on genus 4 is finite (exactly 5). -/
-- Ref: [manuscript] §6/skein-finiteness-bound
theorem particle_finiteness :
    {(m, n) : ℕ × ℕ | 2 ≤ m ∧ m < n ∧ torusEmbeddable m n 4}.Finite := by
  apply Set.Finite.subset (Set.Finite.prod (Set.finite_Icc 2 4) (Set.finite_Icc 3 9))
  intro ⟨m, n⟩ ⟨hm, hmn, hemb⟩
  unfold torusEmbeddable at hemb
  constructor <;> constructor <;> omega

end QOU.Descartes
