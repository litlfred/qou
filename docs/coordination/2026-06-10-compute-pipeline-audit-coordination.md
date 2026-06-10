# Coordination ledger — compute-pipeline deep audit (#2104) × Δ_λ/binding siblings

**Date:** 2026-06-10 · **Driver PR:** #2104
(`claude/compute-pipeline-audit-generalize-2026-06-10`)
**Goal:** generalized any-(Z,N) compute infra + accuracy wiring + optimize;
NO FLOAT64 / NO FITTING. Coordinated against the Δ_λ / binding-closure cluster.

## Scope map

| PR | scope | relationship | action |
|----|-------|--------------|--------|
| **#2104** (this) | 4-axis compute audit → float64/wiring/perf fixes + generalized `predict(Z,N)` | driver | — |
| **#2103** | per-isotope binding-constituent stack for any (Z,N): symmetrization + `y_lambda_tower_infra` + Rust lossless χ (`chi_q_via_gp` matrix-M) | **strong overlap** (both generalize binding to any (Z,N); both build a χ engine) | intent posted ([#2103](https://github.com/litlfred/qou/pull/2103#issuecomment-4675612013)) |
| **#2078** | atom→V_hyp→Δ_λ closure workplan; stage ③ Δ_λ via `vol_density` (Li_2^q depth-2) | **dependency** (my Phase-3 binding consumes its Δ_λ; its stage ③ hits my GAP#1) | intent posted ([#2078](https://github.com/litlfred/qou/pull/2078#issuecomment-4675612592)) |
| #1942 | GAP-A4 categorical chain content (T17) | loose (categorical Δ_λ route) | no comment (content-only) |
| #2095 | Lean full-lib build errors | tangential (touches QOU lean lib) | no comment |

## Key coordination findings

1. **χ-engine duplication risk (#2103 ↔ #2104).** #2103 builds any-(Z,N) χ on
   matrix-M `chi_q_via_gp` (⁵Li 67 s); my merged transfer-χ (#2097,
   `chi_monotone_transfer`) is **d_λ-free** (⁶Li 0.62 s). Proposed: their y_λ
   tower + symmetrization + **my transfer χ** = the shared any-(Z,N) stack —
   not two χ engines. Awaiting reply.
2. **C2 float64 fix may consume #2103's y_λ tower.** My Axis-A flags
   `wedderburn_jones_markov.y_lambda_at` (`sp.Float`/f64). #2103's
   `y_lambda_tower_infra` closed-form path may be 50-dps/no-float64 — if so,
   consume it for C2 instead of re-lifting. **Open question to #2103** →
   C2 deferred until answered (avoid duplicate re-lift).
3. **GAP#1 (uniform vs per-knot vol_density) blocks #2078's stage ③.** Their
   Δ_λ-via-`vol_density` lands per-knot only if the 65-isotope sweep migrates
   off uniform `vol_density_borromean`. Flagged on #2078.
4. **NO-FITTING agreement.** My Axis-B (clean) and #2078's "canonical, not a
   fit" `vol_density` Route A agree: Δ_λ stays categorical.

## Next non-overlapping task

C4 (exact `(c,d)` in `atom_braid_word_3A`) — the root of ~half the 22 float64
violations, clearly owned here (feeds the merged transfer), independent of
#2103. ~30 consumers ⇒ needs careful per-consumer verification (run the
transfer D=0.388 assertion + the C6 audit delta). C2 (y_λ) waits on #2103.