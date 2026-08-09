---
# qou-o7qo
title: Sweep context-class sorries in the 870 always-compiled modules — never audited
status: todo
type: task
created_at: 2026-08-09T10:50:58Z
updated_at: 2026-08-09T10:50:58Z
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
