---
# qou-edt7
title: 'GAP: what replaces the multiplicative assembly W=1-PROD f — both corpus assemblies miss the 3-body sign, in OPPOSITE directions'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T03:16:24Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
---

Opened 2026-08-30 after #6059 merged (207ee81f). The merged tranche 3 named the
ASSEMBLY as the defect locus; this bean is the successor question.

## The trilemma -- both corpus assemblies miss the 3-body sign, opposite ways

AME2020 Ursell cumulants (measured, he4_body_order_shortfall_location_probe):
    b2 = 2.224566   b3 = +1.426222   b4 = +9.243387  MeV

ASSEMBLY 1 -- multiplicative / Mayer, W(K) = 1 - PROD f_ij, normalised at the
deuteron. This is what the 08-29 probe and PROBE 2 use.
    b3 = 3*f_pn - 2 - P3,  P3 >= 0  =>  b3 <= 3*f_pn - 2
    b3 > 0 REQUIRES f_pn > 2/3; all four measured f_pn are below it (largest
    z_D = 0.61269). => b3 < 0 ALWAYS.
    PROVED: QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos (merged, sorry-free).

ASSEMBLY 2 -- pairwise-additive log form, B = -alpha * SUM_{i<j} ln f_ij. This is
the form the 2026-08-08 audit s10a DERIVES (tr_M multiplicative + energy
extensive => Cauchy functional equation => f = c*ln x, "the log form is forced").
    A pairwise-additive map has ALL connected cumulants above 2 identically zero:
      uniform g: B(2)=g, B(3)=3g, B(4)=6g
      b2 = g;  b3 = 3g - 3*g = 0;  b4 = 6g - 6g - 4*0 = 0
    => b3 = 0 EXACTLY, not merely small. (Arithmetic, not a fit.)

So: assembly 1 gives b3 < 0, assembly 2 gives b3 = 0, nature gives b3 > 0.
NEITHER corpus assembly can produce a positive connected 3-body cumulant.

## What this constrains about a replacement

  * It must be NEITHER pairwise-additive (b3 = 0 identically) NOR
    multiplicative-with-f_pn<=2/3 (b3 < 0).
  * It cannot be reached by changing the EDGE SET (b3 bound is edge-set
    independent), the LIKE-PAIR TYPING (inside P3), or the ENERGY SCALE
    (b3's sign is scale-free) -- all three proved in the merged file.
  * It cannot be a per-lambda reweighting (PROBE 4 / #5234 scaling wall).
  * Tranche 2 adds: it must be ARRANGEMENT-INDEPENDENT, which the linear chain
    provably is not at q != 1 (ChainBondOrderDependence.orderIndependent_iff).

## The tension worth noticing

s10a's derivation of the log form is a real argument (multiplicativity +
extensivity => Cauchy => log). If it is right, assembly 2 is FORCED -- and
assembly 2 has b3 = 0, so the corpus would be committed to a functional that
provably cannot reproduce a nonzero 3-body cumulant. Either the s10a derivation
has an unstated hypothesis (most likely: it assumes the atom trace factorises
over INDEPENDENT subsystems, which is exactly what a bound state is not), or the
body-order series is not the right decomposition of B.

That is the honest next question, and it is a DERIVATION question, not a fit.

## Do NOT

  * propose a functional chosen because it lands b3 > 0 -- that is the forbidden
    anchor inversion in new clothes;
  * re-run an edge-set / typing / scale variant expecting the sign to move.


## HALF LANDED 2026-08-30 — the trilemma is now machine-checked

> **SUPERSEDED 2026-08-30 (PR #6088, Copilot review) — the artifacts named in
> this block DO NOT EXIST.** `QOU/MassTheory/PairwiseAdditiveCumulants.lean` and
> its `pairwise_b3_eq_zero` / `pairwise_b4_eq_zero` / `ame_b3_pos` /
> `no_pairwise_matches_ame` / `trilemma` were DELETED, not merged — #6101 landed
> a strictly more general version. Read the "SUPERSEDED IN PART" section below
> for the full account. The live artifacts are:
>
> | result | lives in | declarations |
> |---|---|---|
> | pairwise-additive => b3 = b4 = 0, every bond functional | `QOU/Mass/PairwiseCumulantVanishing.lean` | `b3_eq_zero_of_isPairwise`, `b4_eq_zero_of_isPairwise`, `b3_eq_zero_ofBondFunctional`, `not_isPairwise_of_b3_ne_zero` |
> | the AME instantiation (b3 = 1.4262225, not pairwise) | `QOU/MassTheory/AmeBindingNotPairwise.lean` | `ameMap`, `ame_b3_eq`, `ame_not_isPairwise` |
>
> The block below is kept as the record of what this bean asked for and what was
> built for it; it is not a pointer to live code.


Lean: QOU/MassTheory/PairwiseAdditiveCumulants.lean, sorry-free, lean-direct
exit 0, #print axioms clean on all 9 decls.

  pairwise_b3_eq_zero / pairwise_b4_eq_zero -- a pairwise-additive assembly
      B(A) = C(A,2)*g has b3 = 0 and b4 = 0 EXACTLY, for every g. Not small.
  ame_b3_pos            -- AME's b3 > 0, from the 08-29 probe's own literals.
  no_pairwise_matches_ame / trilemma -- so no pairwise-additive assembly
      reproduces the measured 3-body cumulant.

With the merged MayerThreeBodySign.b3_neg_of_le (multiplicative assembly below
the 2/3 threshold => b3 < 0), both corpus assemblies are now machine-checked to
miss the measured sign, in opposite directions. The trilemma is no longer an
argument in a bean; it is two sorry-free files.

### STILL OPEN — and it is the whole question

What replaces the assembly. Nothing here proposes one, and the constraint list in
the body above stands unchanged. The 08-08 s10a Cauchy derivation of the log form
is untouched by this: if it is right, the corpus is committed to a functional
with zero 3-body content while the body-order programme needs some. My reading
of where the escape is -- judgement, marked as such in the Lean docstring too --
is that s10a assumes the trace factorises over INDEPENDENT subsystems, which a
bound state is not.


## SUPERSEDED IN PART ON MAIN 2026-08-30, and ONE SEAM CLOSED

#6101 (merged 06:42) landed QOU/Mass/PairwiseCumulantVanishing.lean with
b3_eq_zero_of_isPairwise / b4_eq_zero_of_isPairwise / b3_eq_zero_ofBondFunctional
-- general over EVERY bond functional. My PairwiseAdditiveCumulants.lean assumed
a COMMON BOND VALUE and is a special case, so it was DELETED rather than merged.

WHAT WAS GENUINELY MISSING, and is now added
(QOU/MassTheory/AmeBindingNotPairwise.lean, sorry-free, axioms clean):
their not_isPairwise_of_b3_ne_zero is the falsifiable form, and its docstring
instantiates it against measurement -- "Since AME2020 gives b3 = +1.426222 != 0,
the physical binding is not of this shape" -- IN PROSE. No BindingMap is built
from AME numbers anywhere on main. So the step from the general theorem to the
physical conclusion was asserted, not checked. Now:
  ameMap        -- pairs at B(D)=2.224566, triples at the 3H/3He isospin average
  ame_b3_eq     -- b3 = 2852445/2000000 = 1.4262225 exactly
  ame_not_isPairwise

DISCREPANCY NOTED, NOT RESOLVED: the 4He AME literal is 28.295673 in
he4_body_order_shortfall_location_probe.py and 28.2956624 in #6101's writeup --
1.1e-5 MeV apart. b3 does not depend on it, so the b4 leg was deliberately NOT
instantiated. Someone should reconcile the two literals against the AME2020
table before any b4 statement is machine-checked.

THE GATE IS STILL OPEN. Both assemblies are now excluded on main; nothing
proposes a replacement.


## RESOLVED (2026-08-30): the ⁴He AME literal discrepancy is a KNOWN, already-fixed defect

#6088 flagged `28.295673` (in `he4_body_order_shortfall_location_probe.py:90`) against
`28.2956624` (used in the #6101 writeup) — 1.06e-5 MeV apart — and deliberately left it
unresolved. It is settled, and the corpus settled it before either of us:

**28.2956624 is correct. 28.295673 is a hand-typed legacy literal.**

The producer `computations/ame_2020_binding_energies.py` names this exact pair in its own
docstring (lines 14-24), as one of six entries where a hand-typed witness disagreed with the
vendored AME2020 publication table:

    B_he4   28.295673   vs  28.2956624   (+10.6 eV)

and records that AME's own uncertainty on B(⁴He) is 0.8 eV, so "a 10.6 eV gap is ~13 sigma —
not a rounding artifact".

Independent confirmation, three ways:
1. Mass-excess route by hand: 2*7288.971064 + 2*8071.31806 - 2424.91587 = 28295.662378 keV.
2. `computations/ame-2020-binding-energies.witness.json` carries
   `B_he4_MeV = 28.2956624` and `B_he4_MeV_mass_excess_route = 28.295662378`, and the
   producer asserts the per-A and mass-excess columns agree for every nuclide.
3. `codata_constants.ame_binding_mev(2, 4)` returns `28.2956624` (run at 50 dps).

**The fix already exists as a function call** — `AME_B_HE4_MEV_VALIDATION = _ame_binding_mev(2, 4)`
in `computations/substrate/codata_constants.py:315`. What never happened is the consumer
migration: **82 live (non-`_deprecated/`) files still hardcode `28.295673` or `28.295674`**,
including 11 under `computations/deltalambda/` and 20 under `computations/probes/`.

Magnitude: 3.7e-7 relative. It cannot move any conclusion in this arc — the assembly defect
is 30 %+ — so the trilemma above stands unchanged with either literal. Recording it as a
separate stale-literal class rather than sweeping it here; a sweep touches long-compute
producers and would need its own scope. Tracked separately.


## SUCCESSOR QUESTION — a reframing, not a functional (2026-08-30, e04728dc09)

Lean: `QOU/Mass/CoordinationWeightDifferences.lean` (sorry-free, lean-direct exit 0,
11 decls, axioms clean). Probe:
`computations/probes/body_order_is_finite_difference_of_coordination_weight_probe.py` (5/5).
Audit: `docs/audits/2026-08-30-body-order-cumulants-are-finite-differences-of-w.md`.

**This proposes no functional.** The bean forbids choosing one because it lands
b3 > 0, and that prohibition is respected. It changes variables.

### The identity

Write B(A) = C(A,2) * w(A-1), with w(z) the mean binding per nucleon pair at
coordination z = A-1. A DEFINITION, not a model — the formula recovers any B.
Under it the Ursell cumulants are exactly

    b_n = C(n,2) * Delta^{n-2} w(1)

term-by-term via C(n,k)C(k,2) = C(n,2)C(n-2,k-2). Lean-proved at n = 3, 4;
symbolically verified n = 2..8 against an arbitrary w; NOT claimed proved in general.

### THE TWO WALLS ARE ONE WALL

- w constant       => b3 = 0  — the pairwise wall, recovered as the Delta w = 0 case
- w non-increasing => b3 <= 0 — `b3_nonpos_of_le`

So the Mayer sign is **not a separate obstruction**. ANY saturating assembly has a
non-increasing w and lands at b3 <= 0. That is why this bean's own constraint list
found edge set, like-pair typing and energy scale all failed to move the sign:
none of them changes whether w RISES.

### The whole content of b3 > 0

    w(1) < w(2)

i.e. the mean binding per pair is larger at coordination 2 than at coordination 1.
Measured w(1) = 2.2245662, w(2) = 2.6999729 MeV/pair, rise 0.4754. That single
inequality is the falsifiable form (`lt_of_b3_pos`). Similarly b4 > 0 <=> w convex
at z = 1.

### The new constraint, and it is a pincer

Measured w rises to a SHARP MAXIMUM AT THE ALPHA PARTICLE (4.7159 at z = 3) then
decays monotonically (2.133 at 6Li, 1.063 at 16O, 0.320 at 56Fe). And:

- b3 > 0                     <=> w rises at z = 1
- saturation of B/A          <=> z*w(z) bounded, so w -> 0

**=> w MUST BE NON-MONOTONE.** Any derivation producing a monotone coordination
weight is refuted at one end or the other. That is a genuine prune on the search
space and it did not exist before.

### The A>=5 blow-up gets a cause

High forward differences of a peaked function grow and alternate; the tower
multiplies by a growing C(n,2). Measured at z=1: D^0..D^4 w = 2.225, 0.475, 1.541,
-5.639, 11.321, giving b_2..b_6 = 2.225, 1.426, 9.243, -56.39, +169.8. The series
expands a peaked w around z = 1, THREE STEPS BELOW ITS MAXIMUM. The divergence is
an expansion-point defect, not evidence against the assembly — which reframes it
from 'the framework fails at A>=5' to 'this is the wrong series', a much cheaper
problem.

### SCOPE — do not over-cite this

The identity is a REPARAMETERISATION and is tautologically available. **It derives
no magnitude and cannot**: w is defined by inverting B, so fitting w to AME is
fitting B to AME with extra steps. THE MAGNITUDE GATE IS NOT CLOSED and this is
not progress toward closing it by derivation — it is progress on knowing what a
derivation has to produce.

### STILL OPEN — now one question instead of a tower

Derive w(z). Specifically: why does w rise from z = 1 to z = 2, and why does it
turn over at the alpha particle? The corpus has a coordination story already
(`CoordinationSaturation`, `bk-coordination-multiplicity`) whose contact with this
is unexamined — that is the next place I would look, marked as judgement.


## THE NEGATIVE HALF IS CLOSED (2026-08-30, PR #6173)

Lean: `QOU/Mass/UniformBondSimpleGraphExclusion.lean` (sorry-free, axioms clean).
Probe: `computations/probes/coordination_weight_rise_and_turnover_probe.py` (4/4).
Audit: `docs/audits/2026-08-30-why-w-rises-the-negative-half-is-closed.md`.

**PROVED — the rise is NOT about which pairs bind.** For a uniform bond weight over
a SIMPLE GRAPH, b3 = eps*(e3 - 3*e2) <= 0 always: a simple graph on 3 vertices has
at most 3 edges, a bonded pair at least 1. No monotonicity, no cap, no relation
between mass numbers. Case-(b) exclusion (the invariant is a proved counting bound).

**Strictly stronger than CoordinationSaturation**, which checked two endpoints. In
the w coordinate, a degree function gives w(z) = eps*d(z+1)/z, so complete => w
constant => b3 = 0; bounded-degree => w ~ 1/z => b3 < 0; chain => b3 = -eps. An
intermediate profile cannot rise at the bottom because d(3) <= 2 on any simple
graph. **THE WHOLE COORDINATION-MULTIPLICITY FAMILY IS EXCLUDED** as a source of
b3 > 0 — which answers the 'unexamined contact with CoordinationSaturation' I named
as the next place to look. The contact exists and it is negative.

**So the rise is non-transferability, and it is one number:**
eps(2)/eps(1) = 1.2137076 — the bond is 21.4% stronger at coordination 2.

**REFUTED — single-ratio (Markov-power) scaling, for EVERY r.** tr_{n+1} = z*tr_n
makes a bond n-dependent, which is the right kind of mechanism; its simplest form
eps(z) = eps(1)*r^(z-1) requires eps(2)/eps(1) = eps(3)/eps(2). Measured 1.2137 vs
1.7467, **43.9% apart**. Convention-independent: a single ratio of ANY value cannot
produce two ratios 44% apart. Scope-(a) — kills the family, not the mechanism.

**REFUTED — same-orbital pair fraction** beyond A=7: <8% at A=5,6,7 with one
normalisation, then 29.7% at A=9, 166% at A=16. Scope-(a).

**SURVIVES — the turnover LOCATION.** Wigner SU(4)'s [1^n] has dim = C(4,n), which
VANISHES for n >= 5, so the maximally-symmetric regime ends at A=4, where the peak
is. Parameter-free. Caveats asserted in the witness: it LOCATES without SIZING, and
rests on Wigner's symmetry-to-binding assumption, not derived here. NOTE this is a
SUPPORT bound (C(4,n)=0), not the C(4,n)>0 positivity argument an earlier probe of
mine made about a SIGN — that was wrong and is not reused.

### STILL OPEN — one number
Why eps(2)/eps(1) = 1.2137 (and eps(3)/eps(1) = 2.1200). Nothing tested predicts
either. No magnitude is derived here; what changed is that a large family is gone
from the search and the remainder is a single sharply stated quantity.


## beta CANNOT BE DERIVED — and the answer RETRACTS the lead (2026-08-30)

Lean: `QOU/Mass/SU4CasimirIsAffineInPairCount.lean` (sorry-free, axioms clean).
Probe: `computations/probes/su4_casimir_beta_derivation_probe.py` (3/3).

**The SU(4) Casimir of [1^n] is AFFINE IN THE PAIR COUNT:**

    C2([1^n]) = (5/8)n(4-n) = (15/8)n - (5/4)C(n,2)

and the sum a two-body SU(4)-invariant interaction actually contributes,
S(n) = (1/2)[C2 - n*C2(fund)] with C2(fund) = 15/8, is EXACTLY proportional to
the pair count:

    S(n) = -(5/8) C(n,2)      for every n, exactly (verified n=2..12, dev 0.0)

So such an interaction contributes a CONSTANT PER PAIR => w constant => b3 = 0.
That is the pairwise wall reached from group theory instead of from the counting
bound in UniformBondSimpleGraphExclusion; the two agree, which checks both.

**Therefore the fitted w = alpha - beta*C2 is NOT the SU(4) prediction**, and
there is no coupling for beta to be. The lead is retracted as a derivation route.

### What the fit actually was
C2 = 2.5, 1.875, 0 at A=2,3,4, so fitting the endpoints and predicting the middle
is a FIXED interpolation with zero remaining freedom: lambda = 3/4 EXACTLY, i.e.

    w(3) = (3/4)w(2) + (1/4)w(4)   <=>   B(4) = 8B(3) - 18B(2)

Two consequences:
1. It IS better than the corpus simplex baseline mu4=0 (B(4)=4B(3)-6B(2)), which
   misses B(4) by 32.7%; this misses by 1.7% on the Coulomb-corrected convention.
   Real, and why the fit looked good.
2. The residual is variable-dependent. SAME convention: 0.71% on B(3), 1.709% on
   B(4), amplification 8*B(3)/B(4) = 2.4. I quoted the smaller.

### A correction to my own scratch output
A scratch run printed '18x' for that amplification. It was hardcoded prose, not
computed, AND it crossed two conventions (0.71% from 3H against 12.5% from the
isospin average). The computed factor is 2.4, consistent across conventions.

### UNTOUCHED
The SUPPORT bound dim[1^n] = C(4,n) = 0 for n >= 5 still locates the turnover at
A=4. It uses the VANISHING OF THE REPRESENTATION, not its Casimir, so this result
does not reach it. Wigner SU(4) as physics is not refuted; one route is closed.

### STILL OPEN
The rise itself. Both SU(4) routes to the MAGNITUDE are now shut (two-body: no
Casimir term; single-ratio Markov: refuted under all three conventions), and
closed-form guessing is entropically dead at the target's 1-2 significant digits.
What is left needs a genuine three-body operator, and the corpus's own candidate
is the Milnor triple linking number (all pairwise linking zero, mu-bar_123 != 0)
-- the topological object with exactly the required structure. That is qou-brng.


## MILNOR CANNOT CARRY THE MAGNITUDE EITHER (2026-08-30)

Lean: `QOU/Mass/MilnorCarriesOrderNotMagnitude.lean` (sorry-free, axioms clean).
Probe: `computations/probes/milnor_order_not_magnitude_probe.py` (1/1).

I proposed Milnor mu-bar_123 as the last candidate — 'three-body by construction',
since a Brunnian link has all PAIRWISE linking zero while mu-bar(123) != 0. Right
about the SHAPE, wrong about the TYPE, and **the corpus already said so**:
`QOU.KnotTheory.Vassiliev.brunnian_exact_leadingOrder` states the A-component
Brunnian link's first non-vanishing Vassiliev invariant sits at degree
leadingOrder A = 2(A-1) and takes the value **+-1**.

**mu-bar is NORMALISED. It has no size.** If b_A = c_A * mu-bar then |b_A| = |c_A|
— the magnitude is entirely c_A's. Same category error as the SU(4) Casimir: right
structure, wrong type.

**And the order law it does suggest is REFUTED.** mu-bar supplies the DEGREE
2(A-1); the minimal quantitative reading b_A = s_A g^{2(A-1)} with |s_A| = 1 gives
a division-free test with g eliminated:

    b3^2 = b2 * b4

Measured it is out by **10.11x** (isospin average) and **5.25x** (Coulomb-
corrected). Scope-(a): the single-coupling family falls, not Milnor's involvement.

**NOT claimed**: MilnorParitySignLaw predicts sign(1-tau_A) = (-1)^(A-1) = -,+,-
while the measured cumulant signs are +,+,+. 1-tau_A is NOT b_A and no relation
between them is established — flagging it as a non-conflict rather than reporting
a refutation I have not earned.

### WHERE THIS LEAVES THE FRONT
Three mechanism families are now closed by proof or measurement: uniform-bond
simple-graph (proved), SU(4) two-body (proved), single-coupling Markov/Milnor
order laws (refuted under every convention). Closed-form guessing is entropically
dead at the target's 1-2 significant digits.

What survives is one shape: **a multi-term closure in which a topological
invariant fixes each term's SIGN and ORDER while separate coefficients carry the
SIZES.** Nothing tested supplies those coefficients, and I am not proposing a
candidate — proposing one because it would fit is the anti-fit violation.

### A BEAN MIS-NAMING OF MINE, CORRECTED
I twice named `qou-brng` as 'the Milnor bean'. It is not: qou-brng is the
hbar_q^2 saturated-binding-fraction bean whose surviving route is the
linking-vs-self-energy AMPLITUDE question. Adjacent, not the same, and untouched
by this work.


## THE TWO-TERM PAIRING I PROPOSED IS DEGENERATE (2026-08-30)

Lean: `QOU/Mass/SaturationInvisibleToCumulants.lean` (sorry-free, axioms clean).
Probe: `computations/probes/two_term_structure_degeneracy_probe.py` (2/2).

I proposed pairing a CONVEX s-shell term with the corpus's SATURATING bounded-
degree term. **The saturating half is inert where the data is.**

A degree cap at k gives bond count f_k(A) = A*min(A-1,k)/2. For A <= k+1 the cap
DOES NOT BIND, so f_k is identically C(A,2) there — and C(A,2) contributes
exactly zero to b3 and b4. Measured:

    k=1: b3-contrib -1.5, b4 +2.0   (pure dimer; wrong sign)
    k=2: b3-contrib  0.0, b4 -2.0
    k>=3: b3 0.0, b4 0.0  — the cap never binds below A=5

Every (saturating, convex) pair gave a SINGULAR 2x2 system, and the singularity
IS this fact. Not a contradiction with the two-term necessity theorem — the terms
act in DISJOINT REGIMES, not together.

### What replaces the target, and it is sharper
With the saturating half inert, ONE term carries b2, b3 AND b4: three constraints
on one coefficient, and scaling cancels in a ratio, so TWO PARAMETER-FREE
predictions —

    isospin average     b3/b2 = 0.6411228   b4/b2 = 4.1551403
    Coulomb-corrected   b3/b2 = 0.8127866   b4/b2 = 3.4684851

Nothing tested is close: dim[1^A] (-2.333, 3.5), A^3 (0.375, 0.5), A! (0, 6),
indicator (-2, 3), k=1 dimer (-1.5, 2), 2^A (-1, 2).

**This is real progress on the epistemics even though no magnitude is derived.**
The old target was ONE ratio inside a 9.4% convention band, which many candidates
sit in and hitting which is not evidence. The fingerprint is TWO numbers with
ZERO free parameters — the discriminator the earlier work said it needed.

### SCOPE
Refutes the SPECIFIC pairing as an explanation of the cumulants. Does NOT touch
CoordinationSaturation (a statement about A -> infinity, unaffected by having no
A <= 4 signature), and does NOT refute two-term structures generally.


## SCREENED THE FINGERPRINT — 0 hits, and the METHOD result is the keeper (2026-08-30)

Probe: `computations/probes/fingerprint_screen_zero_parameter_probe.py` (2/2).

**Exploited an asymmetry first**: f(4) = B(4)/B(2) = 12.71963154 does not involve
the A=3 binding at all, so it is CONVENTION-INDEPENDENT; f(3) carries the whole
4.7% band [3.641123, 3.812787].

### RESULT 1 — a free parameter destroys the test (this is the durable one)
Design A: fit each one-parameter family to the solid f(4), predict f(3). Ten
families, ONE hit (alpha^A * A at alpha = 2.5219 -> f(3) = 3.7828).

**That hit is exactly chance.** The 9 valid predictions span 3.089..4.820 (range
1.731); the band is 0.172; per-candidate chance 9.9%; EXPECTED hits 0.89;
observed 1. Spending the f(4) constraint on a fitted parameter leaves ONE
prediction against a 4.7% band — a ~10% false-positive filter.

**So the fingerprint discriminates only at ZERO free parameters.** That is a
constraint on how any future candidate may be tested, and it is the useful output
of this turn.

### RESULT 2 — zero-parameter screen: 0 of 14
Both numbers predicted, nothing fitted, q0 at the proton pin. Closest overall is
the central binomial C(2n,n) at 8.45% / 8.28% — not a hit, and unremarkable among
14 candidates.

### RESULT 3 — the miss is STRUCTURED
The factorial family lands f(3) ~ 3.00-3.04 against a measured 3.64-3.81 (low by
16-18%), while [n]_q! is within **1.66%** on f(4). They get the A=4 growth roughly
right and the A=3 step badly wrong: b3/b2 ~ 0 where the measurement wants 0.64.

That is the arc's recurring defect in the fingerprint's own coordinates — **a
smooth growth law reproduces b4 far better than b3.** Whatever supplies b3 is not
a smooth growth law.

### SCOPE
Honest negative. Derives nothing, refutes no named framework claim, and is NOT an
enumeration — 14 hand-chosen functions is a sample. Do not cite it as 'the
fingerprint has been screened'.


## PAIRING PARITY DERIVES THE b3 SIGN — the first mechanism that does (2026-08-30)

Lean: `QOU/Mass/PairingParityForcesPositiveB3.lean` (sorry-free, axioms clean).
Probe: `computations/probes/pairing_parity_b3_sign_probe.py` (2/2).

Followed the structured miss (smooth laws get b4 to 1.66%, b3 low by 16-18%) to
whatever is NON-SMOOTH at A=3. It is the parities:

    A=2  2H  Z=1,N=1  ODD-ODD      A=3  3H/3He  ODD-A      A=4  4He Z=2,N=2  EVEN-EVEN

and the SEMF pairing term is parity-dependent by construction (+d even-even, 0
odd-A, -d odd-odd, d > 0).

### THE SIGN IS DERIVED
    b3-contribution = p(3) - 3p(2) = 0 - 3(-d) = **+3d > 0 for EVERY d > 0**

The signs come from which nuclei are odd and even; the magnitude never enters the
sign. **First mechanism in the arc with the measured sign for a principled
reason** — every earlier candidate either could not contribute (Delta^3 = 0),
carried no magnitude (mu-bar = +-1), or had the sign wrong (b4/b3 <= 0).

Textbook physical reading: the deuteron is ODD-ODD so pairing PENALISES it, which
is the standard reason 2H is weakly bound — and a weak B(2) is exactly what makes
b3 = B(3) - 3B(2) positive.

### THE MAGNITUDE IS NOT — and the good number was convention luck
Fit smooth + pairing to b3,b4; PREDICT b2. Best smooth partner C(2n,n):

    raw AME, isospin avg   b2 pred 2.196193   **1.28%**
    raw AME, 3H            b2 pred 1.887753    15.14%
    Coulomb-corrected      b2 pred 2.044540     8.09%

**The 1.28% does not survive the Coulomb correction, and that correction is the
physically required one**: Coulomb ~ Z(Z-1)/A^(1/3) touches 3He and 4He but NOT
2H or 3H, so 3H is the Coulomb-free A=3 point and 4He needs its own shift. A
model with no Coulomb term must be compared against corrected data. The 1.28% was
the best of nine trials on the one dataset that flatters it.

### STATUS
Strongest candidate the arc has produced. **Sign derived, size open.** Not a
closure and not a refutation — and the 1.28% must not be quoted as a result.


## delta IS OVER-DETERMINED, AND THE TWO DETERMINATIONS DISAGREE 25-40x (2026-08-30)

Probe: `computations/probes/pairing_delta_overdetermination_probe.py` (1/1).

**Method note first:** hunting a formula for delta is BANNED by this arc's own
entropy result (closed-form guessing is dead at 1-2 significant digits). The
legitimate move is OVER-DETERMINATION — delta is fixed by the A<=4 cumulants AND
independently measurable as the odd-even staggering. No formula is proposed.

    DETERMINATION 1, from the A<=4 cumulants (smooth C(2n,n) + pairing):
       raw isospin-avg    delta = 0.58901076 MeV  -> pairing at A=2  0.208 MeV
       Coulomb-corrected  delta = 0.95593837 MeV  -> pairing at A=2  0.338 MeV

    DETERMINATION 2, from the odd-even staggering (51 triples, A >= 8):
       median |D3| = 1.80355 MeV   (consistent with the standard 1-3 MeV gap)
       SEMF pairing at A=2 (a_P = 12/sqrt(A)) = 8.48528 MeV

    DISAGREEMENT: **25-41x**, the fitted term being far TOO WEAK.

**The exponent cannot rescue it.** Pairing DECREASES with A, so a term giving
0.2-0.34 MeV at A=2 cannot reach ~1.8 MeV at A~10 for any positive exponent — it
is smallest exactly where pairing is largest. The discrepancy is in the STRENGTH.

### TWO MEASUREMENT SLIPS OF MINE, both recorded
1. Taking the median of |D3|*A^1.5 over ALL A gives 88 MeV and a 92-150x ratio.
   **Contaminated**: the low-A entries (A=4 -> 85, A=5 -> 90, A=6 -> 119) are
   SHELL-CLOSURE jumps, not pairing, and dominate the median. Restricting to
   A >= 8 and comparing pairing ENERGIES gives the honest 25-40x. Headline moved
   by ~4x when the artifact was removed.
2. An earlier pass printed NO staggering rows at all — a sign filter (if d3 > 0)
   of mine that dropped every entry. Recorded so the absence is not later read as
   an absence of signal.

### VERDICT
**The SIGN result is untouched** — pairing forces b3 > 0 from the parities for
EVERY delta, and that argument never uses delta's value.

**The MAGNITUDE route is refuted.** The pairing term reproducing b3 and b4 is
25-40x too weak to be the physical nuclear pairing force. Either the term is not
really pairing, or pairing supplies only a small part of b3.

Scope (a): refutes pairing as the SOLE quantitative mechanism, not its presence
in a multi-term closure. **delta is NOT derived.**


## TWO RETRACTIONS OF MY OWN, and the reframing that survives (2026-08-30)

Probe: `computations/probes/b3_is_the_deuteron_deficit_probe.py` (2/2).

### RETRACTION 1 — the '25-100x systematic under-shoot across four mechanisms'
**I asserted this and proposed a turn investigating it. It is FALSE.** Measured in
the b3/b2 coordinate (measured 0.64112282):

    SU(N) Casimir     Delta^3 = 0 EXACTLY — ZERO contribution, not small
    Milnor mu-bar     normalised +-1 — NO magnitude at all
    n!                0.0          -> INFINITE
    [n]_q!            0.0437062    -> 14.67x
    C(2n,n)           0.3333333    -> **1.92x**

Two have no magnitude, so 'too small' is undefined for them; the rest span 1.92x
to infinite — and C(2n,n) under by less than 2x **directly contradicts the range I
quoted**. What is actually there is the tautology 'nothing produces b3'.

### RETRACTION 2 — 'the fitted pairing delta is 25-40x too weak'
Worse, because it stood as a REFUTATION. I judged the fitted A=2 pairing against
the SEMF a_P = 12/sqrt(A) = 8.485 MeV. **The SEMF has no validity at A <= 4** —
with standard coefficients it predicts

    2H  B = -4.661 MeV  (UNBOUND)    3H  2.325 vs 8.482    4He  22.841 vs 28.296

A formula that puts the deuteron below threshold cannot supply that standard.
**The refutation is WITHDRAWN.** Against the quantity pairing must actually
explain — the deuteron deficit, 0.475-0.603 MeV — the fitted 0.208-0.338 MeV is
the SAME ORDER, covering **34.5-71.1%** of it. The SEMF extrapolation is 17.8x
the entire deficit.

**PAIRING IS RESTORED as a live candidate: sign derived, magnitude the right order.**

### WHAT SURVIVES — and it is sharper than the pattern I invented
    b3 = B(3) - 3B(2) = 3 * (B(3)/3 - B(2)) = 3 * (deuteron deficit)   EXACTLY

**The b3 question IS the deuteron-weakness question.** The deuteron is 17.6-21.3%
weaker than b3 = 0 requires; in B/A it sits 2.54x below A=3 and 6.36x below 4He.
Every mechanism treating B(2) as an ordinary member of a smooth family gets b3
too small because none makes the deuteron anomalously weak — **a TWO-body anomaly
dominating a connected THREE-body cumulant.**

Relocated target: derive the deuteron deficit, not b3. It has an established
cause (near-unitary 3S1, a_t = 5.42 fm against a ~1.4 fm range; unbound 1S0
virtual state), so it is a sharper question than 'produce b3'.

The identity is trivial and is NOT a result; its value is the relocation.

## Near-unitary two-body channel — asked and answered (2026-08-30, PR #6197)

**Question:** does the framework produce a near-unitary two-body channel — the
mechanism that would explain the deuteron deficit the previous commit relocated
b3 onto?

**STRUCTURE: yes, and not by analogy.** The Hecke relation sigma^2 = h*sigma + 1
has eigenvalues q and -1/q, split by h = q - 1/q = 0.2090602988 at q0. h -> 0 as
q -> 1, so **q = 1 is the framework's degenerate point** — the structural
analogue of the 3S1/1S0 near-degeneracy that makes the physical two-nucleon
system near-unitary. Symmetric and antisymmetric channels; one splitting
parameter.

**NEARNESS: no, and the route is closed by RULE, not by physics.** q0 is a CAL-2
calibration input. Deriving q0 from the substrate is FOREVER GATED (owner ruling
2026-08-02, bean qou-eic1). A nearness derivation would have to answer 'why is q0
close to 1', which is precisely the forbidden question. **The deuteron-deficit
route therefore terminates at the q0 gate rather than at a wall in the
mathematics.**

**A near-match deliberately NOT reported as evidence.** h = 0.2090603 sits 1.93%
from the 3H deficit fraction 0.2131739. That fraction is convention-dependent
over [0.1760783, 0.2131739] — 21.07% wide — and 3 of 8 framework small parameters
land inside it (h, 1 - 1/q^2, 2*hbar_q). Three of eight is not discrimination.
Recorded in the witness so a later agent does not rediscover it and read it as a
hit.

Probe: computations/probes/framework_near_unitary_channel_probe.py (mpmath 65
dps, no float64, 2/2). Commit 755965d10d.


## THE SECOND ESCAPE HATCH IS ALSO CLOSED — isospin typing (2026-08-30, PR #6229)

Lean: `QOU/Mass/TypedBondSiteInvariance.lean` (lean-direct exit 0; `#print
axioms` on all 14 declarations = `[propext, Classical.choice, Quot.sound]`).
Audit: `docs/audits/2026-08-30-typed-bond-site-invariance-and-the-corrected-prune-map.md`.

`UniformBondSimpleGraphExclusion` names its escape hatch as "drop *uniform
bond weight* or drop *simple graph*". There are **two** ways to drop the
first, and this bean had been tracking only one of them:

* **coordination-dependence** `eps(z)` — the survivor, `eps(2)/eps(1) = 1.2137076`;
* **isospin typing** `L_pp` / `L_pn` / `L_nn` — believed closed by
  `ChainBondOrderDependence`. **It was not.** Now closed.

### Why it was open — an arity error, not a gap in effort

`ChainBondOrderDependence.orderIndependent_iff` proves arrangement-invariance
iff `L_pp = L_pn = L_nn`, and reads as "physical => uniform bonds". It does
not say that: it is a theorem about `bondSum`, the sum over **adjacent pairs
of a List Bool**, i.e. the linear chain. The counterexample is one line — on
the **complete graph** the typed sum is site-invariant for *arbitrary* L,
because `C(Z,2)`, `Z*N`, `C(N,2)` are fixed by `(Z,N)` alone.

### PROVED — the general classification

For `G` on `A >= 3` carrying both a bond and a non-bond, site invariance
(the binding depends on how many protons, not which sites) holds **iff**

    G is regular  AND  L_pp + L_nn = 2*L_pn

The mean condition is **strictly weaker** than uniformity and genuinely
suffices on a regular graph. The chain's stronger conclusion is an artifact
of the chain being **irregular** (endpoints have degree 1). Under both,

    2*B(S) = k * (L_pp*Z + L_nn*N)

— **linear in the nucleon counts**, a one-body self-energy. The graph is
erased; only the scalar `k` survives.

### Two kills

**Regular branch, two nuclei, no fit.** Along `N = Z`, with `k_2 = 1` and the
simple-graph degree bound `k <= A-1`:

    B(4He)/B(2H) = 2*k_4 <= 6        AME2020: 28.2956624/2.224566 = 12.7196

**Complete branch — and this is a HOLE IN `CoordinationSaturation`, worth
recording separately.** `complete_graph_no_saturation` assumes a single
`eps > 0`, so it does **not** cover mixed signs. The `A^2` coefficient of the
isobaric complete-graph typed sum is `L_pp + L_nn + 2*L_pn`, which **can
cancel** — a saturating complete-graph family does exist and that lemma does
not see it. It dies to a *different* invariant: under exactly that
cancellation `b3 = -2*b2`, so a bound deuteron (`b2 = 2.224566 > 0`) forces
`b3 = -4.449` against the measured `+1.426222`.

### What this changes for this bean

The pairwise class is now exhausted along every axis tested:

| vary | result |
|---|---|
| which pairs bond | `UniformBondSimpleGraphExclusion` — `b3 <= 0` |
| the bond function `f` | `PairwiseCumulantVanishing` — `b3 = 0` |
| the isospin typing | **this PR** — collapses to one-body, `2*k_4 <= 6` |
| the assembly (multiplicative) | `MayerThreeBodySign` — `b3 < 0` |

**One axis left, and it is this bean's own:** non-transferability, i.e. the
bond weight depending on coordination number. `eps(2)/eps(1) = 1.2137076`,
`eps(3)/eps(1) = 2.1200`, with single-ratio scaling already refuted here
(1.2137 vs 1.7467, 43.9% apart).

The upgrade is **epistemic, not directional**: this bean concluded "the rise
is non-transferability" after excluding the uniform family. That is now
*proved* rather than *asserted-after-one-exclusion* — it is
non-transferability, and **not isospin typing either.** Do not spend another
tranche re-testing bond typing.

### Correction to the map several briefs have been working from

A dispatch brief for this front named four prunes (`CoordinationSaturation`,
`ChainBondOrderDependence`, `BodyOrderRecurrenceDepth`, `MayerThreeBodySign`).
The tree holds at least **nine**. The five missing —
`ChainBindingNoSaturationPeak`, `UniformBondSimpleGraphExclusion`,
`PairwiseCumulantVanishing`, `SU4CasimirIsAffineInPairCount`, and now
`TypedBondSiteInvariance` — are tabulated in the audit doc above. Note
especially that `PairwiseCumulantVanishing` is **orthogonal** to the typed
classification, not stronger: it fixes the complete pair set and varies the
bond *function*, while this varies the *edge set and typing* at fixed
pairwise shape. Neither subsumes the other.

## THE GATE CLOSES ONE ROUTE, NOT THE FRONT (2026-08-30, PR #6227)

Lean: `QOU/Mass/CumulantTurnoverLowerBound.lean` (sorry-free, lean-direct exit 0,
6 decls, axioms clean). Probe:
`computations/probes/deuteron_deficit_off_gate_probe.py` (6/6).
Audit: `docs/audits/2026-08-30-deuteron-deficit-off-gate.md`.

### THE SCOPE CORRECTION -- the main finding

#6197 concluded the deuteron-deficit route "terminates at the q0 gate rather than
at a wall in the mathematics". Correct for the route it tested; does NOT
generalise. Three things get called the gate:

  G1  derive q0's VALUE from the substrate      FORBIDDEN (qou-eic1, permanent)
  G2  derive F, EVALUATE at the calibrated q0   ROUTINE -- every framework
                                                prediction does this
  G3  explain WHY q0 is near 1                  = G1, correctly gated

The near-unitarity route needs G3, because NEARNESS is a claim about q0's value.
The DEFICIT needs only G2. **So the front is an ordinary open derivation problem
and must not be recorded as gated.**

Measured, not asserted: every target quantity (b2, b3, b4, w(1..3), the deficit
fraction, B(4)/B(2)) is AME2020-only. The probe reads and prints q0 and uses it
NOWHERE below; that absence is the test.

### TURNOVER PINNED FROM BOTH SIDES, parameter-free

b3 > 0 AND b4 > 0 give w(1) < w(2) < w(3) -- the coordination weight rises
THROUGH z=3, so the turnover is at A >= 4. A LOWER bound, from measured cumulant
signs with no representation theory in it (`max_at_three`). The corpus's Wigner
SU(4) support bound dim[1^n] = C(4,n) = 0 for n >= 5 is an UPPER bound from the
opposite direction. **Independent inputs, opposite directions, meeting at A = 4.
Neither alone pins the location; together they do.**

    isospin avg   b3 = 1.42622016  b4 = 9.24338456
    Coulomb-corr  b3 = 1.80809760  b4 = 7.71587480
    w(1..3), w(5) = 2.2245662, 2.69997292, 4.715943733, 2.13293248

### THE ABSENT CHANNEL CARRIES AT LEAST THE WHOLE DEFICIT

Every closed mechanism is saturating, hence non-increasing in w -- which is why
each lands at b3 <= 0. Split w = u + v with u that background and v absent at
z=1. Then b3 <= 3*v(2) (`b3_le_three_mul_channel`):

    v(2) >= 0.47540672 MeV/pair  (21.37% of w(1))   isospin avg
    v(2) >= 0.60269920 MeV/pair  (27.09% of w(1))   Coulomb-corrected

**Not a perturbative correction on a background that nearly works.** The deficit
is an ABSENCE at z=1, not a suppression of something the background supplies.

### THE TARGET IS KNOWN TO ~21%, AND THAT IS A PROPERTY OF THE TARGET

Of four fingerprint coordinates exactly ONE is convention-independent, and it is
the one that never touches A=3 -- where the deficit lives:

    b3/b2             0.641122822 vs 0.812786601   26.775%
    b4/b2             4.15514025  vs 3.46848514    19.797%
    deficit fraction  0.176078329 vs 0.213173903   21.068%
    f(4)=B(4)/B(2)    12.7196315  vs 12.7196315     0.0%

So no derivation of the deficit can be VALIDATED better than ~21% until the A=3
convention is settled. A single-number near-match is uninformative BY
CONSTRUCTION.

This strengthens #6197's refusal of h = 0.2090603 rather than repeating it.
#6197 argued from CANDIDATE DENSITY (3 of 8 small parameters land in the band) --
an argument about the candidates, answerable by finding a sparser family. The
argument here is about the TARGET: the band exists because the quantity is only
defined to 21%, so NO candidate can be discriminated against it, however sparse.

**NAMED NEXT STEP, and it is cheap.** Settle the A=3 convention -- a Coulomb
correction on 3He and its own shift on 4He. That narrows the target from ~21% to
the few-percent level, at which a zero-parameter candidate becomes testable. It
is a data-convention question, not a derivation.

### A RETRACTION OF MY OWN, made before anything was built on it

I framed this front mid-session as: H2(q) is commutative for every q
(`TrefoilSurfaceStateSum.commutator_zero`), so a binding channel on the
non-commutative part vanishes identically at A=2, q-independently. **WITHDRAWN.**

The deuteron's mass/binding-frame braid word is the 3A-STRAND word
(`mass_at_3A_proper.atom_braid_word_3A(1,1)`), so A=2 sits in H6(q), which is
NON-abelian -- `docs/audits/2026-08-21-deuteron-two-adjudications-reconciled.md`
and `deuteron_frame_arity_reconciliation.py`, whose finding 3 records that frame
1 does not descend to the coordination frame. H2 commutativity is a KNOT-LEVEL
fact about the 2-strand trefoil, and the 2026-08-02 audit that states it says so,
naming "the non-abelian H6 interface braid" as where a deuteron commutator charge
would live.

Same failure mode as the SU(4) Casimir lead (two-body object for a three-body
role) and the Milnor mu-bar lead (normalised invariant asked to carry a
magnitude): **right structure, wrong type.** Caught by corpus-grep path 3.

### STILL OPEN
The magnitude. Nothing here proposes a mechanism and the constraint list above
stands unchanged. What changed is that the front is not closed by the ruling, the
turnover is pinned from both sides, the missing channel has a proved lower bound
equal to the whole deficit, and the target's own 21% width is now measured.


## CONSOLIDATION 2026-08-30 — three fronts returned, all negative, and together they close the loop on WHY

The arc question is "derive the missing magnitude in closed form". Three
independent fronts ran in parallel on the three places the magnitude could
have come from. All three returned a measured negative, and the three
negatives are *not* three failures of the same attempt — they are three
different routes each blocked by the same missing object.

### Front A — the braid does not supply the multiplicity (PR #6313, qou-x3y4)

`bk-coordination-multiplicity` reads the coordination degree `z = A-1` as a
topological reading of the canonical link `B_K`. Measured: the braid's
inter-nucleon crossing set is the PATH graph `P_A` (bonds {(k,k+1)},
degrees [1,2,...,2,1]). Its `A-1` is an EDGE COUNT; the block's `A-1` is a
VERTEX DEGREE. Handshake `A*z = 2|E|` with both values forces `A <= 2`, so
the identification is IMPOSSIBLE for every `A >= 3` — the eight rows where
it was measured. Sorry-free: QOU/MassTheory/BraidPathNotCoordination.lean
(11 decls, axiom-clean).

Sharpest finding: `bk_crossing_coordination.py:106` is
`def z_coord(A): return A - 1` — a Python literal in `A` alone. `B_K` never
enters it; `z` is identical for 3H (8_11) and 3He (L6a4). Nothing derives
`z` from anything. Three distinct quantities in this corpus are spelled
`A-1`; the six matching rows could never have separated them, because both
are the SAME AFFINE FUNCTION OF A.

### Front B — the closed-shell factor is derived, but the identification is not (PR #6315, qou-22vu/qou-sh62)

Corrects this corpus in the other direction. The block says the
`M_need/z ~ 2.52` factor "is likewise an AME read rather than a derived
Schur-Weyl period". HALF BACKWARDS: `a_D(n) = lw(n-1) = SUM_{lam|-n}
dim_q(lam)/n` at theta_wn_kernel_derive_or_refute.py:86 is computed with NO
AME input at all. Measured `a_D^(4) = 2.5327796563993915` (q=1 limit exactly
5/2) against the AME read `M_need/z = 2.5188914618`.

So the number IS derived and the IDENTIFICATION is what fails: the a-priori
law `z*a_D^(A)` gives 3H +33.49%, 3He +29.73%, 4He +0.5514% (28.4517 vs
28.2957 MeV). Genericity: 7 of 3996 pre-registered candidates land inside
the +-0.551% window and ALL SEVEN are closer than `a_D^(4)` — `q0^5*(3/2) =
2.52734` at 0.336%. A 0.55% hit on one nucleus, with 7 rivals beating it, is
not evidence. Scope-(b) Lean: QOU/Mass/WignerSU4RowBoundInactive.lean —
the SU(4) row bound is INACTIVE for all n <= 4 and first bites at n = 5.

### Front C — the jet filtration has zero out-of-sample support (this branch, a68eb17fba)

`B(K) = SUM_n m_e * a_D^(n) * w_n` runs on THREE points (2H, 3H/3He, 4He),
all three of which were used to set it, and stops at `A = 4` for want of
`Vol_A`. Nothing in the corpus evaluates it anywhere it was not fitted. My
own earlier claim on this front was RETRACTED in 8da6755e8c: I asserted
`mu_n = a_D^(n) * w_n` conditionally on `M_n(A) = C(A,n)`, and the block
states `M_n(A) = z = A-1`. The antecedent is false.

### What the three have in common — it is DATA, not MECHANISM

Every route needs a nucleus->link assignment past `A = 4`, and there isn't
one:

- Front A can test any candidate bond set but has no link to read it off.
- Front B's `a_D^(n)` is defined for all n; the comparison target
  `M_need(A)` needs `Vol_A`.
- Front C's sum stops exactly where `Vol_A` stops.

Independently established this session: the AME light-nucleus cumulant
tower is convention-limited to under 1 significant digit everywhere
(b4/b3 = 0.030 digits); the N=Z chain is convention-free (~8 digits) but
its leading content is an algebraic rewrite of B/A; every braid/Seifert
invariant is affine in A (scope-(b)).

### The one thing that would change it

EXTEND THE NUCLEUS->KNOT/LINK ASSIGNMENT PAST A=4 (16O in particular). That
is a construction task, not a search, and it unblocks all three routes at
once. Front B reached the same conclusion independently and from the other
side: "extending Vol_A to 16O, or deriving the multiplicity from the
jet-filtration SUM rather than its collapse".

Until then the honest statement is: the magnitude is not derived, and with
the present data it is not DECIDABLE either — any candidate that lands
within 0.55% on one nucleus has at least seven rivals doing better.


## 2026-09-03 — ANSWERED (structurally): `b₃ = 0` is the TRACE's doing, not the assembly's

**The replacement is not another assembly.** Every ingredient was already on
`main`; what was missing was the composition.

`PairwiseCumulantVanishing` scopes itself honestly — its premises *"constrain `f`
on **disjoint** clusters, and the observable that fails is a **connected**
quantity"* — leaving open the hope that the **bound** atom's trace carries
irreducible many-body content. It does not, because of **`qou-g8i1`** (completed):

    tr(x·(σ_g + d·I)) = (z+d)·tr(x)   ⇒   tr_free/tr_atom = ∏_b 1/(z + d_b)

on 16 nuclei numerically (A = 2..10, to `4.45e-31`) and 6 symbolically, with the
recorded mechanism *"the Markov property applied at a **GAP**, not at the last
strand"* — **interior** generators, so the **bound** atom word, not the disjoint
sector M3 covers (`probe_inter_knot_decoupling.py` is the M3 case).

    bond rule → trace ratio = ∏_bonds μ_b        [bound atom, interior gaps]
  + f multiplicative→additive                    [§10a Cauchy]
  ⇒ binding is a bond functional
  ⇒ b₃ = b₄ = 0 identically                      [PairwiseCumulantVanishing]
  vs AME b₃ = +1.426222 MeV.

**So the replacement must BREAK THE BOND RULE** — a trace that is not Markov, or
an object that is not a trace of the atom word. Not a different `f` (`f` does not
appear in the conclusion), and **not a different edge set** (measured: chain,
all-pairs and star all give `b₃ = 0`).

**Two things this makes cheaper.** §10a's uniqueness step (continuous Cauchy
solutions are `c·log`), which `binding_functional_extensivity_probe.py` records
as *classical and NOT in Lean*, is **irrelevant** rather than merely
unformalised — the conclusion holds for a discontinuous `f` too (measured). And
the hypothesis is carried as `SatisfiesBondRule`, a named hypothesis, not an
axiom: what is proved is the **implication**.

**Scope (b)** on bindings `f ∘ (bond-rule trace of the atom word)`, invariant
named: the bond rule makes the cluster trace a product over **pairs**, so the
connected part above order two has nothing to be built from. **(a)** on
everything else — non-trace carriers are untouched, and if the bond rule fails at
some `A` the exclusion lapses there.

**Artifacts.** `QOU/Mass/MarkovBondRuleForcesPairwise.lean` — 4 theorems,
`lean`-direct exit 0, sorry-free, `#print axioms` gives **`[propext]` alone**.
`computations/probes/markov_bond_rule_forces_pairwise_probe.py` — 5/5, exact
`Fraction` for the cumulants, mpmath 50 dps for the logs, zero float64,
P30-stamped.

**Credit where it is due:** the two halves are `qou-g8i1`'s and
`PairwiseCumulantVanishing`'s. This tranche is the join and the identification of
the invariant, not a new exclusion.


## 2026-09-03 (cont.) — the positive half, narrowed to a search over WORDS

Checked the obvious candidate for a non-Markov carrier and it is already worked,
with a measured verdict — plus one apparent tension that turns out to be a
category difference worth recording.

**No contradiction with the bond rule.** `qou-v7ro` proves the **Brunnian trace
deficit** `D_A = 1 − qtr(ρ(w_A))/[2]^A` is **nonzero ∀A** (#6217:
`D_{A+1} = −h²(h²+2)·D_A`, `D_3 = 1.44e-3`). Beside a bond rule verified to
`4.45e-31` that reads like a factorisation failure. It is not — **different
words**: the bond rule governs the nucleon **atom word** (a product of bond
letters `σ_g + d·I` at interior gaps), while `w_A` is the **iterated commutator**
`w_n = [w_{n−1}, b]`, and a commutator is not a product of independent bond
letters. So `SatisfiesBondRule` is not falsified for the atom word and the
exclusion is not vacuous there.

**`D_A` is the one known member of the class my exclusion leaves open.** A
carrier must *break* the bond rule; a word with nonzero deficit is exactly such a
word. So the aim is right — and `qou-v7ro` has already measured why this member
does not finish: `|D_A|` **falls** geometrically (`1.44e-3 → 8.2e-9` over A=3..8,
factor `−0.0893226497` per step) while the empirical binding fraction **rises**
(`0.767 → 0.954·ℏ_q²`, ⁴He → ⁵⁶Fe). Opposite trends ⇒ order/parity marker, not
magnitude. **Scope (a)** on that carrier, not on the class.

**So the positive half is now a stated search: is there a non-factorising word
whose deficit RISES with `A`?** Not a search over functionals `f` (`f` does not
appear in the conclusion) and not over edge sets (measured: chain, all-pairs,
star all give `b₃ = 0`). That is a narrower question than the bean opened with.

**Judgement, not a finding:** the falling/rising mismatch is a *trend* mismatch,
and trends are cheap to test — any candidate word can be screened by computing
its deficit at A = 3..6 before any Lean is written. That screen is the next
concrete step and it is cheap.

Recorded as a scope note in the header of
`QOU/Mass/MarkovBondRuleForcesPairwise.lean`, so a reader arriving from
`qou-v7ro` does not read that file as contradicted.


## 2026-09-03 — the positive half is WALLED, and my own "search over words" was the wrong shape

**Retracting my own stated next step**, before spending a tranche on it. Last
entry I wrote that the open half is *"a search over words: is there a
non-factorising word whose deficit rises with `A`?"* That search **cannot close
the gap whatever it returns**, and the reason is already proved.

`qou-1xne` / [`2026-08-29-w3-closeability.md`](../docs/audits/2026-08-29-w3-closeability.md):
**`w_3` is a required boundary condition of a rank-2 problem, and the corpus
supplies exactly one boundary condition** (n=2, the deuteron bond). Every attempt
to derive it fails on **counting**, not precision — so no amount of further
carrier data helps. Four routes examined:

| route | verdict |
|---|---|
| R1 the period `a_D^(3)` | **determined** — and a *different object* from `w_3`; the gap is the weight, not the period |
| R2 the SL₂ depth-2 recurrence | **circular** (consumes `a_D^(3)`), refuted past n=5 |
| **R3 a third anchor at A > 3** | **none exists under any reading of the tower** |
| R4 the magic form as the n=4 term | determines `w_3` — **negative**, predicting unbound tritium |

Plus a sorry-free scope-(b) exclusion:
`QOU.Mass.BindingScalarKernelParityExclusion.no_scalar_kernel_on_carrier` — the
q-Borel-normalised carrier is pure isoclinic of Newton slope `1/2`, every rank-1
q-difference module has integer slope, so **no scalar `R(q,x)` acts on the
carrier at any depth**.

**Why this kills the word search specifically.** A word with a rising deficit
would be *another candidate weight*, not an anchor. R3 says the tower supplies no
second boundary condition, so a rank-2 recursion stays underdetermined however
many carriers are screened. Producing one and wiring it would be a **fit**, which
the Δ_λ gate forbids.

**How this composes with the bond-rule result above.** They are two halves of one
wall, and neither alone says it:
- `MarkovBondRuleForcesPairwise`: the carrier **must break the bond rule** — no
  function of the atom-word trace can work.
- `qou-1xne`: even a bond-rule-breaking carrier **does not supply the missing
  boundary condition**.

So the open problem is not *"find a carrier"*. It is *"find a second boundary
condition"*, and it must come from **outside** the tower — which is the same
thing as deriving `w_3`, i.e. the gate itself.

**HONEST STATUS: walled.** Not refuted — scope **(a)** on everything except the
two cited Lean invariants. Nothing here says a second boundary condition cannot
exist; it says the corpus has none and that the tower does not contain one, so
the next real move is an ingredient from outside it, not another search inside.

**Judgement, marked as such:** I would leave this walled rather than open a
carrier-screening tranche. The counting argument makes such a tranche unable to
close by construction, and its most likely output is a plausible-looking weight
that would then need labelling as a fit.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress Update (Round 67 — PR #8279)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8279`](https://github.com/litlfred/qou/pull/8279) (branch `feat/round67-diproton-coordination-markov-cut-parity-43c1`, Commit 1 `cfebb01621939a34b7b6881f7cb1f8c1de011515`, Commit 2 / Head `6ad7f37ff2f830c6b6b24c3e111bd408c518e8e6`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/Mass/CoordinationWeightDifferences.lean (`bind_three_and_four_ursell_reconstruct`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/diproton_coordination_markov_cut_parity_probe.py` (`scriptHash: 54f10b23e4d2`) + `test/results/witnesses/diproton-coordination-markov-cut-parity.witness.json` (`allPassed: true`).
