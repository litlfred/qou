---
# qou-ssf9
title: 'Trace #9395 witness movers: gram-matrix-dual, a-K LP dual, unified-low-isotope, atom-level tower'
status: in-progress
type: task
priority: normal
created_at: 2026-11-24T21:01:22Z
updated_at: 2026-11-25T11:06:49Z
parent: qou-s028
---

## 2026-11-24 trace (agent, session 01Eucf)
Full trace posted on #9395: https://github.com/litlfred/qou/pull/9395#issuecomment-7144386562. Summary: (a) gram-matrix-dual: G byte-identical; np.linalg.eigvals unsorted; spectrum {4.2303,0.7527x3,~0,-0.7527} both before and after, so it was never PSD. Separate finding: the bilinear tr_M(b_i b_j) form has signature (3,1) on the (2,1) block, which contradicts the 'positive definite' wording in categorical-mass-markov-proof §1 (owner decision). (b) a-K u* x1e-4 only on y_lambda=0 rows (dual not identified, qou-fu8c); likely trigger is the Clarabel fork bump 0b5b85fbaf6. (c) unified-low-isotope and (d) atom-level-tower: word ruling 7db032fb482 (qou-hu1f, beta_Bor interleaved), plus the Plancherel self-normalisation fe861ef2e87 for (c). (d) reproduces bit-for-bit with intra_order=grouped. New values are correct per the corpus.

## 2026-11-24 owner rulings (cards, relayed by coordinator)
1 'A: switch' -> eigvalsh done (PR https://github.com/litlfred/qou/pull/9401, 50f8ecc64d7). 2 'A: Hermitian form' -> NOT applied: section 1 of categorical-mass-markov-proof defines the Frobenius object via the bilinear pairing, so the ruling's stop condition fired. Reported on https://github.com/litlfred/qou/pull/9401 with options; recommendation is 'non-degenerate' plus a positivity sentence for the Hermitian form. 3 'A: revert' -> done (qou-mi15). 4 #9395 merged by the coordinator. All four rows are in docs/coordination/owner-rulings.md.

## 2026-11-25
PR #9401 merged (by the coordinator) with commits 82643b15227..31756fa8fe0. Ruling 2 (Hermitian rewording) is still unapplied by design (stop condition); it awaits the owner's choice between A (non-degenerate + Hermitian positivity sentence) and B.

## 2026-11-25 §1 applied (https://github.com/litlfred/qou/pull/9404, 0f6c2441a62)
Owner 'A: non-degenerate': the word is replaced and the positivity sentence for the sesquilinear form is added.

## 2026-11-25 exact dual face (PR https://github.com/litlfred/qou/pull/9420)
Pre-registered (076ab8fb4ff), then solved the a-K LP in exact rationals and min/maxed each coordinate over the optimal face. Rows with c=y*chi=0 (= y=0, all l>=3): u in [0,+inf), NOT identified; c!=0 rows u=1 exactly; y0=0, w=0, opt=0. Holds on p,n,d,t,3He; so the x1e-4 move is a solver picking another point. Also unidentified: active_set/n_active, chirality_dual_sum (5 atoms), self_conjugate_dual_sum (d,t,3He), x_star on zero rows when >=2. Exception 4He: chi cache has 1e-73..1e-149 residue not exact 0, so exact LP identifies all (y0=1.45e-149, u=1-y0/|c|) and published 4He u=6.3288 lies outside; exact-zero arm restores the structure. Why 4He did not move in the refresh is not explained. Owner decision framed in RESULTS.md (1 intervals [rec] / 2 canonical min-norm u=0 / 3 re-pose on support / 4 no-op default). Producer unchanged.
