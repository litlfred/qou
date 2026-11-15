import UGB.GrobnerShirshov.NormalForms

/-!
# Local confluence fails without unit leading coefficients

`local_confluence` (`CompositionLemma.lean`) was stated for every
Gröbner–Shirshov basis over every ring `k`. This file shows that form is
false, at `G = SU2Gen`, `k = ℤ`, the deg-lex order, and the one-rule system
whose relation is `2·K + 1`.

## The counterexample

The rule's leading monomial is the single letter `K`, so the system is a
Gröbner–Shirshov basis (`isGrobnerShirshovBasis_of_single_letter_rule`), and
the free algebra on `SU2Gen` has no quasi-zeros. Take `f = 2·K E₊ K`.

* Reducing the left `K` (`c = 1`) gives `g₁ = −E₊ K`.
* Reducing the right `K` (`c = 1`) gives `g₂ = −K E₊`.

Each of `g₁`, `g₂` contains `K` with coefficient `−1`, and a step would need
`c · 2 = −1` in `ℤ`, so neither can move. They differ, so they have no common
reduct.

This is the same failure as `normal_form_exists_false`: when the leading
coefficient is not a unit, "not in normal form" and "can take a step" come
apart. The repair is the same hypothesis, `IsUnit (r.lc ord)` for every rule,
which `local_confluence` now carries. Bean `qou-n2un`.
-/

namespace UGB.GrobnerShirshov.LocalConfluenceRefutation

open UGB.GrobnerShirshov AlgElement SU2Gen

/-- The one-letter word `K`. -/
abbrev wK : Monomial SU2Gen := [K]

/-- The relation `2·K + 1`. -/
noncomputable def rel : AlgElement SU2Gen ℤ := add (single wK 2) (single [] 1)

theorem rel_coeff (m : Monomial SU2Gen) :
    rel.coeff m = if m = wK then 2 else if m = [] then 1 else 0 := by
  show (single wK (2:ℤ)).coeff m + (single [] (1:ℤ)).coeff m = _
  by_cases h1 : m = wK
  · subst h1; simp
  · by_cases h2 : m = []
    · subst h2; simp
    · rw [single_coeff_of_ne _ h1, single_coeff_of_ne _ h2]; simp [h1, h2]

theorem rel_support : rel.support = {wK, []} := by
  show (if (2:ℤ) = 0 then ∅ else {wK}) ∪ (if (1:ℤ) = 0 then ∅ else {[]}) = _
  norm_num; exact Finset.pair_comm _ _

theorem rel_support_nonempty : rel.support.Nonempty := by
  rw [rel_support]; exact ⟨wK, by simp⟩

/-- The rule `2·K + 1`. -/
noncomputable def rule : ReductionRule SU2Gen ℤ := ⟨rel, rel_support_nonempty⟩

theorem nil_lt_wK : degLexOrder.lt [] wK := by
  rcases degLexOrder.trichotomy [] wK with h | h | h
  · exact h
  · exact absurd h (by simp)
  · exact absurd h (AdmissibleOrder.not_lt_nil _ _)

theorem rule_lm : rule.lm degLexOrder = wK := by
  apply leadingMonomial_eq_of_max
  · show wK ∈ rel.support
    rw [rel_support]; simp
  · intro m hm hne
    rw [show rule.relation = rel from rfl, rel_support] at hm
    simp only [Finset.mem_insert, Finset.mem_singleton] at hm
    rcases hm with rfl | rfl
    · exact absurd rfl hne
    · exact nil_lt_wK

theorem rule_lc : rule.lc degLexOrder = 2 := by
  show rel.coeff (rule.lm degLexOrder) = 2
  rw [rule_lm, rel_coeff]; simp

/-- The one-rule system. -/
noncomputable def sys : RewritingSystem SU2Gen ℤ := ⟨[rule], by simp⟩

theorem sys_isGS : IsGrobnerShirshovBasis SU2Gen ℤ degLexOrder sys :=
  isGrobnerShirshovBasis_of_single_letter_rule degLexOrder rule K rule_lm

theorem sys_noQuasiZeros : NoQuasiZerosFree SU2Gen ℤ :=
  noQuasiZerosFree_of_generator K

/-- The source `f = 2·K E₊ K`. -/
noncomputable def f : AlgElement SU2Gen ℤ := single [K, E_plus, K] 2

/-- Left reduct, `f − (2K+1)·E₊K`. -/
noncomputable def g₁ : AlgElement SU2Gen ℤ :=
  sub f (smul 1 (contextMul [] rule.relation [E_plus, K]))

/-- Right reduct, `f − K E₊·(2K+1)`. -/
noncomputable def g₂ : AlgElement SU2Gen ℤ :=
  sub f (smul 1 (contextMul [K, E_plus] rule.relation []))

theorem step₁ : SingleStepReduction degLexOrder sys f g₁ := by
  refine ⟨⟨rule, by simp [sys], [], [E_plus, K], 1, ?_, ?_, fun _ => rfl⟩⟩
  · rw [rule_lm]; simp [f]
  · rw [rule_lc, rule_lm]; simp [f]

theorem step₂ : SingleStepReduction degLexOrder sys f g₂ := by
  refine ⟨⟨rule, by simp [sys], [K, E_plus], [], 1, ?_, ?_, fun _ => rfl⟩⟩
  · rw [rule_lm]; simp [f]
  · rw [rule_lc, rule_lm]; simp [f]

/-- `g₁` is `−E₊K`. -/
theorem g₁_coeff (m : Monomial SU2Gen) :
    g₁.coeff m = if m = [E_plus, K] then -1 else 0 := by
  simp only [g₁, sub_coeff, smul_coeff, one_mul]
  by_cases hs : ∃ w, m = [] ++ w ++ [E_plus, K]
  · obtain ⟨w, rfl⟩ := hs
    rw [contextMul_coeff_middle, show rule.relation = rel from rfl, rel_coeff]
    by_cases h1 : w = wK
    · subst h1; simp [f]
    · by_cases h2 : w = []
      · subst h2; simp [f]
      · have hf : f.coeff ([] ++ w ++ [E_plus, K]) = 0 := by
          apply single_coeff_of_ne; intro h
          apply h1; simp only [List.nil_append] at h
          exact List.append_cancel_right (h.trans (rfl : [K, E_plus, K] = [K] ++ [E_plus, K]))
        have hne : [] ++ w ++ [E_plus, K] ≠ [E_plus, K] := by
          intro h; apply h2; simpa using h
        rw [hf, if_neg h1, if_neg h2, if_neg hne]; simp
  · push_neg at hs
    rw [contextMul_coeff_of_not_shape _ hs]
    have hK : m ≠ [K, E_plus, K] := fun h => hs [K] (by simp [h])
    have hE : m ≠ [E_plus, K] := fun h => hs [] (by simp [h])
    rw [show f.coeff m = 0 from single_coeff_of_ne _ hK, if_neg hE]; simp

/-- `g₂` is `−K E₊`. -/
theorem g₂_coeff (m : Monomial SU2Gen) :
    g₂.coeff m = if m = [K, E_plus] then -1 else 0 := by
  simp only [g₂, sub_coeff, smul_coeff, one_mul]
  by_cases hs : ∃ w, m = [K, E_plus] ++ w ++ []
  · obtain ⟨w, rfl⟩ := hs
    rw [contextMul_coeff_middle, show rule.relation = rel from rfl, rel_coeff]
    by_cases h1 : w = wK
    · subst h1; simp [f]
    · by_cases h2 : w = []
      · subst h2; simp [f]
      · have hf : f.coeff ([K, E_plus] ++ w ++ []) = 0 := by
          apply single_coeff_of_ne; intro h
          apply h1; simp at h; exact h
        have hne : [K, E_plus] ++ w ++ [] ≠ [K, E_plus] := by
          intro h; apply h2; simpa using h
        rw [hf, if_neg h1, if_neg h2, if_neg hne]; simp
  · push_neg at hs
    rw [contextMul_coeff_of_not_shape _ hs]
    have hK : m ≠ [K, E_plus, K] := fun h => hs [K] (by simp [h])
    have hE : m ≠ [K, E_plus] := fun h => hs [] (by simp [h])
    rw [show f.coeff m = 0 from single_coeff_of_ne _ hK, if_neg hE]; simp

/-- An element whose only nonzero coefficient is `−1` cannot step. -/
theorem stuck (g : AlgElement SU2Gen ℤ) (w : Monomial SU2Gen)
    (hg : ∀ m, g.coeff m = if m = w then -1 else 0) :
    ∀ h, ¬ SingleStepReduction degLexOrder sys g h := by
  rintro h ⟨r, hr, a, b, c, hne, hc, -⟩
  have hrr : r = rule := by simpa [sys] using hr
  subst hrr
  rw [rule_lc] at hc
  rw [hg] at hne hc
  split_ifs at hne hc
  · omega
  · exact hne rfl

theorem eq_of_stuck {g h : AlgElement SU2Gen ℤ}
    (hst : ∀ x, ¬ SingleStepReduction degLexOrder sys g x)
    (hm : MultiStepReduction degLexOrder sys g h) : h = g := by
  rcases hm.cases_head with h' | ⟨a, ha, -⟩
  · exact h'
  · exact absurd ha (hst a)

/-- **The refutation.** Local confluence, for every Gröbner–Shirshov basis over
every ring without the unit-leading-coefficient hypothesis, is false. -/
theorem local_confluence_false :
    ¬ (∀ (ord : AdmissibleOrder SU2Gen) (sys : RewritingSystem SU2Gen ℤ),
        IsGrobnerShirshovBasis SU2Gen ℤ ord sys → NoQuasiZerosFree SU2Gen ℤ →
        ∀ f g₁ g₂ : AlgElement SU2Gen ℤ,
          SingleStepReduction ord sys f g₁ → SingleStepReduction ord sys f g₂ →
          ∃ h, MultiStepReduction ord sys g₁ h ∧ MultiStepReduction ord sys g₂ h) := by
  intro H
  obtain ⟨h, h₁, h₂⟩ :=
    H degLexOrder sys sys_isGS sys_noQuasiZeros f g₁ g₂ step₁ step₂
  have e₁ := eq_of_stuck (stuck g₁ _ g₁_coeff) h₁
  have e₂ := eq_of_stuck (stuck g₂ _ g₂_coeff) h₂
  have := congrArg (fun x : AlgElement SU2Gen ℤ => x.coeff [E_plus, K]) (e₁.symm.trans e₂)
  simp only [g₁_coeff, g₂_coeff] at this
  simp at this

/-- The system violates exactly the repaired hypothesis: `2` is not a unit. -/
theorem sys_not_unit_lc : ¬ (∀ r ∈ sys.rules, IsUnit (r.lc degLexOrder)) := by
  intro h
  have h2 := h rule (by simp [sys])
  rw [rule_lc] at h2
  obtain ⟨u, hu⟩ := h2
  have h1 : (u : ℤ) * (↑u⁻¹ : ℤ) = 1 := u.mul_inv
  rw [hu] at h1
  omega

end UGB.GrobnerShirshov.LocalConfluenceRefutation
