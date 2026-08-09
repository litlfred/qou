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

**Complete and `sorry`-free.** `det_mul_eq_sum_minors` is the general theorem;
`det_gram_map_ne_zero` is the corollary `sp01` consumes. Every declaration in
this file checks with `#print axioms` reporting only
`propext, Classical.choice, Quot.sound`.

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

/-! ## Step 3b — the same factoring, without the injectivity hypothesis

The split used above never needed `φ` injective: for *every* `φ`, the
`σ`-sum is `det (A.submatrix id φ)` times the `σ`-independent `B` product.
Stating it that way subsumes step 3 (the non-injective case is then just
`det = 0`) and is the form the assembly actually consumes. -/

/-- For every `φ`, the inner `σ`-sum factors as a determinant times the
`σ`-independent `B` product. -/
theorem sum_over_perms_eq {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) (φ : Fin r → Fin n) :
    (∑ σ : Equiv.Perm (Fin r),
        Equiv.Perm.sign σ • ∏ i, A (σ i) (φ i) * B (φ i) i)
      = (A.submatrix id φ).det * ∏ i, B (φ i) i := by
  have key : ∀ σ : Equiv.Perm (Fin r),
      Equiv.Perm.sign σ • ∏ i, A (σ i) (φ i) * B (φ i) i
        = (Equiv.Perm.sign σ • ∏ i, A (σ i) (φ i)) * ∏ i, B (φ i) i := by
    intro σ
    rw [Finset.prod_mul_distrib, smul_mul_assoc]
  rw [Finset.sum_congr rfl (fun σ _ => key σ), ← Finset.sum_mul,
    sum_perm_eq_det_submatrix]

/-- **`det (A * B)` as a sum of minors-times-products over all `φ`.** The
non-injective terms are already zero by `det_submatrix_eq_zero_of_not_injective`. -/
theorem det_mul_eq_sum_det_submatrix {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) :
    (A * B).det
      = ∑ φ : Fin r → Fin n, (A.submatrix id φ).det * ∏ i, B (φ i) i := by
  rw [det_mul_eq_sum_over_functions]
  exact Finset.sum_congr rfl (fun φ _ => sum_over_perms_eq A B φ)

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

/-- A selector composed with a permutation is injective. -/
theorem comp_perm_injective {r n : ℕ} (f : Selector r n) (π : Equiv.Perm (Fin r)) :
    Function.Injective (f.1 ∘ π) :=
  f.2.injective.comp π.injective

/-- **Round trip, selector half.** Sorting `f ∘ π` recovers `f` — because `f`
is already the increasing enumeration of that image, and
`Finset.orderEmbOfFin_unique` says there is only one. -/
theorem sortSelector_comp {r n : ℕ} (f : Selector r n) (π : Equiv.Perm (Fin r)) :
    (sortSelector (comp_perm_injective f π)).1 = f.1 := by
  symm
  refine Finset.orderEmbOfFin_unique (card_imageFinset (comp_perm_injective f π)) ?_ f.2
  intro x
  have hx : f.1 x = (f.1 ∘ π) (π.symm x) := by simp
  rw [hx]
  exact mem_imageFinset _ _

/-- **Round trip, permutation half.** Sorting `f ∘ π` recovers `π`, since the
factorization pins it and `f` is injective. -/
theorem sortPerm_comp {r n : ℕ} (f : Selector r n) (π : Equiv.Perm (Fin r)) :
    sortPerm (comp_perm_injective f π) = π := by
  refine Equiv.ext (fun i => ?_)
  have hfac := sortSelector_comp_sortPerm (comp_perm_injective f π) i
  rw [sortSelector_comp f π] at hfac
  exact f.2.injective hfac

/-- **Permuting the columns.** `A.submatrix id (f ∘ π)` is `A.submatrix id f`
with its columns shuffled by `π`, so the determinants differ by `sign π`. -/
theorem det_submatrix_comp_perm {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (f : Fin r → Fin n) (π : Equiv.Perm (Fin r)) :
    (A.submatrix id (f ∘ π)).det
      = Equiv.Perm.sign π * (A.submatrix id f).det := by
  have : A.submatrix id (f ∘ π) = (A.submatrix id f).submatrix id π := rfl
  rw [this, Matrix.det_permute']

/-! ## Step 6 — assembly

Three moves, each with its ingredient already proved above:

1. drop the non-injective `φ` (their terms are `0`);
2. reindex the injective `φ` by `(f, π)`, using the two round trips;
3. regroup: the `π`-sum for a fixed `f` is `det (minorB B f)` by `det_apply`,
   with the sign absorbed by `det_submatrix_comp_perm`.
-/

/-- The summand, named so the reindexing has something to talk about. -/
def term {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) (φ : Fin r → Fin n) : R :=
  (A.submatrix id φ).det * ∏ i, B (φ i) i

/-- Only injective `φ` can contribute. -/
theorem term_eq_zero_of_not_injective {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) {φ : Fin r → Fin n}
    (hφ : ¬ Function.Injective φ) : term A B φ = 0 := by
  rw [term, det_submatrix_eq_zero_of_not_injective A hφ, zero_mul]

/-- For a fixed selector, summing the term over all permutations gives the
product of the two minors. -/
theorem sum_term_comp_perm {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) (f : Selector r n) :
    (∑ π : Equiv.Perm (Fin r), term A B (f.1 ∘ π))
      = (minorA A f).det * (minorB B f).det := by
  have hB : (minorB B f).det
      = ∑ π : Equiv.Perm (Fin r), Equiv.Perm.sign π • ∏ i, B (f.1 (π i)) i :=
    Matrix.det_apply _
  rw [hB, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun π _ => ?_)
  rw [term, det_submatrix_comp_perm, minorA]
  -- `(f ∘ π) i` vs `f (π i)` is definitional once the composition is
  -- unfolded; the rest is the `ℤˣ`-action and associativity
  simp only [Function.comp_apply, Units.smul_def]
  ring

/-- The injective `φ` — after `term_eq_zero_of_not_injective`, the only index
set that carries any weight. -/
def injFns (r n : ℕ) : Finset (Fin r → Fin n) :=
  Finset.univ.filter (fun φ => Function.Injective φ)

theorem mem_injFns {r n : ℕ} {φ : Fin r → Fin n} (hφ : φ ∈ injFns r n) :
    Function.Injective φ :=
  (Finset.mem_filter.mp hφ).2

theorem mem_injFns_of {r n : ℕ} {φ : Fin r → Fin n}
    (hφ : Function.Injective φ) : φ ∈ injFns r n :=
  Finset.mem_filter.mpr ⟨Finset.mem_univ _, hφ⟩

/-- **The reindexing.** Sorting is a bijection from the injective `φ` onto the
pairs `(f, π)`, and `Finset.sum_bij'` takes exactly the two round trips proved
above plus the factorization.

Note the direction of `sum_bij'`'s `i`: it is allowed to depend on membership,
which is what lets it be `φ ↦ (sortSelector hφ, sortPerm hφ)` — `sortSelector`
needs the injectivity proof, so the non-dependent `sum_nbij'` cannot express
this map. -/
theorem sum_term_eq_sum_pairs {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) :
    (∑ φ ∈ injFns r n, term A B φ)
      = ∑ p : Selector r n × Equiv.Perm (Fin r), term A B (p.1.1 ∘ p.2) := by
  refine Finset.sum_bij'
    (fun φ hφ => (sortSelector (mem_injFns hφ), sortPerm (mem_injFns hφ)))
    (fun p _ => p.1.1 ∘ p.2)
    (fun _ _ => Finset.mem_univ _)
    (fun p _ => mem_injFns_of (comp_perm_injective p.1 p.2))
    ?_ ?_ ?_
  · -- `sortSelector` ∘ `sortPerm` rebuilds `φ`
    intro φ hφ
    exact funext fun i => sortSelector_comp_sortPerm (mem_injFns hφ) i
  · -- sorting `f ∘ π` recovers the pair; the two halves are the round trips
    rintro ⟨f, π⟩ _
    simp only [Prod.mk.injEq]
    exact ⟨Subtype.ext (sortSelector_comp f π), sortPerm_comp f π⟩
  · -- the summands agree, again by the factorization
    intro φ hφ
    exact congrArg (term A B)
      (funext fun i => (sortSelector_comp_sortPerm (mem_injFns hφ) i).symm)

/-- **Rectangular Cauchy–Binet.** `det (A * B) = ∑_f det (A_f) * det (B^f)`
over the strictly monotone `f : Fin r → Fin n`.

Absent from Mathlib as of this writing — see the header note. -/
theorem det_mul_eq_sum_minors {r n : ℕ} (A : Matrix (Fin r) (Fin n) R)
    (B : Matrix (Fin n) (Fin r) R) :
    (A * B).det = ∑ f : Selector r n, (minorA A f).det * (minorB B f).det := by
  -- Ref: [aitken1956] Aitken, Determinants and Matrices, §II (Cauchy–Binet)
  -- 3. regroup the pair-sum: for a fixed `f`, the `π`-sum is `det (minorB B f)`
  have hpairs : (∑ p : Selector r n × Equiv.Perm (Fin r), term A B (p.1.1 ∘ p.2))
      = ∑ f : Selector r n, (minorA A f).det * (minorB B f).det := by
    rw [Fintype.sum_prod_type]
    exact Finset.sum_congr rfl (fun f _ => sum_term_comp_perm A B f)
  -- 1. the non-injective `φ` contribute nothing, so the sum may be restricted
  have hdrop : (∑ φ ∈ injFns r n, term A B φ)
      = ∑ φ : Fin r → Fin n, term A B φ := by
    refine Finset.sum_subset (Finset.filter_subset _ _) ?_
    intro φ _ hφ
    exact term_eq_zero_of_not_injective A B fun h => hφ (mem_injFns_of h)
  rw [det_mul_eq_sum_det_submatrix]
  show (∑ φ : Fin r → Fin n, term A B φ) = _
  -- 2. reindex, then 3.
  rw [← hdrop, sum_term_eq_sum_pairs, hpairs]

/-! ## Corollary — the Gram determinant is a sum of squares

This is the form `sp01` (`specht_form_nondegenerate`) asks for, and the reason
the general theorem was worth building. Specialising `B := Aᵀ` makes the two
minors transposes of each other, so each term of the Cauchy–Binet sum is a
*square*:

  `det (A Aᵀ) = ∑_f (det A_f)²`

Over an ordered ring that is immediately `≥ 0`, and `> 0` as soon as a single
minor is nonzero — no positive-definiteness machinery, no rank argument.

The last lemma is the transfer that made this route preferable to the ℝ-only
shortcut `sp01` declined: run the positivity over `ℤ`, where the sum of
squares lives, then push the *nonzero* conclusion along `ℤ → k` for any
characteristic-zero field. The hypothesis stays `[Field k] [CharZero k]`
rather than collapsing to `ℝ`. -/

/-- **Gram form.** `det (A Aᵀ)` is the sum of the squares of the `r × r`
minors of `A`. -/
theorem det_mul_transpose_eq_sum_sq {r n : ℕ} (A : Matrix (Fin r) (Fin n) R) :
    (A * Aᵀ).det = ∑ f : Selector r n, (minorA A f).det ^ 2 := by
  rw [det_mul_eq_sum_minors]
  refine Finset.sum_congr rfl (fun f _ => ?_)
  -- `minorB Aᵀ f` and `(minorA A f)ᵀ` are the same matrix on the nose
  have hT : minorB Aᵀ f = (minorA A f)ᵀ := rfl
  rw [hT, Matrix.det_transpose, sq]

section Ordered

variable {S : Type*} [CommRing S] [LinearOrder S] [IsStrictOrderedRing S]

/-- A Gram determinant is never negative. -/
theorem det_mul_transpose_nonneg {r n : ℕ} (A : Matrix (Fin r) (Fin n) S) :
    0 ≤ (A * Aᵀ).det := by
  rw [det_mul_transpose_eq_sum_sq]
  exact Finset.sum_nonneg fun _ _ => sq_nonneg _

/-- **One nonzero minor suffices.** A single nonvanishing `r × r` minor makes
the whole Gram determinant strictly positive — the other terms cannot cancel
it, because they are squares. -/
theorem det_mul_transpose_pos {r n : ℕ} (A : Matrix (Fin r) (Fin n) S)
    {f₀ : Selector r n} (h : (minorA A f₀).det ≠ 0) : 0 < (A * Aᵀ).det := by
  rw [det_mul_transpose_eq_sum_sq]
  refine Finset.sum_pos' (fun _ _ => sq_nonneg _) ⟨f₀, Finset.mem_univ _, ?_⟩
  exact lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 h))

end Ordered

section CharZeroTransfer

variable {k : Type*} [Field k] [CharZero k]

/-- **The transfer.** An integer matrix with a nonzero `r × r` minor has a
nonsingular Gram matrix over *every* characteristic-zero field.

The order is only used over `ℤ`; `k` never needs to be ordered, which is
exactly what keeps `sp01`'s hypothesis at `[Field k] [CharZero k]`. -/
theorem det_gram_map_ne_zero {r n : ℕ} (M : Matrix (Fin r) (Fin n) ℤ)
    {f₀ : Selector r n} (h : (minorA M f₀).det ≠ 0) :
    ((M.map (Int.cast : ℤ → k)) * (M.map (Int.cast : ℤ → k))ᵀ).det ≠ 0 := by
  -- casting commutes with the Gram product entry by entry
  have hmap : (M.map (Int.cast : ℤ → k)) * (M.map (Int.cast : ℤ → k))ᵀ
      = (M * Mᵀ).map (Int.cast : ℤ → k) := by
    ext i j
    simp only [Matrix.mul_apply, Matrix.map_apply, Matrix.transpose_apply,
      Int.cast_sum, Int.cast_mul]
  rw [hmap]
  -- over `ℤ` the determinant is a positive sum of squares …
  have hZ : (M * Mᵀ).det ≠ 0 := (det_mul_transpose_pos M h).ne'
  -- … and `det` commutes with the cast, so the conclusion travels to `k`
  have hmm : (Int.castRingHom k).mapMatrix (M * Mᵀ)
      = (M * Mᵀ).map (Int.cast : ℤ → k) := rfl
  have hdet := (Int.castRingHom k).map_det (M * Mᵀ)
  rw [hmm] at hdet
  rw [← hdet]
  simpa using (Int.cast_ne_zero (α := k)).mpr hZ

end CharZeroTransfer

end QOU.MathlibExt.CauchyBinet
