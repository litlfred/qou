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

/-! ## Step 2 — regroup by `φ : Fin r → Fin n`

`Fintype.prod_sum` turns the product-of-sums into a sum over functions. After
commuting the two sums, the outer index is `φ`, which is what the vanishing
and factoring arguments both case on. -/

/-- The product-of-sums, expanded as a sum over `φ : Fin r → Fin n`. -/
theorem prod_sum_interchange {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) (σ : Equiv.Perm (Fin r)) :
    (∏ i, ∑ k : Fin n, A (σ i) k * B k i)
      = ∑ φ : Fin r → Fin n, ∏ i, A (σ i) (φ i) * B (φ i) i :=
  Fintype.prod_sum (fun i k => A (σ i) k * B k i)

/-- **`det (A * B)` grouped by `φ`.** Every later step is a statement about a
single `φ`: non-injective ones vanish, injective ones factor. -/
theorem det_mul_eq_sum_over_functions {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) :
    (A * B).det
      = ∑ φ : Fin r → Fin n, ∑ σ : Equiv.Perm (Fin r),
          Equiv.Perm.sign σ • ∏ i, A (σ i) (φ i) * B (φ i) i := by
  rw [det_mul_leibniz]
  simp_rw [prod_sum_interchange, Finset.smul_sum]
  exact Finset.sum_comm

/-! ## Step 3 — a non-injective `φ` contributes nothing

The textbook argument pairs each `σ` with `σ ∘ (swap i j)` and cancels. That
involution is fiddly here, because the `B` factor carries the row index and
does not survive the reindexing unchanged.

Cleaner: the `σ`-sum **is a determinant**. Factoring the `σ`-independent `B`
product out leaves exactly `Matrix.det_apply` for `A.submatrix id φ`, and a
non-injective `φ` repeats a column of that submatrix — which Mathlib already
knows kills the determinant. No hand-rolled involution needed. -/

/-- The `σ`-sum is the determinant of the column-selected submatrix. -/
theorem sum_perm_eq_det_submatrix {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (φ : Fin r → Fin n) :
    (∑ σ : Equiv.Perm (Fin r), Equiv.Perm.sign σ • ∏ k, A (σ k) (φ k))
      = (A.submatrix id φ).det := by
  rw [Matrix.det_apply]
  rfl

/-- A repeated column kills it: if `φ` is not injective, `A.submatrix id φ`
has two equal columns. -/
theorem det_submatrix_eq_zero_of_not_injective {r n : ℕ}
    (A : Matrix (Fin r) (Fin n) R) {φ : Fin r → Fin n}
    (hφ : ¬ Function.Injective φ) :
    (A.submatrix id φ).det = 0 := by
  obtain ⟨i, j, hij, hne⟩ := Function.not_injective_iff.mp hφ
  rw [← Matrix.det_transpose]
  refine Matrix.det_zero_of_row_eq hne ?_
  funext l
  simp only [Matrix.transpose_apply, Matrix.submatrix_apply, id_eq, hij]

/-- **Step 3.** A non-injective `φ` contributes `0` to the regrouped sum. -/
theorem sum_over_perms_eq_zero_of_not_injective {r n : ℕ}
    (A : Matrix (Fin r) (Fin n) R) (B : Matrix (Fin n) (Fin r) R)
    {φ : Fin r → Fin n} (hφ : ¬ Function.Injective φ) :
    (∑ σ : Equiv.Perm (Fin r),
        Equiv.Perm.sign σ • ∏ i, A (σ i) (φ i) * B (φ i) i) = 0 := by
  have key : ∀ σ : Equiv.Perm (Fin r),
      Equiv.Perm.sign σ • ∏ i, A (σ i) (φ i) * B (φ i) i
        = (Equiv.Perm.sign σ • ∏ i, A (σ i) (φ i)) * ∏ i, B (φ i) i := by
    intro σ
    rw [Finset.prod_mul_distrib, smul_mul_assoc]
  rw [Finset.sum_congr rfl (fun σ _ => key σ), ← Finset.sum_mul,
    sum_perm_eq_det_submatrix, det_submatrix_eq_zero_of_not_injective A hφ,
    zero_mul]

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
