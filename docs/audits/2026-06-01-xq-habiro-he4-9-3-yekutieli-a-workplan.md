# X(q) Habiro / ⁴He (9,3) / Yekutieli-A workplan (2026-06-01)

**Branch:** `claude/xq-habiro-he4-9-3-yekutieli-a-2026-06-01`
**Status:** Workplan stub; probes follow as commits.
**Triggered by:** user 2026-06-01 "1 5 2 3 4" after PR #1673 merge.

## Scope

Three follow-on probes against PR #1673's verdicts:

| # | Goal | Source verdict | Probe |
|---|------|----------------|-------|
| 2 | X(q) Habiro element identification | PR #1673 Probe 1 (multiplicative refutation) | `xq_habiro_element_search_probe.py` |
| 3 | ⁴He (9,3) interface operator targeting | PR #1673 Probe 2 ((4,4,4) reframed → (9,3) is actual top) | `he4_9_3_interface_operator_probe.py` |
| 4 | Yekutieli Session A — per-cell α_em/π weight | PR #1673 Probe 3 scaffolding doc | `yekutieli_per_cell_alpha_em_derivation_probe.py` |

## Discipline guards

- Item 2: probe MUST report TIER (`proved-candidate`/`near-match`/`refuted`)
  + evaluate at q_proton AND q_muon. Habiro element lives at the fibre
  level (per AGENTS.md Im(q) framing). Use qLambert_single_term
  (main commit 58308c24a) as building block where applicable.
- Item 3: NO new substrate constant. Compute per-block A^(9,3)_{ξν}(I)
  extract; verdict is binary (matches required ρ_F or doesn't).
- Item 4: per PR #1673 Probe 3 scaffold, Session A only; pre-stated
  failure signature applies.

## Sequence

1. Item 2 first — highest precision-table impact (m_n + Δ_pn 100×
   targets both close if it lands).
2. Item 3 next — ⁴He retargeting, medium effort.
3. Item 4 last — Yekutieli-A is structural-derivation, lowest
   numerical certainty.

## Cross-refs

- PR #1673 (merged) — refuted multiplicative X(q) family + reframed (4,4,4)
- PR #1662 — bar-symmetric discipline tests
- PR #1657 / `ab11001cc` — Li_2^q Im z-independence
- PR #1666 / `58308c24a` — qLambert_single_term Lean prove
- PR #1511 — α_EM `[2]_q·(1-h²α)` Habiro element (template)
- `docs/audits/2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md`
- `docs/coordination/1ppq-mass.md`
- `.beans/research-queue.json`
