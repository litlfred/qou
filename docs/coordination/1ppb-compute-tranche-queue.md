# 1ppb compute tranche — prioritised work queue

> **Authoritative work queue** for the post-PR #901 1ppb compute /
> speed program. Ranked by (ROI × independence). Status updated as
> items complete.

## In-flight / completed (this session)

| # | Item | Status | PR / commit |
|---|---|---|---|
| **D1** | Block-graph hygiene (15 .ts files SUPERSEDED → mass-tower-operator-valued) | MERGED | #889 / `5a123ca39` |
| **D2** | Wenzl bridge Rust rayon MPFR wire-up | MERGED | #901 / `c9df2d34a` |
| **D3** | `mass_at_3A_proper` mmap-mode | MERGED | #901 / `c9df2d34a` |
| **D4** | H_12 A-operator Phase-1 extraction launched | background compute, ~60-90 min | log `/tmp/h12-phase1-extract.log` |
| **D5** | λ_scale q-dilog-tower agent brief | MERGED | #901 / `c9df2d34a` |
| **D6** | 210× scale-gap audit v3 (CAL-4 in λ_scale identified) | MERGED | #879 / `07e272f42` |
| **D7** | skill: default merge=merge-commit | MERGED | #881 / `52e5518eb` |

## Prioritised queue (ranked by ROI × independence)

| Pri | # | Item | Effort | Status |
|----:|---|---|---|---|
| **1** | **W1** | Refactor `atomic_tr_m_helium4.direct_h12_recursion` to use Wenzl bridge (unblocks item #1 of speed tranche; auto-benefits from #901's Rust wire-up) | hours | **in progress** (smoke-testing) |
| **2** | W2 | Closed-form `tr_M(𝓑_K) = tr_M(𝓑_K^vac) · z^{p_+} · (z-h)^{p_-}` refactor (Migration Backlog #4) — 4 production scripts | 4-8 hrs | queued |
| **3** | W3 | Strategy A — Rogers `Li_2^q` PSLQ at ℚ(q_0) algebraic locus (λ_scale closure candidate, parallel to #909's Strategy D) | hours | queued |
| **4** | W4 | Strategy C — cosh / cos_q ladder higher-order PSLQ (λ_scale; cheapest forward path) | hours | queued |
| **5** | W5 | Reeb-flow / Garside closed-form compute verification (Migration Backlog #5) | hours | queued |
| **6** | W6 | Strategy B — Faddeev `Φ_q` PSLQ (mass-side, parallel to W3) | hours | queued |
| **7** | W7 | H_12 Phase-2 (≥3500 test words, multi-nucleon canonical braids) — gated on D4 completion + rank-deficiency mitigation | 2-3 days compute | **gated on D4** |
| **8** | W8 | Migrate remaining 20 SUPERSEDED-importer scripts off `mass_endomorphism.py` — gated on W7 | hours per script | gated on W7 |
| **9** | W9 | Strategy E — universe-level closure cross-check (verification leg for any A/B/C/D candidate) | hours | gated on a candidate from W3/W4/W6/#909 |

## Sibling-PR review queue (waiting)

| Pri | PR | Theme | Status |
|----:|---|---|---|
| **R1** | #895 | Rust adapter wire-up for `atomic_tr_m_mpfr_50dps` | open; Gemini quota-blocked |
| **R2** | #904 | demote `prop:lambda-scale-bring-bloch-identity` → conj | open |
| **R3** | #909 | Strategy D — λ_scale from canonical 𝓑_p (stage-1) | open; Gemini quota-blocked |
| **R4** | #886 | Tier 1.A Rust LaurentQ reduce port + MPFR pipeline | open |
| **R5** | #892 | demote `prop:mobius-limit-from-thimble` → conj (CAL-4 cleanup) | open |
| **R6** | #900 | rename descartes→archimedean (chapter + namespace) | open |

## Anti-patterns (do NOT do)

1. Do not introduce a 7th-ansatz fit for `λ_scale` against m_p — that's the CAL-4 violation we're trying to close, not perpetuate (per `lambda-scale-qdilog-tower-direct.md` brief §Anti-patterns).
2. Do not introduce any new calibration constants. CAL-1 (m_e), CAL-2 (q_0 via m_μ/m_e), CAL-3 (𝔇_π) are the only allowed inputs.
3. Do not use float64 in production paths — MPFR ≥ 50 dps per AGENTS.md `compute-author`.
4. Do not silently squash on merge — `merge_method: "merge"` (merge-commit) is the standing default per #881.
5. Do not duplicate work that sibling PRs are doing. Coordinate first.
6. **Do not assume Δ_λ is atom-independent / global / shared across atoms.** The canonical framework formula in [`prop:rho-k-h3a-refinement`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md) has Δ_λ(K) **K-dependent by construction**. Probe-2 (PR #1229, [reframing audit](../audits/2026-05-25-delta-lambda-K-dependence-reframing.md)) empirically falsified the global hypothesis at max |Δ_λ| = 431.7 (vs 15.7 D-only) on the joint D+T+³He LP — confirming the framework's existing K-dependence. The closure problem is the **categorical determination of Δ_λ(K)** (Option E, PR #1252), not a global ansatz across atoms. Any future probe / ansatz that imposes Δ_λ^{global} = Δ_λ across atoms is a regression and will be rejected on review.

## Conventions

- Branch naming: `claude/<theme>-<utc-ymd>`
- One PR per logical work unit; small structured commits.
- All commits with merge-commit (not squash).
- Cherry-pick with `-x` flag + inform source PR.
