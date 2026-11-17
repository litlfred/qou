---
# qou-6nd0
title: 'VALUES review pass: adjudicate the 57 C->D witness value changes, sign flips first'
status: in-progress
type: task
priority: normal
tags:
    - needs-owner
    - reorg-2026-10-04
created_at: 2026-08-09T09:51:39Z
updated_at: 2026-10-04T15:14:19Z
parent: qou-10v9
---


Branch: claude/anchor-followups-2026-08-08. CLAIMED. Follows qou-gjkv (wave5).
Adjudicating the 57 VALUES the wave classified and reverted. Sign flips first.

## FLIP 1 of 3 — delta-lambda-jsj-phase3 — ADJUDICATED: not C->D at all

Regenerated, diffed, reverted (diff saved to scratchpad/flip1.diff). The move is
NOT a convention effect. Three separate things, none of them D:

1. **ANCHOR MIGRATION.** q0 in the witness: 1.1099785955541805 ->
   1.1099785827513808. That is 11.5 ppb, i.e. exactly the recorded
   `q rel diff (proton - muon)/muon = -11.5371 ppb`. This witness predates the
   q0 re-pin. That alone explains the `delta_over_vol_ratios.3He` move of
   0.00013 flagged as the flip.
2. **SnapPy NON-DETERMINISM.** n_tetrahedra changed 20->21, 31->38, 30->29,
   49->47 while the hyperbolic volumes agree to ~1e-8. The triangulation count
   is not stable run-to-run. Worth its own note: this producer is not
   reproducible at the field level even with identical inputs.
3. Witness predates `precisionMetadata` and `environment` being recorded; both
   blocks are added.

VERDICT: reclassify as ANCHOR_MIGRATION + tooling drift, not a convention
change. Do NOT read it as evidence about C vs D.

## LESSON, and it changes how the other 56 must be read

At least some of the 57 VALUES are STALE-WITNESS artifacts (pre-q0-repin,
pre-schema) rather than C->D effects. The wave compares HEAD-of-tree witnesses
against a fresh run, so it cannot separate "the convention changed" from "this
witness was simply old". Every remaining VALUES must be checked for a q0 move
BEFORE being attributed to D. The tell is cheap: diff the `q0` / `q_50dps`
field first.

## Owner directive 2026-08-09 — LANDED (d1938e77)

"use full series even if slightly worse. want all derived bits in there even if
negligible."

Meson EM correction switched from the 2-term truncation `(3q^2-1)/(2q^2)` (==
`1 + hbar_q - hbar_q^2/2`) to the FULL series `1 + log(1+hbar_q)`.
46.80 -> 102.86 ppb on ratio^2. Still MEETS L2 (target 263.6 ppb on the ratio,
full series 51.43, margin 5.13x). qou-v6oz is DISSOLVED: `(3q^2-1)/(2q^2)` is
not the physical object, it is where the series was stopped.

## NEXT, in order

1. FLIP 2: he4-canonical-tr-m-block-fingerprint (334 fields, 1 flip,
   `assertions[pct_block_10_2].computed` moved 0.145).
2. FLIP 3: qbeta-li2q-spectral-combiner-crossanchor (14 fields, 1 flip,
   `cross_anchor_analysis.candidate_swing_abs` moved 4.06e+03).
3. The other 54, q0-field first per the lesson above.
4. **WIRE THE WRITHE TERM** — the second half of the owner directive. Bean
   qou-c6gx recorded it as "REAL but negligible ... should still be wired in for
   rigour": the normalisation `S_hat = S*(1-h)^((e-n)/2)`, Lean-proved SORRY-FREE
   in `QOU/QBeta/WritheNormalisation.lean` (`writhe_factor_sq`,
   `writhe_factor_unique_up_to_sign` — base AND exponent derived). VERIFIED
   2026-08-09 that it is NOT wired into the binding path (no reference in
   mass_binding_dashboard.py or chi_monotone_transfer.py). Effect ~3.2e-4 MeV.
   Negligible is exactly the case the directive covers.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR litlfred/qou#8222)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8222 (`95ddc04a72f67a43b1ccf1d77e08572625847a9b`, scriptCommitSha `4ed1888aba96f0c3e837a57c93b666bdd892604e`)
- **Summary**: Added `calugareanu_self_linking_sub_twist_eq_writhe`, `calugareanu_twist_zero_iff_eq_writhe`, and `calugareanu_writhe_sign_flip_diff` in `QOU/Topological/RibbonWritheHolonomy.lean`, verified by 80-dps mpmath probe `keystone_writhe_ramified_stokes_ladder_probe.py` (`scriptHash: 75539ba8f436`).
