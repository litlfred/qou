/-
  **Generalized Wronskians in several variables** — the determinant of a matrix of
  differential operators applied to `m` multivariate polynomials.

  Bean `qou-br3w`, third Roth prerequisite.  ⚠ Mathlib-style, Mathlib imports only, no QOU
  dependency: liftable verbatim.

  ═══ WHY THE UNIVARIATE VERSION IS NOT ENOUGH ═══

  `QOU.Mathlib.GenWronskian` builds the `m × m` determinant of *iterated single*
  derivatives, and proves the dependence criterion for it in full
  (`genWronskian_eq_zero_iff`).  Roth's lemma does not consume that: its auxiliary
  polynomial lives in `m` variables, and the independence certificate it needs is a
  determinant of **products of partials of bounded total order** — one operator per row,
  chosen, not canonical.

  This file supplies the several-variable object and **both** directions: a dependence kills
  every generalized Wronskian, and — in characteristic zero — an independent family has one
  that is non-zero (`linearIndependent_iff_exists_mvGenWronskian_ne_zero`).

  ═══ WHY THE OPERATOR FAMILY IS AN ARGUMENT ═══

  In one variable there is a canonical `i`-th row: apply `d/dx` `i` times.  In several
  variables there is no such choice, and the choice matters: taking the same operator twice
  gives a matrix with two equal rows, whose determinant vanishes whatever the polynomials
  are.  So `D : Fin m → List σ` is an explicit parameter, and the theorem below is *for
  every* `D` while the certificate it powers is *for some* `D`.

  `mvGenWronskian_one_X` pins that this is not vacuous — some family does give a non-zero
  determinant.

  ═══ WHY `pderivList` IS A LINEAR MAP ═══

  The operator is defined as a composite of `Derivation.toLinearMap`s rather than a raw
  function.  That is the whole trick: the Wronskian argument needs exactly that the operator
  carries a constant-coefficient combination through, and for a bundled linear map that is
  `map_sum` and `map_smul` rather than an induction.

  ⚠ **Characteristic.**  Ordinary partials are used, not Hasse derivatives.  That is correct
  for Roth, which lives over number fields, but it confines the **converse** to characteristic
  zero: the bridge from coefficients to derivatives rescales each row by a positive integer,
  and in characteristic `p` those integers can vanish in `K`.  The dependence direction is
  characteristic-free; the converse is not, and not removably so.
-/
import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.RingTheory.MvPolynomial.Basic
import Mathlib.LinearAlgebra.Matrix.Nondegenerate
import Mathlib.LinearAlgebra.LinearIndependent.Basic

namespace MvPolynomial

open Matrix

variable {σ R : Type*} [CommRing R]

/-- Iterated partial derivative along a list of variables, **as a linear map** — which is
what makes the linearity the Wronskian argument needs free rather than proved. -/
noncomputable def pderivList (l : List σ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  l.foldr (fun j L => (pderiv j).toLinearMap ∘ₗ L) LinearMap.id

@[simp]
theorem pderivList_nil : pderivList (R := R) ([] : List σ) = LinearMap.id := rfl

@[simp]
theorem pderivList_cons (j : σ) (l : List σ) :
    pderivList (R := R) (j :: l) = (pderiv j).toLinearMap ∘ₗ pderivList l := rfl

/-- A differential operator carries a constant-coefficient combination through.

This is the only property of the operators the Wronskian argument uses — in particular it
never needs them to commute, which is why no ordering condition appears on `D`. -/
theorem pderivList_sum_C_mul {m : ℕ} (l : List σ) (c : Fin m → R)
    (f : Fin m → MvPolynomial σ R) :
    pderivList l (∑ j, C (c j) * f j) = ∑ j, C (c j) * pderivList l (f j) := by
  rw [map_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [← smul_eq_C_mul, ← smul_eq_C_mul, map_smul]

/-- The **generalized Wronskian matrix** in several variables: entry `(i, j)` is the `i`-th
differential operator applied to `f j`. -/
noncomputable def mvWronskianMatrix {m : ℕ} (D : Fin m → List σ)
    (f : Fin m → MvPolynomial σ R) : Matrix (Fin m) (Fin m) (MvPolynomial σ R) :=
  Matrix.of fun i j => pderivList (D i) (f j)

@[simp]
theorem mvWronskianMatrix_apply {m : ℕ} (D : Fin m → List σ) (f : Fin m → MvPolynomial σ R)
    (i j : Fin m) : mvWronskianMatrix D f i j = pderivList (D i) (f j) := rfl

/-- The **generalized Wronskian** in several variables, against a chosen family of `m`
differential operators. -/
noncomputable def mvGenWronskian {m : ℕ} (D : Fin m → List σ)
    (f : Fin m → MvPolynomial σ R) : MvPolynomial σ R :=
  (mvWronskianMatrix D f).det

/-- **A constant linear dependence kills every generalized Wronskian.**

The direction Roth's lemma consumes, via its contrapositive: if *some* generalized
Wronskian is non-zero, the family is linearly independent over the constants.

The proof is the same one the univariate file uses — the constant vector sits in the kernel
of the matrix, so the determinant vanishes — and it works verbatim because
`pderivList_sum_C_mul` is all that was ever needed of the derivative. -/
theorem mvGenWronskian_eq_zero_of_dependent [IsDomain R] {m : ℕ} (D : Fin m → List σ)
    (f : Fin m → MvPolynomial σ R) (c : Fin m → R) (hc : c ≠ 0)
    (h : ∑ j, C (c j) * f j = 0) : mvGenWronskian D f = 0 := by
  classical
  set v : Fin m → MvPolynomial σ R := fun j => C (c j) with hv
  have hvne : v ≠ 0 := by
    intro hzero
    refine hc (_root_.funext fun j => ?_)
    have : C (c j) = (0 : MvPolynomial σ R) := congrFun hzero j
    exact C_eq_zero.mp this
  refine Matrix.exists_mulVec_eq_zero_iff.mp ⟨v, hvne, ?_⟩
  refine _root_.funext fun i => ?_
  simp only [Matrix.mulVec, dotProduct, mvWronskianMatrix, Matrix.of_apply, hv, Pi.zero_apply]
  have key : ∑ j, pderivList (D i) (f j) * C (c j)
      = pderivList (D i) (∑ j, C (c j) * f j) := by
    rw [pderivList_sum_C_mul]
    exact Finset.sum_congr rfl fun j _ => mul_comm _ _
  rw [key, h, map_zero]

/-- ⚠ **Non-vacuity.**  `mvGenWronskian_eq_zero_of_dependent` is used through its
contrapositive, which certifies nothing if every generalized Wronskian vanishes
identically.  It does not: against the operators `(id, ∂/∂x₀)` the family `(1, x₀)` gives
the identity matrix.

This also exhibits why `D` is *chosen* rather than canonical — with `D = (id, id)` the
matrix has two equal rows and the determinant vanishes for every family, dependent or not,
so a "for all `D`" independence certificate would be empty. -/
theorem mvGenWronskian_one_X :
    mvGenWronskian (R := ℚ) ![[], [0]] ![1, X 0] = 1 := by
  simp [mvGenWronskian, mvWronskianMatrix, Matrix.det_fin_two, Fin.isValue]

/-! ### Towards the converse: the coefficient minor

The converse asks for an operator family witnessing independence.  The linear algebra under
it does not mention derivatives at all: a family of polynomials is independent over the base
field exactly when some `m × m` minor of its **coefficient** matrix is non-singular.  That is
proved here in full; what remains to reach the Wronskian converse is the bridge from
coefficient functionals to differential operators, which in characteristic zero is a diagonal
rescaling by factorials. -/

section CoeffMinor

variable {K : Type*} [Field K]

/-- The matrix of coefficients of `f` at the multi-indices `α`. -/
noncomputable def coeffMatrix {m : ℕ} (α : Fin m → (σ →₀ ℕ)) (f : Fin m → MvPolynomial σ K) :
    Matrix (Fin m) (Fin m) K :=
  Matrix.of fun i j => coeff (α i) (f j)

/-- **An independent family has a non-singular coefficient minor.**

Induction on `m`, by cofactor expansion along the new row. If *every* extension of the
inductive minor were singular, the cofactors along that row would give a fixed linear
relation `∑ⱼ cⱼ · coeff β (fⱼ) = 0` holding at **every** multi-index `β` — and a relation
holding at every coefficient is a relation between the polynomials themselves. The cofactor
in the last column is the inductive minor, so `c` is not the zero vector, contradicting
independence.

⚠ The cofactors must not depend on `β`, which is why the expansion is along the *last* row:
deleting it removes every entry `β` occurs in. -/
theorem exists_coeffMatrix_det_ne_zero :
    ∀ {m : ℕ} (f : Fin m → MvPolynomial σ K), LinearIndependent K f →
      ∃ α : Fin m → (σ →₀ ℕ), (coeffMatrix α f).det ≠ 0 := by
  intro m
  induction m with
  | zero =>
    intro f _
    exact ⟨fun i => i.elim0, by simp [coeffMatrix]⟩
  | succ n ih =>
    intro f hf
    have hinit : LinearIndependent K (Fin.init f) :=
      hf.comp Fin.castSucc (Fin.castSucc_injective n)
    obtain ⟨α', hα'⟩ := ih (Fin.init f) hinit
    by_contra hcon
    push_neg at hcon
    set N : (σ →₀ ℕ) → Matrix (Fin (n+1)) (Fin (n+1)) K :=
      fun β => coeffMatrix (Fin.snoc α' β) f with hN
    set c : Fin (n+1) → K :=
      fun j => (-1) ^ ((Fin.last n : ℕ) + (j : ℕ)) *
        ((N 0).submatrix (Fin.last n).succAbove j.succAbove).det with hc
    have hsub : ∀ (β : σ →₀ ℕ) (j : Fin (n+1)),
        (N β).submatrix (Fin.last n).succAbove j.succAbove
          = (N 0).submatrix (Fin.last n).succAbove j.succAbove := by
      intro β j
      ext i k
      simp [hN, coeffMatrix, Fin.succAbove_last, Fin.snoc_castSucc]
    have hexp : ∀ β : σ →₀ ℕ, (N β).det = ∑ j, c j * coeff β (f j) := by
      intro β
      rw [Matrix.det_succ_row (N β) (Fin.last n)]
      refine Finset.sum_congr rfl fun j _ => ?_
      rw [hsub β j, hc]
      have hentry : N β (Fin.last n) j = coeff β (f j) := by
        simp [hN, coeffMatrix, Fin.snoc_last]
      rw [hentry]
      ring
    have hzero : ∑ j, c j • f j = 0 := by
      ext β
      have hβ := hexp β
      rw [hcon (Fin.snoc α' β)] at hβ
      simpa [coeff_sum, coeff_smul, smul_eq_mul] using hβ.symm
    have hlast : c (Fin.last n) ≠ 0 := by
      have hminor : (N 0).submatrix (Fin.last n).succAbove (Fin.last n).succAbove
          = coeffMatrix α' (Fin.init f) := by
        ext i k
        simp [hN, coeffMatrix, Fin.succAbove_last, Fin.snoc_castSucc, Fin.init]
      have hsign : (-1 : K) ^ ((Fin.last n : ℕ) + ((Fin.last n : ℕ))) = 1 := by
        rw [← two_mul, pow_mul]; norm_num
      rw [hc]
      simp only [hminor, hsign, one_mul]
      exact hα'
    exact hlast (Fintype.linearIndependent_iff.mp hf c hzero (Fin.last n))

/-- A non-singular coefficient minor certifies independence. -/
theorem linearIndependent_of_coeffMatrix_det_ne_zero {m : ℕ} (α : Fin m → (σ →₀ ℕ))
    (f : Fin m → MvPolynomial σ K) (h : (coeffMatrix α f).det ≠ 0) :
    LinearIndependent K f := by
  classical
  rw [Fintype.linearIndependent_iff]
  intro c hc
  have hker : coeffMatrix α f *ᵥ c = 0 := by
    funext i
    have hi : coeff (α i) (∑ j, c j • f j) = 0 := by rw [hc]; simp
    rw [coeff_sum] at hi
    simp only [Matrix.mulVec, dotProduct, coeffMatrix, Matrix.of_apply, Pi.zero_apply]
    rw [← hi]
    exact Finset.sum_congr rfl fun j _ => by rw [coeff_smul, smul_eq_mul]; ring
  intro i
  exact congrFun (Matrix.eq_zero_of_mulVec_eq_zero h hker) i

/-- **Independence is exactly a non-singular coefficient minor.** -/
theorem linearIndependent_iff_exists_coeffMatrix_det_ne_zero {m : ℕ}
    (f : Fin m → MvPolynomial σ K) :
    LinearIndependent K f ↔ ∃ α : Fin m → (σ →₀ ℕ), (coeffMatrix α f).det ≠ 0 :=
  ⟨exists_coeffMatrix_det_ne_zero f, fun ⟨α, h⟩ =>
    linearIndependent_of_coeffMatrix_det_ne_zero α f h⟩

end CoeffMinor

/-! ### The bridge from coefficients to derivatives

`exists_coeffMatrix_det_ne_zero` produces multi-indices; the Wronskian needs differential
operators.  In characteristic zero the two differ by a positive-integer factor per row,
which is invisible to a determinant being non-zero. -/

section Bridge

/-- Differentiating shifts the coefficient index and multiplies by the exponent. -/
theorem coeff_pderiv [DecidableEq σ] (j : σ) (γ : σ →₀ ℕ) (g : MvPolynomial σ R) :
    coeff γ (pderiv j g) = ((γ j : R) + 1) * coeff (γ + Finsupp.single j 1) g := by
  induction g using MvPolynomial.induction_on' with
  | monomial s a =>
    rw [pderiv_monomial, coeff_monomial, coeff_monomial]
    by_cases h : s = γ + Finsupp.single j 1
    · subst h
      have hsub : γ + Finsupp.single j 1 - Finsupp.single j 1 = γ := by simp
      rw [hsub, if_pos rfl, if_pos rfl]
      simp only [Finsupp.add_apply, Finsupp.single_eq_same]
      push_cast
      ring
    · rw [if_neg h, mul_zero]
      by_cases h2 : s - Finsupp.single j 1 = γ
      · -- ⚠ the degenerate case: truncated subtraction fixed `s`, which forces `sⱼ = 0`,
        -- and `pderiv_monomial`'s factor `sⱼ` then kills the term anyway
        have hsj : s j = 0 := by
          by_contra hne
          apply h
          have hle : Finsupp.single j 1 ≤ s := by
            rw [Finsupp.single_le_iff]; omega
          rw [← h2, tsub_add_cancel_of_le hle]
        rw [if_pos h2, hsj]
        simp
      · rw [if_neg h2]
  | add p q hp hq => simp [hp, hq]; ring

/-- The multi-index counting occurrences of each variable in a list. -/
noncomputable def multiIndexOf (l : List σ) : σ →₀ ℕ := (l.map fun j => Finsupp.single j 1).sum

@[simp] theorem multiIndexOf_nil : multiIndexOf ([] : List σ) = 0 := rfl

@[simp] theorem multiIndexOf_cons (j : σ) (l : List σ) :
    multiIndexOf (j :: l) = Finsupp.single j 1 + multiIndexOf l := by
  simp [multiIndexOf]

theorem multiIndexOf_append (l₁ l₂ : List σ) :
    multiIndexOf (l₁ ++ l₂) = multiIndexOf l₁ + multiIndexOf l₂ := by
  simp [multiIndexOf, List.sum_append]

theorem multiIndexOf_replicate (j : σ) (n : ℕ) :
    multiIndexOf (List.replicate n j) = Finsupp.single j n := by
  induction n with
  | zero => simp
  | succ k ih => rw [List.replicate_succ, multiIndexOf_cons, ih, ← Finsupp.single_add]; ring_nf

/-- **Every multi-index is realised by a list**, so an operator family can be built from any
family of multi-indices. -/
theorem exists_multiIndexOf_eq (α : σ →₀ ℕ) : ∃ l : List σ, multiIndexOf l = α := by
  classical
  induction α using Finsupp.induction with
  | zero => exact ⟨[], rfl⟩
  | single_add a b f _ _ ih =>
    obtain ⟨l, hl⟩ := ih
    exact ⟨List.replicate b a ++ l, by rw [multiIndexOf_append, multiIndexOf_replicate, hl]⟩

/-- **Iterating `coeff_pderiv` along a list.**

⚠ The constant depends only on `γ` and `l`, **never on `g`** — the quantifier order matters,
because the whole point is to pull a single factor out of an entire matrix row. -/
theorem exists_coeff_pderivList [DecidableEq σ] (l : List σ) (γ : σ →₀ ℕ) :
    ∃ c : ℕ, 0 < c ∧ ∀ g : MvPolynomial σ R,
      coeff γ (pderivList l g) = (c : R) * coeff (γ + multiIndexOf l) g := by
  induction l generalizing γ with
  | nil => exact ⟨1, Nat.one_pos, fun g => by simp⟩
  | cons j l' ih =>
    obtain ⟨c', hc', hstep⟩ := ih (γ + Finsupp.single j 1)
    refine ⟨(γ j + 1) * c', by positivity, fun g => ?_⟩
    have hcons : pderivList (j :: l') g = pderiv j (pderivList l' g) := rfl
    rw [hcons, coeff_pderiv, hstep]
    have hidx : γ + Finsupp.single j 1 + multiIndexOf l' = γ + multiIndexOf (j :: l') := by
      rw [multiIndexOf_cons]; abel
    rw [hidx]
    push_cast
    ring

end Bridge

/-! ### The converse -/

section Converse

variable {K : Type*} [Field K]

/-- **An independent family has a non-zero generalized Wronskian.**

The Wronskian is non-zero because it is non-zero **at the origin**. Independence gives a
non-singular coefficient minor at multi-indices `α`; realise each `α i` as a list of
variables to get the operator family; then `constantCoeff` is a ring hom, so it commutes
with the determinant, and the resulting scalar matrix is `diagonal c * coeffMatrix α f`.

⚠ **Where characteristic zero enters, and why it cannot be avoided here.** The `c i` are
positive integers — products of exponents thrown off by `coeff_pderiv`. Their product must
be non-zero *in `K`*, which is exactly `CharZero`. Over `𝔽ₚ` the same construction can
produce a genuinely zero determinant from an independent family, which is the multivariate
face of the failure that makes the univariate converse false in characteristic `p`. -/
theorem exists_mvGenWronskian_ne_zero [CharZero K] [DecidableEq σ]
    {m : ℕ} (f : Fin m → MvPolynomial σ K) (hf : LinearIndependent K f) :
    ∃ D : Fin m → List σ, mvGenWronskian D f ≠ 0 := by
  classical
  obtain ⟨α, hα⟩ := exists_coeffMatrix_det_ne_zero f hf
  choose D hD using fun i => exists_multiIndexOf_eq (α i)
  choose c hcpos hc using fun i => exists_coeff_pderivList (R := K) (D i) 0
  refine ⟨D, fun hzero => ?_⟩
  have hmat : (mvWronskianMatrix D f).map (constantCoeff (R := K) (σ := σ))
      = Matrix.diagonal (fun i => (c i : K)) * coeffMatrix α f := by
    ext i j
    rw [Matrix.diagonal_mul]
    simp only [Matrix.map_apply, mvWronskianMatrix, Matrix.of_apply, coeffMatrix]
    rw [constantCoeff_eq, hc i (f j), hD i, zero_add]
  have hdet : constantCoeff (mvGenWronskian D f)
      = (∏ i, (c i : K)) * (coeffMatrix α f).det := by
    rw [mvGenWronskian, RingHom.map_det, RingHom.mapMatrix_apply, hmat, Matrix.det_mul,
      Matrix.det_diagonal]
  rw [hzero, map_zero] at hdet
  have hprod : (∏ i, (c i : K)) ≠ 0 := by
    refine Finset.prod_ne_zero_iff.mpr fun i _ => ?_
    exact Nat.cast_ne_zero.mpr (hcpos i).ne'
  exact hα (by
    rcases mul_eq_zero.mp hdet.symm with h | h
    · exact absurd h hprod
    · exact h)

/-- **Independence is exactly a non-vanishing generalized Wronskian**, in characteristic
zero — the certificate Roth's lemma consumes, in both directions. -/
theorem linearIndependent_iff_exists_mvGenWronskian_ne_zero [CharZero K] [DecidableEq σ]
    {m : ℕ} (f : Fin m → MvPolynomial σ K) :
    LinearIndependent K f ↔ ∃ D : Fin m → List σ, mvGenWronskian D f ≠ 0 := by
  classical
  refine ⟨exists_mvGenWronskian_ne_zero f, ?_⟩
  rintro ⟨D, hDne⟩
  rw [Fintype.linearIndependent_iff]
  by_contra hcon
  push_neg at hcon
  obtain ⟨c, hsum, i, hci⟩ := hcon
  refine hDne (mvGenWronskian_eq_zero_of_dependent D f c ?_ ?_)
  · intro h
    rw [h] at hci
    exact hci rfl
  · rw [← hsum]
    exact Finset.sum_congr rfl fun j _ => (smul_eq_C_mul _ _).symm

end Converse

/-! ### Next

Both directions of the generalized-Wronskian criterion are now proved, so the independence
certificate Roth's lemma needs is complete. What remains is **Roth's lemma itself** — the
induction on the number of variables — and then Roth's theorem.

⚠ One gap between this criterion and the form Roth's lemma consumes: Roth needs the operator
family to have **bounded order** (`Δᵢ` of total order `< i`, or bounded by `m`). The `D`
produced by `exists_mvGenWronskian_ne_zero` comes from arbitrary multi-indices and carries
no such bound. Getting the bound is a genuine extra step, not bookkeeping — it is where the
degree hypotheses on the auxiliary polynomial actually enter. Recorded so nothing downstream
consumes this as though the bound were already there. -/

end MvPolynomial
