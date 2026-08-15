import Mathlib.Logic.Basic

/-!
# QOU.Information.ObstructionVerdictCap — one scalar cannot carry three verdicts

**Companion to** [`ObstructionGenericity`](ObstructionGenericity.lean) and content
block [`thm:qou-obstruction-reduction`](../../../quantum-observable-universe/stochastic-mechanics/qou-obstruction-reduction.md).

## The setting

`thm:qou-obstruction-reduction` computes the classical-limit obstruction space:

```
dim_k Obs(𝐂, q → 1) = dim_k HH²(𝒰_q, Ad) = 1,      [φ₁] ↦ χ(A)
```

It is **one**-dimensional, and its class is `χ(A) = -6 ≠ 0`. The corpus then
attaches three Millennium reformulations to restrictions of that single class,
**with two different polarities**:

| Leg | Assertion in the corpus | Polarity |
|---|---|---|
| q-Collatz | conjecture ⟺ `κ_C = 0` | **vanishing** |
| q-Navier–Stokes | regularity ⟺ `NS(A) = 0` | **vanishing** |
| P-vs-NP | `P ≠ NP` ⟺ `res_ℛ(χ(A)) ≠ 0` | **non-vanishing** |

and `conj:qou-p-neq-np` states that the proportionality of those evaluations is
itself part of the conjecture, not a consequence of it.

## What this file proves (all sorry-free, all trivial-by-design)

The theorems here are deliberately short: the content is not their proofs but
the fact that the corpus's own stated hypotheses **already** entail them.

* `verdict_cap` — two predicates faithful to the *same* scalar verdict are
  equivalent. One scalar cannot separate two questions.
* `opposite_polarity` — a predicate faithful to *vanishing* and a predicate
  faithful to *non-vanishing* of the same scalar are **negations** of one
  another.
* `collatz_iff_not_pnp_of_proportional` — assembling the two: under the
  proportionality hypothesis, q-Collatz holds **iff** `P ≠ NP` fails.
* `pnp_and_collatz_of_nonzero` — evaluating at the derived value `χ(A) ≠ 0`:
  the package asserts `P ≠ NP` **and** the failure of both vanishing-polarity
  legs, i.e. it predicts **q-Collatz is false** and **q-NS regularity is false**.

The q-NS half of that last conclusion matches the corpus
(`thm:ns-singularity-descartes` records `NS(A) = e(ξ)|_Σ ≠ 0`, QOU-internally
singular). The q-Collatz half **contradicts** the corpus, which conjectures
q-Collatz true and argues for it via the surreal squeeze. So the three
faithfulness claims and the proportionality claim are **not jointly tenable**
with the corpus's own stated beliefs: at least one must be given up.

## Scope (per AGENTS.md "Before declaring refuted")

This is a **scope-(a)** result about a *package of stated hypotheses*, not a
scope-(b) structural exclusion of any ingredient. It refutes no obstruction
class and no conjecture. What it shows is that the four claims — three
faithfulness equivalences plus proportionality — cannot all hold alongside the
corpus's stated expectation that q-Collatz is true. Dropping any one of them
restores consistency; the natural casualty is **proportionality**, which
`conj:qou-p-neq-np` already labels conjectural.

Nothing here is instantiated: every hypothesis is a named argument, never an
`axiom` or an `instance`. `P ≠ NP`, q-Collatz and q-NS regularity appear only as
opaque `Prop`s, exactly as they do in `QouPNeqNp`.
-/

namespace QOU.Information

/-! ### The cap -/

/-- **Verdict cap.** If a single verdict `v` (e.g. "the obstruction is non-zero
    at `q₀`") is faithful to two predicates, those predicates are equivalent. A
    one-dimensional obstruction space supplies exactly one such verdict, so it
    cannot answer two independent questions differently. -/
theorem verdict_cap {v A B : Prop} (hA : v ↔ A) (hB : v ↔ B) : A ↔ B :=
  hA.symm.trans hB

/-- **Opposite polarity.** A predicate faithful to the *vanishing* of a verdict
    and a predicate faithful to its *non-vanishing* are negations of each other.
    This is the formal content of the corpus attaching `κ_C = 0 ⟺ Collatz` and
    `res ≠ 0 ⟺ P ≠ NP` to restrictions of one class. -/
theorem opposite_polarity {z A B : Prop} (hA : z ↔ A) (hB : ¬ z ↔ B) : A ↔ ¬ B := by
  constructor
  · intro ha hb; exact (hB.mpr hb) (hA.mpr ha)
  · intro hnb; exact hA.mp (Classical.byContradiction fun hz => hnb (hB.mp hz))

/-! ### Applied to the three legs

`Vanishes` is "the (proportional) obstruction restriction vanishes at `q₀`".
`Collatz`, `NSRegular`, `PNeqNP` are opaque propositions — the QOU-internal
conjectures. `hColl`, `hNS`, `hPNP` are the corpus's three faithfulness claims,
all open; each is a hypothesis here, never assumed globally. -/

variable {Vanishes Collatz NSRegular PNeqNP : Prop}

/-- **q-Collatz and `P ≠ NP` are negations, under proportionality.** Given the
    corpus's own faithfulness claims at their stated polarities, the two
    conjectures cannot both be true. -/
theorem collatz_iff_not_pnp_of_proportional
    (hColl : Vanishes ↔ Collatz) (hPNP : ¬ Vanishes ↔ PNeqNP) :
    Collatz ↔ ¬ PNeqNP :=
  opposite_polarity hColl hPNP

/-- **q-NS regularity and `P ≠ NP` are negations too.** Same argument on the
    other vanishing-polarity leg. -/
theorem nsRegular_iff_not_pnp_of_proportional
    (hNS : Vanishes ↔ NSRegular) (hPNP : ¬ Vanishes ↔ PNeqNP) :
    NSRegular ↔ ¬ PNeqNP :=
  opposite_polarity hNS hPNP

/-- **q-Collatz ⟺ q-NS regularity**, under proportionality — both sit on the
    vanishing side, so the verdict cap identifies them. Two questions the corpus
    treats as independent open problems collapse to one. -/
theorem collatz_iff_nsRegular_of_proportional
    (hColl : Vanishes ↔ Collatz) (hNS : Vanishes ↔ NSRegular) :
    Collatz ↔ NSRegular :=
  verdict_cap hColl hNS

/-- **Evaluating at the derived non-zero class.** `χ(A) = -6 ≠ 0` is derived from
    the axioms (observability kills `HH⁰`; Frobenius–Hopf duality gives
    `HH² ≅ (HH¹)^∨ ≅ k`; Riemann–Roch on Bring's surface pins the value), and
    `q₀` is strictly non-torsion so no finite Kummer level applies. Feeding
    `¬ Vanishes` through the three faithfulness claims, the package asserts
    `P ≠ NP` **and** the failure of q-Collatz **and** the failure of q-NS
    regularity.

    The q-NS conclusion is what `thm:ns-singularity-descartes` already records.
    The q-Collatz conclusion contradicts `conj:q-collatz`. -/
theorem pnp_and_collatz_of_nonzero
    (hnonzero : ¬ Vanishes)
    (hColl : Vanishes ↔ Collatz) (hNS : Vanishes ↔ NSRegular)
    (hPNP : ¬ Vanishes ↔ PNeqNP) :
    PNeqNP ∧ ¬ Collatz ∧ ¬ NSRegular :=
  ⟨hPNP.mp hnonzero, fun hc => hnonzero (hColl.mpr hc), fun hr => hnonzero (hNS.mpr hr)⟩

/-- **The joint package is inconsistent with believing q-Collatz.** Stated as the
    explicit contradiction: the four claims plus `Collatz` are unsatisfiable.
    This is the file's punchline — the reader must give up one of the four. -/
theorem not_all_of_collatz
    (hnonzero : ¬ Vanishes) (hColl : Vanishes ↔ Collatz) (hc : Collatz) : False :=
  hnonzero (hColl.mpr hc)

end QOU.Information
