---
# qou-qbk1
title: 'S0: level-d q-Borel kernel in Lean — generalize QBorelKernel from d=1, prove the closed-form degree law'
status: todo
type: task
priority: normal
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-08-08T08:05:00Z
---

Generalize `QOU/MathlibExt/QBorelKernel.lean` (currently level `d = 1`,
`t_n = q^C(n,2)`) to general level `d`, per RSZ §3.3: `t_n = q^{n-d} * t_{n-d}`,
growth `q^{n^2/2d}`.

**Deliverable (sorry-free, `#print axioms` clean):**
- `qBorelKernelLevel d q n`
- the recurrence lemma `t_n = q^{n-d} * t_{n-d}`
- the **closed-form degree law**. For `d = 2` the even/odd chains give
  `deg t_{2m} = m(m-1)`, i.e. `~ n^2/4`. General `d`: the sum over the chain.

**Why cheap and why first.** Pure algebra, no analysis. It is the Lean statement
of the growth table in the plan doc, and it is the same shape as the already-proved
`cCoeff_natDegree` (`QOU/QBeta/C1InfDegreeLaw.lean`) -- reuse that pattern:
degrees add over a domain, no-cancellation on the top term.

**Falsifiable:** the closed form either satisfies the recurrence or it does not.

Plan: `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md` (stage S0).
