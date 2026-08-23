/-
  **Separated representations** — every polynomial in two variable groups is a finite sum
  `∑ₖ φₖ(x)·ψₖ(y)`.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/SeparatedHeight.lean` for
  `sumElim_eq_mapDomain_add` and `eq_sumElim`.

  ═══ THE AUDIT FOUND THIS MISSING ═══

  Now that Roth's lemma has a statement (`QOU/Mathlib/RothLemmaStatement.lean`), its
  hypotheses can be matched against named theorems.  Doing that for the induction step: the
  separated machinery — `RothInductionStep`, `SeparatedIndex`, `SeparatedHeight`,
  `det_separated_wronskian` — all *takes* a separated representation
  `∑ₖ rename inl (φ k) * rename inr (ψ k)` as given, and **nothing in the corpus produced
  one.**  Checked by grep before writing: no `exists_separated…` of any kind.

  ═══ ⚠ WHAT THIS GIVES, AND WHAT IT DOES NOT ═══

  `exists_separated_representation_monomial` gives a representation whose `φ` are **distinct
  monomials**, hence linearly independent (`linearIndependent_monomial`).  That is the half
  the bounded-order Wronskian criterion needs on the `x` side.

  Two gaps were recorded here when the module was first written, and **both are now closed**:

  * the `ψ` were not independent — `exists_separated_representation_indep` fixes that by
    reducing to a minimal-length representation, in which both families are independent;
  * the indexing was by `Finset (σ →₀ ℕ)` rather than `Fin r` —
    `exists_separated_representation_fin` fixes that via `Finset.equivFin`.

  ⚠ The minimal version needs a **field**: the reduction divides by a non-zero coefficient of
  the dependence relation.  Roth's lemma works over `ℚ`, so this costs nothing there, but the
  crude and grouped versions above hold over any `CommRing` and the minimal one does not.
-/
import QOU.Mathlib.SeparatedHeight
import Mathlib.RingTheory.MvPolynomial.Basic

namespace MvPolynomial

variable {σ τ R : Type*} [CommRing R]

/-- A monomial on `σ ⊕ τ` splits as a product, with the coefficient on the left factor. -/
theorem monomial_sumElim_eq (i : σ →₀ ℕ) (j : τ →₀ ℕ) (c : R) :
    monomial (Finsupp.sumElim i j) c
      = (rename Sum.inl (monomial i c) : MvPolynomial (σ ⊕ τ) R)
        * rename Sum.inr (monomial j (1 : R)) := by
  rw [rename_monomial, rename_monomial, monomial_mul, mul_one, sumElim_eq_mapDomain_add]

/-- The same split with the coefficient on the *right* factor — the orientation the grouped
representation below needs, since there the left factors are bare monomials. -/
theorem monomial_sumElim_eq' (i : σ →₀ ℕ) (j : τ →₀ ℕ) (c : R) :
    monomial (Finsupp.sumElim i j) c
      = (rename Sum.inl (monomial i (1 : R)) : MvPolynomial (σ ⊕ τ) R)
        * rename Sum.inr (monomial j c) := by
  rw [rename_monomial, rename_monomial, monomial_mul, one_mul, sumElim_eq_mapDomain_add]

/-- **Every polynomial has a separated representation**, indexed by its own support.

The crude version: one term per monomial of `P`.  ⚠ Its `φ` are *not* independent — distinct
monomials of `P` can share an `x`-part.  Use the grouped version below when independence
matters. -/
theorem exists_separated_representation (P : MvPolynomial (σ ⊕ τ) R) :
    ∃ (s : Finset ((σ ⊕ τ) →₀ ℕ)) (φ : ((σ ⊕ τ) →₀ ℕ) → MvPolynomial σ R)
      (ψ : ((σ ⊕ τ) →₀ ℕ) → MvPolynomial τ R),
      P = ∑ n ∈ s, (rename Sum.inl (φ n) : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr (ψ n) := by
  classical
  refine ⟨P.support,
    fun n => monomial (Finsupp.sumFinsuppEquivProdFinsupp n).1 (coeff n P),
    fun n => monomial (Finsupp.sumFinsuppEquivProdFinsupp n).2 (1 : R), ?_⟩
  conv_lhs => rw [as_sum P]
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [← monomial_sumElim_eq, ← eq_sumElim]

/-- **A separated representation with linearly independent `φ`.**

Grouping the monomials of `P` by their `x`-part makes the left factors *distinct* monomials,
which `linearIndependent_monomial` shows are independent.  The `ψ` collect the corresponding
`y`-parts.

⚠ The `ψ` need not be independent, and Roth's lemma wants a representation where both families
are — see the module header. -/
theorem exists_separated_representation_monomial (P : MvPolynomial (σ ⊕ τ) R) :
    ∃ (t : Finset (σ →₀ ℕ)) (ψ : (σ →₀ ℕ) → MvPolynomial τ R),
      P = ∑ i ∈ t, (rename Sum.inl (monomial i (1 : R)) : MvPolynomial (σ ⊕ τ) R)
            * rename Sum.inr (ψ i) := by
  classical
  refine ⟨P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1),
    fun i => ∑ n ∈ P.support.filter (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1 = i),
      monomial (Finsupp.sumFinsuppEquivProdFinsupp n).2 (coeff n P), ?_⟩
  conv_lhs => rw [as_sum P]
  rw [← Finset.sum_fiberwise_of_maps_to
    (g := fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1)
    (t := P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1))
    (fun n hn => Finset.mem_image_of_mem _ hn)
    (fun n => monomial n (coeff n P))]
  refine Finset.sum_congr rfl fun i _ => ?_
  dsimp only
  rw [map_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun n hn => ?_
  obtain ⟨-, hni⟩ := Finset.mem_filter.mp hn
  rw [← monomial_sumElim_eq', ← hni, ← eq_sumElim]

/-- Distinct monomials are linearly independent: they are part of `basisMonomials`. -/
theorem linearIndependent_monomial (t : Set (σ →₀ ℕ)) :
    LinearIndependent R (fun i : t => (monomial (i : σ →₀ ℕ) (1 : R) : MvPolynomial σ R)) := by
  have h := (basisMonomials σ R).linearIndependent
  rw [coe_basisMonomials] at h
  exact h.comp _ Subtype.val_injective

/-- **The `Fin r`-indexed form**, which is what `det_separated_wronskian` and the
bounded-order Wronskian criterion actually consume, together with independence of the `φ`.

Reindexing is `Finset.equivFin`; independence transports because `equivFin.symm` is injective.

⚠ Still only the `φ` are independent.  See the module header. -/
theorem exists_separated_representation_fin (P : MvPolynomial (σ ⊕ τ) R) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ R) (ψ : Fin r → MvPolynomial τ R),
      LinearIndependent R φ ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr (ψ k) := by
  classical
  obtain ⟨t, ψ₀, hP⟩ := exists_separated_representation_monomial P
  refine ⟨t.card, fun k => monomial ((t.equivFin.symm k : σ →₀ ℕ)) (1 : R),
    fun k => ψ₀ ((t.equivFin.symm k : σ →₀ ℕ)), ?_, ?_⟩
  · exact (linearIndependent_monomial (t : Set (σ →₀ ℕ))).comp _ t.equivFin.symm.injective
  · rw [hP, ← Finset.sum_coe_sort]
    exact (Equiv.sum_comp t.equivFin.symm
      (fun i : { x // x ∈ t } =>
        (rename Sum.inl (monomial (i : σ →₀ ℕ) (1 : R)) : MvPolynomial (σ ⊕ τ) R)
          * rename Sum.inr (ψ₀ (i : σ →₀ ℕ)))).symm

/-! ### Minimal representations

⚠ **Field required** from here on: the reduction below divides by a non-zero coefficient of a
dependence relation. -/

section Field

variable {K : Type*} [Field K]


theorem exists_shorter_of_psi_dep {n : ℕ}
    (φ : Fin (n + 1) → MvPolynomial σ K) (ψ : Fin (n + 1) → MvPolynomial τ K)
    (h : ¬ LinearIndependent K ψ) :
    ∃ (φ' : Fin n → MvPolynomial σ K) (ψ' : Fin n → MvPolynomial τ K),
      ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k)
        = ∑ k, (rename Sum.inl (φ' k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ' k) := by
  classical
  obtain ⟨c, hsum, j, hcj⟩ := Fintype.not_linearIndependent_iff.mp h
  refine ⟨fun i => φ (j.succAbove i) - (c (j.succAbove i) / c j) • φ j,
          fun i => ψ (j.succAbove i), ?_⟩
  -- the dependence, solved for ψ j
  have h0 := Fin.sum_univ_succAbove (fun k => c k • ψ k) j
  rw [hsum] at h0
  have h1 : ∑ i : Fin n, c (j.succAbove i) • ψ (j.succAbove i) = -(c j • ψ j) :=
    eq_neg_of_add_eq_zero_right h0.symm
  have key : ∑ i : Fin n, (c (j.succAbove i) / c j) • ψ (j.succAbove i) = - ψ j := by
    calc ∑ i : Fin n, (c (j.succAbove i) / c j) • ψ (j.succAbove i)
        = (c j)⁻¹ • ∑ i : Fin n, c (j.succAbove i) • ψ (j.succAbove i) := by
          rw [Finset.smul_sum]
          exact Finset.sum_congr rfl fun i _ => by rw [smul_smul, div_eq_inv_mul]
      _ = (c j)⁻¹ • (-(c j • ψ j)) := by rw [h1]
      _ = - ψ j := by rw [smul_neg, smul_smul, inv_mul_cancel₀ hcj, one_smul]
  -- expand the new terms
  have expand : ∀ i : Fin n,
      (rename Sum.inl (φ (j.succAbove i) - (c (j.succAbove i) / c j) • φ j)
        : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ (j.succAbove i))
      = (rename Sum.inl (φ (j.succAbove i)) : MvPolynomial (σ ⊕ τ) K)
          * rename Sum.inr (ψ (j.succAbove i))
        - (c (j.succAbove i) / c j) •
            ((rename Sum.inl (φ j) : MvPolynomial (σ ⊕ τ) K)
              * rename Sum.inr (ψ (j.succAbove i))) := by
    intro i
    rw [map_sub, map_smul, sub_mul, smul_mul_assoc]
  rw [Fin.sum_univ_succAbove (fun k => (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K)
      * rename Sum.inr (ψ k)) j,
    Finset.sum_congr rfl (fun i (_ : i ∈ Finset.univ) => expand i), Finset.sum_sub_distrib]
  have hpull : ∑ i : Fin n, (c (j.succAbove i) / c j) •
      ((rename Sum.inl (φ j) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ (j.succAbove i)))
      = -((rename Sum.inl (φ j) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ j)) := by
    have : ∀ i : Fin n, (c (j.succAbove i) / c j) •
        ((rename Sum.inl (φ j) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ (j.succAbove i)))
        = (rename Sum.inl (φ j) : MvPolynomial (σ ⊕ τ) K)
            * rename Sum.inr ((c (j.succAbove i) / c j) • ψ (j.succAbove i)) := by
      intro i
      rw [map_smul, mul_smul_comm]
    rw [Finset.sum_congr rfl (fun i (_ : i ∈ Finset.univ) => this i), ← Finset.mul_sum,
      ← map_sum, key, map_neg, mul_neg]
  rw [hpull, sub_neg_eq_add, add_comm]


theorem exists_shorter_of_phi_dep {n : ℕ}
    (φ : Fin (n + 1) → MvPolynomial σ K) (ψ : Fin (n + 1) → MvPolynomial τ K)
    (h : ¬ LinearIndependent K φ) :
    ∃ (φ' : Fin n → MvPolynomial σ K) (ψ' : Fin n → MvPolynomial τ K),
      ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k)
        = ∑ k, (rename Sum.inl (φ' k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ' k) := by
  classical
  obtain ⟨c, hsum, j, hcj⟩ := Fintype.not_linearIndependent_iff.mp h
  refine ⟨fun i => φ (j.succAbove i),
          fun i => ψ (j.succAbove i) - (c (j.succAbove i) / c j) • ψ j, ?_⟩
  have h0 := Fin.sum_univ_succAbove (fun k => c k • φ k) j
  rw [hsum] at h0
  have h1 : ∑ i : Fin n, c (j.succAbove i) • φ (j.succAbove i) = -(c j • φ j) :=
    eq_neg_of_add_eq_zero_right h0.symm
  have key : ∑ i : Fin n, (c (j.succAbove i) / c j) • φ (j.succAbove i) = - φ j := by
    calc ∑ i : Fin n, (c (j.succAbove i) / c j) • φ (j.succAbove i)
        = (c j)⁻¹ • ∑ i : Fin n, c (j.succAbove i) • φ (j.succAbove i) := by
          rw [Finset.smul_sum]
          exact Finset.sum_congr rfl fun i _ => by rw [smul_smul, div_eq_inv_mul]
      _ = (c j)⁻¹ • (-(c j • φ j)) := by rw [h1]
      _ = - φ j := by rw [smul_neg, smul_smul, inv_mul_cancel₀ hcj, one_smul]
  have expand : ∀ i : Fin n,
      (rename Sum.inl (φ (j.succAbove i)) : MvPolynomial (σ ⊕ τ) K)
        * rename Sum.inr (ψ (j.succAbove i) - (c (j.succAbove i) / c j) • ψ j)
      = (rename Sum.inl (φ (j.succAbove i)) : MvPolynomial (σ ⊕ τ) K)
          * rename Sum.inr (ψ (j.succAbove i))
        - (c (j.succAbove i) / c j) •
            ((rename Sum.inl (φ (j.succAbove i)) : MvPolynomial (σ ⊕ τ) K)
              * rename Sum.inr (ψ j)) := by
    intro i
    rw [map_sub, map_smul, mul_sub, mul_smul_comm]
  rw [Fin.sum_univ_succAbove (fun k => (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K)
      * rename Sum.inr (ψ k)) j,
    Finset.sum_congr rfl (fun i (_ : i ∈ Finset.univ) => expand i), Finset.sum_sub_distrib]
  have hpull : ∑ i : Fin n, (c (j.succAbove i) / c j) •
      ((rename Sum.inl (φ (j.succAbove i)) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ j))
      = -((rename Sum.inl (φ j) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ j)) := by
    have hterm : ∀ i : Fin n, (c (j.succAbove i) / c j) •
        ((rename Sum.inl (φ (j.succAbove i)) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ j))
        = (rename Sum.inl ((c (j.succAbove i) / c j) • φ (j.succAbove i))
            : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ j) := by
      intro i
      rw [map_smul, smul_mul_assoc]
    rw [Finset.sum_congr rfl (fun i (_ : i ∈ Finset.univ) => hterm i), ← Finset.sum_mul,
      ← map_sum, key, map_neg, neg_mul]
  rw [hpull, sub_neg_eq_add, add_comm]

theorem exists_indep_representation (r : ℕ) :
    ∀ (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K),
    ∃ (r' : ℕ) (φ' : Fin r' → MvPolynomial σ K) (ψ' : Fin r' → MvPolynomial τ K),
      LinearIndependent K φ' ∧ LinearIndependent K ψ' ∧
      ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k)
        = ∑ k, (rename Sum.inl (φ' k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ' k) := by
  induction r with
  | zero =>
      intro φ ψ
      exact ⟨0, φ, ψ, linearIndependent_empty_type, linearIndependent_empty_type, rfl⟩
  | succ n ih =>
      intro φ ψ
      by_cases hφ : LinearIndependent K φ
      · by_cases hψ : LinearIndependent K ψ
        · exact ⟨n + 1, φ, ψ, hφ, hψ, rfl⟩
        · obtain ⟨φ', ψ', heq⟩ := exists_shorter_of_psi_dep φ ψ hψ
          obtain ⟨r', φ'', ψ'', h1, h2, h3⟩ := ih φ' ψ'
          exact ⟨r', φ'', ψ'', h1, h2, heq.trans h3⟩
      · obtain ⟨φ', ψ', heq⟩ := exists_shorter_of_phi_dep φ ψ hφ
        obtain ⟨r', φ'', ψ'', h1, h2, h3⟩ := ih φ' ψ'
        exact ⟨r', φ'', ψ'', h1, h2, heq.trans h3⟩

theorem exists_separated_representation_indep (P : MvPolynomial (σ ⊕ τ) K) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K),
      LinearIndependent K φ ∧ LinearIndependent K ψ ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k) := by
  obtain ⟨r, φ, ψ, -, hP⟩ := exists_separated_representation_fin P
  obtain ⟨r', φ', ψ', h1, h2, h3⟩ := exists_indep_representation r φ ψ
  exact ⟨r', φ', ψ', h1, h2, hP.trans h3⟩



end Field

/-! ### Next

Nothing here.  `exists_separated_representation_indep` is what the induction step wants:
`Fin r`-indexed, both families independent.

The induction step can now be fed: `exists_separated_representation_indep` produces the
representation, `det_separated_wronskian` factors its Wronskian, `BoundedOrderWronskian` turns
the two independences into non-vanishing Wronskians, and `RothInductionStep` splits the index
and the height.

⚠ The other entry the audit came back empty on is **`ω(m, ε)`** — the growth constant in
`RothGrowth`.  Nothing supplies or constrains it, and nothing can until the recursion is
written, because `ω` is whatever the recursion's error terms force it to be.  That is the one
open item that is genuinely mathematical rather than mechanical. -/

end MvPolynomial
