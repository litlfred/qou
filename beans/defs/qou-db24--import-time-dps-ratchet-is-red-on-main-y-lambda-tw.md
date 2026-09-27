---
# qou-db24
title: 'import-time dps ratchet is RED on main: y_lambda_two_row_cap_gate.py builds mpf(''1e-30'') before dps is raised'
status: in-progress
type: bug
priority: normal
created_at: 2026-08-28T15:18:36Z
updated_at: 2026-09-27T06:17:41Z
---

## Found 2026-08-28, incidentally, on a clean main tree

Running `scripts/precision-gates.sh` on `origin/main` (cdbdc84af1) with no local
changes to any producer, the **import-time dps ratchet** reports:

    proven lossy (literal arg): 1
       L47: mpf('1e-30')  [literal]
    baseline literal / expr : 185 / 103
    now      literal / expr :   1 /  20
    NEW files (not baselined) : 1
       literal=1  expr=0   computations/audits/y_lambda_two_row_cap_gate.py

`new_not_baselined: 1` is a ratchet RED. The committed
`mpf-import-time-dps-audit.witness.json` still records `literal_findings: 0`
and `new_not_baselined: 0`, so the committed audit disagrees with a fresh run.

## Whose

`computations/audits/y_lambda_two_row_cap_gate.py` landed recently in
`25e8f8c1d9 gate(y_lambda): assert the convention-D two-row cap at the TABLE,
not per consumer`. Not the discoverer's file; recorded rather than fixed to
avoid widening an unrelated PR.

## The defect

Line 47 builds `mpf('1e-30')` at module scope, i.e. while `mp.dps` is still
mpmath's default 15. The ratchet's whole subject: string-sourcing is necessary
but not sufficient, the TIMING matters too. A tolerance constant built at dps 15
carries 15 digits no matter what the caller later sets.

For a bare tolerance like `1e-30` the practical impact is likely nil — the value
is exactly representable and used as a comparison threshold. **That is a reason
to check it, not a reason to leave it red**: a ratchet with one unexplained
entry is a ratchet people learn to ignore, which is the failure mode this gate
family's own comments keep returning to.

## Two honest options

1. **Fix at the literal** — move the constant inside the function, or build it
   after `set_compute_dps()`. Cheapest if the value is genuinely used at
   precision.
2. **Baseline it with a stated reason** — only if the value provably cannot
   lose anything. NOTE the standing rule: baselines DRAIN, never grow. Adding
   an entry needs an argument in the commit, not a `--rebaseline`.

Do not simply regenerate `mpf-import-time-dps-audit.witness.json` to make the
committed count match: that records the regression as the new normal, which is
the widening this repo forbids.


--------

## SECOND, independent red in the same run — `audits-tree raw-float64`

The same clean-tree run of `scripts/precision-gates.sh` reports a second
BLOCKING red, unrelated to the first:

    RED: import-time dps ratchet   audits-tree raw-float64

    audits-tree raw-float64  (scan root: docs/audits)
      NEW dirty witnesses : 1
      REGRESSED           : 0
             2  docs/audits/2026-08-26-kernel-defeq-sample.witness.json

Two raw float64 fields in a witness under `docs/audits`, dated 2026-08-26 and
landed on main. Also not the discoverer's file.

So the gate suite is red on `main` for TWO independent reasons, neither of them
belonging to any in-flight branch. Worth stating because a branch that runs the
suite and sees red will reasonably wonder whether it caused it — that costs a
cycle each time until one of these is drained.

Fix per the standing rule, for both: **at the producer**, carrying `mpmath.mpf`
end to end and serializing with `_precision.fmt`. Do not add either file to a
baseline and do not `--rebaseline`.

## Caveat on the numbers above

The gate suite was first run here against a tree that was being modified
concurrently (two audit witnesses regenerated then reverted mid-run), so that
run's per-gate counts were unreliable. Both reds were then re-established by
running the two audits individually against a tree whose only change was one
unrelated file, and each named its offending file explicitly — which is the
evidence quoted above, not the racing run.


## 2026-09-27 — TRIAGED 7-for-7. Not fixed, and two would be WRONG to fix.

Picked up because this bean was `todo` and unclaimed. Measured on clean
`origin/main` (`aedd199fc0`) with `computations/mpf_import_time_dps_audit.py`.

**The specific site this bean names is GONE.** `y_lambda_two_row_cap_gate.py:47`
(`mpf('1e-30')`) does not appear in a fresh run — it was fixed. The **class**
recurred in different files, so the bean is stale in its instance and live in its
subject.

**The counts have moved a long way, and mostly the right way:**

| | 2026-08-28 (this bean) | 2026-09-27 |
|---|---|---|
| proven lossy (literal) | 1 | **7** |
| baseline literal / expr | 185 / 103 | 185 / 103 |
| now literal / expr | — | **7 / 26** (−178 / −77) |
| NEW files not baselined | 1 | **9** |

So the ratchet has **drained 185 → 7** on literals. The RED is the
`new_not_baselined` arm (9 files), exactly as this bean describes — not a
regression in the baselined population.

### 🛑 This bean's stated REASON is wrong, and the correction matters

It argues *"For a bare tolerance like `1e-30` the practical impact is likely nil
— **the value is exactly representable**"*. **Measured: it is not.** A negative
power of ten is not a dyadic rational, so it has no exact binary form at any
precision. dps-15 vs dps-70 relative difference, all seven:

    -2.0693425728   5.457e-17      1e-40      7.071e-17
    0.577           7.389e-17      4.0e-4     4.792e-17
    1.82306787      1.905e-17      0.0565947  3.912e-17
    1e-25           3.849e-17

**Uniformly ~1e-17** — which is what a binary constant pinned at dps 15 costs,
and it is the same for a "round" literal as for an 11-digit one. The conclusion
(impact nil) survives; the reason does not, and the reason is what a later agent
would reuse.

### Why the impact IS nil here — the per-site determination

All seven are **comparison thresholds or deliberately-quoted reference values.
None is an input to a computed quantity.** Four say so in their own comment:

| site | literal | role |
|---|---|---|
| `qbeta/qbeta_ck_c5_slot_and_size_mismatch_probe.py:94` | `-2.0693425728` | `C3_PROTON`, `# recorded extraction; see Caveat` |
| `qbeta/qbeta_ck_c5_slot_and_size_mismatch_probe.py:95` | `0.577` | `AGENTS_QUOTED_OMITTED_TERM`, `# ppb, as written into AGENTS.md` |
| `probes/beta_ew_n3_second_trace_probe.py:71` | `1.82306787` | `COT_THETA_W_CODATA` — *"the target the two consumer files compare against, **not as an input to anything computed here**"* |
| `probes/molien_blast_radius_remainder_triage_probe.py:79` | `1e-25` | `Q_NEAR_ONE = 1 + 1e-25`, a probe point |
| `probes/uic_sign_decomposition_probe.py:99` | `1e-40` | `ZERO`, a vanishing tolerance |
| `qbeta/qbeta_fibre_unit_circle_opens_route5_probe.py:102` | `4.0e-4` | `TARGET_OWN_UNCERTAINTY` — experimental gap, PR #6688, TWO sig figs |
| `qbeta/qbeta_required_phase_target_provenance_probe.py:79` | `0.0565947` | `QUOTED_TARGET`, `# as quoted by HolonomySpectrumSignObstruction` |

In every case the consumer is a comparison whose own tolerance is many orders
looser than 1e-17. **No number in the corpus is wrong because of these seven.**

### 🛑 TWO of the seven would be ACTIVELY WRONG to "fix"

- **`0.577`** *is the claim under adjudication*, quoted verbatim from AGENTS.md
  so the probe can test it. Re-deriving it to full precision would destroy the
  probe's subject — it exists to check a figure *as written*.
- **`4.0e-4`** is an experimental uncertainty carried at its published two
  significant figures. Extending it implies precision the measurement lacks.

So a blanket "raise these to `set_compute_dps()`" pass is not a drain, it is a
corruption of two probes. Whoever takes this must go site by site.

### Why I did not fix the other five

The 2026-09-07 override's exemption 1 tests whether a change makes a number
*more correct* or a wrong number *impossible*. Measured, none of the five does:
the consumers are comparisons and the 1e-17 pinning cannot move a verdict. That
leaves it as tidying-near-a-number, which the override names as **not** exempt,
and as a per-file basis determination, which it also names. So: measured,
reported, **not swept**. Bean stays open.

### What would actually clear the RED

The red arm is `new_not_baselined`, so the options are (i) baseline the 9 new
files — but **baselines drain, never grow**, so no; (ii) fix the five benign
sites site-by-site and leave the two quoted ones with an explicit
`# float64-intentional`-style marker if the audit grows one; or (iii) teach the
audit that a module-scope `mpf("<literal>")` assigned to an UPPER_CASE name
whose comment marks it as quoted/target/tolerance is the corpus's declared
convention for a reference value, not a defect. **(iii) is my judgement of the
right answer** — the corpus has a consistent convention here and the audit does
not know it — but it is a detector change on a blocking gate, which is the
owner's call, and I have just been wrong once this session about narrowing a
blocking gate.
