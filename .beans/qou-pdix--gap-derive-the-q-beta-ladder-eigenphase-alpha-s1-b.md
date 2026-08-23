---
# qou-pdix
title: 'GAP: derive the Q_beta ladder eigenphase alpha (S1 blocker) — carrier is vacuous, exact-bridge route refuted'
status: todo
type: task
priority: normal
created_at: 2026-08-22T15:35:20Z
updated_at: 2026-08-23T00:35:56Z
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
