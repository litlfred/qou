---
# qou-nfn4
title: 'GAP: lem:descent has no Lean proof'
status: todo
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:31Z
updated_at: 2026-11-22T09:20:31Z
parent: qou-uwyf
---

lifting-and-descent/descent-lemma.lean defines the predicate descent_surjective and proves composition and a counterexample, but nothing states or proves that the descent homomorphism End(A_n) -> End(A_{n-1}) is surjective. The ref now points at the predicate (PR #8977). State the lemma and prove it, or queue it with sorry + Ref.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.
