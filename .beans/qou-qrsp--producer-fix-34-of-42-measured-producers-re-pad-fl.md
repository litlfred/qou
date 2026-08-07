---
# qou-qrsp
title: 'PRODUCER FIX: 37 of 45 measured producers re-pad float64 on re-run (qou-gqt5 follow-up)'
status: todo
type: task
priority: high
created_at: 2026-08-07T09:01:16Z
updated_at: 2026-08-07T09:09:03Z
---

Follow-up to qou-gqt5 (parent-less: beans disallows task-under-task).
MEASURED, not assumed -- docs/audits/2026-08-07-producer-repadding-empirical-sweep.md
Tool: computations/producer_repad_sweep.py (reproducible; detached worktree).

Commit 4aa48b63 stripped 58 witnesses (452 -> 13 padded fields). The strip is
value-preserving but NOT durable: re-running the producers regenerates 289 of
those fields in ONE pass. 37/45 measurable producers re-pad (82%); 8 could not
be measured at all and are NOT clean.

Consequence, and why this is high priority: the strip drains the ratchet BASELINE
while leaving the defect intact. The gate reads green, the producers still emit
fake precision, and the next routine re-run silently re-pads with no signal. This
is the hand-edit branch of what qou-gqt5 explicitly prescribed ("fix producers to
carry values as strings then re-run -- never hand-edit").

Clean (8, leave alone): binding_a3plus_joint_ji_combiner,
binding_block_multiplicative, binding_depth_stratified, meson_gen3_eta_phi,
probe_k_ud_bring_color_tube_empirical_baseline, probe_k_ud_fractional_and_alt_ansatz,
qbeta_habiro_element_probe, su2_spinor_multiplicity_resolution.
Heaviest re-padders: the qbeta_* and option_e_* families.

Known mechanism -- the mpf(<float-valued NAME>) blind spot, which the source
detector (23075055) documents it cannot catch. Live instance,
binding_factor_f_sequence.py:76:  return mpf(tf) - mpf(ta)   # tf, ta are floats

NOT MECHANIZABLE -- per-file judgment. For each re-padder decide whether the
quantity is GENUINELY float64 (then stop promoting it to mpf) or was DOWNCAST
upstream from full precision (then padding is a symptom and the real defect is the
lost precision). Guessing wrong either fakes precision or hides a real loss. This
is the part worth fanning out across agents; the strip was not.

Blocked in part by qou-wu80 (stale folio-assistant path) and qou-dgkf
(pyhecke_native has no wheel) -- both hide producers from measurement.

## Measured at the source (PR #4677) — "NOT MECHANIZABLE" was half wrong

The localization IS mechanizable: `computations/float64_entry_tracer.py`
patches mpmath's `from_float`/`from_npfloat` and reads off the source line
where a float64 enters. The *judgment* above stays per-file; the hunting does
not. Re-measured: RE_PADS 19 / 228 fields (was 20/229 — the delta is exactly
the one gt_matrix fix). 18 traced, `rho_k_co_casimir_extended` (+71) still
exceeds a 900s budget and is NOT measured.

- **A — float64 really enters (9 producers, 118 fields).** Three idioms, not
  nine investigations: one shared library downcast
  (`hecke/hecke_characters.py:214`, hit 527310x by su4), `mpf(<float out of
  JSON>)` across four producers, and `mpf(<float-valued name>)` — including
  the `binding_factor_f_sequence.py:76` instance this bean already names.
  The largest (chirality, 71) is DELIBERATE f64 — Rust kernel called with
  `precision="f64"`, witness records `kernel_precision: f64` — so the fix is
  to stop serializing 53 bits at 50 dps. Two sites are comparison tolerances
  and must not move.
- **B — no float64 enters at all (9 producers, 39 fields).** Their values are
  genuine computations of exact integers (tr_M(1) = 1 - 1.4e-51). Flagged
  because `is_f64_padded` catches anything within 1e-30 of a double, and so is
  a real padded value truncated at 50 dps (1.56e-50). No static test separates
  them. These need no producer fix.

**`propagated = 0` is refuted.** qbeta_markov_trace_compute_accuracy_diagnostic
regenerates a string already committed verbatim in
qbeta-markov-trace-norm-probe.witness.json. That classifier was never committed
with its claim, so it was never reproducible — the propagated class is
unmeasured, not zero, and an exact-string search over the POST-strip corpus is
biased toward LOCAL by construction.

Next: measure rho_k_co_casimir_extended; re-measure LOCAL vs propagated with a
committed tool; fix the two library-level Class A idioms (source fix and
witness regeneration as separate commits — they change numbers).

## CORRECTION to the section above: `propagated = 0` was NOT refuted

The claim above that `propagated = 0` is refuted was **wrong** and is retracted.
It rested on grepping a worktree this session had itself been running producers
in — the "upstream" witness holding the padded string was this session's own
regenerated output, not the committed corpus. `git show HEAD:` shows only the
short form. That is the failure `producer_repad_sweep.py` warns about in
capitals, committed while cataloguing the same habit in others.

Measured properly with a committed tool
(`computations/witness_padding_provenance.py`, indexes the COMMITTED corpus
before anything runs, excludes the producer's own fresh output), over all 19
re-padders / 218 padded fields:

  VERBATIM_UPSTREAM        0   <- the exact-string result is CONFIRMED
  VALUE_UPSTREAM          37   <- distinctive value upstream, invisible to it
  VALUE_UPSTREAM_ROUND    15   <- matched 1.0/6.0; vacuous, not propagation
  LOCAL                  166

So `propagated = 0` is right about strings and 17% short about values. The
round-number split is load-bearing: without it the gap_a4 near-integers read as
inherited only because `1.0` is everywhere.

The two tools agree and were built independently: where the tracer finds a
local float64 entry, provenance says LOCAL (chirality 71/71); where it finds
none, the value is upstream (qbeta diagnostic 7/7).
