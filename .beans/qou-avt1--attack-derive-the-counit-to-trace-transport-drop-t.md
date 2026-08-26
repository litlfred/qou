---
# qou-avt1
title: 'ATTACK 1 (best): derive the counit->trace transport; the cosine is the unjustified step'
status: in-progress
type: task
priority: high
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-08-26T04:22:51Z
---

Parent: `qou-cds1`. The highest-value Q_beta vector, and it is already in the
corpus rather than speculative.

THE IDENTITY (exact, any z):    eps(Delta) - tr_M(Delta) = h(z-1) = 2*alpha

So the ladder's phase is EXACTLY HALF THE COUNIT-MINUS-TRACE GAP: the precision
ladder is implicitly TRANSPORTING the evaluation from the Frobenius counit to
the Markov trace, and alpha measures that transport's infinitesimal generator.
Q_A = -E_0*eps(Delta) is a COUNIT object; conj:binding-qbeta-complex-volume's
frak-V = E_0*tr_M((Pi_free - 1).M) is a TRACE object. The corpus states outright
that "the counit and the Markov trace are genuinely distinct functionals on the
substrate" (nuclear-interactions/qbeta-counit-closed-form.md).

WHERE THE UNJUSTIFIED STEP IS. Not the gap -- the gap is structural. It is the
COSINE: exponentiating a difference into cos(alpha - u/2). That is exactly
QOU.Interactions.QBetaCosResummation, which is AXIOMATISED, so DROPPING IT COSTS
NOTHING PROVED. This is a far more specific target than "derive a different
functional form".

DISCIPLINE -- READ BEFORE RUNNING ANYTHING. Do NOT hunt combinations landing
near F_required = 0.998325. That is the fit qou-cds1 forbids, and the bare
transport ratios were already measured once and deliberately not pursued
(C: trM/eps = 0.44087, odd(trM)/eps = 0.55761; D: 0.56748 / 0.68421). The move
is FORMALIZE-FIRST: state what a counit->trace transport must satisfy
structurally (functoriality, its behaviour under the bar involution, its
q -> 1 limit), and check whether that PRUNES the class -- before any numerics.
A transport found by search is a fit however good it looks.

Also live: ce is resolved to only 1.45% (68.8 sigma), so no identification
quoted better than 1.5% is measurement.


## 2026-08-26 — RUN. The transport OVERSHOOTS by ~300x. Scope-(a).

Gates pre-stated before the run and reproduced in the probe docstring; the
formalize-first instruction above was followed and NO search near F_required was
performed. 6/6, exit 0, mpmath 60 dps.

KC19 (`evalMap_affine` / `evalMap_ratio`, proved-lean) makes the transport
CONCRETE rather than mysterious: E(w) = h^2/2 - h*w is AFFINE in the crossing
weight, eps = E(1) (trivial loop) and tr_M = E(z), so "transport counit -> trace"
means exactly MOVING THE LOOP WEIGHT w FROM 1 TO z ALONG A LINE. That is sharp
enough to test, so I tested it.

MEASURED. Solving the ONE linear equation L(w*) = F_required (one unknown,
determinate, not a search):

    F_required = 0.99832524167324658888
    w*         = 0.99850030441134736542        <- within 0.15% of the COUNIT
    z_C = 0.4993203  z_D = 0.6126880

    frac_C = (w*-1)/(z_C-1) = 0.0029953   -> overshoot 333.85x
    frac_D = (w*-1)/(z_D-1) = 0.0038721   -> overshoot 258.26x

The G4 kill criterion was fixed in advance at frac < 0.01 => overshoot. Both
frames fail it by more than a factor of two.

VERDICT. "The ladder transports the evaluation from the counit to the Markov
trace" is NOT supported as stated. Whatever the ladder does, it moves the
evaluation ~0.3-0.4% of the way to the trace, not all of it. The counit->trace
gap is REAL (the identity eps - tr_M = 2*alpha is exact) but it is ~300x too
BIG to be the correction. This is the same shape as the two-row cap result,
which was an order too big and left no residue.

SECOND FINDING (G2), independent of the numbers. L(w) = E(w)/E(1) is AFFINE in
w, because the denominator is w-free. So Q_beta/Q_A would be affine in the loop
weight -- while the ladder asserts a COSINE. Two different functional forms;
they agree only at isolated points. This is the same "transversal crossing, not
identity" pathology cds1 found for alpha_required vs alpha_C and again in the F
coordinate, now located in a third place. The cosine remains the axiomatised
step (QBetaCosResummation) and remains the thing to drop.

w* IS A MEASUREMENT, NOT A VALUE. It is what the current parameterisation
demands in the natural coordinate, exactly as cds1 measured z* and
alpha_required. It is resolved no better than ce (1.45%). DO NOT wire it and DO
NOT hunt a closed form for it -- at that resolution any identification is
arithmetic. G5 records it is not bar-even under h -> -h.

WHAT SURVIVES IN THIS BEAN. The gap identity and its Lean backing are untouched;
what is refuted is the READING that the ladder completes the transport. The live
residue is G2: the form clash. A correction affine in the loop weight and a
cosine cannot both be right, and only one of them is axiomatised.

Probe: computations/qbeta/qbeta_counit_trace_transport_overshoot_probe.py
