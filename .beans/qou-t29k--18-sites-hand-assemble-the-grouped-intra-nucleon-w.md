---
# qou-t29k
title: '18 sites hand-assemble the grouped intra-nucleon word: a third mechanism, distinct from qou-cgyn and qou-y2o7'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T06:35:57Z
updated_at: 2026-09-14T06:45:48Z
---

## The mechanism

`_PROTON_G0`/`_PROTON_G1` (and the neutron pair) are the canonical eleven
letters **bucketed by generator**. `mass_at_3A_proper` says so where it imports
them: they "cannot express the interleaving, which is the whole point of
`nucleon_word_letters`". And `pyhecke.atom.nucleon_word_letters` defines the
legacy ordering as exactly one line:

```python
if intra_order == "grouped":
    return [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]
```

So a caller that writes all of `g0` then all of `g1` has transcribed that
branch. It is the grouped word **by construction** — not a stale value, not a
mirror that drifted, and unreachable by re-running anything.

## Why the value fingerprint could not see it

`qou-4383`'s `intra_ordering_value_fingerprint_audit` matches committed
*numbers* against the known grouped constants. That needs a witness carrying a
|tr_M| at a canonical atom, so it is blind to symbolic producers, to producers
too slow to have been re-run, and to witnesses recording a ratio or a slope.
Under `qou-4383` I re-ran six safe producers hunting stale artifacts and every
one came back byte-identical — which correctly retired the stale-value
hypothesis and left the residue unexplained. This is the explanation.

## What found it

`tr_m_algebraic_q` — a symbolic mirror of the production atom word whose own
witness had recorded
`algebraic_q0_matches_transfer  computed=9.76e-01  tol=1e-09  passed=False`
since 2026-09-07, unread. Its `build_atom_symbolic_q` looped `g0` then `g1`.
Rebuilt on `nucleon_word_letters`: deuteron 4.23e-01 -> **8.9e-14**, triton
-> 2.5e-11, both atoms landing on the canonical values (D `0.151968339`,
T `0.029144042`). All three assertions now pass. Fixed, committed.

The sibling that does NOT have the defect confirms the diagnosis:
`atom_nf_symbolic_D` calls `atom_braid_word_3A` directly, is not among the 18,
and closes to 3.44e-25.

## The detector

`computations/audits/intra_ordering_structural_assembly_audit.py`, registered
in `scripts/precision-gates.sh` as `intra-order assembly`, green on arrival.

- **A** grouped branch cloned as a concat — 11 sites (ratchet)
- **B** same assembly as sequential loops — 7 sites (ratchet)
- **C** a file that stamps `intra_ordering_frame` while hand-building the
  grouped word — **0, blocking**. This is the sharp one: the stamp is read off
  `atom_braid_word_3A`'s signature default, so it reports the frame the
  *production* builder considers canonical while the file built something else,
  and `canonical_trm_reference` trusts that field. A correct-looking stamp
  would defeat the guard `qou-y4gi` installed.
- **D** detector integrity — **blocking**. The A matcher is run against
  `nucleon_word_letters` itself and must fire on its grouped branch, so a
  rewrite there cannot retire this gate silently.

Self-test: 4 must-fire, 5 must-stay-quiet. Deliberately quiet on
`intra_order="grouped"` (asking by name is the declared, reviewable use) and on
order-insensitive bucket use — `vertex_volume(_PROTON_G0)`,
`len(g0) + len(g1)`, per-generator channel decompositions. ~30 live modules
import these constants and most never assemble a word.

## A third mechanism, not a duplicate

| bean | mechanism |
|---|---|
| `qou-cgyn` | per-generator **volume** route — the product of bucket volumes is order-blind, so it equals the grouped trace |
| `qou-y2o7` | `compute_tau_M_nucleon_H3` locked grouped by its monotone-only chi kernel; 18 consumers inherit |
| **this** | an ordered **word** hand-assembled from the buckets; 18 sites |

`qou-cgyn`'s domain is exactly what this audit's "NOT FLAGGED" list excludes —
the two are complementary, not contradictory.

## Correction to my own qou-4383 triage

Three qbeta probes I had filed as *hardcoded grouped values* awaiting an owner
call are on this list as *grouped assemblies*. That is a different defect with
a mechanical fix (call `nucleon_word_letters`), so they do not need the owner
call I said they did.

## The 18 sites

| file | line | check |
|---|---:|---|
| `computations/atom_orbit_reduction.py` | 92 | B |
| `computations/binding_canonical.py` | 381 | A |
| `computations/binding_multibond_wenzl.py` | 71 | B |
| `computations/chi_4he_binding_lossless.py` | 83 | B |
| `computations/closed_form_tau_M.py` | 564 | A |
| `computations/fitted_ideal_low_isotope_calibration.py` | 172 | A |
| `computations/legacy_marshalled_frame.py` | 87 | A |
| `computations/markov/d_frame_neutron_cyclotomic_rule_probe.py` | 121 | A |
| `computations/probes/b_pred_mirror_slope_closed_form.py` | 90 | A |
| `computations/qbeta/qbeta_chi_block_symbolic_closure_probe.py` | 79 | A |
| `computations/qbeta/qbeta_d_frame_baseline_element_consistency_probe.py` | 117 | A |
| `computations/qbeta/qbeta_d_frame_trace_baseline_probe.py` | 103 | A |
| `computations/qbeta/qbeta_delta_bar_parity_probe.py` | 184 | B |
| `computations/qbeta/qbeta_delta_element_fork_pricing_probe.py` | 181 | B |
| `computations/qbeta/qbeta_delta_vs_deltaTbeta_settled_probe.py` | 105 | A |
| `computations/qbeta/qbeta_epsnpq_functional_mismatch_probe.py` | 74 | A |
| `computations/qbeta/qbeta_level_k_binding_operator_probe.py` | 257 | B |
| `computations/rho_k_h3a_gg_trajectory.py` | 127 | B |

## Draining

Fix at the site, then `--rebaseline` to lower the ratchet. **Not uniform work:**
switching a site to the canonical ordering moves **absolute** traces (3.785x at
2H, 7.868x at 3H, 6.891x at 3He, 14.325x at 4He) while leaving log-ratios and
the three bond constants untouched, so each site needs reading for which kind
of quantity it reports before it is switched. `legacy_marshalled_frame` almost
certainly wants `intra_order="grouped"` **named**, not changed.

## Progress

**1 of 18 drained.** `legacy_marshalled_frame.legacy_marshal_intra` now calls
the new named API `pyhecke.atom.grouped_word_from_chains`, which
`nucleon_word_letters`' grouped branch also delegates to — one definition,
where before there were a dozen transcriptions and no API for a caller holding
chains rather than quarks. Values unmoved (proton 1.3215929842373446, neutron
1.2575579046963120). Ratchet 18 -> 17.

That site is the easy one: the module exists to BE the legacy frame. The
remaining 17 each need reading first, and check E exists so that converting one
to the named helper cannot be mistaken for fixing it.
