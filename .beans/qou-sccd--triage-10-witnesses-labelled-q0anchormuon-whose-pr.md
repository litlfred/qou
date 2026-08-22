---
# qou-sccd
title: Triage 11 witnesses labelled q0Anchor=muon whose producer my migration moved to physical_proton
status: todo
type: task
priority: normal
created_at: 2026-08-22T09:48:18Z
updated_at: 2026-08-22T10:27:39Z
---

## Triage complete — 11 candidates, and a second producer my migration BROKE

Re-ran every candidate (600 s cap), diffing mathematical fields only:

| producer | verdict |
|---|---|
| `binding_canonical` | **stale label** — math byte-identical |
| `derived_chi_catalogue_matrix_m_mpfr` | **stale label** — math byte-identical |
| `markov_peel_atomic_witness` | **stale label** — math byte-identical (116 s) |
| `cross_check_trM_1ppb` | **🛑 BROKEN BY MY MIGRATION** — see below |
| `borromean-axial-coupling` | cannot run — `KeyError: 'gram_inverse'` (pre-existing, `qou-cnbm`) |
| `hadron_knot_table` | cannot run — numpy `TypeError` (float64 conversion) |
| `parabolic_cylinder_channel_mixing_probe` | cannot run — solver: *"try another starting point"* |
| `vhat_per_crossing_chain` | cannot run — numpy `_UFuncInputCastingError` |
| `binding_via_interface_knot` | timeout at 600 s (known slow, >1200 s) |
| `block_swap_binding` | timeout at 600 s |
| `he3_tritium_cosh_asymmetry_diagnosis` | timeout at 600 s |

**3 stale labels, 1 live break, 4 pre-existing breakages, 3 unmeasured (slow).** So the *latent-straddle* reading holds for the three measured non-broken ones: their muon labels describe nothing the numbers depend on, which is sibling #5436's class (ii).

### `cross_check_trM_1ppb` — refused to run, and its own guard said exactly why

```
L1 cross-check must run under the MUON q0 pin, but the runtime
q_parameter.Q_50_DIGIT_STR = 1.1099785827513808… is not the muon q0
(1.10997859556). Set QOU_Q0_ANCHOR=ideal — else peel/chi-cache
color-weighting is mixed-pin (audit 2026-07-18-avg-color-delta-q0-pin-mismatch.md).
```

That is a **second** producer with a documented muon-pin requirement that my migration moved to `physical_proton`. Unlike `atomic_tr_m` it fails **loudly** rather than straddling silently — good design on its author's part, and the reason it shows up as "cannot run" rather than as a wrong number.

Manifest entry restored. `ideal_muon` now holds three: `q_pinning_50_digit` (anchor-definer), `atomic_tr_m_mpfr_50dps`, `cross_check_trM_1ppb`.

### The muon-required cluster is bounded — measured

Grepping for the muon-pin guard idiom finds **9** producers. Eight are **undeclared**, so the manifest never bound them and my migration did not touch them. Only `cross_check_trM_1ppb` was declared. The cluster is therefore *not* large, and the two restorations cover the manifest side of it.

### 🛑 Still open — the artifact, not the manifest

With the manifest fixed, `cross_check_trM_1ppb` gets **past** the first guard and fails on a second:

```
chi-cache witness was computed at a q0 that is NOT the muon pin
(1.1099785827513808… vs 1.10997859556); regenerate it under QOU_Q0_ANCHOR=ideal
```

`canonical-tr-m-via-chi-cache.witness.json` now carries `q0Anchor: proton`, re-pinned by my own migration batches (`1fead8dd49`, `4326460a44`), and its producer is declared `physical_proton`.

**This is a design question, not a fix to guess at.** The chi cache appears to serve both a muon L1 cross-check and proton consumers; flipping it to muon would break the other side. That is precisely AGENTS.md §q₀ rule 4 constraint 3 — *"a comparison producer needs BOTH pins and the manifest cannot serve it"* — and the answer is probably a per-anchor cache pair (as `_Y_LAMBDA_BY_ANCHOR` already does for y_λ), not a re-pin.

Not doing that here. Recording it because I caused it and the next agent should not have to re-derive it.
