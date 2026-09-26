---
# qou-o7qo
title: Sweep context-class sorries in the 870 always-compiled modules — never audited
status: completed
type: task
priority: normal
created_at: 2026-08-09T10:50:58Z
updated_at: 2026-09-26T11:03:21Z
---


qou-octr swept only the **newly-visible** modules — those outside the pre-drain
`lake build` import closure (822 of 1692). Result there: **8 of 8 context-class
`sorry`s refutable.**

The other **870 modules always compiled** and have never been swept for this
defect. Nothing about the drain suggests they are better: the defect is not
caused by a module failing to compile, it is caused by a class carrying data the
theorem then makes claims about. A module compiles perfectly happily with a
`sorry` on a false statement.

If the 8/8 rate holds outside the newly-visible set, this is a corpus-wide
issue with the §3b-cond pattern rather than a local one — and §3b-cond's
guarantee (a downstream result may keep its provable kind because it rests on a
class-axiomatised conjecture) is void wherever the class carries no hypotheses
to rest on.

## First step

Enumerate context-class `sorry`s in the 870, then apply the qou-octr method.
The closure walk that produced the newly-visible list:
`/tmp/.../closure.py` in that bean's notes — BFS `import QOU.*` from `QOU.lean`,
subtract from the full module list, and take the complement for this bean.

Worth doing as a fixed-size sample first (say 12 at random) to get a rate before
committing to the full sweep.

---

## Swept 2026-08-09 — exhaustive, and my expectation above was wrong

This bean predicted "nothing about the drain suggests they are better". That is
**not what the data says**, and the correction is the interesting part.

| module set | modules | context-class `sorry`s |
|---|---|---|
| never compiled (outside the closure) | 822 | **18** |
| always compiled (inside) | 870 | **3** |

Six times the density in the modules no build ever touched, on a slightly
smaller module count. The defect is strongly concentrated where nothing was
ever built — which makes sense in hindsight: a module that compiles gets read,
its `sorry`s get reported every build, and the §3b-cond pattern gets applied
with more care in code that is actually exercised.

So no sampling was needed. All three were attempted, and **all three are
refutable** (proofs now sit beside the theorems, and in
`docs/audits/2026-08-09-unclosable-context-sorries.lean.txt`):

- `obstruction_trace_gap`
- `bare_is_lp_unstable`
- `dressed_is_lp_stable`

## The one that is worth reading

`obstruction_trace_gap`'s **own docstring** records how it got this way:

> The two conjuncts were previously carried as class fields
> (`kappa0_eq_chi_A`, `phi_1_image_eq_chi_A`) and projected here, which made
> this theorem assume exactly what it claims … Fields deleted; the gap is now
> real.

Someone found the **#1 self-assuming projection**, fixed it by deleting the
fields — and produced a **#10 unclosable sorry**. The gap became "real" in the
sense of no longer vacuous, and simultaneously became impossible to close.

**The two criteria are adjacent, and the naive fix for one creates the other.**
Deleting a conclusion-bearing field is only half a repair; the other half is
putting back the hypotheses the derivation needs. That belongs in the skill.

## Also worth noting

`bare_is_lp_unstable` (`∃ X, …`) and `dressed_is_lp_stable` (`¬ ∃ X, …`) share
a class, and **both are refutable** — by opposite instances (`Candidate := Empty`
for the first, one satisfying candidate for the second). A class that
constrains nothing refutes a statement and its structural opposite alike.

## Corpus total

**16 context-class `sorry`s attempted, 16 refutable, 0 survivors.** Three in the
newly-visible set remain unattempted (`nsi_q_kernel_identification`,
`four_term_pair_nucleon_counts`, `confinement_categorical`).
