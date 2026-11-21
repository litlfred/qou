import UGB.GrobnerShirshov.NormalForms

/-!
# `normal_form_exists` is false as stated

`UGB.GrobnerShirshov.normal_form_exists` (`Basic.lean` §6) asserts:

> given a Gröbner–Shirshov basis and any element `f`, there exists a normal form
> reachable from `f`.

**This is false.** This file refutes it at a concrete instance: `G = SU2Gen`,
`k = ℤ`, the deg-lex order, and the one-rule system whose single relation is
`2·K`.

## Why it fails

Two conditions that the framework treats as interchangeable are not:

* `isNormalForm` is a condition on **monomials** — no rule's leading monomial
  occurs as an infix of a monomial carrying a non-zero coefficient;
* taking a `SingleStepReduction` additionally requires solving
  `c · lc(r) = f.coeff (a ++ lm(r) ++ b)` for `c` — a condition on
  **coefficients**.

When `lc(r)` is not invertible these come apart, and an element can be *stuck*:
not in normal form, yet with no reduction available. Here `lc = 2` is not a unit
in `ℤ`, and `f = K` has coefficient `1`, so a step would need `c · 2 = 1`.

Nothing rules this system out. `IsGrobnerShirshovBasis` places no condition on
leading coefficients, and this system satisfies it for a reason already in the
tree: `isGrobnerShirshovBasis_of_single_letter_rule` — a one-rule system whose
leading monomial is a single letter is a GS basis, because the length forces
every composition to have empty contexts.

## What this costs

`reduce` is defined as `(normal_form_exists …).choose`, so it and everything
through it — `composition_lemma`, `retraction_property`, `buchberger`,
`pbw_corollary`, `main_theorem_statement` — currently rest on a false axiom, from
which anything follows. The repair is `normal_form_exists_of_unit_lc`
(`CompositionLemma.lean`): the same statement with `IsUnit (r.lc ord)` on every
rule, **proved** from `reduction_well_founded`, and with the unused `hgs`
dropped. Threading that hypothesis through `reduce` and its consumers is the
migration this refutation motivates; it is not done here.

Note the axiom's `hgs` argument is a red herring: this counterexample *is* a
Gröbner–Shirshov basis. Strengthening the confluence hypothesis cannot rescue
the statement, because the failure is about coefficients, not about overlaps.
-/

namespace UGB.GrobnerShirshov.NormalFormExistsRefutation

open UGB.GrobnerShirshov AlgElement

/-- The single-letter monomial `K`. -/
abbrev w : Monomial SU2Gen := [SU2Gen.K]

/-- The relation `2·K`. Its leading coefficient is `2`, which is not a unit in
`ℤ` — the whole point. -/
noncomputable def rel : AlgElement SU2Gen ℤ := single w 2

theorem rel_support : rel.support = {w} := by
  show (if (2 : ℤ) = 0 then ∅ else {w}) = {w}
  norm_num

theorem rel_support_nonempty : rel.support.Nonempty := by
  rw [rel_support]; exact ⟨w, Finset.mem_singleton_self w⟩

/-- The rule `2·K ↦ …`. -/
noncomputable def rule : ReductionRule SU2Gen ℤ := ⟨rel, rel_support_nonempty⟩

/-- The one-rule system. -/
noncomputable def sys : RewritingSystem SU2Gen ℤ := .ofList [rule] (by simp)

/-- Its leading monomial is the single letter `K`: the support is a singleton, so
maximality is vacuous. -/
theorem rule_lm : rule.lm degLexOrder = w := by
  apply leadingMonomial_eq_of_max
  · show w ∈ rel.support
    rw [rel_support]; exact Finset.mem_singleton_self w
  · intro m hm hne
    rw [show (rule.relation) = rel from rfl, rel_support] at hm
    exact absurd (Finset.mem_singleton.mp hm) hne

/-- Its leading coefficient is `2`. -/
theorem rule_lc : rule.lc degLexOrder = 2 := by
  show rel.coeff (rule.lm degLexOrder) = 2
  rw [rule_lm]
  exact single_coeff_self w 2

/-- **The system is a Gröbner–Shirshov basis** — by the tree's own witness for a
single-letter leading monomial. So no confluence hypothesis excludes it. -/
theorem sys_isGS : IsGrobnerShirshovBasis SU2Gen ℤ degLexOrder sys :=
  isGrobnerShirshovBasis_of_single_letter_rule degLexOrder rule SU2Gen.K rule_lm

/-- The stuck element: the monomial `K` with coefficient `1`. -/
noncomputable def f : AlgElement SU2Gen ℤ := singleton w

theorem f_coeff_self : f.coeff w = 1 := singleton_coeff_self w

theorem f_coeff_of_ne {m : Monomial SU2Gen} (h : m ≠ w) : f.coeff m = 0 :=
  singleton_coeff_of_ne h

/-- **`f` is not in normal form**: the rule's leading monomial `K` is an infix of
`K`, which carries coefficient `1 ≠ 0`. -/
theorem f_not_normal : ¬ isNormalForm degLexOrder sys f := by
  intro hnf
  have h1 : f.coeff w ≠ 0 := by rw [f_coeff_self]; exact one_ne_zero
  have h2 : rule.lm degLexOrder <:+: w := by simp [rule_lm]
  exact hnf rule (by simp [sys]) w h1 h2

/-- **No step applies to `f`.** Any step would have to target `a ++ K ++ b = K`,
forcing `a = b = []`, and then solve `c · 2 = 1` in `ℤ`. -/
theorem f_no_step : ∀ g, ¬ SingleStepReduction degLexOrder sys f g := by
  rintro g ⟨r, hr, a, b, c, hne, hc, -⟩
  have hrr : r = rule := by simpa [sys] using hr
  subst hrr
  rw [rule_lm] at hne hc
  -- the targeted monomial carries a non-zero coefficient, so it must be `w`
  have hmw : a ++ w ++ b = w := by
    by_contra hne'
    exact hne (f_coeff_of_ne hne')
  rw [hmw, rule_lc, f_coeff_self] at hc
  omega

/-- **`f` has no normal form.** It cannot step, so its only reduct is itself, and
itself is not normal. -/
theorem f_no_normal_form : ¬ ∃ nf, ReducesToNF degLexOrder sys f nf := by
  rintro ⟨nf, hred, hnorm⟩
  rcases hred.cases_head with rfl | ⟨a, hstep, -⟩
  · exact f_not_normal hnorm
  · exact f_no_step a hstep

/-- **The refutation.** The `normal_form_exists` axiom, instantiated at
`G = SU2Gen`, `k = ℤ`, is false.

The axiom is universe-polymorphic and quantifies over all `G`, `k`, `ord` and
`sys`, so refuting this instance refutes it. -/
theorem normal_form_exists_false :
    ¬ (∀ (ord : AdmissibleOrder SU2Gen) (sys : RewritingSystem SU2Gen ℤ),
        IsGrobnerShirshovBasis SU2Gen ℤ ord sys →
        ∀ f : AlgElement SU2Gen ℤ, ∃ nf, ReducesToNF ord sys f nf) := by
  intro h
  exact f_no_normal_form (h degLexOrder sys sys_isGS f)

/-- **The repaired hypothesis is exactly what this system violates**, which is
the check that `normal_form_exists_of_unit_lc` is not merely a sufficient
condition pulled out of the air: `2` is not a unit in `ℤ`. -/
theorem sys_not_unit_lc : ¬ (∀ r ∈ sys.rules, IsUnit (r.lc degLexOrder)) := by
  intro h
  have h2 := h rule (by simp [sys])
  rw [rule_lc] at h2
  obtain ⟨u, hu⟩ := h2
  have h1 : (u : ℤ) * (↑u⁻¹ : ℤ) = 1 := u.mul_inv
  rw [hu] at h1
  omega

end UGB.GrobnerShirshov.NormalFormExistsRefutation
