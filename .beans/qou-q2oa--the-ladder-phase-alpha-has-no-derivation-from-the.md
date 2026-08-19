---
# qou-q2oa
title: The ladder phase alpha has no derivation from the actual Wedderburn weights
status: todo
type: task
priority: high
created_at: 2026-08-16T11:40:16Z
updated_at: 2026-08-16T11:40:16Z
parent: qou-cdx1
---

Parent tranche: `qou-cds1` (S1 — re-derive the Q_β `c_k` ladder under D).
This bean names **where the S1 wall actually sits** after PR #5187's
retraction; `qou-cds1` predates that finding and does not enumerate it.

## The claim

**There is no derivation of the ladder's phase `α` from the actual
Wedderburn weights — in either convention frame.**

Stated as the wall by PR #5187 (merged `fdd58a4f39`), verbatim:

> The D-frame weight vector is no longer open — S2 computed it, and
> `y_(1³) = 0` falls out. What *is* open is the **phase**: the relation
> `α = −h/4 − (h/2)·y_(2,1)` was read off the bogus instance, so **there is
> no derivation of the ladder's `α` from the actual Wedderburn weights in
> either frame.** That is the wall, and it is narrower and differently
> placed than this PR originally said.

## What was retracted, and why

The affine relation `α = −h/4 − (h/2)·y_(2,1)` was read off the vector
`(z, 1/2−z, z)`, which satisfies **only** the normalisation condition of
`CanonicalMarkovWeightsH3` and **fails** the other two Markov conditions
(h2/h3). It is therefore not a weight vector of `H₃(q)` at all, and
`1/2 − z_D` is simply not `y_(2,1)` — at `q ≈ 1.11` the two differ in sign
as well as magnitude (`−0.1127` vs `+0.2473`).

PR #5187 classes this as a **symbol-collision / claim-shape failure**: a
formula was given the name of an object whose defining conditions it does
not satisfy. A topic grep returned plenty and read as corroboration; the
skipped step was checking the defining conditions. (AGENTS.md §"Grep the
claim SHAPE, not only the topic".)

## The input now exists; the derivation does not

S2 solved the corpus's own three defining conditions for the `H₃(q)` Markov
weights at `z = z_D`:

| λ | rows | `y_λ` under D | sign for `q > 1` |
|---|---|---|---|
| `(3)`   | 1 | `(q⁴+1)/(q²+1)²` | positive |
| `(2,1)` | 2 | `q²/(q²+1)²`     | positive |
| `(1³)`  | 3 | `0`              | identically zero |

Signature `(5, 0, 1)` — positive semidefinite. So the D-frame weight vector
is **known**. What is missing is any argument connecting it to the ladder's
phase. The gap is a derivation, not a measurement.

## What survives and must not be re-broken

- **The Lean stands, renamed.** `1/2 − z_D < 0` for `q > 1` is true and was
  never in question; only the interpretation was wrong.
  `threeRowMiddleWeight*` → `ladderPhaseCoeff*`, so the names now describe
  what is actually proved. Sorry-free; `#print axioms` clean on all ten
  declarations.
- **`κ(z) = 1/2 − z` is an affine coefficient in one ansatz.** Its sign
  carries **no trace-positivity content.** Do not re-read a `κ` sign change
  as a statement about either trace.
- **Convention D does not fail positivity.** That scope-(b) structural
  exclusion was withdrawn — the invariant it cited (a negative Wedderburn
  weight) does not exist. The surviving statement is scope-**(a)**: the C
  ladder's phase formula does not transport to D by substituting the
  parameter.
- **`−974.43` is a sensitivity measurement, not a proposed value.** It is
  what the current extractor returns when fed `z_D`. Do not wire it
  anywhere. (Also recorded on `qou-cds1`.)

## What to do

1. Derive `α` from the weight vector above, or establish that it is not
   determined by the weights alone — a clean negative is a result here.
2. **Do not** re-read a relation off an instance without first checking it
   satisfies the defining conditions of the object it is named for. That is
   the exact failure this bean records; PR #5187's probe A7r exists to stop
   the specific conflation returning (asserts D weights PSD and
   `κ(z_D) = −0.1127 < 0 < 0.2473 = y_(2,1)`), but it guards one instance,
   not the habit.
3. Keep the anti-fit discipline: a phase obtained by inverting the Q_β
   anchor is a **fit**, must be labelled one, and may not be wired to
   production as canonical.

## Provenance

Filed 2026-08-16 from an agent that could not reach the `beans` CLI. All
quotations from PR #5187's merged body (`fdd58a4f39`, merged 2026-08-16);
the D weight table is S2's, PR #5185 §3bis, cited there rather than
re-derived.
