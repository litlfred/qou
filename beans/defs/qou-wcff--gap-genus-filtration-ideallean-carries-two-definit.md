---
# qou-wcff
title: 'GAP: genus-filtration-ideal.lean carries two definitional-tautology decls the vacuity ledger never saw'
status: completed
type: task
priority: normal
created_at: 2026-08-15T22:41:43Z
updated_at: 2026-08-15T23:31:00Z
parent: qou-pq8k
---

## What

Found while judging the `qou-5r17` derivation-claim candidates (`qou-1tls`).
The prose side is fixed on this branch; this bean is the Lean side, which is
outside that task's remit.

[`content/quantum-observable-universe/brings-surface/genus-filtration-ideal.lean`](../content/quantum-observable-universe/brings-surface/genus-filtration-ideal.lean)
has two `theorem`s whose **docstrings carry the file's non-trivial content**
and whose **statements carry none of it**:

1. `chebyshev_degree_eq_genus` — docstring: *"the polynomial degree of `a_p`
   in `u = s²` equals `(p-1)/2`. This is the non-trivial content: the
   algebraic complexity (Chebyshev degree) equals the topological complexity
   (Seifert genus). Stated as an opaque axiom because the full polynomial ring
   formalization is deferred."* The actual conclusion is
   `seifertGenus_T2p p = (p - 1) / 2`, closed `by intros; rfl`. Since
   `def seifertGenus_T2p (p : ℕ) : ℕ := (p - 1) / 2`, that is
   `(p-1)/2 = (p-1)/2`. `heckeCoeff` and `s` are bound in the statement and
   never appear in the conclusion.

2. `leading_chebyshev_coeff_is_one` — docstring: *"the coefficient of
   `s^{p-1}` (equivalently `u^{(p-1)/2}`) in `heckeCoeff s p` is 1. Stated as
   opaque axiom."* The actual conclusion is the `heckeCoeff` recurrence with
   `- s^(p-1)` added to both sides, closed by `ring`. It is a rearrangement of
   the defining equation and says nothing about a leading coefficient.

## Why it escaped every checker

`lean-vacuity-axiom-audit.ts` keys on **syntactic** tautologies (`: True`,
`X = X := rfl`). These are **definitional** tautologies: `A = B` where `A`
unfolds to `B`. Measured: `genus-filtration-ideal` appears **0 times** in
[`docs/audits/lean-vacuity-review-ledger.json`](../docs/audits/lean-vacuity-review-ledger.json),
and neither decl name appears at all. The file is a content-block sibling, so
it is in scope — it simply does not trip the pattern.

Note also that bean `491r` ("Prove genus_filtration_ideal", 2026-06-23) is
marked **completed** with an empty body, which reads as an all-clear over a
file whose two load-bearing declarations prove nothing.

## Two things to do

- **Instance:** discharge both honestly — state the real proposition (degree
  in `u`, leading coefficient) and prove it, or state it with `sorry` +
  `-- Ref:` per AGENTS.md §1. A docstring that says "stated as an opaque
  axiom" beside a `theorem … := by rfl` is the §1a audit-dodge shape: it is
  strictly worse than an `axiom`, because an `axiom` is visible to
  `#print axioms` and this is not.
- **Checker:** extend the vacuity detector to flag `theorem X : A = B` where
  `A` and `B` are definitionally equal after unfolding the file's own `def`s
  (whnf compare), not only where they are syntactically identical. This is a
  recall gap, not a one-off.

Claimed 2026-08-15 by claude/agent-discussions-queue-gibk4e (session qou-pq8k).


## RESOLVED 2026-08-15 (PR #5164)

**Instance — both decls proved, sorry-free.** Replaced with real statements
over `ℤ[X]` (`heckeCoeff` is stated for an arbitrary `s : R_q`, the wrong
shape for a degree claim):
`heckePoly_monic_natDegree` (monic, degree n), `heckePoly_coeff_parity`
(only degrees ≡ n mod 2 occupied), `chebyshev_degree_eq_genus` (deg_s a_p =
p-1 ∧ a_p even in s ∧ p-1 = 2·seifertGenus_T2p p ⇒ deg_u = genus),
`leading_chebyshev_coeff_is_one` (leadingCoeff = 1 ∧ coeff (p-1) = 1).
Verified: lean-direct exit 0; `#print axioms` on all five = exactly
[propext, Classical.choice, Quot.sound], no sorryAx; 0 sorries.

**Checker — two independent gaps, both closed.** (1) `RFL_BODY` did not list
`intros`, so `by intros; rfl` failed the body test. (2) `detectUnusedHypothesisRfl`
scans only parenthesised binders BEFORE the colon, so a ∀-telescope inside the
type left `head` empty and nothing was scanned. Added `telescopeParts` +
`detectTelescopeVacuousRfl` (two new patterns on the existing criterion).

**Measured, not overclaimed.** Fires on the pre-fix file with an accurate
diagnosis; corpus-wide the new patterns find **0** further instances, and no
first-party .lean outside vendored .lake/packages carries the shape. The
recall gap was real (structurally invisible); the instance count was 1, now 0.
Does NOT cover `leading_chebyshev_coeff_is_one`, which was ring-closed — a
rearrangement, not a definitional tautology, and a separate harder class.

**CORRECTION to this bean's own framing.** The claim that bean `491r` is 'a
stale all-clear over a file whose two load-bearing declarations prove nothing'
conflated two files. `491r` is about the LIBRARY file
`lean/QOU/Archimedean/genus_filtration_ideal.lean`, which carries neither
vacuous decl (grep count 0) and whose self-assuming projection flagged in
`docs/audits/2026-06-26-vacuity-candidate-triage.md` has already been
restructured into an honest conditional conjecture over the context. The two
vacuous decls were in the SIBLING block file. `491r` remains arguably
mislabelled (title 'Prove X', completed while X is a conjecture) but it is not
the all-clear this bean asserted.

**Left open:** the checker has no test harness and the repo has no root
tsconfig, so no regression fixture pins the new detector — its only evidence is
the pre-fix-file run recorded above.
