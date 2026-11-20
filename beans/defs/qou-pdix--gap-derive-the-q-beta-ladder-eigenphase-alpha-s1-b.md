---
# qou-pdix
title: 'GAP: derive the Q_beta ladder eigenphase alpha (S1 blocker) — carrier is vacuous, exact-bridge route refuted'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T15:35:20Z
updated_at: 2026-11-20T14:39:28Z
parent: qou-avtq
---

Parent: qou-cds1 (tranche S1). **This is the S1 blocker.** The c_k tail is
settled — tail_common proves z reaches the ladder only via the N=1 phase, so
c_2/c_3/c_4/c_5 are all phase-blind. What is missing is a DERIVATION of alpha.

## Why there is nothing to port from C

QOU.Interactions.TransferMatrixEigenphase (content-block sibling
nuclear-interactions/q-beta-cos-resummation.lean) is documented as axiomatising
'M_beta has spectrum {e^{+i.alpha}, e^{-i.alpha}} on V_(2,1) of H_3(q),
alpha = (z-1)h/2'. Its two fields encode NONE of that: '-2 <= 2cos <= 2' and
'cos(x) = cos(-x)' hold for EVERY real. PROVED vacuous:
QOU.QBeta.EigenphaseCarrier.carrier_is_trivial : ... <-> True
(QOU/QBeta/EigenphaseCarrierVacuity.lean, sorry-free, axioms clean).

So q_beta_cos_resummation is UNCONDITIONAL, not conditional, and there is no
C-frame content to port to D. AGENTS.md 3b-tax proof-claims-unencoded.

## Routes already closed — do NOT re-run

1. **Substitute z_D into alpha = (z-1)h/2.** PRUNED by
   qbeta_ladder_required_phase_probe.py (not mine): required phase pinned to a
   window of half-width ~1.1e-5 rad; z_D sits ~1.19e-2 rad away (23%). The
   FUNCTIONAL FORM must change, not the value of z.
2. **Use the exact Form-A/Form-B bridge (1-h/2)/(1-z.h/2) instead of its O(h)
   truncation.** REFUTED this session, scope-(a). alpha = (z-1)h/2 IS that
   bridge's O(h) coefficient (verified symbolically), but the EXACT bridge is
   far WORSE: misses by 530% (C) and 456% (D) vs the truncation's 0.04% and 23%.
   Corollary worth keeping: C's 0.04% agreement is therefore NOT explained by
   the bridge.

## What a derivation must discharge

The content-bearing replacement is already stated and left UNINSTANTIATED (per
3b-tax, that is the honest open state):
  QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum (q) (M) :
    M.trace = 2*cos(eigenphase q)  /\  M.det = 1
For a 2x2 matrix that IS the spectrum {e^{+-i.alpha}}. Non-vacuity proved
(replacement_excludes_some_matrix). Deriving alpha = producing M from the Hecke
seminormal representation on V_(2,1) and proving those two fields — the
'Lean machinery for Hecke seminormal characters is downstream work' the original
docstring defers.

## Also needs doing (small)

The content-block class itself is untouched here; repairing it has QA-sidecar
implications (nuclear-interactions/q-beta-cos-resummation.{ts,md,lean}) and any
downstream [TransferMatrixEigenphase]-conditional statement would need its
banner re-checked, since those results are unconditional as written.


## 2026-08-22 — ROUTE 3 CLOSED, scope-(b): no braid word supplies M

Attempted the derivation. The seminormal rep on V_(2,1) CANNOT supply the M that
TransferMatrixSpectrum demands.

**Rep derived, not assumed.** sigma_1 = diag(q, -1/q) on the two standard
tableaux of shape (2,1); sigma_2 is then FORCED by Hecke + braid to
d_2 = -1/(q(q^2+1)), d_1 = q^3/(q^2+1), with only b*c fixed. That product is
exactly hoefsmitB(q)^2 = (q^4+q^2+1)/(q^2+1)^2 — so hoefsmitB, d_1 and d_2 are
RECOVERED here rather than imported (they appear as asserted inputs in
qbeta_alpha_required_c_vs_d_probe).

**The invariant.** Every character lies in Z[q,q^-1]: b enters a trace only via
b*c, which is rational, so the sqrt never survives. Verified on ALL words of
length 2,4,6 — 17 distinct traces, 0 exceptions. And (z_C-1)h/2 is a
non-constant ALGEBRAIC function of q, whose cosine is not algebraic. So
2cos((z-1)h/2) is not a Laurent polynomial and the two cannot agree AS FUNCTIONS.

**Scalar normalisation does not rescue it:** det rho(sigma_i^{+-1}) = -1, so
det rho(w) = (-1)^L; det M = 1 forces L even and lambda = +-1, leaving the trace
in +-Z[q,q^-1].

**Sharpest instance:** trace(sigma_1 sigma_2) = -1 IDENTICALLY in q (proved in
Lean) with det = 1 — so if it were M, cos(alpha) = -1/2, i.e. alpha = 2*pi/3, a
CONSTANT. The asserted alpha is non-constant. It meets the det half and fails
the trace half.

SCOPE — this is about identity of FUNCTIONS. Does NOT exclude: a non-scalar
(q-dependent, non-rational) normalisation; an M outside the braid image (a
general element of H_3(q), or an operator on a larger space restricted to
V_(2,1)); or numerical coincidence at one anchor — at q0 the nearest non-trivial
character is only 2.7e-3 away. That gap is NOT the basis of the exclusion.

## Routes now closed (do not re-run)

1. Substitute z_D into alpha = (z-1)h/2 — PRUNED (23% vs a 1.1e-5 rad window).
2. Exact Form-A/Form-B bridge instead of the O(h) truncation — REFUTED
   (530%/456% vs 0.04%/23%).
3. **M = lambda*rho(braid word) in the seminormal rep — EXCLUDED, scope-(b),
   invariant named.**

## What is left

The two survivors named in the scope above. The non-scalar-normalisation route
is the more promising: the Markov trace itself carries a q-dependent
normalisation, and that is precisely the kind of factor that could take a
Laurent-polynomial character outside Z[q,q^-1].

LEAN: QOU/QBeta/SeminormalV21Trace.lean (9 decls, sorry-free, axioms clean).
PROBE: computations/qbeta/qbeta_eigenphase_seminormal_exclusion_probe.py (6/6).


## 2026-08-22 (2) — a THIRD detector-blindness class, found because a QA sweep missed this

A trap-drain swept nuclear-interactions this window (11d039dc9d) and passed over
the vacuous carrier. Ran the vacuity audit on that file: 0 candidates, '0
carrier(s)' — not flagged, not even seen.

ISOLATED with a controlled comparison in ONE file: an empty carrier and a
':True'-field carrier were both caught; a carrier whose fields are real-looking
Props that happen to be Mathlib theorems for every argument was not. Genuine
third shape, not a parsing/scoping artifact.

  proof-no-empty-prop-carrier  -> zero fields          (existing)
  true-class-field             -> a field literally ': True'  (existing)
  tautological-field           -> neither, but holds for an arbitrary
                                  substitution of the subject   (NEW)

Why both existing detectors structurally miss it: the carrier HAS fields (so the
zero-field detector is silent) and the docstring's claim count does not exceed
the field count (so the bullet-counting detector cannot fire). It looks
populated and is inert.

DETECTOR ADDED, deliberately narrow — matches only shapes unconditionally true
of the FUNCTION applied (bounds on a bounded function; even-symmetry
identities), and fires only when EVERY field is tautological. Verified on 4
controls: catches the real defect; does NOT flag TransferMatrixSpectrum (the
content-bearing replacement) nor a mixed carrier. Corpus-wide: exactly 2 hits —
the real one (ledger 'genuine') and my own verbatim reproduction in
EigenphaseCarrierVacuity.lean section 1 (ledger 'legit'; must NOT be repaired,
that would destroy the demonstration).

ATTRIBUTION TRAP AVOIDED: regenerating the record took total_defects 81 -> 67, a
DROP of 14 while my detector adds 2. Reverted the detector and re-ran — baseline
65, so my effect is exactly +2 and the drop is pre-existing tree state (13
trivial-true + 3 others fixed by siblings after the record was generated
2026-08-21T21:30Z at 3015 files; tree now 3033). Not my change. Worth recording
because attributing a sibling's 13 fixes to my own commit would have been the
error, and the record moving the WRONG way is exactly when to stop and measure.

Guard test 2 pass; --check-ledger exit 0.


## 2026-08-22 (3) — the exclusion's BOUNDARY located: tr_M is the escape

Route 3's scope named 'a non-scalar normalisation' as a survivor. Pinned down.

The exclusion is about the MATRIX character trace(rho(w)) in Z[q,q^-1]. The
MARKOV trace is a different object:
    tr_M(beta) = sum_lambda y_lambda(z) * chi_lambda(beta)
Its Wedderburn weights carry z. Solved the three H_3(q) Markov equations
symbolically: ALL THREE weights are genuinely z-dependent. So tr_M is NOT in
Z[q,q^-1] and the integrality obstruction does not reach it.

Two independent reproductions of corpus facts confirming this is the real
boundary, not bookkeeping:
  * at z_D: y_(2,1) = q^2/(q^2+1)^2 — exactly the corpus stdWeightD — and
    y_(1^3) = 0, the two-row Temperley-Lieb forcing. Re-derived from the Markov
    equations, not assumed.
  * at z_C: the weights are NOT Laurent polynomials — half-integer powers of q,
    inherited from the sqrt(q) in z_C.

So a transfer matrix normalised by the Markov trace is exactly the non-scalar,
z-dependent object route 3's scope does not cover. **This does NOT say the route
works** — only that the proved obstruction does not close it, and where to look.

## Route status

1. z_D into alpha=(z-1)h/2 ................ PRUNED (23% vs 1.1e-5 rad window)
2. exact Form-A/Form-B bridge ............. REFUTED (530%/456% vs 0.04%/23%)
3. M = lambda*rho(braid word), matrix char  EXCLUDED scope-(b), invariant named
4. M normalised by tr_M ................... OPEN — the live route, boundary now
                                            located; tr_M carries z via y_lambda
5. M outside the braid image .............. OPEN, unexplored

Probe now 8/8 (assertions 7-8 added), exact symbolic Q(q).


## 2026-08-22 (4) — RETRACTION: route 4 closes too. It is ONE invariant.

**Retracting my own entry (3) above**, which said tr_M 'escapes' the obstruction
and named route 4 'the live route'. It escapes Z[q,q^-1] — which is what I
checked — but NOT the field the argument needs, which I did not check before
naming it live.

tr_M(beta) = sum_lambda y_lambda(z)*chi_lambda(beta): weights rational in (q,z),
characters Laurent in q, so **tr_M is RATIONAL in (q,z)**. And
alpha = (z-1)h/2 = (q^2-1)(z-1)/(2q) is itself rational and NON-CONSTANT, so
2cos(alpha) is transcendental over Q(q,z) (cos f = (e^{if}+e^{-if})/2, and e^f is
transcendental over a rational function field unless f is constant).

**No rational assembly of the Hecke/Markov data equals 2cos(alpha).** One
statement subsumes three routes I had been arguing separately:
  route 2  exact bridge -- rational (its 530% miss was a symptom, not the reason)
  route 3  matrix character -- Z[q,q^-1] subset Q(q,z)
  route 4  Markov-normalised trace -- Q(q,z)

## Route table (corrected)

1. z_D into alpha=(z-1)h/2 ......... PRUNED (23% vs 1.1e-5 rad window)
2. exact Form-A/Form-B bridge ...... CLOSED by the rationality invariant
3. M = lambda*rho(w), matrix char ... CLOSED by the rationality invariant
4. M normalised by tr_M ............ CLOSED by the rationality invariant
5. TRANSCENDENTAL construction ..... **OPEN — and now the ONLY route**
6. numerical coincidence at a specialised anchor -- not excluded (identity of
   FUNCTIONS is what is excluded; at q_0 the nearest character is 2.7e-3 away)

## The direction this gives

The obstruction is exactly a RATIONALITY obstruction, so what survives is
precisely the transcendental constructions: a q-exponential, Faddeev's Phi_q, a
holonomy/monodromy, a matrix exponential. A phase e^{i.alpha} arising as a
HOLONOMY rather than a character value is untouched.

**The honest reading is not 'the phase is impossible' but 'the phase cannot come
from character algebra; it has to come from an exponential'** — consistent with
alpha appearing in the corpus only ever inside a cos. That is where a derivation
must look, and it is a much narrower target than 'derive alpha'.

Probe now 10/10 (assertions 9-10 added); the boundary section is corrected in
place rather than appended, since it said the opposite.


## 2026-08-22 (5) — route 5: the obligation is a TRICHOTOMY; my own §2 repair was insufficient

SELF-CORRECTION. TransferMatrixSpectrum (my replacement for the vacuous carrier)
constrains a GIVEN M, but does not force M to come from the Hecke data. For EVERY
alpha there is a matrix with trace 2cos(alpha), det 1 — the rotation exp(alpha*J),
built FROM alpha. So it can be discharged circularly. Proved: 
QOU.QBeta.EigenphaseCarrier.circularWitness is an instance for every q (sorry-free).

With route 3, this gives three branches and only one is contentful:

  1. M in the braid image  -> EXCLUDED (rationality: characters in Z[q,q^-1] c
     Q(q,z); 2cos((z-1)h/2) transcendental over Q(q,z))
  2. M arbitrary           -> CIRCULAR (rotationOfPhase works for any alpha)
  3. M = exponential/holonomy of an INDEPENDENTLY-DEFINED connection whose
     monodromy reproduces the Hecke braiding -> THE ONLY CONTENTFUL OPTION

Branch 3 escapes (1) because a holonomy is transcendental, and escapes (2)
because the connection is defined WITHOUT reference to alpha — which is then
DERIVED as its holonomy angle rather than assumed.

**That is the Kohno-Drinfeld / KZ picture, and the canonical chain already
invokes exactly that shape ('Yekutieli non-abelian Stokes', step 2).** So the
target is now specific: build the KZ/Stokes connection whose monodromy is the
H_3(q) braiding on V_(2,1), and compute its holonomy angle. If that angle is
(z-1)h/2, alpha is derived; if it is not, the ladder's N=1 factor is wrong.

## Why alpha being INFINITESIMAL supports branch 3

alpha = (z-1)h/2 -> 0 as q -> 1 (h = q - 1/q -> 0). A first-order-small phase is
exactly what a holonomy gives: hol(loop) = exp(int A) ~ 1 + int A, phase linear
in the connection strength. An algebraic character has no reason to be
first-order small in h; a holonomy does. Consistent with alpha appearing in the
corpus only ever inside a cos.

## NOT DONE, and it is the whole remaining job

Building that connection. This entry establishes WHERE a derivation can live,
not the derivation.


## 2026-08-22 (6) — branch 3: alpha IS holonomy-shaped to 2nd order; the discriminator is z'(1)

Cheap falsifiable test before building any connection: does alpha even LOOK like
a holonomy angle?

Kohno-Drinfeld FIXES the scale rather than leaving it free. Braiding =
P*exp(hbar*t/2), t eigenvalues +-1, matches Hecke {q, -1/q} exactly when
q = e^{hbar/2}, so hbar = 2 ln q and a holonomy angle is a multiple of ln q.
Test: agreement with c*ln(q) for a SINGLE c, with c pinned at O(t) so every
higher order is a prediction.

    alpha_C: c = -1/2 from t^1;  t^2 pred 1/4  actual 1/4     MATCH
                                 t^3 pred -1/6 actual -5/16   differs
    alpha_D: c = -1/2 from t^1;  t^2 pred 1/4  actual 5/4     differs

STRUCTURAL DISCRIMINATOR (not a coincidence). Expanding alpha = (z-1)h/2 about
q = 1+t with h = 2t - t^2 + ...:
    t^1 coeff = z(1) - 1      -> needs z(1) = 1/2   (both)
    t^2 coeff = 1/4 + z'(1)   -> needs z'(1) = 0    (only C)
    z_C: z'(1)=0, z''(1)=-1/8      z_D: z'(1)=1, z''(1)=1/2

**alpha is second-order logarithmic exactly when the Markov parameter is
STATIONARY at the classical point.** z_C's only critical point on q>0 is q=1 and
it is a MAXIMUM; z_D is not stationary there.

SCOPE: consistency, NOT derivation. Does not derive alpha; does not establish
the angle is -hbar/4 (c came from t^1); ONE predicted order; t^3 fails for C too
so alpha_C is not a logarithm either.

**Falsifiable target for branch 3:** a real KZ/Stokes holonomy should reproduce
alpha through t^2. A construction that misses at t^2 is wrong. That is a much
sharper acceptance test than 'derive alpha'.

TENSION WITH THE RULING, plainly: on this test the decay phase looks C-shaped.
Does not overturn the ruling (corpus-wide trace convention vs one channel's
phase) but deepens the recorded decayLadder_zC_threeRow_ne_zero tension.

PROBE: computations/qbeta/qbeta_eigenphase_holonomy_consistency_probe.py (7/7).


## 2026-08-22 (7) — branch 3: the crux is EXACT, and 'eigenphase' tracks the MODULI

REFUTED (my own first idea, tested not asserted). sigma_1 = diag(q,-1/q) as a
half-monodromy exp(i.pi.A) gives log-gap = 2 ln q - i.pi. The obvious story —
alpha is a QUARTER of that gap (half-monodromy x Markov symmetrisation) — is
WRONG: target/gap = -ln q/(4 ln q - 2 i pi) is not constant, and at q0 the i.pi
dominates the real part 15x. Recorded because it is the first thing the next
reader will reach for.

EXACT: target / Re(log-gap) = -1/4, with Re(log-gap) = 2 ln q. Two things
unexplained, and together they ARE the remaining content:
   (a) why 1/4
   (b) why the i.pi is discarded

## The structural consequence — this is the useful part

sigma_1's eigenvalues: q (modulus q, phase 0) and -1/q (modulus 1/q, phase pi).
Its PHASE content is {0, pi} — CONSTANT, zero q-dependence. All q-dependence
lives in the MODULI (log-ratio 2 ln q). **alpha tracks the moduli.**

Consequences:
 - 'eigenphase' is a questionable name: relative to this operator alpha is a
   log-modulus, not a phase.
 - **A UNITARY holonomy cannot produce a q-dependent alpha from this spectrum**
   (unitary => modulus-1 eigenvalues; here the phases are q-free). So either the
   connection is NON-UNITARY, or the phase comes from somewhere other than
   sigma_1's spectrum. Falsifiable fork, not a refutation.

## Acceptance test for any branch-3 construction (now two-part)

 1. reproduce alpha through order t^2 (entry 6: needs z'(1) = 0)
 2. account for the -1/4 of Re(log-gap) AND for discarding the i.pi (entry 7)

A construction that misses (1) is wrong. One that satisfies (1) but cannot say
why (2) has not derived alpha, only re-fitted it.

## NOT DONE

The connection itself. Building it half-way and reporting a match would be the
fitted result the discipline forbids. Delivered instead: the crux stated
exactly, one candidate refuted, and a sharper constraint (non-unitary or
off-spectrum) on what remains.


## 2026-08-22 (8) — the modular/cosh horn is EXCLUDED; one horn of the fork closes

If alpha tracks the MODULI (entry 7), the natural resummation is cosh not cos —
and cosh(c*ln q) = (q^c + q^-c)/2 is ALGEBRAIC in q for rational c, so the whole
rationality obstruction would dissolve. Worth one line of arithmetic:

    required N1 = Q_codata/(Q_A(1 + c_2 u^2)) = 0.99839767  < 1
    cosh(x) >= 1 for every real x
    cosh((1/2) ln q) = 1.00136  -- wrong side of 1

**EXCLUDED.** A genuine oscillation is required; cos cannot be re-read as cosh.

NEAR-MISS, FENCED. The deviations are comparable and opposite in sign
(1 - N1 = 1.60e-3 vs cosh - 1 = 1.36e-3), which invites an identity. There is
none — 2-cosh and 1/cosh are both off by 2.4e-4 relative, parting at the 4th
digit. Recorded so it is not chased.

REFINEMENT of my own entry 7. 'sigma_1's phases are q-free' is exact FOR
sigma_1 and must not be read as a claim about the representation. PRODUCTS do
carry q-dependent phases (route 3 found elliptic words e.g. sigma_1 sigma_2^-1,
trace -q^2+1-q^-2). The Hecke rep supplies oscillatory q-dependent phases; it
just never supplies THIS one — that is the rationality exclusion, not a shortage
of phases.

## Fork status after this

  non-unitary / modular (cosh) origin ....... CLOSED (N1 < 1)
  phase from outside sigma_1's spectrum ..... SURVIVES, and is now the only
                                              live description: a genuine
                                              oscillation from a transcendental
                                              source outside the Hecke
                                              character ring

## Acceptance test for a branch-3 construction (now three-part)

  1. reproduce alpha through t^2 (entry 6: requires z'(1) = 0)
  2. account for -1/4 of Re(log-gap) AND for discarding the i*pi (entry 7)
  3. be genuinely oscillatory, delivering a value BELOW 1 (entry 8)

PROBE: qbeta_eigenphase_holonomy_consistency_probe.py, now 11/11.


## 2026-08-22 (9) — SUPERSESSION + a synthesis, from sibling work landed on main

Two cds1 commits landed on main while #5448 was open, both on this territory.

### My q=1 coincidence motivation is SUPERSEDED (a0caca71cb)

QOU/BraidKnot/JonesHopfSkein.lean, jonesHopf_at_one, sorry-free over any
CommRing, derives V_Hopf = -2 from the Jones SKEIN axioms. No z, no Markov
trace, no anchor.

So c_3's provenance never needed my argument. I had reasoned: J_Hopf is a Markov
trace, a Markov trace depends on z, therefore the written-form result
(tail_common) leaves a provenance gap that the q=1 coincidence closes. The skein
route closes it better -- the constant does not come from a trace evaluation at
all.

SURVIVES: the theorem zCsub_eq_zDsub_iff itself (conventions agree at q=1 and
nowhere else on the positive branch; sharper than decayLadder_zC_not_jones,
which only rules out s>1). RETRACTED: its stated purpose. #5448 §3 re-scoped.

### The other landing STRENGTHENS the rationality result (93d211598f)

2*alpha = eps(Delta) - tr_M(Delta) -- the ladder phase IS the counit-minus-trace
gap. Their own note says 'locates, closes nothing'. This bean explains why that
is correct:

  eps(Delta) and tr_M(Delta) are both RATIONAL in (q,z) => alpha is ALGEBRAIC
  (consistent with alpha = (q^2-1)(z-1)/(2q), no conflict)
  but 2cos(alpha) is TRANSCENDENTAL over Q(q,z)  [entry 4]

**The phase ANGLE is an algebraic counit-minus-trace gap; the ladder needs its
COSINE, and that is where the rational world is left.** Locating alpha
algebraically therefore cannot close the ladder -- the transcendence enters at
EXPONENTIATION, not at alpha. Same conclusion as entry 4 from the other side,
and neither PR states the synthesis.

Sharpens branch 3: a holonomy construction must exponentiate THAT SPECIFIC gap,
eps(Delta) - tr_M(Delta), not an arbitrary connection.

### Checked, not assumed

Entries 1-8 otherwise unaffected: the rationality invariant, the carrier
vacuity, the -1/4 crux, the two refuted candidates, and the detector were each
checked against these landings.


## 2026-08-23 (10) — branch 3 DEFLATED: the gap is abelian, so the target is a PERIOD

Followed the sibling identity to its consequence, which neither PR draws.

93d211598f proves 2*alpha = eps(Delta) - tr_M(Delta) via
CrossingWeightAffine.evalMap h w = h^2/2 - h*w. Verified: E(1) - E(z) = h(z-1)
= 2*alpha exactly.

**The map is AFFINE in the crossing weight (degree exactly 1):**
    E(w0) - E(w0 + d) = d*h        d^2 coefficient EXACTLY 0

A genuine non-abelian holonomy carries a second-order Magnus/BCH term in the
departure. This gap has NONE. So the phase is an **abelian period of an affine
map**, not a curvature integral — much smaller than the 'non-abelian Stokes'
holonomy the canonical chain invokes at step 2.

TWO READINGS, not chosen between:
  (a) the non-abelian Stokes framing is not what produces THIS phase — it may be
      right elsewhere in the chain and simply not here;
  (b) evalMap's affineness is itself a truncation, higher-order weight structure
      dropped upstream. Its docstring reads definitional, but a docstring is not
      a proof; settling this means chasing evalMap's provenance.

**ACCEPTANCE TEST for branch 3, now three-part and sharper:**
  1. reproduce alpha through t^2 in q (requires z'(1) = 0)
  2. account for alpha = -1/4 of Re(log-gap) AND the discarded i*pi
  3. be EXACTLY FIRST-ORDER IN THE CROSSING WEIGHT — any d^2 term contradicts
     evalMap_affine. This is the constraint an honest non-abelian construction is
     most likely to violate, so it is the discriminating one.
  (plus: deliver a value BELOW 1, entry 8)

This does not derive alpha. It says what KIND of object alpha is, and deflates
the holonomy framing for this channel from non-abelian to abelian.

NEXT: resolve reading (a) vs (b) by chasing evalMap's provenance — is the affine
form definitional or a truncation? That is now the bottleneck, and it is a
corpus-archaeology question rather than a derivation.

PROBE: qbeta_eigenphase_holonomy_consistency_probe.py, now 13/13.


## evalMap provenance: fork SETTLED — affineness is not a truncation (probe now 16/16)

The last entry left the bottleneck as archaeology: is `evalMap h w = h²/2 − h·w`
definitional or a truncation? Chased; it settles, and the answer is sharper than
either branch of the fork.

**It is neither definitional-by-fiat nor a truncation — it is a linear
functional on a fixed vector.** The NF difference is
`(n−p) = [h²/2, −h/2, −h/2, 0, 0, 0]` in `[γ, σ₀, σ₁, L₊, L₋, e⁻]`, and the
Markov rule is `tr_M(eᵢ) = z^#cr(eᵢ)`. So `deg_z E = max{#cr(eᵢ) : cᵢ ≠ 0} = 1`
because the support is crossing-numbers {0,1}. No small parameter enters the
step at all, so "truncation" was the wrong category. Reading (a) adopted.

**The part worth carrying forward — the abelian character belongs to the
DIFFERENCE, not to the evaluation.** `L₊ = s₁s₂` has TWO crossings and
coefficient **1 in both n and p**; it cancels. Restore it and the map is
quadratic in w with d²-coefficient −1 (assertion 15). So n and p each carry a
genuine second-order-in-weight term and the abelian gap is what survives their
cancellation.

**That corrects my own acceptance test.** I had written that a construction
"must be exactly first-order in the crossing weight". Wrong as stated: a
non-abelian construction is not forbidden second-order weight structure — it
must have that structure *cancel between n and p*, as `L₊` does. Same
falsifiability, different and more specific target.

**Residual, named narrowly.** The NF vector is asserted in
`docs/audits/2026-06-16-...counit-vs-trace.md` ("audit step 5") and transcribed
downstream — the Lean `epsNP`/`trMNP` are defs encoding it, and the single
probe carrying it (`probes/probe_path_a_net_vs_trm_leading_order.py:137`)
comments "from the .md". Nothing in `computations/` recomputes it. Assertion 16
confines the exposure: the conclusion depends on the SUPPORT, not the values.
The one thing that overturns it is a nonzero L₊/L₋/e⁻ coefficient in the
difference.

NEXT: branch 3's construction itself, against the corrected test.


## CORRECTION to the entry above — I named the residual, then checked it, and it fails

New probe `computations/qbeta/qbeta_nf_single_wrap_vs_typed_probe.py` (8/8).

The entry above said the residual was narrow and that "the one thing that
overturns it is a nonzero L+/L-/e- coefficient in the difference." **It is
nonzero.** Reimplemented `pyhecke.gram.hm` + `atom.build_nucleon_nf`
symbolically over Q(h), validated against the live PROTON_NF/NEUTRON_NF to
float64 eps, and the typed 6-term difference has FULL support: deg_z E = 3,
with d^2 and d^3 both surviving. Nothing cancels, L+ least of all.

**These are two different corpus objects, and the corpus already said so.**
`docs/audits/2026-05-11-q-beta-residual-decomposition.md` §1 names both and the
factor between them — 1.00579, "typed-crossings 6-term NF picks up nonzero
L+-, e- contributions that exactly cancel at single wrap". Both its numbers
reproduce from the symbolic run: single-wrap |eps| = 0.187207 (audit 0.18721),
typed |eps| = 0.188291 (audit 0.18829). So the 2026-06-16 vector is the
SINGLE-WRAP NF. It was never wrong — it is a simpler object than the one the
live mass compute uses.

**Consequence 1 — my abelian deflation needs a qualifier it did not have.**
On the single-wrap NF: deg_z = 1, d^2 vanishes, abelian period, reading (a)
holds. On the typed NF: none of that. The non-abelian Stokes framing is NOT
deflated there. Commit 17afd55cbe stated it unqualified.

**Consequence 2 — the sharper one, and it is bigger than branch 3.** The ladder
needs an N=1 factor of 0.99839767, a 0.160% correction. The
single-wrap-vs-typed ambiguity in the very object it corrects is 0.579% —
3.6x larger. A 0.16% phase cannot be derived from an object whose NF convention
is unsettled at 0.58%. Scope-(a): settle which NF is canonical FIRST; settling
it moves the target by more than the target. Neither declared canonical here —
the 2026-05-11 audit treats the 1.00579 as still to be explained.

NEXT: this is now the gating question for the whole alpha derivation, ahead of
branch 3. Which NF is canonical for the Q_beta counit chain?


## 2026-08-30 (11) — the FOUR NAMED transfer matrices, excluded by determinant

Routes 1-4 above are for the SEMINORMAL BRAID IMAGE and are not re-run. The gap
they leave: `prop:q-beta-cos-resummation` is conditional on
`prop:beta-decay-transfer-matrix`, which defines four explicit 2x2 matrices over
`Z[q^+-1]` — and TWO OF THEM ARE NOT BRAID-IMAGE ELEMENTS, so the rationality
invariant does not reach them. `T_mix` is an algebraic average (the block says
so) and `Delta_beta` is a scalar multiple of the identity.

    T(c,d) = [[c*h+d, c],[c, d]]
    T_pp = T(1,0) = sigma;  T_nn = T(1,-h) = sigma^-1  (proved: T_pp*T_nn = 1)
    T_mix = T(1,-h/2) = (T_pp+T_nn)/2      NOT a group element
    Delta_beta = T_mix - T_nn = T_pp - T_mix = (h/2)*I    SCALAR

**Excluded by DETERMINANT, no hypothesis on q, over a generic field:**

    det T_pp = det T_nn = -1
    det T_mix = -(1 + h^2/4)   <= -1 < 1  for EVERY real q
    det Delta_beta = h^2/4     = 1 only at h = +-2  (q = 1+sqrt2)

A unit-circle pair forces `det = 1`, so all four fail at the first clause.
Cheaper and more uniform than the rationality invariant, and it covers the two
matrices that one cannot.

**M_beta is undefined.** Six-path corpus-grep, this session: exactly two
occurrences corpus-wide, both inside the claim in
`nuclear-interactions/q-beta-cos-resummation.md`. The only "universal beta
decay matrix" the conditional-on block defines is `Delta_beta = (h/2)*I`, whose
spectrum is the REPEATED REAL eigenvalue `h/2`. A scalar matrix has no
eigenphase at all — proved via centrality (`Delta_beta_central`).

## z_D IS the seminormal diagonal entry — sharper than the recorded wording

`qbeta_alpha_required_c_vs_d_probe.py:37` records `d1` as "numerically identical
to z_D ... a different object". The identity is stronger: `z_D = q^3/(q^2+1)`
and `d1` are THE SAME RATIONAL FUNCTION of q, at every q, not a coincidence at
one anchor. With the already-proved `d1 + d2 = h`:

    z_D + d2 = h        D splits the Hecke differential across the V_(2,1) diagonal

Convention C does not (`z_C(4) = 2/5` vs `d1(4) = 64/17`, Lean-proved). **That
is an argument FOR the 2026-08-15 owner ruling from the representation side**,
independent of the trace-convention registry. Worth carrying into the cds1
write-up; it is the first non-registry reason for D I have seen.

## The braid image is NOT short of q-dependent phases

`sigma_1 sigma_2^-1`: det 1, trace `-1 - h^2`. Genuinely elliptic when
`h^2 <= 1`, i.e. `q <= golden ratio` — the substrate (h = 0.2091) qualifies,
eigenphase 2.1198 rad. But it tends to `2pi/3` as `q -> 1` while the ladder
phase tends to 0 (h(1) = 0, for ANY z). **They do not share a classical limit.**
A quantitative separation to sit alongside entry 4's functional-identity one,
and it refines entry 8's "the rep supplies oscillatory phases; it just never
supplies THIS one" with the reason: wrong classical limit.

## Two errors of mine, both caught by computing rather than asserting

1. I took `sigma_2`'s diagonal as `(d1, d2)`; the braid relation FAILED. The
   off-diagonal residual `b*(a*q^2 - d + q)` forces `d = a*q^2 + q`, hence
   `a = d2, d = d1` — which is exactly what `SeminormalV21Trace.lean` already
   had. The prior agent was right; my guess was the wrong one.
2. My first ellipticity assertion was a TAUTOLOGY (`(-1-h^2)+2 = 1-h^2`, an
   algebraic restatement that cannot fail). Replaced with the golden-ratio
   boundary, which can. Same class as the tautological-field carrier defect
   this bean's entry (2) added a detector for — in an assertion this time.

## Hypothesis note

The Lean carries `(2 : K) != 0`, NOT `CharZero`. The half lives in the OBJECT:
`T_mix = T(1, -h/2)`, so in characteristic 2 it collapses to `T_pp` and
`Delta_beta_eq_scalar` is FALSE, not merely unprovable. `4 != 0` is derived from
`2 != 0` rather than assumed.

## Route table — unchanged where it matters

Routes 1-4 stay closed; **route 5 (transcendental / holonomy) is still the only
live one** and is untouched by this. What changes is coverage, not status: the
four matrices the block is actually conditional on are now excluded too, by a
named invariant, so "M_beta is some other matrix in the corpus" is no longer an
escape.

LEAN: QOU/QBeta/MBetaV21Spectrum.lean — 27 theorems, lean-direct exit 0,
#print axioms clean on all 27, zero sorryAx.
PROBE: computations/qbeta/qbeta_mbeta_v21_spectrum_under_d.py (23/23, exact
Q(q) + mpmath 50 dps at the proton pin). precision-gates.sh --changed exit 0.


## 2026-08-30 (12) — the NF gate is NOT a gate on the entry-6 test: the gap is O(t^3)

The last entry made this the gating question ahead of branch 3: *"A 0.16% phase
cannot be derived from an object whose NF convention is unsettled at 0.58%.
Scope-(a): settle which NF is canonical FIRST; settling it moves the target by
more than the target."* Two results, and the second changes that conclusion for
one specific purpose.

### 1. It is NOT a change of BASIS — it is two different ELEMENTS

`docs/audits/2026-05-11-q-beta-residual-decomposition.md` §1 labels the 1.00579
factor **"basis-change typed-vs-single-wrap"**. **Its own §2 proves the
dual-basis identity** `G^-1 . t = e_gamma`, i.e. *"the framework's net
sum_i (Delta_NF)_i IS the Frobenius counit eps(beta)"*.

Those cannot both be about one element. `eps` is a canonical algebra map, so it
is **basis-independent**: one element has one `eps`, in every basis. The two
NFs give different polynomials, therefore they expand **DIFFERENT ELEMENTS**,
and §1's label is a category error against §2 of the same document.

**This reframes the open question.** "Which NF is canonical" sounds like a
convention to be picked. It is actually *"which braid element is the canonical
nucleon pair"* — a modelling question with a physical criterion, not a
bookkeeping one. Worth carrying into whoever takes this next.

### 2. The gap is O(h^3), so it cannot reach the t^1 or t^2 coefficients

Exact, and it reproduces the audit's 1.00579 to six digits:

    eps_typed - eps_sw = h^3 (h^4 + 2h^3 + 2h^2 + 2h - 1) / 4
                       = -h^3/4 + h^4/2 + h^5/2 + h^6/2 + O(h^7)

The two NFs **agree through O(h^2)** and first differ at **O(h^3)**. With
`h = 2t - t^2 + ...` that is `O(t^3)`.

Entry (6) states the branch-3 acceptance test as *reproduce alpha through order
t^2*, with the coefficient pinned at t^1 so t^2 is a prediction. **An O(t^3)
ambiguity contributes nothing at t^1 or t^2, so it cannot move that test.**

**Scope, carefully.** The bean's magnitude argument is untouched and remains
correct for the ABSOLUTE 0.160% target: 0.579% really is 3.6x larger, and any
derivation targeting the absolute value is still blocked on which element is
canonical. What is now established is narrower and useful: *a magnitude at q0
and an order in the expansion are different claims*, and only the order governs
which Taylor coefficients an ambiguity can reach. So **branch 3's falsifiable
test is available now** — it does not have to wait on the NF question.

### An error of mine, caught by Lean

I wrote the gap at `h = 1` as `-1/4`, which is the **cofactor at h = 0**, a
different quantity. The actual gap at h=1 is `1 - (-1/2) = 3/2`, which the
closed form gives as `(1+2+2+2-1)/4 = 3/2`. `norm_num` reduced my claim to
`False` on the first run. Recorded because the two numbers sit one line apart
in the same theorem block and the conflation is easy to repeat.

LEAN: QOU/QBeta/NFCounitGapOrder.lean — 7 theorems, lean-direct exit 0,
#print axioms clean on all 7, zero sorryAx. Generic `Field K` with `(2:K) != 0`
where the halves require it; the cofactor statement needs no hypothesis at all.
PROBE: computations/qbeta/qbeta_nf_counit_gap_order_probe.py (8/8, exact Q(h),
reproducing 1.00579 at the proton pin).

### Route table

Unchanged: routes 1-4 closed, route 5 (transcendental/holonomy) still the only
live one. What changes is that its acceptance test is **no longer gated on the
NF question**, so it can be attempted now.


## 2026-08-30 (13) — RETRACTION of entry (12): the gate STANDS. I applied an eps result to alpha.

Entry (12) concluded *"the NF gate is NOT a gate on the entry-6 test: the gap is
O(t^3)"*. **Wrong.** I proved a statement about the COUNIT and applied it to the
PHASE. They are different functionals — this bean's own entry (9) says so:

    alpha = (eps(n-p) - tr_M(n-p)) / 2

and only the `eps` half is insensitive. Measured, first nonzero order in `t`,
identical in BOTH conventions:

    eps    gap   t^3   (coeff -2)
    tr_M   gap   t^1   (coeff -1/4)
    ALPHA  gap   t^1   (coeff  1/8)

**The NF choice moves the phase at FIRST order. The gate stands exactly as
entry (11) wrote it.** The bean was right; my correction of it was not.

### Why the two halves differ — the part worth keeping

The counit sets every `z^k -> 1`; the Markov trace weights by `z^{#cr}`. The two
NFs differ precisely in the `L_+/L_-/e^-` coefficients, whose crossing numbers
are 2, 2, 3 — so under `eps` those differences cancel to `O(h^3)`, and under
`tr_M` they survive at `O(t)`.

**The NF sensitivity of the phase lives entirely in the CROSSING-NUMBER
GRADING, not in the algebra.** That is a sharper statement of the gate than
"unsettled at 0.58%": it says where the sensitivity is, and why no re-basing of
the counit can remove it. A derivation of alpha must fix the crossing-number
grading of the nucleon element, not merely pick a normal form.

### The typed NF is WORSE, not better — the hypothesis that motivated (12)

I went in expecting the typed NF to repair the `t^3` mismatch, since entry (6)
found single-wrap C matches `c*ln q` at `t^2` and fails at `t^3`, and the counit
gap first bites at `t^3`. It does the opposite — it destroys the `t^2` match:

    C single-wrap  [-1/2,  1/4, -5/16]    vs pred [-1/2,  1/4, -1/6]
    C typed        [-3/8, 11/16, -71/32]  vs pred [-3/8,  3/16, -1/8]
    D single-wrap  [-1/2,  5/4, -1/2]     vs pred [-1/2,  1/4, -1/6]
    D typed        [-3/8, 19/16, -45/16]  vs pred [-3/8,  3/16, -1/8]

**Single-wrap C remains the only combination matching through `t^2`**, and
entry (6)'s recorded tension with the D ruling is unchanged. The first two rows
reproduce entry (6) exactly from an independent construction, which is what
established that the machinery is right rather than merely self-consistent.

### What SURVIVES entry (12)

1. **The closed form.** `eps_typed - eps_sw = h^3(h^4+2h^3+2h^2+2h-1)/4`,
   leading `-h^3/4`, reproducing the audit's 1.00579 to six digits. The seven
   Lean theorems are statements about `eps` only and are **all correct**; only
   the docstring's conclusion about `alpha` was wrong, and it is fixed in place.

2. **It is NOT a change of basis — it is two different ELEMENTS.** `eps` is a
   canonical algebra map, hence basis-independent, so one element has one `eps`;
   different `eps` => different elements. The 2026-05-11 audit's §1 label
   "basis-change" is a category error against its own §2 (which proves the net
   IS the counit). Unaffected. The open question is *"which braid element is the
   canonical nucleon pair"*, not which basis.

3. **The alpha-gap leading coefficient is 1/8 in BOTH conventions** — the NF
   sensitivity is convention-independent at leading order.

### Contamination check

Entry (12), commit `0d414e780f`, and that commit's message all carry the wrong
claim. All three are corrected here / in the amended probe and Lean docstring.
The claim did NOT reach the PR body of #6180 (which is about the M_beta spectrum
and was written before this work) or any content block, audit doc, or witness
other than `qbeta-nf-counit-gap-order.witness.json`, which is regenerated.

PROBE: qbeta_nf_counit_gap_order_probe.py, now 17/17 with the retraction and the
entry-6 reproduction as assertions.


## 2026-08-30 (14) — the gate is not 0.58%: THREE builders, three alphas, spanning a SIGN CHANGE

Entry (11) gates branch 3 on the NF being "unsettled at 0.58%". That figure is
the COUNIT ratio 1.00579 between two builders. Measured on the PHASE, across
the three builders the tree actually contains (convention C, proton pin,
against the required N=1 factor 0.99839767):

    builder                       alpha        cos(alpha)    unexplained
    single-wrap                -0.0523361      0.99863078       +14.5%
    build_nucleon_nf (9 cr)    -0.0354101      0.99937313       +60.9%
    build_atom_nf (gluon)      +0.2355793      0.97237929       -1624%

The two bare-nucleon builders UNDER-correct; the gluon-complete one
OVER-corrects by an order of magnitude, with the opposite sign of residual.
**No choice among them is a small perturbation of another.**

### They are three different SYSTEMS, not three bases — read this before using the table

  single-wrap       bare A=1 nucleon. What the Q_beta counit chain is built on.
  build_nucleon_nf  bare nucleon, B_3 + quark crossings, 9 crossings. **Its own
                    docstring declares it DEFECTIVE**: "NO GLUON TERM -- and
                    this is a DEFECT, not a convention ... 6 (B_3) + 3 (quarks)
                    + 2 (gluon) = 11 is the SDP-consistent budget. Use
                    build_atom_nf." So the "typed" leg of entries (12)-(13) was
                    a known-defective builder.
  build_atom_nf     gluon-complete AND includes electrons (sigma_1^-1 per Z), so
                    `(0,1) - (1,0)` is neutron minus HYDROGEN -- the
                    atomic-mass convention beta^- decay actually uses, arguably
                    the physically right object, but a different object from
                    the bare-nucleon difference the other two compute.

So this is **not a convention to be picked**. It is a modelling question about
which system the Q_beta channel describes, and the answer moves the phase by
more than the phase. Choosing by which one fits best is exactly what the
anti-fit discipline forbids.

### A docstring defect found on the way — in tools/pyhecke, not fixed here

`pyhecke/atom.py:218` — `build_atom_nf`'s docstring still carries *"No separate
gluon dressing -- B_3 IS the gluon structure"*, the exact sentence
`build_nucleon_nf` retracts as unbacked **while redirecting to
build_atom_nf**. There it is not merely unbacked but **FALSE ABOUT ITS OWN
FUNCTION**: lines 252-253 and 264-265 apply `hm(nf, 1, 0, 0)` twice per
nucleon, commented "gluon 1"/"gluon 2". A prior agent corrected one docstring
and left its twin, and the redirect points at the uncorrected one. Code is
right, redirect is sound, only the line is stale. Wants its own change in
tools/pyhecke.

### Two errors of mine here, both caught by reading the body not the docstring

1. I hypothesised the two NFs were not competing, because "a free neutron is
   A=1 and has no nucleon pairs". **Wrong** — `build_nucleon_nf(quarks)` pairs
   are QUARK pairs within one nucleon (uu/dd/ud), so it does apply.
2. I then read the retraction as evidence that `build_atom_nf` has no gluon
   term either, on the strength of line 218. **Wrong** — the code adds two.
   Reading the docstring instead of the body is the same error that line causes
   in others.

### Consequence for the route table

Routes 1-4 stay closed; route 5 stays the only live one, and it is **more**
gated than entry (13) left it, not less. Before any holonomy construction can
be tested, the corpus has to say which of the three systems the Q_beta channel
is describing. That is an author-level modelling question, not a measurement I
can settle — and I have deliberately not settled it by picking the best-fitting
one.

PROBE: computations/qbeta/qbeta_three_nucleon_nf_alpha_spread_probe.py (5/5,
exact Fractions from build_atom_nf_exact carried into mpmath at 50 dps).
Gates: NEW dirty witnesses 0 on both ratchets.


## 2026-08-30 — 🟧 OWNER RULING: single-wrap is canonical for the Q_beta channel

Verbatim: **"single-wrap. it's A=1, no gluon, no electron"**.

The three-builder fork of entry (14) is settled, and settled STRUCTURALLY rather
than by residual: free-neutron beta decay is **A=1** — one nucleon, no nucleus —
so the gluon dressing and the electron that `build_atom_nf` carries describe a
different system.

    CANONICAL   single-wrap             bare A=1 nucleon                alpha = -0.0523361
    not this    build_nucleon_nf (9cr)  bare nucleon + quark crossings  alpha = -0.0354101
    not this    build_atom_nf           + gluons + electrons            alpha = +0.2355793

### Consequence 1 — the corpus split is CORRECT, not an inconsistency

Entry (14) framed the Q_beta chain (single-wrap) and the live mass compute
(`build_atom_nf`) as two objects of which "one is wrong for this channel".
**Under the ruling neither is wrong.** They describe different systems and each
is used where it belongs: a nucleus has gluon dressing and electrons, a decaying
free neutron does not. That is a resolution of the tension, not a choice between
its horns — and it retires the framing rather than deciding it.

No electron double-count: the framework's Q_beta carries `m_e` as an explicit
prefactor (`Q_beta = m_e * |q0^2-2q0-1|(q0+1)/(2q0^3)`), so the emitted electron
enters the Q-value there, not inside the normal form. The atomic-mass convention
comparing neutron to HYDROGEN is experiment's bookkeeping, not this
construction's.

### Consequence 2 — branch 3's acceptance test is UN-GATED

The retraction of entry (12) established that the NF choice moves `alpha` at
O(t), which is what gated the test. With one NF fixed there is no such freedom
left, so entry (6)'s acceptance test is runnable against a fixed object.

### Consequence 3 — and it immediately reads C, not D

With the builder fixed, entry (6)'s Kohno-Drinfeld test (does `alpha` look like
a holonomy angle `c*ln q`, `c` pinned at t^1 so t^2 is a PREDICTION) is
unambiguous:

    single-wrap C   t^1 -1/2   t^2 pred 1/4   actual 1/4   MATCH
    single-wrap D   t^1 -1/2   t^2 pred 1/4   actual 5/4   FAILS

**Under the canonical builder AND the canonical convention D, the ladder phase
fails the holonomy acceptance test at second order.** Entry (6) recorded this as
a "tension with the ruling" and could not press it, because the builder
ambiguity was a live alternative explanation. That alternative is now gone: the
t^2 failure is a property of convention D in this channel, not of a modelling
choice.

**Scope, carefully.** This does NOT overturn the 2026-08-15 convention-D ruling,
which is corpus-wide and about the trace convention; it is one channel's phase
failing one consistency test. It also does not make C right — entry (6) notes
C's own t^3 coefficient (-5/16) misses its prediction (-1/6), so C is not a
logarithm either. What is established is that the D reading of THIS phase now
carries a second-order defect with no remaining excuse.

### What the ruling does NOT do

It does not close the ladder. At the proton pin the canonical builder still
leaves **14.5%** of the required N=1 correction unexplained under C and **48.9%**
under D. The ruling picks the object; the residual is untouched.

### Route table

Routes 1-4 stay closed. **Route 5 (transcendental / holonomy) is now the only
live route AND is un-gated** — the first time in this bean's history that it is
attemptable against a fixed object. Its three-part acceptance test stands
(reproduce alpha through t^2; account for the -1/4 of Re(log-gap) and the
discarded i*pi; deliver a value below 1), with the added datum that any
construction must now explain why C passes t^2 where the canonical convention
does not.

PROBE: `qbeta_three_nucleon_nf_alpha_spread_probe.py`, now 9/9 — the ruling and
both C/D holonomy verdicts are assertions, not prose.


## 2026-08-30 — the C-passes-t2 tension DEFLATES: it is a bar-symmetry test in disguise

Chasing the tension entry (6) recorded (*"TENSION WITH THE RULING ... deepens
the recorded decayLadder_zC_threeRow_ne_zero tension"*). **It does not deepen
it. It restates it.**

### The chain, each link exact

1. With `q = 1+t`, `h = 2t - t^2 + ...`, the phase `alpha = (z-1)h/2` has

       t^1 coefficient = z(1) - 1
       t^2 coefficient = 1/4 + z'(1)        verified for BOTH conventions

2. Kohno-Drinfeld fixes the scale (`hbar = 2 ln q`), so a constant-residue
   holonomy angle is a multiple of `ln q`. Both conventions have `z(1) = 1/2`,
   pinning `c = -1/2` at `t^1`, and `c*ln q` predicts `t^2 = 1/4`.

3. Therefore **alpha is second-order logarithmic iff `z'(1) = 0`**.

4. **Bar-evenness FORCES `z'(1) = 0`.** Differentiate `z(1/q) = z(q)` at the bar
   fixed point `q = 1`: `-z'(1) = z'(1)`. **No property of the function is used.**

5. `z_C = sqrt(q)/(q+1)` IS bar-even — as `u/(u^2+1)` in `u = sqrt q` it is
   manifestly `u <-> 1/u` symmetric. `z_D = q^3/(q^2+1)` is not, `z_D'(1) = 1`.

### The deflation

C passes the `t^2` holonomy test **because it is bar-invariant**; D fails it
**because it is not**. These are not two facts. The corpus already knows z_D is
not bar-even — `QOU.Interactions.markovZC`'s docstring says so, and
`QOU.QBeta.DFrameBarAction` (this branch) proves the stronger form: the whole
bar ACTION changes shape, affine reflection under C vs multiplicative under D.

**So the t^2 failure is NOT independent evidence against convention D.** The
2026-08-15 ruling does not have to answer a second objection. Entry (6)'s
"tension" line should be read as an observation about z_D's bar parity, which
was already recorded, not as a new finding.

### 🛑 A CORRECTION to the branch-3 acceptance test

Entry (6) states part 1 as *"reproduce alpha through order t^2 (requires
z'(1) = 0)"*. Given link 4, **that part has ZERO discriminating power for route
5**: any construction over a bar-even `z` passes it automatically, and any over
`z_D` fails it automatically, whatever the construction is. It tests the Markov
parameter, not the holonomy hypothesis. Because the Lean theorem quantifies over
an arbitrary function, this is airtight rather than a property of two examples.

**Acceptance test, corrected to two parts:**
  1. ~~reproduce alpha through t^2~~  — VACUOUS, see above
  2. account for `alpha = -1/4` of `Re(log-gap)` AND the discarded `i*pi`
  3. be genuinely oscillatory, delivering a value BELOW 1
  (plus entry-10's corrected weight-cancellation constraint)

### And neither convention is a logarithm at all

`alpha` is **ALGEBRAIC**: exactly `-(u-1)(u+1)(u^2-u+1)/(2u^2)` in `u = sqrt q`
under C, and `(q-1)(q+1)(q^3-q^2-1)/(2q(q^2+1))` under D. `c*ln q` is
transcendental, so exact agreement is impossible in either convention. Measured
deviations from `-1/2 ln q`:

    alpha_C - c*ln q = -7t^3/48 + 7t^4/32 - 337t^5/1280 + ...   first at t^3
    alpha_D - c*ln q =    t^2   -   t^3/3 +     t^4/4   + ...   first at t^2

So C's advantage is exactly one order, and it is bought by bar-evenness rather
than by being closer to a holonomy.

LEAN: `QOU/QBeta/BarEvenForcesStationarity.lean` — 5 theorems, lean-direct
exit 0, zero warnings, #print axioms clean on all 5, zero sorryAx. The main
theorem `deriv_at_one_eq_zero_of_barEven` is stated for an ARBITRARY
differentiable `f` with `f(x⁻¹) = f(x)` near 1, which is what makes the
acceptance-test correction general.
PROBE: `qbeta_holonomy_t2_is_a_bar_symmetry_test_probe.py` (11/11, exact).


## 2026-08-30 — ROUTE 5: constant-residue holonomies EXCLUDED, and entry (7)'s "EXACT" is not exact

Two results, and together they mean the branch-3 acceptance test no longer
discriminates anything.

### 1. The exclusion — by the logarithm's FUNCTIONAL EQUATION, no transcendence

Kohno-Drinfeld fixes the scale (`hbar = 2 ln q`), so a **constant-residue**
holonomy angle is `c * ln q`. The obvious objection is transcendence — `alpha`
is algebraic, `c ln q` is not — but that needs transcendence theory. **The
elementary substitute needs none:** `ln(q^2) = 2 ln q`, so EVERY `c * ln`
satisfies `f(q^2) = 2 f(q)` whatever `c` is, and `alpha` fails it:

    C: alpha(q^2) - 2alpha(q)
         = -(2q^{7/2} - 2q^{3/2} + q^5 - 2q^4 - 3q^3 + 3q^2 + 2q - 1)/(2q^2(q+1))
    D: alpha(q^2) - 2alpha(q)
         = (q-1)^2(q+1)(q^9+q^8+2q^6+q^5+3q^4-q^3+q^2-q+1)/(2q^2(q^2+1)(q^4+1))

Both nonzero. **So alpha is not `c ln q` for ANY c, in either convention.**
Scope-(b), invariant named.

### 2. Entry (7)'s "EXACT: target / Re(log-gap) = -1/4" is a 0.32% APPROXIMATION

Measured at the proton pin:

    quantity          value          ratio to 2 ln q0     deviation from -1/4
    alpha_C        -0.05233612          -0.25079432             0.32 %
    alpha_D        -0.04048578          -0.19400756            22.4  %
    alpha_required -0.05661728          -0.27130960             8.52 %

And by result 1 it **cannot** be exact: exactness would give
`alpha = -(1/2) ln q`, which fails the doubling identity. Entry (7) states it as
EXACT and builds acceptance-test part 2 on it. It is not an identity, so there
is nothing exact there to account for — and a construction reproducing `-1/4`
exactly would be **wrong by 0.32%**.

### 🛑 Consequence: the acceptance test does not discriminate

    part 1  reproduce alpha through t^2         VACUOUS — a bar-symmetry test in
                                                disguise (previous entry)
    part 2  account for the -1/4 of Re(log-gap) RESTS ON A NON-IDENTITY
    part 3  deliver a value below 1             a sanity check, not a test

Both discriminating parts are defective. **This is a finding about the test, not
about the hypothesis** — it does not refute a holonomy origin for alpha; it says
the three-part test built over entries (6)-(8) cannot tell a right construction
from a wrong one, and should not be used to accept one.

### What route 5 still has — the exclusion is NARROW

Result 1 removes **constant-residue** connections only. A connection whose
residues depend on `q`, a non-flat construction, or a genuinely
`q`-dependent-parameter transcendental object is untouched and need not satisfy
the doubling identity. What is gone is precisely the Kohno-Drinfeld reading the
acceptance test encoded — which is why the test went with it.

### Honest position on route 5 after this session

Routes 1-4: closed. Route 5: its constant-residue horn is now closed too, and
its acceptance test is retired as non-discriminating. What remains is a
genuinely open construction problem with **no accepted test to judge a candidate
by** — building one is now part of the work, and a candidate accepted against
the old three parts would not have been evidence of anything.

LEAN: `QOU/QBeta/PhaseFailsLogFunctionalEquation.lean` — 9 theorems, lean-direct
exit 0, ZERO warnings, #print axioms clean on all 9, zero sorryAx. The doubling
lemma is stated for an ARBITRARY additive `L` and arbitrary `c`, so the
exclusion holds for every `c` at once rather than for a fitted one.
PROBE: `qbeta_phase_fails_log_functional_equation_probe.py` (7/7, exact
symbolic + mpmath 50 dps at the proton pin).


## 2026-08-30 — a REPLACEMENT acceptance test, in two tiers, with the burden stated

The retired test did not discriminate. This is its replacement, validated against
known-wrong candidates — **and carrying a correction of my own first draft.**

### 🛑 The correction: the supergolden zero is NOT a fingerprint

I first built the test around `alpha_D`'s zero at the **supergolden ratio**
psi = 1.4655712318767680 (real root of `q^3-q^2-1`), calling it *"a rigid
fingerprint no generic construction reproduces by accident"*. **Wrong twice:**

    z_D - 1 = (q^3 - q^2 - 1)/(q^2 + 1)      verified
    z_D(psi) = 1.0000000000                   verified

psi is **exactly where `z_D = 1`** — immediate from `alpha = (z-1)h/2`, not an
arithmetic coincidence. And it is **already in the corpus, twice**:
`QOU/Observations/centered_hecke_variance_positive.lean` names psi by value as
the `z < 1` threshold, and `predicted-spectra/spectrahedral-phase-collapse`
carries it as the convention-C Gram degeneracy at `u = 1/psi`, multiplicity 5.
Prior art, found by grep before the claim shipped rather than after.

**The consequence reshaped the test.** Since `alpha = (z-1)h/2` EXACTLY, its
zeros, poles and bar behaviour are all inherited from `z` and `h`. So every
output-side criterion is automatic for any candidate of the form `c*(z-1)h`.
They pin the constant `c` and nothing else.

### TIER 1 — necessary, cheap, rejects perturbations, NOT evidence alone

    D1 algebraic over Q(q)        closes the constant-residue holonomy horn
    D2 zero locus + multiplicity  inherited from (z-1)h
    D3 pole locus + multiplicity  inherited from z
    D4 bar defect exact           the only one that pins c

Nine independent conditions: 5 numerator + 3 denominator + 1 normalisation.

### TIER 2 — where the discriminating power actually is

    D5 NON-CIRCULAR   the construction must not take alpha, (z-1)h/2, or the
                      ladder residual as an INPUT. Entry (5)'s circularWitness
                      is why: for EVERY alpha a rotation matrix with trace
                      2cos(alpha) exists, built FROM alpha.
    D6 OVER-DETERMINED  fewer than 9 free parameters. A deg-5/deg-3 rational
                      function has exactly 9 after scaling, so 9+ tunables hit
                      all of tier 1 by FITTING and passing it is worth nothing.
                      A parameter-free construction meeting all nine is
                      over-determined by nine conditions — that is evidence.

D5/D6 check the **definition**, not the output, so no script can run them.
Stated explicitly so the burden is not quietly dropped again.

### Validation — the rejections, which the old test never had

    candidate                        D1 D2 D3 D4   OLD part1   verdict
    alpha_D (target)                  Y  Y  Y  Y       Y        PASS
    alpha_C (other convention)        Y  .  .  .       .        reject
    c*ln q (constant-residue)         .  .  .  .       .        reject
    NEAR-MISS alpha_D + (q-1)^3       Y  .  Y  .       Y        reject
    NEAR-MISS alpha_D*(1+(q-1)^3)     Y  .  .  .       Y        reject
    cosh-shaped                       Y  .  .  .       .        reject
    2*alpha_D                         Y  Y  Y  .       .        reject

**The near-miss row is the point**: it agrees through `t^2`, so the RETIRED test
accepts it and tier 1 rejects it. **The `2*alpha_D` row shows D4 is
load-bearing** — right zeros, right poles, wrong constant.

### What this does NOT deliver

Tier 1 is nearly free for anything built from `z`, and cannot detect a
construction handed `(z-1)h/2` — the same circularity that retired the old test.
**Only D5/D6 close that, and they are read, not run.** A candidate passing tier 1
while silent on tier 2 has shown nothing.

PROBE: `computations/qbeta/qbeta_route5_discriminating_test.py` (19/19; the
correction and the tier-1-is-automatic fact are assertions, not prose).


## 2026-08-31 — ROUTE 5's three survivors close at once: the generator must be ELLIPTIC

The constant-residue exclusion left exactly three survivors, recorded above as
*"a connection whose residues depend on `q`, a non-flat construction, or a
genuinely `q`-dependent-parameter transcendental object is untouched"*. **All
three close together**, by a sign argument that never reads the residues. Probe
`qbeta-holonomy-spectrum-sign-obstruction` (6/6), Lean
`QOU/QBeta/HolonomySpectrumSignObstruction.lean` (6 theorems, sorry-free, axioms
clean), write-up
`docs/audits/2026-08-31-qbeta-holonomy-spectrum-sign-obstruction.md`. Commit
`4471ee72ce`.

### The argument

The correction is read as a holonomy's normalised character — the
`EigenphaseCarrier` shape `tr M = 2 cos α`. Measured, it is **strictly below 1**:
`Q_β/Q_A = 0.998325`; ladder cosine factor `0.998399` (C), `0.998999` (D).

A generator with **real** spectrum `±a` has character `cosh a ≥ 1` for **every**
real `a`, equality only at `a = 0`. **The bound is quantified over all real `a`**,
so a `q`-dependent residue only changes which `a` occurs — the bound is unmoved.
That is the residue-independent step, and it is exactly what the doubling-identity
argument could not reach.

At the Kohno–Drinfeld value the miss is elementary. This bean's own scale-fixing
(`braiding = P exp(ħt/2)`, `t` eigenvalues `±1`, Hecke `{q, −1/q}`) gives
`ħ = 2 ln q`, **real** at the substrate's real `q₀ = 1.10998 > 1`, so the
generator eigenvalues `±ln q₀` are real and

    (q + 1/q)/2 − 1 = (q−1)²/(2q)

a square over a positive — never negative. **1.005448** against a required
**0.998399**: not merely off by 0.706 %, but **on the wrong side of 1**.

| `a` | `cosh a` | below target? |
|---|---|---|
| 0 | 1.000000 | no |
| `ln q₀` = 0.104341 | 1.005448 | no |
| 0.0566 | 1.001602 | no |
| 1 | 1.543081 | no |

No analysis, no transcendence, no appeal to `cosh`: the whole obstruction is
`(x−1)² ≥ 0`.

### What route 5 is left with

Not *"find a connection"* but **"find one whose generator is ELLIPTIC at real
`q`"** — `det A > 0`, spectrum `±iθ` with `θ = 0.0565947`, against
Kohno–Drinfeld's `det A = −(ln q₀)² = −0.010887 < 0`. The imaginarity has to come
from somewhere, and the corpus already names that place:
**`conj:im-q-physical-role`**, whose "phase coordinate" candidate role is exactly
this. Materially narrower and more checkable than the open construction problem
this bean recorded.

### 🆕 TIER-0 for the D1–D6 acceptance test

    D0  ELLIPTIC GENERATOR   the construction's traceless generator must have
                             det A > 0 at real q (spectrum +-i*theta), not
                             det A < 0. Kohno-Drinfeld's scale-fixing gives the
                             latter, so a candidate that does not say where its
                             imaginarity comes from has already failed.

Like D5/D6 it is **read, not run** — a condition on the *generator*, not on `α`'s
output. Distinct from the validation table's "cosh-shaped" row, which checks the
shape of `α` as a function of `q`, not a generator's spectrum.

**Scope-(b).** Does not show no connection exists, does not derive `α`, does not
adjudicate a convention, wires nothing.

---

## 2026-09-01 (13) — what the two carrier fields force at the CLASSICAL POINT, and the exclusion of the only D0-satisfying operator

[`qbeta_eigenphase_carrier_classical_limit_probe.py`](../computations/qbeta/qbeta_eigenphase_carrier_classical_limit_probe.py)
(5/5) ·
[`QOU/QBeta/EigenphaseCarrierClassicalLimit.lean`](../folio/quantum-observable-universe/lean/QOU/QBeta/EigenphaseCarrierClassicalLimit.lean)
(sorry-free).

Entry 6 expands `α` and tests it against a holonomy ansatz. **Nobody had asked
what the two `TransferMatrixSpectrum` fields force about `M` itself.** They force
three things, all cheap enough to disqualify a candidate before any construction.

**Falsifier checked first:** `χ^{(2,1)}` on `S₃` is `+2` on `e`, `0` on the three
transpositions, `−1` on the two 3-cycles — **trace 2 identifies the identity
class uniquely.** Had it not, everything below collapses to `tr M(1) = 2` alone.

### The three conditions

`α(1) = 0` (its `t¹` coefficient is `z(1) − 1 = −1/2` under **both** conventions),
so with `det M = 1`:

1. `tr M(1) = 2` and `det M(1) = 1` ⟹ charpoly `(x−1)²` ⟹ **`M(1)` is UNIPOTENT.**
   *Not* `M(1) = I`: at `q = 1` the algebra is `ℂ[S₃]` whose `(2,1)` block is all
   of `M₂(ℂ)`, so a nontrivial Jordan block is permitted.
2. `tr M` has **no `t¹` term** — stationary at the classical point.
3. its **`t²` coefficient is `−1/4`**, i.e. `d²/dt²(tr M)|₀ = −1/2`.

**1′ — a second, simpler reason route 1 is closed.** If `M` normalises a single
braid word's image, `M(1)` lies in the `S₃` image — finite group in char 0,
semisimple by Maschke, hence diagonalisable. Unipotent **and** diagonalisable
⟹ `M(1) = I`, so the word must degenerate to the **identity permutation**. Needs
only the classical point; no eigenphase computation.

### ⚠️ The acceptance test's part 1 is CONVENTION-BLIND on the trace

`tr M = 2 − t²/4 + O(t³)` **identically** for `z_C` and `z_D`, because the `t²`
coefficient of the trace depends only on `α`'s `t¹` coefficient, which is
`z(1) − 1 = −1/2` for both. They first differ at **`t³`** — `1/4` vs `5/4`.

So "reproduce `α` through `t²`", read on the trace, shows **nothing** about which
convention a construction belongs to. Discrimination lives at `t³`. (The `α`
expansions here reproduce entry 6's recorded coefficients — C: `1/4`, `−5/16`;
D: `5/4` — independently.)

### The exclusion — `Δ_L` fails at ORDER ZERO

Merged today (PR #6413, `qou-cds1` Step 26): `Δ_L = NF(n) − NF(p)` is the
corpus's **only elliptic** operator, i.e. the only one clearing this bean's
TIER-0 condition **`D0`** (`det A > 0`, spectrum `±iθ`). Its classical eigenphase
is **exactly `2π/3`**, because every NF coordinate carries `(q−1)(q+1)` and the
leading direction is `−(1 + T₁T₀)` with `T₁T₀` the `S₃` three-cycle.

| | |
|---|---|
| carrier requires | `tr M(1) = +2` |
| `Δ_L` gives | `2cos(2π/3) = −1` |
| gap | exactly `3` — the identity-to-3-cycle character distance |

**Structural, not a near-miss.** `Δ_S` is excluded more simply still: hyperbolic
at every real `q` (Step 26), so no eigenphase at all.

### Scope

Does **not** derive `α`, does not construct a carrier, does not adjudicate a
convention. It supplies a three-condition classical-point filter, shows it is
convention-blind through `t²`, and disqualifies both operators the `qou-cds1`
arc produced — including the only one that clears `D0`.

### Same day, second pass — how strong is that filter? Measured: a DISQUALIFIER

Condition 1 above is not scale-invariant (it is about the *normalised* `M`). The
invariant form: with `R := tr²/det`, a carrier needs **`R(1) = 4`**, i.e.
`disc = 0`, i.e. the underlying operator is **parabolic at `q = 1`**. `Δ_L` gives
`R(1) = 1`; `Δ_S` has `tr ≡ 0` so `R = 0`.

Writing `A(q) = Σ_b c_b(q)·B_b` in the NF basis, at `q = 1`:

```
disc A(1) = 4·Q_T − 3(c₃ − c₄)²,   Q_T = ½[(c₁−c₂)² + (c₁−c₅)² + (c₂−c₅)²] ≥ 0
```

so the **parabolic locus** is

```
2[(c₁−c₂)² + (c₁−c₅)² + (c₂−c₅)²]  =  3(c₃ − c₄)²
```

- **`c₀` is absent** — `disc(A + λI) = disc(A)`. And the three transposition
  coefficients enter **only through their differences**: their class sum
  contributes `0` to the `(2,1)` block, because `χ^{(2,1)}` vanishes on a
  transposition.
- **`Q_T = 0 ⟺ c₁ = c₂ = c₅`, and on the locus that holds ⟺ `c₃ = c₄`.** That
  stratum is exactly the **centre of `ℂ[S₃]`** — constant on each conjugacy
  class — which acts as a **scalar** on the irreducible `(2,1)` block (verified:
  `−b·I`, independent of the transposition weight). So `M(1) = I` exactly there.
  The centre is the distinguished stratum of the locus.

### ⚠️ Correction to my own recommendation, one entry up

I wrote that the filter "says what to build toward". **It does not.** Condition 1
is one quadratic equation on the six `c_b(1)`; conditions 2 and 3 constrain the
first and second derivatives of the `c_b` at `q = 1` — two more equations on
twelve new parameters. **Cumulative: 3 equations on 18 parameters.**

So the filter **rules candidates out cheaply** — including both operators the
`qou-cds1` arc produced, and every one of the six NF basis elements except
`γ = I` — but it does **not** tell a construction what to be. It is a
disqualifier, not a target. Route 2 ("arbitrary `M`") stays closed as circular
for exactly this reason: the two `TransferMatrixSpectrum` fields are one
equation on a four-dimensional matrix space, and the classical-point conditions
do not repair that.

Probe now 7/7.

### ~~On the `t³` discriminator — a cheap FIRST MILESTONE for branch 3~~ — **SUPERSEDED, same day, by the entry below**

> 🛑 The `ζ(3)` test proposed here targets the MONODROMY reading of branch 3,
> which the next entry closes by a cheaper argument (trace-invariance). No
> associator computation is needed. On the surviving OPEN-PATH reading the
> associator coefficients are not the obstruction either, because nothing
> forces that holonomy to be algebraic. Left in place, struck through, so the
> reasoning is legible.

Entry 5 fixes the one contentful target: *"build the KZ/Stokes connection whose
monodromy is the `H₃(q)` braiding on `V_(2,1)`, and compute its holonomy angle."*
That is a large construction. The `t³` discriminator suggests a much smaller
first check, which either kills the branch or licenses the build.

**The observation.** `α = (z−1)h/2` is **algebraic** in `q`, so its Taylor
coefficients at `q = 1` are **rational at every order** — `α_C = −t/2 + t²/4 −
5t³/16`, `α_D = −t/2 + 5t²/4 − t³/2`. But a genuine KZ holonomy angle for `B₃`
carries the **Drinfeld associator**, whose coefficients are multiple zeta values
— `ζ(2)` at weight 2, `ζ(3)` at weight 3.

**The proposed test.** Compute only the `t³` coefficient of the KZ holonomy angle
in the `(2,1)` representation. If a nonzero `ζ(3)` survives into it, that
coefficient is irrational and cannot equal `−5/16` or `−1/2`: **branch 3 closes
without building the rest of the connection.** If the `ζ(3)` term collapses — and
it may, since nested commutators can degenerate in a 2-dimensional
representation — the branch survives and the full build is licensed.

⚠️ **PROPOSAL, NOT A RESULT.** The rational half is established (`α` is algebraic;
its coefficients are rational). The `ζ(3)`-survival half is **not checked here**
and must not be quoted as though it were: whether the weight-3 associator term
contributes to the *eigenphase* of a 2-dimensional rep is exactly the thing the
computation would decide. Recorded because it makes the branch's first milestone
small and falsifiable, not because it settles anything.

Distinct from the exclusion already recorded at entry 4, which is about
`2cos(α)` being transcendental over `ℚ(q,z)` while Hecke characters are
algebraic. This one is about the **angle's own Taylor coefficients** versus
associator `ζ`-values — a different comparison, and it bites on branch 3, which
that exclusion explicitly does not reach.


---

## 2026-09-01 (14) — branch 3's MONODROMY reading is CLOSED by trace-invariance; only the open-path reading survives

[`qbeta_kd_monodromy_reading_closed_probe.py`](../computations/qbeta/qbeta_kd_monodromy_reading_closed_probe.py)
(4/4) ·
[`QOU/QBeta/MonodromyTraceInvariance.lean`](../folio/quantum-observable-universe/lean/QOU/QBeta/MonodromyTraceInvariance.lean)
(sorry-free).

Entry 5 words branch 3 as a connection *"whose monodromy reproduces the Hecke
braiding"*, escaping the rationality exclusion *"because a holonomy is
transcendental."* **That escape fails, in one line:**

> Kohno–Drinfeld gives holonomies **gauge-conjugate** to the braid-image
> matrices. **Conjugation preserves the trace**, and the carrier condition is
> **on the trace**.

So such a monodromy's trace is *exactly* some `tr ρ(w)`. Measured symbolically in
the `(2,1)` block, exactly in `q`:

- **`det ρ(σ) = −1` for all four generators**, so an even-length word has
  `det = +1` exactly. **The carrier's `M.det = 1` field is automatic and free on
  the braid image — it was never the obstruction.** Odd-length words have
  `det = −1` and cannot meet it at all, so the image splits cleanly by parity.
- **Every word trace lies in `ℤ[q,q⁻¹]`** — the seminormal radical
  `√(q⁴+q²+1)` cancels identically, as characters must. Ten words checked:
  `σ₀σ₁ ↦ −1`, `σ₀σ₁⁻¹ ↦ −(q⁴−q²+1)/q²`, `σ₀σ₁σ₁σ₀ ↦ (q⁴+1)/q²`, …
- **`(σ₀σ₁)³ = I` exactly, for every `q`** — verified as a matrix identity, not
  just a trace. The full twist generates the **centre of `B₃`**, so the `(2,1)`
  representation factors through **`B₃/⟨Δ²⟩ ≅ PSL(2,ℤ)`** and the achievable
  traces are indexed by conjugacy classes there: a countable set of Laurent
  polynomials.

`2cos((z−1)h/2)` is transcendental over `ℚ(q,z)` (entry 4). A Laurent polynomial
is not. **Branch 3 as entry 5 words it is CLOSED** — no Drinfeld associator, no
`ζ(3)`, no construction.

Entry 5's escape clause is the wrong reason, and worth naming: transcendental
matrix *entries* do not buy a transcendental closed-loop *trace* when the loop is
required to reproduce the braiding.

### What survives — and it is narrower than entry 5's wording

The **open-path / non-abelian Stokes** reading. An open-path holonomy is not a
monodromy — not a closed loop, not a braid-group image — so it is not
trace-pinned; and it is gauge-**dependent**, transforming by the endpoint frames
rather than by conjugation, which is exactly the hypothesis
`trace_conj_of_mul_eq_one` needs and does not get. Entry 5 cites *"Yekutieli
non-abelian Stokes"*, so this **is** the corpus's intended shape; its own wording
just does not capture it.

**Route table:** routes 1–4 stay closed. Route 5 remains the only live one, but
its branch-3 content is now the open-path reading **only** — the monodromy half
is closed.

Scope-(a). Nothing derived, proposed, wired or readmitted; no convention
adjudicated. No anchor required (exact symbolic identities in `q`).

## 2026-09-04 (session tender-keller, PR #6572) — three corrections to THIS BEAN, and a new two-number target

### A. The carrier is REPAIRED — this bean's central premise is stale

The bean says `TransferMatrixEigenphase`'s two fields encode none of the
spectrum claim (`-2 <= 2cos <= 2` and `cos(x) = cos(-x)`). That was true when
written. Commit `913fb1bf18` (2026-09-03, on `main`) replaced them:

    class TransferMatrixEigenphase (q : R) (M : Matrix (Fin 2) (Fin 2) R) : Prop where
      trace_eq : M.trace = 2 * Real.cos (eigenphase q)
      det_eq   : M.det = 1

i.e. `TransferMatrixSpectrum` itself, and `q_beta_cos_resummation` now genuinely
consumes it (`rw [h.trace_eq]`, negative control recorded).
`carrier_is_trivial` still stands as the record of the SUPERSEDED encoding.
**The bean's "Also needs doing (small)" item is done.**

### B. Route 3's closure is STRONGER than recorded — not Laurent, algebraic

The bean's argument is "every H_3 character lies in Z[q,q^-1], and cos of a
non-constant algebraic function is not a Laurent polynomial". The registry
flags that transcendence step as an unproved docstring assertion. The live
Lean does not need it: `QOU.QBeta.BraidImageEigenphaseAlgebraic`
(`coeffs_zero_of_surjective_nonpos`) excludes **any algebraic relation of any
degree**, by zero-counting.

**But read its hypothesis before citing it.** It requires alpha to be
SURJECTIVE onto the non-positive reals (`alphaC_surjective_nonpos` /
`alphaD_neg_surjective_nonpos`). That is a property of the unbounded
`(z-1)h/2` family. An `arccos`-valued alpha is bounded in `[0, pi]`, fails the
hypothesis, and **the theorem never engages**. So "it is algebraic, therefore
excluded" is false; the exclusion is about unboundedness, not algebraicity.

### C. NEW — the "802 fine-tuning signature" is coordinate-dependent

Probe: `computations/qbeta/qbeta_eigenphase_character_coordinate_probe.py`,
witness `qbeta-eigenphase-character-coordinate.witness.json`, 3/3 assertions.

`docs/audits/2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md` rejects
the `(z-1)h/2` family because a viable z needs `z = 0.4991044802`,
`dz/dq = +400.2896759` -- slope/value **802** -- "a fine-tuning signature, not
a derivation". In the character coordinate `P := tr M = 2 cos alpha` the same
constraint is `P = 1.997259194490263`, `|P'/P| = 2.176`. Exact algebra:

    (z'/z)/(P'/P) = -2/(h*z*tan alpha) ~ -2/(h*z*alpha)

measured 369.74 vs closed form 365.76 (1.09 %, and that residual IS the dropped
`2*alpha*h'/h^2` term). **The factor is large because alpha is small**, which
is forced by the ladder's correction being small. So slope/value in z cannot
discriminate: every candidate with a small phase carries it. Scope-(b).

**This does NOT rescue the `(z-1)h/2` family** and I am not claiming it does.
That family stays excluded by the OTHER argument in
`qbeta-ladder-required-phase.witness.json`: `d(alpha_req)/dq = +41.53` vs
`d(alpha_C)/dq = -0.455`, opposite signs, curves crossing transversally. A
derivative sign disagreement is invariant under this reparametrisation. What
changes is what the exclusion rests on, not the exclusion.

### D. NEW — the derivative empties the declared basket. This is the deliverable.

`qbeta_d_frame_terminus_probe.py` correctly calls its value match "basket
distance, not isolation" -- six declared forms within 0.7 %. Tested on BOTH
constraints at the proton pin:

  form                  value miss   |P'/P|   vs required 2.176
  2 - h^4                  0.042 %   0.0331   65.7x too flat
  2 - h^2/8                0.136 %   0.0475   45.8x too flat
  2 (identity word)        0.137 %   0        slope exactly 0
  2 - 3h^4                 0.150 %   0.0996   21.8x too flat
  chi^(2,1)(B_3)           0.154 %   0.1018   21.4x too flat
  [2]_q                    0.683 %   0.0937   23.2x too flat
  tr M_4_1                 145.6 %   1.7363   1.25x too flat

Value alone separates the six by a factor 17. Log-slope separates the same six
by one to two orders and **empties the basket**. The only form within 1.25x on
slope is `tr M_4_1`, whose value is -0.911.

**The entropy objection is about matching ONE number.** The second constraint
is independent and free -- a derivative of the same committed ladder, no extra
experimental precision. A derived candidate now has a two-number target:

    P(q0) = 1.997259194490263   (+/- 5.7e-7 relative, from the |c3|<=1 window)
    |P'/P|(q0) = 2.176          (~4 figures; d(alpha_req)/dq is a central
                                 difference at +/-1e-4 relative in q)

`2cos` is even, so only `|P'/P|` is branch-independent.

Scope-(a) on the basket: no DECLARED form passes; not a proof that no Laurent
polynomial does.

### E. Two housekeeping items found by the corpus-grep, NOT actioned here

1. **Bean `qou-xjh4` (created 2026-09-03) is already wrong.** It asserts branch
   3 is "the only remaining option" and "NOT ATTEMPTED, by anyone". Both false
   against main: `0ed8fcbc61` closes the constant-residue horn, `4471ee72ce`
   proves the elliptic-generator requirement, `f65a953dd3` closes Im(q) as the
   imaginarity source. It also attributes branch 1's exclusion to
   "transcendence over Q(q,z)" -- the unproved docstring assertion, not the
   proof that exists. Someone should reconcile it with this bean.
2. **`qbeta_d_frame_terminus_probe.py:7-14` transfers the MASS channel's
   two-row cap to the DECAY channel** ("DERIVED, not a ruling ... so z = z_D is
   FORCED") and calls `qou-n1dj` "resolved". That contradicts
   `QOU/QBeta/DecayFibreBarParity.lean` (whose sorry-free
   `threeRow_undetermined_by_decay` shows the cap is *undeterminable* by the
   decay pairing at any precision), the trace-convention registry, and
   `qou-n1dj`'s own status (`todo`, "Item 1 is untouched"). The probe's
   headline verdict inherits the transfer.


## 2026-09-04 — D0 does not need theta, and two of my own readings were wrong

Arrived here on the author's instruction to "re-derive c_3 under convention D",
ran the corpus-grep first, and it stopped two errors before they landed. Both are
recorded because the second is the more instructive.

### ERROR 1 (withdrawn): "the D0 target is C-frame; it should be 0.0447444"

Verified from scratch at 40 dps, not taking this bean's labels on trust:

    C  z=sqrt(q)/(q+1)   alpha_N1 = -0.05659473754   cos = 0.9983989453
    D  z=q^3/(q^2+1)     alpha_N1 = -0.04474439462   cos = 0.9989991366

This bean's TIER-0 `theta = 0.0565947` is `|alpha_N1|` in convention **C** to 7
significant figures, which looked like a C-frame number sitting in the tier-0
gate of a convention-D bean — the exact class the `qou-9ugp` drain has been
clearing all session.

**It is not.** `docs/audits/2026-08-25-qbeta-ck-ladder-convention-d-eigenphase-window.md`
labels `-0.04474439` explicitly as **"D, naive `z`-swap (banned)"**. My proposed
correction would have installed a BANNED value in the acceptance test. The
corpus's live D candidate is the **bar-odd derived** `-0.05567095` (that audit
§2), which is within 1.7 % of the C figure this bean quotes — so quoting the C
value here is at worst imprecise, not a frame error. **Withdrawn.**

### ERROR 2 (corrected): I computed the banned object and did not recognise it

Earlier in the same session I reconstructed a `c_3` and got **-974.07 / -974.12**,
reported it as "not the canonical c_3" and moved on. That was true and far too
weak. It is the **naive z-swap**, which that audit's calibration table records at
**-974.43** — a named object this corpus has explicitly banned, and the reason
AGENTS.md says "this is NOT a z-swap". Getting -974 was not an artefact of my
reconstruction; it was me performing the banned substitution.

### What actually survives — D0 needs no target value

The elementary obstruction reproduces exactly:

    ln q0                    = 0.10434072032
    det A (Kohno-Drinfeld)   = -(ln q0)^2 = -0.0108869859168     (bean: -0.010887)
    cosh(ln q0) = (q+1/q)/2  = 1.00544843335                     (bean:  1.005448)
    cosh(ln q0) - 1 == (q-1)^2/(2q)   verified to 9e-42

And it generalises off the single target. This bean argues D0 against C's
`0.998399`. It does not need it:

    C, as recorded             cos = 0.998398945114   < 1
    D, naive z-swap (banned)   cos = 0.998999136781   < 1
    D, bar-odd derived         cos = 0.998450772846   < 1

`cos(theta) < 1` for **every** `theta != 0`, and `cosh(a) >= 1` for **every**
real `a`. So the real-spectrum exclusion holds for any nonzero real eigenphase,
in any convention, whatever the D value turns out to be.

**Consequence, and it is the useful part:** D0 is applicable NOW. It does not
wait on the D eigenphase being derived. A candidate generator can be screened on
`det A > 0` alone — the question is only whether the construction supplies
imaginarity at real `q`, never what `theta` equals. Restating D0 that way removes
its one dependence on an unsettled number.

**Scope (b) for the exclusion** (`(x-1)^2 >= 0` is a proved invariant, quantified
over all real `a`), **scope (a) for everything else**. Derives no `alpha`,
adjudicates no convention, wires nothing.


## 2026-09-04 (2) — Route A's "impossible" is OBSERVABLE-level, and D0 only bites at real q

Following the author's instruction to chip at where the imaginarity comes from.
Read `ImQCannotSupplyEllipticGenerator.lean` first; it closes routes A and B and
leaves the conjecture's **chirality** role untouched. That is the gap examined here.

### The two closed routes share a hypothesis, and it is an evaluation point

`abs_sq_gt_one {x y} (hx : 1 < x) : 1 < x² + y²` and everything built on it carry
`1 < Re q`. Candidate (i) — chirality — lives in the Kashaev regime, `q` on or near
the **unit circle**, where that hypothesis simply fails:

    arg q = 0.05659474 :  Re q = 0.998398945114   1 < Re q ?  False   |q| = 1
    arg q = 0.04474439 :  Re q = 0.998999136781   1 < Re q ?  False   |q| = 1
    arg q = 0.05567095 :  Re q = 0.998450772846   1 < Re q ?  False   |q| = 1

So the Route-A exclusion does not reach candidate (i). It is not wrong; its
hypothesis is the substrate's **archimedean evaluation point**, and the record
reads "impossible, since Re q = 1.10998 > 1" without that scope. `qou-cds1` draws
exactly this distinction 5,000 lines earlier for the complex-volume route —
"cannot supply the D-frame correction **at the observable level** AT ALL ... must
first close a FIBRE-level construction" — and the elliptic-generator entry does
not carry it.

### At |q| = 1 the generator is elliptic BY CONSTRUCTION

`ln q = iθ` exactly, so spectrum `±iθ` and `det A = +θ² > 0`:

    C, as recorded       cos θ = 0.998398945114   det A = +0.0032029646
    D, naive (banned)    cos θ = 0.998999136781   det A = +0.0020020604
    D, bar-odd derived   cos θ = 0.998450772846   det A = +0.0030992547

and the character `(q + 1/q)/2 = cos θ` reproduces **any** sub-unit target
exactly. **That last point is a tautology, not evidence** — θ was chosen as
`arccos(target)`. What it establishes is only that the modulus-1 locus is
precisely the set where the generator is elliptic *and* the character sub-unit,
so no tuning is required there.

### Consequence, and it sharpens my own D0 entry above

The frontier as recorded — *"find one whose generator is ELLIPTIC at real q"* —
asks for something the proved argument forbids. Ellipticity is free off the real
axis and impossible on it. **So D0, which I argued above is applicable without
knowing θ, is a screen against REAL-q constructions specifically**; off the real
axis it excludes nothing. That is a real limit on the criterion I proposed, and
it belongs beside it.

The open problem is therefore not "supply imaginarity" — candidate (i) supplies
it and passes D0 identically — but **the bridge**: a fibre-level connection at
`|q| = 1` whose archimedean evaluation sits at `|q₀| = 1.10998`, an 11.0 % gap in
modulus. That is the fibre-vs-observable structure AGENTS.md already names, and
it is where this route's remaining content is.

### Also filed: `qou-c66b`

Chipping at the conjecture directly turned up that its stated obstacle — *"no
mass observable can detect Im(q)"*, candidate (iii) *"needs a categorical formula
for decay widths Γ"* — overlooks `Q_β`, whose formula modulus-projects **one of
three factors**, making it Im(q)-sensitive with `∂Im(Q_β)/∂Im(q) ≈ 3.418` while
the mass shape is invariant to the last digit. Requiring `Im Q_β = 0` then forces
`Im q = 0` from a decay observable. Caveat there is load-bearing: the complex
extension of `Q_β` is mine, not the corpus's.

Scope (a) throughout — no `α` derived, no construction proposed, nothing wired.


## 2026-09-12 — route-option triage for the BRIDGE, after entry (2026-09-04 (2)) reshaped the gap

**Not a new result** — no `α` derived, nothing wired. This records which attacks the
corpus is already *equipped* for, so the next agent does not re-survey. **Scope:
read from this bean's section headers and its latest entry, not all 1684 lines.**

**The gap as it now stands.** Routes 1–4 closed; route 5's only survivor is the
open-path reading. Entry 2026-09-04 (2) establishes that **ellipticity is free at
`|q| = 1` and impossible at real `q`**, so the previously-recorded frontier
("find one elliptic at real q") asks for what the proved argument forbids. The
gap is the **bridge**: a fibre-level object at `|q| = 1` whose archimedean
evaluation lands at `|q₀| = 1.10998` — **11.0 % in modulus**. AGENTS.md's
fibre-vs-observable banner names this structure and its resolution shape.

**A — Habiro ring / roots of unity.** A Habiro element is *determined by its
values at roots of unity*, i.e. on `|q| = 1` — exactly the elliptic locus — and
extends to real `q`. Assets on main: `qbeta_habiro_wenzl_tower_zeta_n.py`,
`qbeta_habiro_delta_am_partial_sum_scan.py`, `qbeta_ohtsuki_sixone_kappa_series.py`,
`def:qz-bicompletion`. AGENTS.md names this as the right reformulation.
*Best structural fit; risks circularity — the Habiro-element construction is part
of what `qou-cds1` waits on.*

**B — Faddeev quantum dilogarithm / modular double.** `Φ_q` lives on **both**
sides (`|q| = 1` and `|q| ≠ 1`), related by modular inversion `b → 1/b`: the
textbook bridge for this exact modulus gap. **And the corpus has Lean:**
`QOU/Mathlib/FaddeevRatioPeriodic.lean`, `FaddeevSolutionSet.lean`,
`QOU/MathlibExt/FaddeevPhiBRealIntegral.lean`, plus
`stochastic-mechanics/phi-q-aj-machinery-identification-details.md` and
`quantum-observable-universes/q-dilogarithm-pentagon-associator.md`.
*Cheapest formalize-first step of the four.*

**C — Stokes / resurgence.** If `α` is a **Stokes constant** rather than an
evaluation, it is complex by nature and *defined by continuation across the gap* —
which dissolves the "elliptic at real q" impossibility instead of fighting it.
AGENTS.md lists Stokes-constant extraction as open research, so parallel attack is
permitted.

**D — two evaluation points** (`α` at `|q| = 1`, mass at real `q₀`).
**Listed to mark it as the trap:** a second anchor is a fourth calibration under
CAL-1/2/3. Cheap and almost certainly forbidden.

**Two traps already in this bean, restated so they are not re-run as results:**
1. `θ = arccos(target)` reproduces **any** sub-unit target exactly — this bean
   already says that is *"a tautology, not evidence"*.
2. `qou-c66b`'s Im(q)-sensitivity of `Q_β` (`∂Im(Q_β)/∂Im(q) ≈ 3.418`) carries its
   own caveat: the complex extension of `Q_β` is the recording agent's, not the
   corpus's.

**Judgement, not a finding: attack B.** The Lean assets exist, so formalize-first
is cheap, and the modular double is the standard tool for this modulus bridge.
A is the better structural fit but risks circularity.

**Why this matters downstream:** `qou-iagg` (the second dashboard re-score) waits on
`qou-cds1`, which waits on this. The dashboard's `Q_β`/`m_n`/`Δ_pn` rows are
base-only at ~1.7e+8 ppb precisely because no ladder exists on an admissible base;
on the retired `z = 1` base the ladder was worth 1312×.

---

## 2026-09-13 (later still) — attack C is closed too, by two results already on `main`

With A and B measured earlier today, **C (Stokes / resurgence) was the one route
I recommended as having no measured negative against it.** That recommendation
was also wrong. The corpus already carries **two independent negatives**, and
neither needed a new probe — this entry is a synthesis with citations, not a
measurement.

**No new compute was written for this entry.** Every figure below is read from
an existing artifact and re-derived only where re-deriving was one line.

### C-negative 1 — the channel where `α` lives is CONVERGENT

[`2026-07-12-borel-alien-calculus-utilization-audit.md` §C4](../docs/audits/2026-07-12-borel-alien-calculus-utilization-audit.md)
records the three-probe contradiction as resolved into a **channel dichotomy**,
scope-**(b)** with cited invariant (the bridge growth-obstruction audit):

| channel | growth | resurgent structure |
|---|---|---|
| **even** (4₁ / Ohtsuki) | Gevrey-1 **divergent**, ratios 1.32 → 3.63 → 4.93 rising without bound | yes |
| **odd** (the **Q_β ladder**) | **convergent**, KC8 simple pole, `c_{k+1}/c_k → 1/u = 117.41` plateau | **no** |

**A convergent series has no Stokes constant to extract.** The Stokes phenomenon
*is* the resummation ambiguity of a divergent asymptotic series; where the sum is
unambiguous there is no ambiguity for `α` to be. So "`α` is a Stokes constant"
has nothing to attach to **in the channel the Q_β ladder occupies**. The *even*
channel does have resurgent structure — but that is the 4₁/Ohtsuki object, not
where `α` lives.

### C-negative 2 — and "resurgence at the anchor" is refuted outright

[`qbeta_c3_uq0_radius_branchpoint_probe.py`](../computations/qbeta/qbeta_c3_uq0_radius_branchpoint_probe.py)
(bean `qou-iyj5`) computes the radius of convergence of the figure-8 argument map
`u(q₀)` directly, from the branch points of the A-polynomial's longitude
discriminant — exact algebra, no numerical integration:

    disc_L A = (M−1)²(M+1)²(M²+1)²·(M²−M−1)(M²+M−1)(M²−M+1)(M²+M+1)
    nearest geometric branch point: M² = φ² = (3+√5)/2
    ⇒ R = 2·log φ = 0.962423650119        (the GOLDEN RATIO)
    anchor u = ln q₀ = 0.10434072032 = 0.108·R      — deep inside

and validates its own A-polynomial + `u`-convention against the corpus's
**sorry-free** leading coefficient `(√3/4)u²`
(`FigureEightComplexVolume.lean`) via a Puiseux expansion at `u = 0`. Its verdict,
verbatim: *"The on-anchor-singularity / resurgence-at-anchor reading is
REFUTED."* There is no singularity near the anchor for a Stokes phenomenon to
live at.

### What is NOT settled — and it is a specific, cheap measurement

**The two negatives govern two different objects, and neither touches a third.**
Per the notation register's `u` ruling, say which `u` you mean:

| `u` | value | governed by |
|---|---|---|
| `u = ln q₀` (geometric argument map) | **0.10434072032** | C-negative 2 — analytic, R = 0.9624 |
| `u_ladder = b·ℏ_q²` | **0.00851999999989** | C-negative 1 — convergent channel |

They differ by **12.25×**. Now the loose end: C-negative 1's own recorded plateau
is `c_{k+1}/c_k → 117.41`, and `1/u_ladder = 117.370892020289747`. Those agree to
**0.033 %**. If the plateau really is `1/u_ladder`, the ladder's generating
function has its nearest singularity at radius `≈ u_ladder` — i.e. **the ladder
is evaluated at or extremely near its own radius of convergence**, where the term
ratio `(c_{k+1}u^{k+1})/(c_k u^k) → 1` and the ratio test is inconclusive. Which
side of the boundary is **not determined** by a plateau quoted to four figures:
117.41 > 117.3709 would put the pole *inside* the evaluation point.

**I am flagging this, not claiming it.** It is a candidate, it is cheap to
settle (re-read the extracted `c_k` and compute the ratio to full precision
rather than to a rounded plateau), and it sits in a *third* object that neither
existing negative covers. It also does **not** rescue attack C: a pole at the
evaluation radius is a convergence problem, not a Stokes constant.

### Where that leaves the triage — all four routes are now accounted for

| route | status |
|---|---|
| **A** Habiro | bridge closed at both admissible functionals (this bean, earlier today) |
| **B** Faddeev / modular double | inert at the real substrate inside the derivable `z`-window (earlier today); intact on the root-of-unity face |
| **C** Stokes / resurgence | closed by two independent results already on `main` (this entry) |
| **D** two evaluation points | the trap — a fourth calibration under CAL-1/2/3 |

**Recommendation — judgement, and it is the third I have given today; read that
as a reason to trust it less, not more.** The triage's four routes are
exhausted, so the honest next step is **not** to pick among them: it is to
accept that `α` needs a route the triage does not list, and to say so in the
bean rather than keep re-ranking four options that have each been measured out.
The one structural fact that survives all of today's measurements is the
replacement carrier the bean already states and leaves uninstantiated —
`TransferMatrixSpectrum (q) (M) : M.trace = 2·cos(eigenphase q) ∧ M.det = 1` —
whose discharge needs `M` produced from the **Hecke seminormal representation on
V_(2,1)**, the "downstream work" the original docstring defers. That is the
target; it is not one of A-D.

**Default if nothing is done:** the triage still reads "attack B, cheapest
formalize-first step of the four", and now all four have been measured against.

**Bean stays `in-progress`.** `α` is underived and this entry derives nothing —
per rule 13a it is not closeable while the conjecture is open.

---

## 2026-09-13 (same hour) — CORRECTION to the entry above, and a real finding underneath it

The entry above flagged a "loose end": that C4's plateau `117.41` and
`1/u_ladder = 117.370892` agree only to **0.033 %**, so the ladder's pole might
sit just *inside* its evaluation point. **That gap does not exist. I
manufactured it.**

### What I did wrong

I took `u_ladder ≈ 0.00852` from AGENTS.md's **rounded prose** and inverted it to
get `b = 0.8678657617`. That is circular — a constant back-derived from a
rounded figure. The exact Hoefsmit coupling is in the corpus:

    b = sqrt(q^4 + q^2 + 1)/(q^2 + 1)     [qbeta_d_n2_factor_bar_invariance_probe.py:50]
      = 0.86758406696525115565            (proton pin, mp.dps = 50)

giving `u_ladder = b·ℏ_q² = 0.0085172345501561421893` and
**`1/u_ladder = 117.409001`**. The recorded `117.41` is right to every figure it
quotes. My `117.370892` was the inverse of the rounded prose, not of `u`.

**The rule this cost me: a rounded figure in prose is not an input.** AGENTS.md
quotes `u ≈ 0.00852` as an orientation number; using it to solve for another
constant reintroduces the rounding as a fake signal. That is the second time
today a phantom discrepancy came from taking a documented figure as data — and
this document warns about exactly that, repeatedly.

### What survives, and it is KC8's own claim rather than my inference

The gate block hardcodes

    noncomputable def u_substrate : ℝ := 0.008517234550156142
      [q-beta-radius-of-convergence-gate.lean:75]

which agrees with the live `u_ladder` to **2.2e-17** — the same number. So there
is no discrepancy anywhere, and the gate is self-consistent.

But that is precisely what makes the structural point sharp. KC8's registered
statement is

> *"`g(u) = sum c_k u^k` has its nearest singularity (simple pole) at
> `u_substrate`; ratio test `c_{k+1}/c_k -> 1/u_substrate`"*
> — `kernel-constraints-registry.json`

and `u_substrate` **is** the point at which the ladder is evaluated. So the
ladder is evaluated **exactly at its own radius of convergence** — not just
inside it, not just outside it, but on the boundary, by KC8's own construction.
Which side is therefore not a numerical question at all; it is definitional.

### The finding that actually matters — KC8 is NOT a proved invariant

| where | tier |
|---|---|
| `ck-dk-canonical-registry.md` row 348 | `gate §4(a), **empirical basis**` |
| `kernel-constraints-registry.json` | `"tier": "gate"` |
| `q-beta-radius-of-convergence-gate.lean` | **0 sorries**, and **two `axiom` declarations**: `qBetaLadderCoefficients : ℕ → ℝ`, `qBetaCandidatePoleLocation : ℝ` |

That is the *"sorry-free ≠ derived"* / §"Axiomatization is NOT a Proof" shape:
the file compiles clean because the content is axiomatised, not derived.

**Consequence for the entry above.** The growth-obstruction audit labels its
channel dichotomy **"scope-(b) with cited invariant"**. AGENTS.md's rule for
scope-(b) is explicit — a structural exclusion is *"only permitted when a
**proved invariant** forbids it … Cite the invariant. Without one, you may not
write (b)."* On the odd side the cited invariant is KC8, which the registry
tiers **empirical/gate** and whose Lean is **axiom-backed**. So the scope label
is stronger than its own tier on that side.

**This does NOT overturn the audit's arithmetic.** Given both growth classes as
measured, a factorially-divergent series and a positive-radius one cannot be
equated term-by-term; that contrast holds. What is over-labelled is the tier,
not the comparison.

### So attack C stays closed — on C-negative-2, not C-negative-1

- **C-negative-2 is unaffected and is the load-bearing one**:
  `qbeta_c3_uq0_radius_branchpoint_probe` is exact algebra from the
  A-polynomial's longitude discriminant, validated against the corpus's
  sorry-free `(√3/4)u²`. `R = 2 log φ = 0.9624`, anchor at `0.108·R`. *"The
  on-anchor-singularity / resurgence-at-anchor reading is REFUTED."*
- **C-negative-1 should be cited as empirical, not as a proved invariant.** It
  still says what it says; it is simply not a scope-(b) foundation on its own.

**Net: attack C remains closed, and my own framing of why was one tier too
strong.** Fourth correction of my own work on this bean today.

---

## 2026-09-13 — route 5's ellipticity requirement is on the RETIRED base, and on the ruled base it INVERTS

Probe: [`qbeta_route5_ellipticity_target_is_on_a_retired_base_probe.py`](computations/qbeta/qbeta_route5_ellipticity_target_is_on_a_retired_base_probe.py)
— 6/6, proton pin, 50 dps, scope (b) for the two class statements / (a) for the
numbers.

**Steps 18→19→20 are one chain hanging on one number.** Step 18
(`HolonomySpectrumSignObstruction`) excludes real-spectrum holonomies because
their character is `cosh a ≥ 1` while the required correction is `0.998399 < 1`
⇒ **needs elliptic**. Step 19 (`ImQCannotSupplyEllipticGenerator`) refutes `Im q`
as the source at the archimedean level. Step 20
(`qbeta_fibre_unit_circle_opens_route5_probe`) puts the locus on the fibre at
`|q| = 1`, reducing it to "is `θ/2π` rational", with `N = 111` the only
low-denominator candidate.

**That number is computed on the `z = 1` cell.** Measured, not asserted: route 5
uses `θ = acos(Q_β^exp/(Q_A(1−u²)))` with `Q_A = m_e|q²−2q−1|(q+1)/(2q³)`, and
this probe reproduces its printed `0.05661730079406103` **to 1e-14** from that
formula. The owner **retired `z = 1` as the base on 2026-09-08**. All three
step-18/19/20 files are `87bf883793`, dated **2026-09-07** — **correct when
written**, stale by a ruling one day later. Same class as the attack-A finding in
#7326, second arc.

**On the ruled base the requirement inverts.** `R(base) = Q_β^exp/(base·(1−u²))`:

| base | Q_base (MeV) | R | consequence |
|---|---|---|---|
| `z = 1` (Form A) — **RETIRED** | 0.783645827375 | **0.998397668719** | needs elliptic |
| `z_D = q³/(q²+1)` — **RULED** | 0.444700408522 | **1.75936462427** | elliptic **excluded** |
| `z = q` (augmentation) | 0.87989056126 | **0.889190317068** | needs elliptic |
| dashboard scored cell — **RULED** | 0.65185631006 | **1.20024943393** | elliptic **excluded** |

An elliptic generator has character `cos θ ≤ 1` (`Real.cos_le_one`, the invariant
the carrier file's own `replacement_excludes_some_matrix` already uses), so on
both ruled bases `acos(R)` is **not real** — the exact mirror of step 18. What
the ruled base asks for instead is the class step 18 excluded, at
`a = arccosh(R)` = **1.16530530037** (`z_D`) / **0.622738411685** (dashboard).
So steps 19 and 20 — `Im q`, `|q| = 1`, `θ/2π` rational, `N = 111` — are
downstream of the **opposite** requirement and do not arise on the ruled base.

**The direction is base-dependent, not uniform.** The augmentation keeps
`R < 1`. So "route 5 needs an elliptic generator" is a fact about *which
admissible functional is the base*, not about the framework — invisible while
only the `z = 1` cell was in view. **This is not a reason to prefer a base**:
per §NO FITTING a base is never chosen by which obstruction it removes, and the
ruled base is ruled whatever it does to this chain.

**It does NOT resurrect Kohno–Drinfeld.** KD's own `cosh(ln q₀) = (q₀+1/q₀)/2 =
1.00544843335` misses R by **−42.85 %** (`z_D`) and **−16.23 %** (dashboard).
The failure moves from a **class** exclusion (wrong side of 1) to a **magnitude**
gap (right side, wrong size) — weaker, and a different problem.

**Not retracted:** steps 18–20's algebra is exact and correct for the target they
were given. What changed is the target.

### Secondary: `θ = 0.0565947` in prose is the convention-C FORM value

Live at three sites, **all in `87bf883793` — the same commit whose probe corrects
the target to the experimental `0.05661730079`**:
`EigenphaseCarrierVacuity.lean:221`, `BringEllipticCurveJInvariant.lean:39`,
`nuclear-interactions/q-beta-cos-resummation.lean:191` (plus this bean and
`qou-cds1`). The gap is **3.99e-4**, which is precisely route 5's own documented
"moved it by 4.0e-4" form-vs-experiment correction; this bean records 0.0565947
as `|α_N1|` in convention **C** to 7 digits.

**NOT swept.** On the ruled base `θ` does not exist at all, so these need
*re-deriving*, not re-numbering — and the 2026-09-07 ask-first directive governs.
Recorded for the owner.

**How it was found, and it is my own error:** this probe's first draft took
`0.0565947` from that Lean prose as its reproduction target and **failed its own
check 1**. A rounded figure in prose is not an input — the third time this
session I have had to relearn that, and the second time it produced a phantom
discrepancy before the producer was run.

### What is next

`trace_eq` is still the open field. What the ruled base now asks for is a
real-spectrum generator at `a ≈ 1.165`, against KD's `ln q₀ = 0.104` — a factor
**11.2**. That is the concrete, falsifiable target replacing the elliptic ask,
and nothing in the corpus supplies it yet.
## 2026-09-13 — attack B measured: INERT at the substrate, inside a derivable z-window

The route triage above recommends **attack B (Faddeev `Φ_b` / modular double)**
as *"the textbook bridge for this exact modulus gap"*, on the judgement that the
Lean assets make formalize-first cheap. Measured at the real substrate, the
bridge does not bridge, and the corpus already half-held the reason **five days
before the triage was written**.

Probe: [`computations/qbeta/qbeta_phib_dual_validity_window_probe.py`](../computations/qbeta/qbeta_phib_dual_validity_window_probe.py),
5/5, witness `qbeta-phib-dual-validity-window.witness.json`, proton pin, scope (a).

### 1. The premise was already excluded on `main`, on 2026-09-07

`qbeta_modular_double_reciprocity.py` (scope-**(b)**, landed **2026-09-07**)
proves `log q · log q̃ = 4π²` identically in `y`. At the proton pin
`t = ln q₀ = 0.10434072`, that *forces*

    |log q̃| = 4π²/t = 378.3606        ⇒    q̃ = 4.787e-165

Reproduced here independently from the b-map alone (rel `0.0`), so it is not a
re-read of that producer's own output. The modular dual is not a bridge at a
real substrate — it is 165 decades away. **The triage did not cite this**, and
it predates the triage by five days.

### 2. But "q̃ ≈ 1e-165, therefore drop the dual half" is FALSE as a global claim

This is the part the corpus does **not** hold. `qbeta_fmap_modular_dual_missing_probe.py`
states the conclusion — *"|q̃| ≈ 0 at the substrate ⇒ dual NEGLIGIBLE ⇒ Φ_b ≈ phi_q
here"* — inferring it from the **size of `q̃` alone**. That probe evaluates no
product, writes **no witness**, and contains **no occurrence of an argument
variable at all** (`grep -c z` = 0 over its 115 lines).

The inference is not valid as stated. The k-th dual factor is

    1 + q̃^{k+1/2} · e^{2πz/b}

and the **second factor grows in `z`**, at `2π Re(1/b) = 34.4769` per unit,
because `|1/b| = 7.7600` at this substrate. Measured: at `z = 10.9743` the dual
half departs from 1 by **1.4453e+82** — the 378-nat suppression is overcome.

### 3. The window, in closed form, derived before measuring

    z*(d) = [ (4π²/ln q₀)/2 − d·ln 10 ] / ( 2π Re(1/b) )

giving `z* = 4.4186` at double precision and `2.1478` at 50 digits. It
reproduces the measured departure at `d = 16, 30, 50` to `3.1e-13` decades —
which **confirms the algebra rather than testing it**: successive `k` differ by
`exp(−4π²/t) = 10^−164.32`, so the tail was known irrelevant in advance and the
ratios are 1.0 for that reason. The check is named
`k0_inversion_reproduces_the_full_product_as_derived` so it cannot be quoted as
evidence *for* the window; the window's content is checks 4 and 5.

### 4. The pdix consequence

Inside the window, `Φ_b` and the corpus's compact half-product are the **same
function** (departure `5.19e-67` at `z = 1.0739`). So any α-derivation that
evaluates `Φ_b` at the real substrate with an O(1) argument **is using the
compact object**, and the modular double is invisible to it. **Attack B buys
nothing it did not already have there** — unless an α-route drives `|z|` past
~2–4, and no route yet does, because no route yet exists.

### What this does NOT show — read before quoting it

- **It does not weaken attack B on the root-of-unity face, where B is correctly
  aimed.** That same existing probe measures `|q̃| = 1` at `q = e^{4πi/5}`; the
  dual is genuinely order-one there, the compact form genuinely fails, and that
  is where the Q_β decay saddle sits. Nothing here touches it. Quote the finding
  narrowly: **the modular double is inert AT THE REAL SUBSTRATE for O(1)
  arguments.**
- It is a **refinement** of the existing probe, not a refutation. That probe's
  conclusion is correct in a window; it simply states no window.
- Scope (a), `b₊` branch, corpus b-map and product convention. Asserts nothing
  about α.

### Correcting my own earlier claim in this session

I said the triage *"names 3 Faddeev Lean files where there are 18"*. **Both
numbers were wrong**, and my 18 was an undercount of exactly the kind I was
flagging. Measured on this tree, `.lake` artifacts excluded — say which you
mean, they are four different populations:

| measure | count |
|---|---|
| files whose **name** carries `Faddeev`/`PhiB` | **38** |
| files that **mention** `Faddeev`/`Phi_b`/`PhiB` | **110** |
| files that **declare** such an identifier (`def`/`theorem`/`class`/…) | **37** |
| **sorry-free** among the 110 | **73** |

The triage names 3. Among the ones it omits is
`QOU/QBeta/FaddeevModularDouble.lean` — sorry-free, and *itself attack B's
structural core*.

### Recommendation — judgement, not a finding

**Re-rank A above B for the substrate face.** Attack A (Habiro / roots of unity)
is now the only one of the four whose premise survives measurement where the
anchors sit, and the triage already calls it *"the better structural fit"*,
declining it only for circularity risk. Attack B should be **re-scoped**, not
dropped: from *"the textbook bridge for this exact modulus gap"* to *"the right
tool on the root-of-unity face, where the dual is order-one"* — which is where
the decay saddle is anyway. The cost of the re-scope is a paragraph; the cost of
not making it is a formalize-first tranche against a bridge that is 165 decades
inert at the point it would be evaluated.

**Default if nothing is done:** the triage stands as written, and the next agent
reads "cheapest formalize-first step of the four" and spends a tranche on it.

### Follow-on noticed, not actioned

`qbeta_fmap_modular_dual_missing_probe.py` **writes no witness** — it is in the
`qou-4383` "producer that exits 0 and writes nothing" class (that sweep is the
current `main` HEAD). Not fixed here: it is someone else's arc, and changing it
is outside the two AGENTS.md exemptions.

---

## 2026-09-13 (later) — attack A measured; MY OWN RECOMMENDATION ABOVE IS WITHDRAWN

Earlier today, in the entry above, I recommended **re-ranking attack A above
attack B for the substrate face**, on the grounds that B's premise had been
measured false and A's had not. **That recommendation was wrong.** A's premise
had been measured too — by a prior agent, against a target that has since been
retired — and once re-aimed the negative holds. Both routes now carry measured
negatives on their principal route.

Probe: [`computations/qbeta/qbeta_delta_tr_vs_ruled_base_probe.py`](../computations/qbeta/qbeta_delta_tr_vs_ruled_base_probe.py),
4/4, witness `qbeta-delta-tr-vs-ruled-base.witness.json`, proton pin, convention D, scope (a).

### 1. The triage's stated reason for declining A is not what the corpus shows

The triage declines A for *"circularity — the Habiro-element construction is
part of what `qou-cds1` waits on"*. Measured:
`prop:habiro-precision-ladder-equivalence` — the block that would carry A's
bridge — has a **one-element `uses[]` cone**, `thm:jones-markov-trace`. It is
**not** downstream of `qou-cds1`. Attack A does not loop.

### 2. What actually blocks it, established by a prior agent, not by me

`QOU.BraidKnot.QbetaHabiroTaylorBridgeClass` equates `precisionLadderCoeff` and
`habiroTaylorCoeff`, and **both are `opaque ... := fun _ => 0`** with no
defining properties (lines 214 / 221; `habiroTaylorCoeff` has 3 occurrences,
all in that one file — no consumers). So it is a **named hole**, not a
hypothesis-carrying conditional, and its companion theorem is the §3b-cond
item-5 self-assuming projection (`:= h.ck_eq_taylor k`; the file's own
docstring says so and is scrupulous about it).

All of that was already established in
`qbeta_habiro_bridge_class_is_not_a_lean_target_probe.py`, which went further
than I did — it verified the seal does **not** leak under six tactics
(`rfl`, `unfold`, `simp`, `decide`, `norm_num`, `aesop`, all `lean`-direct) and
drew the right conclusion: *"Progress on the bridge is COMPUTATIONAL — give the
two sequences definitions — not deductive."* **I re-derived its structural half
before finding it.** Credit where due; this entry does not re-do it.

### 3. The corpus ran that computation, and it is aimed at a RETIRED cell

`qbeta-delta-tr-vs-formA.witness.json` (`computedAt` 2026-08-08, last touched
`87bf883793` on 2026-09-07) finds Habiro `Δtr_M` and Form A's net-winding slot
structurally distinct: `−5/4 ε` against `−2 ε`. The sibling probe verified that
inference is not a mere normalisation.

**But its comparison target is `Abs((q²−1)(q(q−2)−1))/(2q³(q−1))`, which is
algebraically identical to the published `|q²−2q−1|(q+1)/(2q³)` — the `z = 1`
cell.** The owner **retired that cell as the base on 2026-09-08**, one day
after that witness was last touched, ruling `ε` = the Markov trace at
`z_D = q³/(q²+1)`. So the one computational test of A's bridge was aimed at a
functional that is no longer canonical, and nothing had re-aimed it.

### 4. Re-aimed at the ruled base, the negative HOLDS — at both admissible points

| leading Taylor, `ε = q − 1` | `Δtr_M` | slot object |
|---|---|---|
| vs `tr_M` at `z_D` (**RULED**) | `−5/4 ε` | `−1 ε` |
| vs `tr_M` at `z = q` (augmentation) | `−5/4 ε` | `−2 ε` |

and the `z_D` mismatch is **structural, not a normalisation** — the
term-by-term ratio runs `5/4, −11/4, −1/16, −20/11, −589/52`: five distinct
values over five orders, **sign change at k = 2**. Same discipline the sibling
probe applied to the Form A negative, applied here for the same reason.

**Calibrated before anything new was read off the harness.** It reproduces the
recorded `−2 ε` / `−5/4 ε` exactly, and independently reproduces **all three**
recorded cells: `z = 1` at **+0.1677568 %** (recorded 0.17 %), `z = q` at
**+12.470022 %** (recorded +12.470 %), `z_D` at **−43.15717 % / 0.4447004085
MeV** (recorded −43.157 % / 0.4447004).

### 5. A trap, flagged rather than taken

`Δtr_M` **itself** lands at **−17.49592 %** — better than *both* admissible
functionals. Under §NO FITTING that is **not** a point in its favour and must
not become one: it is a third object with a better residual that is **not
admissible**, which is precisely the selection-against-the-target shape the
directive names. Recorded so the next agent meets it as a trap rather than as
a lead.

### Scope — read before quoting

Scope **(a)**, proton pin, convention D. It does **not** derive `α`; does
**not** retract the 2026-08-08 Form A negative (that inequality is exact
algebra and stands on its own terms); and does **not** exclude the Habiro ring
from an `α` closure by another route. What is closed is **this specific
identification** — `Δtr_M` as the slot object — now at both admissible
functionals rather than only at the retired one.

### Where that leaves the four routes

| route | status after today |
|---|---|
| **A** Habiro | bridge closed at both admissible functionals (this entry). Not circular; the triage's reason was wrong. Broader Habiro routes untouched. |
| **B** Faddeev / modular double | inert at the real substrate inside the derivable `z`-window (entry above). Untouched on the root-of-unity face, where it is correctly aimed. |
| **C** Stokes / resurgence | unmeasured |
| **D** two evaluation points | the trap — a fourth calibration |

**Recommendation — judgement, not a finding, and it replaces mine from this
morning.** Neither A nor B is now the obvious next spend. **C (Stokes /
resurgence) is the only one of the four with no measured negative against it**,
and it is the one whose framing dissolves rather than fights the
elliptic-at-real-`q` obstruction — `α` as a Stokes constant is complex *by
nature* and defined by continuation across the gap. AGENTS.md already lists
Stokes-constant extraction as open research, so it is in scope.

**Default if nothing is done:** the triage still reads "attack B, cheapest
formalize-first step of the four", which two measurements now contradict.

---

## 2026-09-13 (correction) — my `det_eq` "prune" is a RE-DERIVATION of THIS BEAN

Earlier today I committed
[`qbeta_eigenphase_carrier_det_forces_even_length_probe.py`](computations/qbeta/qbeta_eigenphase_carrier_det_forces_even_length_probe.py)
and framed it as a formalize-first prune on the carrier's second field:
`det ρ(w) = (−1)^len(w)`, so `det_eq` ⟺ even length.

**That is already in this bean, twice, and stated more strongly.**

- **line ~81** — *"det rho(sigma_i^{±1}) = -1, so det rho(w) = (-1)^L; det M = 1
  forces L even and lambda = ±1, leaving the trace in ±Z[q,q^-1]."*
- **line ~1409** — *"`det ρ(σ) = −1` for all four generators, so an even-length
  word has `det = +1` exactly. **The carrier's `M.det = 1` field is automatic and
  free on the braid image — it was never the obstruction.** Odd-length words have
  `det = −1` and cannot meet it at all, so the image splits cleanly by parity."*

And `qbeta_mbeta_v21_spectrum_under_d.py` independently records
`det T_pp = det T_nn = −1` ("Hecke unimodularity") and labels its
`σ₁σ₂⁻¹` det = 1 assertion **"even word length"**.

**The bean's framing is stronger than mine, in the direction that matters.** It
calls `det_eq` **free** — never the obstruction. I called it "a prune that
bites". A necessary-but-automatic condition does not bite, and describing it that
way overstates what it buys. The correction stands independently of the
arithmetic, which is fine.

**What actually survives as mine**, and it is small:

1. **`nuc11_interleaved`** — eleven letters, odd, so it cannot satisfy `det_eq`.
   The bean never names it (grep: zero hits). Force limited: branch 1 (M in the
   braid image) is independently excluded by
   `BraidImageEigenphaseAlgebraic.coeffs_zero_of_surjective_nonpos`, so the
   parity bites on a branch already closed.
2. **The Hecke-relation gate** on the seminormal matrices, which caught a
   hand-written `σ₂` that produced the nonsense determinant
   `−q²+q−3+1/q−1/q²`.

**How it happened:** corpus-grep **path 6 — "grep the beans" — was not run**
before writing that probe, on the very bean the probe is filed under. Path 6's
own rationale in AGENTS.md names this exact failure: a prior agent's conclusion
sits in the bean before it reaches any other artifact. That is now seven
corpus-grep interventions in this session, and this is the one that got through.

**Not retracted, scoped.** The probe stays — its two small contributions are
real and its docstring, witness `description`, `duplicates` and `own_contribution`
fields now say plainly what is re-derived and what is not. Contaminated sites
corrected: the probe docstring, its witness, this bean, and the PR #7340 body.

**Unaffected:** the route-5 retired-base finding in the entry above is NOT in
this bean or anywhere else (checked: `retired`/`z = 1`/`Form A`/`arccosh` all
return only my own entry). That one stands.

---

## 2026-09-13 — blast radius of the retired `z = 1` base: 42 single-base `.py` files, and one of them is the canonical ladder producer

Audit: [`qbeta_retired_z1_base_consumer_audit.py`](computations/qbeta/qbeta_retired_z1_base_consumer_audit.py)
— 3/3. **Measurement only.** It changes nothing and proposes nothing; the
2026-09-07 ask-first directive permits measuring and forbids the sweep, and this
is the blast radius that directive asks to be put in front of the owner.

**Why count.** Three consumers of the retired cell were found *by accident* in
one day, across two arcs: the 2026-08-08 `Δtr_M` vs Form-A negative (#7326),
route 5's ellipticity target `θ` (#7340), and `qbeta_alpha_required_c_vs_d_probe`.
Three by accident is a reason to count rather than keep stumbling.

| bucket (`.py`, AST on assignment RHS) | count |
|---|---|
| **SINGLE-BASE** — binds the retired cell, no `z_D` in the file | **42** |
| **COMPARISON** — binds both; deliberate, not a defect | 39 |
| **MENTION-ONLY** — signature in no assignment RHS | 46 |
| `.lean` / `.md` / `.json` — counted, **not** classified | 12 / 49 / 38 |
| `.beans` — excluded as records | 11 |

**The consequential hit: `computations/qbeta/qbeta_ck_cache.py` is SINGLE-BASE.**
That is the canonical `c_k` extraction producer — not a dated record, not a
comparison, but the producer the ladder is read from. Consistent with AGENTS.md's
own note that it **refuses to run under convention D**.

### The first number was wrong, and the calibration check is what caught it

The first run reported **29** SINGLE-BASE. Its calibration check then resolved
two of the three hand-found consumers into **MENTION-ONLY** — impossible for a
real consumer, so the classifier was wrong, not the corpus. Two missing
spellings, both algebraically identical to `q²−2q−1`:

- **absolute value pre-resolved** — `(2*q + 1 - q**2)`, legitimate because
  `q₀²−2q₀−1 = −1.988 < 0`, so the corpus drops the `abs()`
  (`qbeta_alpha_required_c_vs_d_probe.py:85`);
- **Horner form** — `q*(q - 2) - 1`
  (`qbeta_delta_tr_vs_ruled_base_probe.py:149`).

Widened (five spellings, `(q-1)**2 - 2` added pre-emptively), all three
calibrate into real buckets and the count goes **29 → 42**, a **45 %**
undercount by the naive regex. This is row-44 material for the
detector-blindness taxonomy and it was hit on first contact.

**Two process notes, both self-corrections.** Three of the audit's original
checks were `check(..., True, ...)` — self-certifying assertions of exactly the
kind this corpus bans. The calibration one now resolves buckets and **fails** if
a known consumer is missing; the two that were scope statements rather than
measurements moved into witness fields, where nothing pretends they were tested.
Had the calibration stayed hardcoded, 29 would have shipped.

### What this is NOT

**SINGLE-BASE is a candidate set, not a defect list.** A dated audit doc, a
historical record, or a probe whose subject *is* the retired form is legitimately
single-base. Separating those from genuine stale consumers is a reading task, not
a regex task, and is left to the owner. **Declared blind spots:** a cell reached
through a function call is invisible (the return-form blindness that made the
convention-C producer audit read 0 for months); a two-step build is bucketed by
its assignment only; `.lean`/`.md`/`.ts` are counted, never classified.

The witness measures the **tree**, so it goes stale on any commit touching these
files. Re-run it; do not quote it.

---

## 2026-09-13 (correction) — the route-5 gap is **139×**, not the "factor 11.2" I reported an hour ago

Two additions to
[`qbeta_route5_ellipticity_target_is_on_a_retired_base_probe.py`](computations/qbeta/qbeta_route5_ellipticity_target_is_on_a_retired_base_probe.py)
(now 8/8).

### 1. Cross-validated against `qou-99qc` — the two figure-pairs are NOT in conflict

`qou-99qc` inverts the functional for CODATA, gets `z* = 0.99850`, and reports
`z = q` at **+11.17 %** and `z_D` at **−38.64 %**. This arc records **+12.470 %**
and **−43.157 %**. A reader meeting both pairs will conclude one is stale. They
are the same shortfall in two coordinates:

| | in `z` (qou-99qc) | in `Q_β` (this arc) |
|---|---|---|
| `z = q` (augmentation) | +11.1646 % | **+12.47006 %** |
| `z_D` (ruled) | −38.6392 % | **−43.15716 %** |

Reproduced by pushing the z-distances through the exact functional
`h²/2 − z·h`; both land on this arc's figures. The non-proportionality is the
`h²/2` term. **Not a discrepancy** — recorded so neither pair gets "corrected"
into the other.

### 2. My own "factor 11.2" understated the gap by an order of magnitude

I reported the ruled base's target as *"a real-spectrum generator at `a ≈ 1.165`
against KD's `ln q₀ = 0.104` — a factor 11.2"*. The arithmetic is right
(`a_needed/a_KD = 11.1683`) and **the framing is wrong**, in the direction that
flatters the route.

`a` enters only through `cosh`, and near `a = 0`, `cosh a − 1 ≈ a²/2`. So a ratio
in `a` is roughly the **square root** of the ratio in the quantity the correction
must actually supply. Measured:

```
deviation needed   R − 1                = 75.936 %
KD supplies        cosh(ln q₀) − 1      =  0.5448 %
ratio                                    = 139.373×
```

**Quote 139×, not 11.2×.** Stating a `cosh`-mediated gap in its pre-`cosh`
coordinate is a systematic understatement, not a rounding difference — and I
made it in the same turn that corrected two other framing errors.

Contaminated sites: this bean's preceding entry, the PR #7340 body's
recommendation, and two chat reports. The probe and witness now carry the
correction in a `gap_magnitude_correction` field.


## 2026-09-13 (session gifted-feynman) — the braid-image exclusion left the CONSTANT case open; closed by QUANTIZATION

**Part 1 is a result (scope-(b), proved invariant). Part 2 is a fit and is labelled
one.** Probe: `computations/qbeta/qbeta_eigenphase_rationality_quantization_probe.py`
(14/14), witness `qbeta-eigenphase-rationality-quantization.witness.json`.

### The hole in the sibling exclusion, and it is the case a derivation would want

`qbeta_braid_image_eigenphase_exclusion_probe.py` closes branch (1) like this:
`tr ρ(w)` is a Laurent polynomial, `|2cos α| ≤ 2`, bounded on `(0,∞)` ⟹ constant,
and `α_C`/`α_D` are both non-constant ⟹ contradiction. **A CONSTANT `α` walks
straight through that**, and nothing in the ladder requires the phase to vary —
`Q_N1 = Q_A·cos(α − u/2)` is already `q`-dependent through `u`. Anyone proposing
`α = α_req`, a pure number, was excluded by nothing in the corpus.

### The closure — the same argument, carried through INTEGRALITY

  1. `det ρ(σ_i) = −1` identically ⟹ `det ρ(w) = (−1)^{e(w)}`. So **`det = 1` is
     not an assumption on `M` — it is a parity condition on the WORD.**
  2. `σ^{-1} = σ − (q − q^{-1})I` (Hecke relation) ⟹ every word matrix is over
     `ℤ[q,q^{-1}]`, so `tr ρ(w) ∈ ℤ[q,q^{-1}]`.
  3. bounded ⟹ constant ⟹ **an integer**. On the 2-dim `V_(2,1)`, `|tr| ≤ 2` then
     forces `tr ∈ {−2,−1,0,1,2}` and

         α ∈ {0, π/3, π/2, 2π/3, π}

`|α_req| = 0.05235868` is **4795 windows** from the nearest member. So branch (1)
is closed on `V_(2,1)` for **every** `α`, not only the `(z−1)h/2` family, and
**without the transcendence assertion** the corpus carries in a docstring.

General `d`: every `tr ρ(w^k)` is a constant integer ⟹ integral char poly ⟹
eigenvalues are algebraic integers with all conjugates on the unit circle ⟹
**Kronecker: roots of unity**, so `α ∈ 2πℚ` in any irrep. The five-element set is
its `d = 2` case. **The Lean twin of the Kronecker step is NOT written.**

Verified exhaustively over all **5460 words `|w| ≤ 6`** in exact `ℤ[q,q^{-1}]`
integer Laurent arithmetic (no sympy simplify, no floats); anchors at 60 dps.

### Corollary for `qou-cds1`, and it is convention-free

If `α` is a braid-image eigenphase at all, it is a **pure number with no `z` in
it**. So the C-vs-D question for the **phase** dissolves — the phase does not need
re-deriving per convention. It survives only for the **base**.

### Part 2 — 2π/120 is the unique rational in the window. THIS IS A FIT.

Given `α ∈ 2πℚ` the search space is discrete, so one can just ask which members
fit. Never run before. Answer: `2π/120 = π/60` is the **unique** primitive
rational phase with `N ≤ 1000` inside the `|c₃| ≤ 1` window — **0.109 windows**
from `α_req`, where convention C is **2.066** (i.e. C is *outside*). It implies
`|c₃| ≈ 0.1095` against C's `−2.0693`.

**🛑 Under §NO FITTING this is SELECTION AGAINST THE TARGET** — `N = 120` was
picked because it reproduces `α_req`. Not adopted, not wired, not proposed as a
value for anything. Three honesty checks, all in the probe:

  * **the cross-anchor swing discriminates nothing** — 0.049 in `c₃` for the
    candidate and 0.049 for C, because it is `α_req`'s own anchor dependence, not
    a property of either phase;
  * **a unique hit at `N ≤ 1000` is GENERIC** (E = 1.06). Only *which* denominator
    won carries information: `P(N = 120 | one hit) = 1.05e-4`. At `N ≤ 120`,
    E = 0.0152;
  * **🛑 the mechanism a reader reaches for first is REFUTED, in the same probe.**
    `|2I| = |S_5| = |Aut(Bring)| = 120` — but a *primitive* 120th root of unity
    needs an **element** of order divisible by 120, and **`S_5`'s maximal element
    order is 6** while **`2I = SL(2,5)`'s is 10** (exponent 60, not 120). A group
    of order 120 does not supply a 120th root of unity. **The candidate has no
    identified mechanism at all**, which makes it weaker than the uniqueness
    measurement alone suggests.

### Scope limit, load-bearing

The ladder inverted here sits on `Q_A = m_e|q²−2q−1|(q+1)/(2q³)` — the **`z = 1`
cell, RETIRED as the base by the 2026-09-08 ruling** (`qou-99qc`). Nothing here
moves the dashboard, whose `Q_β` row is base-only at ~4.3e+8 ppb on the ruled
`z_D` base. **A ~0.1 % phase cannot address a 43 % base gap: the D-base miss is
not a phase problem**, and this entry must not be cited as if it were.

### What would close it

Derive the **120** — exhibit a braid word and a partition whose `q`-uniform
eigenphase is `2π/120` — rather than read it off `α_req`. Given the refutation
above, that requires an element of order divisible by 120 from somewhere the
framework actually supplies, and no such source is identified here.


## 2026-09-13 (session gifted-feynman, 2) — 🛑 DERIVING α CANNOT UNBLOCK `qou-cds1`. The gap is in the BASE.

**This supersedes the dependency chain the whole S1 tranche is organised around.**
Lean twin sorry-free (`lean`-direct exit 0, axioms `[propext, Classical.choice,
Quot.sound]`): `QOU/QBeta/EigenphaseQuantization.lean`. Probe now 16/16.

The author asked whether the `2π/120` candidate was a compute problem. **It is
not — and the question was the right one.** The compute is correct; it is
computing a **retired** object. On the **live** object the entire rung is
structurally excluded, which nobody had checked.

### The exclusion, one line

`qou-iagg` ← `qou-cds1` ← `qou-pdix`. **The second link does not hold.** On the
ruled `z_D` base the ladder must supply

    Q_codata / Q_D = 0.78233341 / 0.4447004 = 1.7592370…  > 1

while its `N = 1` rung is `cos(α − u/2) ≤ 1` for **every** `α`, and its `N = 2`
rung is `(1 + c₂u²) = 0.99992745… < 1` at the committed `c₂ = −1`. The two
together are bounded by `0.99992745 < 1 < 1.7592`.

**No phase whatsoever repairs a base that is 43 % low, because a cosine cannot
exceed one.** The `c₃` that would be required instead is **1.23e6**, not `O(1)`
— which is the same fact the corpus already reports as "c₃ ≈ −974 under D",
seen from the side that shows it is not a coefficient problem.

Scope-(b), citing `Real.cos_le_one`. **This is the mirror of this bean's own
2026-08-22 (8) entry**, which excluded a `cosh` re-reading because `cosh ≥ 1`
sat on the wrong side of a required value *below* 1. Here the required value is
*above* 1 and `cos ≤ 1` is on the wrong side of it.

### What this means for the arc

  * **The `Q_β` L2 residual is a BASE problem** — not a phase problem, and not a
    ladder problem at all. Work on `α` is not on the L2 critical path.
  * `qou-cds1`'s blocker is **not** this bean. Re-deriving the `c_k` ladder on
    the `z_D` base cannot succeed in the committed multiplicative-cos form
    whatever `α` is; the form itself, or the base, has to change.
  * `qou-iagg` (the second re-score) is therefore **not** waiting on `α` either.
  * This does **not** say the ladder is wrong, or that no `Q_β` closure exists.
    It says where the gap is not.

### Lean, formalize-first (all sorry-free)

  * `cos_rung_lt_of_base_short` — the exclusion, general form
  * `cos_rung_lt_of_base_short_ladder` — the `(1 − u²)` shape the ladder uses
  * `two_cos_eq_int_cases` — Part 1: `2cos α ∈ ℤ ∩ [−2,2]` ⟹ five cosines
  * `not_isInt_of_mem_Ioo_one_two` — the exclusion mechanism
  * `not_braid_eigenphase_of_two_cos_mem_Ioo` — `2cos(α_req) = 1.99725…` is
    strictly inside `(1,2)`, hence not an integer. **This covers a CONSTANT `α`**,
    the case the boundedness-only argument leaves open.

**NOT formalised, named so it is not mistaken for done:** "a Laurent polynomial
bounded on `(0,∞)` is constant", and the general-`d` Kronecker step. Both proved
on paper and verified numerically over all 5460 words `|w| ≤ 6`; neither has a
Lean twin. **Options stay open until those land** — per the author's standing
instruction, nothing is closed on the strength of the paper argument alone.

### Status of the `2π/120` candidate after this

Weaker still, and its scope is now doubly moot: its base is retired, **and** on
the live base no `α` at all can matter. Kept recorded, not adopted, not wired.


## 2026-09-13 (session gifted-feynman, 3) — Part 3 RE-OPENS the cosh route: that exclusion was computed on the retired base

**A re-opening, not a candidate.** Nothing is proposed, nothing is wired.

Entry **2026-08-22 (8)** closed the modular/cosh horn like this: *"required N1 =
0.99839767 < 1; cosh(x) ≥ 1 for every real x; wrong side of 1 — EXCLUDED."*
That arithmetic is correct **and its `required N1` came from `Q_A`, the `z = 1`
cell retired as the base on 2026-09-08.**

Recomputed per base (assertion 17):

| base | required `N=1` factor | `cosh ≥ 1` |
|---|---|---|
| retired `z = 1` | **0.998325241673** (< 1) | wrong side — correctly excluded |
| **ruled `z_D`** | **1.7592370279** (> 1) | **right side — the exclusion is VOID** |

So the 2026-08-22 horn was closed against a base that no longer holds, and no
one re-checked it when the base was ruled. Under the ruling, the requirement
inverts: the `N = 1` factor must be **above** 1, which is exactly where `cos`
cannot go (Part 3) and where `cosh` lives.

### 🛑 And nothing clean is on offer — this is the half that must not be dropped

`arccosh(1.7592370279) = 1.16521714843`. Against the natural substrate
quantities (assertion 18):

    arccosh / ln q     = 11.16742481
    arccosh / h        =  5.573593624       (h = q - 1/q)
    arccosh / hbar_q   = 11.76016318

**None is within 1e-3 of an integer or a half-integer.** `5.5736` is 1.3 % from
`11/2`, which is not a match at this precision. So there is **no cosh closed
form here**, and hunting for a `c` that fits would be selection against the
target under §NO FITTING. The finding is that the *exclusion* fails, not that
the route succeeds.

### The other admissible cell, recorded only (assertion 19)

Of the two admissible Markov points, only the **augmentation** cell admits a
bounded multiplicative rung at all:

    CODATA / Q(z = q)  = 0.889125773136   < 1   -> a cos rung CAN reach it
    CODATA / Q(z_D)    = 1.7592370279     > 1   -> none can

(The two cells sit at the exact ratio `1/α = (q²+1)²/(q⁴+1) = 1.97861424`,
measured `1.97861437`, confirming AGENTS.md's proportionality.) **`z_D` is the
owner-ruled cell and nothing here proposes changing it** — this is recorded so
the asymmetry is visible, not as an argument.

### Consequence for `qou-cds1`

The tranche's job was "re-derive the `c_k` ladder under D". Part 3 says the
committed **form** cannot be carried over whatever `α` is; this entry says the
one alternative form the bean already considered was dismissed on the old base.
So `qou-cds1` needs a **form** decision before any coefficient work, and that
decision is the author's — it is not something to settle by which shape fits.

Probe now 19/19.


## 2026-09-14 — SYNTHESIS across two sessions: the retired-cell staleness is a CLASS, and it cuts both ways

Merged `origin/main` into `claude/gifted-feynman-fhjzwv`. Both sessions worked
this bean on 2026-09-13 in parallel; **nothing duplicated** — the two entry sets
are disjoint and this reconciles them.

### 1. Two sessions, two places, the SAME defect class — independently

The sibling entry *"attack A measured"* found that the one computational test of
A's bridge *"was aimed at a functional that is no longer canonical, and nothing
had re-aimed it"* — `qbeta-delta-tr-vs-formA.witness.json` compares against the
`z = 1` cell, retired as the base on **2026-09-08**, one day after that witness
was last touched.

This session found the same thing in two different places:

  * the **2026-08-22 (8) cosh exclusion** — its `required N1 = 0.99839767 < 1`
    is the `z = 1` cell's requirement; on the ruled base the requirement is
    `1.7592 > 1` and the exclusion is **void**;
  * the **ladder form itself** — `α_req` and its window are inverted from that
    same retired base.

**Neither session found the other's instance.** Two independent hits make this a
**class**, not two accidents: *the 2026-09-08 base ruling silently invalidated
arguments that were computed against the old cell, and the corpus was not swept
for them.* Assume more remain. The cheap test is: does the artifact's number
trace to `Q_A = m_e|q²−2q−1|(q+1)/(2q³)`? If so it is aimed at a retired cell.

### 2. 🛑 It cuts BOTH ways, and that is the part a sweep would get wrong

The sibling's instance invalidated a **positive** (a bridge test) and the
re-aimed negative *held*. This session's cosh instance invalidated a
**negative** — a route the bean had closed is now **re-opened**. A sweep that
assumes "stale ⇒ the claim was too optimistic" will re-close the cosh horn by
reflex. It must be re-aimed, not re-asserted, in each direction.

### 3. Part 3 is UPSTREAM of both attacks, and changes what they are for

Attacks A and B are both routes to **derive `α`**. Part 3 (this session,
sorry-free Lean) shows that on the ruled `z_D` base **no `α` whatsoever** moves
`Q_β`, because the `N = 1` rung is a cosine bounded by 1 while the required
factor is `1.7592 > 1`.

So the two measured negatives on A and B, and any future positive on either,
are **moot for the L2 `Q_β` gap** — they bear only on `qou-pdix`'s own stated
goal of deriving `α` as mathematics. This does not diminish them; it re-labels
what they are evidence about. **`α` is not on the L2 critical path.**

Combined state of the tranche:

| item | status |
|---|---|
| attack A (Habiro / roots of unity) | measured negative, re-aimed at the ruled base — sibling |
| attack B (Faddeev modular double) | measured negative, inert at the substrate — sibling |
| branch (1), braid image, `q`-varying `α` | closed (prior) |
| branch (1), braid image, **constant** `α` | closed this session by quantization, Lean sorry-free |
| **any `α` at all, for L2** | **excluded this session — the gap is in the BASE**, Lean sorry-free |
| the cosh / modular form | **RE-OPENED** — its exclusion was aimed at the retired cell |

### 4. What is actually left, stated without a recommendation

`qou-cds1` needs a **form** decision before any coefficient work: the committed
multiplicative-cos ladder cannot reach a base that is 43 % low, and the one
alternative form the bean considered (cosh) was dismissed on a base that no
longer holds. **No closed form is on offer for it** — `arccosh(1.7592370279) =
1.16521714843` over `ln q` / `h` / `ℏ_q` gives 11.1674, 5.5736, 11.7602, none
near an integer or half-integer. Choosing a shape because it fits would be
selection against the target; this is an author decision, not an agent one.

### 5. Scope limit on Part 3, stated explicitly

Part 3 assumes the correction multiplies the base — `Q = Q_base · cos(…) ·
Π(1 + c_k u^k)`, the committed form. **It does not exclude a non-multiplicative
correction**, and `Q_β = |ε(Δ)|·E₀` with `Δ` a *difference* of two words
(sibling retraction `a64570260f`) is a reminder that the surrounding structure
is additive one level down. If a D-frame ladder were additive, the cosine bound
would not apply. That limit belongs beside the result.


## 2026-09-14 (session gifted-feynman, 2) — 🛑 MY OWN Part 3 WAS AN INSTANCE OF THE CLASS IT DOCUMENTS

**Correcting my own figure, and the correction is the point.** Part 3 hardcoded
one base cell, `Q_D = 0.4447004` MeV (−43.157 %), giving a required ladder
factor of **1.7592**. **That cell had already moved when I wrote it.**

The scored base changed twice on 2026-09-13 — `173da443b6` made the
tower-summed `E₀` canonical, then `573b2ece24` migrated the scored element to
the γγ word `nuc11_interleaved`. The live dashboard row has read **1.668e+8 ppb,
−16.678 %** since 2026-09-12, not 4.316e+8 / −43.157 %. Verified directly
against `origin/main:computations/per-observable-100x-status.witness.json`.

**So the required factor is 1.2002, not 1.7592 — wrong by 1.47×.** My *Part 4*,
in the same probe, names exactly this failure class ("an argument aimed at a
cell that has since moved"), and Part 3 was an instance of it. The
`AGENTS.md` paragraph I read the figure from even carries the instruction that
would have caught it — *"Quote the witness, not this paragraph"* — and I quoted
the paragraph.

### What is contaminated, and what is not

  * **The conclusion is UNAFFECTED.** 1.2002 is still > 1, so a cosine rung
    still cannot reach it.
  * **The Lean is UNAFFECTED.** `cos_rung_lt_of_base_short` takes
    `Qbase * d < Qtarget` as a *hypothesis*, never a literal, so the theorem was
    already stated at the right generality. Only the probe's instantiation and
    its prose carried the stale number.
  * **Contaminated and now fixed:** the probe docstring, its Part 3 block, its
    witness, the 2026-09-13 (2) bean entry above, PR #7262's body and one PR
    comment. All quote 1.7592 / 0.4447004.

### The fix is to stop naming a cell at all

The exclusion is **base-independent**, and stating it that way makes it immune
to the element moving again — which it may, since the 2026-09-13 ruling records
that the scored element **fails** the confinement SDP and its replacement is an
open owner decision:

| cell | vs CODATA | required factor | `cos` rung reaches it? |
|---|---|---|---|
| `nuc11_interleaved`, tower `E₀` — **LIVE** | −16.678 % | **1.2002** | **no** |
| `z_D` on `Δ_S`, tower `E₀` | −42.594 % | **1.7420** | **no** |
| `z_D` on `Δ_S`, order-zero `E₀` | −43.157 % | **1.7592** | **no** |
| bar-odd survivor (parity-forced) | −54.825 % | **2.2136** | **no** |
| augmentation `z = q` — *not ruled* | +12.470 % | 0.8891 | yes |
| retired `z = 1` — *retired* | +0.17 % | 0.9983 | yes |

**Every cell the ruling admits sits below CODATA**, so each needs a factor
above 1, and the `N = 1` rung is a cosine bounded by 1 while the `N = 2` rung is
`0.99992745 < 1`. **The two cells a cosine can reach are exactly the two the
ruling does not select.** So the exclusion holds for the live element, for its
two predecessors, for the parity-forced alternative, and for whatever replaces
the element provided the replacement is below CODATA.

`c₃` required on the live cell: **324098.7**, not `O(1)`. (It was 1.23e6 on the
stale cell — same order of conclusion, different number.)

Probe re-run 19/19; Lean re-verified `exit 0`, axioms unchanged.

## 2026-09-14 (session gifted-feynman) — the SAME stale-cell defect, inside the probe that documents it

Third instance this arc, and the first one *inside* the artifact whose Part 4
is about the defect class.

**The claim.** Assertion 18's failure message in
`qbeta_eigenphase_rationality_quantization_probe.py` hardcoded
`arccosh(required)/{ln q, h, ℏ_q} = 11.1674, 5.5736, 11.7602`. Those are the
**retired-cell** ratios (`need = 1.7592`, the `z_D`-on-`Δ_S`-order-zero-`E₀`
cell). The code four lines above already computed `need_D = live_factor`, i.e.
the **live** `nuc11_interleaved` / tower-`E₀` cell, so the printed table and the
assertion message disagreed by 47 % on every figure.

**Evidence.** Live-cell ratios, computed: `ln q 5.967071281`, `h 2.97812889`,
`ℏ_q 6.283788176`, from `arccosh(1.2001632) = 0.62260851569`. The assertion's
own *predicate* (`not near_int and not near_half`) was always evaluated on the
computed ratios and is unaffected — **the test was right and its explanation
was wrong**, which is the worst shape: a reader checking the reasoning gets
retired numbers from a passing assertion.

**Implication.** The defect is a hardcoded literal in a message, so the fix is
structural rather than arithmetic: the message now interpolates `ratios`
directly and no literal remains to go stale. Same treatment applied to the
witness note. Assertion count unchanged, **19/19**.

**Recorded, not proposed.** Computing the live-cell ratios surfaces
`arccosh/ℏ_q = 6.283788176` against `2π = 6.283185307` — `6.029e-4` apart, rel
`9.6e-5`, about **55 `α_req` windows**. That is *not* a hit (the window is
`1.0919e-5`), it is not within the assertion's own `1e-3` integer tolerance
under any reading, and no mechanism is offered. It is written into the
assertion message only so a later reader who recomputes it does not read it as
a discovery. Chasing a `c` that makes it exact would be selection against the
target, per the anti-fit directive.

**What did NOT change.** Parts 1 and 3 and the Lean twin are untouched;
`EigenphaseQuantization.lean` is `lean`-direct exit 0 against the post-merge
tree (108 commits of `origin/main` merged as `0433359e6f`), and the live `Q_β`
dashboard row is still `err_ppb 1.668e+8` / `miss_factor 2.139e+7`, so Part 3's
corrected figure holds across the merge. Part 3 is base-independent regardless.

## 2026-09-14 (session gifted-feynman) — TRAP: `precision-gates.sh` in a bare container rewrites 12 audit witnesses with ITS OWN environment

**The claim.** `scripts/precision-gates.sh --changed` exits **0** on this branch
(the blocking ratchets are clean), but running it leaves **12 modified audit
witnesses** in `computations/`, and those modifications are **artifacts of the
container, not measurements of the corpus**. Restore them; do not commit them.

**Evidence.** This container has no `scipy`, no `clarabel`, and `mpmath 1.3.0`.
The committed witnesses record `scipy 1.17.1`, `clarabel 0.11.1`,
`mpmath 1.4.1`. So the re-run does not merely refresh timestamps — it
*removes* two packages from every `environment` block it touches and downgrades
a third. The counts move with it:

| witness | committed | this container |
|---|---|---|
| `witness-provenance-audit` | 105 | **91** |
| `q0-anchor-consistency-audit` | 2 | **4** |
| `witness-raw-float64-audit` `dirty_witnesses` | 981 | **978** |
| `witness-value-copy-audit` `indexed_literals` | 232482 | **232638** |

The provenance drop (105 → 91) is the one to notice: it moves in the direction
a *missing dependency* produces, not the direction a drain produces, and
committing it would read as 14 witnesses' worth of progress that nobody made.

**Implication.** This is the AGENTS.md sibling-witness hazard one level up —
the doc warns that *producers* write sibling witnesses, and the same is true of
the **gate**. The gate's job is to tell you whether *your* change is clean; its
exit code is the deliverable and the witnesses it rewrites are not. In a bare
container the rewrite is worse than noise, because an `environment` block is
exactly what a later agent consults to decide whether a re-run is comparable.

**Action taken.** `git checkout -- computations/`; tree clean; nothing from the
gate run is committed. The gate's verdict (**exit 0**) is recorded here and in
PR #7262 instead.

**Rule for the next agent.** After `precision-gates.sh`, run
`git status --porcelain computations/` and restore anything it touched unless
you deliberately intend a witness refresh AND your container's `environment`
matches the committed one. Check that with
`python3 -c "import scipy, clarabel, mpmath; print(mpmath.__version__)"` before
trusting any count the gate prints.

---

## 2026-09-14 — on the RULED base the ladder is excluded for EVERY phase, so α is not the blocker

Probe: [`qbeta_ladder_form_cannot_reach_ruled_base_probe.py`](computations/qbeta/qbeta_ladder_form_cannot_reach_ruled_base_probe.py)
— 5/5, proton pin, 50 dps. Scope **(b)** for the exclusion (proved invariant
cited); (a) for the numbers.

**`qou-cds1`'s last entry (2026-09-08) holds two halves that do not fit
together.** It adopts the ruled base and keeps the old blocker in one sentence:
*"eps := tr_M at z_D … the D-frame ladder is to be re-derived on the z_D base
(0.4447004 MeV, −43.157 %) … the blocker is still the N=1 phase (qou-pdix)."*

The ladder's correction factor is `F(α) = cos(α − u/2)·(1 − u²)·Π(1 + c_k u^k)`,
and what it must supply is `F_required = Q_codata/Q_base`:

| base | Q_base (MeV) | `F_required` | |
|---|---|---|---|
| `z = 1` (Form A) — **RETIRED** | 0.783645827375 | **0.998325241673** | < 1 |
| `z_D`, order-zero `E₀` — **RULED** | 0.444700408522 | **1.75923699418** | **> 1** |
| `z = q` (augmentation) | 0.87989056126 | **0.889125812282** | < 1 |
| dashboard scored cell — **RULED** | 0.65185631006 | **1.20016236389** | **> 1** |

**`cos ≤ 1`, so `F_N2(α) = cos(α − u/2)(1 − u²) ≤ 1 − u² = 0.99992745…` for
EVERY real α** — the supremum is attained at `α = u/2` and is still below 1.
Both ruled cells need more than 1. **No phase closes it**, derived or fitted.

**So deriving α cannot unblock this ladder on the base the bean adopted.** The
blocker line was correct for the retired cell — there `F_required = 0.9983 < 1`,
a small phase fits, and α is exactly the interesting unknown. It does not
survive the base change.

**Pushing the shortfall into the rungs instead is not a route either:** it needs
`c_2 ≈ 1.047e4` (z_D) or `2.760e3` (dashboard cell) against the structural
`c_2 = −1` — four orders, wrong sign. The `1/u² = 13784.87` magnifier is why,
which is this bean's own finding about `c_k` being the wrong coordinate.

### Calibration, run before anything was concluded

The probe first reproduces **this bean's own F-table** on the retired base —
**−0.0762164 / −35.9111 / −3.17063 %** against the recorded −0.076 / −35.9 /
−3.17 — so the machinery is the bean's, not a re-invention.

### A coordinate trap this exposes

That table reports relative deviation of **`1 − F`**, not of `F`. On the retired
base both are small and positive and the ratio is informative. On a ruled base
`1 − F_required = −0.7592` is **negative** while the model's `1 − F_N2 = +0.0016`
stays positive, so the same ratio returns −100.21 % — opposite-signed
quantities, meaningless rather than merely large. **Report `F` directly on a
ruled base;** the reldev table is retired-base-only.

### What this does NOT say

It does **not** retire α: `qou-pdix` stays open on its own terms, α is still the
N=1 phase, and this says only that α is not what stands between the ladder and
the ruled base. It does **not** refute the ladder or the forced bar-odd
projection `a_odd = a − h²/4` — both C-frame, sorry-free, untouched. And it does
**not** choose a base: `F_required < 1` on the retired cell is **not** a reason
to prefer it (§NO FITTING — a base is never chosen by which obstruction it
removes).

### What it changes about the next step

The open question is no longer "what is α" but **what object supplies a factor
above 1 at all** — the ladder's multiplicative form cannot, whatever its phase.
That is a question about the *base or the assembly*, not about the phase.

---

## 2026-09-14 — the question above has an answer already in the corpus, and it reverses route 5

The entry above closes asking *"what object supplies a factor above 1 at all"*.
Route 5's own machinery does — and it is the branch route 5 currently treats as
excluded.

**The step-18 obstruction is conditional, and its hypothesis is false on the
ruled base.** `qbeta_holonomy_spectrum_sign_obstruction_probe` argues a
real-spectrum holonomy has character `cosh(a) ≥ 1` and so cannot supply a
correction **below 1** — *"1.005448 against a required 0.998399: wrong SIDE of
1."* That `0.998399` is the requirement on the **retired** `z = 1` cell.
Measured (`qbeta_ruled_base_inverts_the_route5_obstruction_probe`, 6/6, proton
pin, 50 dps), with `κ = F_required/(1 − u²)`:

| base | `κ` | hypothesis `κ < 1` |
|---|---|---|
| `z = 1` (Form A) — RETIRED | 0.998397668719 | TRUE → **fires** |
| `z_D`, order-zero `E₀` — RULED | 1.7593646242717 | FALSE → **does not fire** |
| `z = q` (augmentation) | 0.889190317068 | TRUE → fires |
| dashboard scored cell — RULED | 1.20024943392874 | FALSE → **does not fire** |

Calibrated first against step 18's own two quoted figures (required and KD
character), to 1.3e-6 and 4.3e-7 — same object, not a near-relative.

**The Lean is untouched and correct.** `correction_below_one_excludes_real_spectrum`
carries the hypothesis `(hκ : κ < 1)` explicitly and was always a conditional.
What the base change falsified is its **premise** — AGENTS.md's
*conditional-proved ≠ premise-established*, here in the direction where the
corpus stated the conditional properly and the prose around it then treated the
hypothesis as settled.

**On a ruled base the two proved inequalities point the other way.** `cosh ≥ 1`
(`real_spectrum_character_ge_one`, sorry-free) and `|cos| ≤ 1`
(`Real.cos_le_one`, via `ladderN2_lt_of_one_le`, sorry-free) together exclude the
**elliptic** generator and leave the **hyperbolic** one — which is what the
substrate's Kohno–Drinfeld generator already is at real `q₀` (`ħ = 2 ln q`,
`det A = −(ln q)² = −0.01088698592 < 0`). Step 18 recorded that as the defect; it
is no longer a defect.

**So the narrowing to `det A > 0` / `|q| = 1` / the Kashaev locus / the `N = 111`
question rests on a retired premise.** `qbeta_fibre_unit_circle_opens_route5_probe`
is not wrong — its `det A > 0 ⟺ |q| = 1` identity is exact — but the *requirement*
that sent route 5 to the fibre no longer holds on the ruled base.

**This does not derive anything.** The KD character `1.00544843335` is on the
right side of 1 and the wrong size against `1.75936462427` required. Route 5 goes
from a **structural** obstruction back to a **quantitative** gap, which stays
open. Non-exclusion is not a derivation, and per NO FITTING the fact that the
ruled base makes this exclusion lapse is not a reason to prefer it. The required
character and generator eigenvalue are recorded to check **against**; no search
was run for a construction producing them.

### The coordinate, again — and it resolves a live disagreement

The residual gap at the `z_D` order-zero base, in three spellings:

    generator eigenvalue    a_req / a_KD       =  11.16826965
    character excess        (κ − 1)/(KD − 1)   = 139.3730225
    character ratio         κ / KD             =   1.7498308

A sibling branch (`claude/cds1-pdix-attack-c-stokes-2026-09-13`) recorded *"the
route-5 gap is 139x, not the 'factor 11.2' I reported an hour ago"*. **Both are
right and they are the same gap** — the second is a change of coordinate, not a
correction, and neither figure should be retracted.

With `c_k` (magnifier `1/u² = 13784.8735`) and `1 − F`, this arc now has **five**
coordinates for one deviation. Every confusion in it so far — the `−100.21 %`
above, the 11.2/139 pair here — has been about which one is in use. **Say the
coordinate before quoting a factor.**

**Status: still open.** α is underived; the gap is quantitative. Rule 13a.

### 🛑 Two corrections to the entry immediately above, same day

**1. The `cos ≤ 1` exclusion in the 2026-09-14 entry *before* this one is not
original — PR #7262 Part 3 has it**, reached independently and done better:
sorry-free Lean strictly covering mine (`cos_rung_lt_of_base_short`,
`cos_rung_lt_of_base_short_ladder`), a fuller base table including the bar-odd
survivor at **2.2136**, and a self-correction mine lacked. Per §"Measured
research-overlap … converge on landing", **#7262 lands the exclusion** and #7355
re-scopes to the route-5 reversal above, citing Part 3 rather than restating it.
Two independent derivations strengthen it; two claims of priority do not.

#7262 also already names the mirror — *"this bean's own 2026-08-22 entry
excluded a `cosh` re-reading because `cosh ≥ 1` sat on the wrong side of a
required value below 1"*. The reversal above is that mirror's **consequence**,
traced into the step-18 → step-19 → fibre-unit-circle chain that still assumes
the `cosh` branch is shut.

**2. I led with a superseded cell.** The tables above put `z_D` order-zero /
`κ = 1.7594` first. The **live scored row** has been `nuc11_interleaved` /
**`κ = 1.20024943`** since 2026-09-12 (`173da443b6` tower-summed `E₀`,
`573b2ece24` the γγ element). Both appear in my probe — the "dashboard scored
cell" row *is* the live one, matching #7262's 1.2002 to six digits — but the
framing was wrong. **Quote 1.2002.** Every conclusion is unaffected: 1.2002 is
still above 1, so the hypothesis still fails and the reversal still holds.

Worth noting *which* error this was: quoting a figure that had already moved, from
a bean entry, while writing a bean entry about quoting figures in the wrong
coordinate. #7262's Part 4 names this exact failure class and its own Part 3 was
an instance; so was this.

---

## 2026-09-14 (3) — the branch the reversal re-opens is closed too, and route 5 now has ONE live branch on either reading

The entry above re-opened the hyperbolic branch. Re-opening a branch is not a
result, so it has been worked. Two of its three cases are now closed.

**Case 1 — constant residue: EXCLUDED as a function.** Kohno–Drinfeld fixes
`ħ = 2 ln q`, so a constant-residue generator eigenvalue is `c·ln q` and its
character is `cosh(c ln q)`. `PhaseFailsLogFunctionalEquation` excludes exactly
this holonomy on the **elliptic** reading via `ln(q²) = 2 ln q`. The hyperbolic
reading observes the **character** rather than the angle, so the analogue is the
cosh double-angle law — `χ(q²) = 2χ(q)² − 1`, holding for **every `c` at once**.
Measured, `κ(q)` on the `z_D` base misses it by **62.30 / 70.47 / 68.79 /
59.30 %** at `q ∈ {q₀, 1.5, 2, 3}`, against **1.9e-60** for a genuine character.

*The check the argument needed:* the identity is **not** scale-invariant and `κ`
carries the experimental `Q_cod` as an overall scale. Solving
`2λ²κ(q)² − λκ(q²) − 1 = 0` gives `λ(q)` spreading **28.86 %** over five points
against `|λ − 1| ≤ 1.6e-61` for a genuine character — so it is not a
normalisation artifact.

**Case 2 — arbitrary `q`-dependent residue: VACUOUS.** `cosh` is onto
`[1, ∞)`, so wherever `1 ≤ κ` a residue reproducing it exists by construction:
`a(q) := arcosh(κ(q))`, read off the answer. Measured, `κ` stays `≥ 1`
throughout `q ∈ (1, 10]` — **1.5333** at `q → 1⁺` rising monotonically to
**8.0243** at `q = 10`, no crossing — so the vacuity is not conditional in the
physical domain. Had `κ` dipped below 1 anywhere that region would have been a
genuine constraint (`cosh ≥ 1` always); it does not.

**Case 3 — derived `q`-dependence: OPEN.** The only contentful branch.

### The trichotomy now mirrors the elliptic one exactly

| | elliptic | hyperbolic |
|---|---|---|
| constant | `ln(q²) = 2 ln q` → **excluded** | Chebyshev doubling → **excluded** |
| arbitrary | `EigenphaseCarrierVacuity`: *"M arbitrary — CIRCULAR"* | `arcosh(κ)` → **vacuous** |
| derived | **open** | **open** |

Reached independently on the two sides. **So route 5 has one live branch on
either reading, and it is the same branch.** Step 18 claimed to close all three
at once *"by a sign argument that never reads the residues"* — that argument is
the one the ruled base voids, and what replaces it closes two of three.

### Scope, load-bearing

Case 1 is scope-**(b)** for *"as a function of `q`"* **only**. At `q₀` alone the
free `c` reaches the requirement **exactly** (`c = 5.96831620`, defect `0.0`), so
a pointwise match is always available and carries no information.

### A prune that FAILED, recorded as a failure

Cross-anchor rigidity — the obvious test — has **no power** here. With the pins
11.6141 ppb apart, `c` is amplified **9.58×** and `c_3` **2.05889e+6×** (through
its `1/u³` extraction): ratio **2.15e5**. The pins' agreement on `c` to ~1e-7 is
evidence about the *test*, not about `c`. An agent reading only the agreement
would conclude `c` is anchor-independent, which this does **not** show. The `c_3`
swing reproduces AGENTS.md's recorded 2.3912 %, which is the calibration.

*(My first re-derivation of `c_3` gave −2710 — I divided by the bare base where
the corpus divides by the N=2 ladder value. The recorded pair is used instead.)*

### Not pursued

`c = 5.96832` at the live cell is **0.5281 %** from 6. Check-**against** only: a
near-integer found by solving against the target is selection against the target,
and the cell is provisional anyway — the 2026-09-13 ruling records that its
element `nuc11_interleaved` **fails** the confinement SDP on `(2,1)` and
`(1,1,1)`, so `c` moves when the element is replaced. No search was run for a
reason `c` should be 6, and none should be until something independent selects
one.

**Status: still open.** Branch 3 is a live open problem on both readings.
Rule 13a.

---

## 2026-09-14 (4) — swept properly, and a tooling trap found by doing so

**The Lean was verified with bare `lean`-direct only.** AGENTS.md is explicit
that on a branch touching `.lean` this is a claim about the **olean snapshot**,
not about the library source — a file calling a moved signature compiles clean
*and* is red against the source it names, both at once, with no signal. The
sweep is the gate. Run:

| module | result |
|---|---|
| `QOU.QBeta.CharacterDoubling` | **1 ok, 0 RED** (126 s, shadow built) |
| `QOU.QBeta.LadderFactorBound` | **1 ok, 0 RED** (3 s, shadow reused) |

Dirty closure 1 in each case; 2877 library modules, 2876 snapshot-current.

### 🛑 `--only-exact` is NOT repeatable, and it fails silently

Passing it twice —

    scripts/lean-library-sweep.py --only-exact A --only-exact B

— sweeps **B only**. The flag is `store`, not `append`, so the first value is
dropped without a word; the run's own selection line reads `selection
QOU.QBeta.CharacterDoubling` and the summary reads `1 ok`. **An agent reading
"1 ok, 0 RED" after asking for two modules would report both verified having
verified one.** Caught here only because the module count in the summary did
not match the number of modules asked for.

That is the taxonomy's own class — a verification tool silently covering less
than it was asked to, and reporting success — applied to the sweep rather than
to a detector. **Sweep one module per invocation**, or check that the reported
count matches what you asked for.

**Not fixed here.** Making the flag repeatable is a change to shared tooling and
falls outside both exemptions of the 2026-09-07 ask-first directive — it is
neither a precision fix nor corpus-derived. Raised rather than enacted.

**No taxonomy row added either**, for the same reason plus a practical one: a
sibling and I collided on that document's row numbering once already today
(row 44 → 45), and it is not my document to grow unasked.
## 2026-09-14 — still open, and explicitly NOT retired; only its priority changes

**Status stays `in-progress`. Nothing here closes this bean** (§13a — α is still
the ladder's N=1 phase and is still underived).

What changed is that α is **off the `Q_β` L2 critical path**, not that it is
answered. `qou-cds1` is not blocked on this bean on the ruled base: `cos ≤ 1`
caps the N=2 factor `F_N2(α) = cos(α − u/2)·(1 − u²)` at `1 − u² = 0.99992745`
for **every real α**, while `F_required = Q_codata / Q_base` is **above 1** on
both bases the 2026-09-08 ruling selects — `1.75923699418` at `z_D` with
order-zero `E₀`, `1.20016236389` at the dashboard scored cell. The two cells a
cosine can reach (`z = 1`, retired; `z = q`, the augmentation) are exactly the
two the ruling does not select. So no value of α unblocks `qou-cds1`.

**The reusable half:** this bean was described in AGENTS.md as *the* S1 blocker,
and that framing was correct only for the retired `z = 1` cell. Deriving α
remains worth doing on its own terms; it is not the thing standing between the
corpus and a `Q_β` ladder on an admissible base.

**Provenance.** PR #7355 (`LadderFactorBound.lean`, 4 lemmas, 7/7 probe) and PR
#7262 (`EigenphaseQuantization.lean`, 19/19) — both sorry-free, both still open.
Verified and **merged** in
`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` §5.1/§5.1a
(PR #7276, `f3cb908ee7`). Cite the merged audit, not the two PRs.

Previous entry here was 2026-09-12 and predates this. AGENTS.md's two
"blocked on the phase `qou-pdix`" sites are scoped in the same PR as this
append.


## 2026-09-14 (session gifted-feynman, 3) — a stale figure in this arc's own probe, and the sign-free bound

**Stale figure, fixed at the producer.**
`qbeta_eigenphase_rationality_quantization_probe.py:117` read *"the `c₃` that
would be required instead is `1.23e6`"* while **its own witness** carries
`c3_required_on_live_cell = 324098.735988813964`. Both are right for their own
cell — `(F−1)/u³` is 1.23e6 on the **superseded** `z_D` order-zero cell
(`F = 1.7592`) and 324098.7 on the **LIVE SCORED** one (`nuc11_interleaved`,
tower `E₀`, `F = 1.20016`) — so it is a cell-attribution error, not arithmetic.

What makes it worth recording: that same file carries a
`stale_figure_corrected` witness field **one screen below the bad line**,
documenting this exact failure class for this exact quantity. The code was
corrected and the prose was not moved with it. Fixed to name the cell beside
the number and to point readers at the witness field rather than the docstring.
Found by the corpus-grep checklist, not by me.

**The phase stays open and its priority is unchanged** — α is still the
ladder's N=1 phase and still underived. What is new is that the *reason* it is
off the L2 critical path no longer leans on the signs of the `c_k`:
`QOU.QBeta.LadderUniformBound` (sorry-free, 7 declarations) proves the
exclusion from **uniform boundedness** instead, so it survives the `qou-cds1`
re-derivation that would void `LadderFactorBound.ladder_lt_of_rungs` with a
single positive rung. `C_min = 2279.46` against a corpus whose largest live
`|c_k|` is 2.0693 — a factor of 1101.5, and still 177.1 against the largest
coefficient the corpus has ever held. Full record on `qou-cds1`.


## 2026-09-14 (session gifted-feynman, 4) — the near-2π landing is PRICED, and it is cheap

The session's own assertion 13 recorded that `arccosh(F_required)/ℏ_q` lands
`9.6e-5` from `2π` and refused to treat it as a candidate. The refusal was
right; it was **unpriced**, and `9.6e-5` reads impressive to a cold reader.
Assertion 15 prices it. Three measurements, all saying not much:

**(a) Cell-dependence.** `arccosh(F)/ℏ_q` over the four cells that need a
factor at all:

| cell | `arccosh(F)/ℏ_q` |
|---|---|
| `nuc11_interleaved`, tower `E₀` (LIVE SCORED) | **6.283788176** |
| `z_D` on `Δ_S`, tower `E₀` | 11.63893426 |
| `z_D` on `Δ_S`, order-zero `E₀` | 11.7601251 |
| bar-odd survivor (parity-forced) | 14.45612053 |

A **130.05 %** spread. All four share the same `q₀`, so the ratio varies
exactly as `arccosh(F)` does — the `2π` attaches to **one value of `F`** and to
no structure.

**(b) Look-elsewhere.** **1** independent hit over **171** (divisor, target)
trials at `1e-4` relative, against **0.0342** expected — about **1 in 50**, not
1 in 10000. The single-trial `9.6e-5` overstates it by ~50×. The grid is fixed
in the source before any result is inspected, and it **collapses algebraically
identical hits**: `x/(2ℏ_q) ≈ π` and `x/ℏ_q ≈ 2π` are the same statement, and a
naive grid carrying both reports two hits where there is one. Mine did, until
it was keyed on `x/(d·t)` rather than on `(d, t)`.

**(c) Decisive, and not a statistics argument.** `F = Q_codata/Q_base` is a
ratio to an **experimental** value, so any identity pinning `arccosh(F)/ℏ_q` is
a constraint on the **measured** `Q_β`, not a prediction, unless the base
derives it independently. And per the 2026-09-13 ruling the scored element is
**rejected** by the confinement-SDP selection rule, so `F_live` moves when the
element is replaced. A coincidence attached to a number under revision is worth
nothing.

**Scope-(a), stated in the assertion itself:** this does **not** exclude a cosh
structure — Part 4's re-opening of that route stands untouched. It prices
**this** near-coincidence and finds it cheap, so a later agent does not spend a
session on it. Assertion 13 now points here.


## 2026-09-14 (session gifted-feynman, 5) — the Laurent-boundedness lemma is FORMALISED; the Kronecker step still is not

Assertion 5 of the eigenphase probe — *"no word is bounded-but-not-constant"* —
was a **paper step asserted numerically** over the sampled words, and it is the
hinge of PART 1: the sibling exclusion probe closes the braid-image branch only
against a **q-varying** ansatz, so a constant `α` walks straight through it.

**`QOU.QBeta.LaurentBoundedness`** — 5 declarations, sorry-free, `lean`-direct
exit 0 with `-DautoImplicit=false -s 65536`, `#print axioms` on all 5 =
`[propext, Classical.choice, Quot.sound]`.

**The argument is one asymptotic lemma applied twice, not two.** The `q → ∞`
end is `degree_le_of_bounded_div_pow`, off Mathlib's
`abs_div_tendsto_atTop_of_degree_gt`. The `q → 0⁺` end needs **no** second
asymptotic argument, because

    P(x) / x^m  =  (reflect m P)(1/x)        for x ≠ 0, given deg P ≤ m

(`laurent_reflect`, from `Polynomial.eval₂_reflect_mul_pow` through
`RingHom.id`) — the Laurent polynomial **is** an honest polynomial read at
`1/x`, with no division on the right. `q ↦ 1/q` is a bijection of `(0,∞)`, so
boundedness transports and the same lemma finishes it.
`laurent_const_of_bounded` **names** the constant (`P.coeff m`) rather than
asserting existence.

**🛑 Scope — three things this does NOT do, all of them recorded in the file's
own docstring so they cannot be misread later:**

1. **The Kronecker step is still not formalised.** Assertion 8 read *"the Lean
   twin of this step is NOT written"*; it now reads that the chain's **first
   input** is written and that the step from bounded-hence-integer to
   root-of-unity is not. Do **not** read the new file as closing assertion 8.
2. **This is not L2 progress.** Part 3 already established the phase is off the
   L2 critical path — the `Q_β` residual is a base/assembly problem. This
   closes a named gap in an argument whose conclusion does not move L2, and
   reporting it as L2 progress would be wrong.
3. **No integrality claim.** Bounded ⟹ constant is here; constant ⟹ integer
   runs through `σ⁻¹ = σ − (q − q⁻¹)I` and is a separate argument about the
   Hecke presentation.

**Container note, worth more than the lemma to the next agent.**
`Mathlib.Analysis.Polynomial.Basic` and
`Mathlib.Analysis.Asymptotics.SpecificAsymptotics` are **not** in the restored
`lake-cache/qou-v4-24-0`; `scripts/lean-build-mathlib-gap-cone.py
Mathlib.Analysis.Polynomial.Basic` builds both in **~5 s**. They land in the
**paper** mathlib tree, which `scripts/lean-direct-env.sh` puts *after* the root
tree — prepend it to `LEAN_PATH` or the import still will not resolve. Two
failures this session were that path ordering, not the proof. A third was
`Mathlib.Analysis.SpecialFunctions.Polynomials`, which **no longer exists** in
this Mathlib: the gap-cone builder reports it as one missing module and then
fails in 0 s because the *source* is absent. A 0-second failure from that script
means a renamed module, not a build error.


## 2026-09-14 (session gifted-feynman, 7) — 🛑 CORRECTION: my own `LEAN_PATH` advice was wrong, and it would have RED-ed a file

The entry above told the next agent to build the missing Mathlib modules into
the default (**paper**) tree and **prepend** it to `LEAN_PATH`. **Retracted.**
It makes `LaurentBoundedness` compile and it **breaks `QOU/MobiusEnergy.lean`**,
which needs `Mathlib.GroupTheory.SpecificGroups.Dihedral` — present in the
**root** tree and absent from the paper one.

**The two trees are missing DIFFERENT modules, so neither ordering verifies the
whole set.** Measured on all five Lean files of this branch, both ways:

| `LEAN_PATH` | result |
|---|---|
| paper tree **prepended** (my old advice) | `MobiusEnergy` **RED** — no `Dihedral` |
| paper tree **appended** | `LaurentBoundedness` **RED** — no `Analysis.Polynomial.Basic` |
| **stock `lean-direct-env.sh`, after the fix below** | **all five exit 0** |

**Path ordering is not the fix; completing the root tree is:**

    scripts/lean-build-mathlib-gap-cone.py Mathlib.Analysis.Polynomial.Basic \
      --dest "$(git rev-parse --show-toplevel)/.lake/packages/mathlib/.lake/build/lib/lean"

~7 s, and afterwards the **stock** env needs no override at all. The file's own
docstring now carries the corrected recipe and the retraction.

**Why this is worth its own entry rather than a silent edit.** The wrong advice
was *load-bearing and plausible* — it was derived from a real failure, it fixed
the file I was looking at, and I verified that file and no other. Verifying the
one file the advice was written for is exactly what hides this class. The
20-commit merge is what surfaced it, because the check-in re-verified **all
five** rather than the one I had changed.

**Also checked this pass, and it is a real check rather than an assumption:**
`main` landed a **sharpened** `scripts/lean-self-assuming-audit.py` (the
conjunctive `⟨X.a, X.b, X.c⟩` blind spot, taxonomy row 46, +7 hits). Run against
this branch: **none of the five files is flagged.**


## 2026-09-14 (session gifted-feynman, 8) — the Kronecker gap is NOT LOAD-BEARING, and the d=2 chain is now complete in Lean

Assertion 8 carried *"the Lean twin of this step is NOT written"* for the
general-`d` Kronecker step. I went to close it and found the more useful thing:
**it does not need closing.**

**Why.** `V_(2,1)` is **2-dimensional**, so the conclusion this probe actually
draws — *"a q-uniform braid-image eigenphase on `V_(2,1)` lies in
`{0, π/3, π/2, 2π/3, π}`"* — is the **`d = 2`** case. At `d = 2` the argument
is elementary: an integer trace with `|tr| ≤ 2` has five values, full stop. No
Kronecker anywhere in it. The general-`d` step therefore **generalises a
conclusion already had**, and nothing downstream consumes the generalisation.
Leaving it open costs nothing — a different situation from a gap that blocks,
and the assertion's wording did not distinguish the two.

**The `d = 2` chain is now complete in Lean, sorry-free end to end:**

| step | carrier |
|---|---|
| bounded ⟹ constant | `LaurentBoundedness.laurent_const_of_bounded` (this session) |
| constant integer character ⟹ cos α ∈ 5 values | `EigenphaseQuantization.two_cos_eq_int_cases` (existing) |
| **⟹ α ∈ {0, π/3, π/2, 2π/3, π}** | `EigenphaseQuantization.phase_quantized` **(new)** |
| the whole thing | `EigenphaseQuantization.braid_eigenphase_quantized` **(new)** |

`#print axioms` on both new theorems: `[propext, Classical.choice, Quot.sound]`.

**The `phase_quantized` step was a real gap, not bookkeeping.**
`two_cos_eq_int_cases` quantises the **cosine**; the corpus's sentence is about
the **phase**. Those are different statements and the bridge was prose
arithmetic. `Real.injOn_cos` is what makes it an equality rather than a
containment.

**The cost of closing the general-`d` step, measured rather than guessed:**
**Mathlib has no Kronecker theorem.** `Mathlib/` contains only
`kroneckerTMul*` — the matrix *product*, unrelated. So it is a from-scratch
formalisation: bounded roots ⟹ bounded elementary symmetric functions ⟹
finitely many monic integer polynomials of that degree and height ⟹ pigeonhole
on powers ⟹ finite order. Days, not hours, for a generalisation nothing
consumes. **Recommendation (my judgement, not a finding): leave it open and
say why, which assertion 8 now does.**


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Open on its own terms, but it is not the S1 blocker. On the ruled base no α makes the ladder reach CODATA. Its "S1 blocker" title and the ckwt/v6wz/iagg chains that cite it should be rescoped. No activity since 2026-09-14, so todo rather than in-progress.

Evidence: α is still underived; all four named attacks are closed or withdrawn (bean, 2026-09-14). It is off the Q_β critical path because of `EigenphaseQuantization.cos_rung_lt_of_base_short_ladder` and `LadderFactorBound`/`LadderUniformBound` (verified merged audit `docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` §5.1). `EigenphaseCarrierVacuity.lean`: the carrier is vacuous. Last activity 2026-09-14.

Status: `in-progress` → `in-progress` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.


## 2026-10-10 — a witness this bean cites is red (cross-cluster check, verification sweep of `qou-avtq`)

`qbeta_habiro_wenzl_tower_zeta_n.py` is listed as an "asset on main" for route A, but its witness (`qbeta-habiro-wenzl-tower-zeta-n.witness.json`, 2026-06-02, no q0Anchor) fails `level_4_tower_holds_at_M_11` (0 vs 1) and predates the C→D move. Do not cite it as a working asset.

See also `qou-cds1`'s 2026-10-10 entries: on the ruled base no phase α unblocks the ladder, so this bean is not on the critical path for `qou-cds1` (cluster 3 found the chain `iagg ← cds1 ← pdix` broken). This bean stays open on its own terms.

## 2026-10-10 — follow-up review (re-check of the `qou-avtq` sweep flags)

The Habiro–Wenzl tower probe cannot run on main: it looks for the helium witnesses under `qbeta/`, but they live in `computations/` (`:144-161`). With the paths fixed in a scratch copy it reports **"FALSIFIED at levels [2, 4]"**. The level-2 baseline the route builds on now fails too (|S_7(ζ_8)| = 69650); the 06-02 witness had it passing, but its inputs were regenerated on 09-06/09-07.

Suggested: strike it from the assets list (`:1706`) and drop "S1 blocker" from the title; fix the helium path (code, needs owner OK). Whether route A stays viable is the owner's call. α itself stays open.

Checked read-only against qou `main` at `aa914b606a`, mpmath 1.3.0. Full write-up: `qou-review/avtq-reopened-beans-2026-10-10.md` (project files). Status unchanged.

<!-- ported 2026-11-15 from PR #7441 (branch predates the beans/defs and folio/ moves) -->

### 2026-09-19 — owner picked option 2: #7252 CLOSED, the locus Lean salvaged to #7441

Owner's disposition on the supersession audit above. Executed:

  * **#7252 CLOSED** as superseded, with a comment stating exactly what was
    superseded and why, and pointing at the successor. Branch retained per the
    never-delete-branches rule. Unsubscribed.
  * **#7441 OPENED** — `QOU/QBeta/ModularDoubleLocusSeparation.lean` alone, six
    sorry-free theorems, branched from current `origin/main` `665c91e403a` and
    **re-verified there** rather than carried over: `lean`-direct exit 0
    (`-DautoImplicit=false -s 65536`, PAPER olean tree, 3564 mathlib oleans),
    0 warnings, 0 sorry, all six `#print axioms` →
    `[propext, Classical.choice, Quot.sound]`. Subscribed.

**Three defects fixed in the salvage, not merely carried:**

  1. **Prior art now CITED.** `qbeta_modular_double_reciprocity.py` (scope-(b),
     2026-09-07) is named as the sharper result *at the substrate pin*
     (`log q · log q̃ = 4π²` ⇒ `q̃ ≈ 4.8e-165`), with this file positioned as
     the *pin-independent* complement. #7252 cited only the weaker `FaddeevPhi`
     docstring and missed the producer entirely.
  2. **Convention stated, and shown not to matter.** Canonical is
     `q = exp(2πib²)`; the file's display uses `q = exp(iπb²)`. Every theorem is
     independent of the choice — the loci are cut out by `b²` alone and the
     principal branch `Re b² = 0` lies in both admissible sets. The docstring
     says so, and says why it is worth saying: the same slip made the numerical
     claim wrong by a factor 4.
  3. **No probe shipped.** Both salvage candidates measured against `α_req`,
     which is inverted from the retired `z = 1` base. Left behind explicitly
     rather than silently.

**NOT salvaged, and named so nobody re-lands them as they stand:**
`qbeta_pdix_step2_holonomy_slope_probe.py`, `qbeta_pdix_target_in_kz_level_probe.py`.
Both need **re-aiming, not re-asserting** — and per the 2026-09-14 synthesis the
class cuts both ways, so a stale *negative* in them could be re-opening a route
rather than closing one.

This bean stays **OPEN** (rule 13a — the conjecture is unclosed) and at **lower
priority** than #7252 claimed: α is off the L2 critical path.


## 2026-11-20T14:39:28Z W13 — owner asked "if derived+proved, update compute; if not, work on it"

Mirror projection alpha_D - h^2/4: algebra proved (LadderPhaseMirrorCovariance.lean, phaseTwiceD_sub_hsq_bar_odd, sorry-free). Open premise: that the ladder phase must be bar-odd (docstring analogy to writhe only); u is not bar-even so the projection is incomplete (qou-cds1 ~:258). Not wired by default; owner asked it to be worked on.
