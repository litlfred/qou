import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Field.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Reeb-flow pn-bond magnitude — structural identities

Formalizes the exact algebraic content behind the landed pn-bond magnitude
`g = 1/√(5 + (q₀−1)²/q₀)` (main, 2026-07-06; ²H "reeb-flow" tier of
`categorical_q_decay_ba_low_isotopes.py`), per
`docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`
§2b and `computations/probes/reeb_g_structural_identity_probe.py`.

Three statements, all generic over the base ring per AGENTS.md §7c (no `ℝ`,
no `Real.sqrt` — the square-root-free forms carry the full content):

* `deformation_eq_ceiling` (**I1**): with `v² = q`, the deformation identity
  `5 + (v − v⁻¹)² = 1 + (v + v⁻¹)²` — i.e. `(a+b)² − (a−b)² = 4ab` at
  `ab = 1`.  The "mystery" term `(q−1)²/q` is the classical `√5`-ceiling
  identity rewritten; both sides are `1 + [2]_v²`.
* `ss_matrix_sq` (**I2**, Cayley–Hamilton form): the traceless ss-sector
  exchange matrix `[[1, b], [b, −1]]` squares to `(1 + b²)·1`.  With
  `b = [2]_v` this is the q-deformation of the classical `[[1,2],[2,−1]]`
  (whose square is `5·1` — the `√5` ceiling); the landed `g` satisfies
  `g²·(1 + [2]_v²) = 1`, i.e. it sits at criticality of the deformed
  ss-sector.
* `pn_sign_conjugation` (**pn-sign isospectrality**): conjugating the
  uniform-magnitude [1⁴] complete-graph exchange matrix by
  `D = diag(1,1,−1,−1)` flips the sign of every pn entry while fixing the
  pp/nn entries.  Hence `det(1 + S(a, w)) = det(1 + S(a, −w))`
  (`pn_sign_det_invariant`): **no determinant-class observable at uniform
  per-pair magnitude can distinguish the two mixed pn signs** — the "open
  pn sign" of PR #3426 is unobservable in this class.  (Scope: uniform
  magnitude, complete graph; per-pair non-uniform framings can break it.)
-/

namespace QOU
namespace MassTheory
namespace ReebPnMagnitude

open Matrix

variable {K : Type*} [Field K]
variable {R : Type*} [CommRing R]

/-- **I1** — the deformation identity: `5 + (v − v⁻¹)² = 1 + (v + v⁻¹)²`
for any invertible `v`.  It is `(a+b)² − (a−b)² = 4ab` with `ab = 1`;
with `v = √q` the left side is `5 + (q−1)²/q` and the right side is
`1 + [2]_v²` — the landed pn-magnitude radicand equals the q-deformed
ss-ceiling eigenvalue squared. -/
theorem deformation_eq_ceiling (v : K) (hv : v ≠ 0) :
    5 + (v - v⁻¹) ^ 2 = 1 + (v + v⁻¹) ^ 2 := by
  field_simp
  ring

/-- The 2×2 ss-sector exchange matrix `[[1, b], [b, −1]]`:
`1` is the pp−nn bar asymmetry, `b` the (quantum-counted) pn degree. -/
def ssMatrix (b : R) : Matrix (Fin 2) (Fin 2) R := !![1, b; b, -1]

/-- **I2** (Cayley–Hamilton form) — the traceless ss-sector matrix squares to
the scalar `1 + b²`.  At `b = 2` (classical pn degree) the scalar is `5`
(the `√5` ceiling); at `b = [2]_v` it is the deformed radicand of I1. -/
theorem ss_matrix_sq (b : R) : ssMatrix b * ssMatrix b = (1 + b ^ 2) • 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [ssMatrix, Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.smul_apply] <;> ring

/-- The ss-sector determinant is affine in `g²`:
`det(1 + g·M(b)) = 1 − g²·(1 + b²)`. -/
theorem ss_det_marginal (g b : R) :
    (1 + g • ssMatrix b).det = 1 - g ^ 2 * (1 + b ^ 2) := by
  simp [ssMatrix, Matrix.det_fin_two, Matrix.add_apply]
  ring

/-- **Marginal stability** — at the deformed criticality
`g²·(1 + b²) = 1` (the landed magnitude, by I1/I2 with `b = [2]_v`) the
ss-sector determinant vanishes exactly: `det(1 + g·M) = 0`.  The landed
`g_reeb` is the marginal-stability point of the q-deformed exchange — the
algebraic counterpart of the deuteron being marginally bound.  (Below
criticality the determinant is positive; the AME value sits on the bound
side, `B_AME < 5g`, consistent in sign.) -/
theorem ss_det_zero_at_criticality (g b : R) (h : g ^ 2 * (1 + b ^ 2) = 1) :
    (1 + g • ssMatrix b).det = 0 := by
  rw [ss_det_marginal, h, sub_self]

/-- The ss-sector exchange matrix is **traceless**: `tr M(b) = 0`. -/
theorem ssMatrix_trace_zero (b : R) : (ssMatrix b).trace = 0 := by
  simp [ssMatrix, Matrix.trace_fin_two]

/-- **Open-bond vs closed-loop dichotomy** — the closed-loop (determinant)
binding of a single exchange kills the linear term.  For a 2×2 matrix the
determinant expands as `det(1 + g·M) = 1 + g·tr M + g²·det M`; since the
ss-sector `M(b)` is traceless (`ssMatrix_trace_zero`), the **linear-in-`g`
coefficient vanishes** and the loop binding is `O(g²)`:
`det(1 + g·M(b)) = 1 + g²·det M(b)`.

This is the structural reason the determinant (closed-loop) form
**under-binds** the deuteron (`−E₀·ln(1−g²) ≈ 0.93` vs AME `2.22`): a single
*open* pn bond contributes to the binding at first order in the crossing
amplitude `g`, but the trace-free loop object has no first-order term.  The
deuteron is one open pn bond, so its binding is the **linear** `O(g)` object
(the reeb-flow `5g` law), not the quadratic loop determinant — which is why
the linear form is the physically correct one for the single pair.  (The
residual open question is the MeV unit of that linear object, not its
`g`-order: see the audit §2h.) -/
theorem ss_det_no_linear_term (g b : R) :
    (1 + g • ssMatrix b).det = 1 + g ^ 2 * (ssMatrix b).det := by
  rw [ss_det_marginal]
  simp [ssMatrix, Matrix.det_fin_two]
  ring

/-- The uniform-magnitude [1⁴] complete-graph exchange matrix on blocks
`[p, p, n, n]`: pp entry `a`, nn entry `−a`, all four pn entries `w`. -/
def exchangeMatrix (a w : R) : Matrix (Fin 4) (Fin 4) R :=
  !![0, a, w, w;
     a, 0, w, w;
     w, w, 0, -a;
     w, w, -a, 0]

/-- The parity conjugator `D = diag(1, 1, −1, −1)` (proton block `+`,
neutron block `−` — the p↔n bar grading). -/
def parityD : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![1, 1, -1, -1]

theorem parityD_sq : (parityD : Matrix (Fin 4) (Fin 4) R) * parityD = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [parityD, Matrix.mul_apply, Matrix.diagonal]

/-- **pn-sign conjugation** — `D · S(a, w) · D = S(a, −w)`: the parity
conjugator flips every pn entry and fixes the pp/nn entries. -/
theorem pn_sign_conjugation (a w : R) :
    parityD * exchangeMatrix a w * parityD = exchangeMatrix a (-w) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [parityD, exchangeMatrix, Matrix.mul_apply, Matrix.diagonal]

/-- **pn-sign isospectrality for determinant-class observables** —
`det(1 + S(a, w)) = det(1 + S(a, −w))`.  Since `D² = 1` and
`det D = 1`, `1 + S(a, −w) = D (1 + S(a, w)) D` and the determinant is
conjugation-invariant.  Consequence: the "open pn sign" (PR #3426) is
unobservable in any `−ln det(I + G)`-class binding form at uniform
per-pair magnitude. -/
theorem pn_sign_det_invariant (a w : R) :
    (1 + exchangeMatrix a w).det = (1 + exchangeMatrix a (-w)).det := by
  have hconj : (1 : Matrix (Fin 4) (Fin 4) R) + exchangeMatrix a (-w)
      = parityD * (1 + exchangeMatrix a w) * parityD := by
    rw [Matrix.mul_add, Matrix.add_mul, ← pn_sign_conjugation]
    congr 1
    · rw [Matrix.mul_one, parityD_sq]
  have hdetD : (parityD : Matrix (Fin 4) (Fin 4) R).det = 1 := by
    simp [parityD, Matrix.det_diagonal, Fin.prod_univ_four]
  rw [hconj, Matrix.det_mul, Matrix.det_mul, hdetD, one_mul, mul_one]

/-- Conjugation by an involution distributes over powers:
`(D M D)^k = D M^k D` whenever `D * D = 1`. -/
theorem conj_pow (D M : Matrix (Fin 4) (Fin 4) R) (hD : D * D = 1) (k : ℕ) :
    (D * M * D) ^ k = D * M ^ k * D := by
  have hDD : ∀ X : Matrix (Fin 4) (Fin 4) R, D * (D * X) = X := fun X => by
    rw [← Matrix.mul_assoc, hD, Matrix.one_mul]
  induction k with
  | zero => rw [pow_zero, pow_zero, Matrix.mul_one, hD]
  | succ n ih =>
      rw [pow_succ, pow_succ, ih]
      simp only [Matrix.mul_assoc, hDD]

/-- `pn_sign_conjugation` extended to powers:
`S(a, −w)^k = D · S(a, w)^k · D`. -/
theorem pn_sign_conjugation_pow (a w : R) (k : ℕ) :
    exchangeMatrix a (-w) ^ k = parityD * exchangeMatrix a w ^ k * parityD := by
  rw [← pn_sign_conjugation, conj_pow _ _ parityD_sq]

/-- **pn-sign blindness of charge-diagonal observables** — for any operator
`T` commuting with the p/n grading `D` (every charge-diagonal / isospin-
diagonal observable does), all mixed traces are pn-sign invariant:
`tr(T · S(a, w)^k) = tr(T · S(a, −w)^k)`.

Consequence: the [1⁴] pn writhe sign is invisible not just to the
determinant (`pn_sign_det_invariant`) but to the ENTIRE spectral/mixed-trace
observable class built from grading-commuting operators.  Sign-sensitivity
requires an operator that fails to commute with `D` — i.e. one that mixes
the p and n blocks, which in the framework is the weak/β sector (isospin
raising/lowering).  The "open pn sign" of PR #3426 is therefore a
weak-sector observable, not a binding-sector one. -/
theorem pn_sign_trace_blind (a w : R) (k : ℕ)
    (T : Matrix (Fin 4) (Fin 4) R) (hT : T * parityD = parityD * T) :
    (T * exchangeMatrix a w ^ k).trace = (T * exchangeMatrix a (-w) ^ k).trace := by
  rw [pn_sign_conjugation_pow]
  have hmove : T * (parityD * exchangeMatrix a w ^ k * parityD)
      = parityD * (T * exchangeMatrix a w ^ k) * parityD := by
    calc T * (parityD * exchangeMatrix a w ^ k * parityD)
        = T * parityD * exchangeMatrix a w ^ k * parityD := by
          simp only [Matrix.mul_assoc]
      _ = parityD * T * exchangeMatrix a w ^ k * parityD := by rw [hT]
      _ = parityD * (T * exchangeMatrix a w ^ k) * parityD := by
          simp only [Matrix.mul_assoc]
  rw [hmove, Matrix.trace_mul_cycle, ← Matrix.mul_assoc, parityD_sq,
    Matrix.one_mul]

end ReebPnMagnitude
end MassTheory
end QOU
