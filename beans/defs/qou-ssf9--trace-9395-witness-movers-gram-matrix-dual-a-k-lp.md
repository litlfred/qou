---
# qou-ssf9
title: 'Trace #9395 witness movers: gram-matrix-dual, a-K LP dual, unified-low-isotope, atom-level tower'
status: in-progress
type: task
priority: normal
tags:
    - compute-accuracy
created_at: 2026-11-24T21:01:22Z
updated_at: 2026-11-27T14:18:46Z
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

## 2026-11-25 — owner ruling implemented (intervals), PR #9438

Owner ruling card 3 / answer "1 intervals" implemented on branch `claude/ak-lp-dual-intervals-20261125`, draft PR #9438 (commit 0b0f7f8a0).
- `aK_via_lp_dual_full.py`: c=0 rows publish `u_lambda_star: null`, `u_lambda_star_interval: ["0","+inf"]`, `u_identified: false`, `is_active: null`; row `y_star`/`y_star_str` masked + same-length `y_star_interval`. `x_star` null with `[-M, n+M(k-1)]` (M=1e6, now passed explicitly) when k>=2 zero-cost rows. `active_set`, `n_active`, both dual sums over identified rows only, labelled `*_scope`.
- Helium-4 l>=3 cache residues (70 rows, max 2.568e-73) set to exact 0 on `ocneanuWeight_conventionD_eq_zero_of_three_rows` (qou-u2jg); dropped residue published (`l3_residue_max_abs`), guard 1e-40. He-4 now has the same face structure as the other five.
- `lp_dual_witness_validator.py`: `check_unidentified_intervals()` accepts null only with a valid interval (exact comparison). Validator totals unchanged (5/31 WARN, pre-existing).
- Determined fields (y0_star ~0, degeneracy flag, a_K null) unchanged in meaning; no consumer moves.
- Still open (not done here): the He-4 chi-cache producer computing at 50 dps vs 80 (data hygiene), and re-posing the LP on the two-row quotient (this bean).
