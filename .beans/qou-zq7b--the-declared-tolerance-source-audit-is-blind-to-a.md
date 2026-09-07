---
# qou-zq7b
title: The declared-tolerance source audit is blind to a tolerance passed as a VARIABLE
status: completed
type: task
priority: normal
created_at: 2026-09-05T09:52:42Z
updated_at: 2026-09-05T09:59:22Z
---

## What is open

`computations/audits/tolerance_guard_bypass_audit.py` pass 2 runs
`ast.literal_eval` on the token after `"tolerance":` and skips anything that is
not a literal. A producer whose assertion helper takes `tolerance` as a
**parameter** is therefore invisible to it, however many floats reach it.

## Why this is not hypothetical

On 2026-09-05, `3277607d39` re-ran `qbeta_ck_qholonomic_recurrence_test.py` on
`main`; its `gate(name, passed, computed, expected, tolerance, source)` helper
re-emitted `1e-45`, `1e-12` and `1.1` as floats, undoing PR #5910's drain for
that file. **Pass 2 had reported the corpus LATENT-free at the time.**

Pass 1 (the artifact scan) caught it — LIVE-DIRTY 1 — as did the raw-float64
ratchet independently, REGRESSED `65 -> 67`. That is the division of labour the
two passes exist for: the artifact check is the guarantee, the source check is
only the early warning, and the early warning is the half that failed.

Producer + artifact fixed in #6760 (`9ad50d8d9c`). This bean is the DETECTOR.

## Measured surface (2026-09-05, `main` after #6760)

**16** hand-building files (`json.dump`, no `declared_tolerance` import) pass a
non-literal tolerance. Most are already safe and must not be flagged:

- `mp.nstr(TOL, …)`, an f-string, and `str(t)` all yield **strings**;
- two hits are these audits' own docstrings.

About **five** pass a bare name that could be a float —
`m_tau_complex_volume_search`, `lw2_c2_independent_hopf_test_attempt`,
`he4_binding_k_presentation_correction_probe`,
`qbeta_habiro_integrality_kill_test`, `aoperator_a5_crosscheck`. **Pass 1
reports all five clean today**, so this is prevention, not a live dirty count.

## The trap to avoid building

A detector that flags all 16 would add eleven false positives to the one number
this audit exists to keep honest — the same failure the taxonomy catalogues, and
the reason it was deliberately NOT built inside #6760. It must key on what the
helper's call sites actually pass (resolve the parameter to its arguments, and
recognise the string-producing wrappers), not on "the token is not a literal".

## Also to fix here

`tolerance_guard_bypass_audit.py`'s new blind-spot section says *"Tracked in
bean `qou-9tqx`"*. That bean is **completed**, so an open item points at a
closed bean. Retarget it to this one.

## BASELINE (2026-09-05, main `9ad50d8d9c`)

    PYTHONPATH=computations:tools/qou-substrate/python \
      python3 computations/audits/tolerance_guard_bypass_audit.py --strict

  -> exit 0; 3250 witnesses; LIVE-DIRTY 0; LATENT 0; UNRESOLVED 4.


---

## CLOSED — `_source_unguarded_param`, PR #6816

The detector resolves rather than pattern-matches, in three steps: an f-string
or a call to a stringifier (`str`/`repr`/`format`/`mp.nstr`) is SAFE; a
parameter is resolved to its function's **call sites** and each argument
literal-eval'd, flagged only when a call site actually passes a value the guard
would change; a name bound to a literal resolves to that literal. Anything
computed is left **unreported** rather than guessed.

**The stringifier rule is the whole design.** 11 of the 16 non-literal sites are
already safe for exactly that reason, so a shape-matching detector would have
reported eleven false positives against one true one — the outcome this bean
was opened to avoid.

## CALIBRATION — because it reports ZERO, and zero is not soundness

Taxonomy row 34: a tier that had fired on nothing was asserted correct having
measured only that. So the detector is calibrated against the real defect:

| input | hits |
|---|---|
| `qbeta_ck_qholonomic_recurrence_test.py` at `3277607d39` (pre-fix) | **4** |
| the same file after #6760 | **0** |
| the whole `computations/` tree | **0** |

The 4 are the three that actually reverted (`1e-45`, `1e-12`, `1.1`) plus a
fourth (`1e-09`). `--selftest` locks it in on a fixture carrying all four forms
— parameter-passed float, `mp.nstr`, integral, f-string — and fails unless
exactly the first is flagged, so a future narrowing cannot look like a clean
tree.

Corpus 0 with the true positive caught means the ~5 at-risk files do not in
fact pass guard-changing floats. That is prevention working, not a silent
detector.

## Also done

`tolerance_guard_bypass_audit.py`'s blind-spot note said *"Tracked in bean
`qou-9tqx`"* — completed — so an open item pointed at a closed bean. Retargeted.

## BASELINE (2026-09-05, PR #6816 head `b3097ae73e`)

    PYTHONPATH=computations:tools/qou-substrate/python \
      python3 computations/audits/tolerance_guard_bypass_audit.py --strict
    ... --selftest

  -> both exit 0; 3250 witnesses; LIVE-DIRTY 0; LATENT 0; VARIABLE-PASSED 0.
