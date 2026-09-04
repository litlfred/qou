---
# qou-1bua
title: 'GAP: ExplicitCentralIdempotentConjecture has no conj: content block, so its conjectural cone is invisible to the propagation audit'
status: todo
type: task
priority: normal
created_at: 2026-09-04T03:22:25Z
updated_at: 2026-09-04T03:22:58Z
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
