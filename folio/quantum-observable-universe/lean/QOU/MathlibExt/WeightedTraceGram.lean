import QOU.MathlibExt.RegTraceGramProduct
import QOU.MathlibExt.SignProdComm

/-!
# QOU.MathlibExt.WeightedTraceGram — the Gram determinant of a character-weighted trace

Bean `qou-kwoa`, the `q`-part: the determinant side of **Geck–Pfeiffer 7.2.6**.

    Ref: [geckpfeiffer2000] Geck–Pfeiffer, *Characters of Finite Coxeter Groups and
    Iwahori–Hecke Algebras*, Thm 7.2.6.

**The citation stays, and its role changes.** In `QOU.MathlibExt.WenzlSchurElement` the
Geck–Pfeiffer criterion is carried as `SchurElementCriterion`, a hypothesis **class with no
instance** — the theorem is *assumed*. What is proved below is the determinant half of that
theorem, so for the split semisimple case the citation becomes an **attribution** rather than
a load-bearing assumption. Geck and Pfeiffer proved it first; a Lean proof does not change
that, and every declaration here says so.

## The observation this file is built on

On a split semisimple algebra `A ≅ ∏_λ M_{d_λ}(K)` every trace is a combination of the block
characters, `t = Σ_λ c_λ · χ_λ`. Two such traces matter here and they differ **only in the
weight**:

| trace | `c_λ` | Gram determinant |
|---|---|---|
| regular, `x ↦ tr(L_x)` | `d_λ` | `∏_λ ± d_λ^(d_λ²)` |
| canonical symmetrizing `τ`, `τ(T_w) = δ_{w,1}` | `1/s_λ` | `∏_λ ± s_λ^(−d_λ²)` |

`s_λ` is the **Schur element** of the block, and the second row is Geck–Pfeiffer's identity.
Proving the *weighted* statement therefore subsumes
`QOU.MathlibExt.regTraceGram_pi_matrix_det` (the regular case, `c_λ = d_λ`) and supplies the
determinant side of the symmetrizing case at the same time.

## What is proved

* `weightedGram_det` — the determinant, for any weights.
* `weightedGram_det_ne_zero_iff` — it is nonzero **iff every weight is nonzero**. With
  `c_λ = 1/s_λ` this reads *"the Gram of `τ` is nondegenerate iff every Schur element is
  nonzero"*, which is exactly the equivalence `SchurElementCriterion` currently assumes.
* `weightedGram_regular` — the regular trace is the `c_λ = d_λ` case, so the merged result is
  recovered rather than duplicated.

## What is NOT proved, and what still stands between here and the criterion

Two algebra-specific facts, neither of which this file touches:

1. **That `H_n(q)` carries the canonical symmetrizing trace `τ` at all**, with
   `τ(T_w) = δ_{w,1}`. Mathlib has no symmetric-algebra theory — there is no occurrence of
   the word *symmetrizing* anywhere in it — and the corpus has none either.
2. **That `τ`'s weights are `1/s_λ` for the Wenzl Schur element** formalised in
   `QOU.MathlibExt.WenzlSchurElement.schurElement`. That identification *is* the content of
   the Schur element and is where the `q`-dependence enters.

Until both land, `SchurElementCriterion` stays a cited class and must not be given an
instance. **In particular the shortcut of discharging it from `heckeWedderburn`** — legal,
since semisimplicity is separately available — **is refused**: the implication would hold
with the Schur elements doing no work at all, which would misrepresent a Wedderburn result as
a Schur-theoretic one.
-/

namespace QOU.MathlibExt

open LinearMap Matrix BigOperators

section Weighted

variable {K : Type*} [Field K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- **A character-weighted trace on a product of matrix algebras**: `Σ_i c i · tr(x i)`.

Every trace on a split semisimple algebra has this shape; the regular trace and the canonical
symmetrizing trace of [geckpfeiffer2000] differ only in `c`. -/
def weightedTrace (c : ι → K) (x : ∀ i, Matrix (J i) (J i) K) : K :=
  ∑ i, c i * (x i).trace

/-- **The matrix unit `E_ab` of block `i`, as an element of the product.**

The declared return type is load-bearing: written inline, `Pi.single i (Matrix.single a b 1)`
elaborates against the WRONG family — Lean infers `ι → J _ → K` rather than the dependent
`∀ j, Matrix (J j) (J j) K` and reports an application type mismatch. Naming it fixes the
family once. -/
def blockUnit (i : ι) (a b : J i) : ∀ j, Matrix (J j) (J j) K :=
  Pi.single i (Matrix.single a b (1 : K))

omit [Fintype ι] [∀ i, Fintype (J i)] in
@[simp] theorem blockUnit_self (i : ι) (a b : J i) :
    blockUnit (K := K) i a b i = Matrix.single a b (1 : K) :=
  Pi.single_eq_same _ _

omit [Fintype ι] [∀ i, Fintype (J i)] in
@[simp] theorem blockUnit_of_ne (i : ι) (a b : J i) {j : ι} (h : j ≠ i) :
    blockUnit (K := K) i a b j = 0 :=
  Pi.single_eq_of_ne h _

/-- **The matrix-unit product rule**: `tr(E_ab · E_a'b') = δ_{b,a'} δ_{a,b'}`.

The whole Gram computation is this one identity; it is why the Gram is a permutation matrix
scaled by the weight, and hence why its determinant is a pure power. -/
theorem trace_single_mul_single {J' : Type*} [Fintype J'] [DecidableEq J'] (a b a' b' : J') :
    ((Matrix.single a b (1 : K) * Matrix.single a' b' (1 : K))).trace
      = if (b, a) = (a', b') then 1 else 0 := by
  rcases eq_or_ne b a' with rfl | hba
  · rcases eq_or_ne a b' with rfl | hab
    · simp
    · simp [Matrix.trace_single_eq_of_ne _ _ _ hab, Prod.ext_iff, hab]
  · simp [Prod.ext_iff, hba]

/-- **The Gram matrix of a weighted trace**, in the matrix-unit basis of the product. -/
def weightedGram (c : ι → K) :
    Matrix ((i : ι) × (J i × J i)) ((i : ι) × (J i × J i)) K :=
  Matrix.of fun p q =>
    weightedTrace c (blockUnit p.1 p.2.1 p.2.2 * blockUnit q.1 q.2.1 q.2.2)

/-- **Different blocks are orthogonal**: the product of matrix units from different factors is
zero in every coordinate. -/
theorem weightedGram_apply_of_ne (c : ι → K) (p q : (i : ι) × (J i × J i)) (h : p.1 ≠ q.1) :
    weightedGram c p q = 0 := by
  refine Finset.sum_eq_zero fun i _ => ?_
  rcases eq_or_ne i p.1 with rfl | hip
  · rw [Pi.mul_apply, blockUnit_of_ne _ _ _ h, mul_zero, Matrix.trace_zero, mul_zero]
  · rw [Pi.mul_apply, blockUnit_of_ne _ _ _ hip, zero_mul, Matrix.trace_zero, mul_zero]

/-- **The diagonal block is the weight times the transpose permutation.** -/
theorem weightedGram_apply_same (c : ι → K) (i : ι) (a b a' b' : J i) :
    weightedGram c ⟨i, (a, b)⟩ ⟨i, (a', b')⟩
      = c i * (if (b, a) = (a', b') then 1 else 0) := by
  rw [weightedGram, Matrix.of_apply, weightedTrace, Finset.sum_eq_single i]
  · rw [Pi.mul_apply, blockUnit_self, blockUnit_self, trace_single_mul_single]
  · intro j _ hji
    rw [Pi.mul_apply, blockUnit_of_ne _ _ _ hji, zero_mul, Matrix.trace_zero, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ i) h

/-- **The determinant of a weighted-trace Gram matrix.**

`∏_λ ± c_λ^(d_λ²)`, the sign being the signature of the transpose involution on `J λ × J λ`,
evaluated in closed form by `QOU.MathlibExt.sign_prodComm` as `(-1)^(d_λ(d_λ-1)/2)`.

With `c_λ = 1/s_λ` this is the determinant identity of [geckpfeiffer2000] Thm 7.2.6 for a
split semisimple algebra; with `c_λ = d_λ` it is the regular-trace case already merged. -/
theorem weightedGram_det (c : ι → K) :
    (weightedGram (J := J) c).det
      = ∏ i : ι, (Equiv.Perm.sign (Equiv.prodComm (J i) (J i)) : K)
          * c i ^ (Fintype.card (J i) * Fintype.card (J i)) := by
  classical
  haveI : LinearOrder ι :=
    LinearOrder.lift' (Fintype.equivFin ι) (Fintype.equivFin ι).injective
  rw [det_eq_prod_of_offDiagonal_eq_zero _ (weightedGram_apply_of_ne (J := J) c)]
  refine Finset.prod_congr rfl fun i _ => ?_
  have hblock : (Matrix.of fun a b : J i × J i => weightedGram c ⟨i, a⟩ ⟨i, b⟩)
      = (c i • (1 : Matrix (J i × J i) (J i × J i) K)).submatrix
          ⇑(Equiv.prodComm (J i) (J i)) _root_.id := by
    ext a b
    obtain ⟨a₁, a₂⟩ := a
    obtain ⟨b₁, b₂⟩ := b
    rw [Matrix.of_apply, weightedGram_apply_same]
    simp [Matrix.submatrix_apply, Matrix.one_apply, Equiv.prodComm]
  rw [hblock, Matrix.det_permute, Matrix.det_smul, Matrix.det_one, mul_one, Fintype.card_prod]

/-- **The determinant with the sign evaluated**: `∏_λ (-1)^(d_λ(d_λ-1)/2) · c_λ^(d_λ²)`.

`weightedGram_det` leaves the sign as the signature of the transpose involution, matching the
style of `QOU.MathlibExt.regTraceGram_pi_matrix_det`; `QOU.MathlibExt.sign_prodComm` evaluates
it. The two are separated because the signature is an equation in `ℤˣ` while the determinant
lives in `K`, so the substitution is a cast step rather than a rewrite. -/
theorem weightedGram_det_explicit (c : ι → K) :
    (weightedGram (J := J) c).det
      = ∏ i : ι, ((-1 : K) ^ (Fintype.card (J i) * (Fintype.card (J i) - 1) / 2))
          * c i ^ (Fintype.card (J i) * Fintype.card (J i)) := by
  rw [weightedGram_det (J := J)]
  refine Finset.prod_congr rfl fun i _ => ?_
  congr 1
  rw [sign_prodComm]
  push_cast
  ring

/-- **The Gram of a weighted trace is nondegenerate exactly when no weight vanishes.**

This is the equivalence that `QOU.MathlibExt.WenzlSchurElement.SchurElementCriterion` carries
as a cited hypothesis. Instantiated at the canonical symmetrizing trace, where `c_λ = 1/s_λ`
and `1/s ≠ 0 ↔ s ≠ 0` over a field, it reads: *the Gram of `τ` is nondegenerate iff every
Schur element is nonzero* — [geckpfeiffer2000] Thm 7.2.6.

**It is not yet an instance of that class**, and must not be made one: see the module
docstring for the two algebra-specific facts still missing. -/
theorem weightedGram_det_ne_zero_iff (c : ι → K) [∀ i, Nonempty (J i)] :
    (weightedGram (J := J) c).det ≠ 0 ↔ ∀ i, c i ≠ 0 := by
  rw [weightedGram_det (J := J), Finset.prod_ne_zero_iff]
  simp only [Finset.mem_univ, forall_const]
  refine forall_congr' fun i => ?_
  constructor
  · intro h hc
    exact h (by rw [hc, zero_pow (by positivity), mul_zero])
  · intro hc
    refine mul_ne_zero ?_ (pow_ne_zero _ hc)
    rcases Int.units_eq_one_or (Equiv.Perm.sign (Equiv.prodComm (J i) (J i))) with h | h <;>
      simp [h]

/-- **The regular trace is the `c_λ = d_λ` case.**

So `QOU.MathlibExt.regTraceGram_pi_matrix_det` is the weight-`d` specialisation of
`weightedGram_det`, not an independent result. -/
theorem weightedTrace_card_eq_regTraceForm
    [∀ i, FiniteDimensional K (Matrix (J i) (J i) K)]
    (x : ∀ i, Matrix (J i) (J i) K) :
    weightedTrace (fun i => (Fintype.card (J i) : K)) x
      = regTraceForm K (∀ i, Matrix (J i) (J i) K) x 1 := by
  rw [regTraceForm_pi, weightedTrace]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Pi.one_apply, regTraceForm_matrix, mul_one]

end Weighted

end QOU.MathlibExt
