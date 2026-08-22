---
# qou-v90i
title: 5 producers declared physical_proton but pin muon — disposition is per-file, not mechanical
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:37:16Z
updated_at: 2026-08-22T19:37:46Z
---

Found while re-baselining `qou-1c4y`; measurement +
`computations/audits/q0_muon_population_partition.py --list-contradictions`,
audit `docs/audits/2026-08-22-q0-migration-worklist-partition.md`.

Five producers are declared `physical_proton` in `q0_anchor_manifest.json`
yet bind q0 straight out of the **muon-anchored**
`q-pinning-50-digit.witness.json`, never importing `q_parameter`. Confirmed
in both directions: the emitted witness is stamped `q0Anchor: proton` while
recording the muon value.

## The disposition is NOT uniform — this is why the sweep needs judgement

| producer | evidence | disposition |
|---|---|---|
| `b_over_m_order_probe` | docstring: *"Computed at the **proton-pinned** q₀"* | **read is the bug** — intent is proton |
| `path4_rho_K_at_h3A` | compares against proton/neutron `ρ_K_CODATA`; experimental-layer | **read is the bug** (docstring also carries the `1.1097859` rounding) |
| `q_beta_form_a_n1_extension` | comment: *"Load **CAL-2** q_0 from canonical pinning witness"* | **MANIFEST is the bug** — CAL-2 *is* the ideal muon layer; the code is right |
| `q1_mass_gap_probe` | reads the witness as a **reference table** (`plancherel_weights_n3`, `[2]_q`) AND binds q0 from it; `:170` comments "(proton anchor)" | **mixed** — table read legitimate, q0 bind is the bug |
| `aK_via_lp_dual_hecke_basis` | "H_3 (proton, neutron)" names the *particle*, not the pin; no pin statement | **ambiguous** — needs a call |

## Why this matters beyond the five

A mechanical "re-pin everything declared `physical_proton`" would have
**broken** `q_beta_form_a_n1_extension`, which deliberately wants the
ideal CAL-2 pin. That is the same class of failure as `qou-m9xp` (the
first sweep attempt, which broke main for 208 producers). Two of five
here need the *manifest* changed or a human call, not the code — so the
per-file read is load-bearing, not ceremony.

## Next

1. Fix the two clear read-bugs (`b_over_m_order_probe`,
   `path4_rho_K_at_h3A`): route through `q_parameter`, re-run, refresh
   the witness. Precision preflight per AGENTS.md before commit.
2. Fix the manifest entry for `q_beta_form_a_n1_extension`
   (`physical_proton` -> `ideal_muon`).
3. `q1_mass_gap_probe`: separate the two reads — keep the reference-table
   read, bind q0 via `q_parameter`, drop the wrong "(proton anchor)"
   comment at `:170`.
4. `aK_via_lp_dual_hecke_basis`: needs an owner/author call on which layer
   it belongs to.

Gate: `--list-contradictions` exits 1 while any remain, so it can be
wired into a preflight once drained.
