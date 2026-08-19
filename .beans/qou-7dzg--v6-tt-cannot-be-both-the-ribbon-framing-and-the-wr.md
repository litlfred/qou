---
# qou-7dzg
title: 'V6: T(t) cannot be BOTH the ribbon framing AND the writhe-separating coordinate -- the block''s two load-bearing sentences are incompatible'
status: todo
type: task
created_at: 2026-08-16T13:33:51Z
updated_at: 2026-08-16T13:33:51Z
---


## Answers V5 (qou-a6ma), and the answer costs the candidate its pedigree

V5 asked: are the tr_M framing and T(t) the same framing? Explored 2026-08-16.
The answer is NO, the corpus does carry two framing notions (V5's branch (b)) --
but establishing that also breaks the block's own justification for the datum.

### The two load-bearing sentences

`appendix-standard-model/strand-twist-datum.md` asserts BOTH:

  (A) "the datum is **the framing that the ribbon structure of the braided
       category carries** in addition to the crossing data of beta"

  (B) "the framing is genuinely **independent** of the crossing data: over any
       fixed braid word -- hence any fixed writhe w -- there exist framings with
       distinct total twist"

and (B) is explicitly the load-bearing one: "This last point is what qualifies
the datum as a candidate for the hypercharge invariant."

### They cannot both hold

In a genuine ribbon category the twist theta is CANONICAL -- determined by the
braiding, not freely assignable. For Hecke its exponent is the content sum. So:

  - If (A): the datum is determined by the object/word. Fixing the braid word
    FIXES it. That directly contradicts (B).
  - If (B): the datum varies at fixed word, so it is not determined by the
    braiding, so it is NOT the ribbon structure's framing. It is an extra free
    label -- the fit risk already proved in TwistBatteryVacuity.

### Why that settles V5

tr_M's framing IS a function of the braid word: `markov-axioms-primitive.md`
puts the writhe prefactor OUTSIDE the trace to restore link invariance, so tr_M
alone is a framed (regular-isotopy) invariant with framing determined by w.

(B) says T(t) varies while w is held fixed. A quantity that varies at fixed w is
not a function of w. Therefore T(t) is NOT tr_M's framing -- two different
framings on the same object, exactly V5's branch (b). The corpus must say so
explicitly rather than calling T(t) "the framing the ribbon structure carries".

### The Lean-shaped statement (V9's argument, reused)

This is the same shape as `chirality_not_a_function_of_crossing`
(ChiralityIndependentOfCrossing.lean): a datum that FACTORS THROUGH the crossing
data cannot separate states that share it. Here:

    a twist that is a function of the braid word cannot separate a
    writhe-degenerate pair

and the block's own factorization criterion requires the hypercharge invariant to
separate exactly such a pair. Hence the CANONICAL ribbon twist cannot be the
hypercharge separator. Independently consistent with theta = contentSum/3 having
been TESTED AND FAILED
(computations/ribbon_twist_charge_quantum_probe.py; n=3 gives {+1,0,-1}, no
n<=8 gives both quark charges).

### Disposition -- the block must drop (A) or (B)

  drop (B): T(t) is the canonical ribbon twist, word-determined, and the
            hypercharge candidacy COLLAPSES (it cannot separate).
  drop (A): the candidacy survives, but T(t) is reclassified as a free label
            with proved vacuity risk -- NOT "the ribbon structure", and V2's
            (qou-m4fp) free/independent row applies, where the framing must be
            pinned by something else or it is a fit.

Either way one published sentence is wrong as written. Scope (a): this is an
internal-consistency finding about two claims in one block plus one in
markov-axioms-primitive; it does not refute the hypercharge programme, and it
does not touch tr_M's correctness (tr_M's framing is unambiguous).

### Next

Formalize the separation lemma (small, mirrors V9's, no new Mathlib), then take
the (A)/(B) disposition to the owner -- it is a published-claim change, not an
agent call.

## CORRECTION to my own V6 above: (B) was never proved (2026-08-16)

The section above treats (A) and (B) as two established claims in tension.
That is wrong about (B), and the correction makes the finding stronger, not
weaker. I read the Lean sibling.

### The independence theorem does not mention a braid

`appendix-standard-model/strand-twist-datum.lean`:

    def TwistDatum (n : ℕ) : Type := Fin n → ℤ

    theorem exists_same_writhe_ne_totalTwist (n : ℕ) (hn : 0 < n) :
        ∃ t₁ t₂ : TwistDatum n, totalTwist t₁ ≠ totalTwist t₂ := by
      refine ⟨fun _ => 0, fun i => if i = ⟨0, hn⟩ then 1 else 0, ?_⟩

Its real content is "there exist two ℤ-valued functions with different sums",
witnessed by the zero function and delta_0. That is true of ℤ-valued functions
on ANY nonempty index type. There is no braid word, no writhe, and no fixed-word
hypothesis anywhere in the TYPE -- the name says `same_writhe` and the type
never mentions it.

Verified over the whole file: every occurrence of braid / writhe / word is in a
comment or docstring (lines 11, 13, 26-29, 91-93, 134, 180-182). The imports are
`Mathlib.GroupTheory.Perm.Basic`, `Mathlib.Data.Fintype.Perm`, `Mathlib.Tactic`
-- no braid group, no knot theory, no category theory. The file's entire
mathematical content is functions Fin n → ℤ, their sums, multisets, a
permutation action, and negation.

### So the model assumes the answer

Independence is not a discovered property of ribbon framings here. It is true BY
CONSTRUCTION: once the framing is modelled as an arbitrary `Fin n → ℤ`,
independence from the crossing data is immediate and contentless. Which is
exactly (A)'s problem stated from the other side -- a freely-chosen function is
not the ribbon category's canonical twist.

This lands in AGENTS.md's documented `proof-claims-unencoded` family: the
docstring asserts "over any fixed braid word (hence fixed writhe) there exist
framings with distinct total twist" while the Lean proves a triviality about
integer functions. The theorem is TRUE; it simply does not support the claim its
name and docstring make. (Not `: True`-vacuous -- worth stating precisely, since
the vacuity detectors key on that shape and would not fire here.)

### What this does to the disposition

My (A)-or-(B) disposition above was two-sided. It is one-sided:

  - dropping (A) does NOT rescue the hypercharge candidacy, because the property
    that would rescue it -- (B), separation at fixed braid word -- was never
    established.
  - the candidate's qualifying property is docstring-only.

`conj:sm-hypercharge-invariant`'s factorization criterion requires a coordinate
separating a writhe-degenerate PAIR OF STATES. `exists_same_writhe_ne_totalTwist`
exhibits two FUNCTIONS, not two states of a common braid. Those are different
claims, and only the second one would qualify the datum.

### The test the file skips, and it is small

State the claim with the braid in the type:

    ∀ (β : braid word), ∃ t₁ t₂ : TwistDatum n,
        (t₁, t₂ both arise as framings OF β) ∧ totalTwist t₁ ≠ totalTwist t₂

The content is entirely in the conjunct the current file omits -- what it means
for a framing to BE a framing of β. Supply that and independence is either a
theorem or false; as written it is neither. Until then the hypercharge candidacy
rests on an unformalized sentence.

Scope (a): a statement about what this file proves versus what it says. It does
not refute the hypercharge programme and does not touch tr_M.

## The missing formalization now exists (2026-08-16)

`QOU/StandardModel/TwistSeparationContent.lean` — lean-direct exit 0, no
warnings, no sorry / axiom / native_decide. Library file, no sidecar, so my own
verification is the gate (AGENTS.md §QA is agent-owned).

I said the test the original skips is "state the claim with the braid in the
type". Done, and the result is sharper than expected:

  separation_at_fixed_word
      the docstring's sentence, formalised WITH a word and a writhe present:
      at a fixed word beta, two framings of beta differ in total twist, and the
      pair is writhe-degenerate by construction. Proved for an ARBITRARY `Word`
      type and an ARBITRARY `writhe : Word -> Z`, both entirely UNUSED in the
      proof. The hypotheses are not there to be used.

  separation_holds_with_one_word
      the concrete kill: instantiate Word := Unit. ONE word, constant writhe,
      and the separation still holds. A statement that survives collapsing the
      braid group to a point is not evidence about braid groups.

  factoring_twist_cannot_separate
      the other horn: a twist factoring through the writhe (as a canonical
      ribbon twist does) is constant on writhe-degenerate pairs. V9's
      chirality_not_a_function_of_crossing argument applied to the twist.

  twist_dilemma
      the two horns as one statement.

`#print axioms`: factoring_twist_cannot_separate depends on NOTHING; the other
three on [propext, Classical.choice, Quot.sound] only — standard Mathlib, from
`by_cases`/`push_neg` and `Finset.sum`, not laundering.

### What this settles

The independence claim is TRUE and BRAID-FREE. Not false, not vacuous in the
`: True` sense — it simply cannot be evidence for a property of braid framings,
because it holds with no braid in sight. So the hypercharge candidacy cannot
rest on it, and the corpus faces the dilemma: free twist (separating power put
in by hand) or canonical twist (separates nothing).

### Untouched by both horns — the live route

A twist datum DERIVED from the braid word (qou-kebu, T2b) is neither free nor a
function of the writhe alone, so neither horn applies to it. That is the route
with content left in it. This file narrows the search; it does not close it, and
it does not refute conj:sm-hypercharge-invariant.
