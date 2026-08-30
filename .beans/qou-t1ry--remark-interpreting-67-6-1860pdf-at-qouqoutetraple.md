---
# qou-t1ry
title: Remark interpreting 67-6-1860.pdf at qou:QOU.Tetraplectic.su2L_su2R_commute
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:53Z
updated_at: 2026-08-24T18:59:49Z
---

The prior art's conclusion -- that the quaternionic construction naturally yields a left-right symmetric gauge group -- is a concrete consequence of the corpus's own interpretive identification and should be recorded as such, so the identification is falsifiable rather than merely 'interpretive'.

**From the source**
- Abstract and Sec. 1 — Formulating fermions and Higgs mesons over the quaternions reproduces the left-right symmetric SU(2)_L x SU(2)_R x U(1) electroweak theory phenomenologically, gives an algebraic account of the replication of quarks and leptons in flavour doublets, and correlates the breakdown to U(1)_em with the existence of a Fock space for gauge singlets but not for quaternionic states.
  Use here: Supplies the missing attribution for the corpus's quaternionic-electroweak Lean file and, more usefully, tells the corpus what its own construction predicts: a left-right symmetric gauge group, which is a testable consequence of the interpretive identification bring_tetraplectic.md already flags as underived.

Source: `library/67-6-1860/67-6-1860.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/67-6-1860/  ->  [morita1982]
  Quaternionic Weinberg-Salam Theory

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [morita1982] as the citation key when you do it.

## CLOSED 2026-08-24 — the remark exists

`rem:tetraplectic-su2-gauge-reading`
(`content/quantum-observable-universe/brings-surface/`) is that remark. Its
`lean.ref` is `qou:QOU.Tetraplectic.su2L_su2R_commute` — the declaration in this
bean's title — and it cites `[morita1982]`.

It records the consequence the bean asked for, in the terms the bean asked for:
Morita's quaternionic Weinberg-Salam reproduces the **left-right symmetric**
`SU(2)_L x SU(2)_R x U(1)`, and the reason carries over unchanged — both the
left and the right unit-quaternion actions are available and the algebra
distinguishes neither, so the Reeb triad has no way to prefer `g.psi` over
`psi.g`. If the Reeb `SU(2)` is the electroweak `SU(2)`, the framework inherits
a left-right symmetric gauge sector and owes an account of how the right-handed
factor breaks. That is checkable, which is what the bean wanted: the
identification is falsifiable, not only interpretive.

Written as part of incorporating `bring_tetraplectic.md` into `brings-surface`
(bean `qou-wy6d`).
