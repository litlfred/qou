---
# qou-g6vb
title: 'F4 research: prove trM_cyclic on H4 via bilinearity ⇒ 24² basis identities'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T01:52:06Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-59vq
---


## Finding (2026-07-19)
The bilinearity reduction (isolate 24 per-word functionals trM(W_j u), then
Gram symmetry A_{j,i}=A_{i,j}) is mathematically correct but does NOT rescue
the Lean proof: a SINGLE depth-6 word already whnf-explodes. 6 tactic
strategies infeasible (brute simp; per-word simp; per-word rfl; incremental
have-chain rfl; incremental fin_cases; 200k–4M heartbeats). Root cause:
top-down Matrix.cons indexing re-derives inner-word entries per outer index
(exponential, non-memoized). Single-layer rfl works (opaque u); depth-2+ fails.
Tractable path: Matrix.Reflection re-encode (needs Matrix.Notation olean,
absent from sandbox cache) OR abstract regular-rep trace tr(AB)=tr(BA).
Audit: docs/audits/2026-07-19-h4-cyclicity-whnf-explosion.md. Sorry kept honest.

## Both approaches assessed (2026-07-19)
Owner asked to try BOTH (reflection re-encode + abstract trace). Result:
neither closes trM_cyclic in-sandbox, but the assessment is now definitive.
- Approach 1 (Matrix.Reflection): BLOCKED — Matrix.Notation olean absent +
  source 404s at pinned rev (reorganized); needs full lake build (wipe risk).
  Also dubious: reflection is for small matrices, not 24x24 depth-6 (~83k ops).
- Approach 2 (abstract regular-rep trace): the regular trace is cyclic for free
  (Matrix.trace_mul_comm) but trM4 is NOT the regular trace (Ocneanu weights
  differ). Connecting the Markov functional to a cyclic-by-construction trace
  still needs Fin-24 compute [blocked] OR Ocneanu word-length induction = the
  general-n MarkovStabilization class on main, which stays OPEN. The abstract
  route IS the open item, not a shortcut.
Key contrast: mulNF_assoc closed at Fin 6 via funext+fin_cases+ring, proving the
wall is Fin-24 depth-6 grinding (assoc would explode too), NOT cyclicity-specific.
Convergence: confirms main's abstract-algebra/MarkovStabilization direction is
the only path; brute Fin-24 compute is a dead end. This module's n=4 mulNF is
complementary to main's H4 rung (mulσ/trace only), not a duplicate.
Next actionable: upstream abstract cyclic-trace lemma (discharges all n at once).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-19 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 73 (`lane-e667`): Formalized `qou-0fmb`, `qou-4lft`, `qou-avt2`, `qou-cf3m`, `qou-g6vb` in `QOU.Foundations.TowerCompatibilityRootOfUnitySeminormalNormalizationRadicalKernelBilinearSymmetry` with 80-dps `mpmath` 2-commit witness stamp (`98224baac4097812a7a075b15a3d78cd7d6d0f26` -> `57db1e21b3add3a8efd73f5cd0f4cff40a2a1827`, `scriptHash=28e0042d776cdc079c85f0254ab21558d7f5b492e88420dbd3fa8ba157431743`) in PR `litlfred/qou#8394` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8394, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
