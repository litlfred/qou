---
# qou-bore
title: Remark interpreting 0306165v1.pdf at conj:kashaev-volume-conjecture
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:27Z
updated_at: 2026-11-21T13:32:29Z
parent: qou-vva9
---

The generalised (one-parameter) volume conjecture strictly contains the Kashaev statement the corpus adopts; a remark recording that containment would place the corpus's 4_1 anchor in its published family.

**From the source**
- sec. 3.1 + sec. 5.2, eq. (5.12) — The classical A-polynomial's zero locus is the Lagrangian of the SL(2,C) Chern-Simons phase space, and its quantisation governs a one-parameter family of colored-Jones asymptotics (Vol(l,m) + i 2 pi^2 CS(l,m)) that contains the volume conjecture at m = 1.
  Use here: Supplies the Chern-Simons saddle-point reading of the AJ operator that prop:phi-q-aj-machinery-identification asserts but sources only on the algebraic side.

Source: `library/arxiv-hep-th-0306165v1/0306165v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-th-0306165v1/  ->  [arxiv-hep-th-0306165v1]
  Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-hep-th-0306165v1] as the citation key when you do it.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

conj:kashaev-volume-conjecture: paragraph citing arxiv-hep-th-0306165v1 §5.2 eqs. (5.12)-(5.13) and §5.3, placing the 4_1 case as the m = 1 member.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
