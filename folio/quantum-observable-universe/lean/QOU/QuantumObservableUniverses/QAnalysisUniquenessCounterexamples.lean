import QOU.QuantumObservableUniverses.QAnalysis

/-!
# QOU.QuantumObservableUniverses.QAnalysisUniquenessCounterexamples

Refutations of six axioms that stood in the q-analysis display siblings
until 2026-09-06.  Five asserted **uniqueness** of a distinguished
element from agreement of the ambient maps; one asserted **existence**
of a `QDilogarithm` over every additive carrier.  All six are false.

## The one defect, six times

Each of `QDilogarithm`, `QExponential` and `QLogarithm` carries its
ambient structure -- the coproduct, the counit, the Jackson derivative,
the pentagon arguments -- as **free function fields**, and its axioms as
proof fields *about those functions*.  So the functions can be chosen to
make the axioms hold for **every** value of the distinguished element:

* `coprod := fun x => (x, x)` makes `grouplike`, `primitive_left` and
  `primitive_right` hold whatever `e_q` or `log_q` is;
* a constant `counit` makes `counit_eq_one` / `counit_eq_zero` hold
  whatever it is;
* `D_q := id` makes `flow_invariant` hold whatever it is.

Two records then agree on every hypothesised field and differ in the
concluded one.  The `QDilogarithm` case is starker still: `Li2`, the
field the conclusion is about, is **not mentioned by the `pentagon`
field at all** -- the pentagon constrains `Li2_eval`, a different field,
and nothing ties the two.  `Li2` is free data.

The witnesses below are not exotic.  They are the same shape as the
records the corpus's own `*-exists.lean` siblings use to prove these
types inhabited (`QExponential.exists_in_shuffle_hopf` and
`QLogarithm.exists_in_shuffle_hopf`, both of which say in a comment that
the witness is trivial and the intended Kassel construction is sharper).
The existence witness and the uniqueness counterexample are the same
degenerate record.

## The existence axiom (`not_qDilogarithm_exists_over_every_add_carrier`)

`QDilogarithm.exists_axiom : ∀ (H : Type*) [Add H], Nonempty (QDilogarithm H)`
quantified over *every* carrier with an `Add`, including empty ones.  A
`QDilogarithm Empty` would have to supply `log_q : Empty`.  Unlike the
five uniqueness axioms this one is repairable rather than wrong in
substance: over an `AddZeroClass` the type really is inhabited, and
`QDilogarithm.nonempty_of_addZeroClass` below proves it with no axiom --
while being explicit that inhabiting the type is not the Kassel
construction the proposition's prose describes.

## What the citations actually say

[kassel1995] §III.3 proves grouplikes are **linearly independent**, and
§IV.3 identifies primitives with a Lie algebra -- neither is a
uniqueness statement, and a Lie algebra of primitives is exactly a
statement that primitives are *not* unique.  A corrected uniqueness
claim needs a normalisation the structures do not carry, and is
deliberately **not** supplied here: guessing the missing normalisation is
how these six arose.

## References

- [kassel1995] Quantum Groups (Springer GTM 155), §III.3, §IV.3
- [leitner2026] docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md
-/

namespace QOU.QAnalysisCounterexamples

noncomputable section

/-! ## §1  Witnesses -/

/-- A pentagon-satisfying `QDilogarithm ℕ` whose `Li2` first component is
    `c`.  Every field other than `Li2` is independent of `c`, and
    `pentagon` holds because `Li2_eval` is constantly `0`. -/
def dilog (c : ℕ) : QDilogarithm ℕ where
  Li2 := (c, 0)
  log_q := 0
  Li2_eval := fun _ => 0
  mul := fun _ _ => 0
  compl := fun _ => 0
  div := fun _ _ => 0
  pentagon := by intro x y; rfl

/-- A `QExponential ℕ` with grouplike `c`.  `coprod := fun x => (x, x)`
    makes `grouplike` hold for every `c`; the constant counit and
    `D_q := id` do the same for the other two fields. -/
def qexp (c : ℕ) : QExponential ℕ where
  e_q := c
  coprod := fun x => (x, x)
  counit := fun _ => 1
  D_q := id
  grouplike := rfl
  counit_eq_one := rfl
  flow_invariant := rfl

/-- A `QLogarithm ℕ` with primitive `c`, by the same construction. -/
def qlog (c : ℕ) : QLogarithm ℕ where
  log_q := c
  coprod := fun x => (x, x)
  counit := fun _ => 0
  one := 0
  primitive_left := rfl
  primitive_right := rfl
  counit_eq_zero := rfl

/-! ## §2  The five uniqueness refutations -/

/-- **`QDilogarithm.unique_axiom` is false**, and so is its verbatim twin
    `QDilogarithm.unique_up_to_shift_axiom`: `dilog 0` and `dilog 1`
    agree on `log_q`, `mul`, `compl` and `div` and differ in `Li2.1`. -/
theorem not_qDilogarithm_unique :
    ¬ (∀ {H : Type} [Add H] (L₁ L₂ : QDilogarithm H),
        L₁.log_q = L₂.log_q → L₁.mul = L₂.mul → L₁.compl = L₂.compl →
        L₁.div = L₂.div → L₁.Li2.1 = L₂.Li2.1) := by
  intro h
  exact absurd (h (dilog 0) (dilog 1) rfl rfl rfl rfl) (by decide)

/-- **`QExponential.unique_axiom` is false** -- in both files that
    declared it: `qexp 0` and `qexp 1` agree on `coprod`, `counit` and
    `D_q` and differ in `e_q`. -/
theorem not_qExponential_unique :
    ¬ (∀ {H : Type} (e₁ e₂ : QExponential H),
        e₁.coprod = e₂.coprod → e₁.counit = e₂.counit → e₁.D_q = e₂.D_q →
        e₁.e_q = e₂.e_q) := by
  intro h
  exact absurd (h (qexp 0) (qexp 1) rfl rfl rfl) (by decide)

/-- **`QLogarithm.unique_axiom` is false**: `qlog 0` and `qlog 1` agree
    on `coprod`, `counit` and `one` and differ in `log_q`. -/
theorem not_qLogarithm_unique :
    ¬ (∀ {H : Type} (ℓ₁ ℓ₂ : QLogarithm H),
        ℓ₁.coprod = ℓ₂.coprod → ℓ₁.counit = ℓ₂.counit → ℓ₁.one = ℓ₂.one →
        ℓ₁.log_q = ℓ₂.log_q) := by
  intro h
  exact absurd (h (qlog 0) (qlog 1) rfl rfl rfl) (by decide)

/-! ## §3  The existence refutation, and its repair -/

/-- `Empty` carries an `Add`; the axiom quantified over every such
    carrier. -/
instance : Add Empty := ⟨fun a _ => a.elim⟩

/-- **`QDilogarithm.exists_axiom` is false** as stated: a
    `QDilogarithm Empty` would have to supply `log_q : Empty`. -/
theorem not_qDilogarithm_exists_over_every_add_carrier :
    ¬ (∀ (H : Type) [Add H], Nonempty (QDilogarithm H)) := by
  intro h
  exact (h Empty).elim fun L => L.log_q.elim

/-- The repaired statement, with **no axiom**: over an `AddZeroClass` the
    type is inhabited.

    This is what the Lean existence claim always said, and it is worth
    being plain that it is much weaker than the proposition's prose: the
    witness is the all-zero record, so this establishes *inhabitation of
    the structure*, not the shuffle-recursion construction of the
    q-dilogarithm.  The same caveat applies to the two
    `exists_in_shuffle_hopf` theorems, which say so themselves. -/
theorem QDilogarithm.nonempty_of_addZeroClass (H : Type*) [AddZeroClass H] :
    Nonempty (QDilogarithm H) :=
  ⟨{ Li2 := (0, 0)
     log_q := 0
     Li2_eval := fun _ => 0
     mul := fun _ _ => 0
     compl := fun _ => 0
     div := fun _ _ => 0
     pentagon := by intro x y; simp }⟩

end

end QOU.QAnalysisCounterexamples
