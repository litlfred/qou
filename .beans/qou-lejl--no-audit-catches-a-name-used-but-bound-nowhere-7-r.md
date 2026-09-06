---
# qou-lejl
title: No audit catches a name used but bound nowhere — 7 real defects found by an ad-hoc scan this session
status: todo
type: task
created_at: 2026-09-06T11:01:16Z
updated_at: 2026-09-06T11:01:16Z
---

## The gap

Every mechanism here that could catch a `NameError` requires EXECUTION, and the
files that break this way are exactly the ones nothing executes.

- `producer_importability_audit` imports each producer, so it sees names
  undefined at **module level** only. A name used inside a function is
  invisible: the import succeeds, the module looks healthy, and the NameError
  waits for whoever calls that function.
- `tests/` + `tools/qou-substrate/tests/` run 209 tests and execute **none** of
  the 300+ probes. A probe can be dead for weeks and stay green.

## Evidence it is not hypothetical

An ad-hoc version of this scan found **7 live defects** this session that both
mechanisms had passed — and every one has the same shape: **a block rewrite
dropped a definition while its consumer, elsewhere in the file, survived.**
Merges, bulk transforms and convention migrations all produce it; none is
careless, the consumer is simply outside the diff's line range.

| where | name | what dropped it |
|---|---|---|
| `hecke_core_legacy` | `_is_sparse_sigma` | merge took HEAD for 12 hunks, call site auto-merged outside them |
| `qbeta_cosine_parametrisation…` | `_os_sidu` | bulk transform injected the import INSIDE the docstring |
| `witness_failed_assertion_audit` | `_os_sidu` | same |
| `qbeta_delta_vs_deltaTbeta_settled…` | `Path` | `pathlib` never imported; dead at import for six days |
| `he_nu_sdp_barfold_h9_test` | `RAIL` | q0-anchor migration rewrote the `Q0 = …` / `RAIL = …` block |
| `he_nu_sdp_psd_count_test` | `H` | same |
| `he_nu_sdp_saturation_obstruction` | `RAIL` | same |

Only the first was caught by a suite, and only because it happened to be
module-level (46 tests red). The three `he_nu_sdp` names sit on the **LP success
path** and all three publish witnesses.

## Built: `computations/audits/undefined_name_audit.py`

Static AST over every tracked `.py`. **No execution.** Whole-file scoping
deliberately — a name bound anywhere counts as bound — so it under-reports
rather than false-alarms, which is the right side to err on for a detector
nobody trusts after its third bad call.

`--selftest` proves the classifier on **15** cases, including the calibrated
false positives that a naive version gets wrong.

### Calibration mattered — the first run was 14 findings, 7 of them wrong

- **Lambda parameters.** Without binding them, `key=lambda kv: kv[1]` reports
  `kv`: **95 false positives** in the very first run.
- **Annotation-only loads.** `derivation_chain.py` has
  `M_HECKE_PIPELINE_AT_Q0: dict[str, mp.mpf]` with mpmath never imported. Under
  `from __future__ import annotations` that annotation is a string and is never
  evaluated — no runtime error. Reporting it would have put a false alarm on a
  module **27 files import**. A name is now reported only when some load of it
  is OUTSIDE an annotation.
- **`exec()` / `eval()`.** `computations/hecke/jm_*_probe.py` (5 files) exec a
  sibling probe's source for its `build`. The name IS defined at runtime and no
  static pass can see it, so such files are skipped as unsound, like
  `from x import *`.

## Result: 7 NEW findings, on top of the 7 already fixed

    scanned 4503 tracked .py | star-import skipped 12 | exec/eval skipped 39

| file | line | name |
|---|---|---|
| `computations/crt_markov.py` | 352 | `_q_sym` |
| `computations/deltalambda/a4_interface_operator_driver_search_probe.py` | 77 | `Q_50_DIGIT_STR` |
| `computations/from_scratch/derive_he3.py` | 66 | `tr_M_q0` |
| `computations/markov/hecke_regular_nf_table.py` | 187 | `_HERE_W` |
| `computations/probes/finite_q_volume_conjecture_probe.py` | 158 | `vol41` |
| `fluid_part2.py` | 98 | `append_to_file` |
| `qou-mass/.../schur_principal_mpmath.py` | 258 | `_pb` |

Spot-checked four by reading the code: all genuinely used and bound nowhere —
`_q_sym` inside a loop, `vol41` in a print, `_pb` loading a witness path.

The witness asserts `findings == 0` and is therefore **red at 7**, which is the
ratchet. That is the convention here: 18 of 48 audit witnesses are red.

## NOT fixed here — unclaimed

This is a DETECTOR. A finding is a question ("where did this name go?"), not a
verdict, and the answer belongs with whoever knows the intent. The three
`he_nu_sdp` names were recovered from the commit each witness records in
`scriptCommitSha` rather than invented from a plausible magnitude; the 7 above
deserve the same treatment and have not had it.
