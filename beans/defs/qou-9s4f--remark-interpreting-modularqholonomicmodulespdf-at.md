---
# qou-9s4f
title: Remark interpreting modular.qholonomic.modules.pdf at rem:phi-q-aj-machinery-identification-details
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:00Z
updated_at: 2026-11-21T13:32:29Z
parent: qou-vva9
---

The improved analyticity across |q| = 1 is directly about the boundary between the corpus's fibre-level formal q and its archimedean real q_0, a distinction AGENTS.md flags as a recurring source of confusion; a remark connecting modularity to that boundary would be more useful than a bare citation.

**From the source**
- Def. 1.1 with Thm 1.2 (the slash operator), and Thm 1.4 — A q-difference equation is modular when the monodromy relation holds for all of SL(2,Z); it suffices to check the generators S and T, and the generalised q-hypergeometric equation is modular and self-dual with the two natural cocycles equal.
  Use here: A checkable criterion (two generators) for the modularity of the q-difference equations the corpus works with, and with it the effective solution method the Stokes-matrix work currently lacks.

Source: `library/modularqholonomicmodules/modular.qholonomic.modules.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/modularqholonomicmodules/  ->  [garoufalidis-wheeler-modular]
  Modular q-holonomic modules

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis-wheeler-modular] as the citation key when you do it.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

rem:phi-q-aj-machinery-identification-details: paragraph citing garoufalidis-wheeler-modular Def. 1.1 + comment 1, Thm 1.2(a), Thm 1.4, §1.5 Thms 1.5-1.7; records that modularity of A-hat_K is the source's conjecture (comment 5), not a theorem.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
