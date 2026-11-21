---
# qou-3ja5
title: Cite 0411505v2.pdf at conj:kashaev-density-equals-sdp-multiplicity
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:47Z
updated_at: 2026-11-21T13:32:29Z
pr: 8315
parent: qou-ysb7
---

Driver (x) is named 'MacMahon-style partition algebra' three times in this block with no source; Thm 2 is the source.

**From the source**
- Thm 2 (with Defn 1.4) — For every knot diagram K, J_n(K,q) = q^{delta(K,n)} / Ferm(B'_K) n-evaluated, where Ferm(A) = sum over subsets J of (-1)^{|J|} det_q(A_J) is the alternating sum of quantum minors and B'_K is the arc-graph matrix.
  Use here: Supplies the literature link the corpus's driver (x) asserts but does not source: the MacMahon/boson-fermion mechanism is what produces the colored Jones, so a MacMahon-style partition count is not an arbitrary menu entry. Cite it where driver (x) is introduced.

Source: `library/arxiv-math-0411505v2/0411505v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0411505v2/  ->  [garoufalidis-loebl2005]
  A non-commutative formula for the colored Jones function

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis-loebl2005] as the citation key when you do it.

### Progress (Round 60)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8315 (`bfd875bed8570b98aa208b007cb51288416e1d03`). Status kept `in-progress` pending PR merge.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8315, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

conj:kashaev-density-equals-sdp-multiplicity now cites garoufalidis-loebl2005 Def. 1.4 + Thm 2, with the scope boundary: that theorem is a q-MacMahon formula for J_n, not a statement about Wedderburn multiplicities of H_n(q), so the block's partition-algebra identification is not supplied by it.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
