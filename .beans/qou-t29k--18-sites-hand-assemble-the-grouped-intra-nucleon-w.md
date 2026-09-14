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

## One site is EXCLUDED pending an owner call — `qou-u8ji`

`probes/b_pred_mirror_slope_closed_form.py:90` is not drainable mechanically.
Its headline result — the framework half of the writhe coefficient kappa,
`plateau = log_q0(tau_p/tau_n)` — holds **only** in the grouped ordering:

| ordering | plateau | kappa_FW |
|---|---|---|
| grouped (as committed) | 1.4223 | -0.3556 |
| borromean (canonical) | **2.6936** | **-0.6734** |

against a measured mirror slope of 1.372. Canonical overshoots by 96 %, and
`kappa_AME` — the piece attributed to experiment — flips from -0.094 to +0.236.

`tau_p/tau_n` is a ratio between two DIFFERENT nucleons, so it is not in the
ordering-invariant class that `nucleon_word_letters` documents (that covers
`tr_M(W_atom)/tr_M(W_free)`, one nucleus over its own free word). Left
unswitched; picking the ordering that matches would be selection against the
target. See `qou-u8ji`.

**This is the general lesson for the remaining 16.** "Call
`nucleon_word_letters`" is the mechanical shape of the fix, but each site has
to be read for what it reports first — some will move a claim, not just a
number.

## Triage, 2026-09-14 — 16 unguarded, 1 guarded, 2 excluded

The audit now separates a DECLARED legacy branch from a silent default (the
nearest enclosing `if` whose test names the ordering). Measured: **16 unguarded,
1 guarded**. The guarded one, `closed_form_tau_M:564`, was already correct
(`intra_order` defaults to borromean, grouped arm opt-in, resolved under
`qou-y2o7`) and is now drained to `grouped_word_from_chains` — ratchet 17 -> 16,
E 1 -> 2, both arms byte-exact.

**Two of the sixteen are excluded pending an owner call**, and they are the only
two I have examined in depth:

| site | route | grouped | canonical | bean |
|---|---|---|---|---|
| `b_pred_mirror_slope_closed_form:90` | ratio `tau_p/tau_n` | 1.4223 vs measured 1.372 | 2.6936, +96 % | `qou-u8ji` |
| `binding_multibond_wenzl:71` | difference `tr_vac - tr_b` | B(2H) -6.3 % vs AME | -75.2 % | `qou-y1w0` |

Two for two. That is not a corpus-wide claim — fourteen remain unexamined and
these two looked the most likely to be interesting — but it settles that this
drain is not code hygiene.

**The triage question for the remaining fourteen** is which class the reported
quantity is in. `nucleon_word_letters` documents invariance only for
`tr_M(W_atom)/tr_M(W_free)`, one nucleus over its own free word. Ratios between
different nucleons, differences of traces, and absolute traces all move. A site
is safe to switch iff it reports only the first kind — answerable by reading it,
not by re-running it.

## Triage map, 2026-09-14 end of session — 18 -> 14, four drained, two escalated

**Drained (4, all zero numeric change, all verified by re-run):**

| site | why it was safe |
|---|---|
| `legacy_marshalled_frame:78` | the module exists to BE the legacy frame |
| `closed_form_tau_M:564` | already opt-in behind `intra_order`, defaulted borromean (`qou-y2o7`) |
| `markov/d_frame_neutron_cyclotomic_rule_probe:121` | the measured `(m, cancelled)` is ordering-INVARIANT — established by the probe's own stale assertion, see below |
| `qbeta/qbeta_delta_vs_deltaTbeta_settled_probe:105` | grouped is reasoned and dated (2026-09-06); it already passes `intra_order="grouped"` to its sibling call |

**Escalated, NOT switched (2):** `b_pred_mirror_slope_closed_form` (`qou-u8ji`)
and `binding_multibond_wenzl` (`qou-y1w0`). Both have agreement with experiment
that exists only in the grouped frame.

**Remaining 12, with what is known:**

*Six qbeta probes* — `qbeta_chi_block_symbolic_closure_probe:79`,
`qbeta_d_frame_baseline_element_consistency_probe:117`,
`qbeta_d_frame_trace_baseline_probe:103`, `qbeta_delta_bar_parity_probe:184`,
`qbeta_delta_element_fork_pricing_probe:181`,
`qbeta_epsnpq_functional_mismatch_probe:74`. All compute
`chi_lambda(beta_n) - chi_lambda(beta_p)` — the Delta element as a
CROSS-NUCLEON DIFFERENCE, so **not** in the invariant class. **None of the six
mentions `intra_order` and none carries a grouped pin literal**: their frame is
inherited from the `_word` shape, undocumented, and possibly accidental. Their
sibling `qbeta_delta_vs_deltaTbeta_settled_probe` reasoned the same choice out
in forty lines; these six did not. Only `qbeta_chi_block_symbolic_closure_probe`
references the `paper` closed forms, which the settled probe says are stated in
the grouped frame — so that one likely NEEDS grouped and merely fails to say so;
the other five are open.

*`qbeta/qbeta_level_k_binding_operator_probe:257`* — same cluster, marked 🛑 in
its own docstring; not read yet.

*`binding_canonical:381`* — the module is marked "🛑 SUPERSEDED LAW ... kept for
provenance and comparison; do not quote". Likely legacy-by-design, but it is
production-adjacent and wants reading, not assuming.

*`fitted_ideal_low_isotope_calibration:172`* — module PAUSED by owner ruling
2026-08-26. Do not touch without unpausing.

*`atom_orbit_reduction:92`*, *`chi_4he_binding_lossless:83`*,
*`rho_k_h3a_gg_trajectory:127`* — unexamined.

## What the triage method turned out to be

Not "is the site broken" but **which class is the reported quantity in**:

  1. `tr_M(W_atom)/tr_M(W_free)`, one nucleus over its own free word —
     INVARIANT (documented in `nucleon_word_letters`, ~1e-60 at A = 2, 3, 4).
     Covers `L` and the three bond constants.
  2. A functional that is invariant for a different reason — the cyclotomic
     `(m, cancelled)` is, because it counts per-GENERATOR content and
     reordering moves no letter between generators.
  3. Everything else — absolute traces, differences of traces, ratios between
     DIFFERENT nucleons. These move by 3.785x (2H) to 14.325x (4He).

Classes 1 and 2 are safe to switch; class 3 needs an owner call whenever the
site's result is a claim rather than a number. Both escalations are class 3.

## 18 -> 10, and the qbeta cluster was misdiagnosed as "silent"

Four more drained: `qbeta_d_frame_trace_baseline_probe`,
`qbeta_epsnpq_functional_mismatch_probe`,
`qbeta_d_frame_baseline_element_consistency_probe`,
`qbeta_chi_block_symbolic_closure_probe`. All four pass every assertion with
every measured value unchanged (4/4, 7/7, 5/5, 9/9).

They are **not** silent defaults. All four use
`chi_monotone_transfer.chi_all_lambda`, which accepts only a monotone
generator sequence, and the canonical borromean word is non-monotone by
construction. Measured:

    grouped   [0,0,0,0,0,0,0,1,1,1,1] -> OK, chi_(3) = 1.38249446339
    borromean [0,1,0,1,0,1,0,0,1,0,0] -> ValueError: non-monotone word:
                                          gen 0 after 1

So grouped is **forced by the kernel**, and these are the SAFEST sites in the
baseline, not the riskiest: a monotone-kernel caller cannot silently report a
wrong-frame number — it either uses the grouped word correctly or raises. The
declaration is what was missing, not the correctness. Each docstring now says
so, and `qou-11l4` records that `qou-y2o7` — whose mechanism this is — closed
as completed without these four in its blast radius.

`qbeta_chi_block_symbolic_closure_probe` holds the QUARKS, so it now calls
`nucleon_word_letters(..., intra_order="grouped")` rather than
`grouped_word_from_chains`: same object, one caller closer to the definition.

Ratchet 14 -> 10. E 4 -> 7.

**Remaining 10**, none of them kernel-locked: `atom_orbit_reduction:92`,
`binding_canonical:381`, `binding_multibond_wenzl:71` (escalated, `qou-y1w0`),
`chi_4he_binding_lossless:83`, `fitted_ideal_low_isotope_calibration:172`
(module PAUSED by owner ruling), `probes/b_pred_mirror_slope_closed_form:90`
(escalated, `qou-u8ji`), `qbeta_delta_bar_parity_probe:184`,
`qbeta_delta_element_fork_pricing_probe:181`,
`qbeta_level_k_binding_operator_probe:257`, `rho_k_h3a_gg_trajectory:127`.

The three remaining qbeta probes do NOT import `chi_monotone_transfer`, so
whatever forces their frame is something else and has to be found per site.

## Environment note

The container restarted mid-session and came back with mpmath 1.3.0 -> 1.4.1
and a rebuilt `pyhecke_native`. Every witness regenerated after that carries
the new provenance. All four probes above produced byte-identical values
across the change, so it is benign so far, but it is a corpus-wide provenance
shift that did not come from any commit.
