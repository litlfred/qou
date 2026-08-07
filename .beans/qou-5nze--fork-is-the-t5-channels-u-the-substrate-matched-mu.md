---
# qou-5nze
title: 'FORK: is the T5 channel''s u the substrate-matched Murakami meridian, or not?'
status: todo
type: task
priority: critical
created_at: 2026-08-07T22:22:06Z
updated_at: 2026-08-07T22:22:06Z
---

The derivational probe (`qbeta_qnnq_theta_is_im_u_probe.py`, PR #4513) closed
the "what IS theta_K" question and opened a sharp two-branch fork.

WHAT IS SETTLED. theta_K is not a search target. `DeltaLambdaT5Assembly.lean`
(`s_channel_at_substrate`) gives S = A_omega*kappa*(Re^2 u - Im^2 u) with
Re u = ln q0 proved (`meridian_holonomy_boost`), so

    theta_K = Im(u(q0))

and `SDeformedVolumeChannel.u : R -> C` is documented as "the substrate ->
deformation map u(q0) (LOG MERIDIAN HOLONOMY)". The ln^2 q0 - theta^2 shape is
just Re^2 u - Im^2 u.

THE COLLISION. `FigureEightDeformedMeridianWinding.lean` proves SORRY-FREE that
the substrate-matched Murakami meridian is u = N*t - 2*pi*i*k, so Im u = -2*pi*k.
Conjoined with the above, theta_K is QUANTIZED in units of 2*pi. Tested:

  - k_mu = 0 rows STRADDLE ln q0 — the first readings in the whole arc to pass
    the necessary condition that all nine measured readings failed — then miss
    the A-free ratio by >= 890x.
  - common k = 0 forces theta = 0 at BOTH anchors, so S has the same sign at
    both, contradicting the MEASURED sign flip S_mu > 0 > S_p.

THE FORK — exactly one of these is true, and both are cheap to settle:

(a) THE TWO u ARE DIFFERENT OBJECTS. The T5 channel's `u` is a class FIELD —
    any function R -> C — while the Murakami quantization arises from the
    specific matching q_eval = exp((u + 2*pi*i)/N) to a real substrate. If the
    channel does not impose that matching, its u is unconstrained and the
    quantization simply does not apply. In that case the T5 docstring's "log
    meridian holonomy" wording is MISLEADING and theta_K needs a stated
    alternative definition — which is then the real open question, and a much
    better-posed one than "find a geometric quantity of the right size".

(b) THE T4-INVERTED THETA VALUES ARE INCOMPATIBLE with the proved meridian
    quantization. They are A_omega-conditioned anyway; this would be a second,
    independent reason to distrust them.

HOW TO SETTLE IT: read whether any instance of `SDeformedVolumeChannel` imposes
the Murakami matching condition on `u`, or whether `u` is left free. That is a
Lean-reading task, not a compute task, and it decides which branch holds.

WHY THIS MATTERS MORE THAN ANOTHER READING: branch (a) reframes the whole gap —
it says the arc has been searching for a quantity whose DEFINITION is not yet
pinned, which is why no reading fit. Branch (b) invalidates the targets every
probe has been compared against. Either way the next step is definitional, not
exploratory.

Guard recorded in the probe: the (k_mu,k_p) = (1,2) row's |ratio| = 0.24995 sits
1.9% from |r| = 0.24539 and looks like a hit. It is not — the ratio tends to
k_mu^2/k_p^2 = 1/4 identically as L -> 0, |r| merely lies near 1/4, and the sign
is wrong (r < 0 requires straddling).
