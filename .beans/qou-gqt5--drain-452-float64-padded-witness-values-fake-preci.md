---
# qou-gqt5
title: 'DRAIN: 452 float64-padded witness values (fake precision) + source-level mpf(float) detector'
status: in-progress
type: task
priority: high
created_at: 2026-08-06T23:54:42Z
updated_at: 2026-08-19T05:51:53Z
---

Owner directive: NO FLOAT64. witness_float64_padding_audit.py finds 283 distinct values / 452 occurrences across 61 files (56 live) where a float64 was serialized at 50+ dps, writing 30+ digits of binary-rounding garbage on values with ~8 significant figures. Dominant class: B_AME_MeV / B_target_MeV (AME experimental binding energies). Example: 8.4817962 serialized as 8.4817962000000015621026250300928950309753417968750000000000. DISCRIMINATOR: relative distance to nearest binary64 is ~1e-50 for padded vs ~1e-17 for genuine 50-dps. ROOT CAUSE: mpf(<python float>) instead of mpf('<string literal>') -- the value is binary-rounded before mpmath sees it. Ratchet is in place (baseline 452, --strict blocks new). TWO FOLLOW-UPS: (1) drain by fixing producers to carry values as strings then re-running -- never hand-edit, never --rebaseline to go green; (2) add a SOURCE-level AST detector for mpf(<float literal or float-valued var>) so the anti-pattern is caught at authoring time rather than after it reaches a witness. That second one likely prevents more than the drain fixes.


## 2026-08-19 — taken over (12 days idle); both halves resolved, and the numbers here were stale

### Item (1), the drain: DONE by other arcs, not by me

Measured today: **452 -> 13 occurrences, 61 files -> 6 (1 live)**. The
description above is 12 days out of date. Disposition of the 13 survivors:

- **12 are in `computations/_deprecated/`** — dead code. Re-running those
  producers buys nothing.
- **1 'live' hit is a meta-artifact**: `hardcoded-literal-audit.witness.json`
  QUOTING a padded literal it found. That literal now survives only inside a
  COMMENT (`delta_lambda_k_star_variance_phase5d_5b.py:218`), so the source
  was already fixed.

So the live padded surface produced by any live producer is **zero**. Baseline
untouched — not rebaselined, not hand-edited.

### Item (2), the source detector: it already existed, and it did not cover this

`mpf_float_source_audit.py` (written 2026-08-07) covers `mpf(<literal>)` and
`mpf(float(x))`. It does NOT cover the shape that actually bit us, because
that shape contains **no `mpf()` call at all** — the float64 enters through
arithmetic.

### The gap I measured, and the new gate

    fmt(mpf(f64))                 padding ratchet: CAUGHT
    fmt(exact_mpf * mpf(f64))     padding ratchet: BLIND
    fmt(sum(exact_k * mpf(f64)))  padding ratchet: BLIND

One exact factor launders a float64 past the value-level detector while the
result still carries ~16 good digits. New advisory gate
`computations/mpf_mixed_arithmetic_audit.py`, wired into precision-gates.sh:
float64 **taint** reaching a high-precision **sink** (`fmt`/`_fmt`, or
`mp.nstr(x, n)` with n > 17).

**I got the invariant wrong first.** Written as 'is a binop mixing mpf with
float64?' it scored ZERO on pre-fix h6 — accumulator seeded `0.0` (exactly
representable), weights via `dict.get()`, `y_lambda_at` unannotated, so both
operands were untagged. Rewritten as taint->sink; the self-test pins that
regression.

**One measured false positive, fixed:** a probe-local
`def tr_M_atomic(...) -> float` poisoned the canonical symbolic
`markov_peel.tr_M_atomic` via bare-name resolution. Registry now drops any
name defined more than once corpus-wide. 39 -> 28 candidates.

**Precision: 3/3 adjudicated rows are TRUE positives**, all on values whose
field names assert precision — including `rho_k_full_via_wenzl_lr:280`
`"tr_M_q0_mp30dps"`, which is h6's defect exactly
(`mp.mpf(repr(float(y_lam)))` then multiplied by an exact chi) on the
canonical trace.

### What is left (NOT done here)

The **28 candidates need agent verdicts**, and the three above need fixes at
their producers. They sit in other arcs' files (qbeta, phase5, rho_k), so I did
not touch them from this branch. Gate is ADVISORY until those verdicts land;
flip to blocking then. Baseline can only shrink, never grow.
