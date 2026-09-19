---
# qou-pdix
title: 'GAP: derive the Q_beta ladder eigenphase alpha (S1 blocker) — carrier is vacuous, exact-bridge route refuted'
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T15:35:20Z
updated_at: 2026-09-19T05:50:18Z
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
[`QOU/QBeta/EigenphaseCarrierClassicalLimit.lean`](../content/quantum-observable-universe/lean/QOU/QBeta/EigenphaseCarrierClassicalLimit.lean)
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
[`QOU/QBeta/MonodromyTraceInvariance.lean`](../content/quantum-observable-universe/lean/QOU/QBeta/MonodromyTraceInvariance.lean)
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


## 2026-09-12 — attack B (the Faddeev MODULAR DOUBLE): pruned twice over. Route 5 SPLITS.

Owner asked for attack B. Result: **two independent negatives, and route 5 now
has internal structure** — its candidate list splits into a modular-double family
(pruned here) and the holonomy family (branch 3, untouched). qou-pdix STAYS OPEN.

PR #7252. Probe 13/13:
`computations/qbeta/qbeta_pdix_modular_double_locus_probe.py`
Lean sorry-free: `QOU/QBeta/ModularDoubleLocusSeparation.lean`

### B1. Inversion-as-a-bridge — EXCLUDED, scope-(b), proved invariant

Attack B's mechanism was that `Phi_b`'s duality `b -> 1/b` (with `q = exp(i pi b^2)`,
`q~ = exp(i pi / b^2)`) carries the fibre-level `|q| = 1` elliptic regime, where an
eigenphase is natural, over to the real `q > 1` substrate where the ladder is
evaluated. The two regimes are cut out by

    fibre / elliptic  |q| = 1          <->  b^2 REAL       (arg b = 0)
    substrate         q real positive  <->  b^2 IMAGINARY  (arg b = pi/4)

and `z -> 1/z` fixes BOTH the real axis and the imaginary axis setwise. Each locus
maps into itself; neither is reachable from the other. On the substrate branch
inversion's only motion is to flip `sign(Im b^2)`, sending the PhiBProd-supported
`Im b^2 > 0` branch to its own reflection.

Six sorry-free theorems (lean-direct exit 0, `-DautoImplicit=false -s 65536`,
PAPER olean tree, 0 warnings, axioms `[propext, Classical.choice, Quot.sound]`):
`fibre_inv_mem`, `substrate_inv_mem`, `substrate_inv_im_neg`,
`loci_inter_eq_zero` (the loci meet only at `b^2 = 0`, which `FaddeevPhi.hb`'s
`0 < Re b` excludes — no shared point to pass through), `modular_cannot_bridge`,
`modular_cannot_bridge'`.

**THIS SEPARATION IS ALREADY IN THE CORPUS — I did not discover it, I walked into
it.** `FaddeevPhi`'s own class docstring draws exactly this line and records that
only one side is discharged: *"on the `Im b^2 > 0` substrate branch this is
discharged by the modular-double product — see QOU.MathlibExt.PhiBProd; the
`|q| = 1` fibre regime, real `b`, remains open."* Anyone reaching for inversion as
a bridge is reaching across a boundary the class definition already draws. Worth
recording as a trap: the class's `hb : 0 < b.re` reads like a mild positivity
hypothesis and is in fact the thing that keeps the two branches apart.

### B2. `q~` as a CARRIER — pruned on the SECOND target number, scope-(a)

This is the finding that generalises, and it is the first use I have made of
section D's `|P'/P|` constraint against a non-Laurent candidate. Target:

    P(q0)       = 1.997259194490263    (+/- 5.7e-7 relative)
    |P'/P|(q0)  = 2.176                (~4 figures)

`q~ = exp(+- pi^2 / ln q)`, so `|d ln q~/dq| = pi^2/(q ln^2 q) = 816.73` at q0.

    [2]_q                0.0937     23.2x too flat
    2 - 3h^4             0.0996     21.8x too flat
    chi^(2,1)(B_3)       0.1018     21.4x too flat
    tr M_4_1             1.7363     1.25x too flat
    TARGET               2.176        --
    q~ (modular dual)  816.73      375.3x too STEEP

**So the target is BRACKETED: basket max 1.7363 < 2.176 < 816.73.** The declared
Laurent forms are all too flat; the modular-dual scale is far too steep. The
overshoot is branch-independent (the two `arg b` branches flip the sign of
`ln q~`, not the slope), so this is a fact about the modular-dual SCALE and not a
convention choice. Cross-checked closed form vs central difference to 15 digits.

That bracket is a reusable filter: it says the carrier's steepness is
intermediate, which is a real constraint on route 5 and not merely another
exclusion.

### ROUTE 5 SPLITS — update the route table's reading, not its rows

Route 5 ("TRANSCENDENTAL construction") named four candidates: *"a q-exponential,
Faddeev's Phi_q, a holonomy/monodromy, a matrix exponential."* Those are not
interchangeable. After this session:

    5a  modular-double / q~ family ...... PRUNED (B1 mechanism, B2 magnitude)
    5b  holonomy / monodromy family ..... OPEN — unchanged, and it IS branch 3

Rows 1-4 and 6 are untouched.

### WHAT IS DELIBERATELY NOT PRUNED — `Phi_b` survives as an INGREDIENT

Per "Before declaring refuted", a scope-(b) exclusion must not over-narrow.
`Phi_b`'s `b`-shift relation

    Phi(z - i b/2) = (1 + exp(2 pi b z)) * Phi(z + i b/2)

carries NO `exp(-1/t)` non-perturbative scale — its prefactor is an ordinary
exponential in `z`, so B2's 375x overshoot does not touch it. `Phi_b` remains a
live transcendental ingredient for 5b/branch 3. What is excluded is the
INVERSION as a bridge and `q~` as a carrier.

### AND THE NEXT MOVE IS A FIT — naming it rather than taking it

The shift prefactor's log-slope in `q` depends on `z`, so `z` is a dial that can
be set to hit 2.176. That is selection against the target, banned outright by
§NO FITTING. `z` has to come out of the braiding.

### THE SHARPEST THING THIS SESSION FOUND IS A POINTER, NOT A PRUNE

Branch 3 / 5b is the Kohno-Drinfeld / KZ picture, and this bean's own 2026-08-22
entry already noted that **the canonical chain invokes exactly that shape at
step ②, "Yekutieli non-abelian Stokes."** Combined with the bracket above, the
target for the next agent is much narrower than "derive alpha":

  - the carrier is a HOLONOMY of the step-② connection, not a character value
    and not a modular-dual scale;
  - it must land at `P(q0) = 1.99726` with `|P'/P| = 2.176` — intermediate
    steepness, between the Laurent basket and the modular-dual scale;
  - `z` (or whatever plays its role) must be DERIVED from the braiding, since
    fitting it is what is being refused.

The concrete next step I would take: compute the holonomy log-slope of the
step-② non-abelian Stokes connection at q0 and check it against 2.176 BEFORE
attempting any closed form. That is the formalize-first move — the slope is one
number and it either brackets or it does not.

Two traps for the next agent, both cost me time here:
  - **A bare `lean` is a WEAKER check than `lake`.** Without `-DautoImplicit=false`
    this file's first draft would have auto-bound rather than errored.
  - **`LEAN_PATH` must put the PAPER tree FIRST.** With `scripts/lean-direct-env.sh`
    alone the ROOT tree shadows it and the import fails on a Mathlib olean that is
    present in the paper tree and absent from the root one — and the error names a
    root-tree path, so it reads like a missing dependency rather than a shadowing.


## 2026-09-12 (2) — 5b measured. Step-2 is FLAT too, and my own "next step" was not runnable.

SELF-CORRECTION FIRST. My entry above closed with "compute the holonomy log-slope
of the step-2 non-abelian Stokes connection at q0". **That is not runnable as
worded** — there is no constructed step-2 connection — and establishing that is
the useful half of this entry.

PR #7252 (same branch). Probe 7/7:
`computations/qbeta/qbeta_pdix_step2_holonomy_slope_probe.py`

### There is no step-2 connection to take a holonomy of

Verified at the Lean, NOT from the cheat sheet — whose own §2a records that its
status column was the thing that was wrong, so it is not a primary source here
either:

  * `QOU.Mass.HeckeStokes.stokes_curvature_factors` is
    `X^2 - (q - 1/q)X - 1 = (X - q)(X + 1/q)`, discharged by `field_simp; ring`
    over a generic field. Sound and load-bearing (it is where the eigenvalues
    `q`, `-1/q` come from) but it is an algebraic factorisation. No connection,
    no curvature form, no surface, no multiplicative integral in that file.
  * The curvature reading is a DOCSTRING in `NaStokesKeystone.lean`: the 2-form
    is STIPULATED to be the Hecke quadratic, so imposing flatness recovers it
    tautologically. AGENTS.md Derive-then-check item 8, verbatim.

So branch 3 / 5b's escape from circularity — "a connection defined WITHOUT
reference to alpha" — has no instance in the corpus. The only candidate has its
curvature put in by hand, which is the same defect `circularWitness` already
proves for branch 2, one level up.

### What IS measurable: the keystone `lw` period ladder — and it is FLAT

`NaStokesKeystone.lean` carries more than the stipulation: a content-bearing §3b
class whose open core is a genuine PERIOD, `aD(c+1) = lw c` with
`lw c = (1/(c+1)) sum_{lam|-c+1} dim_q V_lam`, stating closed forms as hypotheses
to a sorry-free conditional theorem. Measured at the proton pin against §D's
SECOND number, `|P'/P|(q0) = 2.176`:

    lw 1                1.0            slope 0        constant
    lw 2                1.33696562     0.046958636    46.3x TOO FLAT
    lw 3                2.53277966     0.22430586      9.7x TOO FLAT
    tauOf               2.64238631     0.11385448     19.1x TOO FLAT
    2*chi^(2,1)/[2]_q   1.983379502    0.1954502      11.1x TOO FLAT

**PER-REP NORMALISATION DOES NOT ESCAPE IT — the sharpest line, and it bears on
this bean's own standing structural claim.** The corpus says the carrier is the
per-rep q-Reeb phase `theta_lam = arccos(chi^lam/d_lam)` and that scalar `tr_M`
COLLAPSES it, which predicts per-rep behaves differently from the average. It
does move — dividing by `d_lam` takes the slope `0.1018 -> 0.1955`, factor 1.92 —
and is STILL 11.1x short. So **the collapse is not what costs the slope.** The
per-rep structural claim survives as a claim about WHERE the carrier lives; it
does not supply the steepness.

**The value-only trap, caught explicitly.** `lam=(3)` and `lam=(1^3)` have
`d_lam = 1`, `chi = 1` on the Borromean, so `2*chi/d = 2` EXACTLY — 0.137 % from
the target VALUE, better than most of the declared basket — with slope
identically ZERO. A value-only comparison promotes them; the second number
rejects them. This is the concrete payoff of §D being a two-number target.

CALIBRATED rather than self-consistent: the central-difference method reproduces
this bean's own recorded bare-`chi^(2,1)` entry `0.1018` as `0.101787393`
(rel 1.2e-4). A slope method that could not reproduce a known entry would be no
evidence about the unknown ones.

### The bracket is now a SPECIFICATION, not a list of exclusions

    step-2 / Laurent family   0.047 .. 0.224      9.7x - 46x TOO FLAT
    best declared basket      1.7363              1.25x too flat
    TARGET                    2.176                 --
    modular dual q~         816.73                375x TOO STEEP

Both sides are real corpus objects; the middle is empty. And the flatness is not
bad luck in which forms were tried — a low-degree rational in `q` at `q0 ~ 1.11`
CANNOT be steep, and a non-perturbative `exp(-1/t)` CANNOT be shallow. So the
carrier must be an INTERMEDIATE transcendental: what an ordered exponential (a
real holonomy) supplies and a polynomial average cannot.

### Consequence for the route table — no row changes, the DEPENDENCY changes

    5a  modular-double / q~ ....... PRUNED (previous entry)
    5b  holonomy / monodromy ...... OPEN, and now BLOCKED ON STEP 2 ITSELF

5b is not merely open; it is blocked on the framework's single acknowledged
geometry->algebra gap. So the honest next step is **step 2's gap**, not another
candidate-form sweep: a multiplicative-integral construction whose curvature is
COMPUTED to be `sigma^2 - (q-q^-1)sigma - 1`, or an honest §3b restatement with
the geometric step as its hypothesis. Cheat-sheet §2a already names both options.

Scope (a) throughout, and CONDITIONAL: that `lw` IS the step-2 period is the
unproved keystone class — assumed in the measurement, not shown.

### Chain this sits in, for whoever picks it up

    qou-pdix (alpha carrier)  ->  blocked on step 2 (NaStokes geometric derivation)
    qou-cds1 (c_k ladder on the z_D base)  ->  blocked on qou-pdix
    qou-iagg (2nd dashboard re-score)      ->  blocked on qou-cds1

So the Q_beta L2 row cannot move until step 2 is constructed. That is worth
stating plainly rather than leaving qou-iagg looking like a scheduling item.


### 2026-09-12 (3) — CORRECTION to entry (2): step 2 is NOT a stipulation, and 5b's blocker is `qou-6ers`

Entry (2) above asserted, quoting cheat-sheet §2a, that *"the curvature reading
lives in a DOCSTRING ... the 2-form is STIPULATED to be the Hecke quadratic, so
imposing flatness recovers it tautologically."* **That was stale by six days.**

MEASURED DIRECTLY (2026-09-12): `QOU/Mass/HeckeMonodromy.lean` (8687 B) carries a
content-bearing **primary §3b conjecture class** `HeckeMonodromy` with four
content fields — `quad` (the Hecke quadratic on every generator), `braid`,
`far_comm`, `shadow_involution` — and `hecke_factor` **DERIVES**
`(g − q)(g + q^-1) = 0` from `quad`, sorry-free. `NaStokesKeystone.lean:23` and
`HeckeStokesEigenvalues.lean:14` are both re-scoped to cite it. Bean `qou-ba73`
did this on **2026-09-06** and is `completed`.

So the Stokes eigenvalues are a **consequence of a named conjecture**, not a
stipulation. Step 2 is honestly stated, with **no instance** — the correct open
state per §3b-tax.

HOW I GOT IT WRONG, and the route matters more than the claim: I took §2a as
current *after* quoting its own warning that its status column had been the thing
that was wrong, and I did **not** run corpus-grep **path 6 (the beans)**. Path 6
is exactly what catches this — `qou-ba73` is `completed` and its body states the
fix in one line. Same class of error as everything else in this bean's history,
committed in the entry that was correcting someone else's staleness.

WHAT THE ERROR CONTAMINATED, since a fix in one place is not a fix: commit
`89ec14181ce`, audit-doc §8.3 and §8.5, the PR #7252 body, and entry (2) above —
all said "stipulated" and "5b needs step 2 CONSTRUCTED". All four are corrected.
Cheat-sheet §2a is itself still stale on `main` and now carries a dated
correction.

WHAT DOES NOT CHANGE — the measurement. The `lw` slopes (46.3x / 9.7x / 19.1x
short; per-rep 0.1018 -> 0.1955, still 11.1x short) are computed from the
keystone's own closed forms and are independent of how the curvature is scoped.
`stokes_curvature_factors` really is a `field_simp; ring` factorisation, and
there is still no multiplicative-integral construction.

WHAT DOES CHANGE — the blocker is now locatable, and it is not "step 2 is
stipulated". Of §2a's two admissible closures:

    honest §3b restatement ...... DONE      qou-ba73 (completed 2026-09-06)
    geometric discharge ......... OPEN      qou-6ers (todo)

**And the distinction is load-bearing for 5b specifically.** `HeckeMonodromy`'s
`quad` field IS the Hecke quadratic, taken as a hypothesis — so a holonomy built
on the class inherits the Hecke relation BY ASSUMPTION. Branch 3's whole escape
from circularity is that the connection is defined WITHOUT reference to what it
is meant to produce, so the honest restatement does not supply it; only the
geometric discharge does. That is the same circularity `circularWitness` proves
for branch 2, one level up.

**So 5b is blocked on `qou-6ers`** — not on another candidate-form sweep, and not
on "constructing step 2" in the vague sense. The alternative is to carry 5b
openly as conditional on `HeckeMonodromy`, which is legitimate, but then the alpha
carrier is conditional on an unproved primary conjecture and that must be stated
wherever the carrier is cited (conditional-proved != premise-established).

I did NOT open a step-2 bean: `qou-6ers` and `qou-ba73` already cover both
options, and `beans create` is not idempotent.


### 2026-09-12 (4) — CORRECTION 2: `qou-6ers` is the WRONG bean; the state of the art is `qou-d0qq`, and it is far ahead of what entry (3) said

Entry (3) concluded "**5b is blocked on `qou-6ers`**". **That is wrong.** `qou-6ers`
is *"Formalize multiplicative-integral/non-abelian Stokes for
**tm_transient_localisation**"* — a **Ch 7 lemma** in the lifting-descent arc
(`QOU.LiftingDescent.tm_transient_localisation`, "Transient terms localise to
exceptional divisors"), with an **empty body**, created 2026-08-21. I matched it
on the phrase "non-abelian Stokes" in a bean that had no body to check the match
against: match-by-shape-not-subject, the error the detector-blindness taxonomy
records for beans specifically.

THE REAL FAMILY is the `qou-2akx` step-2 tranche, and it is much further along:

    qou-0jcd  in-progress  Step-2 plan: close cheat-sheet §2a
    qou-ba73  completed    Step-2 A: HeckeMonodromy §3b class
    qou-xipk  completed    Step-2 B: Picard-Lefschetz classical shadow
    qou-74ip  completed    Step-2 C-prune: unit-modulus KZ vs the real pin q0
    qou-d0qq  in-progress  Step-2 C: sl2 KZ on Conf3(C) pulled back along the
                           colour cubic's root map -- does its monodromy
                           reproduce the Hecke quadratic and z_D?

`qou-d0qq` is branch 3's question verbatim, and it is largely DONE on the KZ side.

### Two relationships to THIS bean's work that are worth recording

**(i) `qou-74ip` is the KZ analogue of my own locus theorem, and KZ ESCAPES where
Faddeev does not.** `unit_modulus_ne_real_gt_one`: `‖exp(iθ)‖ = 1 ≠ q` for real
`q > 1` — a real-level KZ monodromy eigenvalue cannot be the real pin. That is
structurally the same obstruction as `modular_cannot_bridge` (2026-09-12 entry 1),
reached independently. **But KZ survives it by moving to an IMAGINARY level**
(`ħ = (2/iπ) ln q ≈ −0.0664i`; `k+2 = 15.05i / 30.11i / 60.22i` under the three
`ħ` conventions). That escape is exactly what my Faddeev result shows is NOT
available to the modular double, because inversion *preserves* each locus. So the
two routes diverge precisely at the point my theorem measures, and the comparison
**favours KZ** — worth stating, since my entry (1) pruned the Faddeev sibling.

**(ii) A finding neither bean draws: the KZ MONODROMY cannot be the alpha carrier,
by the same rationality invariant that closed routes 2-4.** `qou-d0qq` records
that each `ϱ(w_j)` satisfies the Hecke quadratic (eigenvalues `q`, `−1/q`) and
that `ϱ(w₁⋯w₆) = ϱ(Δ²)` is central with eigenvalue `q⁶` on spin-3/2 and `1` on
both spin-1/2 blocks. **Every one of those is in `ℤ[q,q⁻¹]`**, so any normalised
trace of them is in `ℚ(q)` — and `2cos((z−1)h/2)` is transcendental over
`ℚ(q,z)`. Hence a **closed-loop monodromy** of the KZ connection, however
correctly it derives `HeckeMonodromy.quad`, **cannot carry alpha**.

This does NOT refute `qou-d0qq`. Its purpose is step 2 — deriving the Hecke
quadratic — and for that the monodromy is exactly right. The point is that the
SAME construction cannot double as the alpha carrier: branch 3 needs the
**OPEN-PATH holonomy** of that connection (an ordered exponential, transcendental
in the level), not its monodromy. Grepped: the monodromy-vs-open-path distinction
appears nowhere in `qou-d0qq` — the only corpus hit is this bean, where I wrote it
in entry (1) about `Φ_b`.

**And that is consistent with my bracket, which is the satisfying part.** The
monodromy eigenvalues are Laurent, so they land in the FLAT basket — the same
place `lw`, `tauOf` and the per-rep Reeb objects landed (46.3x / 19.1x / 11.1x
short). An open-path holonomy at an imaginary level is a genuine ordered
exponential and is not constrained to be Laurent, so it is the one shape that can
sit at the intermediate steepness the bracket specifies. Two independent lines —
the rationality invariant and the log-slope bracket — point at the same object.

### Corrected status of 5b

    5b  holonomy / monodromy .... monodromy half EXCLUDED (rationality, this entry)
                                  open-path half OPEN, and the KZ connection at
                                  imaginary level is the concrete candidate
                                  (qou-d0qq has the construction; the framework-
                                  side connection is its open remainder, with
                                  C1/C2/C3 already scope-(b) dead and the
                                  survivor C3' requiring the deformation as an
                                  INPUT -- forever-gate-consistent)

So the honest next step is **not** a new route: it is the open-path holonomy of
`qou-d0qq`'s KZ connection, measured against `P(q0) = 1.99726` and
`|P'/P| = 2.176`. That is a well-posed computation on an object that now exists.

I did NOT create a bean for this: `qou-d0qq` is the carrier and is in-progress. A
cross-link note has been appended there, status untouched.


### 2026-09-12 (5) — the target restated in the KZ level variable: `|d ln F/dhbar| = 3.794`, an O(1) number

Small, and deliberately scoped. Probe 4/4:
`computations/qbeta/qbeta_pdix_target_in_kz_level_probe.py`

Entry (4) put the surviving route at the OPEN-PATH holonomy of `qou-d0qq`'s KZ
connection. A holonomy of that connection is naturally a function of the LEVEL,
not of `q`, so the target has to be converted before anything is computed with it.
`qou-d0qq` fixes `hbar = (2/(i*pi)) ln q`, purely imaginary at the real pin.

    |hbar|             = 0.066425365618482     (matches the bean's -0.0664i)
    |dhbar/dq| at q0   = 0.5735423928537
    => |d ln F/dhbar|  = 3.793965411

The bracket in the same units: Laurent `lw 2` 0.0819, `lw 3` 0.3911, best declared
basket 3.0273, **TARGET 3.7940**, modular dual 1424.0.

**WHAT IT DOES NOT ADD, stated first because this is the part that would get
mis-quoted.** The conversion is multiplication by a CONSTANT at fixed `q0`, so
**no ratio moves** — verified in the probe: the worst flat factor is 46.338654x in
`q` and 46.338654x in `hbar`, identical. The `hbar` column is the same measurement
in different units, **not** a second confirmation. A units change that leaves every
ratio fixed is exactly the kind of thing that gets re-quoted as independent
evidence, so the probe asserts the equality rather than leaving it implicit.

**WHAT IT DOES ADD: a shape constraint on the carrier.** In the connection's own
variable the required log-derivative is **O(1)** — not O(0.1) like a low-degree
Laurent polynomial at `q0 ~ 1.11`, not O(10^3) like a non-perturbative
`exp(-1/t)`. For a perturbative series `F = F0 (1 + a1*hbar + ...)` that reads
`a1 ~ 3.794`, which is the size of a **Drinfeld-associator coefficient** (the
associator's entries are multiple zeta values — O(1) rationals in `zeta(n)`). So
the bracket's qualitative verdict, "intermediate transcendental", becomes a
**checkable target on the leading coefficient of the open-path holonomy's
hbar-expansion**. That is a sharper handoff than "compute the holonomy".

**🛑 AND A NON-FINDING, recorded so it is not rediscovered as structure.**
`a1*|hbar| = 0.2520155395`, which is **0.806 % from 1/4**. This carries **no
information**: `a1` is *defined* by dividing the target by `|dhbar/dq|`, so the
product is the target rearranged, and any target value would yield some such
product. It fails the `S_leak` offset-genericity test trivially, because the
quantity is not independent of the thing it is being compared to. Noted only
because a suggestive simple fraction at sub-1 % is precisely what gets written up
as a result.

**STILL OPEN — this is a restatement of the target, not a holonomy computation.**
And what can be computed today is the KZ side alone: `qou-d0qq`'s open remainder is
the FRAMEWORK-side connection (C1/C2/C3 scope-(b) dead, survivor C3' needing the
deformation as an INPUT), so any agreement found on the KZ side would be
**conditional on the `KZPullbackGenerators` interface**, not derived. Worth saying
before someone computes an associator coefficient, matches 3.794, and reports a
closure.


### 2026-09-12 (6) — my "well-posed single number" is NOT well-posed: the open-path holonomy has two free choices and a factor-2

Entry (5) closed by calling the next step "a well-posed single number": compute the
open-path holonomy's leading `hbar`-coefficient and compare it to 3.794. **Checked
against what `qou-d0qq` actually pins, that is wrong, and running it as stated
would be a fit.**

WHAT IS PINNED. The LEVEL is genuinely pinned convention-free —
`KZLevelFromHeckeNormalisation` (sorry-free) fixes it from the half-twist
eigenvalue RATIO (split Casimir 1/4 on Sym^2, -3/4 on Lambda^2 => ratio
`-e^{i pi hbar}`; matching Hecke's `-q^2` gives `q^2 = e^{i pi hbar}`). That is a
ratio, so it is independent of overall normalisation. Good.

WHAT IS NOT PINNED, and each one is a dial that could be turned to hit 3.794:

1. **The open PATH is unspecified.** Everything `qou-d0qq` measures is a CLOSED
   loop — the six lassos (all positive half-twists) and their product `Delta^2`.
   An open-path holonomy needs endpoints, and none are named. Different paths give
   different leading coefficients.
2. **The FUNCTIONAL is unspecified.** For the closed loops the bean uses the
   pivotal trace (giving `z_D`), but an open-path holonomy is **not
   conjugation-invariant**, so "its trace" is not canonical — it depends on the
   endpoints and the framing. Which matrix element or invariant plays the role of
   `P` is a choice, not a consequence.
3. **And the level carries a factor-2 ambiguity the bean itself records.** Its
   2026-09-07 correction: *"q^2 = e^{i pi hbar} is conditional on Skein
   normalisation (H) — under (J) the ratio is -q and hbar halves"*, with the level
   mapping `k+2 = 15.05i / 30.11i / 60.22i` across the three `hbar` conventions.
   A factor 2 in `hbar` moves the required `a1` by a factor 2 — from 3.794 to
   1.897 or 7.588 — which is larger than the gap between the target and the best
   declared form (1.25x).

So the comparison has at least two unfixed choices plus a factor-2, against a
single target number. **Landing on 3.794 under those conditions is selection
against the target, which §NO FITTING forbids outright.** I am not running it.

WHAT WOULD MAKE IT WELL-POSED, in order:

  (a) resolve the Skein normalisation (H) vs (J) so `hbar` is fixed, not fixed
      up to 2 — this is already a known open item on `qou-d0qq`;
  (b) derive the open path from the construction (the framework-side connection
      is what would supply endpoints; C1/C2/C3 are scope-(b) dead and survivor C3'
      needs the deformation as an INPUT, so this is the same blocker as before);
  (c) derive the functional from the pivotal structure rather than choosing a
      matrix element.

Only (a) is plausibly separable from the framework-side connection. (b) is that
connection. So **5b's real blocker is unchanged from entry (4)** — it is
`qou-d0qq`'s framework-side connection — and entry (5)'s O(1) statement stands only
as a SHAPE constraint, not as a runnable comparison.

META, because this is the third time this session and it has cost turns. I named a
"next step" three times at a level of abstraction where it read as actionable, and
each time the detail showed it was not: (i) "compute the step-2 holonomy" — no
connection exists; (ii) "blocked on qou-6ers" — wrong bean; (iii) "a well-posed
single number" — two free choices and a factor-2. The common failure is naming the
step from the SHAPE of the object rather than from what is pinned about it. The fix
is the one this entry applied: before calling a computation well-posed, enumerate
what the source artifact actually fixes and what it leaves free, and count the
dials against the number of targets.


### 2026-09-19 — RESUMING AFTER 6 DAYS / 1099 COMMITS: most of PR #7252 is superseded, and I am an instance of the staleness class this bean documents

Branch `claude/pdix-attack-b-modular-double-2026-09-12` sat unmerged for six days.
`origin/main` is **1099 commits** ahead; main's copy of this bean is **3363 lines
against my branch's 2224**. Audited my own PR against it rather than assuming.
No textual conflict (all my files are new). The substance is another matter.

#### What is DEAD

**1. The target itself is on the RETIRED base — this kills §3 and §4 of the PR.**
The 2026-09-14 synthesis entry states it directly: *"the **ladder form itself** —
`α_req` and its window are inverted from that same retired base."* `α_req` **is**
my target `P = 1.997259194490263`, `|P'/P| = 2.176`. So my flat-basket table and
the whole "bracket is a specification" conclusion measure corpus objects against a
requirement that no longer holds. The cheap test that entry gives — *does the
number trace to `Q_A = m_e|q²−2q−1|(q+1)/(2q³)`?* — is exactly the `z = 1` cell
retired on 2026-09-08. **I reported that bracket to the author across many turns
with increasing confidence. It is aimed at a retired cell.**

**2. The dependency chain is superseded, by sorry-free Lean.** My PR asserts
`qou-cds1 -> qou-pdix -> qou-d0qq` and "the Q_β L2 row cannot move until the
framework-side connection lands". The 2026-09-13 entry *"DERIVING α CANNOT UNBLOCK
qou-cds1"* excludes the second link scope-(b) via `Real.cos_le_one`: the ruled
base needs `Q_codata/Q_D = 1.7592 > 1` while every cos-rung is `≤ 1`, so **no
phase repairs a 43 %-low base**. α is **not** on the L2 critical path.

#### What is DEFECTIVE but repairable

**3. My `375× too steep` is convention-unlabelled, and the corpus has a canonical
convention that predates my work by five days.**
`computations/qbeta/qbeta_modular_double_reciprocity.py` (scope-**(b)**, landed
**2026-09-07**) uses `q = exp(2πi b²)` (line 95) and proves
`log q · log q̃ = 4π²` identically, forcing `|log q̃| = 378.36`, `q̃ ≈ 4.8e-165`.
I used `q = exp(iπ b²)`. Measured: my `|d ln q̃/dq| = 816.73` is `3266.91` in the
canonical convention — **1501× too steep, not 375×**. The conclusion strengthens;
the quoted number was unlabelled.

**And my corpus-grep missed that producer entirely** — a scope-(b) exclusion of
the modular-double bridge, on `main`, five days before I began attack B. My PR
instead cites the weaker `FaddeevPhi` docstring as "the corpus's own" separation.

#### What SURVIVES

**4. `ModularDoubleLocusSeparation.lean` (6 sorry-free theorems) is a genuine
pin-INDEPENDENT complement**, and is not duplicated. The reciprocity producer
gives a *quantitative* exclusion **at the substrate pin** (165 decades). Mine
gives a *structural* one at **every** pin: inversion fixes the real axis and the
imaginary axis setwise, so no pin admits the bridge. Different statements; the
sibling's is sharper where it applies, mine is broader. Parallel derivation is
permitted — but it must CITE the prior result, which the PR does not.

#### The class, and that I am in it

The 2026-09-14 entry names this as a **class**: the 2026-09-08 base ruling
silently invalidated arguments computed against the old cell, and two sessions
found instances independently. **This is a third instance, and it is mine.** It
also cuts both ways there — a stale *negative* re-opens a route — so my §3/§4
must be **re-aimed, not re-asserted**, if anyone wants them.

#### Disposition

PR #7252 is being cut back to the surviving claims. `qou-pdix` stays **OPEN** and
its priority is lower than I reported: α is off the L2 critical path.
