# Regeneration queue — producers edited while the nuclide table held the checkout

Two producers must never run at once in this checkout (bean `qou-uiut`); the
hadron table saturates four cores and shares `.work/kernel-memo`. So a source
fix made while it runs leaves its witness stale by construction. This file is
that debt, written down rather than remembered.

Drain it at the next idle window — the container suspends the table roughly
every 25-45 minutes, and the checkpoint survives, so idle windows are frequent.
Run each ONE AT A TIME, then `scripts/hkt-resume.sh --commit` to put the table
back.

## Owed

| producer | why | bean |
|---|---|---|
| `computations/probes/cumulant_hierarchy_does_not_converge_probe.py` | description now DERIVES every measured number; it had drifted (`2.7e-15` prose vs `1.78e-15` data) | `qou-n62l` |
| `computations/binding_hbarq_rung_forward_test.py` | emits `mass_mult_vs_lambda_A_gap_pct` + `mass_mult_times_hbar_q_sq`, the derived quantities its prose already quoted | `qou-n62l` |
| `computations/phase3_triton_binding_convention_b.py` | NO-FLOAT64 fixed in code 2026-09-03; witness still carries the 25 raw-float64 fields | `qou-qe81` |
| `computations/sweeps/paper_six_term_isotope_sweep.py` | returns EMPTY instead of raising; committed witness still has 12 `FileNotFoundError` rows | `qou-qe81` |
| `computations/probes/symbolic_nf_q_degree_magic_probe.py` | revived by the qou-sidu fix, exceeded 900 s — needs a dedicated long run | `qou-sidu` |
| `tools/pyhecke/python/pyhecke/atom.py` | last `mp.mpf(repr(` site; it is a CHECKPOINT-KEY file, so editing it discards the table's completed atoms | `qou-gxsd` |

## Confirm-only — SETTLED 2026-09-07, no run owed

`a-K-via-lp-dual-hecke-basis`, `he-nu-sdp-saturation-obstruction`,
`markov_weights_symbolic`, `binding-closed-form-c-vs-d`,
`binding-production-route-c-vs-d-deut`, `binding-sum-c-vs-d-deut`.

These were taken as OURS in the 59-commit merge and listed here to confirm by
re-running. **Answered statically instead, so no producer time is spent.**

Main changed 17 `.py` files in those 59 commits. Transitive first-party import
cones (built with `witness_import_cone_staleness_audit.import_cone`, 20-57
modules each) intersect that set in **exactly one file for all six**:
`tools/qou-substrate/python/qou_substrate/witness.py`.

And main's change to it is
[`stamp_staleness_metadata`](../tools/qou-substrate/python/qou_substrate/witness.py)
gaining `payload.setdefault("scriptFile", os.path.basename(spath))` — bean
`qou-4383`. Metadata, no numeric path, and a **`setdefault`**, so a caller
that already named its producer keeps its own value. All six witnesses
already carry `scriptFile`:

    aK_via_lp_dual_hecke_basis.py          he_nu_sdp_saturation_obstruction.py
    markov_weights_symbolic.py             binding_closed_form_C_vs_D_probe.py
    binding_production_route_C_vs_D_probe.py
    binding_sum_C_vs_D_per_isotope_probe.py

so the change is a no-op for every one of them. **Nothing moves; taking OURS
was correct and needs no confirmation run.**

Method note for the next merge: this is cheaper and stronger than re-running.
Cheaper because it costs a cone walk instead of six producer runs; stronger
because a re-run that reproduces the numbers only shows the numbers did not
move *this time*, whereas the cone intersection shows *why* they cannot have.

## Blocked, not owed

`qbeta_computable_observables_vs_row_cap_probe` and
`qbeta_derived_w_overdetermined_test_probe` cannot run at all —
`RuntimeError: tr_m_word_lq: Case C (multiple top-1 in segment) not
implemented`. Pre-existing kernel gap, documented in the second probe's own
docstring. Not a regeneration problem.
