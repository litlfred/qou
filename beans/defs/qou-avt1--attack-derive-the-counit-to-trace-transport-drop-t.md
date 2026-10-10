---
# qou-avt1
title: 'ATTACK 1 (best): derive the counit->trace transport; the cosine is the unjustified step'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-10-04T15:10:48Z
parent: qou-avtq
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


## 2026-08-29 — G2 SHARPENED: the affine transport's even part is the CONSTANT 1 (convention-agnostic)

Idle-window analytical advance (reseed build running). Makes G2 precise and
frame-independent, and connects it to the two proved Lean files.

REPARAMETRISE the proved KC19 transport by the gap. CrossingWeightAffine.evalMap_ratio
(sorry-free, generic field) gives L(z) = evalMap h z / evalMap h 1 = (h-2z)/(h-2).
With alpha = (z-1)h/2 (so eps - tr_M = 2 alpha, the exact identity), this is
  T(alpha) = 1 - 4 alpha / (h (h-2))     -- LINEAR in alpha.

EVEN PART = CONSTANT 1. Under alpha -> -alpha, z -> 2-z, so
  (T(z) + T(2-z))/2 = [(h-2z) + (h-4+2z)] / [2(h-2)] = (2h-4)/(2(h-2)) = 1  exactly.
So the proved affine transport carries ZERO even-order content.

THE CLASH, SHARPENED. q-beta-cos-resummation.lean axiomatises the correction as
cos(alpha) (class TransferMatrixEigenphase), whose even part is cos(alpha) itself
= 1 - alpha^2/2 + O(alpha^4). Since the proved transport's even part is the
constant 1, the ENTIRE O(alpha^2) content of the cosine resummation is sourced by
the AXIOM alone -- nothing proved (KC19) supplies it. This is why the transport
overshoots ~300x: a linear-in-alpha transport structurally cannot source a
quadratic alpha^2 correction.

CONVENTION-AGNOSTIC. This is a statement about functional FORM in alpha, not about
z. It holds for any z (C or D) -- evalMap is over a generic field and alpha is a
free parameter. So unlike the numerical w* (C/D-dependent), the G2 form-clash does
NOT wait on qou-cds1's D re-derivation. (The cos file's own markovZ is C and cannot
migrate to D -- its bar-antisymmetry needs z bar-even -- but the even-part clash is
upstream of that.)

LEAN PLAN (queued for verification when the reseed build lands; drafted, sorry-free
target ~55 lines, new file QOU/QBeta/LadderCosClash.lean):
 - transportFactor k a := 1 - k*a; transport_even_part_const: T(a)+T(-a) = 2  [ring, CommRing]
 - evalMap_ratio_eq_transportFactor: KC19 ratio at w0=1 = transportFactor (4/(h(h-2))) ((z-1)h/2)  [field_simp;ring, Field]
 - cos_lt_one_of_mem_Ioo (0<a<2pi): cos a < 1  [Real.cos_le_one + Real.cos_eq_one_iff]
 - cos_correction_ne_affine_even_part: cos a != (T(a)+T(-a))/2 = 1  [the G2 theorem]
This DROPS nothing yet but makes 'the cosine is the thing to drop' precise: the
cosine is the SOLE carrier of the O(alpha^2) term. Verified affine even-part = 1 by
hand two ways.


## 2026-08-29 — workflow-verified (adversarial, both lenses survive): cosine loses justification under D
Under canonical D the cosine correction is NOT derived: its evenness-forcing (Markov cyclicity via eigenphase_bar_involution) EVAPORATES because z_D is neither bar-even nor bar-odd (symbolic-exact: alpha_D(1/q)+alpha_D(q)=q^2/2-1+1/(2q^2) != 0; alpha(1/q)=-alpha(q) IFF z(1/q)=z(q), true C false D). The only convention-agnostic PROVED transport is affine (even-part 1), O(alpha^2)=0, so the cosine's O(alpha^2) is axiom-only with no D backing. Scope-(a) (not 'false under D'). NEW: a SECOND carrier QOU.BraidKnot.V21Eigenphase / markovSymmetrizedV21Character (HoefsmitV21CosSymmetrization.lean) is ALSO on the C eigenphase -> verdict STRONGER; C-scope/drop must cover BOTH files. Next: land LadderCosClash.lean (drafted) + open the fork bean (does a bar-odd alpha_D exist reproducing the H3 V_(2,1) spectrum?). Audit docs/audits/2026-08-29-convention-d-qbeta-front-adversarial-audit.md.


## 2026-08-29 — G2 is now PROVED-LEAN (landed)
QOU/QBeta/LadderCosClash.lean committed (0f4df6eed6), sorry-free, verified lean-direct (axioms={propext,Classical.choice,Quot.sound}): transport_even_sum (affine even part =1), evalMap_ratio_eq_transportFactor (KC19 ratio = 1-4a/(h(h-2))), cos_correction_ne_affine_even_part (cos a != affine even part on (0,2pi)). The cosine is the SOLE carrier of the O(a^2) term. Still open: the fork bean (does a bar-odd alpha_D exist reproducing the H3 V_(2,1) spectrum) + C-scope/drop BOTH cosine carriers (QBetaCosResummation + V21Eigenphase).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
