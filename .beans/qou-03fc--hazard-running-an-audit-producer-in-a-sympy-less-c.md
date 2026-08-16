---
# qou-03fc
title: 'HAZARD: running an audit producer in a sympy-less container silently DEGRADES its witness (two q0 witnesses are also genuinely stale on main)'
status: todo
type: bug
created_at: 2026-08-16T12:39:42Z
updated_at: 2026-08-16T12:39:42Z
---

Found while running `scripts/precision-gates.sh --changed` as the pre-commit
preflight on PR #5205, whose diff touched only a `.lean` and `docs/audits/`.

## Two separate things, and they pull in opposite directions

**1. Two committed witnesses ARE genuinely stale on main.** Regenerating moved
real counts, not just metadata:

| witness | count that moved |
|---|---|
| `computations/q0-value-drift-audit.witness.json` | `proton-pin` **796 -> 797** (new entry: `computations/qbeta/qbeta-decay-channel-convention-status.witness.json`, a recent main landing) |
| `computations/audits/q0-anchor-consistency-audit.witness.json` | `Q0_OK` **650 -> 651**, `Q0_AMBIGUOUS` **16 -> 15** (`binding-alpha-shift-witness.witness.json` reclassified) |

By the gate's own instruction ("if a COUNT moved, the committed witness was
stale: commit the regenerated one and say which count changed") these should be
refreshed.

**2. But I could not refresh them honestly, because this container has no
sympy.** The regenerated `q0-anchor-consistency-audit.witness.json` **drops the
`"sympy": "1.14.0"` environment entry entirely** — no replacement value, the key
just disappears. Committing that would record my container's missing dependency
as a fact about the computation. That is the same failure class as widening a
baseline to make a red run green: it makes the gate pass by degrading the
evidence rather than by fixing anything.

**So I reverted both files and shipped neither.** Recording rather than
half-fixing.

## Why this is a hazard and not just a chore

The degradation is **silent and asymmetric**. The producer does not fail, warn,
or exit non-zero when sympy is absent — it emits a witness that is *correct in
its numbers* and *wrong in its provenance*, and the missing key is a deletion,
which reads in a diff as tidying rather than as loss. An agent that runs a
precision gate as a preflight, sees "modified witnesses", and follows the gate's
own advice to commit them will land the degradation without noticing.

Two aggravating factors:

- **`precision-gates.sh --changed` regenerated these even though nothing
  precision-relevant was in my diff** (a `.lean` file and two `docs/audits/`
  files). Whatever selects producers to re-run is over-broad, so the hazard
  fires on PRs that never touch `computations/`.
- **The gate reported RED after mutating the tree**, so the RED was partly about
  files its own run had just changed. A preflight that dirties the working tree
  and then grades it is hard to act on correctly.

## What to do

1. **Make the producer refuse rather than degrade.** If an environment key
   cannot be determined, exit non-zero (or write an explicit
   `"sympy": "unavailable"`) instead of dropping the key. A missing dependency
   should never be expressible as a silent deletion.
2. **Refresh the two witnesses from a container that has sympy**, and say which
   counts moved (they are recorded above, so the refresher can check the numbers
   still match rather than trusting a fresh run blind).
3. **Narrow `--changed`** so it does not re-run `computations/` producers for a
   diff that contains no `computations/` or witness file.
4. Consider whether other producers drop environment keys the same way — this
   was found by eye in a diff, not by any checker.
