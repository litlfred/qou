---
# qou-avt1
title: 'ATTACK 1 (best): derive the counit->trace transport; the cosine is the unjustified step'
status: todo
type: task
priority: high
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-08-26T04:14:19Z
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
