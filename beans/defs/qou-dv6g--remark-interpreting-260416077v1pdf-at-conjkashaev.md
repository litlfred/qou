---
# qou-dv6g
title: Remark interpreting 2604.16077v1.pdf at conj:kashaev-volume-conjecture
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:09Z
updated_at: 2026-10-04T15:23:41Z
parent: qou-vva9
---

Record the epistemic status honestly: a rigid semi-classical volume limit is proved for the figure-eight complement, for the quantum hyperbolic invariants and subject to a parity condition. What would need checking before it could touch the Lean class: whether the invariants here and the Kashaev invariant the class axiomatises are the same object at the relevant limit, and whether the parity condition holds at the corpus's chosen longitude/logarithm branch. Until both are settled this is a scope statement, never a discharge of the conjecture.

**From the source**
- Abstract; Theorem 1.1 and its triangulation version (section 1.2) — The real part of the semi-classical limit of the quantum hyperbolic invariants of the figure-eight knot complement is rigid (independent of the holonomy representation chosen) and equals 0 or Vol/(2*pi) according to a parity condition on the logarithms of the holonomy eigenvalues on the canonical longitude.
  Use here: The nearest published theorem to the corpus's axiomatised volume conjecture, on the exact manifold the CAL-2 anchor uses; it also supplies a rigidity statement (no dependence on the holonomy choice) that the corpus's anchor implicitly assumes.

Source: `library/arxiv-2604.16077v1/2604.16077v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2604.16077v1/  ->  [baseilhac2026]
  VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [baseilhac2026] as the citation key when you do it.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

conj:kashaev-volume-conjecture: paragraph citing baseilhac2026 §1.1 Thm 1.1 and App. A. Correction: the source normalises the limit as (2pi/N)Log|H_N| -> Vol(M) (case a), not Vol/2pi. Its QHI of the cusped manifold are not the Kashaev invariant (which is the QHI of the pair (S^3,L)); recorded as a neighbouring statement, not an instance of the class.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.
