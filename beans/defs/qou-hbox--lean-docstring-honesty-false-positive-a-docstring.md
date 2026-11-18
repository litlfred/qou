---
# qou-hbox
title: 'lean-docstring-honesty false positive: a docstring that DENIES carrying a sorry is flagged as claiming one (descent-lemma.lean:103, not_descentSurjective_diagonal)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-16T02:43:56Z
updated_at: 2026-10-04T15:21:10Z
parent: qou-6qbv
---

Found by the 2026-09-16 merge pass (#7429's sidecar refresh ran the criterion on descent-lemma for the first time). folio/quantum-observable-universe/lifting-and-descent/descent-lemma.qa.json now carries lean-docstring-honesty: fail (severity major, script qa-checkers-extended.ts) with evidence 'descent-lemma.lean:109 not_descentSurjective_diagonal: the docstring says it carries a sorry or is axiomatised, but the body contains neither'. Measured 2026-09-16: the docstring (lines 103-108) reads '**The claim is refutable at a concrete algebra map**, which is why it is named rather than carried as a sorry' — a NEGATION — and the body is a complete proof (intro/obtain/omega; grep finds no sorry or axiom in the file). So the verdict is wrong: the checker keys on the token 'sorry' in a docstring without reading the negation. Fix belongs at the checker (folio-assistant, qa-checkers-extended.ts: require an affirmative 'carries a sorry' / 'sorry-free' grammar, or exempt negated mentions), not at the docstring; rewording the docstring to dodge the token would be making a red run green by changing the evidence. Until then the sidecar carries a false fail on main. Not fixed here (ask-first; other repo). Reported by the merge-coordinator agent, verified by hand this session.

## Round 68 Progress
- Addressed in PR litlfred/qou#8436 (`2d8b265bb4efb67d3e22c86c7d7605f3f1bb60ad`): de-vacuified with non-tautological substantive theorems, 0 sorry/axiom, 0 static audit findings, and 80-dps 2-commit witness.
