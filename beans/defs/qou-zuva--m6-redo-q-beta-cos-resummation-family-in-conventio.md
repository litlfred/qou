---
# qou-zuva
title: 'M6: redo q-beta-cos-resummation family in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:08Z
updated_at: 2026-11-16T17:56:00Z
parent: qou-wxhi
---

nuclear-interactions/q-beta-cos-resummation.md:8,12 and table data use z_C; residual +305.7 ppm is C-measured (6 users). Overlaps qou-cds1. Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: redone in D on PR #7562 (subagent, reviewed). Ruled base 0.4447004085 MeV (-431571.8 ppm); cos factor 0.99918 makes it worse (-432037.5 ppm), forced since cos<=1 and F_required>1. Form A historical: +1677.6 -> +856.8 ppm with D phase (was 5.49x under C, now 1.96x). Bar-evenness argument for the cosine fails under D (z_D(1/q) != z_D(q)), so cosine is now a tested definition, not derived. OPEN: Lean sibling still markovZC (eigenphase_bar_involution false under D); downstream eps_DeltaS 1015->185 ppm still C; no D producer/witness (computation field points at old producer). Stays open.

2026-10-10 (branch claude/q-beta-cos-resummation-d-2026-10-10, commits 39879de5d 1787c85d6 a331b5aa0): leftovers (1)-(3) done. (1) Lean sibling restated in D: eigenphase uses markovZD = q^3/(q^2+1); class + q_beta_cos_resummation now on alpha_D. C kept, labelled C-historical (markovZC, eigenphaseC, eigenphaseC_bar_involution; deprecated alias eigenphase_bar_involution kept because 4 library docstrings + 3 probes + 1 witness cite it). New sorry-free D theorems: markovZD_bar_ne (z_D(1/q) != z_D(q), q>0, q!=1), eigenphase_bar_even_sum (alpha_D(1/q)+alpha_D(q) = (q^2-1)^2/(2q^2)), eigenphase_not_bar_odd. lean-direct -DautoImplicit=false exit 0, axioms propext/Classical.choice/Quot.sound. (2) eps_DeltaS recomputed under D (mpmath, proton pin, Q_ref 0.78233341): Form A 1014.8 -> 518.2 ppm; ruled z_D base -261056.6 -> -261338.4 ppm. C figure reproduces as 1014.8 -> 185.1 (labelled historical). Only site quoting 1015->185 is the block's .ts authorNote; now scoped C-measured with D beside it. docs/coordination/1ppb.md carries the C 305 ppm as a dated ledger record, left alone. (3) New producer computations/qbeta/qbeta_cos_resummation_d_probe.py + qbeta-cos-resummation-d.witness.json (5/5, Q0_OK), reproduces every block number (4.7e-11 values, 0.047 ppm residuals); computation field repointed. Side note: |z_D(q) - z_D(1/q)| = h exactly. Still OPEN (why bean stays open): the cosine is an untested definition under D (no derivation), the transfer-matrix eigenphase identification is circular/unproved (qou-pdix/qou-cds1), and no admissible factor > 1 exists on the ruled base.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.



2026-11-15: moved under epic `qou-wxhi` (c_k ladder under convention D). Previous parent kept in history.


## Round 46 Update (2026-11-16 — PR `litlfred/qou#8142`)

- **Status**: `in-progress` (verified on `origin/main` and extended in Round 46; kept `in-progress` per strict non-closure rule).
- **Verification & Extension**:
  - Verified that the `2026-10-10` Convention-D cosine resummation deliverables (`folio/quantum-observable-universe/nuclear-interactions/q-beta-cos-resummation.{lean,md,ts}` and `computations/qbeta/qbeta_cos_resummation_d_probe.py` + `computations/qbeta/qbeta-cos-resummation-d.witness.json`) are present on `origin/main` and pass all 5 assertions (`reproduces_block_published_values`, `reproduces_block_published_ppm`, `ruled_base_cos_moves_residual_away_from_zero`, `alpha_D_bar_even_part_matches_closed_form`, `eps_DeltaS_chain_identity`).
  - Extended `folio/quantum-observable-universe/nuclear-interactions/q-beta-cos-resummation.lean` with `eigenphase_bar_sum_eq_half_heckeH_sq`, `wedderburnMiddleWeightD_pos`, `ladderPhaseCoeff_zD_eq`, `ladderPhaseCoeff_neg_at_zD`, `ladderPhaseCoeff_ne_wedderburnMiddleWeight`, `eigenphase_eq_affine_ladderPhaseCoeff`, `eigenphase_mirror_covariant_projection`, `eigenphase_mirror_covariant_projection_sub_harmonic`, and `eigenphase_mirror_covariant_projection_bar_odd` (`0` `sorry`, `#print axioms` clean).
- **PR**: `https://github.com/litlfred/qou/pull/8142` (`7ba86df415ad231cf6e834adee99dcb383115c6d`).
