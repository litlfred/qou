# Sequencing plan — over-count refactor (`j1hg`) + muon→proton q₀ witness migration (`z5vu`)

**Status:** RESOLVED — owner chose **disposition B** (2026-06-30). `z5vu` closed
will-not-migrate-by-design (computations/ stays muon-q₀ canonical; proton anchor
enforced at the reporting layer per AGENTS.md rule 4). `j1hg` decoupled and now
proceeds independently in small per-batch PRs (§"Proposed order" step 4).
**Date:** 2026-06-30
**Beans:** `j1hg` (12 over-count scripts — proceeding), `z5vu` (closed will-not-migrate), `tnjb` (closed — root).

## Why these two are one job

The 2026-06-22 over-count triage ([`docs/audits/2026-06-22-overcount-3input-triage.md`](../audits/2026-06-22-overcount-3input-triage.md))
ruled the remaining genuine over-count scripts must be *"owner-sequenced
(alongside the q₀-repin sweep), not done as a mechanical pass."* Both are
**value-changing, witness-churning** changes to the canonical derivation
layer, and both are gated by AGENTS.md §"q₀ anchor convention" rule 4
(*"Do NOT migrate the ~840 muon-q₀ witnesses to proton without explicit owner
sign-off — large, gated"*). Sequencing them together avoids regenerating the
same ~840 witnesses twice.

## What each costs

| Bean | Change | Blast radius |
|---|---|---|
| `j1hg` (12) | Rewrite each script to derive `m_n = m_p + Q_β + m_e` instead of importing CODATA `m_n` directly | 12 producers + their witnesses; values shift by the m_n CODATA-vs-derived gap (~1.5 ppb) |
| `z5vu` (~840) | Re-pin the `computations/` witness layer from muon-q₀ (`1.10997859555733471…`) to proton-q₀ (`≈1.10998`) | ~72 producers / ~840 witnesses; m_μ flips MET→FAIL by construction (the documented μ–p tension) |

The current 12 over-count scripts (fresh audit, 2026-06-30): `atomic_mass_via_rho_k`,
`channel_product_mass`, `hecke_core_legacy`, `iterative_lp_dual_h6_deuteron`,
`per_knot_density_per_block_wiring`, `rho_k_h3a_{co_casimir,crystal,lp_dual,refinement,wenzl_bridge}`,
+ 2 more (run `computations/audits/canonical_script_input_audit.py` for the live list).

## Hard blocker (must resolve before z5vu execution)

The proton-q₀ solver `_solve_q_proton_f64` embeds the **fitted Habiro ratio**
`(1+46u⁴)(1+4u⁵)(1−29u⁶)…` — a CODATA fit purged from production (per `tnjb`).
So z5vu **cannot** recompute proton-q₀ through the live solver without
re-importing a purged fit. Options for the owner to pick:

- **(A)** Pin proton-q₀ to a committed high-precision constant (as `tnjb`/#2897
  did for the m_μ row) — no fit, but needs a canonical proton-q₀ string sourced
  cleanly (the package `Q`/`Q_MP` are both the muon value today).
- **(B)** Keep the `computations/` layer muon-q₀ canonical (status quo) and only
  enforce the proton anchor at the *reporting* layer (where `tnjb` already put
  it). Then z5vu is **not executed** — the 840 witnesses stay muon-canonical by
  design, per AGENTS.md rule 4's note that the convention is *"enforced at the
  reporting/precision layer, not by rewriting the canonical derivation witnesses."*

> **Recommendation:** (B). AGENTS.md already states the muon-q₀ `computations/`
> witnesses are the canonical 3-CAL derivation and the proton anchor belongs at
> the reporting layer. Under (B), `z5vu` resolves as *"will-not-migrate (by
> design)"* rather than an 840-witness churn, and `j1hg` decouples from it.

## Proposed order (if owner approves execution)

1. **Owner decision on the q₀ blocker** → (A) pin-proton or (B) keep-muon. This
   gates everything below.
2. **If (B):** `z5vu` closes as will-not-migrate; document in the q₀-convention
   ledger. `j1hg` then proceeds independently (step 4) since m_n is derived from
   the *same-anchor* m_p + Q_β + m_e regardless of anchor choice.
3. **If (A):** stage the proton-q₀ constant first (clean string + witness), then
   batch-regen the ~840 in small per-cluster groups (≤49 files/PR), L1/L2
   dashboards after each batch, no-regression gate.
4. **`j1hg` 12-script refactor** — one small PR per ~3–4 scripts:
   - replace `import … M_N_MEV*` input use with `m_n = m_p + Q_β + m_e`
     (`Q_β` from CAL-1+CAL-2, the canonical chain);
   - regenerate each script's witness in the canonical env (`-u … | tee`);
   - run the over-count audit — `over_count_count` must monotonically drop;
   - L1/L2 dashboards: no verdict regression.
5. **Close-out:** over-count audit `over_count_count → 0` (modulo whitelisted
   registry-source/comparison-only); refresh `docs/audits/2026-06-22-overcount-3input-triage.md`.

## Verification gates (every batch)

- `computations/audits/canonical_script_input_audit.py` — `over_count_count` strictly decreasing.
- `per_observable_100x_status.py` — summary stays **3/7** (no observable regresses).
- `onepb_status_dashboard.py` — L1 cross-method Δ within floor.
- No new `DeprecationWarning` (deprecated non-`_VALIDATION` alias use).

## What does NOT need owner gating (already done / safe)

- The over-count **audit refresh** (witness `over_count_count 23→12`) — landed
  2026-06-30 (PR #3168), pure static analysis.
- The CODATA-2022 registry edition + precision-lift (PR #3166) — the validation
  constants are now correct-edition and ≥50-dps, so the refactor's m_p/Q_β
  inputs are clean.
