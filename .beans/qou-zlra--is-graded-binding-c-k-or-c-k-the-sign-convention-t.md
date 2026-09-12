---
# qou-zlra
title: Is graded binding +c_k or -c_k? The sign convention the type-two result hangs on
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T12:02:10Z
updated_at: 2026-09-12T12:06:42Z
---


Opened 2026-09-04 from `qou-oooq`. Small, cheap, and everything in the type-two
result hangs on it.

## The problem

`the_asymmetry_term_lives_at_vassiliev_type_two_probe` reads binding as
`-alpha c_2/c_0`. With that sign the asymmetry PENALISES `|N-Z|` and the
volume-like term is positive — both correct.

With the opposite sign every conclusion inverts: symmetric nuclei become the
LEAST bound and the volume term becomes negative.

**And the opposite sign is the more natural reading of the corpus.**
`vassiliev-filtration-mass-tower` writes the trace as
`tr_M = c_0 + c_1 h + c_2 h^2 + ...` and calls the higher terms "precision
refinements" that are ADDED. A mass formula built from `tr_M` would then carry
`+c_2 h^2`, not `-c_2 h^2`. The probe's `-` was chosen because it makes the
physics come out right, which is exactly the kind of choice this corpus's
discipline is meant to catch.

Note also that `c_2/c_0` is MINIMISED at `N = Z` (it is `(N-Z)^2/2` plus a
constant), so the sign is not a cosmetic convention — it decides whether the
symmetric nucleus is the most or the least bound.

- [ ] Read how `unified-iterative-correction` and the six-term mass formula
      actually combine trace coefficients into an energy: is there a `-log`, a
      shadow price `u_lambda`, or a bare sum? `B_lambda = m_e H_q(lambda)
      u_lambda (ln|tr M| - ln d_lambda)` suggests a LOG of the trace, which is a
      third possibility and would change the graded analysis again.
- [ ] Settle the sign, then re-state the type-two result with it — or retract
      the sign-dependent half.
- [ ] If the natural sign is `+`, say so plainly: the type-two term would then
      make symmetric nuclei least bound, which is a falsification rather than a
      caveat.
