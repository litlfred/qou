import UGB.GrobnerShirshov.NormalForms

/-!
# `local_confluence` as stated is false: structural equality of reducts

`CompositionLemma.local_confluence` concludes a **structurally equal** common
reduct `h`. But `SingleStepReduction f g` constrains `g` only up to `CoeffEq`:
its `support` field is any finite superset of the live monomials. So one step
can land on two representatives of the same element that differ only in
`support`. When both are normal forms, the only multi-step reduct of each is
itself (`MultiStepReduction.eq_of_isNormalForm`), and no common `h` exists.

`local_confluence_structural_false` exhibits this at the smallest possible
system: one monic single-letter rule `K` over `ℤ` (a Gröbner–Shirshov basis by
`isGrobnerShirshovBasis_of_single_letter_rule`, no quasi-zeros, unit leading
coefficient), source `f = K`, reducts `0` with `support = ∅` and `0` with
`support = {K}`. Every hypothesis of the axiom holds, so **the axiom makes
the UGB development inconsistent**. `normal_form_unique` (structural `nf₁ = nf₂`)
inherits the defect: both reducts are normal forms of `f`.

The mathematics is not at fault — the two reducts are the same element. The
statements must be made up to `CoeffEq` (bean `qou-lc7q`).

This file uses no framework axiom.
-/


namespace UGB.GrobnerShirshov.SupportRefutation

open UGB.GrobnerShirshov AlgElement SU2Gen

abbrev wK : Monomial SU2Gen := [K]

/-- The relation `K`. -/
noncomputable def rel : AlgElement SU2Gen ℤ := single wK 1

theorem rel_support : rel.support = {wK} := by
  show (if (1:ℤ) = 0 then ∅ else {wK}) = _
  norm_num

noncomputable def rule : ReductionRule SU2Gen ℤ := ⟨rel, by rw [rel_support]; simp⟩

theorem rule_lm : rule.lm degLexOrder = wK := by
  apply leadingMonomial_eq_of_max
  · show wK ∈ rel.support
    rw [rel_support]; simp
  · intro m hm hne
    rw [show rule.relation = rel from rfl, rel_support] at hm
    exact absurd (Finset.mem_singleton.mp hm) hne

theorem rule_lc : rule.lc degLexOrder = 1 := by
  show rel.coeff (rule.lm degLexOrder) = 1
  rw [rule_lm]; simp [rel]

noncomputable def sys : RewritingSystem SU2Gen ℤ := ⟨[rule], by simp⟩

theorem sys_isGS : IsGrobnerShirshovBasis SU2Gen ℤ degLexOrder sys :=
  isGrobnerShirshovBasis_of_single_letter_rule degLexOrder rule K rule_lm

theorem sys_noQuasiZeros : NoQuasiZerosFree SU2Gen ℤ :=
  noQuasiZerosFree_of_generator K

theorem sys_lc : ∀ r ∈ sys.rules, IsUnit (r.lc degLexOrder) := by
  intro r hr
  simp only [sys, List.mem_singleton] at hr
  subst hr; rw [rule_lc]; exact isUnit_one

noncomputable def f : AlgElement SU2Gen ℤ := single wK 1

/-- The zero element, with empty support. -/
noncomputable def g₁ : AlgElement SU2Gen ℤ := zero

/-- The zero element, carrying the monomial `K` in its (superset) support. -/
noncomputable def g₂ : AlgElement SU2Gen ℤ where
  coeff := fun _ => 0
  support := {wK}
  support_spec := fun _ _ => rfl

theorem g₁_ne_g₂ : g₁ ≠ g₂ := by
  intro h
  have := congrArg AlgElement.support h
  simp only [g₁, g₂, AlgElement.zero] at this
  exact Finset.notMem_empty wK (this ▸ Finset.mem_singleton_self wK)

theorem step (g : AlgElement SU2Gen ℤ) (hg : ∀ m, g.coeff m = 0) :
    SingleStepReduction degLexOrder sys f g := by
  refine ⟨⟨rule, by simp [sys], [], [], 1, ?_, ?_, ?_⟩⟩
  · rw [rule_lm]; simp [f]
  · rw [rule_lc, rule_lm]; simp [f]
  · intro m
    rw [hg m, sub_coeff, smul_coeff, contextMul_nil_nil_coeff]
    show (0:ℤ) = (single wK 1).coeff m - 1 * (single wK 1).coeff m
    ring

theorem normal (g : AlgElement SU2Gen ℤ) (hg : ∀ m, g.coeff m = 0) :
    isNormalForm degLexOrder sys g := fun _ _ m hm => absurd (hg m) hm

/-- **The structural form of local confluence is false**, at a one-letter
    Gröbner–Shirshov basis over `ℤ` with a monic rule. `f = K` reduces in one
    step to two representatives of `0` that differ only in their (superset)
    `support` field; both are normal, so the only multi-step reduct of each is
    itself, and they are not equal. -/
theorem local_confluence_structural_false :
    ¬ (∀ (f' g₁' g₂' : AlgElement SU2Gen ℤ),
        SingleStepReduction degLexOrder sys f' g₁' →
        SingleStepReduction degLexOrder sys f' g₂' →
        ∃ h, MultiStepReduction degLexOrder sys g₁' h ∧
          MultiStepReduction degLexOrder sys g₂' h) := by
  intro H
  obtain ⟨h, h₁, h₂⟩ := H f g₁ g₂ (step g₁ (fun _ => rfl)) (step g₂ (fun _ => rfl))
  have e₁ := MultiStepReduction.eq_of_isNormalForm (normal g₁ (fun _ => rfl)) h₁
  have e₂ := MultiStepReduction.eq_of_isNormalForm (normal g₂ (fun _ => rfl)) h₂
  exact g₁_ne_g₂ (e₁.symm.trans e₂)

end UGB.GrobnerShirshov.SupportRefutation
