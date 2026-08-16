---
# qou-y0mc
title: 'GAP: the binding law''s interpretation block names two inequivalent objects (trace-ratio free energy vs channel-measure entropy)'
status: todo
type: task
priority: normal
created_at: 2026-08-16T16:27:01Z
updated_at: 2026-08-16T16:27:59Z
---

Opened from the L2 binding axis after six repair routes and the alpha direction
all closed. Every one of those closures rests on the binding law, so the law
itself was checked. **It is derived, not conventional** —
`content/quantum-observable-universe/mass-endomorphism/markov-trace-gibbs-free-energy.md`:

    E_bind = E_0 * ln( tr_M(W_free) / tr_M(W_atom) )

a Gibbs free-energy difference dF = kT ln(Z1/Z2) with kT = E_0, resting on Markov
traces as temperature states on the Hecke tower (Jones 1987). With
tr_free/tr_atom = 1/mu exactly, that is B = -E_0 log mu. So the floor stands.

**The gap:** the same block, two sentences later, says *'The entropy in play is
that of the normalized channel measure y_lambda chi^lambda over Wedderburn
blocks.'* For a two-channel split those are inequivalent:

    implemented   S = -log(mu+) - log(mu-)          >= 2 log 2   (FLOORED)
    named         H = -mu+ log(mu+) - mu- log(mu-)  <=   log 2   (CEILINGED)

Disjoint ranges. Measured: S = 1.681247 nats -> 7.0377 MeV (3.27x nature);
H = 0.559347 nats -> 2.3414 MeV (1.09x). Nature's 0.513850 nats is OUTSIDE S's
range and INSIDE H's.

**DO NOT read this as 'H is right'.** Four reasons, recorded so the next agent
does not skip them:

1. Post-hoc — the alternative was sought only after the floor failed.
2. It does NOT fix the sign, which is the primary defect: -a*mu*log(mu) > 0 for
   every 0<mu<1, so under H both channels still bind (T=1 +0.8951, T=0 +1.4463).
3. The +-10% window is 14.8% of the available [0, log2] range — an 8.85% miss
   inside it is weak evidence.
4. The headline formula is S; the channel-measure line is a secondary remark.
   Promoting H because it fits better launders a fit through an ambiguity.

**What would settle it (a derivation, not a fit):** which object does the
confinement reweighting actually cost — the free-energy difference of the TRACE
RATIO, or the entropy of the CHANNEL MEASURE? These are different physical
claims about what confinement does, and the corpus currently asserts both. A
derivation of one from the categorical action would settle it; a preference
based on which fits better would not, and is blocked.

Secondary, cheap: reconcile or scope the block's own two sentences regardless of
which wins — as written it is self-inconsistent for any 2-channel split.

Probe: computations/probes/binding_law_surprisal_vs_entropy_ambiguity_probe.py
