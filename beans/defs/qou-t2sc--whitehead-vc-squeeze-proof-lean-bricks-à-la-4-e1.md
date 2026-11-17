---
# qou-t2sc
title: Whitehead VC squeeze proof — Lean bricks (à la 4₁ E1-E5 / Borromean B1-B5), gated on the positive-sum form
status: in-progress
type: task
priority: normal
tags:
    - close-candidate
    - reorg-2026-10-04
created_at: 2026-08-01T19:45:02Z
updated_at: 2026-10-04T15:14:24Z
parent: qou-n4nr
---


## Lean squeeze-proof plan (2026-08-01) — ingredients now in hand

The Whitehead VC as a LIMIT is NOT yet Lean-proved (only the geometric
identity Vol(L5a1)=4G is, via QOU.Archimedean.WhiteheadVolume). Ingredients
for the squeeze proof are now assembled:

- **Published proof**: van der Veen, arXiv:math/0611181 (uploads/0611181v2.pdf)
  proves the VC for the Whitehead link W_[0,1,1,0].
- **Positive-sum form (validated)**: computations/whitehead_van_der_veen.py —
  J_N = φ_N Σ_n (2n+1) χ_{N,n}^{-1} (Σ_{k=0}^{N-1-n} S_{n,k}), with
  S_{n,k}=∏ 2 sin²((k+j)π/N)/sin(jπ/N) > 0. Agrees with the [Kas95] §3 state
  sum EXACTLY at N=3..11; Richardson volume 3.66521 vs 4G (0.037%).
- **Reusable landed bricks**: FigureEightVolumeSqueeze (E1-E5d) and the
  Borromean B1-B5 proofs use the SAME machinery — positive Riemann sums of
  log(2 sin) squeezed against the Clausen primitive. The Whitehead integrand
  is log S_{n,k} = Σ_j [log(2) + 2 log sin((k+j)π/N) - log sin(jπ/N)] — the
  same log(2 sin) integrand, so E1 (log-sum≈max) + the Clausen value bricks
  transfer; new bricks: the S_{n,k} max-term saddle location (x=k/N extremum)
  and the (2n+1)χ weighting.

Target: a WhiteheadVolumeConjecture class (or sorry-free limit theorem)
mirroring VolumeConjecture41. Multi-session; needs live Lean/LSP. Not started.

Status: TODO (ready to start — gate qou-x76e is CLOSED).

## Progress (2026-08-01) — first bricks landed sorry-free

QOU/Knot/WhiteheadVolumeConjecture.lean (registered in QOU.lean; verified via
lean-direct, exit 0):
- catalanG, whiteheadS (van der Veen kernel) — defs
- whiteheadS_factor_pos, whiteheadS_pos, whiteheadInnerSum_pos — SORRY-FREE
  (the positive-sum bricks; analogue of FigureEightVolume.kashaevProd_pos)
- whitehead_volume_conjecture — state-and-queued (sorry + Ref [vanderveen2008])

Remaining (mirror 4₁ E1-E5d / Borromean B1-B5): reduce log whiteheadInnerSum to
the landed Clausen/log(2 sin) Riemann-sum machinery + a whiteheadS max-term
saddle-location lemma. Still in-progress.

## Update 2 (2026-08-01) — squeeze reduction fully machine-verified (#4532)

Ten sorry-free bricks now (lean-direct verified, Mathlib-only). The entire
squeeze REDUCTION is proved; the only remaining sorry is the unconditional
VC target:
- whiteheadS_factor_pos / _pos / whiteheadInnerSum_pos — kernel positivity
- whiteheadS_log — log(2 sin) Riemann-sum expansion
- whiteheadS_le_innerSum / whiteheadInnerSum_le_card_nsmul — E1 envelopes
- whiteheadInnerSum_saddle — E1 packaged at the saddle
- tendsto_slack_zero — (2π/N)log N → 0
- innerSum_saddle_scaledLog_diff_tendsto_zero — CAPSTONE: reduces VC to the
  saddle-TERM value (sorry-free)
- whitehead_vc_of_saddle_value — sorry-free CONDITIONAL VC (§3b-cond): IF
  (2π/N)log(saddle term) → 4G THEN the inner-sum VC holds

REMAINING (the single open input): discharge `hsaddle` — identify the
saddle-term value with 4G (van der Veen's Clausen/Lobachevsky max-value
evaluation). This needs the QOU.Infra.Clausen import → a QOU-library build
to verify (no longer Mathlib-only). Deferred to avoid lake-build collision
while the #4394 prepare-merge agent is active on the shared workspace.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-01 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR litlfred/qou#8244)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8244 (`457d28e500f11a4249f57fd33fcd18112faef23b`, scriptCommitSha `1086b0ae6f630df61ca513a195514ef5d6137b5c`)
- **Summary**: Added `whiteheadLinkPhase_fresnel_symm` and `whiteheadLinkPhase_arg_at_half_even` in `QOU/Knot/WhiteheadPhaseAlgebra.lean`, verified by 80-dps mpmath probe `frust_cubic_tower_jhopf_whitehead_probe.py`.
