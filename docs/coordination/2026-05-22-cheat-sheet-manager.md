# Cheat-sheet §5 manager — 2026-05-22

**Role:** This document tracks **execution of the
[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
§5 Compute-pipeline migration backlog** to completion.  One ledger,
five items, status at-a-glance.

Per owner direction 2026-05-22:
> "update cheat sheet/trackers. you are manager of getting cheat
> sheet done."

## Current status

| # | Status | Item | Closure / PR | Next concrete step |
|---|---|---|---|---|
| 1 | ✅ closed | LAMBDA literals → PROVED Family A | #888 + #895 | **Strategy H V_7** (#916) — right sign on h², +0.144% gap; refine sub-leading character correction |
| 2 | ⏸️ gated | SUPERSEDED `mass_endomorphism.py` migration (20 importers) | #889 (15/20 graph edges) | H_12 A-operator extract (2-3 day compute) |
| 3 | ✅ closed | Rust LR adapter into `atomic_tr_m_*` | #901 + #895 + **#915** | — (both `atomic_tr_m_*` files now Rust-backed) |
| 4 | ⬜ open | Closed-form `tr_M(𝓑_K)` refactor (4 scripts) | Phase 5q verification green | thread `pn_convention="chi_lambda_braid"` flag through `closed_form_tau_M` |
| 5 | ⬜ open | Reeb-flow / Garside compute verification | — | not started (lowest priority) |

Two of five closed.  Three remaining; one gated, two open.

### 2026-05-22 update: #915 closed the `atomic_tr_m_helium4` exception

PR #895 deliberately left `atomic_tr_m_helium4.py` alone (it had a
documented PR #564 disjoint-product banner).  PR #915 refactored it
to the Wenzl bridge — now both `atomic_tr_m_*` files are Rust-backed
and fix #3 is fully closed across both entry points.

### 2026-05-22 update: V_7 is structurally better than Family A

PR #916 enumerates eight Wedderburn linear functionals on H_4
characters and identifies **V_7 = Σ dim_q V_λ / [4]_q** as the
**first one with the right sign on h²** — c_2 = −13/16 (vs target
~ −G = −0.916).  Lands +0.144% vs CODATA target (vs Family A's
+2.89% with WRONG sign).

Implication for cheat-sheet §5 #1: Family A is **algebraically
proved but mis-identified** as λ_scale.  The actual λ_scale is in
the V_7 family, with a small categorical sub-leading correction
still to be derived.  The Family A swap in #895 is the
safest-minimal-risk production state; V_7 is the next step.

## Plan to close — execution order

### Track A: code-level work that can start now

1. **#4 — Closed-form `tr_M(𝓑_K)` refactor (next session)**
   - Wire `closed_form_tau_M(Z, N, q, tau_p, tau_n)` (already
     verified at Phase 5q, rel.err 1e-50) into one of the 4 target
     scripts as a `--method closed-form` opt-in (mirrors the
     `--method canonical-rust` pattern from #895).
   - Cross-check against `canonical_tr_m_via_rust` at the boundary
     so production output bit-identical for the chi_lambda_braid
     convention.
   - Then propagate to the remaining 3 scripts.
   - **Effort:** ~1 day per script, mostly mechanical.

### Track B: blocked on compute

2. **#2 — SUPERSEDED `mass_endomorphism.py` migration**
   - Code-level migration of the 14 remaining `.py` importers
     gated on **H_12 A-operator extract** (rank-deficiency risk).
   - Direct unblock: `markov_peel.tr_M_atomic(2, 2)` H_12 run
     (already runnable at 50 dps; just needs compute time).
   - **Effort:** 2-3 day compute task + 1-2 day per-importer
     mechanical swap.
   - Note: PR #889 already did the **graph edges** (15 `uses[]` /
     `interprets:` swaps); only the **code imports** remain.

### Track C: research-tier

3. **#5 — Reeb-flow / Garside compute verification**
   - Paper-only commits exist; no verification script.
   - **Effort:** unknown — depends on how the paper-side claim
     is structured; could be a 2-hour numerical spot-check or a
     multi-day research-grade probe.
   - **Defer** until #2 and #4 are done — lowest production
     impact.

## Adjacent open work (informs but doesn't gate cheat-sheet §5)

| Item | Owner | Gate |
|---|---|---|
| Tier 1.A 4× speed gate | PR #886 | ⁶Li wall < 60 s (currently 84.5 s) — 1-2 day Rust optimisation |
| Tier 1.B orbit reduction | none yet | gates A ≥ 8 / organic chemistry; preflight required |
| Q_β 1.4× miss (Subgoal-1 closest) | research | brane-tower full-sum OR substrate-q_0 |
| Bring color-tube p-n averaging | research | flavor-asymmetric closed form |

## Per-PR status (live)

| PR | Topic | Status |
|---|---|---|
| #886 | Tier 1.A Rust port | open, 4× gate at 2.65× |
| #892 | CAL-4 curve-fit taxonomy | open |
| #904 | CAL-4 Bring-Bloch taxonomy | open |
| #909 | Strategy D research | open, stage 1 complete |
| #917 | per-observable dashboard refresh | open (Family A post-#895) |

## Pending refresh: dashboards
- `per-observable-100x-status.witness.json` post-#895 (in PR #917)
- `onepb-status-dashboard.witness.json` L1 (green; no refresh needed)

## Next manager action

After #917 merges:
1. **Cherry-pick Track A** — open a new branch and execute the
   first closed-form `tr_M(𝓑_K)` swap (`atomic_chirality_residue.py`
   is the simplest target — uses chi_lambda_braid already, so
   convention matches).
2. **Re-evaluate Track B** — check if H_12 A-operator extract has
   landed on any sibling PR (likely close, given #886 / #889
   recent activity).
3. **Defer Track C** until A + B complete.

This ledger updates after every merged PR in the cluster.
