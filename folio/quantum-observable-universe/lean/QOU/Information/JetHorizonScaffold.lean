import QOU.Information.QouPNeqNp
import QOU.Information.JetHorizonTransfer
import Mathlib.Tactic

/-!
# QOU.Information.JetHorizonScaffold — structure behind the transfer

Scaffolding for `JetHorizonTransfer` (bean `qou-iv9f`).  It makes the
transfer's antecedent *concrete* — grounding it in the degree-graded
**observation trace** — while keeping the one genuinely open step (the
degree↔complexity dictionary) an explicit, auditable hypothesis.  Nothing
here fabricates the transfer instance; it exposes exactly what such an
instance would have to supply.

## Taking a trace is the observation step

In the QOU an **observable result is obtained by taking a trace** (the
observation frame `τ` / Markov trace, AGENTS.md canonical chain): the
categorical fibre `A` is collapsed to a scalar `τ(a) ∈ k`.  The observed
value splits by Taylor/jet degree,
`τ(a) = ⟨degree-0 part⟩ + ⟨degree-≥1 part⟩`, and the two parts play
different computational roles (below).

## Why `NP`-witness ≡ degree-≥1 (not `P`-witness)

A recurring question: since degree-≥1 data is the *accessible* (leaking)
layer, why call it an `NP`-witness rather than a `P`-witness?  Because a
**witness is a defining feature of `NP`, not `P`**:

* `NP` = "a short certificate exists and is **verifiable** in poly time."
  The degree-≥1 data that leaks across the horizon is exactly such a
  certificate — you *receive and verify* it.  That is the `NP` notion.
* `P` = "the answer is **computed directly** in poly time."  `P` has no
  external certificate; it produces the degree-0 answer itself.  Calling
  degree-≥1 a "`P`-witness" conflates the verifier's certificate (`NP`)
  with the solver's computation (`P`) — a category error.

So the horizon picture is: degree-≥1 certificates are poly-verifiable
(in reach), the degree-0 answer is poly-inaccessible (blocked) ⇒
`P ≠ NP`.  **But the assignment is a modelling choice**: a *different*
dictionary (e.g. degree-≥1 read as `P`-computable partial data) yields a
*different* conclusion.  That non-uniqueness is precisely why the
transfer is conjectural — it is encoded below as an explicit
`ComplexityDictionary` with **no instance**.
-/

namespace QOU.Information

/-- **The observation frame / trace grading.**  An observable result
    `τ(a)` splits into its degree-0 part (the decision **answer**) and its
    degree-≥1 part (the **witness** / Hawking-leakage data). -/
structure ObservationGrading (A k : Type*) [Add k] where
  /-- The observation trace `τ : A → k` (Markov trace / observation frame). -/
  τ : A → k
  /-- Degree-0 component of the observed value: the decision answer. -/
  answer : A → k
  /-- Degree-≥1 component: the verifiable witness data that leaks. -/
  witness : A → k
  /-- The observable splits by degree. -/
  degree_split : ∀ a, τ a = answer a + witness a

/-- **The degree↔complexity dictionary (the open bridge, §3b-cond).**
    The interpretive identification the transfer rests on.  `NPVerify`
    and `PDecide` are opaque `Prop`s (no Mathlib complexity theory); the
    fields state the *chosen* reading — degree-≥1 certificates are
    `NP`-verifiable, the degree-0 answer being blocked obstructs `P` —
    and derive the QOU separation.  **No instance is declared**: this map
    is the irreducible conjectural input (anti-laundering). -/
class ComplexityDictionary {M : Type*} (decisionCost : M → ℕ → ℕ) where
  /-- The decision answer (degree-0) is poly-time inaccessible when the
      obstruction blocks it. -/
  answerBlocked : Prop
  /-- Degree-≥1 certificates are poly-verifiable (the `NP` side). -/
  witnessVerifiable : Prop
  /-- **The conjectural transfer**: a blocked degree-0 answer with
      verifiable degree-≥1 witnesses is exactly the `P ≠ NP` separation
      in the QOU. -/
  separation_of_blocked : answerBlocked → witnessVerifiable → PNeqNPInQOU decisionCost
  /-- Degree-≥1 witnesses are always available (they leak across 𝓗). -/
  witnesses_leak : witnessVerifiable

/-- **A jet-horizon transfer is realisable from a complexity dictionary
    (sorry-free).**  Given the interpretive dictionary and the derived
    horizon opacity `chi ≠ 0 ⇒ answerBlocked`, one obtains a
    `JetHorizonTransfer chi`.  This *reduces* the transfer to the
    dictionary — it does not prove the dictionary (which has no instance).
    It shows the transfer's open content is exactly the degree↔complexity
    identification, nothing more. -/
noncomputable def jetHorizonTransfer_of_dictionary {M : Type*}
    (decisionCost : M → ℕ → ℕ) (chi : ℤ)
    [D : ComplexityDictionary decisionCost]
    (opacity : chi ≠ 0 → D.answerBlocked) : JetHorizonTransfer decisionCost chi where
  degreeZeroBlocked := D.answerBlocked
  opacity_of_obstruction := opacity
  transfer := fun hb => D.separation_of_blocked hb D.witnesses_leak

end QOU.Information
