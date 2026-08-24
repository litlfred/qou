---
# qou-a39q
title: 'float64 padding: 71 fake-precision fields in 4 witnesses, three different causes'
status: todo
type: task
created_at: 2026-08-24T07:21:23Z
updated_at: 2026-08-24T07:21:23Z
---

The drain (1e18c44fd) regenerated 5 witnesses that carry PADDED float64 --
values whose 50-digit tail is the binary64 representation, not precision.
witness_float64_padding_audit: new_not_baselined 0 -> 76, now 71 after one fix.

ATTRIBUTION: all 5 are mine by touch, none by cause. The 12 baseline
occurrences are all in _deprecated/ and untouched by either branch. The
producers were NOT changed by this branch -- only their witnesses were, one
commit each (the drain). So the producers already had the defect and the
committed witnesses were simply old enough to predate it. Same shape as the
beta-decay-matrix "downgrades": the drain made stale witnesses agree with
source that had already gone bad.

FIXED (5 occurrences)
  inverse-markov-qvalues.py -- set_compute_dps() sat ~96 lines BELOW the five
  module constants it was written to protect; its own comment said "the
  module-scope constants below" while they were above it. They were built at
  mpmath's default 15 dps (~53 bits = binary64) and then printed to 50+
  digits. Q_exp read
      0.01861000000000000154098955817971727810800075531005859375
  for a source constant of `0.01861  # +/- 0.00001 MeV`. Moving the call
  above the constants gives 0.01861. Only the `mp.mpf("...")` literals inside
  `decays` were ever actually protected.

REMAINING (71), AND THEY ARE NOT ONE BUG -- checked, not assumed
  delta-lambda-categorical-verification (55 rows) -- NOT the ordering bug:
      set_compute_dps() is at line 72 and every mp.mpf assignment (74, 96,
      277, 281) is after it. The padded values are per_lambda[i].delta_lambda,
      e.g. 0.000005004562355627323864439015554950174191617406904697418212890625
      against a real value of 5.004562355627324e-06. So a float64 is reaching
      mpf at RUNTIME, not at import. Needs tracing from delta_lambda's
      producer chain, not a line move.
  qbeta-markov-trace-{compute-accuracy-diagnostic,norm-probe,steps-4-5}
      (16 rows) -- these never call set_compute_dps() AT ALL and contain no
      mp.mpf assignments of their own, so they inherit mpf values from
      imports at whatever dps happens to be current. Adding the call is
      necessary but may not be sufficient; the inherited values need checking.

DETECTOR GAP WORTH CLOSING
  mpf_float_source_audit.py reports DEFECT 0 ("no mpf(<non-representable
  float literal>) in the source tree") while all of the above exist. It
  inspects LITERALS passed to mp.mpf(). None of these are literals: they are
  float64 VARIABLES reaching mpf, or correct literals evaluated before dps
  rose. A source audit over literals cannot see either.
