---
# qou-ke35
title: The mpf migration of the constant modules is HALF DONE, and a consumer that never raises mp.dps now records 15 digits where it used to record 17
status: todo
type: task
priority: high
created_at: 2026-09-13T16:24:39Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

## The claim

The constant modules are **mid-migration from `float` to `mpmath.mpf`, and every
one of them is currently mixed**:

| module | mpf consts | float consts |
|---|---:|---:|
| `codata_constants` | 35 | **0** — fully migrated |
| `experimental_constants` | 24 | 73 |
| `q_parameter` | 11 | 34 |
| `hecke_core` | 9 | 28 |

`q_parameter` carries both spellings of the same quantities under a `_MP`
suffix — `Q_MP`/`Q`, `HA_MP`/`HA`, `HBAR_Q_MP`/`HBAR_Q`, `LN_Q_MP`/`LN_Q` — so
a consumer's precision depends on which name it happened to import.

**The hazard is not the mixture. It is what happens to a consumer that imports
the mpf name and never raises `mp.dps`.** mpmath's default is **15**, and
`_precision.set_compute_dps()` is what moves it to 70. A producer that never
calls it computes its mpf arithmetic at 15 digits — *fewer than the 17 a float64
carries*. So for that producer the migration **lowered** the recorded precision.

## Measured, on a producer, end to end

`per_atom_rho_deviation.py` had never called `set_compute_dps()`. That was
harmless until `experimental_constants.M_E_MEV` became `mpf('0.51099895069')`.
Running the **unmodified** producer against its own committed witness:

```
committed 2026-08-23 (float64)   28.31287182283982       17 sig figs
unmodified re-run today (mpf)   '28.3128718228398'       15 sig figs
raw-float64 count                139 -> 42
```

Two digits lost, and **97 fields dropped off the raw-float64 ratchet at the same
moment** — because an `mpf` serialises as a string and the counter stops seeing
it. A greener gate bought with a worse record, arriving by accident rather than
by anyone's intent. `scriptHash` MATCHES throughout: import-cone drift, invisible
to the `git diff <producer>` check.

Adding the one line restores it — same numbers, ~33 digits instead of 17,
agreeing with the committed float64 across its whole range (rel 1.9e-17 to
2.8e-16). Fixed in the drain branch.

## Population

Of the 979 live dirty witnesses (922 with a resolvable producer, 23,417 fields):

| class | entries | fields | share |
|---|---:|---:|---:|
| producer never calls `set_compute_dps` | 336 | 11,217 | **47 %** |
| producer imports a float64 `Q` | 152 | 6,950 | 29 % |
| producer imports `hecke_core` | 41 | 2,787 | 11 % |
| **imports an mpf constant AND never raises dps** | **61** | **3,110** | **13 %** |

That last row is the one that is *actively recording fewer digits than it used
to*. The other 47 % is the ordinary case — pure-float producers, where
`set_compute_dps` alone changes nothing and a real conversion is needed.

**Do not read the 47 % as 47 % one-line fixes.** `per_atom_rho_deviation` was
cheap only because its constant was already `mpf`. `jet_knot_invariants` and
`delta_q_decoration`, both also missing the call, compute in float throughout and
gain nothing from it.

Top of the hazard set by field count:

```
 637  r5-full-canonical-knot-solver
 299  binding-single-pipeline-comparison
 276  probes/adjacent-vs-full-probe   (and its twin, 276)
 118  unified-mass-molecular
 116  gram-matrix-dual
 112  jet-tower-delta-max
 102  sweeps/low-isotope-binding-sweep
```

## A CANDIDATE mechanism for `qou-sogb`, offered as a lead and not a conclusion

`r5-full-canonical-knot-solver` is the **largest** entry in the hazard set, and
it is the subject of `qou-sogb`: byte-identical producer, `scriptHash` matching,
and **733 of 1448 fields move on re-run** — including `rank_in_full_search`
990 → 1013 and the LP's active channel set. That bean explicitly records the
cause as **not established**, with both the environment and six first-party cone
modules having moved.

This gives a third, specific, testable candidate: a constant in `r5`'s cone
became `mpf` while `r5` never raises `mp.dps`, so its arithmetic moved from
float64 to **15-dps mpf** — a change in both type and precision, at every use.

**I have not tested it**, and it should not be written into `qou-sogb` as the
answer. The discriminator is cheap: add `set_compute_dps()` to `r5`, re-run, and
see whether the 733 moves shrink toward the value the committed witness holds. If
they do, the cause is this; if they do not, this is ruled out and the bean's two
existing candidates stand.

## What I am NOT proposing

**Not a sweep.** 336 producers is exactly the corpus-wide pass the 2026-09-07
ASK-THE-OWNER directive says not to start on the strength of a rule. Each one
needs the same per-producer screen the drain uses — is its constant already mpf
(one line), or is it float throughout (a conversion)? — and the second case is a
real edit with real verification.

**And a one-line fix is not free even when it applies.** It changes every
recorded value in that witness, so it needs the unmodified-first run, a
field-by-field comparison, and a re-run whose cost has to be checked first.

## Options

**A. Leave it; drain producer by producer as the queue reaches them.**
- *Costs*: nothing now.
- *Risks*: the hazard set keeps growing as more constants migrate, and each new
  one silently drops a witness from 17 digits to 15 while making the ratchet
  look better.
- *Default if nobody acts.*

**B. Add a gate.** A check that fails a producer importing an `mpf` constant
without `set_compute_dps()`. Mechanical, cheap to write, and it stops the class
growing.
- *Costs*: one audit script, plus a baseline for the 61 existing.
- *Risks*: another ratchet to drain; false positives where a producer legitimately
  wants low precision (I know of none, but have not looked).

**C. Finish the migration in the constant modules** — retire the `_MP` suffix so
there is one spelling per quantity.
- *Costs*: large, and it moves numbers in every consumer.
- *Risks*: high; this is the sweep the directive is about.

## Recommendation — my judgement, not a finding

**B, then A.** The gate is the cheap part and it is the part that stops the
problem growing; draining the 61 can then happen at whatever pace the queue
allows. C is the real fix and is an owner-scoped decision, not an agent's.

The `r5` discriminator above is worth running on its own regardless — it is one
producer, one line, and it would either explain or eliminate the largest
unexplained witness movement currently on the books.


---

## 🛑 THE `r5` LEAD IS RULED OUT — tested the same hour, and it was mine

The section above offers the missing `set_compute_dps()` as a candidate
mechanism for `qou-sogb`'s 733 moving fields in
`r5-full-canonical-knot-solver`, and says the discriminator is cheap. It was:
**11 seconds**. It is also **negative**, and the candidate is withdrawn.

**Reproduced first.** Committed witness vs an unmodified re-run: **707**
substantive diffs (`qou-sogb` recorded 733 — same phenomenon; I did not chase
the 26, which could be main having moved or a different ephemeral mask).
`scriptHash` matches at `667a84ec1d91` both sides, as that bean says.

**The mechanism is visible in the diff, and it is not precision.** The
**winner changes**:

```
/data/per_atom_results[0]/winner/L           4 -> 6
/data/per_atom_results[0]/winner/braid_word  LEN 4 -> 6
/data/per_atom_results[0]/winner/markov_trace  0.9156174644181682 -> 1.160986499639014
```

A different braid word is selected, and `markov_trace` moves **27 %**. That is
a search returning a different answer, not digits shifting.

**Then the test.** Injected `set_compute_dps()` after the `_path_bridge`
import, re-ran, diffed against the unmodified run:

```
diffs = 156
winner L: 6 -> 6          <-- UNCHANGED
```

The surviving 156 are ~1e-20 LP-solver noise (`y_star_str[0]` differs at the
14th digit) plus one rendering change. **The winner does not move**, so the
selection is not fragile at this precision and the missing `set_compute_dps`
is **not** what changed `r5`'s answer.

Producer restored byte-identical; every witness the run touched reverted.

**What this means for `qou-sogb`:** its two existing candidates — environment
drift and import-cone drift — stand, and one specific sub-candidate is now
excluded. That is a narrowing, not an answer, and it should be recorded there
as such rather than as progress toward a cause.

**What it means for this bean:** the population measurement and the
`per_atom_rho_deviation` case are unaffected — those were measured directly.
Only the `r5` lead was speculative, and it is gone. **The 637 fields of `r5`
are NOT in the drainable-by-one-line set**, which lowers the practical value of
the 61-witness hazard row by its single largest entry: 3,110 → **2,473** fields
once `r5` is removed.

Worth stating plainly because the section above reads as more promising than it
turned out to be: I found a pattern, offered it as a lead, tested it, and it was
wrong. The pattern is still real for `per_atom_rho_deviation`; it is not a
general explanation.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-9nnz`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8357, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-14: "beans(qou-ke35, qou-sogb): the constant modules' mpf migration is half done — and my r5 lead from it is ruled out, teste"). The work may be partly or fully done. Read the bean before you close it.
