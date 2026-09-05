---
# qou-qxsf
title: 'PRODUCER FIX: saddle_offset_zero_location_probe.py computes its whole numeric core in float64'
status: completed
type: task
priority: normal
created_at: 2026-09-04T20:59:25Z
updated_at: 2026-09-05T05:48:39Z
---


Found while draining the never-raises-dps audit after the 2026-09-04 merge of
origin/main (bean `qou-j6gb`). The audit flagged this probe as never raising
working precision; adding `set_compute_dps()` at module scope satisfied the
audit but changed **no published value**, because nothing downstream of it is
an mpf. That is the whole finding: the fix is cosmetic and the audit cannot
see why.

The numeric core is float64 end to end:

    :124  return sum(float(_coeff(coeffs, k)) * q ** k for k in ...)
    :178  spread = (max(vals) - min(vals)) if vals else float("nan")
    :186  tail = [abs(float(_coeff(o, k))) for k in range(1, ORD + 1)]
    :205  rel = abs(r18 - val) / abs(val) if val != 0 else float("inf")
    :236  o0 = float(_coeff(o, 0))
    :254  an = [abs(float(_coeff(o, k))) for k in range(1, ORD + 1)]
    :280  R_geo = math.exp(-b_geo) if b_geo != 0 else float("inf")

42 raw float64 fields reach `saddle-offset-zero-location.witness.json`,
including every `assertions[*].computed` / `assertions[*].expected`. So the
probe's four locked expectations E1-E4 are themselves being checked in float64.

Why it matters here specifically rather than generically: this probe's
headline number is a **root location**, q* = 0.08931, claimed
"truncation-STABLE ... spread over N>=3 = 7.0e-04", and compared against
q_quad = (-9+sqrt(193))/56 = 0.08737 and against substrate quantities at the
~1% level. A stability spread of 7e-04 is far above float64 noise, so the
VERDICT is not currently in doubt -- but the comparison "closest is hbar_q at
~9.9%" and the series-radius estimates (`R_est`, `R_geo`, a `math.exp` of a
fitted slope) are the kind of quantity where float64 error compounds through
an ORD=18 coefficient tail. The claim should be re-derived in mpf before it is
cited as a pinned negative.

Scope:
1. Carry `_coeff(...)` as mpf, not `float(...)`, at all 6 sites.
2. `_mp.exp` / `_mp.inf` / `_mp.nan` for the float64 sentinels and `math.exp`.
3. Serialize with `_precision.fmt`, dropping the file's 42 entries from the
   raw-float64 baseline (regenerate the audit; never hand-edit the baseline).
4. Re-run and diff q*, the N>=3 spread, R_est and R_geo. If the verdict moves,
   that is the finding; if it does not, the negative is now pinned honestly.

NOT a regression introduced by the merge -- the 42 fields are pre-existing
entries in the repo-wide raw-float64 baseline (1032 dirty witnesses / 33998
fields). Filed so the cosmetic fix is not mistaken for a real one.
