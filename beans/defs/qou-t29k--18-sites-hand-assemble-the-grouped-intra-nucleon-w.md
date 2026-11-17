---
# qou-t29k
title: '18 sites hand-assemble the grouped intra-nucleon word: a third mechanism, distinct from qou-cgyn and qou-y2o7'
status: in-progress
pr: 8344
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T06:35:57Z
updated_at: 2026-10-04T15:11:43Z
parent: qou-v2om
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

## 10 -> 9: `qbeta_level_k_binding_operator_probe` switched, and it surfaced a RED

First site where switching to the canonical ordering was the right call rather
than a deferral, and the first time this drain's falsification criterion fired:
I said I would report it if a site turned out safe to switch, and this one is.

`chain_word` built the grouped word by hand while its docstring called it
"`atom_braid_word_3A`'s own chain". Meanwhile `binding_block` in the SAME FILE
calls that production builder directly — so one probe measured A = 2
canonically and A = 3 in the superseded frame. Measured before switching:

    grouped    ord_spread = 22.54043935 %   ppn row = 0.2488, -6.581, -28.75
    borromean  ord_spread = 22.69262522 %   ppn row = 0.2488, -3.624, -2.978

Per-block characters move by up to an order of magnitude; the SPREAD — the
thing the function exists to measure — does not. Downstream assertion is a
threshold (`> 0.1`), satisfied either way. Switched to `nucleon_word_letters`'
DEFAULT rather than a named frame, so a future ruling reaches it by changing
one default. Module docstring literal 22.54 % -> 22.69 %.

**And the file is red on main, from the ordering ruling, unnoticed since
2026-09-05** — `qou-g5oz`. Both its headline assertions fail today on a clean
tree while its witness (2026-09-03, two days pre-ruling) still records
`allPassed: true`. Under canonical the largest binding character falls -9.598
-> 2.458 (under its own `> 5` bar) and the two small eigenphases do not exist
at all. Third frame-conditional result in this drain, after `qou-u8ji` and
`qou-y1w0`, and the first already RED rather than quietly wrong.

**Remaining 9:** `atom_orbit_reduction:92`, `binding_canonical:381`,
`binding_multibond_wenzl:71` (escalated), `chi_4he_binding_lossless:83`,
`fitted_ideal_low_isotope_calibration:172` (module PAUSED),
`probes/b_pred_mirror_slope_closed_form:90` (escalated),
`qbeta_delta_bar_parity_probe:184`,
`qbeta_delta_element_fork_pricing_probe:181`, `rho_k_h3a_gg_trajectory:127`.

## 9 -> 6: the last three tractable sites, and the shared-helper theory was WRONG

I expected `qbeta_net_trace_invariance_probe`'s shared helpers to force the
frame at the two delta probes, the way `chi_monotone_transfer` did for four
siblings. **They do not.** `_mult` multiplies `L[g] + d*ONE` in whatever order
it is handed and the regular-representation helpers are frame-agnostic, so
those two sites were genuinely undeclared choices — my stated falsifier, and it
fired. Recording it rather than inventing a constraint.

So I measured instead. Reordering the SAME symbols into the borromean word
(a permutation, so nothing depends on precision or q):

| probe | grouped | borromean | what moves |
|---|---|---|---|
| `qbeta_delta_bar_parity_probe` | 16/16 | **15/16** | `net_equals_tr_at_z_one_ONLY_when_e_minus_vanishes` |
| `qbeta_delta_element_fork_pricing_probe` | 15/15 | **13/15** | both `calibration_*` legs |
| `rho_k_h3a_gg_trajectory` | allPassed | **allPassed** | nothing asserted |

**Every substantive Delta-fork conclusion is frame-INVARIANT** — the two models
are different elements, the corpus counit and trace closed forms fail on the
long model and hold on the short one, chi^(2,1) vanishes on the short model
only, the phase identity, the bar-parity split, the fork surviving descent.
The fork — what `qou-cds1` / `qou-bg3w` are about — does not depend on the
intra ordering. That is a positive result, not just an absence.

**Disposition, three different answers for three sites:**

1. **The two delta probes: DECLARED grouped.** Their calibration legs check
   against committed grouped-era witnesses and published values, so they are
   frame-bound by construction — the same reason their settled sibling chose
   grouped deliberately. Switching would break the calibration without changing
   a finding. Both re-run 16/16 and 15/15 with every measured value
   byte-identical.
2. **`rho_k_h3a_gg_trajectory`: SWITCHED.** Its docstring claimed "the canonical
   word" and delivered grouped. Uniquely here the ordering IS the subject —
   every prefix is one gg-pair EVENT, so the trajectory is the letter sequence,
   and the grouped bucketing has no physical reading while the borromean word
   does (confinement core, then quark pairs, then gluons). Closure holds either
   way (p 2.673e-51 -> 0.0, n 1.336e-51 -> 6.682e-51, LP gaps 0.0 throughout),
   so **no assertion in that file discriminates** — the per-step trajectory
   changes and nothing checks it, which is why re-running could never have
   caught this one. Checked first that the two interpreting documents quote no
   per-step sequence.
3. One real content finding fell out: **`qou-epmq`** — `Delta_L`'s `e_minus`
   coordinate is 0 grouped and `-(q^2-1)^2 Phi_12(q)^2 / (2 q^6)` canonical, so
   `net` and `tr_M(z=1)` stop coinciding on the long model. The vanishing was a
   property of the grouped word, not of the element.

**Remaining 6, of which only 3 are actionable:** `atom_orbit_reduction:92`,
`binding_canonical:381`, `chi_4he_binding_lossless:83`. The other three are
`binding_multibond_wenzl` (escalated, `qou-y1w0`),
`b_pred_mirror_slope_closed_form` (escalated, `qou-u8ji`) and
`fitted_ideal_low_isotope_calibration` (module PAUSED by owner ruling
2026-08-26).

## 6 -> 4: `chi_4he_binding_lossless` SWITCHED, `binding_canonical` DECLARED

**`chi_4he_binding_lossless` — switched, and this is the cleanest verification
in the whole drain.** `_hp_binding_word` claimed to mirror `atom_braid_word_3A`
and did on every axis but the one it did not name: its interfaces already
matched (p-p `sigma`, n-n `sigma - h`, p-n colour-weighted), and only the intra
ordering was grouped. The claim is true now.

Safe to switch, checked first rather than assumed: the single assertion
`mpfr_binding_chi_extends_f64_atomic` compares MPFR against f64 for the SAME
word, so it moves with the word; and nothing consumes the per-λ table — the only
other file naming the cache is `f64_into_mpmath_audit.py`, matching on filename.

Re-ran (874 s, 77/77 λ⊢12, f64 gate max rel 1.1157e-14, PASS):

    committed (grouped)  tr_M = 0.160974145442407381825873440980716...
    after switch         tr_M = 0.011237417659767421564199549374410...

Both land exactly on the known constants — the grouped ⁴He pin and the
canonical ⁴He pin — and their ratio is **14.3248**, precisely the documented
⁴He absolute-trace factor. End-to-end confirmation that the switch did what it
was supposed to and nothing else.

**NOT the staleness `qou-92u9` tracks**, and worth keeping distinct: those six
caches come from `chi_at_q0_via_hoefsmit_mpfr.py`, which calls
`atom_braid_word_3A` with no `intra_order`, so a fresh run there is already
canonical and the artifact is merely old. This one hand-built the word, so no
re-run could ever have corrected it. That bean records this producer only as a
665 s runtime observation, never as a defect.

**`binding_canonical:381` — declared, not switched.** Two reasons, the first
decisive: below the site, `tr_free = tau_p^Z tau_n^N` and `tr_atom =
closed_form_tau_M(..., tau_p, tau_n)`, so the ratio is `prod f_i(q)` and **the
taus cancel in everything that survived the refutation** — the bond factors
b_pp / b_pn / b_nn are tau-independent, and the live law is the log-RATIO
`B = E_0 log(tr_free/tr_atom)` in `binding_log_free_energy.py`. Only
`Delta_tr = tr_free - tr_atom` scales with them, and that is the REFUTED law
this module is marked "do not quote" for. Second: re-framing a superseded
provenance number makes it stop matching the record it exists to preserve — the
header's 1592x residual spread was measured against these values. Verified a
no-op: word byte-identical, tau_p = 1.145759692457300869689 unchanged.

**Remaining 4, only 1 actionable:** `atom_orbit_reduction:92`. The other three
are the two escalated owner calls (`qou-y1w0`, `qou-u8ji`) and the module PAUSED
on 2026-08-26.

### What `atom_orbit_reduction` needs, for whoever picks it up

The module is internally SPLIT and that is the finding:
`atom_braid_orbit_representative` **delegates to the canonical
`atom_braid_word_3A`** (so `orbit_reduction_crosscheck`'s byte-identity assert
`rep.word == atom_braid_word_3A(Z, N)` holds), while `atom_braid_word_ordered`
— the sibling that takes an arbitrary nucleon ordering, which
`atom_braid_word_3A` cannot express — is hand-built grouped. Same inconsistency
`level_k` had, and the same likely fix.

Its one real consumer of the ordered builder,
`probes/canonical_ordering_dof_probe`, uses it for RATIOS across four nucleon
orderings (`npn/pnn`, `pnp/ppn`), all four in the same frame — so the frame is a
controlled constant there, as it was for `level_k`'s `ord_spread`. Measure those
two ratios both ways before switching; `level_k`'s moved only 22.54 % -> 22.69 %.

## 4 -> 3. THE ACTIONABLE DRAIN IS COMPLETE.

`atom_orbit_reduction:92` switched. All three remaining sites are blocked on
decisions that are not mine:

| site | blocked on |
|---|---|
| `probes/b_pred_mirror_slope_closed_form:90` | owner call, `qou-u8ji` |
| `binding_multibond_wenzl:71` | owner call, `qou-y1w0` |
| `fitted_ideal_low_isotope_calibration:172` | module PAUSED, owner ruling 2026-08-26 |

**18 -> 3 over the arc**, none of it by re-running: every site was read for what
it reports, and the disposition was measured before it was made.

### The last switch, and why it was the safest of them

The module was internally SPLIT. `atom_braid_orbit_representative` — and so
`tr_M_via_orbit_representative`, and so every assertion in
`orbit_reduction_crosscheck` — already DELEGATED to the production
`atom_braid_word_3A` and was always canonical. Only `atom_braid_word_ordered`,
the sibling taking an ARBITRARY nucleon ordering that `atom_braid_word_3A`
cannot express, was hand-built grouped. Two halves of one module in two frames.

Its one real consumer, `probes/canonical_ordering_dof_probe`, reports ratios
across four nucleon orderings, and those are **exactly** invariant:

    T_npn_over_pnn     1.258976624909173     both frames, every digit
    He3_pnp_over_ppn   0.8293909084880151    both frames, every digit

while the absolute traces move by 7.868x (|tr| npn 0.2886552152 ->
0.03668647715), precisely the documented ³H factor. Exact rather than
approximate because `npn` and `pnn` carry the same nucleon multiset, so the
per-nucleon intra factor divides out — contrast `level_k`'s analogous spread,
which moved 22.54 % -> 22.69 %. Post-switch the word is length 35 with
generator sequence [0,1,0,1,0,1,0,0,1,0,0,2], the borromean interleave plus the
interface.

The **colour convention** at that site is still `strict_averaged` (colour-blind
`-h/2`) against the canonical `bring_color_weighted`. That is a different owner
ruling (2026-08-15) and a different axis from this bean; left as it was, and
now said so in the docstring rather than fixed in passing.

### Two pre-existing reds found next to it, both verified on a clean tree

Neither is from this work and neither is a `qou-t29k` defect:

  * `orbit_reduction_crosscheck` FAILS `N2_he4_value_smoke` — reads the
    canonical ⁴He `0.011237417659767421` against a pin of
    `0.0553483351637685668` whose witness (2026-05-30) still says
    `allPassed: True`. Bean `qou-uujo`. Its code is right; the pin is stale,
    and is not the grouped value either, so re-pinning needs that number's
    provenance checked.
  * `canonical_ordering_dof_probe` CRASHES in Part 6,
    `TypeError: cannot create mpf from None`. Part 6 is already tracked as
    blocked by `qou-xy5f`.

Because both consumers are red for unrelated reasons, the switch was verified
directly instead — ratios, absolute traces and word structure all as predicted
above.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (PR #8344)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`291dd36ab34a42866efb444b586e05f0b621971e` -> `38f4a86a95df28f43dea57e331b0e3b812f7f526`) in PR #8344.
