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

### Track A: BLOCKED on convention reconciliation (2026-05-22 spike)

1. **#4 — Closed-form `tr_M(𝓑_K)` refactor**
   - Original plan: wire `closed_form_tau_M(Z, N, q, tau_p, tau_n)`
     (Phase 5q verification green at rel.err 1e-50) into the 4
     target scripts as a `--method closed-form` opt-in.
   - **Spike result (deuteron, 2026-05-22):** the closed-form path
     gives `|tr_M(D)| ≈ 0.491-0.728` depending on tau_p source,
     while the production sympy + canonical-rust paths give
     `|tr_M(D)| = 0.388` (canonical convention).  **Same atom,
     different conventions, factor-of-1.27 to 1.87 numerical
     mismatch.**

   | Path | \|tr_M(D)\| | tau_p source |
   |---|---:|---|
   | `binding_canonical` sympy (production) | 0.388 | symbolic `tr_M_element` |
   | `canonical_tr_m_via_rust(1, 1, "D")` | 0.388 | `hecke-canonical-chi` Rust |
   | `closed_form_tau_M` w/ canonical tau_p (1.0653) | 0.491 | (mixed convention) |
   | `closed_form_tau_M` w/ Phase 5q tau_p (1.2204) | 0.728 | `chi_lambda_braid` convention (Phase 5q witness) |

   Phase 5q is internally consistent in its own convention.  But
   **direct substitution into production gives a different number,
   not a more-precise version of the same number** — so the swap
   is unsafe without convention reconciliation.

   **Concrete unblockers:**
   - **(a)** Identify the basis conversion between the two
     conventions (likely a per-partition normalisation factor;
     suspect connected to the `[n]_q!` denominator in the Wenzl
     bridge weights vs the canonical y_λ normalisation).
   - **(b)** Add a `pn_convention="canonical"` variant to
     `closed_form_tau_M` that takes canonical-convention
     (tau_p, tau_n) and returns canonical-convention tr_M(K).
   - **(c)** Then wire that variant into the 4 production scripts.

   **Revised effort:** 2-3 days of research + 1 day of wiring per
   script (was "mostly mechanical").

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

## 2026-05-22 update — V_7 + H_12 spike results (this session)

See [`docs/audits/2026-05-22-v7-and-h12-spike-results.md`](../audits/2026-05-22-v7-and-h12-spike-results.md)
for the full record.  Manager table update:

| Item | Prior | Post-spike |
|---|---|---|
| §5 #1 V_7 refinement (PR #916 next step) | "recommended" | **NEGATIVE.** 100 dps PSLQ at coeff ≤ 10¹² finds NO clean categorical correction for the −0.00523 V_7-vs-target gap.  V_7's "0.144 % proximity" is suggestive but not structural; Position 2 (V_7 is one of many proved categorical functionals, none with selection-rule justification) is the conservative read. |
| §5 #2 H_12 A-operator extract | "2-3 day compute" | **Memory-bounded.**  Died silently at the 12321 × 77 = 950K character sweep — likely OOM on the seminormal-matrix lru_cache.  Needs chunk-and-GC restructure (1-2 day impl) BEFORE the compute can complete. |

## 2026-05-22 update — Q_β c_3 exploration (this session)

See [`docs/audits/2026-05-22-exploration-c3-q-beta.md`](../audits/2026-05-22-exploration-c3-q-beta.md).

Spike on the "closest Subgoal-1 100× target" (Q_β 1.4× miss).
100 dps PSLQ on `Δc_3 = c_3_emp - c_3_cat = -0.00974` against
natural-substrate basis: **NEGATIVE** at maxcoeff 10¹⁵.  Best
near-coincidence (`-1/100`) is 2.67 % off and the residual has
no clean form.

**Reframing**: Q_β's 1.4× miss is **framework-bounded**, not a
closure gap.  The proved c_3 Hopf categorical value = -2; the
0.5 % gap to the empirical-fit c_3 = -2.00974 has no clean
categorical form in any tested basis.  This makes Q_β
structurally similar to m_p — both are bounded by the
framework's proved categorical predictions, not by a missing
refinement.

Cumulative empirical case is now **5 independent negatives**:

| Search | Target | Status |
|---|---|---|
| λ_p Bring-Bloch (PR #888 #904) | 2.4599527869 | NEG |
| λ_p q-dilog tower (PR #923) | 2.4599527869 | NEG |
| λ_p V̂_S + ℚ(ζ_60) (PR #928) | 2.4599527869 | NEG |
| V_7 sub-leading (this session) | 2.4599527869 | NEG |
| **c_3 Q_β sub-leading (this exploration)** | -2.0097397610 | NEG |

Recommended: update the Q_β row in the per-observable status
dashboard from "1.4× miss" to "framework-bounded at 11.13 ppb"
to reflect the consensus across the cluster.
