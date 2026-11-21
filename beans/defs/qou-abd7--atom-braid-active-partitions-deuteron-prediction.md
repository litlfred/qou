---
# qou-abd7
title: atom_braid_active_partitions deuteron prediction fails at exact h
status: todo
type: bug
priority: normal
created_at: 2026-10-13T00:00:00Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

**Finding (2026-10-13, owner ruling D on the PR #7788 follow-up, branch
`claude/stale-values-dgh-2026-10-13`).**

`computations/atom_braid_active_partitions.py` tests
`conj:atom-braid-exterior-algebra`: the canonical atom braid
`atom_braid_word_3A(Z, N)` should have at most `3A - Z + 1` partitions
`lambda |- 3A` with nonzero character.

Until 2026-10-13 the probe tagged letters against a typed
`HA = 0.20906032198987945`, 1.1095e-7 relative from the live
`h = q - 1/q`. No averaged / inverse letter matched its 1e-12 tag, every
character evaluation raised `ValueError("unexpected d=...")`, the bare
`except` turned each into `None`, and the probe reported 0 active
partitions -> PASS. The PASS was vacuous: no character was ever computed.

With `h` read from its owning source (`Q_50_DIGIT_STR`, as
`atom_braid_word_3A` builds it) and characters through the mpfr kernel:

| atom | active | bound 3A-Z+1 | match |
|---|---|---|---|
| D   | 11 / 11 | 6 | False |
| T   | 30 / 30 | 9 | False |
| 3He | 30 / 30 | 8 | False |

Smallest deuteron `|chi|` = 0.0367 at `(2,2,1,1)`, so the failure is not
the 1e-6 activity threshold. `allPassed` True -> False.

**This agrees with the corpus's own earlier record.**
`docs/audits/2026-05-25-exterior-algebra-lp-claim-falsified.md` (same probe,
2026-05-25) already reported "All p(n0) partitions have non-trivial chi_lambda"
for D, T and 3He. So the committed PASS was a *regression into vacuity* after
that audit, not a confirmation the audit missed: the FAIL restores agreement
with the recorded negative. Remaining work is that audit's item 1 (re-scope
the LP/SDP-implications section of `conj:atom-braid-exterior-algebra`), if it
has not landed — check before acting.

**Scope (a)**: this word, this activity definition (unweighted
`|chi_lambda| > 1e-6`). Not a structural exclusion of the conjecture.

**Open questions (not decided here):**
- Is "active" meant as `chi_lambda != 0` or as `y_lambda chi_lambda != 0`?
  Under convention D every >=3-row `y_lambda` vanishes, which would cut the
  deuteron count from 11 to the <=2-row partitions (4 at n=6) — still
  compare against the bound before reading that as rescue; choosing the
  definition because it passes would be selection against the target.
- Does the conjecture's content block / any consumer cite the old PASS?
  `grep -rn atom-braid-active-partitions content/ docs/` before quoting.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-v2om`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8313, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). **Superseded premise found:** this bean's numbers are computed on the pre-2026-11-15 interface letters of `atom_braid_word_3A`, which the γγ ruling superseded (`docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`; redo waits on the γγ-selected nucleon word, PR #7876). The vacuous-PASS repair (2026-10-13) stands as code hygiene; the D/T/3He active-partition counts are on the old word.
