import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Fintype.Perm
import Mathlib.Order.Fin.Basic

/-!
# Rectangular Cauchy–Binet

`det (A * B) = ∑_f det (A_f) * det (B^f)`, the sum running over the
strictly monotone `f : Fin r → Fin n` — i.e. over the `r`-element column
subsets of `A` and the matching row subsets of `B`.

**Mathlib does not have this.** At the pinned revision there is no file
matching `Cauchy-Binet` / `cauchy_binet` / `CauchyBinet`, and no lemma writing
a determinant as a sum over column subsets; `det_mul` covers only the square
case. This file builds it.

## Why it is wanted here

`sp01` — `specht_form_nondegenerate`, the critical path into the Specht
cluster — names exactly this as one of its two routes, and rules out the
other: an ℝ-only positive-definiteness shortcut was declined because it
would weaken the generic `[Field k] [CharZero k]` hypothesis to `ℝ`.

Cauchy–Binet avoids that. For an integer Gram matrix `G = M Mᵀ`,

  `det G = ∑_f (det M_f)²`

is a sum of squares of *integers*, so it is positive as soon as one minor is
nonzero — and that conclusion transfers to every characteristic-zero field
without specializing to ℝ.

## Status

Being built incrementally. What is proved here is proved; the frontier is
marked with `sorry` and named, never papered over with a weakened statement.

## Proof route

Leibniz, then interchange the product and sum:

  `det (A * B) = ∑_σ sgn σ ∏_i ∑_k A (σ i) k * B k i`
              `= ∑_{φ : Fin r → Fin n} ∑_σ sgn σ ∏_i A (σ i) (φ i) * B (φ i) i`

then group by `φ`. Two facts finish it:

1. a **non-injective** `φ` contributes `0` — the inner alternating sum cancels
   in pairs under the transposition swapping two indices with `φ i = φ j`;
2. an **injective** `φ` factors uniquely as a strictly monotone `f` composed
   with a permutation of `Fin r`, and that permutation's sign factors out.
-/

namespace QOU.MathlibExt.CauchyBinet

open Matrix Equiv Finset

variable {R : Type*} [CommRing R]

/-- The strictly monotone maps `Fin r → Fin n` — equivalently the `r`-element
subsets of `Fin n`, listed in increasing order. These index the minors. -/
abbrev Selector (r n : ℕ) := {f : Fin r → Fin n // StrictMono f}

instance (r n : ℕ) : Fintype (Selector r n) := by
  unfold Selector; infer_instance

/-- The `r × r` minor of `A` on the columns picked by `f`. -/
def minorA {r n : ℕ} (A : Matrix (Fin r) (Fin n) R) (f : Selector r n) :
    Matrix (Fin r) (Fin r) R :=
  A.submatrix id f.1

/-- The `r × r` minor of `B` on the rows picked by `f`. -/
def minorB {r n : ℕ} (B : Matrix (Fin n) (Fin r) R) (f : Selector r n) :
    Matrix (Fin r) (Fin r) R :=
  B.submatrix f.1 id

/-! ## Step 1 — Leibniz, with the inner sum pulled out

`det (A * B)` expands by `Matrix.det_apply` into a signed sum over
permutations of a product of matrix entries, and each entry of `A * B` is
itself a sum. `Finset.prod_sum` turns the product-of-sums into a sum over
functions `φ : Fin r → Fin n`, which is the indexing the whole proof runs on.
-/

/-- `(A * B) i j` written out, so the Leibniz expansion has something to
rewrite with. -/
theorem mul_apply' {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) (i j : Fin r) :
    (A * B) i j = ∑ k : Fin n, A i k * B k j :=
  Matrix.mul_apply

/-- **Leibniz form.** `det (A * B)` as a signed sum over permutations of a
product of `(A * B)` entries — the starting point, with no rearrangement yet. -/
theorem det_mul_leibniz {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) :
    (A * B).det
      = ∑ σ : Equiv.Perm (Fin r),
          Equiv.Perm.sign σ • ∏ i, ∑ k : Fin n, A (σ i) k * B k i := by
  rw [Matrix.det_apply]
  refine Finset.sum_congr rfl (fun σ _ => ?_)
  -- each `(A * B) (σ i) i` is definitionally `∑ k, A (σ i) k * B k i`,
  -- so `congr 1` discharges the product without a further rewrite
  congr 1

/-! ## Frontier

What remains, in order (see bean `qou-8yph`):

* interchange `∏_i ∑_k` into `∑_{φ : Fin r → Fin n} ∏_i` via `Finset.prod_sum`;
* show a **non-injective** `φ` contributes `0`, by pairing each `σ` with
  `σ * swap i j` for two indices where `φ i = φ j`;
* factor an **injective** `φ` uniquely as `f ∘ π` with `f` strictly monotone
  and `π` a permutation, pulling out `sign π`;
* reassemble into the sum over `Selector r n`.

The statement below is the target. It is `sorry` and labelled as such — the
point of this file is that the pieces above get proved one at a time, not that
the conclusion gets asserted early. -/

/-- **Rectangular Cauchy–Binet.** `det (A * B) = ∑_f det (A_f) * det (B^f)`
over the strictly monotone `f : Fin r → Fin n`.

NOT YET PROVED — see the frontier note above and bean `qou-8yph`. -/
theorem det_mul_eq_sum_minors {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) :
    (A * B).det = ∑ f : Selector r n, (minorA A f).det * (minorB B f).det := by
  -- Ref: [aitken1956] Aitken, Determinants and Matrices, §II (Cauchy–Binet)
  sorry

end QOU.MathlibExt.CauchyBinet
