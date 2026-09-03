---
# qou-dg07
title: 'Colour antisymmetry from Milnor mu-bar: located route for eightfold items 4 and 7, gap is one identification'
status: completed
type: task
priority: normal
created_at: 2026-08-29T10:11:14Z
updated_at: 2026-09-03T20:38:20Z
---

## Summary

Audit: `docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md`

The 2026-08-26 discriminator search settled the negative (no object-level gate
separates colour from flavour) and located the discriminator in the Young
channel, naming its own circularity: assigning colour the antisymmetric channel
is an INPUT. It said deriving that input "would supply the one input item 4 is
missing".

This is a candidate route to that input, assembled from things already in the
corpus plus one cited standard fact:

  corpus  the three B_3 components ARE the colours (r,g,b)   borromean-quark.md
  corpus  S_3 acts by permuting the colour assignment        borromean-quark.md
  corpus  mu-bar_123 = +-1 "encodes confinement"             borromean-quark.md
  corpus  mu-bar_123 is the candidate second invariant       SecondCrossingInvariant.lean
  LIBRARY mu-bar_ijk is TOTALLY ANTISYMMETRIC in its indices library/0110001v3

Total antisymmetry in three indices IS the sign representation of S_3. So the
invariant the corpus says encodes confinement transforms in the sign rep of the
S_3 the corpus says permutes colour -- a topological fact, not a QCD import,
and the right shape for colour sitting in lambda = (1^3).

## The gap, NOT closed

  A  mu-bar_123 transforms in the sign rep of S_3        ESTABLISHED (cited)
  B  the state's COLOUR CHANNEL is lambda = (1^3)        NOT established

A is about an invariant of the link; B is about which Young channel the state
occupies. A -> B needs the premise that the state's colour content is READ OFF
mu-bar. The corpus does not assert that and I did not assume it. Item 7 is NOT
derived here and item 4's missing input is NOT supplied.

Claiming B from A would be exactly the arity-conflation failure the
devils-advocate criterion names: a statement about an invariant read as a
statement about a state.

## Why it is still worth having

Replaces "colour antisymmetry is an input" with "colour antisymmetry follows
from ONE identification" -- a strictly smaller ask, and falsifiable in the
useful direction. If the colour degree of freedom is shown not to be carried by
mu-bar, the route dies cleanly.

Also: mu-bar_123 is already SecondCrossingInvariant.lean's candidate for the
hypercharge programme's missing second invariant. If the identification holds,
one object serves both open problems.

## Next

Settle the identification: is the colour degree of freedom carried by mu-bar, or
is mu-bar merely an invariant that happens to be alternating? That is the whole
remaining question on this route.


## Sharper formulation of the route (same session, before any further work)

The audit states the fact as "mu-bar_123 is antisymmetric, hence transforms in
the sign rep". There is a stronger and more natural way to say it, which makes
the identification in the gap a smaller premise rather than a leap:

**The components of the Borromean baryon are UNORDERED.** Milnor's mu-bar_{ijk}
is defined only after choosing an ordering of the components, and relabelling by
sigma in S_3 multiplies it by sign(sigma). So on the physical link mu-bar is not
a number at all: it is well-defined only up to sign, i.e. it is canonically an
element of a ONE-DIMENSIONAL SPACE ON WHICH S_3 ACTS BY THE SIGN CHARACTER.

Under that reading the corpus's own "mu-bar_123 = +-1" is not a convention to be
fixed but the statement that the value lives in the sign line. There is no
preferred ordering of (r, g, b) to fix it with -- the colour tubes are
interchangeable, which is the corpus's own ingredient 2.

So the framework's confinement invariant does not merely HAPPEN to be
alternating; it has nowhere else to live. That is the difference between "an
invariant that is antisymmetric" and "an invariant valued in the sign
representation", and it is the latter that the colour channel lambda = (1^3)
needs.

## What this does and does NOT change about the gap

Still NOT established: that the state's colour content is read off mu-bar. The
premise is unchanged in kind. What changes is its plausibility: the premise is
now "the colour degree of freedom is carried by the canonical confinement
invariant" rather than "the colour degree of freedom happens to share a symmetry
type with some invariant".

## The falsification test to run next, stated so it can be run

The route dies if the colour degree of freedom is a LABEL ON STATES rather than
a property of the link type. mu-bar is an invariant of the LINK TYPE: every
baryon is the same 𝓑_3, so every baryon has the same mu-bar. If colour were a
state label distinguishing baryons, mu-bar could not carry it.

The reason that is NOT obviously fatal, and must be checked rather than waved
through: colour is CONFINED, so all physical baryons ARE the same colour state
(the singlet). "Constant across baryons" is what a confined charge should look
like. So the test is not "does mu-bar distinguish baryons" -- it should not --
but whether the singlet's SIGN BEHAVIOUR under tube exchange is what mu-bar
supplies.

Run that before investing further in the route.


## The falsification test was RUN. Result: the question is now well-posed, and sharper.

I said the next step was to check whether the corpus's colour-state construction
reads the singlet's sign off mu-bar. It does not -- it reads it off an
ASSUMPTION, and that assumption is exactly what mu-bar could supply.

### What the corpus already has

`prop:baryon-product-from-alt` (predicted-spectra, Lean sibling
baryon-product-from-alt.lean):

- S_3 acts on the THREE COLOUR SHEETS by permutation
- Wedderburn: R[S_3] = trivial (+) sign (+) standard
- lambda_baryon(z) := prod_k dc_k/dz IS THE PROJECTION ONTO THE Alt^3 (SIGN)
  ISOTYPE
- and then, verbatim: "The quark-color content of the baryon SELECTS the Alt
  isotype. This selection fixes the integrand up to a scalar."

SELECTS. The Alt choice is an input there, which is item 7's complaint appearing
in a second place.

### The two S_3's are the same one -- checked, not assumed

This was the conflation risk and it is the thing I checked before writing
anything down:

  color-tube-cubic.md      roots are the colour tube coordinate
                           c in {r_z, g_z, b_z}
  bring-trefoil-...md      "the colour-tube cubic's three sheets (r,g,b)"
  photon-channel-...md     "Its three roots are the three quark color charges"
  borromean-quark.md       unknots nu_r, nu_g, nu_b localize IN the red, green,
                           blue colour tubes

Same three tubes, same labels (r,g,b). The cubic's roots are the tubes'
coordinates; the Borromean components are the unknots threaded through those
same tubes. So the S_3 permuting sheets and the S_3 permuting link components
are one group acting on one set of three objects.

### Where that leaves it

TWO one-dimensional sign-isotype objects for the SAME S_3 on (r,g,b):

  lambda_baryon = prod dc_k/dz    Alt^3 projection   ASSUMED to be selected
  mu-bar_123                      sign line          PROVED antisymmetric

### The remaining question, now well-posed

They are not the same object -- lambda_baryon is built from SHEET VELOCITIES
(base/geometric), mu-bar from LINKING of the threaded unknots (fibre). So this
is still an identification, not a theorem. But the question has changed from the
vague

  "is colour carried by mu-bar?"

to the sharp

  "does the Alt selection that prop:baryon-product-from-alt STATES AS AN INPUT
   follow from mu-bar's PROVED antisymmetry, or are these two independent facts
   that happen to agree because both are sign-isotypes of the same S_3?"

That is answerable, and answering it either derives item 7's input or kills the
route. Both outcomes are worth having.

### Honesty note

A one-dimensional sign isotype is UNIQUE up to scalar, so any two sign-valued
objects for the same S_3 are proportional. That is nearly trivial and is NOT by
itself the derivation -- it does not say the physics of one is the physics of
the other. Do not let the uniqueness be mistaken for the identification; it is
the reason the two agree, not evidence that one causes the other.


## The bridge is MONODROMY, and the corpus already computed it

The remaining question was whether the Alt selection follows from something or is
an independent input. It follows -- from the geometry of the colour-tube cubic,
which the corpus has already computed.

`bring-fibre-q0-figure.md`, backed by `bring-chiral-fibre-figure.witness.json`:

- the discriminant Delta(z) vanishes at EXACTLY SIX points, and the witness
  carries all six with discriminant_residual ~ 1e-15, all DISTINCT
- "As z circles z_c at radius 0.15, EXACTLY TWO OF THE THREE SHEETS MERGE. This
  is the B_3-monodromy fingerprint. The third sheet remains well-separated."

A simple zero of a cubic's discriminant (two roots colliding, third distinct)
has TRANSPOSITION monodromy -- an ODD permutation. So the monodromy
representation

    pi_1(P^1 minus Delta)  ->  B_3  ->  S_3

hits transpositions, and composing with sgn gives a NON-TRIVIAL +-1 character.
The Vandermonde sqrt(Delta) = prod_{i<j}(c_i - c_j) is precisely the object
carrying it: double-valued around each simple zero.

### What that buys

The sign character on the three colour sheets is NOT a choice. It is the
monodromy of the colour-tube cubic around its own discriminant. So
`prop:baryon-product-from-alt`'s "the quark-color content SELECTS the Alt
isotype" can be replaced by a derivation: the geometry forces a non-trivial sign
character, and Alt is where it lives.

And it explains the agreement with mu-bar without appeal to the
one-dimensionality triviality I flagged earlier: both the base-side Vandermonde
and the fibre-side Milnor invariant are pullbacks of the SAME sign character of
the SAME monodromy group. The corpus even names it B_3 on both sides -- B_3
monodromy of the cubic, and the Borromean link as a pure braid in B_3.

### Status of each link in the chain

  six distinct discriminant zeros          COMPUTED (witness, residuals 1e-15)
  two sheets merge at the chosen zero      STATED in the .md + figure
  simple branch point => transposition     STANDARD (not machine-checked here)
  transposition => sgn non-trivial         TRIVIAL once the above holds
  sqrt(Delta) carries that character       STANDARD

The one link that is stated rather than computed is the second. It is not in
doubt mathematically -- the six zeros are distinct, and the block says the third
sheet stays well-separated -- but it is prose plus a figure, not a witness field.
A monodromy-permutation field in that witness would close it.

## A SEPARATE question about lambda_baryon, raised NOT asserted

Checking the above surfaced something I could not resolve and am not calling a
defect.

`prop:baryon-product-from-alt` writes

    lambda_baryon(z) := prod_{k=1}^{3} dc_k/dz

and says it "is the projection onto the Alt^3 (sign) isotype".

A product over ALL THREE roots is a SYMMETRIC function of them: permuting the
c_k permutes the factors and a product is invariant under that. Under monodromy
c_1 <-> c_2, the product is unchanged. Read literally, lambda_baryon is
monodromy-INVARIANT, i.e. trivial isotype, not sign.

The likely reading is that `prod` denotes the WEDGE in the tensor module the
block names (bigotimes_k T_{c_k} C), i.e. dc_1 ^ dc_2 ^ dc_3 / (dz)^3, which IS
antisymmetric and IS the Alt projection. That reading is consistent with
everything else in the block.

So this is probably notation (prod written for wedge) rather than mathematics.
Flagging it because the two differ by exactly the sign that this whole route is
about, and because a reader checking the Alt claim against the literal formula
will hit the same wall I did. Worth one clarifying word in the block.


## Update — the Bring side gives the sign rep, computed (2026-08-29)

`computations/probes/bring_cubic_monodromy_probe.py` + witness. The
monodromy of the Bring chiral cubic is the **full S₃**, so its sgn
character is non-trivial. Two independent exact routes over ℚ[z] (no
float): (i) irreducible over ℂ(z) ⇒ transitive, plus depressed p coprime
to Δ ⇒ every local monodromy is a transposition ⇒ S₃; (ii) Δ squarefree
of degree 6 ⇒ not a square in ℂ(z) ⇒ ℂ(z)(√Δ) genuine. Cross-checked at
50 dps: six loops from a common base point, all transpositions,
generating S₃; worst step/separation guard 0.028 over 21600 steps.

**Why it matters:** Λ³ of the 3-dim colour permutation rep is a line
carrying det = sgn. Under A₃ that line would be *trivial* and selecting
Alt would carry no information. S₃ makes Alt a genuinely non-trivial
place for the state to sit. That is the derivable half of
prop:baryon-product-from-alt.

**Correction to my own framing.** The probe names as a gap 'that the
three sheets ARE the three colour tubes'. `rem:brings-qou-4tuple`
already supplies that identification — x₂,x₃,x₄ are the colour DOF, 'the
S₃ permutation of the three sheets' yields the SO(3) holonomy, the fibre
is 'the color ℙ¹ parametrised by the three roots of the elliptic cubic',
the six branch points are 'where color sheets merge'. It is a *remark*
interpreting a definition, so supplied-not-derived, but it is the
corpus's own construction rather than a premise I added.

**Still open (statement B):** that the physical state occupies Alt³
rather than the trivial or standard isotype. §6 supplies the line, not
the state's place in it.

**Two questions raised, not answered:**
1. Are the Milnor sign line (Borromean side) and the monodromy sign line
   (Bring side) the SAME line? Same route twice, or two colour S₃s?
2. `rem:brings-qou-4tuple` says 'degree 4' and 'three sheets' two
   sentences apart. A degree-4 covering has no three sheets. Flagged,
   deliberately not resolved.


## A6 — the sheets ARE the colour tubes (2026-08-29, later)

Worked the open §6.4 question. It turned on arithmetic, not more reading.

**§6.3 of my own audit understated the identification.** It cited
`rem:brings-qou-4tuple` (a remark interpreting a definition) and said the
sheets-to-colour link was 'supplied rather than established'.
`prop:color-elliptic` is a PROPOSITION, states the colour elliptic
equation to be exactly the cubic the probe computes, and names
X = (x_2,x_3,x_4) the colour variable.

**The obstacle that dissolved.** `def:color-tube-fibers` defines
(r_z,g_z,b_z) off a different-LOOKING cubic
c^3+(4z+1)c^2+(6z^2+3z+1)c+(4z^3+3z^2+2z+1). A6 checks the claimed
substitution X = c+z instead of quoting it: it reproduces the tube cubic
coefficient by coefficient, and disc_c(tube) = disc_X(chiral) as
POLYNOMIALS in z. A coordinate translation is an isomorphism at every z,
so it is ONE curve — same branch points, same monodromy.

**So the three sheets are (r_z,g_z,b_z)**, the corpus's own colour tubes,
and Lambda^3 of their span is a non-trivial sign line under the full S_3.

**Partial answer to the same-line question.** Both sign lines are the sign
rep of an S_3 on the same three labels, so the corpus carries ONE colour
S_3, not two: the two routes are one route with two derivations of its key
step, NOT independent evidence. Still open: whether the identification is
canonical — whether mu-bar_123 and the Vandermonde sqrt(Delta) are the
same function or two sections of isomorphic lines. Isomorphic is not equal.

**Flagged, not adjudicated (§7.5).** `prop:color-elliptic` says this
monodromy 'recovers the holonomy generators H_1,H_2'; main's fresh
7be95242b9 makes H_1H_2 = (1 3)(2 4), order 2 in a V_4 on FOUR Lagrange
resolvents. S_3 has order 6, 4 does not divide 6, so no V_4 inside; and
(1 3)(2 4) does not fix w_1, so it does not restrict to {w_2,w_3,w_4}.
Different sets, no stated map. Needs rem:holonomy-trefoil's own definition
read before anyone calls it a defect.


## §8 — the H_1,H_2 flag resolved (2026-08-29, later still)

Read rem:holonomy-trefoil's own text. Two findings, both on main, neither
introduced by this branch.

**§8.1 rem:holonomy-trefoil contradicts itself.** It says x|->H_1, y|->H_2
is an ISOMORPHISM pi_1(S^3\\K_{3,2}) ~= <H_1,H_2> and 'the monodromy group
of the branched cover is exactly the trefoil-knot group'; then that H_1H_2
is a double transposition, hence an involution. Exponent sum is a
homomorphism B_3 -> Z, sigma_1 sigma_2 has exponent sum 2, so it has
INFINITE order in B_3 and cannot be an involution. 'on SO(3)' does not
rescue it: through the 2:1 projection (H_1H_2)^4 = 1, still finite. The
claim that cannot survive is 'exactly the trefoil-knot group' — a finite
branched cover has a finite monodromy group. Scope (b), invariant named.

**§8.2 prop:color-elliptic's closing bridge is unsupported as written.**
'Recovers the holonomy generators H_1,H_2': the H's move FOUR spectral
modes, E_z has THREE sheets; the computed monodromy is S_3 and 4 does not
divide 6 so there is no V_4 in it; and H_1H_2 : w |-> (w_3,w_4,w_1,w_2)
does not preserve the colour triple {w_2,w_3,w_4}. Scope (a).

**§8.3 kept separate:** the two blocks' w_k differ in cardinality (w_1..w_4
vs w_0..w_4) and no block identifies them. Only §8.2's third row depends on
that identification; rows one and two do not.

**AUTHOR DECISION, not agent-fixable.** §8.1's repair means choosing which
of the two claims to keep — surjection-not-isomorphism, or drop the
involution. That changes what the block asserts about the trefoil group, so
it is the author's call, not a typo fix. Left unrepaired deliberately.


## RETRACTION: §8.2 is void; §8.1 stands; A7 replaces it (2026-08-29 15:50Z)

main landed 7adab17a3d 'revert to S3 3-cycle — braid-twist-flip V4 was the
wrong def' at 15:44Z. My §8 was filed at 15:23Z, 21 minutes earlier. NO
causal claim — qou-3nva/qou-htv4 were on the same block independently.

**§8.1 STANDS.** The revert did not touch the isomorphism sentences, and the
argument was never about which finite order: exponent sum is a homomorphism
B_3 -> Z, sigma_1 sigma_2 has exponent sum 2 hence infinite order, so no
isomorphism can carry it to a torsion element. Order 2 before, order 3 now —
same contradiction. 'Exactly the trefoil-knot group' is what cannot stand.
Repair: surjection, not isomorphism.

**§8.2 RETRACTED.** All three rows rested on the reverted V_4 text: the
four-mode formula is gone, there is no V_4 to collide with 4 not dividing 6,
and the cited permutation is no longer asserted. §8.3's cardinality caution
goes with it.

**A7 replaces it, positively.** The six computed local monodromies are TWO
distinct transpositions (0 1) and (0 2); composing two distinct ones gives a
3-cycle of order exactly 3 either way. rem:holonomy-trefoil says H_1,H_2 are
holonomies around two DISTINCT branch points with H_1H_2 a 3-cycle in S_3,
(H_1H_2)^3 = id. Each loop here IS such a holonomy — the corrected block is
exactly what this computation produces. The arithmetic obstruction to
prop:color-elliptic's closing sentence is gone: a 3-cycle sits inside the
computed S_3 where a V_4 could not. CONSISTENT, not derived — no map is
exhibited.

**Lesson (§8.4):** §8.1 was stated against an invariant and survived a change
to the quantity a direct argument would have keyed on; §8.2 was stated against
three quoted numbers and died with them. Same block, same hour.


## §7.4 ANSWERED (2026-09-03) — isomorphic, not the same section

PR #6449, branch claude/colour-sign-line-canonical-2026-09-03.

The 2026-08-30 Brunnian isotype-exclusion note (a sibling, Opus 4.8) built
on this bean's §4/§7.4, narrowed statement B to ONE surviving premise, and
identified that premise as §7.4's own question. So the parked item became
load-bearing while nobody was on it.

**Answer: the two sign lines are isomorphic as S_3-representations, and the
identification of their SECTIONS is not canonical.** Separating invariant:
ker(B_3 -> S_3) = P_3, the pure braid group. The monodromy sign character
factors through S_3, hence is constant on pure-braid closures; mu-bar is
not. Exact — permutations + reduced free-group words, no float, no anchor.

  F2  Borromean = closure of (sigma_1 sigma_2^-1)^3, in B_3 (the SAME braid
      group as the colour monodromy), and PURE.
  F3  nontrivial as a braid, via the faithful Artin rep B_3 -> Aut(F_3).
  F4  it and the trivial braid share an S_3 image but their closures are
      separated by mu-bar (+/-1 vs 0, cited).

**CORRECTS MY OWN §7.4.** I wrote 'the two routes are one route with two
derivations of its key step, not independent evidence'. Withdrawn — the
group claim stands, the identification claim was an over-read.

**F5, the arity check, is part of the result not a footnote.** Sign
character is a function of a LOOP, mu-bar of a LINK; the comparison is
legitimate only after pulling both back to B_3. Unconditional there.
NOT established: that THIS fibration's monodromy image realises a
witnessing pair — the local monodromies are recorded as PERMUTATIONS, not
braid lifts. If the image's pure part carried only mu-bar = 0 the two would
agree vacuously.

**Does not touch** statement B or the Brunnian exclusion — they run on the
Milnor side alone — nor B-i.

**Corpus defect flagged, not repaired:** binding-knots-visual-inventory
states 4 braid words and 3 close to the wrong component count (Hopf -> 1
not 2; trefoil -> 2 not 1; Borromean -> 2 not 3). Only figure-eight is
right; Vol = 8G is exactly right. No producer consumes them. The fix needs
a 0- vs 1-indexing convention choice = author call.


## F5 braid half CLOSED (2026-09-03) — image not confined to the S_3 quotient

Second probe on PR #6449: bring_monodromy_braid_lift_probe.py. Lifted the
six local monodromies from S_3 to B_3 by tracking the three colour tubes'
motion in C at 50 dps and reading crossings off the real-order projection.

All six loops are HALF-TWISTS of exponent sum -1 — the theory prediction
for a simple branch point, so a check not a restatement. 6 of 15 pairwise
products land in P_3 and all 6 are NONTRIVIAL as braids (Artin, faithful).
So the monodromy image is not confined to the S_3 quotient.

TWO DEFECTS IN MY OWN FIRST VERSION, caught pre-push:
 1. the docstring promised a consistency guard the code never ran; now
    implemented against independent continuation-tracking (cycle type
    matches on all six — literal equality is NOT expected, the two
    readings label strands differently);
 2. base point was on the real axis, where the cubic has real coefficients
    so two roots are conjugates with IDENTICAL real parts -> the
    real-order projection is degenerate and recorded phantom crossings
    (min gap 0.0). Moved to 2 + i/2; gap now 2.55e-7, guard asserts > 0.
    The first version's words were superseded, not re-run.

STILL OPEN: whether any pure braid in the image has a closure with
mu-bar != 0. A nontrivial pure braid can still have mu-bar = 0, so the
vacuous-agreement escape is NARROWED, not closed. Milnor computation, not
a braid one.

## §10.2 CLOSED (2026-09-03) — the monodromy image is all of B_3

Probe: computations/probes/colour_mu_bar_monodromy_probe.py
Witness: computations/probes/colour-mu-bar-monodromy-probe.witness.json
Audit: docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md §11

The six local monodromies lift to only FOUR distinct braid words, two of
which generate: sigma_1 = g0^-1, sigma_2^-1 = g0^-1 g1 g0 (g0 = sigma_1^-1,
g1 = sigma_1^-1 sigma_2^-1 sigma_1). The image contains both Artin
generators and is a subgroup of B_3, hence EQUALS B_3; its pure part is all
of P_3. So (sigma_1 sigma_2^-1)^3 is in the image — built from the loop
lifts, Brunnian, mu-bar_123 = -1 — against 0 for the identity, also in the
image, both pure hence both sign character +1. F5's vacuous-agreement
escape is CLOSED, on mu-bar itself.

The sampling route says the opposite and is wrong: 6/6 pure pairwise
products have indeterminacy 1; a radius-5 Cayley ball (14,801 words) has
100 Brunnian pure elements, all mu-bar = 0. The Borromean braid needs 12
generator-letters. A negative from a finite sample bounds the sample.

Two self-caught defects (§11.3): mu-bar written as a SUM of its three
cyclic readings (they are EQUAL; Borromean returned -3 vs +-1), then cyclic
agreement enforced unconditionally (it holds only mod the indeterminacy).
Neither reached a witness or doc. Corpus already had the right form in
gap2_he4_borromean_mu_bar.py.

Still open elsewhere in this arc (unchanged): binding-knots-visual-inventory
braid words (3 of 4 close to the wrong component count — needs an indexing
convention choice); rem:holonomy-trefoil 'isomorphism' -> 'surjection';
rem:brings-qou-4tuple 'degree 4'.

## Three author calls resolved (2026-09-03) — all three approved and fixed on #6449

A. binding-knots-visual-inventory braid words: Hopf s0s1 in B3 -> s0^2 in B2;
   trefoil s0s1s0 in B3 -> s0^3 in B2; Borromean s0s1s2s0s1s2 in B4 ->
   (s0 s1^-1)^3 in B3. Figure-eight was already correct. All crossing counts
   PRESERVED (2/3/6), so 3*E_x(q) and Vol = 8G are untouched.
   CORRECTION to my own framing: I twice called this an indexing-convention
   question. It was not — the block is consistently 0-indexed and the words
   were simply wrong. Do not re-park this as a decision.

B. rem:holonomy-trefoil: 'isomorphism' was false and the block refuted itself
   ((H1H2)^3 = id vs (sigma_1 sigma_2)^3 = the full twist generating the
   infinite cyclic centre of B_3). SPLIT rather than word-swapped: the braid
   half ('monodromy group = trefoil-knot group') is now PROVED by this PR's
   image-is-B_3 result and was previously only asserted; the SU(2) half is a
   surjection onto a proper quotient. .ts gains a computation: block pointing
   at colour_mu_bar_monodromy_probe.

C. rem:brings-qou-4tuple: 'degree 4' -> 'degree 3'. It contradicted 'the S_3
   permutation of the three sheets' in the same sentence; Riemann-Hurwitz with
   six simple branch points gives g=1 at d=3 (matching bring_cubic_monodromy
   _probe A5) and g=0 at d=4. chi(S) = -6 is the state bundle, untouched.

Audit §12. Pipeline validate clean ('Valid — 9 issues', none in these blocks),
run in an ISOLATED worktree because the shared folio-assistant clone is 338
behind and holds 62 files of a sibling's uncommitted work.

STILL OPEN: qa-sweep sidecars for the three blocks are stale by source-hash
drift and were NOT refreshed — qa-sweep lives in that same shared clone.
One sweep needed after this lands.

MERGED 2026-09-03 as 0af489b527 (rebase, 11 commits linear on main).

Post-merge: the one known gap is CLOSED. qa-sweep refreshed all three
sidecars in an isolated worktree at merged main against a fresh
folio-assistant clone; all six source_hashes verified by recomputation,
not by trusting the sweep. PR #6535.

Nothing open on this arc.
