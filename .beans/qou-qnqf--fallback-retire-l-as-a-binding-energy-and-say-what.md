---
# qou-qnqf
title: 'Fallback: retire L as a binding energy and say what it is instead'
status: todo
type: task
created_at: 2026-09-04T06:48:04Z
updated_at: 2026-09-04T06:48:04Z
---


**FALLBACK / cleanup.** Opened 2026-09-04. Not a repair — a retraction, held in
reserve for when the repairs are exhausted.

`L = log(tr_free / tr_bonded)` reads naturally as a free-energy difference if the
Markov trace is a partition function, so `B = alpha L` is an interpretive
identification, not a derivation. `qou-mu1h` showed it produces the wrong
two-body ordering; the convexity result showed no monotone reinterpretation
rescues it, since `B` remains a sum of per-type constants and therefore convex in
`Z` with its maximum at an endpoint. Flipping the sign only moves the maximum
from `Z = 0` to `Z = A`.

So the live question is not what `L` should be rescaled to, but whether `L` is a
binding channel at all.

**The corpus's own numbers already point this way.** `magic-A-binding-formula`
gives `4He` at `29.956` against `28.296`, a miss of `+5.9%`. The bond chain gives
`8.68`, a miss of `-69%`. The exposition's binding predictions do not use `L`;
outside the two blocks written during the `qou-m3sh` arc, nothing in `content/`
references the bond constants at all.

- [ ] Say what `L` IS, if not binding. Free energy of bond formation? A
      topological cost? It is a real, exactly-computable, convention-D-canonical
      quantity and it should be named correctly rather than quietly dropped.
- [ ] Audit which computations/probes depend on `B = alpha L` and mark them.
- [ ] Decide the fate of `B_sym` and the `t7qv` / `qou-brng` arc's numbers.
