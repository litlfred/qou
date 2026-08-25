---
# qou-d5e8
title: '2H ATTACK C: check whether B = -alpha*ln(mu) is the right functional at all - qou-kj4v says the degeneracy argues no flavour-only mu can be'
status: todo
type: task
priority: normal
created_at: 2026-08-25T18:37:51Z
updated_at: 2026-08-25T18:45:53Z
parent: qou-9ot5
---

## RESOLVED 2026-08-25 — converges on the braid word. See docs/audits/2026-08-25-deuteron-attack-c-convergence.md

Three independent lines (my Hecke-element negative, qou-kj4v's exact flavour-only
degeneracy, and the 2026-08-09 chain-walk audit's alpha-is-pinned-elsewhere argument)
all eliminate the interface scalar and alpha and land on the BRAID WORD.

Also found: B = -alpha*ln|tr_M| is POSITED. Five-path corpus-grep finds no derivation
and NOTHING in Lean; the only statement of it in content/ is a row in a NOTATION TABLE.
And the dashboard's cited definition, 'Defn: standard-part-functor.md', is DEAD - that
block defines the standard-part map and functor and contains no B_sym, no alpha and no
binding at all. Same defect class as prop:hecke-spectral-sequence.

Measured: the 2H word is 23 crossings over 6 strands, of which exactly ONE carries the
interface offset (index 2, d = -0.4997h). The other 22 cancel in the free/atom ratio.
The entire deuteron binding rides on a single sigma-type crossing.
