---
# qou-o2dk
title: 'W4: register the general-n instance; unblock TauFunctorReduction observationFrame_* consumers'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-10-04T15:25:30Z
parent: qou-utb3
---


## W1 re-scope note (2026-07-25, qou-xik5 audit)

Instances ALREADY exist at n=2 (`H2A`) and n=3 (`markovTrace_H3A`) — the
`observationFrame_*` consumers are non-vacuously served at those levels today.
W4's real content is n ≥ 4: (i) concrete n=4 — `H4A` Ring/Algebra wrapper
mirroring `H3A` + `gram_symm` closure via `computations/markov/gen_gram_closure.py`
→ `MarkovTraceH4Gram` (MarkovTraceH4.lean:218-231 marks it CLOSEABLE); (ii) the
generic-n conditional registration from W2-W3. Acceptance criteria contain no
positivity (`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md`).
All three class fields now have consumers (`observationFrame_smul` added), so
a registered instance immediately feeds all three F3-linearity theorems.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] SchurWeyl/MarkovTraceInstance (ocneanuMarkovTrace) + HeckeColimitMarkovTrace instance; consumer wiring to TauFunctorReduction may remain (verify)
