---
# qou-hbox
title: 'lean-docstring-honesty false positive: a docstring that DENIES carrying a sorry is flagged as claiming one (descent-lemma.lean:103, not_descentSurjective_diagonal)'
status: todo
type: task
created_at: 2026-09-16T02:43:56Z
updated_at: 2026-09-16T02:43:56Z
---

Found by the 2026-09-16 merge pass (#7429's sidecar refresh ran the criterion on descent-lemma for the first time). content/quantum-observable-universe/lifting-and-descent/descent-lemma.qa.json now carries lean-docstring-honesty: fail (severity major, script qa-checkers-extended.ts) with evidence 'descent-lemma.lean:109 not_descentSurjective_diagonal: the docstring says it carries a sorry or is axiomatised, but the body contains neither'. Measured 2026-09-16: the docstring (lines 103-108) reads '**The claim is refutable at a concrete algebra map**, which is why it is named rather than carried as a sorry' — a NEGATION — and the body is a complete proof (intro/obtain/omega; grep finds no sorry or axiom in the file). So the verdict is wrong: the checker keys on the token 'sorry' in a docstring without reading the negation. Fix belongs at the checker (folio-assistant, qa-checkers-extended.ts: require an affirmative 'carries a sorry' / 'sorry-free' grammar, or exempt negated mentions), not at the docstring; rewording the docstring to dodge the token would be making a red run green by changing the evidence. Until then the sidecar carries a false fail on main. Not fixed here (ask-first; other repo). Reported by the merge-coordinator agent, verified by hand this session.
