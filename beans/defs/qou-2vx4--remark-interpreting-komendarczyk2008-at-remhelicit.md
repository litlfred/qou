---
# qou-2vx4
title: Remark interpreting [komendarczyk2008] at rem:helicity-physical
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:28Z
updated_at: 2026-11-21T13:32:29Z
parent: qou-vva9
---

The registry CSL note is carrying multi-paragraph mathematical findings from two full reads - including corrections to prior corpus readings of the Freedman-He bound - that belong in a citable remark, not in a bibliography note field. Promote the findings to a remark and cite the key there, which also retires the bib orphan.

**From the source**
- Abstract; Sec. 6 (incl. eq. (43)); Rem. 2.6; Cor. 2.5 — Third-order helicity of a volume-preserving field on invariant unlinked domains, realised as an average asymptotic mu-bar-123 of orbits, with an L^2-energy lower bound whose constant is geometric.
  Use here: The Borromean third-order invariant is the natural many-body object for the Borromean-link blocks; the registry note already extracted the two negatives (total antisymmetry of mu-bar-123, and Flux^3 rather than Flux^2 scaling) that constrain a Coulomb-like pair-energy ansatz.

Source: `library/arxiv-0808.1533v3/0808.1533v3.pdf` (`komendarczyk2008`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

rem:helicity-physical now cites komendarczyk2008 (v3 locators: Rem. 2.3 antisymmetry, §6 eqs. (6.1)/(6.6) flux formula, §7 Thm 7.1 eqs. (7.6)-(7.7), eq. (7.8) Freedman-He). Note: the registry note's locators (Thm 6.1, eq. (43), Rem. 2.6) follow v1; the registered PDF is v3.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
