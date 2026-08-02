import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# QOU.Resurgence.StokesMatrixDescent

Categorical descent of the resurgent Stokes data, proved sorry-free over a
generic base ring (see the sibling `.md` for the full narrative):

* `stokes_trace_conj_invariant` (A.ii): trace conjugacy-invariance
  `tr (g S g_inv) = tr S`, the gauge-invariant Markov trace.
* `stokes_block_diagonal` (A.i): Wedderburn equivariance implies
  block-diagonal `S = sum e_i S e_i`.
* `stokes_trace_block_sum`: the trace splits into per-partition block traces.

Ref: manuscript, mass-theory/stokes-matrix-descent.
-/

namespace QOU.Resurgence

open scoped BigOperators
open Matrix

/-! ## (A.ii) Gauge-invariance of the Markov trace `tr_M(S)` -/

section TraceInvariance

variable {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]

/-- **Stokes-trace descent (A.ii).**  A gauge / basis change acts on the
Stokes matrix by conjugation `S ↦ g S g⁻¹`; the bar-invariant, gauge-invariant
observable is the trace, a conjugacy invariant:
`tr(g S g⁻¹) = tr(S)`.  This is the matrix-level Markov trace `tr_M(S)`, and it
is **independent of the gauge `g`** — proved from trace cyclicity.  (The
independence of the *archimedean summation choice*, median vs lateral, is a
separate `ℝ`-level statement and is not part of this generic-ring scaffold.) -/
theorem stokes_trace_conj_invariant (g : (Matrix n n R)ˣ) (S : Matrix n n R) :
    ((g : Matrix n n R) * S * (↑g⁻¹ : Matrix n n R)).trace = S.trace := by
  rw [Matrix.trace_mul_comm, ← mul_assoc, g.inv_mul, one_mul]

end TraceInvariance

/-! ## (A.i) Wedderburn equivariance ⇒ block-diagonalisation

Stated over a general ring `A` (which the matrix algebra `Mat_n(R)` is an
instance of), with `e : ι → A` the family of central idempotents indexed by
partitions `ι`. -/

section BlockDiagonal

variable {ι A : Type*} [Fintype ι] [Ring A]

/-- A **complete orthogonal idempotent family** — the central Wedderburn /
Young idempotents `e_λ` of `H_n(q)`, one per partition `λ : ι`. -/
structure IdempotentFamily (e : ι → A) : Prop where
  /-- Each `e_i` is idempotent. -/
  idem : ∀ i, e i * e i = e i
  /-- Distinct idempotents are orthogonal. -/
  ortho : ∀ i j, i ≠ j → e i * e j = 0
  /-- The family is complete: `∑_i e_i = 1`. -/
  complete : ∑ i, e i = 1

/-- **`Sₙ`/Wedderburn equivariance**: the Stokes matrix `S` commutes with every
idempotent `e_λ` (equivalently, it commutes with the Young symmetrisers, i.e.
is `Sₙ`-equivariant on the multiplicity spaces). -/
def CommutesFamily (e : ι → A) (S : A) : Prop := ∀ i, e i * S = S * e i

/-- **Off-block vanishing.**  Under equivariance, the `(i,j)`-block `e_i S e_j`
of an equivariant `S` vanishes for `i ≠ j`.  Proof: push `e_j` left through
`S`, then use orthogonality `e_i e_j = 0`. -/
theorem offblock_zero {e : ι → A} (hf : IdempotentFamily e) {S : A}
    (hS : CommutesFamily e S) {i j : ι} (hij : i ≠ j) :
    e i * S * e j = 0 := by
  calc e i * S * e j = e i * (e j * S) := by rw [mul_assoc, ← hS j]
    _ = (e i * e j) * S := by rw [mul_assoc]
    _ = 0 * S := by rw [hf.ortho i j hij]
    _ = 0 := zero_mul S

/-- **Block-diagonalisation (A.i).**  An `Sₙ`/Wedderburn-equivariant Stokes
matrix `S` is block-diagonal in the Young/Hecke idempotent decomposition:
`S = ∑_λ e_λ S e_λ`.  Fully **proved** from completeness + off-block vanishing;
no `sorry`, no axiom. -/
theorem stokes_block_diagonal {e : ι → A} (hf : IdempotentFamily e) {S : A}
    (hS : CommutesFamily e S) :
    S = ∑ i, e i * S * e i := by
  have key : (∑ i, e i) * S * (∑ j, e j) = ∑ i, e i * S * e i := by
    rw [Finset.sum_mul, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Finset.mul_sum, Finset.sum_eq_single i]
    · intro j _ hji
      exact offblock_zero hf hS (Ne.symm hji)
    · intro hi
      exact absurd (Finset.mem_univ i) hi
  calc S = (∑ i, e i) * S * (∑ j, e j) := by rw [hf.complete, one_mul, mul_one]
    _ = ∑ i, e i * S * e i := key

end BlockDiagonal

/-! ## Consequence: the invariant trace is the sum of per-partition block traces -/

section BlockTrace

variable {n ι R : Type*} [Fintype n] [DecidableEq n] [Fintype ι] [DecidableEq ι]
  [CommRing R]

/-- **`tr_M(S) = ∑_λ tr(e_λ S e_λ)`.**  Combining block-diagonalisation with
additivity of the matrix trace: the gauge-invariant Markov trace of an
equivariant Stokes matrix decomposes as the sum of its per-partition block
traces.  Proved sorry-free. -/
theorem stokes_trace_block_sum {e : ι → Matrix n n R}
    (hf : IdempotentFamily e) {S : Matrix n n R} (hS : CommutesFamily e S) :
    S.trace = ∑ i, (e i * S * e i).trace := by
  conv_lhs => rw [stokes_block_diagonal hf hS]
  exact Matrix.trace_sum Finset.univ (fun i => e i * S * e i)

end BlockTrace

end QOU.Resurgence
