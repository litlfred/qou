# Q_β residue A — formal acceptance as CAL-3-anchored (2026-06-03)

> **Decision**: Following four independent NEGATIVE searches for a single-
> formula categorical identification of the Q_β residue A at `u_substrate`,
> the residue is **formally accepted as inherently CAL-3-anchored** in
> current production. Promoting `c_3` from tier `cal-anchored` to tier
> `derived` requires a **composite Kashiwara operator structure** that
> is research-grade and infrastructural — out of scope until upstream
> KLR / crystal-graph Lean infrastructure is in place.

## The 4-search NEGATIVE bracket

| Search | Candidates | Result | Source |
|---|---|---|---|
| Chain 1 α — Wenzl-projector Markov trace | 4 conventions (JW, sym, antisym, adjoint-like) | NEGATIVE 4/4 (best: anti-sym at 144,801 ppm) | PR #1760 |
| Chain 1 β — Kashaev tower | 3 variants (standard q-Pochhammer, Bloch-Wigner D(z), Faddeev real-q L_q) | NEGATIVE 3/3 (Bloch-Wigner identically 0) | PR #1760 |
| 15-candidate c_3 re-run — categorical block-eigenvalue / discrete-channel / Markov-trace combinations | 15 closed forms | NEGATIVE 15/15 (best: `-(q² + q⁻²)` at 9,109 ppm m_p-pin / 16,921 ppm muon-pin) | PR #1760 |
| Chain 4 — Kashiwara/crystal-derived single-formula | 6 candidates (Demazure char, SYT maj-index, J_Hopf Kauffman, symmetric+Hopf-center, [2]_q·b, J_Hopf(1)·b²) | NEGATIVE 6/6 (best: `-(q + q²)` SYT maj-index at 131,775 ppm) | PR #1768 |

**Total**: 28 single-formula categorical c_3 candidates tested, all FAIL the 10 ppm gate.

**Gate convention**: the gate is "passes 10 ppm at the m_p-pin anchor" (production anchor used by the L2 dashboard headline). The Chain 1 first-tests and 15-candidate c_3 re-run additionally reported the muon-anchor miss for context, and the best candidates have been characterized at both; the m_p-pin gate is the dispositive one for current production. No candidate has passed BOTH the m_p-pin gate and 10 ppm at the muon anchor.

## What this means for production

1. **c_3 tier stays `cal-anchored`** in `qbeta-ck-cache.witness.json`.
   This was already the production state — the 4-search bracket
   confirms there is no fast path to promote it.

2. **Q_β L2 dashboard headline uses the `derived` tier only** (Q_N2 =
   1279 ppb at proton-pinned q₀), reported as 164× off the 7.8 ppb
   100× target. This is the production status.

3. **The `cal_anchored` tier value** (`0.78233341` MeV at proton-pinned
   q₀, exact-to-CODATA-input precision) **remains a reusable calibrated
   constant** for downstream consumers (m_n Path C, Δ_pn) but **must
   not be reported as a prediction** or counted toward dashboard pass.
   No change.

4. **No fitted form is wired into production**. The Δ_λ gate held
   throughout — every candidate tested was closed-form in q + Hoefsmit
   b, never a fit.

## Why a 7th single-formula ansatz won't help

The flip-flop history in [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
(6 wire/un-wire flip-flops in the c_3 = J_Hopf(q=1) saga) shows that
single-formula promotion of c_3 has been attempted and refuted multiple
times. The 28-candidate bracket is now broad enough that **a 7th
ansatz from any single-formula family should be ruled out a priori**:

- Markov-trace single-formulas: 4 Chain 1 α + 7 of the 15 c_3 re-run = 11 tested
- Kashaev quantum-dilog single-formulas: 3 Chain 1 β + 1 of the 15 = 4 tested
- Kashiwara/crystal single-formulas: 6 Chain 4 + 2 of the 15 = 8 tested
- Combinatorial (SYT, partition statistics): 1 Chain 4 + 3 of the 15 = 4 tested
- Symmetric block combinations: 2 Chain 4 + 4 of the 15 = 6 tested

These categories saturate the natural single-formula search space.
The next productive direction is **composite operator structures**
that combine 2+ of these categories — which requires upstream
infrastructure (per the Mathlib audit below).

## Composite-operator search: upstream infrastructure gap

The natural composite structures that have NOT been tested but could
contain the residue A:

- **Wenzl·Kashaev symmetric products** (one operator from each chain
  combined via symmetric algebra) — would need linear-combination
  `tr_M` infrastructure not currently in `pyhecke`
- **Demazure × q-Pochhammer mixed traces** — would need Demazure
  module Lean / Python infrastructure
- **KLR canonical-basis-weighted Markov traces** — would need KLR
  algebra implementation
- **Type-B folded crystal sums** (per AGENTS.md §7b authoring
  guidance) — would need Type-B Cartan datum + folded-crystal
  machinery

See [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
(this PR) for the upstream-integration roadmap.

## What this is NOT

- This is **not** a claim that the residue A categorical-ID is
  impossible. It's a claim that the SHALLOW search space is exhausted
  and the DEEP search requires infrastructural investment first.
- This is **not** abandoning the 1ppQ Q_β goal. The 100× target stays
  at 7.8 ppb; the current 164× miss stays on the L2 dashboard.
- This is **not** a wire decision. The production c_3 stays at the
  cal-anchored tier; no new mass-formula values change.

## Updates landed in this PR

1. This audit doc — formal acceptance + 4-search bracket
2. Master ledger `docs/coordination/1ppq-qbeta.md` — entry 2026-06-03 cont. 6 closing the search
3. KLR/crystal infra scope doc — upstream integration roadmap
4. `qbeta-ck-cache.py` docstring — updated to reference this audit as
   the formal acceptance (instead of vague "future Lean-formalization
   work" implication)
