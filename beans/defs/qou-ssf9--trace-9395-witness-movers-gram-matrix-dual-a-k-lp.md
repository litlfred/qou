---
# qou-ssf9
title: 'Trace #9395 witness movers: gram-matrix-dual, a-K LP dual, unified-low-isotope, atom-level tower'
status: in-progress
type: task
priority: normal
created_at: 2026-11-24T21:01:22Z
updated_at: 2026-11-24T21:16:58Z
parent: qou-s028
---

## 2026-11-24 trace (agent, session 01Eucf)
Full trace posted on #9395: https://github.com/litlfred/qou/pull/9395#issuecomment-7144386562. Summary: (a) gram-matrix-dual: G byte-identical; np.linalg.eigvals unsorted; spectrum {4.2303,0.7527x3,~0,-0.7527} both before and after, so it was never PSD. Separate finding: the bilinear tr_M(b_i b_j) form has signature (3,1) on the (2,1) block, which contradicts the 'positive definite' wording in categorical-mass-markov-proof §1 (owner decision). (b) a-K u* x1e-4 only on y_lambda=0 rows (dual not identified, qou-fu8c); likely trigger is the Clarabel fork bump 0b5b85fbaf6. (c) unified-low-isotope and (d) atom-level-tower: word ruling 7db032fb482 (qou-hu1f, beta_Bor interleaved), plus the Plancherel self-normalisation fe861ef2e87 for (c). (d) reproduces bit-for-bit with intra_order=grouped. New values are correct per the corpus.

## 2026-11-24 owner rulings (cards, relayed by coordinator)
1 'A: switch' -> eigvalsh done (PR https://github.com/litlfred/qou/pull/9401, 50f8ecc64d7). 2 'A: Hermitian form' -> NOT applied: section 1 of categorical-mass-markov-proof defines the Frobenius object via the bilinear pairing, so the ruling's stop condition fired. Reported on https://github.com/litlfred/qou/pull/9401 with options; recommendation is 'non-degenerate' plus a positivity sentence for the Hermitian form. 3 'A: revert' -> done (qou-mi15). 4 #9395 merged by the coordinator. All four rows are in docs/coordination/owner-rulings.md.
