# Amendment 1 to the free-choice pre-registration — the SU(4) call over-claimed

**Date** 2026-08-27 · **Bean** `qou-04ub` · **Amends**
[`prereg-free-choice-2026-08-27.json`](prereg-free-choice-2026-08-27.json) ·
**The registry is NOT edited.**

## What I registered, and what is wrong with it

The registry called `su4-supermultiplet` the sharpest entry — free of choice,
and *"refutable in one measurement"* because it predicts the term vanishes for
every `A > 4`.

**I classified it from a one-line summary in an audit doc, not from the primary
source.** The primary source is
[`SU4SupermultipletGate.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/SU4SupermultipletGate.lean),
and its theorem is:

```lean
theorem su4_supermultiplet_dim_vanishes_iff (A : ℕ) :
    Nat.choose 4 A = 0 ↔ 4 < A :=
  Nat.choose_eq_zero_iff
```

A one-line consequence of a Mathlib lemma about binomial coefficients. No
nucleon, no braid, no `q₀` enters it. **The vanishing is analytic** — entailed by
the specification's own counting — so a measurement confirming it confirms
binomial arithmetic, and "refutable in one measurement" is wrong.

The gate's own docstring already carried the correct label: it says the gate
*"**predicts** the A=4 locality **already measured**"* (2.09× super-pairwise at
⁴He, ~0.94 by ⁶Li). That is postdiction, correctly marked at source. **My
registry entry lost the label in transit.**

## What this does to the rule under test

The rule: *no free choice ⇒ a definite prediction ⇒ testable.*

Both halves hold here. SU(4) genuinely has no free choice, and it genuinely
yields a definite prediction. What fails is a step **I silently added**: that a
definite prediction is an *informative* one. This one does not discriminate — it
holds for **any** object whose dimension is `C(4,A)`, binding-related or not.

So this is **not** one of the two refutation conditions I registered. It is a
**third failure mode I did not anticipate**:

> a choice-free candidate whose definite prediction is **analytic** rather than
> synthetic.

Recorded as a new mode rather than stretched into an existing one. The rule now
needs a second question after "is a choice left unfixed?" — namely **"could the
prediction have come out otherwise, given the specification?"** A prediction
entailed by the spec's own arithmetic answers no.

## What a synthetic test would be

The falsifiable content is the **identification**: that the missing
super-pairwise term *is* this cluster, at the right **magnitude** for `A ≤ 4`.
The gate's docstring supplies the target — 2.09× super-pairwise at ⁴He, ~0.94 by
⁶Li. **Predicting that magnitude, not the vanishing, is what could fail.**

## Why this is a separate file

The registry's anti-peek clause says corrections go in a new dated entry, never
an edit. Editing the over-claim in place would have destroyed the whole value of
pre-registering — a reader could no longer tell what was actually claimed before
the fact. The registry still carries the over-claim **verbatim**, with
`outcome: null`, and the guard probe asserts it. The git order of the two commits
is the evidence.

## The process error, named

The classification was made from a **secondary summary** when the primary source
was one grep away. That is the same class as the corpus-grep discipline in
AGENTS.md, and it took under an hour to surface — which is the pre-registration
working, not failing. A retrospective scoring would simply have recorded SU(4)
as "testable, confirmed" and learned nothing.

## Artifacts

- [`prereg_su4_prediction_is_analytic_probe.py`](../../computations/meson/prereg_su4_prediction_is_analytic_probe.py)
  — 5/5. One of its assertions failed on first run because I quoted the registry
  wrongly in my own check; the quote is now matched against the registry text.
- The registry and its guard are untouched.

**Scope (a).** This settles nothing about SU(4)'s correctness. It says the
*vanishing* is not a test of it.
