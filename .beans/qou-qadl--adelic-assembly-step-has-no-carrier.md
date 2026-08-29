---
# qou-qadl
title: 'q-RH keystone: the adelic-assembly step is asserted in prose and carried nowhere'
status: todo
type: task
priority: high
created_at: 2026-08-29T17:00:00Z
updated_at: 2026-08-29T17:00:00Z
---

The arc's spine is

```
local q-zeta → Hasse–Weil → Re(ρ_i) = ½ at each place → [assembly] → classical RH
```

Steps 1–3 have blocks, Lean, and (as of `qou-hwax`) an honest conditional status.
**Step 4 has nothing.** `stochastic-mechanics/classical-riemann-hypothesis.md`
states it in a subordinate clause:

> The Hasse–Weil bound guarantees `Re(ρ) = 1/2` for each local geometry
> individually. The Riemann hypothesis asserts that this alignment survives the
> adelic assembly into the global zeta function.

No block, no conjecture, no Lean declaration states that implication.

## What is NOT the gap

`stochastic-mechanics/` does carry adelic infrastructure —
`prop:adelic-reeb-restricted-product` (sorry-free), `def:adelic-substrate`,
`rem:adelic-tate-squeeze`, `rem:adelic-tate-motivic-dual`,
`rem:classical-limit-adelic-assembly`. Do not read that as the step being
carried. The last one is a **remark** with `interprets:
def:classical-limit-functor`, and it is about the archimedean projection `ρ_∞`
of a motivic realization tower — the `q → 1` collapse of the local Reeb
infinitesimal. It says nothing about critical-line persistence.

Corpus-grep, all six paths: "adelic assembly" — 0 in `docs/audits`,
`docs/coordination`, `computations`, `library/INDEX.md`. "critical line" — 0 in
all four. The step is genuinely unstated.

## Why this is the keystone and not one gap among several

Hasse–Weil holds at **every** place, unconditionally, for curves over finite
fields — that is Weil's theorem, and it has been known since 1948 while RH has
stayed open. So local critical-line alignment at every place cannot by itself be
close to RH; the assembly step is carrying the entire distance. Any claim that
the arc "reduces RH to" the local statement is measuring the wrong leg.

Naming it is the whole first task, and it is cheap: a `conjecture` block stating
the implication, `uses` the local corollary, `sorry` + `-- Ref:` per §3b, a
primary conjecture per §3b-tax. That puts the arc's actual claim where it can be
read and attacked instead of inside a subordinate clause — and it makes the
distance visible rather than eliding it.

Sequencing note: `qou-qspc` (the spectral coordinate map) is upstream of this.
The assembly statement should quantify over the *Reeb* spectrum, so it wants that
map to exist first, or it will restate the same ambiguity one level up.
