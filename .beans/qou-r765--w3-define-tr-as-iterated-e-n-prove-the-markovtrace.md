---
# qou-r765
title: 'W3: define tr as iterated E_n; prove the MarkovTrace fields (cyclic + Markov normalization) from the tower'
status: in-progress
type: task
priority: normal
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-08-26T13:33:20Z
parent: qou-utb3
---


## W1 re-scope note (2026-07-25, qou-xik5 audit)

Title correction: the class does NOT carry "Markov normalization" — (M3) is
documented-not-enforced (MarkovTraceOnHecke.lean:70-71) and `tr(1)=1` is not a
field. W3's actual target: prove the THREE class fields (`cyclic`, `map_add`,
`map_smul`) for `tr = tr_1 ∘ E_1 ∘ ⋯ ∘ E_{n-1}`. The tower/stabilization
property feeds the separate `MarkovStabilization` class
(`observationFrame_stabilizes` consumer) — may be delivered alongside, but the
`MarkovTrace` instance does not block on it. No positivity anywhere
(`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md`).
