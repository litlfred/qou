---
# qou-pdix
title: 'GAP: derive the Q_beta ladder eigenphase alpha (S1 blocker) — carrier is vacuous, exact-bridge route refuted'
status: todo
type: task
priority: normal
created_at: 2026-08-22T15:35:20Z
updated_at: 2026-08-22T20:32:20Z
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
