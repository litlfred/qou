---
# qou-2t9y
title: 'GAP: the cross-anchor Stage B probe panics in the Rust engine — its committed PASS is 70 days old and records the mu-p separation 0.719% wrong'
status: in-progress
pr: 8182
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T07:02:45Z
updated_at: 2026-10-04T15:20:25Z
parent: qou-2002
---


Found 2026-09-13 from an unrelated direction — an AST scan for decimal literals
carrying more digits than the parse can keep (bean `qou-gqt5`). Two of the hits
were the substrate anchors in this probe, and running it to verify the fix is
what surfaced the crash.

## The probe does not run, on `main`, unmodified

```
thread '<unnamed>' panicked at tools/hecke-engine/src/seminormal.rs:379:13:
chi_lambda_braid: invalid generator index 0 for n = 3 (valid range: 1..=2)
```

`computations/qbeta/qbeta_hoefsmit_chi_cross_anchor_stage_b_unblocked_probe.py`,
at its first `chi_lambda_braid` call. **Verified against pristine `origin/main`**
(`git show origin/main:<path>` run from a scratch copy), so it is not my edit and
not a tree artifact. It panics before writing anything, so the probe emits no
witness at all today.

This is a Rust `panic!` on a malformed input, **not** one of the deliberate
refusals AGENTS.md warns against mistaking for a defect — the engine is
rejecting the word, not declining to compute. `electron_word = [(1, 0), (1, 1),
(1, 0)]` and the engine wants generator indices in `1..=2` for `n = 3`, so the
word format the probe uses is stale against the engine's current contract.

## The committed witness is a 70-day-old PASS carrying a wrong number

`computations/qbeta/qbeta-hoefsmit-chi-cross-anchor-stage-b-unblocked-probe.witness.json`:

| field | committed value |
|---|---|
| `computedAt` | **2026-07-05T11:21:17Z** |
| `commitSha` | `ce39b659e64f` |
| `anchors.q_proton` | `1.1099785827513808` |
| `anchors.q_muon` | **`1.10997859555`** |
| `anchors.delta_q_over_q` | **`1.1530509914642561e-08`** = 11.5305 ppb |
| `assertions[0].passed` | **`true`** (`stage_b_pass_regression_and_q_stability`) |

The live μ–p separation is **11.61406 ppb** — recomputed here at `mp.dps = 60`
from `Q_50_DIGIT_STR` and `q_muon_at()`, and AGENTS.md independently records
**11.6141 ppb**. So the committed record is **0.719 % wrong on the quantity the
probe exists to measure**, and it is green.

The cause is in the source, not the arithmetic: `Q_MUON` was hand-typed as
`1.10997859555` — twelve significant digits, and **not a truncation of the live
anchor** (`1.109978595642739046681795…`), so it is already wrong at digit 12
while the measured quantity is ~1.16e-8.

## What is fixed here, and what is NOT

**Fixed** (PR on `claude/overlong-float-literal-detector-2026-09-13`): both
anchors now come from the canonical carriers as `mpf`, and `Δq/q` is computed in
mpmath. Verified by running it — the probe now prints `Δq/q = 1.16140603426e-8
= 11.61406 ppb` before it reaches the crash.

**NOT fixed, and this is the gap:**

1. **The panic.** Repairing the braid word needs a per-site determination of what
   the correct word for the electron at `n = 3` is under the engine's current
   contract. That is neither a precision increase nor corpus-derived, so under
   the 2026-09-07 ASK-THE-OWNER directive it waits.
2. **The witness.** It cannot be regenerated while the probe panics, so the
   wrong `11.5305 ppb` and its green assertion stay on `main`. Do not read the
   source fix as having corrected the record.
3. **The χ comparison is float64 regardless.** `chi_lambda_braid` takes a
   `float` `q_value` by engine contract, so every χ in this probe is float64 and
   the anchors being exact does not make the comparison exact. The casts are now
   written out at each call site rather than hidden behind a truncated literal;
   that is visibility, not precision.

## Why this belongs to `qou-58zw` Class 2 as well

Class 2 is "the producer SHRANK" — a committed witness whose producing code can
no longer generate it. This is a cleaner instance than any of the 15 that
`witness_producer_resolution_audit.py` lists, because those are *unresolvable*
records while this one is a **reproducibly-false** one: the producer exists, is
named correctly, resolves correctly, and panics.


## Progress Update — 2026-11-16 (PR litlfred/qou#8182)

- [x] **Lean 4 Formalization (`0` `sorry`, `0` vacuity audit hits/advisories)**:
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/CrossAnchorStraddleAndSelfCertification.lean` (wired into `QOU.lean`) proves:
    - `stageB_truncation_bias_and_coxeter_trace` (`qou-2t9y`)
    - `detector_union_and_truncation_secant` (`qou-2whe`)
    - `operator_input_straddle_residual_and_amplification` (`qou-qyef`)
    - `env_diff_confound_and_true_pin_swing` (`qou-o922`)
    - `cal2_self_certification_roundtrip_and_discrepancy` (`qou-tekx`)
- [x] **50-dps Verification Probe & Witness (`0` raw `float64` fields)**:
  - `computations/probes/cross_anchor_straddle_and_self_certification_probe.py` -> `computations/probes/cross-anchor-straddle-and-self-certification-probe.witness.json` (`allPassed: true`, 5/5 assertions, `scriptHash: ccf81d198aee`, `scriptCommitSha: aa5f4d7a1cb250599dfceca8aa1274da33800a1a`).
- [x] **PR**: `litlfred/qou#8182` (`e87dd879c9ba7ce8a4dbb4751ce6e8dadbaf371b`).
