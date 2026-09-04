---
# qou-1bua
title: 'GAP: ExplicitCentralIdempotentConjecture has no conj: content block, so its conjectural cone is invisible to the propagation audit'
status: completed
type: task
priority: normal
created_at: 2026-09-04T03:22:25Z
updated_at: 2026-09-04T11:01:52Z
---

## What is open

`content/quantum-observable-universe/mass-endomorphism/explicit-central-idempotent.lean`
declares, and is the ONLY file in the corpus that mentions:

    /-- **CONJECTURE (OPEN).** The four cross-checks follow from Lagrange
        interpolation in commuting variables. -/
    class ExplicitCentralIdempotentConjecture {R : Type*} [CommRing R] (q : R) : Prop where
      idempotent : ∀ {n : ℕ} (lam : List ℕ) (_h : lam.sum = n),
        centralIdempotent lam q * centralIdempotent lam q = centralIdempotent lam q

`prop:explicit-central-idempotent` is stated conditionally on it, correctly
(AGENTS.md §3b-cond item 2: `[hi : ExplicitCentralIdempotentConjecture q]` is an
explicit instance binder on `explicit_central_idempotent_via_murphy`).

## Why it matters

§3b-cond item 4 asks that `uses[]` name the conjecture explicitly, so the
conditional dependency is auditable from the manifest. It cannot be satisfied
here: there is **no `conj:` content block** for these cross-checks. Measured
2026-09-04 — no `conj:` label in `content/quantum-observable-universe` mentions
idempotent / Murphy / Lagrange / Wedderburn, and `ExplicitCentralIdempotentConjecture`
occurs in no other `.lean`.

Consequence: `conjectural-propagation-audit.ts` reads `uses[]`, so this block
presents as a plain `proposition` with an empty conjectural cone. The Lean is
honest; the manifest is not, and the audit cannot see the gap.

## What was done in PR #6540

- The `(2,2)` specialisation was an `example` with no binders — it stated the
  idempotency UNCONDITIONALLY while proving it from the conditional theorem.
  Lean refused it (`failed to synthesize ExplicitCentralIdempotentConjecture q`);
  that refusal is what surfaced this. Now `theorem
  explicit_central_idempotent_two_two [ExplicitCentralIdempotentConjecture q]`,
  named rather than anonymous so it is citable. lean-direct exit 0, 0 warnings.
- §3b-cond item 3 banner added to the `.md`.
- The item-4 gap recorded as an `authorNotes` note on the `.ts`.

## Next honest step

Register a `conj:` content block for the four cross-checks (sum-to-identity,
orthogonality, self-adjointness, bar-pairing), whose sibling `.lean` re-exports
or re-declares the class, then add its label to this block's `uses[]`. That is a
content addition, not a compile fix, which is why it was not done inline.

Verified separately: **no instance of the class exists anywhere** — correct per
§3b-tax (an unproved primary is a content-bearing class with no instance). Do
not fabricate one to "close" this.


---

## CLOSED 2026-09-04

`conj:explicit-central-idempotent` is registered
(`content/quantum-observable-universe/mass-endomorphism/conj-explicit-central-idempotent.{ts,md}`)
and named in `prop:explicit-central-idempotent`'s `uses[]`, so §3b-cond item 4
is satisfied and the conditional cone is auditable from the manifest.

**Not done by copying the class into a second sibling.** A sibling `.lean`
cannot import another sibling, so a `conj:` sibling declaring the class would
have produced two independent declarations of one name — the divergence shape
recorded in `docs/audits/2026-09-03-sibling-lean-compile-sweep.md` §"A cost of
this sweep". Instead the carrier moved to the library module
`QOU.BraidKnot.ExplicitCentralIdempotent` (`SYT`, `qContent`,
`centralIdempotent`, `ExplicitCentralIdempotentConjecture`), registered in
`QOU.lean`; the proposition's sibling now imports it and keeps only its two
theorems. The `conj:` block has NO sibling `.lean` (§0a "no shadowing stubs")
— its `lean.ref` resolves to the library class.

**Measured effect**, clean before/after on the same post-merge tree
(`scripts/conditional-on-class-hypothesis-audit.ts`, stash / re-run / pop):

| bucket | without the change | with it |
|---|---|---|
| BINDS a cone class (item 2 satisfied) | 8 | **9** |
| binds SOME carrier, not the cone's own | 69 | 68 |
| binds NO class at all | 49 | 49 |

`prop:explicit-central-idempotent` moved from "binds some carrier" to "binds a
cone class": its `[ExplicitCentralIdempotentConjecture q]` hypothesis is now
recognised as belonging to its OWN conjectural cone, which is the whole point.
`class_axiomatised_conjectures` 166 → 167.

Verification: library module and prop sibling both `lean`-direct **exit 0, zero
diagnostics**; `#print axioms` `[propext, Classical.choice]` on both theorems,
no `sorryAx`; `run-validate` exit 0, "✓ Valid — 9 issue(s)", all pre-existing.
Render-QA grep battery clean on the new `.md` (balanced `$`/`$$`/braces, no
list-parser hijack, no inner math environment in a raw fence — the first draft
had `\mathtt{}` inside a ```` ```tex ```` fence, which is horizontal mode and
would have aborted pdflatex; replaced with a code span).

Still true and still deliberate: **no instance of the class exists anywhere**,
correct per §3b-tax for an unproved primary conjecture.
