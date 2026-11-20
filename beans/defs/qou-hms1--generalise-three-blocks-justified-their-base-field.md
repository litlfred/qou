---
# qou-hms1
title: 'GENERALISE?: three blocks justified their base field / R codomain by a square root convention D does not have'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T21:10:17Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---


## The pattern

Convention C's `z = 1/(q^{1/2} + q^{-1/2})` needs a square root of `q`. Convention
D's `z = q^3/(q^2+1)` is a rational function of `q` and never leaves `ℚ(q)`.
Several blocks had built base-field or codomain arguments on that square root.

`markov-trace-frobenius-selection-proof` already retired its own instance:

> The older $\mathbb{Q}(q^{1/2})$ hypothesis was an artefact of convention C,
> whose $z = 1/(q^{1/2}+q^{-1/2})$ needs the square root; convention D's
> $z = q^{3}/(q^{2}+1)$ does not, and nothing below leaves $\mathbb{Q}(q)$.

**That correction was propagated to exactly one of four places.** The other three
were invisible to any value-based sweep, because none of them quotes a number —
they were found only by the `c-formula-unlabelled` detector added in `e6c7d599b`.

## Status of each

| block | state | commit |
|---|---|---|
| `markov-trace-frobenius-selection-proof` | already correct | pre-existing |
| `qvalue-derivation-chain` | **RESOLVED** — `V̂_i` exact in `ℚ(q)`, not `ℚ(q^{1/2})`; `z` was its only √q source, the transfer matrix `T` is over `ℚ(q)` | `a5ca7e073` |
| `per-braid-mass-tower` | **RESOLVED** — √q was one of three reasons for `ℝ`; the other two (absolute values, `Φ_q`) stand, conclusion unchanged, no Lean signature moves | `48040f71e` |
| `hecke-satisfies-blitvic-hypothesis` | **OPEN — this bean** | `48040f71e` flagged it |

## The open question

`HeckeSatisfiesBlitvicHypothesisContext` types its trace codomain as `ℝ`
(`tr_M : A → ℝ`, `z_real : ℝ`, `pairWeight : ℕ → List ℕ → ℕ → ℝ`,
`centredMoment : List ℕ → ℝ`). The carrier `A` is already a generic `Type u` with
its own `ringA`, so only the *scalar field* is specialised.

Its §7c note gives exactly one reason for that specialisation, and says so:

> That codomain is `ℝ` because of what `z_real` is: the class docstring defines
> the Markov parameter as `z = 1/(q^{1/2} + q^{-1/2})`, i.e. it requires a
> **square root of `q`** … The odd-length vanishing itself would generalise to
> any `AddCommMonoid` codomain, so this is a specialisation of the *scalar
> field*, not of the algebra — **and it is the square root, not the ordering,
> that forces it.**

Under D there is no square root. By the note's own reasoning the stated
obstruction is gone.

**Do not treat that as a licence to generalise.** Losing the stated reason is not
proving no reason exists. Before touching the signature:

- [ ] Audit `pairWeight` for a hidden order or completeness dependence — it is
      `ℕ → List ℕ → ℕ → ℝ` and nothing yet says it lands in `ℚ(q)`.
- [ ] Audit `centredMoment` likewise (a *centred* moment subtracts a mean; check
      whether that needs division only, or ordering).
- [ ] Check whether `z_real` is used anywhere in a way that needs `ℝ`'s
      completeness or order (comparisons, `abs`, limits) rather than just its
      field structure.
- [ ] If all three come back clean, restate the class over a `CommRing`
      (or `Field`) `R` with `z : R` and re-run the Blitvič-hypothesis proof.
- [ ] If any does not, replace the §7c note's justification with the real one —
      the current note would still be wrong even though the conclusion stands,
      which is the `per-braid-mass-tower` situation.

## Why it is worth doing

The Blitvič hypothesis is the odd-length vanishing result. If it holds over a
generic commutative ring it is a statement about the algebra rather than about
evaluated real numbers, and it stops being stranded on the archimedean side of
the §7c wall. That is a genuine strengthening, not tidying.

## Do NOT

Do not "fix" this by deleting the §7c note. It records what was claimed and why;
the correction note added in `48040f71e` sits beside it. Bean `qou-emyt` has the
wider excision context.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8349, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-09: "bean qou-hms1: the sqrt-justified base fields -- two resolved, one open Lean question"). The work may be partly or fully done. Read the bean before you close it.
