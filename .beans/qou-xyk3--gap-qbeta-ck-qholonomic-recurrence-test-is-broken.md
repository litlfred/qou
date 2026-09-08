---
# qou-xyk3
title: 'GAP: qbeta_ck_qholonomic_recurrence_test is BROKEN on main — TypeError: cannot create mpf from None at :359'
status: completed
type: task
priority: normal
created_at: 2026-08-29T21:29:14Z
updated_at: 2026-09-08T09:01:24Z
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


## 2026-09-08 — CLOSED. Fix confirmed ON MAIN and the probe verified running here.

Pulled off the `qou-bstl` completion-candidate queue. The 2026-09-05 note above
records the fix; the status field was left at `todo`, so verifying rather than
taking it on trust — a sibling's bean is not a primary source (`qou-geqa`'s
lesson).

**On main, not just on a branch.** `3277607d390` ("guard qbeta_ck_qholonomic
probe against null extracted c_k") — `git merge-base --is-ancestor` against
`origin/main` returns **yes**.

**Runs to completion here.** `python3 -u
computations/probes/qbeta_ck_qholonomic_recurrence_test.py` → **exit 0**, full
verdict block printed, witness written. The `TypeError: cannot create mpf from
None` that this bean is about does not occur.

Note the path: this bean's title says `qbeta_ck_qholonomic_recurrence_test` and
the file lives at `computations/probes/`, not `computations/qbeta/`. A
`git log` on the qbeta path returns empty and reads exactly like "the fix never
landed". Recording it because that near-miss is one keystroke from a wrong
reopen.

**What is out of scope stays out of scope, and is not laundered by closing
this.** The honest regeneration flips `allPassed` to false and surfaces three
pre-existing failures — `muon_c3_matches_N3_witness` computing c_3 ≈ −974
against an expected −2.02, plus two downstream c3 gates. That is the cds1
convention gate, owned by **`qou-v6wz`**, and it was *revealed* by this fix
rather than caused by it. The probe now reports it instead of hiding it behind a
crash and a stale-green 2026-07-11 witness. Closing this bean does not close
that; `qou-v6wz` is open and is where it belongs.

The probe's own verdict is a scope-(a) NEGATIVE on the 4₁ order-2 qZeilberger
operator, printed in full — a result, not a silent failure, so its `exit 0`
alongside one FAILed assertion is defensible and is not the `qou-li9a` /
`qou-9d6h` silent-producer class.

**qou-xyk3 closes.** The GAP it names is fixed, on main, verified by running it.
