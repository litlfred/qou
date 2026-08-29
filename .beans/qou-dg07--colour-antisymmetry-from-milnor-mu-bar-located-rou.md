---
# qou-dg07
title: 'Colour antisymmetry from Milnor mu-bar: located route for eightfold items 4 and 7, gap is one identification'
status: todo
type: task
priority: normal
created_at: 2026-08-29T10:11:14Z
updated_at: 2026-08-29T10:22:06Z
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
