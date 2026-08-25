/-
  **Wronskians of separated polynomials** — the factorization that drives Roth's lemma's
  induction on the number of variables.

  Bean `qou-4lbh`.  ⚠ Staged for Mathlib; depends only on `QOU.Mathlib.MvGenWronskian`, itself
  staged, and never on QOU content.

  ═══ WHAT THIS IS FOR ═══

  Roth's lemma is an induction on the number of variables.  The step writes the auxiliary
  polynomial with its variables split into two groups,

      P = ∑ₖ φₖ(x) · ψₖ(y),

  and needs the generalized Wronskian of `P` — taken against operators drawn from *both*
  groups — to factor as an `x`-Wronskian times a `y`-Wronskian.  That is
  `det_separated_wronskian` below, and it is what reduces `m` variables to `1` and `m−1`.

  ═══ WHY IT WORKS ═══

  Two ingredients, neither deep, both needed in full:

  * **Separation.** A derivative in one group annihilates a polynomial in the other
    (`pderiv_inl_rename_inr`), so Leibniz produces no cross terms and each operator lands on
    its own factor.  Iterated along whole operator lists this is `pderivList_separated`.
  * **A determinant of separated entries factors.** If the `(i,j)` entry is `∑ₖ Aᵢₖ Bⱼₖ` the
    matrix is `A · Bᵀ`, so the determinant is `det A · det B` (`det_of_sum_mul`).

  The variable split is modelled as `σ ⊕ τ` with `rename Sum.inl` / `rename Sum.inr`, which
  makes "involves only this group" a statement about `vars` rather than a side condition
  threaded through every lemma.
-/
import QOU.Mathlib.MvGenWronskian
import Mathlib.Algebra.MvPolynomial.Variables
import Mathlib.Algebra.MvPolynomial.Rename

namespace MvPolynomial

variable {σ τ K : Type*} [CommRing K]

/-- A polynomial in the second group of variables is killed by a derivative in the first. -/
theorem pderiv_inl_rename_inr (a : σ) (q : MvPolynomial τ K) :
    pderiv (Sum.inl a) (rename Sum.inr q : MvPolynomial (σ ⊕ τ) K) = 0 := by
  classical
  refine pderiv_eq_zero_of_notMem_vars fun hmem => ?_
  have hsub := vars_rename (Sum.inr : τ → σ ⊕ τ) q hmem
  simp only [Finset.mem_image] at hsub
  obtain ⟨b, _, hb⟩ := hsub
  exact Sum.inl_ne_inr hb.symm

/-- Symmetrically, a derivative in the second group kills the first. -/
theorem pderiv_inr_rename_inl (b : τ) (p : MvPolynomial σ K) :
    pderiv (Sum.inr b) (rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) = 0 := by
  classical
  refine pderiv_eq_zero_of_notMem_vars fun hmem => ?_
  have hsub := vars_rename (Sum.inl : σ → σ ⊕ τ) p hmem
  simp only [Finset.mem_image] at hsub
  obtain ⟨c, _, hc⟩ := hsub
  exact Sum.inl_ne_inr hc

/-- **Separation:** a derivative in the first group of variables passes through a product of
a first-group factor with a second-group factor, touching only the first.

This is what makes the Wronskian of a separated polynomial factor: the two operator families
act on disjoint variable groups, so `Δ Δ' (φ ψ) = (Δφ)(Δ'ψ)` with no cross terms. -/
theorem pderiv_inl_mul_separated (a : σ) (p : MvPolynomial σ K) (q : MvPolynomial τ K) :
    pderiv (Sum.inl a) ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)
      = (rename Sum.inl (pderiv a p) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q := by
  rw [Derivation.leibniz]
  simp only [smul_eq_mul, pderiv_inl_rename_inr, mul_zero, zero_add,
    pderiv_rename Sum.inl_injective]
  ring

/-- **Separation along a whole operator list.**  An iterated partial in the first group of
variables passes through the product, touching only the first factor. -/
theorem pderivList_map_inl_separated (lx : List σ) (p : MvPolynomial σ K)
    (q : MvPolynomial τ K) :
    pderivList (lx.map Sum.inl) ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)
      = (rename Sum.inl (pderivList lx p) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q := by
  induction lx with
  | nil => simp [pderivList]
  | cons a lx' ih =>
    have hcons : pderivList ((a :: lx').map Sum.inl)
        ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)
        = pderiv (Sum.inl a)
            (pderivList (lx'.map Sum.inl)
              ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)) := rfl
    rw [hcons, ih, pderiv_inl_mul_separated]
    have : pderiv a (pderivList lx' p) = pderivList (a :: lx') p := rfl
    rw [this]

/-- Applying two operator lists in succession is applying their concatenation. -/
theorem pderivList_append (l1 l2 : List σ) (p : MvPolynomial σ K) :
    pderivList (l1 ++ l2) p = pderivList l1 (pderivList l2 p) := by
  induction l1 with
  | nil => simp [pderivList]
  | cons a l1' ih =>
    have h1 : pderivList ((a :: l1') ++ l2) p = pderiv a (pderivList (l1' ++ l2) p) := rfl
    have h2 : pderivList (a :: l1') (pderivList l2 p)
        = pderiv a (pderivList l1' (pderivList l2 p)) := rfl
    rw [h1, ih, h2]

/-- Mirror of `pderiv_inl_mul_separated` for the second group. -/
theorem pderiv_inr_mul_separated (b : τ) (p : MvPolynomial σ K) (q : MvPolynomial τ K) :
    pderiv (Sum.inr b) ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)
      = (rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (pderiv b q) := by
  rw [Derivation.leibniz]
  simp only [smul_eq_mul, pderiv_inr_rename_inl, mul_zero, add_zero,
    pderiv_rename Sum.inr_injective]

/-- Mirror of `pderivList_map_inl_separated` for the second group. -/
theorem pderivList_map_inr_separated (ly : List τ) (p : MvPolynomial σ K)
    (q : MvPolynomial τ K) :
    pderivList (ly.map Sum.inr) ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)
      = (rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (pderivList ly q) := by
  induction ly with
  | nil => simp [pderivList]
  | cons b ly' ih =>
    have hcons : pderivList ((b :: ly').map Sum.inr)
        ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)
        = pderiv (Sum.inr b)
            (pderivList (ly'.map Sum.inr)
              ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)) := rfl
    rw [hcons, ih, pderiv_inr_mul_separated]
    have hq : pderiv b (pderivList ly' q) = pderivList (b :: ly') q := rfl
    rw [hq]

/-- **The two-sided separation.**  Operators from both groups applied to a separated product
land on their own factors. -/
theorem pderivList_separated (lx : List σ) (ly : List τ) (p : MvPolynomial σ K)
    (q : MvPolynomial τ K) :
    pderivList (lx.map Sum.inl ++ ly.map Sum.inr)
        ((rename Sum.inl p : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr q)
      = (rename Sum.inl (pderivList lx p) : MvPolynomial (σ ⊕ τ) K)
        * rename Sum.inr (pderivList ly q) := by
  rw [pderivList_append, pderivList_map_inr_separated, pderivList_map_inl_separated]

open Matrix in
/-- A determinant of "separated" entries factors: the matrix is `A * Bᵀ`. -/
theorem det_of_sum_mul {S : Type*} [CommRing S] {r : ℕ} (A B : Matrix (Fin r) (Fin r) S) :
    (Matrix.of fun i j => ∑ k, A i k * B j k).det = A.det * B.det := by
  have h : (Matrix.of fun i j => ∑ k, A i k * B j k) = A * Bᵀ := by
    refine Matrix.ext fun i j => ?_
    simp [Matrix.mul_apply, Matrix.transpose_apply]
  rw [h, Matrix.det_mul, Matrix.det_transpose]

open Matrix in
/-- **The generalized Wronskian of a separated polynomial factors.**

For `P = ∑ₖ φₖ(x) ψₖ(y)` with the two variable groups disjoint, the mixed Wronskian is the
product of a Wronskian in `x` and one in `y`.

⚠ **This is the engine of Roth's lemma's induction on the number of variables**: it is what
reduces `m` variables to `1` and `m−1`.  The bounded-order criterion supplies the two factors;
this identity is what lets them be used separately. -/
theorem det_separated_wronskian {r : ℕ} (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) :
    (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr)
        (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))).det
      = (rename Sum.inl (mvGenWronskian Dx φ) : MvPolynomial (σ ⊕ τ) K)
        * rename Sum.inr (mvGenWronskian Dy ψ) := by
  classical
  have hentry : ∀ i j : Fin r,
      pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr)
        (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))
      = ∑ k, (rename Sum.inl (pderivList (Dx i) (φ k)) : MvPolynomial (σ ⊕ τ) K)
          * rename Sum.inr (pderivList (Dy j) (ψ k)) := by
    intro i j
    rw [map_sum]
    exact Finset.sum_congr rfl fun k _ => pderivList_separated _ _ _ _
  have hmat : (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr)
        (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k)))
      = Matrix.of fun i j => ∑ k,
          (Matrix.of fun (i' k' : Fin r) =>
            (rename Sum.inl (pderivList (Dx i') (φ k')) : MvPolynomial (σ ⊕ τ) K)) i k
          * (Matrix.of fun (j' k' : Fin r) =>
            (rename Sum.inr (pderivList (Dy j') (ψ k')) : MvPolynomial (σ ⊕ τ) K)) j k := by
    refine Matrix.ext fun i j => ?_
    simpa using hentry i j
  rw [hmat, det_of_sum_mul]
  congr 1
  · have hA : (Matrix.of fun (i' k' : Fin r) =>
        (rename Sum.inl (pderivList (Dx i') (φ k')) : MvPolynomial (σ ⊕ τ) K))
        = (mvWronskianMatrix Dx φ).map
            ((rename Sum.inl : MvPolynomial σ K →ₐ[K] MvPolynomial (σ ⊕ τ) K).toRingHom) := by
      refine Matrix.ext fun i' k' => ?_
      simp [mvWronskianMatrix]
    rw [hA, ← RingHom.mapMatrix_apply, ← RingHom.map_det, mvGenWronskian]
    rfl
  · have hB : (Matrix.of fun (j' k' : Fin r) =>
        (rename Sum.inr (pderivList (Dy j') (ψ k')) : MvPolynomial (σ ⊕ τ) K))
        = (mvWronskianMatrix Dy ψ).map
            ((rename Sum.inr : MvPolynomial τ K →ₐ[K] MvPolynomial (σ ⊕ τ) K).toRingHom) := by
      refine Matrix.ext fun j' k' => ?_
      simp [mvWronskianMatrix]
    rw [hB, ← RingHom.mapMatrix_apply, ← RingHom.map_det, mvGenWronskian]
    rfl

end MvPolynomial
