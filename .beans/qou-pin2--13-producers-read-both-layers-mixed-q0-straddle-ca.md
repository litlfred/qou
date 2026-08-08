---
# qou-pin2
title: '13 producers read BOTH q0 layers — mixed-layer straddle candidates (8 with hard code evidence)'
status: todo
type: task
priority: normal
created_at: 2026-08-08T19:30:00Z
updated_at: 2026-08-08T19:30:00Z
---

Surfaced by `computations/audits/q0_producer_pin_classifier.py`. Each of these
reads a **stem-resolved** `q₀` (via `q_parameter` / `qou_substrate.constants`)
**and** a muon-layer artifact in the same producer — the straddling hazard
AGENTS.md §q₀-anchor names ("never straddle the two layers inside one
quantity"). The `qbeta-ck-cache` instance fixed on 2026-08-08 was worth
**30.4 ppb** on Q_β, so these are worth checking individually.

**NOT fixed here.** Resolving each one means deciding which layer the computed
quantity belongs to — that is the `tnjb` migration decision, per-quantity, and
it is explicitly not an idle-drain sweep. Filed with evidence so the decision
can be made once per producer.

## Hard code evidence (8) — a literal muon 50-digit or a muon witness read

| producer | evidence | witness pin |
|---|---|---|
| `delta_lambda_fr_identity_phase5c.py` | `q_parameter.Q` + reads `y-lambda-at-q0.witness.json` | **proton** |
| `t25_cinquefoil_deltalambda_sign_probe.py` | `q_at` + hardcoded muon 50-digit + `q-pinning-50-digit` | **proton** |
| `zhabiro_phiq_wiring.py` | `q_at` + hardcoded muon 50-digit | **proton** |
| `zhabiro_phiq_production_crosscheck.py` | `q_at` + hardcoded muon 50-digit | muon |
| `flavor_split_alpha_bond_dilog_probe.py` | `Q_50_DIGIT_STR` + hardcoded muon 50-digit | muon |
| `flavor_split_alpha_dilog_expansion_probe.py` | `Q_50_DIGIT_STR` + hardcoded muon 50-digit | muon |
| `lever1_binding_core_characterization.py` | `.Q_MP` + hardcoded muon 50-digit | muon |
| `lever1_binding_habiro_single_element_test.py` | `.Q_MP` + hardcoded muon 50-digit | muon |

**Start with the three stamped `proton`** — those read muon-layer data under a
proton label, which is the `qbeta-ck-cache` shape exactly.
`delta_lambda_fr_identity_phase5c` is the sharpest: it reads
`y-lambda-at-q0.witness.json`, which is precisely the accessor AGENTS.md §q₀-anchor
flags as reaching an experimental-layer caller **with no signal that a layer
boundary was crossed**. Suggested fix per that section: call
`schur_principal_mpmath.y_lambda_at_q0_mpmath(n, q)` (live closed form) instead
of the cached witness.

## Weak / likely false positives (5) — matched on docstring text only

`alpha_k_macdonald_closed_form.py`, `binding_qgaussian_ell1_ceiling_measurement.py`,
`deltalambda_binding_a_scaling_probe.py`, `deltalambda_o1_manybody_probe.py`,
`y_lambda_at_q0_cache.py`.

The classifier matches muon-artifact names anywhere in a string constant, so a
producer that merely *mentions* `y-lambda-at-q0` in its docstring trips it.
`y_lambda_at_q0_cache.py` is the clearest false positive — it **is** the muon
cache producer, so naming its own output is not a straddle. Confirm by reading
before acting; do not treat these five as defects on this evidence alone.

**Known classifier limitation, stated rather than hidden:** string-constant
matching does not distinguish a docstring from a live path argument. Tightening
it (match only strings reaching an `open`/`load_witness` call) is a worthwhile
follow-up and would cut this false-positive class.
