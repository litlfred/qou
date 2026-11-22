import UGB.GrobnerShirshov.DiamondLemma
import UGB.GrobnerShirshov.Quotient
import Mathlib.LinearAlgebra.Basis.Basic

set_option linter.unusedSectionVars false

/-!
# A Gröbner–Shirshov basis gives a normal-form basis of the quotient

`Quotient.lean` states `NormalFormBasis`: the classes of the normal-form monomials
form a `k`-basis of `A = k⟨G⟩ / (Σ)`. This file proves it from
`Diamond.reductionUnique`, for a Gröbner–Shirshov basis with unit leading
coefficients over a commutative ring. That is clause (i) ⇒ (iii) of
Bokut–Chen–Li 2011, Theorem 4.4, in the one-object case.

## The argument

1. **The normal-form map.** Choose a normal form of each representation
   (`normal_form_exists`). Uniqueness up to `CoeffEq` (`reductionUnique`) makes
   the choice descend to `FreeAlg`, and Bergman's Lemma 1.1 (`nf_add`,
   `nf_smul`) makes it `k`-linear: `nfMap : k⟨G⟩ →ₗ k⟨G⟩`.
2. **It kills the ideal.** Each generator `a·rel·b` reduces to zero in one step
   (`zeroNF_ctx`).
3. **It moves within a coset.** A reduction step subtracts a multiple of some
   `a·rel·b`, so `x − nfMap x ∈ I`.
4. **It fixes normal forms.** An element supported on normal-form monomials is
   its own normal form.

Independence: a relation `Σ gᵢ·[mᵢ] = 0` in `A` puts `X = Σ gᵢ·mᵢ` in `I`, so
`nfMap X = 0` by 2; but `X` is supported on normal-form monomials, so
`nfMap X = X` by 4. Spanning: every class is the class of its normal form by 3,
and a normal form is a combination of normal-form monomials.

## References

- G. M. Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978), Thm 1.2.
- L. A. Bokut, Y. Chen, Y. Li, *Gröbner–Shirshov bases for categories*,
  arXiv:1101.1563, Theorem 4.4.
-/

namespace UGB.GrobnerShirshov.NFBasis

open UGB.GrobnerShirshov AlgElement Diamond

universe u v

variable {G : Type u} [DecidableEq G] {k : Type v} [CommRing k]
variable {ord : AdmissibleOrder G} {sys : RewritingSystem G k}

/-! ## §1  Coefficients as a linear functional -/

/-- The coefficient of a monomial, as a `k`-linear functional on `k⟨G⟩`. -/
def coeffL (m : Monomial G) : FreeAlg G k →ₗ[k] k where
  toFun x := FreeAlg.coeff x m
  map_add' x y := FreeAlg.coeff_add x y m
  map_smul' c x := by simp [smul_eq_mul]

@[simp] theorem coeffL_apply (m : Monomial G) (x : FreeAlg G k) :
    coeffL m x = FreeAlg.coeff x m := rfl

theorem coeff_sub (x y : FreeAlg G k) (m : Monomial G) :
    FreeAlg.coeff (x - y) m = FreeAlg.coeff x m - FreeAlg.coeff y m := by
  rw [sub_eq_add_neg, FreeAlg.coeff_add, FreeAlg.coeff_neg, ← sub_eq_add_neg]

/-! ## §2  Reduction stays inside a coset of the ideal -/

theorem mk_sub_mem_of_single {f g : AlgElement G k}
    (h : SingleStepReduction ord sys f g) :
    FreeAlg.mk f - FreeAlg.mk g ∈ systemIdeal sys := by
  obtain ⟨r, hr, a, b, c, -, -, heq⟩ := h.exists_witness
  have e : FreeAlg.mk f - FreeAlg.mk g =
      c • FreeAlg.mk (contextMul a r.relation b) :=
    FreeAlg.ext fun m => by
      rw [coeff_sub, FreeAlg.coeff_smul, FreeAlg.coeff_mk, FreeAlg.coeff_mk,
        FreeAlg.coeff_mk, heq m, sub_coeff, smul_coeff]
      ring
  rw [e]
  exact Submodule.smul_mem _ _ (mem_systemIdeal_of_context hr a b)

theorem mk_sub_mem_of_multi {f g : AlgElement G k}
    (h : MultiStepReduction ord sys f g) :
    FreeAlg.mk f - FreeAlg.mk g ∈ systemIdeal sys := by
  induction h with
  | refl => simp
  | step _ hgh ih =>
    have := Submodule.add_mem _ ih (mk_sub_mem_of_single hgh)
    simpa [sub_add_sub_cancel] using this

/-! ## §3  The normal-form map -/

/-- A chosen normal form of a representation. -/
noncomputable def nf (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) (f : AlgElement G k) :
    AlgElement G k :=
  Classical.choose (normal_form_exists ord sys hlc f)

theorem nf_spec (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) (f : AlgElement G k) :
    ReducesToNF ord sys f (nf hlc f) :=
  Classical.choose_spec (normal_form_exists ord sys hlc f)

section NF

variable (hgs : IsGrobnerShirshovBasis G k ord sys)
  (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
include hgs hlc

/-- Any normal form of `f` agrees with the chosen one in `k⟨G⟩`. -/
theorem mk_nf_eq {f n : AlgElement G k} (hn : ReducesToNF ord sys f n) :
    FreeAlg.mk (nf hlc f) = FreeAlg.mk n :=
  FreeAlg.mk_eq_mk.mpr (reductionUnique ord sys hgs hlc f _ _ (nf_spec hlc f) hn)

/-- The normal-form map on `k⟨G⟩`, before linearity is recorded. -/
noncomputable def nfFun (x : FreeAlg G k) : FreeAlg G k :=
  Quotient.liftOn x (fun f => FreeAlg.mk (nf hlc f)) (fun f g (hfg : CoeffEq f g) => by
    obtain ⟨n', hn', e⟩ := nf_of_congr hlc hfg (nf_spec hlc g)
    show FreeAlg.mk (nf hlc f) = FreeAlg.mk (nf hlc g)
    rw [mk_nf_eq hgs hlc hn']
    exact FreeAlg.mk_eq_mk.mpr e)

@[simp] theorem nfFun_mk (f : AlgElement G k) :
    nfFun hgs hlc (FreeAlg.mk f) = FreeAlg.mk (nf hlc f) := rfl

/-- **The normal-form map is `k`-linear** (Bergman's Lemma 1.1). -/
noncomputable def nfMap : FreeAlg G k →ₗ[k] FreeAlg G k where
  toFun := nfFun hgs hlc
  map_add' x y := by
    induction x using Quotient.inductionOn with
    | h f => induction y using Quotient.inductionOn with
      | h g =>
        show nfFun hgs hlc (FreeAlg.mk (add f g)) =
          FreeAlg.mk (nf hlc f) + FreeAlg.mk (nf hlc g)
        rw [nfFun_mk]
        exact FreeAlg.mk_eq_mk.mpr (nf_add hlc (reductionUnique ord sys hgs hlc f)
          (reductionUnique ord sys hgs hlc g) (nf_spec hlc _) (nf_spec hlc f)
          (nf_spec hlc g))
  map_smul' c x := by
    induction x using Quotient.inductionOn with
    | h f =>
      show nfFun hgs hlc (FreeAlg.mk (smul c f)) = c • FreeAlg.mk (nf hlc f)
      rw [nfFun_mk]
      exact FreeAlg.mk_eq_mk.mpr (nf_smul hlc c (reductionUnique ord sys hgs hlc f)
        (nf_spec hlc _) (nf_spec hlc f))

@[simp] theorem nfMap_mk (f : AlgElement G k) :
    nfMap hgs hlc (FreeAlg.mk f) = FreeAlg.mk (nf hlc f) := rfl

/-- **The normal-form map kills the ideal.** -/
theorem ideal_le_ker : systemIdeal sys ≤ LinearMap.ker (nfMap hgs hlc) := by
  refine Submodule.span_le.mpr ?_
  rintro _ ⟨r, hr, a, b, rfl⟩
  obtain ⟨n, hn, hz⟩ := zeroNF_ctx (ord := ord) hlc ⟨r, a, b⟩ hr
  show nfMap hgs hlc _ = 0
  rw [nfMap_mk, mk_nf_eq hgs hlc hn]
  exact FreeAlg.ext fun m => by rw [FreeAlg.coeff_mk, hz m]; rfl

/-- **Every element is congruent to its normal form.** -/
theorem sub_nfMap_mem (x : FreeAlg G k) : x - nfMap hgs hlc x ∈ systemIdeal sys := by
  induction x using Quotient.inductionOn with
  | h f => exact mk_sub_mem_of_multi (nf_spec hlc f).reduces

/-- **The normal-form map fixes elements supported on normal-form monomials.** -/
theorem nfMap_of_support (x : FreeAlg G k)
    (hx : ∀ m, FreeAlg.coeff x m ≠ 0 → NormalFormMonomial ord sys m) :
    nfMap hgs hlc x = x := by
  induction x using Quotient.inductionOn with
  | h f =>
    have hn : isNormalForm ord sys f := fun r hr m hm => hx m hm r hr
    show nfMap hgs hlc (FreeAlg.mk f) = FreeAlg.mk f
    rw [nfMap_mk]
    exact mk_nf_eq hgs hlc ⟨MultiStepReduction.refl f, hn⟩

end NF

/-! ## §4  The basis -/

variable [DecidableEq k]

/-- The class of a normal-form monomial in `A`. -/
noncomputable def nfVec (i : {m : Monomial G // NormalFormMonomial ord sys m}) :
    QuotAlg sys :=
  toQuot sys (FreeAlg.mk (AlgElement.single i.val (1 : k)))

theorem coeff_single_one (w m : Monomial G) :
    FreeAlg.coeff (FreeAlg.mk (AlgElement.single w (1 : k))) m =
      if m = w then 1 else 0 := by
  rw [FreeAlg.coeff_mk]
  split_ifs with h
  · subst h; exact single_coeff_self _ _
  · exact single_coeff_of_ne _ h

section Basis

variable (hgs : IsGrobnerShirshovBasis G k ord sys)
  (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
include hgs hlc

theorem nfVec_linearIndependent : LinearIndependent k (nfVec (ord := ord) (sys := sys)) := by
  classical
  rw [linearIndependent_iff']
  intro s g hsum i hi
  set X : FreeAlg G k :=
    ∑ j ∈ s, g j • FreeAlg.mk (AlgElement.single j.val (1 : k)) with hX
  have hcoeff : ∀ m, FreeAlg.coeff X m =
      ∑ j ∈ s, g j * (if m = j.val then 1 else 0) := by
    intro m
    rw [← coeffL_apply, hX, map_sum]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [map_smul, coeffL_apply, coeff_single_one, smul_eq_mul]
  have hmem : X ∈ systemIdeal sys := by
    rw [← toQuot_eq_zero_iff, hX, map_sum]
    simpa [nfVec] using hsum
  have h0 : nfMap hgs hlc X = 0 := ideal_le_ker hgs hlc hmem
  have hfix : nfMap hgs hlc X = X := by
    refine nfMap_of_support hgs hlc X fun m hm => ?_
    by_contra hnm
    apply hm
    rw [hcoeff]
    refine Finset.sum_eq_zero fun j _ => ?_
    rw [if_neg (fun (h : m = j.val) => hnm (h ▸ j.property)), mul_zero]
  have hX0 : X = 0 := hfix.symm.trans h0
  have := hcoeff i.val
  rw [hX0, FreeAlg.coeff_zero, Finset.sum_eq_single i] at this
  · simpa using this.symm
  · intro j _ hji
    rw [if_neg (fun h => hji (Subtype.ext h.symm)), mul_zero]
  · intro hni; exact absurd hi hni

theorem nfVec_span :
    ⊤ ≤ Submodule.span k (Set.range (nfVec (ord := ord) (sys := sys))) := by
  classical
  rintro q -
  obtain ⟨x, rfl⟩ := Submodule.mkQ_surjective (systemIdeal sys) q
  have hx : toQuot sys x = toQuot sys (nfMap hgs hlc x) := by
    rw [← sub_eq_zero, ← map_sub, toQuot_eq_zero_iff]
    exact sub_nfMap_mem hgs hlc x
  change toQuot sys x ∈ _
  rw [hx]
  induction x using Quotient.inductionOn with
  | h f =>
    change toQuot sys (nfMap hgs hlc (FreeAlg.mk f)) ∈ _
    rw [nfMap_mk]
    set n := nf hlc f
    have hn : isNormalForm ord sys n := (nf_spec hlc f).is_normal
    set T := n.support.filter (fun m => n.coeff m ≠ 0)
    have hsum : FreeAlg.mk n =
        ∑ m ∈ T, n.coeff m • FreeAlg.mk (AlgElement.single m (1 : k)) := by
      refine FreeAlg.ext fun m' => ?_
      rw [← coeffL_apply (m := m') (x := ∑ m ∈ T, _), map_sum, FreeAlg.coeff_mk]
      have hterm : ∀ m ∈ T, coeffL m'
          (n.coeff m • FreeAlg.mk (AlgElement.single m (1 : k))) =
          if m' = m then n.coeff m else 0 := by
        intro m _
        rw [map_smul, coeffL_apply, coeff_single_one, smul_eq_mul]
        split_ifs <;> simp
      rw [Finset.sum_congr rfl hterm, Finset.sum_ite_eq]
      by_cases hm : m' ∈ T
      · rw [if_pos hm]
      · rw [if_neg hm]
        by_contra hne
        exact hm (Finset.mem_filter.mpr ⟨mem_support_of_coeff_ne_zero hne, hne⟩)
    rw [hsum, map_sum]
    refine Submodule.sum_mem _ fun m hm => ?_
    rw [map_smul]
    refine Submodule.smul_mem _ _ (Submodule.subset_span ⟨⟨m, ?_⟩, rfl⟩)
    exact fun r hr => hn r hr m (Finset.mem_filter.mp hm).2

end Basis

/-- **Composition–Diamond lemma, (i) ⇒ (iii)**, over a commutative ring with unit
leading coefficients: a Gröbner–Shirshov basis presents an algebra whose
normal-form monomials form a `k`-basis.

Bokut–Chen–Li 2011, Theorem 4.4 (one-object case); Bergman 1978, Theorem 1.2. -/
theorem normalFormBasis_of_isGrobnerShirshovBasis
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) :
    NormalFormBasis ord sys :=
  ⟨Module.Basis.mk (nfVec_linearIndependent hgs hlc) (nfVec_span hgs hlc),
    fun i => Module.Basis.mk_apply _ _ i⟩

end UGB.GrobnerShirshov.NFBasis
