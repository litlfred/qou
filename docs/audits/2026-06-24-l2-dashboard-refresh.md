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

## 1b′ implemented — `q_at()` de-fitted to one cal-anchored `c_4` (2026-06-24)

Per author decision, the `habiro_ratio` in the canonical q₀ solve was changed from
the rounded-integer fit `(1+46u⁴)(1+4u⁵)(1−29u⁶)` to the single data-determined
term-6 Habiro residue `1 + 46.03·u⁴`, dropping the below-floor cosmetic `c_5=4` /
`c_6=29` (σ_c5=1.34, σ_c6=157; `computations/mp_habiro_c4_keystone_probe.py`). Four
coupled sites kept in sync: `qou_substrate/constants.py` (f64 `_solve_q_proton_f64`
+ mpmath `q_at`), `computations/substrate/q_parameter.py` (f64 duplicate),
`computations/m_p_substrate_identity_50dps.py` (producer).

**Effect (verified):** m_p still anchors exactly (residual 2.4e-50); q₀ shifts
**0.0005 ppb** (`…5573347…` → `…567880…`); m_μ prediction stays 0.017 ppb. No
observable regresses; the substrate-identity producer's 2 assertions pass.

**`c_4` status:** cal-anchored / near-match (data-determined ≈ 46.03 ± 0.011 from the
m_p pin); derivation = the open s5-so3 / Habiro keystone (bean s5bb) — exactly the
Q_β `c_k` tier.

**The dashboard 4/7 is unchanged — that is the remaining point.** 1b′ removes the
cosmetic integers but does NOT move the count: m_μ is read from the borromean
`muon_check` round-trip and, scored as a prediction at the (cal-anchored) q₀, is
0.017 ppb → numerically passes. The honest **3/7** requires the *dashboard* to TIER
m_μ as a cal-anchored cross-check (not an independent derived pass), parallel to how
Q_β's cal-anchored rungs are excluded. That is a `per_observable_100x_status.py`
count-semantics change — **deferred to author decision** (it alters the headline
derived count).

**Witness churn (Task 3 — characterized + sweep tool fixed; bulk deferred).** The
0.0005-ppb q₀ shift staleness-marks the q₀-pinning witnesses corpus-wide. After the
tool fix below, `q0_repin_regen_batch.py --plan` reports **614 stale** at the
`computations/` root (**389** re-runnable producers + **77** manual/no-scriptFile);
a recursive scan finds **~1034** including subdirs — all stale only at the **12th
digit** (0.0005 ppb, far below every target; no assertion regresses). This is a
**dedicated post-merge batch**, not foldable into this PR: the tool commits + pushes
**per-producer** on its own branch `claude/q0-repin-regen-batch-*`, with long-timeout
passes for heavy-atom producers (isotope tables, Habiro-coefficient, SDP assemblies).
It should run **after 1b′ merges** (so it pins to the final q₀).

**Sweep-tool bug fixed here.** `q0_repin_regen_batch.py` was silently reporting
`0 stale` — its `REPO = HERE.parent.parent` overshot the repo root after the Phase-6
subdir move, so the scan glob (`REPO / "computations/*.witness.json"`) hit a
non-existent path. Corrected to `HERE.parent`. (A second limitation — the
non-recursive glob misses subdir witnesses — is noted for the sweep operator.)
Without this fix the post-merge sweep would have silently done nothing.

Regenerated in this PR: `m-p-substrate-identity-50dps.witness.json`,
`per-observable-100x-status.witness.json`.

**Cross-PR:** `m_p_substrate_identity_50dps.py` is also edited by **#2723**
(beautiful-wright, Kashiwara-b² neutron). #2723 **has since merged to main**; the 1b′
edit was re-applied cleanly on its rewritten producer during the +66 rebase
(habiro_ratio auto-merged to `1 + 46.03·u⁴`; m_p anchors, m_n unaffected).
