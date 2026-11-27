import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.FeynmanPathIntegrals.markov_identification

Canonical Lean for content block
[`lem:feynman-markov-identification`](../../../mass-theory/feynman-markov-identification.md):
*Markov-weighted eigenbasis sum equals the Markov trace.*

**Lemma.** For `β ∈ Bₙ` acting on `V^{⊗n}` via `ρₙ`, the eigenbasis
transition amplitude — *defined* as the Markov-weighted sum of partial
traces

  `⟨ψ_f | ψ_i⟩_eig := Σ_{λ ⊢ n, ℓ(λ) ≤ 2} w_λ · tr_{S_λ}(ρₙ(β))`

— equals the Jones–Markov trace `tr_M(ρ(β))` on `H_n(R, q)`, where
`w_λ = dim_q(V_λ)·dim(S_λ)/dim_q(V^{⊗n})`.

## 2026-09-03 — a correction that reinstated the defect it documents

The module docstring said the branching identity was

> *"stated as the standalone lemma `markovTrace_branching` about the named
> `opaque` objects `markovTrace`, `markovWeight`, `spechtPartialTrace`,
> **discharged by `sorry`** with the manuscript citation"*

and the declaration docstring repeated *"so the body is `sorry` with the
manuscript citation"*.  **There were no `opaque` objects** — all three were
fields of `MarkovIdentificationContext` — and **there was no `sorry`**
anywhere in the file; every one of its four occurrences was prose.  The body
was `ctx.markovTrace_branching`: the projection, AGENTS.md §3b-cond item 5.

What makes this the sharpest instance in the drain is the paragraph that
followed, which is *correct about its own predecessor*:

> *"A previous revision took the branching identity as a hypothesis
> `h_branching : trM = Σ w·trS` on the main theorem — definitionally the
> conclusion — so the substantive identity was assumed rather than stated;
> that encoding (and its docstring's claim of a `sorry` that did not exist)
> is corrected here."*

The correction moved the hypothesis from a theorem argument into a class
field.  That is the same assumption under a different binder — and it carried
forward, verbatim, the false `sorry` claim it had just diagnosed.  A
documented fix that reinstates the documented defect, in the same commit that
names it.

## Independently corroborated on `main`

Commit `78988da5c92` — *"lean: nine docstrings claim their body is a `sorry`;
it is a projection"* — singled this file out as one of two that were **doubly**
wrong: the docstring said the Wenzl-bridge infrastructure *"cannot be added as
a simple class field, so the body is `sorry`"*, and *"it was added as exactly
such a field, of the same name, and is projected."*

That is the same finding reached here from the other direction, and it
deliberately stopped at the prose, recording the projection as owned by bean
`qou-z9ws` / PR #6422 — this change. The rebase conflicted because its
correction describes the theorem this commit deletes.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

The class is gone.  `markovTrace_branching` is a **`Prop`-valued definition
over caller-supplied data**, and `markov_identification` **derives** the
lemma's conclusion from it — which is what the file was trying to express all
along, and could not while the identity was a field the instance chose.

A `sorry` would not have been sound either: with `markovTrace` free, the
branching identity is refutable (`not_markovTrace_branching_of_free_data`),
so a `sorry` would read as "true, not yet proved" about something false.

## What is proved, and what is open

* `amplitudeEigenbasis_eq_sum` — clause (i), by `rfl`. It is the *definition*
  of the eigenbasis amplitude and is labelled as such: it carries no content
  about Hecke algebras.
* `markov_identification` — clause (ii), **derived** from the branching
  identity taken as a hypothesis.

**Open in this file — and closed at convention D one module over (2026-09-03).**
`QOU.FeynmanPathIntegrals.MarkovIdentificationInstance.markovTrace_branching_of_markovTrace`
proves `markovTrace_branching` at the data the lemma is about — block count, Ocneanu weights,
seminormal block traces, `T.tr n x` — for every Markov trace `T` at `z_D = q³/(q²+1)` and every
`n`, from `QOU.SchurWeyl.MarkovTraceInstance.eq_wtrace_of_markov`; and
`markov_identification_of_markovTrace` is the lemma at that data. The paragraph below is the
status of *this* file, which constructs none of those objects and remains correct as written.

**Open (here):** the branching identity itself — the Wenzl-bridge decomposition
`tr_M = Σ_λ w_λ tr_{S_λ}` of the Jones–Markov trace into Specht-module
partial traces.  Nothing here constructs `ρₙ`, `H_n(R, q)`, the Specht
modules, or the quantum dimensions in `w_λ`; they are reals the caller
supplies.  The in-repo RSK infrastructure
(`QOU.Mathlib.RSK_substrate_proved`) proves the classical Burnside identity
for symmetric groups, **not** this branching.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/feynman-markov-identification.md
-/

namespace QOU.FeynmanPathIntegrals

/-- The eigenbasis transition amplitude, **defined** as the
Markov-weighted sum of partial traces
`Σ_{l ∈ range nPart} w l · tr_S l`. -/
noncomputable def amplitudeEigenbasis (nPart : ℕ) (w trS : ℕ → ℝ) : ℝ :=
  (Finset.range nPart).sum (fun l => w l * trS l)

/-- **Clause (i): the amplitude is the weighted sum.**

True by definition of `amplitudeEigenbasis`, and recorded as such — `rfl`
consults nothing about braids, Hecke algebras or Specht modules. Stating it
separately is what keeps clause (i) from being mistaken for evidence about
clause (ii). -/
-- Ref: [leitner2026] lem:feynman-markov-identification (definition of the eigenbasis amplitude)
theorem amplitudeEigenbasis_eq_sum (nPart : ℕ) (w trS : ℕ → ℝ) :
    amplitudeEigenbasis nPart w trS
      = (Finset.range nPart).sum (fun l => w l * trS l) := rfl

/-- **The branching identity (Wenzl bridge): `tr_M = Σ_λ w_λ tr_{S_λ}`**, as a
proposition over caller-supplied data.

The substantive content of `lem:feynman-markov-identification`: the
Jones–Markov trace decomposes as the Markov-weighted sum of Specht-module
partial traces.

**Named, not asserted.** See the module docstring for why neither a
projection nor a `sorry` is the honest form here, and for what the identity
would need in order to be derived. It is *derived* at convention D in
`MarkovIdentificationInstance.markovTrace_branching_of_markovTrace`. -/
-- Ref: [leitner2026] lem:feynman-markov-identification (Wenzl-bridge branching of tr_M)
def markovTrace_branching (nPartitions : ℕ)
    (markovWeight spechtPartialTrace : ℕ → ℝ) (markovTrace : ℝ) : Prop :=
  markovTrace = (Finset.range nPartitions).sum
    (fun l => markovWeight l * spechtPartialTrace l)

/-- **Clause (ii): the Markov-weighted eigenbasis sum equals the Jones–Markov
trace** ([`lem:feynman-markov-identification`]) — **derived**.

Takes the branching identity as an explicit hypothesis and concludes the
lemma. This is the implication the file exists to record, and it could not be
stated while the identity was a class field the instance chose. -/
-- Ref: [leitner2026] lem:feynman-markov-identification
theorem markov_identification {nPartitions : ℕ}
    {markovWeight spechtPartialTrace : ℕ → ℝ} {markovTrace : ℝ}
    (h : markovTrace_branching nPartitions markovWeight spechtPartialTrace
          markovTrace) :
    amplitudeEigenbasis nPartitions markovWeight spechtPartialTrace
      = markovTrace := by
  simp only [markovTrace_branching] at h
  rw [amplitudeEigenbasis_eq_sum, h]

/-- **The branching identity is refutable at freely-chosen data**, which is
why it is named rather than carried as a `sorry`.

With no partitions the sum is empty, so `tr_M = 1` reads `1 = 0`. Recorded as
a theorem so a later attempt to "finish" this file with a `sorry` fails
against a standing counterexample — the third encoding of this lemma to claim
a `sorry` it did not have. -/
theorem not_markovTrace_branching_of_free_data :
    ¬ markovTrace_branching 0 (fun _ => 0) (fun _ => 0) 1 := by
  simp [markovTrace_branching]

end QOU.FeynmanPathIntegrals
