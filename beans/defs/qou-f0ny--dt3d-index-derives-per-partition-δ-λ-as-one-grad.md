---
# qou-f0ny
title: DT/3d-index derives per-partition Δ_λ as ONE graded Euler characteristic (horn unification)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T08:14:12Z
updated_at: 2026-10-04T15:12:25Z
parent: qou-v2om
---

**Epic:** `qou-r2nh` (the two horns → forward DT/3d-index route). **PR:** #4551.

## Verdict (per-partition Δ_λ): YES — DT/3d-index derives BOTH horns as ONE object

`Δ_λ = (Behrend-signed) Donaldson–Thomas count of the Springer fibre 𝓑_λ`:
- `n(λ) = dim_ℂ 𝓑_λ` (Springer, type A) is the cohomological grade;
- Behrend `(-1)^{dim moduli}` sign = horn-1 chirality `(-1)^{n(λ)}` (PR #4540);
- count `dim V_λ` = horn-2 magnitude (PR #4538);
- the SAME odd a-function grade causes both the minus sign (horn-1) AND the
  ℕ-escape / KL-positivity violation (horn-2) — one phenomenon, not two legs.

This dissolves the ledger's "sign is exogenous / magnitude = dim" framing.

**Proved sorry-free** (`DeltaLambdaDTIndex.lean`, `lean`-direct exit 0):
`dtEuler_eq_deltaLambda` (the unification), `dtEuler_eq_sign_times_dim`,
`dtEuler_magnitude_eq_dim`, `dtEuler_neg_iff_odd_grade`,
`horns_share_one_odd_grade`, `deltaLambda_not_kl_positive`, `dtEuler_mixed_sign`.

## OPEN (honest)

1. **Internal derivation from the 13 drivers** — that the substrate *forces* the
   DT moduli `𝓑_λ` (dim `n(λ)`, count `dim V_λ`), vs. identifying it after the
   fact. The `qou-ujmw` pattern (DT-count established, driver-derivation open).
   Carried as content-bearing primary conjecture `DeltaLambdaDTRealization`, NO
   instance; not consumed by any theorem.
2. **Many-body A=3 magnitude scalar `r* = μ₃/c₃ ≈ 1.585`** — a DISTINCT,
   still-open cluster-integral object (walled from every route), untouched here.

Audit: `docs/audits/2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`.
No fit; nothing wired; no anchor inverted.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
