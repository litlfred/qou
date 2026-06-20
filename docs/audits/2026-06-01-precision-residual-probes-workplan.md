# Precision-residual probes — workplan (2026-06-01)

**Branch:** `claude/research-precision-residual-probes-2026-06-01`
**Status:** Workplan stub; probes follow as commits on this branch.
**Triggered by:** user 2026-06-01 "1 2 3 4" after PR #1662 merge.

## Scope

Three probes targeting open high-priority research queue items
(`.beans/research-queue.json`) + coordination on PR #1640:

| # | Goal | Queue item | Probe deliverable |
|---|------|------------|-------------------|
| 1 | m_n / Δ_pn 100× target (precision) | `research-flavor-split-mn-dpn-refinement` | `mn_dpn_xq_refinement_probe.py` |
| 2 | ⁴He +5.87% (categorical structure) | `research-multi-nucleon-interface-operator` | `he4_interface_operator_first_element.py` |
| 3 | m_p 54 ppb (categorical structure) | `research-yekutieli-substrate-derivation-mp` | audit doc only (scaffolds 3–5 session program) |
| 4 | q-usage audit triage (sibling) | PR #1640 | one coordination comment |

## Discipline guards (AGENTS.md)

- Probe 1: must report TIERED (`proved` / `near-match` / `fitted`) and
  evaluate at BOTH q_proton AND q_muon — single-anchor matches are
  discounted per the fibre/observable Im(q) framing in AGENTS.md.
- Probe 2: NO new substrate constant. The PR #1662 Probe 2 verdict
  exhausted that ansatz family. Must be CATEGORICAL (operator-level)
  or NULL.
- Probe 3: Yekutieli is 3–5 sessions. This session only SCAFFOLDS;
  it does NOT attempt closure. Audit doc maps the derivation chain
  steps + names concrete first probes.
- PR #1640 coordination: read the ~520 findings, propose a triage
  taxonomy, do NOT take ownership.

## Sequence

1. Probe 1 (X(q) refinement) — concrete; biggest precision-table
   impact if it lands. Test 3 candidate refinements at both anchors.
2. Probe 2 (⁴He interface scaffold) — compute the first PSD-dominant
   matrix element of H_3⊗4 → H_12 restricted to (4,4,4).
3. Probe 3 (Yekutieli) — audit doc only.
4. PR #1640 coordination comment.

## Cross-refs

- PR #1662 (merged) — bar-symmetric discipline tests; refuted v9 (1+q)/2
  + exhausted ⁴He ρ_F substrate-constant family
- PR #1621 — ⁴He gap research-state audit
- PR #1581 — m_p (α_em/π)/dim H_3 54 ppb near-match
- `prop:flavor-split-substrate`, `prop:magic-A-binding-formula`
- `docs/coordination/1ppq-mass.md`
