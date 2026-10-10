---
# qou-xyk3
title: 'GAP: qbeta_ck_qholonomic_recurrence_test is BROKEN on main — TypeError: cannot create mpf from None at :359'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T21:29:14Z
updated_at: 2026-10-10T10:40:00Z
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


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** The crash fix landed (3277607d39) and the probe runs. Its "NEGATIVE (scope-(a))" verdict is not supported on main: the empirical ladder it tests is the broken C-frame ladder (c_3 ≈ −974, qou-v6wz), and the verdict text is a hardcoded string that disagrees with the numbers printed above it.

Evidence: `3277607d39` is on main. `qbeta_ck_qholonomic_recurrence_test.py:337` guards the null `c_k` with `skip()`. Re-ran: exit 0, 0.3 s, witness numerics identical (only metadata changed). Residual defects found (see Cross-cluster): the probe exits 0 while `allPassed false` (3 failing: `muon_c3_matches_N3_witness` computed −974.07 vs −2.02, `c3_cross_anchor_swing_near_2p4pct`, `caveat_residuals_below_AME_extraction_noise_floor`). Its printed VERDICT prose is hardcoded (lines 471–475: "100-280%", "c_4 prediction +7.4 to +7.5") and contradicts its own computed output (c_4 prediction 1507.4, empirical c_k+2 = −114130).

Status: `todo` → `completed`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-10-10 — follow-up review (re-check of the `qou-avtq` sweep flags)

**Cause R1 — a convention-D input read with convention-C formulas.** `computations/q-beta-operator-valued-N3.witness.json` (2026-08-21) carries the D-frame phase (α = −0.0404857773) and Q_N2 = 0.7828047136. `qbeta_decay_sdp_full_ck.py`, `qbeta_decay_sdp_extended_ck.py` and `probes/qbeta_ck_qholonomic_recurrence_test.py` extract c_k = (R−1)/u^k from R(q0) = Q_AME/(Q_N2/N2) using C-frame rungs. Reproduced: C gives Q_N2 = 0.782334410 and c_2 = −1.0150; D gives Q_N2 = 0.782804714 and c_2 = −9.2962338, matching the witness. The c_3 = −974 and c_4…c_7 = −1.1e5…−1.8e11 follow from that. Per `qou-8ofm`/`qou-frch`, one scalar R fixes at most one rung, so no extracted c_k at k ≥ 3 is evidence in either convention.

**Consequence here.** The probe's input ladder is the R1 artifact, so its "NEGATIVE (scope-(a))" kill is **inconclusive**, not a negative. Re-run reproduces 3 FAILs, `main()` returns 0 unconditionally (`:627`), and the verdict paragraph is hardcoded (`:466-480`, says "+7.4" where the probe prints 1507.4).

**Open code step (needs owner OK):** exit non-zero when `allPassed` is false and compute the verdict text.

Checked read-only against qou `main` at `aa914b606a`, mpmath 1.3.0. Full write-up: `qou-review/avtq-reopened-beans-2026-10-10.md` (project files). Status unchanged.
