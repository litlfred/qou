---
# qou-2017
title: 'W2: Ocneanu conditional-expectation tower E_n : H_{n+1} -> H_n in Lean — build on the cyclicity bricks (#4126/#4110)'
status: completed
type: task
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-07-25T13:00:16Z
parent: qou-utb3
parent: qou-utb3
---


## W1 re-scope note (2026-07-25, qou-xik5 audit)

Wenzl positivity is SURPLUS to the `MarkovTrace` fields
(`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md`). Trim W2's
deliverable: build `E_n` + the basic-construction absorption + the spanning
decomposition `H_{n+1} = H_n + H_n σ_n H_n` (what Ocneanu cyclicity induction
actually needs). Thread `HeckeConditionalExpectation` / `JonesBasicConstruction`
(HeckeTowerBasicConstruction.lean:169/:187, both positivity-free) as §3b-cond
hypotheses if needed; do NOT thread `WenzlTowerStep` (:209 — the
nondegeneracy/semisimplicity ascent is a different deliverable, not needed for
the three class fields).
