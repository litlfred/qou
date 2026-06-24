# L2 dashboard refresh — fresh Q_β/m_n/Δ_pn margins + an m_μ scoring anomaly

**Date:** 2026-06-24
**Branch:** `claude/clever-volta-uir8ay`
**Scope:** regenerated the two L2 status dashboards; records the fresh failing-trio
margins and flags a producer-semantics anomaly on the m_μ row that should NOT be
read as an accuracy gain. No production formula changed.
**Witnesses:**
[`computations/per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json),
[`computations/onepb-status-dashboard.witness.json`](../../computations/onepb-status-dashboard.witness.json)

## Fresh failing-trio margins (the real refresh)

Re-running `per_observable_100x_status.py` moved the three shared-root failures
slightly (genuine recompute, all improved a touch):

| observable | err_ppb (was → now) | 100× miss (was → now) |
|---|---|---|
| Q_β     | 1279. → **1248.** | 164.0× → **160.1×** |
| m_n     | 1.066 → **1.040** | 185.4× → **181.0×** |
| Δ_pn    | 773.9 → **755.6** | 163.3× → **159.4×** |

These three share one root — the Q_β `c_k` truncation / Habiro-element wall; m_n
and Δ_pn inherit it (see `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`).
Nothing here flips green without closing the Q_β Habiro element (research-grade).

## The m_μ anomaly — "4/7" is an anchor round-trip, not an accuracy gain

The regenerated dashboard reports **4/7** beating 100× (vs AGENTS.md's documented
**3/7**), because the m_μ row changed from **209.8 ppb (963.6× miss)** to
**0.05168 ppb (0.24×, passing)**. This is **not** a real improvement and **not** a
stale-hash artifact — it is a **producer-semantics drift**:

- `per_observable_100x_status.py` (line ~260) reads m_μ from
  `borr_data["muon_check"]["m_mu_pred_MeV"]` in
  `m-p-borromean-verification-50dps.witness.json`.
- That field uses `formula = "vol_4_1_over_hbar_q_squared"` — i.e. the **CAL-2
  anchor relation** `m_μ/m_e = Vol(4₁)/ℏ_q²` itself. Evaluating the anchor formula
  reproduces m_μ to ≈1 ppb (a round-trip), so it trivially "passes" 100×.
- The upstream witness is **fresh** (`scriptCommitSha c4ab12b6`, `scriptHash
  b98027e0c192`) — this is a semantics question, not hash staleness.
- It **contradicts the producer's own header** (line ~90: *"after the 2026-05-29
  q₀ re-pin it is a genuine 9.5σ PREDICTION, NOT [an anchor]"*) and the cheat-sheet
  (q₀ is proton-pinned; m_μ/m_e is a 9.5σ cross-check prediction, the μ–p substrate
  tension ≈ 209.8 ppb).

**Net:** scored as the post-re-pin *prediction*, m_μ misses by ~963.6× and the true
count is **3/7**, exactly as AGENTS.md / `precision-goals.md` state. The live "4/7"
scores m_μ as a CAL-2 *anchor-consistency check* instead.

## Author decision needed (not silently resolved here)

Per the critical-distance / corpus-grep disciplines, this is flagged, not patched:

1. **If m_μ should be the proton-pinned prediction** (matching the producer header
   + AGENTS.md): the producer should compute m_μ as
   `m_e · (Vol(4₁)/ℏ_q²)` at the **proton-pinned** q₀ and score that 209.8-ppb
   deviation — not read the `muon_check` anchor round-trip. Then the dashboard
   returns to the documented 3/7.
2. **If the anchor-consistency reading is intended**, AGENTS.md §Precision-goals and
   `precision-goals.md` should be updated to say so (and the "963.6×" note retired).

The committed witnesses reflect the **current live pipeline output** (option-0:
honest snapshot); this note is the interpretation. No AGENTS.md / precision-goals
edit is made here — that is the author's call.

## onepb dashboard (L1)

`onepb_status_dashboard.py` re-ran clean: LP-dual GB-NF maximizer in active set
6/6, duality gap 0.0; Markov-trace consistency max rel_delta 0.0. Two witnesses
remain absent (`brundan_kleshchev_audit`, `alpha_k_macdonald`) — pre-existing, not
introduced here.
