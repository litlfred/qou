---
# qou-owbd
title: Cite 0905.1873v2.pdf at folio/quantum-observable-universe/lean/QOU/MassTheory/TjonSimplexForm.lean
status: in-progress
pr: 8386
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:59Z
updated_at: 2026-10-04T15:17:07Z
parent: qou-19m0
---

Replace the bare 'arXiv:0905.1873' in the TjonSimplexForm docstring with the registered key so the Lean -- Ref: convention holds and validate-bib can see the dependency.

**From the source**
- p.3, col.2 (discussion of Fig. 3/4, lambda-dependence) — SRG-induced short-range four-body forces contribute about 50 keV net to the 4He ground-state energy at lambda = 2 fm^-1; the long-ranged N3LO four-nucleon contribution to 4He binding is estimated at a few hundred keV.
  Use here: The external numeric ceiling on genuine four-body physics in A = 4 that mu4_target_exceeds_n3lo_bound certifies the corpus target exceeds. It is what turns 'mu_4 = -4.591 is large' into a falsifiable scope-(a) statement about the C(A,k) basis rather than about the operator.
- Fig. 5 and surrounding text, p.4 — Plotting B(4He) against B(3H), the SRG NN-only results trace out the Tjon line; including the evolved NNN force collapses the trajectory to a short segment through the experimental point.
  Use here: The concrete data the reformulated GAP-9 test needs: the B(3H)-B(4He) plane with the field's own trajectory in it, against which the QOU block-trace operator can be tested convention-free. Gives the Lean file TjonSimplexForm its empirical referent.
- Abstract + conclusions, p.4 — The net induced four-body contribution in A = 4 is smaller than the truncation errors of the chiral interaction, but four-nucleon forces are strongly density dependent so their size must be monitored for heavier nuclei.
  Use here: Scopes the bound honestly: the small-4N-force statement is an A = 4 statement, not an all-A statement. Any QOU use of it as a ceiling for heavier isotopes in the mass-table sweep must carry that caveat, or it over-claims.

Source: `library/arxiv-0905.1873v2/0905.1873v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0905.1873v2/  ->  [jurgenson2009srg]
  Evolution of nuclear many-body forces with the similarity renormalization group

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [jurgenson2009srg] as the citation key when you do it.

## Progress (2026-11-18, PR #8386)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`dc2e35b36f4ebb7e9b1575a73bdbe33cb67ee130`, `scriptHash: 2ebaf0631eb0504b9d6d5bd79a3a8425d49d4ffed0fadf6b52c241edb18846dc`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8386`
