---
# qou-edt7
title: 'GAP: what replaces the multiplicative assembly W=1-PROD f — both corpus assemblies miss the 3-body sign, in OPPOSITE directions'
status: todo
type: task
priority: normal
created_at: 2026-08-30T03:16:24Z
updated_at: 2026-08-30T12:43:32Z
parent: qou-mhj9
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
