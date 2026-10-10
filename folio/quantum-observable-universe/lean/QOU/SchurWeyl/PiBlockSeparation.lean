import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Tactic

/-!
# QOU.SchurWeyl.PiBlockSeparation — a subalgebra that separates blocks and covers each is everything

The algebraic crux of SW-7 (`qou-0h5k`), with no Hecke, matrix or tableau content, so it can be
checked on its own terms.

Let `A` be a subalgebra of a finite product of `R`-algebras `∏ i, B i`.  Suppose

* `A` contains a family of **scalar tuples** `(c i v)ᵢ` whose values **separate** the index set, and
* each **block projection** `A → B i` is surjective.

Then `A = ⊤`.

The point is what this argument does *not* need.  The classical Wedderburn route runs through
Jacobson density or a bicommutant theorem, neither of which is in Mathlib; the simplicity of the
blocks is never used here.  Separation puts every block idempotent `Pi.single i 1` into `A` by
finite Lagrange interpolation, and then `x = Σᵢ (Pi.single i 1) · aᵢ` reassembles any target from
per-block preimages.  Both steps are elementary.

Two Lean-shape notes carried over from `DiagonalSeparation`, which proves the single-block analogue:

* `∏ i, B i` is **not** commutative, so `Finset.prod` cannot be taken over it even though the
  interpolation factors do commute.  The product is taken in `ι → R` — which is commutative — and
  pushed across by the ring hom `p ↦ fun i => algebraMap R (B i) (p i)`, with membership recovered
  by induction on the index set.
* Separation is the entire content.  A family of scalar tuples agreeing on two indices generates a
  subalgebra containing neither block idempotent, however large the family.

LaTeX label: `lem:pi-block-separation`
-/

namespace QOU.SchurWeyl

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {R : Type*} [Field R]
variable {B : ι → Type*} [∀ i, Ring (B i)] [∀ i, Algebra R (B i)]
variable {V : Type*} [Nonempty V]

/-- The scalar-tuple ring hom `(ι → R) →+* (∀ i, B i)`, `p ↦ fun i => algebraMap R (B i) (p i)`.
This is what lets the interpolation product be taken in a commutative ring. -/
def piScalarHom : (ι → R) →+* (∀ i, B i) :=
  Pi.ringHom fun i => (algebraMap R (B i)).comp (Pi.evalRingHom (fun _ : ι => R) i)

omit [Fintype ι] [DecidableEq ι] in
@[simp] theorem piScalarHom_apply (p : ι → R) (i : ι) :
    (piScalarHom (B := B) p) i = algebraMap R (B i) (p i) := rfl

/-- **Separating scalar tuples put every block idempotent in the subalgebra.**  Finite Lagrange
interpolation: for each `j ≠ i` pick a tuple separating `i` from `j`, and multiply the normalised
differences.  The product is `1` in block `i` and `0` in every other block. -/
theorem piSingle_one_mem_of_separating (A : Subalgebra R (∀ i, B i)) (c : ι → V → R)
    (hz : ∀ v : V, piScalarHom (B := B) (fun i => c i v) ∈ A)
    (hsep : ∀ i j : ι, i ≠ j → ∃ v : V, c i v ≠ c j v) (i : ι) :
    Pi.single i (1 : B i) ∈ A := by
  classical
  have htot : ∀ j : ι, ∃ v : V, j ≠ i → c i v ≠ c j v := by
    intro j
    by_cases h : j = i
    · exact ⟨Classical.arbitrary V, fun hne => absurd h hne⟩
    · obtain ⟨v, hv⟩ := hsep i j (Ne.symm h)
      exact ⟨v, fun _ => hv⟩
  choose w hw using htot
  set g : ι → ι → R := fun j U => (c i (w j) - c j (w j))⁻¹ * (c U (w j) - c j (w j)) with hg
  -- each factor is in `A`: a scalar multiple of (separating tuple − constant tuple)
  have hfactor : ∀ j : ι, piScalarHom (B := B) (fun U => g j U) ∈ A := by
    intro j
    have hrw : piScalarHom (B := B) (fun U => g j U)
        = (c i (w j) - c j (w j))⁻¹ •
            (piScalarHom (B := B) (fun U => c U (w j))
              - (c j (w j)) • (1 : ∀ i, B i)) := by
      funext U
      simp only [piScalarHom_apply, Pi.smul_apply, Pi.sub_apply, Pi.one_apply, hg,
        Algebra.algebraMap_eq_smul_one, smul_sub, smul_smul]
      ring_nf
      module
    rw [hrw]
    exact Subalgebra.smul_mem _
      (sub_mem (hz (w j)) (Subalgebra.smul_mem _ (one_mem _) _)) _
  -- the interpolation product, taken in the commutative ring `ι → R`
  have hprod : ∀ s : Finset ι, piScalarHom (B := B) (∏ j ∈ s, (fun U => g j U)) ∈ A := by
    intro s
    refine Finset.induction_on s ?_ ?_
    · simpa only [Finset.prod_empty, map_one] using one_mem A
    · intro j t hj ih
      rw [Finset.prod_insert hj, map_mul]
      exact mul_mem (hfactor j) ih
  have hmem := hprod (Finset.univ.erase i)
  -- the product is `1` at `i` and `0` elsewhere
  have hval_i : (∏ j ∈ Finset.univ.erase i, (fun U => g j U)) i = 1 := by
    rw [Finset.prod_apply]
    refine Finset.prod_eq_one (fun j hj => ?_)
    have hji : j ≠ i := (Finset.mem_erase.mp hj).1
    have hne : c i (w j) - c j (w j) ≠ 0 := sub_ne_zero_of_ne (hw j hji)
    show (c i (w j) - c j (w j))⁻¹ * (c i (w j) - c j (w j)) = 1
    exact inv_mul_cancel₀ hne
  have hval_ne : ∀ U : ι, U ≠ i → (∏ j ∈ Finset.univ.erase i, (fun U => g j U)) U = 0 := by
    intro U hU
    rw [Finset.prod_apply]
    refine Finset.prod_eq_zero (Finset.mem_erase.mpr ⟨hU, Finset.mem_univ U⟩) ?_
    show (c i (w U) - c U (w U))⁻¹ * (c U (w U) - c U (w U)) = 0
    rw [sub_self, mul_zero]
  have heq : piScalarHom (B := B) (∏ j ∈ Finset.univ.erase i, (fun U => g j U))
      = Pi.single i (1 : B i) := by
    funext U
    by_cases hUi : U = i
    · subst hUi
      rw [piScalarHom_apply, hval_i, map_one, Pi.single_eq_same]
    · rw [piScalarHom_apply, hval_ne U hUi, map_zero, Pi.single_eq_of_ne hUi]
  exact heq ▸ hmem

/-- **Block idempotents plus per-block surjectivity give everything.**  Any target is the sum of
its blocks, and each block is `(Pi.single i 1) · aᵢ` for a preimage `aᵢ`. -/
theorem eq_top_of_piSingle_of_blockSurj (A : Subalgebra R (∀ i, B i))
    (hidem : ∀ i : ι, Pi.single i (1 : B i) ∈ A)
    (hsurj : ∀ (i : ι) (x : B i), ∃ a ∈ A, a i = x) : A = ⊤ := by
  classical
  refine eq_top_iff.mpr (fun x _ => ?_)
  have hsplit : x = ∑ i : ι, Pi.single i (x i) := (Finset.univ_sum_single x).symm
  rw [hsplit]
  refine sum_mem (fun i _ => ?_)
  obtain ⟨a, ha, hax⟩ := hsurj i (x i)
  have hmul : Pi.single i (1 : B i) * a = Pi.single i (x i) := by
    funext j
    rw [Pi.mul_apply]
    by_cases hji : j = i
    · subst hji
      rw [Pi.single_eq_same, Pi.single_eq_same, one_mul, hax]
    · rw [Pi.single_eq_of_ne hji, Pi.single_eq_of_ne hji, zero_mul]
  rw [← hmul]
  exact mul_mem (hidem i) ha

/-- **The packaged criterion.**  A subalgebra whose scalar tuples separate the blocks and whose
block projections are surjective is the whole product. -/
theorem eq_top_of_separating_of_blockSurj (A : Subalgebra R (∀ i, B i)) (c : ι → V → R)
    (hz : ∀ v : V, piScalarHom (B := B) (fun i => c i v) ∈ A)
    (hsep : ∀ i j : ι, i ≠ j → ∃ v : V, c i v ≠ c j v)
    (hsurj : ∀ (i : ι) (x : B i), ∃ a ∈ A, a i = x) : A = ⊤ :=
  eq_top_of_piSingle_of_blockSurj A
    (fun i => piSingle_one_mem_of_separating A c hz hsep i) hsurj

end QOU.SchurWeyl
