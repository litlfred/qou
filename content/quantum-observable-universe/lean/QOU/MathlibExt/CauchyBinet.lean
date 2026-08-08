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

/-! ## Step 4 — an injective `φ` sorts into `Selector ∘ permutation`

This is the piece with no Mathlib support. An injective `φ : Fin r → Fin n`
has an `r`-element image; enumerating that image in increasing order gives the
strictly monotone `f`, and the permutation `π` records how `φ` shuffles it.

`Finset.orderEmbOfFin` supplies the sorted enumeration; what has to be built
is the bijection onto the image and the resulting `Equiv.Perm`. -/

/-- The image of `φ`, as a `Finset`. -/
def imageFinset {r n : ℕ} (φ : Fin r → Fin n) : Finset (Fin n) :=
  Finset.image φ Finset.univ

theorem mem_imageFinset {r n : ℕ} (φ : Fin r → Fin n) (i : Fin r) :
    φ i ∈ imageFinset φ :=
  Finset.mem_image_of_mem φ (Finset.mem_univ i)

/-- An injective `φ` has an image of exactly `r` elements. -/
theorem card_imageFinset {r n : ℕ} {φ : Fin r → Fin n} (hφ : Function.Injective φ) :
    (imageFinset φ).card = r := by
  rw [imageFinset, Finset.card_image_of_injective _ hφ, Finset.card_univ,
    Fintype.card_fin]

/-- **The selector `φ` sorts to** — its image enumerated in increasing order.
Strict monotonicity comes free from `orderEmbOfFin` being an order embedding. -/
def sortSelector {r n : ℕ} {φ : Fin r → Fin n} (hφ : Function.Injective φ) :
    Selector r n :=
  ⟨(imageFinset φ).orderEmbOfFin (card_imageFinset hφ),
   ((imageFinset φ).orderEmbOfFin (card_imageFinset hφ)).strictMono⟩

/-- `φ` viewed as a map into its own image. -/
def toImage {r n : ℕ} (φ : Fin r → Fin n) (i : Fin r) : (imageFinset φ) :=
  ⟨φ i, mem_imageFinset φ i⟩

theorem toImage_bijective {r n : ℕ} {φ : Fin r → Fin n}
    (hφ : Function.Injective φ) : Function.Bijective (toImage φ) := by
  constructor
  · intro a b hab
    exact hφ (congrArg Subtype.val hab)
  · rintro ⟨x, hx⟩
    obtain ⟨i, _, hi⟩ := Finset.mem_image.mp hx
    exact ⟨i, Subtype.ext hi⟩

/-- **The permutation `φ` induces**: where each index lands once the image is
put in increasing order. -/
noncomputable def sortPerm {r n : ℕ} {φ : Fin r → Fin n}
    (hφ : Function.Injective φ) : Equiv.Perm (Fin r) :=
  (Equiv.ofBijective (toImage φ) (toImage_bijective hφ)).trans
    ((imageFinset φ).orderIsoOfFin (card_imageFinset hφ)).symm.toEquiv

/-- **The factorization.** `φ = f ∘ π`, with `f` the sorted selector and `π`
the induced permutation — the statement the assembly step needs. -/
theorem sortSelector_comp_sortPerm {r n : ℕ} {φ : Fin r → Fin n}
    (hφ : Function.Injective φ) (i : Fin r) :
    (sortSelector hφ).1 (sortPerm hφ i) = φ i := by
  have hround :
      (imageFinset φ).orderIsoOfFin (card_imageFinset hφ) (sortPerm hφ i)
        = toImage φ i :=
    OrderIso.apply_symm_apply _ _
  show ((imageFinset φ).orderEmbOfFin (card_imageFinset hφ)) (sortPerm hφ i) = φ i
  rw [← Finset.coe_orderIsoOfFin_apply, hround]
  rfl

/-! ## Frontier

Steps 1–3 are proved. What remains:

* finish `sortSelector_comp_sortPerm` (the `orderIsoOfFin`/`orderEmbOfFin`
  round trip);
* the sign bookkeeping — `sgn σ` against `sgn (σ ∘ π)` when reindexing the
  `σ`-sum by the induced permutation;
* reassemble: sum over injective `φ` = sum over `Selector r n`, since
  `φ ↦ (sortSelector, sortPerm)` is a bijection onto `Selector × Perm`.

The target below is `sorry` and labelled as such. Both remaining `sorry`s in
this file are on that path and nowhere else. -/

/-- **Rectangular Cauchy–Binet.** `det (A * B) = ∑_f det (A_f) * det (B^f)`
over the strictly monotone `f : Fin r → Fin n`.

NOT YET PROVED — see the frontier note above and bean `qou-8yph`. -/
theorem det_mul_eq_sum_minors {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) :
    (A * B).det = ∑ f : Selector r n, (minorA A f).det * (minorB B f).det := by
  -- Ref: [aitken1956] Aitken, Determinants and Matrices, §II (Cauchy–Binet)
  sorry

end QOU.MathlibExt.CauchyBinet
