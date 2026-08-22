---
# qou-vfy1
title: '221 blocks assert status "verified"; 64 are not supported by the witness they cite, and the field is forbidden anyway'
status: todo
type: task
priority: normal
created_at: 2026-08-22T05:20:00Z
updated_at: 2026-08-22T05:20:00Z
---

The quantified form of class **C2** in the `qou-3nva` ledger — a block and
its witness disagreeing, with the block winning. Measured corpus-wide
2026-08-22.

## Two findings, one scan

**1. The `status` field should not be in a `.ts` at all.** AGENTS.md §4:
*"Formalization status … is **not stored in `.ts` manifests**. It is derived
at build time … Agents must **never** add a `status` field to content block
`.ts` files."* Measured: **278** content-block `.ts` files carry one.

| value | count |
|---|---:|
| `verified` | 221 |
| `experimental` | 52 |
| `not_run` | 4 |
| `pending` | 1 |

**2. Of the 221 `verified` claims, 64 (29 %) are not supported by the
witness they name.**

| | count |
|---|---:|
| witness `allPassed: true` **with real assertions** | 157 |
| witness `allPassed: true` but **assertions array is empty** (vacuous) | **43** |
| witness reports **`allPassed: false`** | **8** |
| cited witness **missing or unreadable** | 5 |
| **no witness cited at all** | 8 |

The 43 vacuous ones are the interesting bulk: `allPassed: true` over zero
assertions is *true* and means nothing, and it is what a block points at
when it says "verified". Related but distinct from the ~383-witness bean on
the same shape — that one is about the witnesses; this is about the blocks
that **cite them as verification**.

## Limits of the measurement, stated

- **The 157 is an upper bound on genuine support.** Passing assertions do
  not imply the assertions *cover the block's claim*. The campaign found
  several where they do not — one witness's assertions covered clause (1)
  of a three-clause proposition; another's two assertions were both about
  vanishing while the block was cited for a field-membership sentence.
- **The 5 "missing" may over-count**: witness paths were resolved with a
  basename fallback under `computations/`, which will miss anything stored
  elsewhere.
- The scan reads the **first** `status` and the **first** witness path in
  each file.

Reproduce: the script is inline in the session; the shape is
`grep '^\s*status:\s*"' content/**/*.ts` joined against the first
`*.witness.json` named in the same file.

## What would close this

The systemic fix and the cleanup are the same act: **delete the field.**
§4 already says status is derived at build time from the Lean and the
witness, so a `.ts` asserting `verified` is both forbidden and structurally
incapable of being wrong — nothing checks it against the thing it claims.
Removing it makes the 64 unsupported claims disappear by construction,
because the derived status would read the witness.

If the field is kept for any reason, it needs a checker that fails when a
block claims `verified` while its witness is absent, failing, or vacuous —
which is the 64.

Order of work, cheapest first:

1. The **8 blocks citing a witness that reports `allPassed: false`** — a
   direct contradiction, and the smallest set.
2. The **8 with no witness at all** and the **5 unresolvable** — either the
   citation is wrong or the claim is unbacked.
3. The **43 vacuous** — these need the witness fixed (assertions added) or
   the block's claim withdrawn; they are not fixable from the block side.
4. The field's removal corpus-wide, per §4.
