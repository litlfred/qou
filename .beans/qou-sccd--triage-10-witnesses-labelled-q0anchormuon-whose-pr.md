---
# qou-sccd
title: Triage 11 witnesses labelled q0Anchor=muon whose producer my migration moved to physical_proton
status: completed
type: task
priority: normal
created_at: 2026-08-22T09:48:18Z
updated_at: 2026-08-22T14:19:20Z
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


## All 11 accounted for — and no live straddle beyond the one already fixed

The three that exceeded the 600 s cap, re-run at 2400 s with the restore **verified** this time (the first harness silently failed to restore `binding-canonical.witness.json`):

| producer | verdict | wall |
|---|---|---|
| `binding_via_interface_knot` | **unmeasurable** — timeout at 2400 s | 2400 s |
| `block_swap_binding` | **unmeasurable** — timeout at 2400 s | 2400 s |
| `he3_tritium_cosh_asymmetry_diagnosis` | **clean re-pin** — 5 math fields moved with `q0` muon → proton | 953 s |

The two timeouts are an honest verdict, not a gap in the method: 40 minutes each is beyond what this container can measure, and both restored cleanly.

### The third is a re-pin, not a straddle — and the distinction is the point

`he3_tritium_cosh_asymmetry_diagnosis` recomputes at proton because the migration moved it there, and 5 mathematical fields move with `q0`. That looks like the `atomic_tr_m` signature, and it is not:

- **`atomic_tr_m`** returns the muon string from `q0_for("ideal")` while its cone follows the manifest — so one quantity carried two pins. A straddle.
- **This one** has **zero** mentions of muon, anchor, or a pin requirement anywhere in its source. It reads whatever pin is in force and computes consistently at it.

So its committed witness is **stale** (still muon-labelled, pre-migration), not wrong. Whether it *should* be proton is the ordinary `qou-1c4y` migration question, and nothing in the producer objects.

### Final tally

| class | n | |
|---|---|---|
| stale label — math byte-identical | 3 | `binding_canonical`, `derived_chi_catalogue_matrix_m_mpfr`, `markov_peel_atomic_witness` |
| **live break** — needs muon, guarded | **1** | `cross_check_trM_1ppb` — **fixed** (`qou-wn6d`) |
| clean re-pin, committed witness stale | 1 | `he3_tritium_cosh_asymmetry_diagnosis` |
| pre-existing breakage | 4 | `borromean-axial-coupling` (`qou-cnbm`), `hadron_knot_table`, `vhat_per_crossing_chain`, `parabolic_cylinder_channel_mixing_probe` |
| unmeasurable here | 2 | `binding_via_interface_knot`, `block_swap_binding` |

**Total damage from the migration across this class: two producers** — the `atomic_tr_m` straddle and the `cross_check_trM_1ppb` break. Both fixed. The other nine are stale labels, pre-existing breakage, or clean re-pins.

That is a better outcome than the bean's opening framing, which treated all 11 as candidate straddles. Measuring beat estimating again: the alarming reading was 11, the real number was 2.

Bean closed on measurement. The two unmeasurable producers are noted rather than assumed — if either matters later it needs a machine that can run them, not a re-run here.
