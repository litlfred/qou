---
# qou-0ddm
title: Add reference for 2312.00624v1.pdf at conj:stokes-dt-bps-bridge
status: completed
type: task
priority: normal
created_at: 2026-08-09T00:10:49Z
updated_at: 2026-08-21T17:03:12Z
---

Orphan; same knots and same state integral as the corpus's A_omega / c_3 chain, and needed as the source for the calibration remark below.

**From the source**
- Sec 6 Conclusions, first open question (its ref [42] = `dimofte-gaiotto-gukov2013`) — The interpretation of the integrality structure of the resummed WKB wave function 'in terms of an enumerative problem, or a BPS counting problem, in the dual supersymmetric theory' is listed as an open question raised by the work, citing the same 3d-3d dictionary the corpus's bridge invokes.
  Use here: Calibration for conj:stokes-dt-bps-bridge, which adopts Stokes = DT = dim H_BPS(T[K]) and describes the first equality as 'proved ... for the figure-eight 4_1'. This document shares an author with `garoufalidis-gu-marino2023peacock` and, on the same knots, treats the BPS-counting reading of its integer invariants as open. IMPORTANT CAVEAT to carry with any use: those integers are the holomorphic-block integrality invariants of a convergent q-series, NOT the resurgent Stokes constants, so this is adjacent evidence about authorial stance and not a statement about Conjecture 3(d) itself. Scope-(a).
- Sec 1 eq (1.1) with Sec 3.2 — The resummed WKB q-series wave function has apparent singularities at every ll in 2 pi Q (i.e. at roots of unity q = exp(i ll)), absent from the non-perturbative definition; a conjectured integrality of the holomorphic blocks makes them cancel against the anti-holomorphic blocks, leaving a finite wave function, with the epsilon-expansion mechanics in Appendix A.
  Use here: A stated cancellation mechanism at rational points, worked explicitly for the figure-eight in Sec 4.1 and Sec 5. Recorded against conj:stokes-dt-bps-bridge only as context for the same 4_1 wave function; there is no block that consumes it, which is why the verdict stays supporting.

Source: `library/arxiv-2312.00624v1/2312.00624v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-2312.00624v1/  ->  [mario2023]
  On the structure of wave functions in complex Chern–Simons theory

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
