---
# qou-pin2
title: 'Producers reading BOTH q0 layers: 3 IMPLICIT crossings stamped proton are the real hazard (explicit q_muon_at probes ruled OK)'
status: completed
type: task
priority: normal
created_at: 2026-08-08T19:30:00Z
updated_at: 2026-08-08T20:45:00Z
---

> **🟧 OWNER RULING 2026-08-08 — explicit comparison probes are OK.** A producer
> that imports `q_muon_at` alongside `q_at` is reaching for the ideal layer
> **deliberately**, and the crossing is visible by construction. Those are
> legitimate cross-anchor comparisons, NOT straddles, and must not be
> "fixed". The classifier now scores `q_muon_at`/`Q_MUON` as muon evidence so
> they classify as BOTH and are excluded from any migration batch — without
> that, ~8 of them would have been swept into the tnjb regeneration.
>
> **The remaining hazard is the IMPLICIT crossing**: a hardcoded muon 50-digit
> literal, or a read of a cached muon witness, inside a producer computing at
> the proton pin. There the layer boundary is crossed with no signal — exactly
> what AGENTS.md §q₀-anchor describes for the `y_lambda_at` accessor. Triage
> below is re-scoped to those.

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

**Per the owner ruling, start with the three IMPLICIT crossings stamped
`proton`** — they read muon-layer data under a proton label with no explicit
accessor to signal it, which is the `qbeta-ck-cache` shape exactly.
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


## RESOLVED 2026-08-08 — all three IMPLICIT crossings handled

**1. `delta_lambda_fr_identity_phase5c.py` — a LIVE straddle, fixed.**
It set `q` from `q_parameter.Q` (proton for this stem) and then loaded
muon-built `y_λ` from `y-lambda-at-q0.witness.json`, forming
`τ_M(β) = Σ_λ y_λ·χ_λ(β)` -- muon `y_λ` against proton `χ_λ`, inside one
quantity. Exactly the μ₃ Fréchet defect AGENTS.md documents, and invisible
because the witness is stamped `proton`.

Fixed with the remedy that section prescribes: `y_lambda_at_q0_mpmath(n, Q0)`
live at the producer's own q₀ instead of the cached witness.

The proof it was real: the Markov-interface identity `τ_M = z^p (z-h)^n` is
EXACT algebra, so its residual should be machine zero. It wasn't --

    atom   BEFORE (straddled)   AFTER (single-layer)
    D      2.39e-08             4.12e-16
    T      6.65e-08             9.58e-16
    3He    4.79e-08             6.53e-16
    4He    9.04e-08             1.19e-15

-- the straddle was injecting ~1e-8 (the 11.5 ppb μ-p separation) into an exact
identity. Residual improved 7.6 MILLION-fold. Largest substantive field shift
was 1.402e-07, matching AGENTS.md's ~1e-7 prediction for this separation.
allPassed True before and after: it was PASSING, 8 orders worse than it should.

**2 + 3. `t25_cinquefoil_deltalambda_sign_probe.py`, `zhabiro_phiq_wiring.py`
-- a DIFFERENT class: cross-layer FALLBACKS.** Their primary path is proton
(`q_at`); the `except` handler substituted a hardcoded MUON literal. So on any
import hiccup they compute at the ideal pin under proton labelling, silently.
zhabiro's own comment declared the q₀ "proton-pinned" while falling back to a
muon value labelled only "literal fallback". Both now raise instead.

That class generalises: `q0_cross_layer_fallback_scan.py` (new) finds **29**
such files. 27 remain -> bean `qou-pin4`, along with 3 TRANSITIVE straddles
(both layers via different helpers, invisible to a file-local scan).
