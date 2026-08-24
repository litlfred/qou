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

/-! ### Grouping on the *other* side — and why the length depends on which

`exists_separated_representation_monomial` groups the monomials of `P` by their `x`-part, so
the representation has one term per **`x`-monomial**.  Mahler's bound is `n ≤ r_m + 1`: one
term per **`y`-monomial**, with `y` the single split-off variable.  Those are wildly different
counts — `∏_{h<m}(r_h+1)` against `r_m+1` — and only the second is what the recursion's error
term `t = r/D₁` can afford.

⚠ So the side you group on is not a presentation choice.  The results below mirror the
grouping and, unlike the originals, state the index set **explicitly** rather than
existentially — the whole point is to count it. -/

/-- **The mirror of `exists_separated_representation_monomial`: group by the `y`-part.**

Now the *right* factors are bare monomials and the left ones collect the coefficients, so the
count is the number of distinct `y`-parts. -/
theorem exists_separated_representation_monomial_right [DecidableEq τ]
    (P : MvPolynomial (σ ⊕ τ) R) :
    ∃ φ : (τ →₀ ℕ) → MvPolynomial σ R,
      P = ∑ j ∈ P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2),
            (rename Sum.inl (φ j) : MvPolynomial (σ ⊕ τ) R)
              * rename Sum.inr (monomial j (1 : R)) := by
  refine ⟨fun j =>
    ∑ n ∈ P.support.filter (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2 = j),
      monomial (Finsupp.sumFinsuppEquivProdFinsupp n).1 (coeff n P), ?_⟩
  conv_lhs => rw [as_sum P]
  rw [← Finset.sum_fiberwise_of_maps_to
    (g := fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)
    (t := P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2))
    (fun n hn => Finset.mem_image_of_mem _ hn)
    (fun n => monomial n (coeff n P))]
  refine Finset.sum_congr rfl fun j _ => ?_
  dsimp only
  rw [map_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun n hn => ?_
  obtain ⟨-, hnj⟩ := Finset.mem_filter.mp hn
  rw [← monomial_sumElim_eq, ← hnj, ← eq_sumElim]

/-- The `Fin r`-indexed form, with `r` pinned to the number of distinct `y`-parts. -/
theorem exists_separated_representation_fin_right [DecidableEq τ]
    (P : MvPolynomial (σ ⊕ τ) R) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ R) (ψ : Fin r → MvPolynomial τ R),
      r = (P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).card ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr (ψ k) := by
  obtain ⟨φ₀, hP⟩ := exists_separated_representation_monomial_right P
  refine ⟨(P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).card,
    fun k => φ₀ (((P.support.image
      (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).equivFin.symm k : τ →₀ ℕ)),
    fun k => monomial (((P.support.image
      (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).equivFin.symm k : τ →₀ ℕ)) (1 : R),
    rfl, ?_⟩
  conv_lhs => rw [hP]
  rw [← Finset.sum_coe_sort]
  exact (Equiv.sum_comp
    (P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).equivFin.symm
    (fun i : { x // x ∈ P.support.image
        (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2) } =>
      (rename Sum.inl (φ₀ (i : τ →₀ ℕ)) : MvPolynomial (σ ⊕ τ) R)
        * rename Sum.inr (monomial (i : τ →₀ ℕ) (1 : R)))).symm

/-- **Mahler's `n ≤ r_m + 1`**, for a single split-off variable.

With `τ = Unit` a `y`-part is determined by one exponent, and that exponent is at most the
degree of `P` in the split-off variable.  So the number of distinct `y`-parts — and hence, by
the results above, the representation length — is at most `d + 1`. -/
theorem card_image_snd_le_of_degreeOf {P : MvPolynomial (σ ⊕ Unit) R} {d : ℕ}
    (hd : degreeOf (Sum.inr ()) P ≤ d) :
    (P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).card ≤ d + 1 := by
  classical
  have hsub : P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)
      ⊆ (Finset.range (d + 1)).image (fun k => Finsupp.single () k) := by
    intro j hj
    obtain ⟨n, hn, rfl⟩ := Finset.mem_image.mp hj
    refine Finset.mem_image.mpr ⟨(Finsupp.sumFinsuppEquivProdFinsupp n).2 (), ?_, ?_⟩
    · refine Finset.mem_range.mpr (Nat.lt_succ_of_le (le_trans ?_ hd))
      have hval : (Finsupp.sumFinsuppEquivProdFinsupp n).2 () = n (Sum.inr ()) := rfl
      rw [hval]
      exact monomial_le_degreeOf (Sum.inr ()) hn
    · exact (Finsupp.unique_single _).symm
  calc (P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).card
      ≤ ((Finset.range (d + 1)).image (fun k => Finsupp.single () k)).card :=
        Finset.card_le_card hsub
    _ ≤ (Finset.range (d + 1)).card := Finset.card_image_le
    _ = d + 1 := Finset.card_range _

/-! ### Factor degrees are bounded by the polynomial's

⚠ **Family-uniform data, which is what `hres` needs.**  The induction step's input quantifies
over the families realising a separated representation, so every hypothesis it carries must be
statable *before* the family is known.  The degree bound below is: it bounds the factors'
degrees by `P`'s own, which does not vary.

And it is **false without the independence hypothesis**.  Take `P = x₀y₀` and the length-`2`
representation `φ = ![x₀ + x₀⁵, −x₀⁵]`, `ψ = ![y₀, y₀]`: the sum telescopes back to `P`, but
`φ 0` has degree `5`.  What rules that out is `ψ` being dependent — and after the tenth
correction `hres` already excludes dependent families, since a dependent family's Wronskians
all vanish. -/

/-- **The factors of a separated representation have degrees bounded by the polynomial's**,
provided the *other* family is linearly independent.

The proof is the disjointness identity again: a non-zero coefficient of `φ k` gives a non-zero
vector `c`, independence of `ψ` makes `∑ cₗψₗ` non-zero, and any non-zero coefficient of that
is a coefficient of `P` at a multi-index whose `σ`-part is the one we started with. -/
theorem degreeOf_factor_le_of_indep [DecidableEq σ] {r : ℕ}
    (φ : Fin r → MvPolynomial σ R) (ψ : Fin r → MvPolynomial τ R)
    (hψ : LinearIndependent R ψ)
    (P : MvPolynomial (σ ⊕ τ) R)
    (hP : P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr (ψ k))
    (j : σ) (k : Fin r) :
    degreeOf j (φ k) ≤ degreeOf (Sum.inl j) P := by
  classical
  rw [degreeOf_eq_sup j (φ k)]
  refine Finset.sup_le fun i hi => ?_
  have hck : coeff i (φ k) ≠ 0 := mem_support_iff.mp hi
  have hcne : (∑ l, coeff i (φ l) • ψ l) ≠ 0 := fun hz =>
    hck (Fintype.linearIndependent_iff.mp hψ (fun l => coeff i (φ l)) hz k)
  obtain ⟨j', hj'⟩ : ∃ j', coeff j' (∑ l, coeff i (φ l) • ψ l) ≠ 0 := by
    by_contra hcon
    push_neg at hcon
    exact hcne (by ext j'; simpa using hcon j')
  have hsplit : coeff j' (∑ l, coeff i (φ l) • ψ l)
      = ∑ l, coeff i (φ l) * coeff j' (ψ l) := by
    rw [coeff_sum]
    exact Finset.sum_congr rfl fun l _ => by rw [coeff_smul, smul_eq_mul]
  have hPcoeff : coeff (Finsupp.sumElim i j') P ≠ 0 := by
    rw [hP, coeff_sum,
      Finset.sum_congr rfl (fun l (_ : l ∈ Finset.univ) =>
        coeff_sumElim_rename_mul (φ l) (ψ l) i j'), ← hsplit]
    exact hj'
  have hmem : Finsupp.sumElim i j' ∈ P.support := mem_support_iff.mpr hPcoeff
  have hle := monomial_le_degreeOf (Sum.inl j) hmem
  exact hle


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
      r' ≤ r ∧ LinearIndependent K φ' ∧ LinearIndependent K ψ' ∧
      ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k)
        = ∑ k, (rename Sum.inl (φ' k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ' k) := by
  induction r with
  | zero =>
      intro φ ψ
      exact ⟨0, φ, ψ, le_rfl, linearIndependent_empty_type, linearIndependent_empty_type, rfl⟩
  | succ n ih =>
      intro φ ψ
      by_cases hφ : LinearIndependent K φ
      · by_cases hψ : LinearIndependent K ψ
        · exact ⟨n + 1, φ, ψ, le_rfl, hφ, hψ, rfl⟩
        · obtain ⟨φ', ψ', heq⟩ := exists_shorter_of_psi_dep φ ψ hψ
          obtain ⟨r', φ'', ψ'', h0, h1, h2, h3⟩ := ih φ' ψ'
          exact ⟨r', φ'', ψ'', h0.trans (Nat.le_succ n), h1, h2, heq.trans h3⟩
      · obtain ⟨φ', ψ', heq⟩ := exists_shorter_of_phi_dep φ ψ hφ
        obtain ⟨r', φ'', ψ'', h0, h1, h2, h3⟩ := ih φ' ψ'
        exact ⟨r', φ'', ψ'', h0.trans (Nat.le_succ n), h1, h2, heq.trans h3⟩

theorem exists_separated_representation_indep (P : MvPolynomial (σ ⊕ τ) K) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K),
      LinearIndependent K φ ∧ LinearIndependent K ψ ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k) := by
  obtain ⟨r, φ, ψ, -, hP⟩ := exists_separated_representation_fin P
  obtain ⟨r', φ', ψ', -, h1, h2, h3⟩ := exists_indep_representation r φ ψ
  exact ⟨r', φ', ψ', h1, h2, hP.trans h3⟩


/-- **A minimum representation, with its length bounded by the number of `y`-monomials.**

The bound is what makes the induction step's error term `t = r/D₁` affordable: grouping on the
`x`-side gives `r = #{x\text{-monomials}}`, which is a *product* of degrees; grouping on the
`y`-side gives one term per `y`-monomial, and the shortening can only reduce that. -/
theorem exists_separated_representation_indep_card_le [DecidableEq τ]
    (P : MvPolynomial (σ ⊕ τ) K) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K),
      r ≤ (P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).2)).card ∧
      LinearIndependent K φ ∧ LinearIndependent K ψ ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k) := by
  obtain ⟨r, φ, ψ, hcard, hP⟩ := exists_separated_representation_fin_right P
  obtain ⟨r', φ', ψ', hle, h1, h2, h3⟩ := exists_indep_representation r φ ψ
  exact ⟨r', φ', ψ', hcard ▸ hle, h1, h2, hP.trans h3⟩

/-- **Mahler's `n ≤ r_m + 1`.**  For a single split-off variable of degree at most `d`, a
minimum separated representation has at most `d + 1` terms.

This is the bound the recursion's row cost needs: with `t = r/D₁` and `r ≤ d + 1`, the growth
condition (`RothGrowth`, which makes the split-off variable's degree the *smallest*) turns `t`
into something of order `1/ω`. -/
theorem exists_separated_representation_indep_le_degreeOf
    (P : MvPolynomial (σ ⊕ Unit) K) {d : ℕ} (hd : degreeOf (Sum.inr ()) P ≤ d) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial Unit K),
      r ≤ d + 1 ∧ LinearIndependent K φ ∧ LinearIndependent K ψ ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) K) * rename Sum.inr (ψ k) := by
  obtain ⟨r, φ, ψ, hcard, h1, h2, hP⟩ := exists_separated_representation_indep_card_le P
  exact ⟨r, φ, ψ, hcard.trans (card_image_snd_le_of_degreeOf hd), h1, h2, hP⟩


end Field

/-! ### Next

`exists_separated_representation_indep` is what the induction step wants: `Fin r`-indexed,
both families independent.  `exists_separated_representation_indep_le_degreeOf` adds Mahler's
length bound `n ≤ r_m + 1`, which is what the recursion's row cost `t = r/D₁` needs.

⚠ The length bound is entirely a matter of **which side the grouping is on**, and the two
sides are not close: the `x`-side gives one term per `x`-monomial (a *product* of degrees), the
`y`-side one term per `y`-monomial (for a single split-off variable, `d + 1`).  Both were
easy; only one is usable.

The induction step can now be fed: `exists_separated_representation_indep` produces the
representation, `det_separated_wronskian` factors its Wronskian, `BoundedOrderWronskian` turns
the two independences into non-vanishing Wronskians, and `RothInductionStep` splits the index
and the height.

⚠ The other entry the audit came back empty on is **`ω(m, ε)`** — the growth constant in
`RothGrowth`.  Nothing supplies or constrains it, and nothing can until the recursion is
written, because `ω` is whatever the recursion's error terms force it to be.  That is the one
open item that is genuinely mathematical rather than mechanical. -/

end MvPolynomial
