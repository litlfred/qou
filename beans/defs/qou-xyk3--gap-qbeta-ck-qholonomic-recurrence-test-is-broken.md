---
# qou-xyk3
title: 'GAP: qbeta_ck_qholonomic_recurrence_test is BROKEN on main — TypeError: cannot create mpf from None at :359'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T21:29:14Z
updated_at: 2026-10-04T15:20:20Z
parent: qou-avtq
---

Parent: qou-x5mi. Found while trying to declare `q0Anchor: comparison` on it.
Independent of the environment hazard that bean records — this one fails in ANY
environment and is a defect on main.

## The failure

    python3 computations/probes/qbeta_ck_qholonomic_recurrence_test.py
    -> TypeError: cannot create mpf from None

    File ".../qbeta_ck_qholonomic_recurrence_test.py", line 358, in main
        worst_ext = max(
    File "...", line 359, in <genexpr>
        abs(anchors["muon"]["c_emp"][k] - mp.mpf(ext[f"c_{k}"]))

`ext[f"c_{k}"]` is `None` for at least one k.

## It is NOT my change

Verified by stashing my patch and running main's version verbatim: identical
traceback, identical exit 1. My edit was in the witness-write block at ~:580,
which the traceback never reaches.

## Consequences

* the producer CANNOT be re-run, so its witness cannot be refreshed by anyone;
* the q0Anchor declaration it needs (`comparison` — it reads both pins
  deliberately, `extract_empirical_ladder(Q0_MUON)` at :328 alongside the
  proton leg) cannot be landed, because a producer-side declaration only
  reaches the witness through a re-run;
* whatever is currently in
  `computations/probes/qbeta-ck-qholonomic-recurrence-test.witness.json` is the
  last output of a version that ran, and nothing on main reproduces it.

## Not diagnosed

I did not chase WHY `ext["c_k"]` is None — whether an upstream extraction
returns None for a rung that is genuinely unavailable (in which case the
consumer needs a guard) or whether something that used to populate it has
changed. That is the first question for whoever picks this up. Note the
c_k ladder is convention-C-frame and cds1-gated (AGENTS.md), so "just make it
not-None" may be the wrong fix; the honest answer might be that the rung has no
value under the current state and the producer should say so.

---

FIXED 2026-09-05 (session fervent-noether). The crash is resolved: `mp.mpf(None)`
at the extended-ck cross-check now guarded. When
`qbeta-decay-sdp-extended-ck.witness.json` carries null `c_k_extracted_50dps`
(float64-drained per qou-p77d / df84635376, and the ladder is convention-C /
cds1-gated so it must NOT be repopulated), the gate is recorded as **skipped**
(a new `skip()` helper; `allPassed` excludes skips) rather than crashing. Probe
now runs to completion (exit 0).

Root cause confirmed as filed: the extended-ck witness `c_2..c_10` are all
`None`. Fix is guard-the-gate, per the bean's own caveat — not repopulate.

REVEALED, NOT CAUSED (out of scope): the committed witness was stale-GREEN
(`allPassed:true`, 2026-07-11) because the probe has crashed ever since, freezing
a pre-breakage snapshot. Regenerating it honestly flips `allPassed` to false and
surfaces THREE pre-existing failures — `muon_c3_matches_N3_witness` computes
c_3 ≈ **-974** vs expected -2.02, plus the two downstream c3 gates. That is the
cds1 convention-gate / **qou-v6wz** c3 breakage, NOT caused by this crash-fix and
NOT laundered here. The probe now honestly reports it instead of hiding it behind
a crash + a stale-green witness.
