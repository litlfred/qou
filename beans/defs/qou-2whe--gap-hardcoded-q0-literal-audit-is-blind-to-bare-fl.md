---
# qou-2whe
title: 'GAP: hardcoded-q0-literal audit is blind to bare floats and to the canonical pin itself'
status: in-progress
pr: 8182
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T11:24:04Z
updated_at: 2026-10-04T15:20:04Z
parent: qou-2002
---

`computations/audits/hardcoded_q0_literal_families_audit.py` exists to find
hardcoded transcriptions of the muon q0. Two spellings pass through it silently.
Both are in one line:

    _LITERAL = re.compile(r'["\'](1\.10997859555[0-9]{1,})["\']')
                           ^^^^^^                    ^^^^^^^^^^^^^
                           quotes REQUIRED           prefix PINNED to A/B

**1. Bare float literals are invisible.** Only a QUOTED value matches, i.e. a
string transcription. `Q0 = 1.1099785955573347` is a float64 literal and never
matches. Measured over non-deprecated `computations/**/*.py`: **201** files
carry a quoted A/B literal (visible), **130** carry a bare one, **104 carry ONLY
a bare one** — wholly invisible.

**2. The canonical pin's own literals are invisible.** `1.10997859555` is the
A/B family. Since `fca08de7d29` (2026-08-28) canonical is C,
`1.10997859564273...`, which this pattern cannot match in ANY form. **28**
non-deprecated files carry a C literal; none is examined.

**Verified against a FRESH witness, not the committed one** — that distinction
mattered: the committed witness showed assertion 2 passing, a fresh run has BOTH
assertions failing and ~219 divergent A-literals. **So this audit is loud, not
quiet** — an earlier draft of this finding said 'reports essentially nothing',
which was reading the stale committed witness. The defect is that its loudness
covers one spelling while two pass through.

Worked case (found via `qou-tekx`, not via this audit): the three
`probes/he_nu_sdp_*` producers, each `Q0 = 1.1099785955573347` bare, each NOT
LISTED. Three C-literal files spot-checked, also NOT LISTED.

## Do NOT just widen the regex

That would be worse than the blind spot. A class-(b) site in
`q0-literal-classification.json` names a superseded value **in order to detect
it** — my own census extension does exactly this and must carry all three — and
a witness recording history legitimately quotes A. The certain finding is about
the DETECTOR; the per-file verdict is not settled. Any widening needs the
triage classes extended alongside it, and the `BASELINE_DIVERGENT = 61` ratchet
re-baselined deliberately rather than as a side effect.

Documented in the audit's own source (comment-only; verified zero non-comment
lines changed) so the next reader is not misled by its output.


## THIRD BLIND SPOT: scope (measured 2026-08-30)

`_SCAN_ROOT = HERE.parent` resolves to `computations/` and nothing else, so
every producer outside that tree is unscanned. Measured .py files carrying a
q0-pin literal outside `computations/`, excluding `_deprecated`:

    19  docs/audits/scripts          <- EMITS COMMITTED WITNESSES; entirely unscanned
     3  qou-mass/src/qou_mass/_internal   (generated mirror — never hand-edit)
     2  tools/qou-substrate/python/qou_substrate
     2  tools/pyhecke/tests
     2  tools/pyhecke/python/pyhecke
     1  tools/qou-substrate/tests
     1  tests

`docs/audits/scripts/` is the one that matters. Found via `qou-tekx`: 6 of the
10 literal-transcribing producers behind unstamped off-canonical witnesses are
`docs/audits/scripts/keystone_*_probe.py`, invisible to this audit purely
because of where they live.

So the three blind spots are **quotes required**, **prefix pinned to A/B**, and
**scope limited to computations/** — and the same caution applies to all three:
widening without extending the triage classes would flag the class-(b) sites
that carry a superseded value in order to detect it.


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
