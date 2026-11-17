---
# qou-qjhc
title: 'GAP: identify the duality involution on PGL(3,C) reps with the sigma-transport on Ptolemy coordinates'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T08:42:32Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
---

OPENED 2026-09-07 on branch `claude/8-fold-way-qou-derivation-qj9uzv` (PR #6898), as the
honest exit from formalising the Ptolemy variety. `PtolemyTwist.lean` is sorry-free and
EXIT 0; this is what it deliberately does NOT prove.

## THE GAP, precisely

The Sym-squared gate for the 13 nontrivial L6a4 obstruction classes runs on two legs.

- **Absolute leg (derived, and now in Lean).** Duality on representations,
  `rho -> rho^{-T}`, inverts the obstruction cocycle: `c* = c^{-1}`, i.e.
  `[rho*] = -[rho]` in `H^2(Gamma; mu_3)`. Concrete cocycle side:
  `ObstructionClassForcesComplexType.lean` section `CocycleModel`
  (`cocycle_dual`, `cocycle_conj`, `obs_neg_of_inv`). Class side:
  `ObstructionH2.cls_eq_zero_of_cohomologous_neg`.
- **Relative leg (measured, and now in Lean).** Negating the obstruction cocycle acts on
  snappy's Ptolemy equations as `u -> u^2`, the nontrivial automorphism of `mu_3`.
  Measured on L6a4 classes 1/2/3 in
  `computations/ptolemy/ptolemy_duality_galois_check.py`; formalised as
  `PtolemyTwist.isSolution_negSystem` / `isSolution_negSystem_iff` /
  `exists_isSolution_negSystem_iff`.

**What joins them has NOT been established: that the duality involution on
representations equals the sigma-transport on Ptolemy coordinates.** Both legs conclude
"negation of the obstruction class", so the two ends meet AT THE LEVEL OF CLASSES — which
is enough for the gate as argued. But the two MAPS have not been identified, and
`PtolemyTwist.sigmaFixed_isSolution_neg` carries the identification as a hypothesis
(`forall v, sigma (x v) = x v`) rather than deriving it. Its docstring says so; do not
read it as the gate.

## WHY THIS IS NOT MERELY BOOKKEEPING

Without the identification, a self-dual representation is not known to give a
sigma-FIXED Ptolemy point. The argument as it stands routes around this: it works on the
class, where both legs deliver `-c`, and never needs the point-level statement. So the
gap does not weaken the Sym-squared verdict. What it blocks is the stronger, more useful
claim -- that `P^c` and `P^{-c}` are exchanged BY DUALITY rather than merely by SOME
automorphism that happens to negate the class.

## WHAT WOULD CLOSE IT

The Ptolemy coordinate `c_t` of a decorated representation is a determinant of lifted
decoration vectors (GGZ arXiv:1207.6711 sections 8-9, "the natural cocycle of a generic
decoration"). Under `rho -> rho^{-T}` those vectors transform by the inverse transpose,
so the determinants should transform by an explicit rule. Working that rule out and
checking it is the sigma-transport is the concrete task. It needs the decoration
machinery formalised, which `PtolemyTwist.lean` deliberately does not build -- the file
formalises the SHAPE of the equations, not the geometry that produces them.

Cheap intermediate step, worth doing first: check the claim NUMERICALLY on class 1, whose
four points are known exactly in `K = Q[T]/(f)` (see PR #6898 section A). Apply the
duality involution to the recovered representation, recompute its Ptolemy coordinates,
and compare against `sigma` applied to the original coordinates. That is a measurement,
not a proof, but it would say whether the identification is even true before anyone
spends a tranche formalising it.

## SCOPE NOTE

This is scope-(a) in the repo's refutation taxonomy on nothing at all -- it is an OPEN
item, not a negative. Nothing here is refuted; a step is unproved.


---

## UPDATE 2026-09-07 — the cheap measurement RAN, and the variety-level half is CLOSED

The bean proposed, as the cheap first step, checking the identification numerically on
class 1 before anyone formalises it. It ran, exactly rather than numerically, and it
turned out to need no representation at all.

**Two structural facts made it cheap.** `K = Q[T]/(f)`, the class-1 field, is **Galois of
degree 4 over Q** (`f` splits over `K`) and **contains `zeta_3`** (`x^2+x+1` splits over
`K`). So both primitive cube roots of unity are IN the field the point is defined over,
and the crossing can be tested by pure substitution -- hold the equations fixed, vary
which cube root is plugged in.

**Result** (`computations/ptolemy/ptolemy_galois_point_transport.py`, exact, no floats):

```
            u = u_1     u = u_2
  P^c         9/34        0/34
  P^-c        0/34        9/34
```

Perfectly antisymmetric, and the SAME nine equations fail in the mirrored cells -- the
nine carrying a nontrivial power of `u`. The point solves `P^c` at `u_2` (the root the
producer used, which is why its recorded roundtrip is clean) and `P^-c` at `u_1 = u_2^2`.

**What this closes.** The relative leg was an *equation-set* identity: `u -> u^2` maps
`P^c` to `P^-c` as polynomial sets. That does not by itself say a genuine solution
crosses -- it would not, if the point were defined over a field missing `zeta_3`. It is
not, and it does. This is `QOU.Eightfold.Ptolemy.TwistedEq.eval_negTwist` instantiated on
corpus data.

**What this does NOT close -- the bean stays OPEN.** Nothing here involves a
representation. The crossing is a fact about the VARIETY and the Galois action on its
coefficient field. That the duality involution `rho -> rho^{-T}` INDUCES this crossing is
still unestablished, and remains this bean's subject. What has changed is the prior: the
crossing that duality would have to induce is now known to exist, on real data, rather
than merely predicted.

## A BUG WORTH KEEPING, because the guard was blind in the informative direction

The first run of this measurement gave

```
            u = u_1     u = u_2
  P^c         0/34        0/34      <- WRONG
  P^-c        9/34        9/34      <- WRONG
```

and would have been reported as CONTRADICTING the equation-level measurement.

Cause: the coordinate file records the cube root of unity it used under the key `u`,
alongside the 27 Ptolemy coordinates. Substituting the dict wholesale pinned `u` to the
recorded root before the script's own `u_1`/`u_2` was applied, so both columns evaluated
at the same root.

What caught it was not a guard but an IMPOSSIBILITY: `A*u^2 = B` at two distinct cube
roots forces `A = 0`, and `A` is not `0`. A table that cannot be true is a stronger
detector than a table that merely looks surprising.

The guard that was in place asserted no symbol was left UNsubstituted. It passed --
because the bug was OVER-substitution. **A guard against a missing substitution is
structurally blind to an extra one.** Both directions are asserted now. This is the same
detector-blindness class the tranche has hit repeatedly, in a new spelling: the check was
correct about the question it asked and the question was the wrong half.


---

## UPDATE 2026-09-07 (second pass) — the DUALITY INDEX MAP is measured, and it is a partial negative

The bean asked whether duality `rho -> rho^{-T}` induces the sigma-transport.  This pass
does not settle that, but it settles the prerequisite: **what duality does to Ptolemy
coordinates at all.**

### From the primary source

GGZ arXiv:1207.6711 Lemma 8.8 defines the Ptolemy coordinate as a DETERMINANT of
decoration columns:

    c_t = det( {g0}_{t0} u {g1}_{t1} u {g2}_{t2} u {g3}_{t3} ),   sum t_i = n

with `{g}_i` the first `i` columns of `g`.  Duality sends `g -> g^{-T}`, whose columns are
the DUAL BASIS (`w_i^T v_j = delta_ij`), so `{g^{-T}}_k` spans the annihilator of
`span(v_{k+1},...,v_n)`: duality carries the flag to the ANNIHILATOR FLAG.

**It needs a `w0` twist to even be defined.**  `g^{-T}` maps upper-unipotent `N` to
LOWER-unipotent, so `g^{-T}N` is not a coset of `G/N`.  The map is `g -> g^{-T} w0`,
giving `{g}_k -> ({g}_{n-k})^perp` in increasing order.

### Measured (`computations/ptolemy/ptolemy_duality_index_map_probe.py`)

Both assignments computed on generic decorations over Q, intersecting the |ratio| = 1
index pairs across SIX independent decorations.  Ten indices get a unique surviving
partner, the map is an involution, and all ten obey one rule:

    0 -> 0,   1 -> 2,   2 -> 1,   3 -> 3     entrywise

### The negative, which is the useful part

For n = 3 the index shapes are `{3,0,0,0}`, `{2,1,0,0}`, `{1,1,1,0}`.

- `{2,1,0,0}` -- the rule exchanges a 1 and a 2, so `sum t_i = 3` is PRESERVED.  These
  are the ten.
- `{3,0,0,0}` -- vertex points, all equal 1 by GGZ Remark 5.3.  Degenerate; they carry
  no information and are correctly excluded.
- `{1,1,1,0}` -- the rule would give `{2,2,2,0}`, sum 6.  **NOT A VALID PTOLEMY INDEX.**

So **duality is NOT a relabelling of the whole variety**: it is one on the `{2,1,0,0}`
coordinates and provably cannot be on the `{1,1,1,0}` ones.  Anything that identifies
duality with the sigma-transport has to say what happens on the `{1,1,1,0}` coordinates,
where the image is not +- a Ptolemy coordinate.

### A guess of mine that this REFUTES

I had reasoned that the natural candidate `t_i -> n - t_i` fails on arithmetic
(`sum (n - t_i) = 4n - n = 3n`).  That is right as far as it goes, but the measured map
is NOT "t_i -> n - t_i restricted somehow" -- it agrees with it on the interior values
{1,2} and DISAGREES on the boundary values {0,3}, where it is the identity rather than
the swap 0 <-> 3.  Do not describe the result as a complementation.

### Also settled this pass: Gal(K/Q) explicitly

`computations/ptolemy/ptolemy_class1_galois_group.py` computes sigma by reducing to a
QUADRATIC over Q(zeta_3) instead of a quartic over Q (since [K:Q(u)] = 2 and {1,T} is a
Q(u)-basis).  The quartic system did not finish; the quadratic route does, in seconds.
Two automorphisms invert zeta_3, both verified EXACTLY (`f(sigma T) = 0 mod f`):

    sigma_a: T -> -64 T^3/101015625 - T + 760000/1293
    sigma_b: T -> -T^3/625000 + 19 T^2/8000 - 1293 T/512 + 11875/8

Exactly two is the right count: |Gal(K/Q)| = 4 and the subgroup fixing Q(zeta_3) has
index 2.

### A near-vacuous test, recorded so it is not re-run as evidence

Before having sigma I checked the 6 coordinates lying in the quadratic subfield Q(zeta_3)
and found all 6 map to another coordinate under sigma, 0 misses.  **That is not
evidence.**  Those 6 take only TWO distinct values, both non-rational; sigma is the unique
non-trivial involution of that subfield so it cannot fix either, and the only place it can
send them is the other one.  Landing back on a coordinate was forced by pigeonhole.  A
test satisfied identically is not a confirmation.

### Still open

Whether duality INDUCES the sigma-transport.  The index map above is a necessary
ingredient, not the identification.  Next: work out what duality does to the
`{1,1,1,0}` coordinates, since that is where it stops being a relabelling and is
therefore where the content is.


---

## UPDATE 2026-09-07 (third pass) — what duality does on {1,1,1,0}: a NEGATIVE at bidegree (2,2)

The second pass left the question "what does duality produce on the {1,1,1,0}
coordinates, where it is not a relabelling".  Answered, negatively.

### The object

With the `w0` twist, `{g^{-T} w0}_1 = ({g}_2)^perp`, a line, which for n = 3 is spanned by
`v_1 x v_2`.  So

    c*_{1110} = det( a x b, c x d, e x f )

with `(a,b), (c,d), (e,f)` the first two columns of `g0, g1, g2`.  The classical expansion
(verified on 40 random 6-tuples; two other candidate expansions FAIL) is

    det(axb, cxd, exf) = det(a,b,e) det(c,d,f) - det(a,b,f) det(c,d,e)

Two of the four factors ARE Ptolemy coordinates: `det(a,b,e) = c_2010`,
`det(c,d,e) = c_0210`.  The other two use **g2's second column alone**, not an initial
segment.  That is the mechanism, not a defect: `v_2` is not N-invariant
(`v_2 -> v_2 + lambda v_1`), but the two lambda terms cancel in the combination -- so
`c*` is well defined while its factors are not.  This is exactly why `c*_{1110}` has no
partner among the coordinates.

### The result

1. **`c*_{1110}` is NOT a degree-2 polynomial in the `c_t`.**  Rank 149 of 210 monomials,
   121 inconsistent rows.
2. **Nor a RATIO of degree-2 polynomials.**  The homogeneous system `c* A(c) = B(c)` has
   kernel dimension 122, and **every** kernel vector has `A` vanishing identically on
   decorations -- relations among the `c_t` in disguise, not formulas for `c*`.

Producer: `computations/ptolemy/ptolemy_duality_1110_not_rational_probe.py`.

### Validity gate (an earlier version of this was invalid)

A decoration is by **SL(3) cosets**.  The first run sampled arbitrary invertible
matrices; with `det != 1` the `c_t` are not Ptolemy coordinates and the verdict is about
nothing.  Every sample is now normalised to `det = 1`, and the probe **refuses to run**
unless the Ptolemy relation GGZ (5.2) holds on those samples -- measured **0 violations
in 100 checks**.  Note the numbers changed materially once this was fixed (rank
206 -> 149, inconsistent rows 64 -> 121), so the gate was not cosmetic.

### TWO false positives this produced, kept because the failure mode is the point

- "Kernel dimension 122" reads as *a rational form exists*.  It does not.
- "122 - 61 relations = 61 genuine solutions" reads as a count of real formulas.  Also
  wrong: that arithmetic assumed the only spurious family is `(A=0, B a relation)`, and
  missed that `(A a relation, B=0)` is equally spurious.

Both readings are about the **coefficient vector**.  `A(c)` can have nonzero coefficients
and vanish identically on every decoration.  Testing `A` as a **function** on samples:
**0 of 122** basis vectors survive, and 4000 random combinations produce none.  Same
class as the near-vacuous subfield test in the previous pass, and as the
over-substitution bug in `ptolemy_galois_point_transport.py`: a check satisfied by the
representation rather than by the object.

### SCOPE -- read before citing

This is a structural exclusion **at bidegree (2,2)**, by exact linear algebra over `F_p`
with the gate above (an identity with integer coefficients must hold mod p, so failure
mod p refutes it over Q).  It says **nothing about degree 3 or higher**, which is
untested.  Do not cite it as "duality is not rational in the Ptolemy coordinates"
without the bidegree.

### Where this leaves the bean -- still OPEN

The sigma-transport sends each coordinate to its Galois conjugate: coordinate-wise, and
staying in K.  Duality on the {1,1,1,0} coordinates is not even a low-degree rational
function of the coordinates.  Those are different kinds of map, which makes the
identification LESS likely than it looked two passes ago -- but that is a heuristic, not
a refutation, and it must not be recorded as one.  What would settle it: push the fit to
degree 3, or find the intrinsic characterisation of `c*_{1110}` (it is a Plucker-type
bracket in the dual flags) and compare that with sigma directly.


---

## UPDATE 2026-09-07 (fourth pass) — DERIVED, and it CORRECTS the third pass

Owner directive this pass: **NO fitting.**  The third pass ended by proposing "push the
fit to degree 3", which is exactly a hypothesis-class search and is refused.  Derivation
instead -- and the derivation both answers the question and overturns the third pass's
headline.

### The identity

`c*_1110 = det(A, C, E)` with `A = a^b`, `C = c^d`, `E = e^f` read as covectors via
`Lambda^2 V = V*`.  For covectors,

    det(A,C,E) * det(x,y,z) = det( <A,x> <A,y> <A,z> ; <C,...> ; <E,...> ),
    <A,x> = det(a,b,x)

Take `x,y,z` = the FIRST COLUMNS of `g1,g2,g3`.  Every pairing is then a Ptolemy
coordinate, `det(x,y,z) = c_0111`, and two entries vanish for free (`C` annihilates `c`,
`E` annihilates `e`):

    c*_1110 * c_0111 = det [[c_2100, c_2010, c_2001],
                            [0,      c_0210, c_0201],
                            [c_0120, 0,      c_0021]]

**Confirmed 300/300, 0 refutations**, on SL(3) decorations with GGZ (5.2) gated at 0/100.
Producer: `computations/ptolemy/ptolemy_duality_1110_plucker_identity.py`.

Nothing is fitted: the identity is written down from the Plucker pairing and then checked.
No hypothesis class searched, no coefficient solved for, no object chosen for matching.

### 🛑 This CORRECTS the third pass

The third pass's headline was "duality takes the {1,1,1,0} coordinates OUT of the
coordinate ring".  **Retracted -- too strong.**  `c*_1110` IS a rational function of the
Ptolemy coordinates; it is simply of **bidegree (1,3)**.

The third pass's actual measurement stands exactly as scoped: there is no (2,2) form, and
a (2,2) search space **cannot contain a (1,3) relation**.  So the negative was sound and
the headline over-read it.  The failure was the SHAPE OF THE SEARCH SPACE, not the
mathematics -- and the fix was a derivation, not a wider search.  That is the reusable
lesson: an exhaustive search at one bidegree is silent about every other, and
"exhaustively searched X and found nothing" must never be reported as "not in the ring".

This is the fourth self-correction in this arc and the second where a NEGATIVE was
over-read (the first being the near-vacuous subfield test read as support).

### Where the bean stands -- still OPEN

Duality is now characterised on BOTH index shapes:

- `{2,1,0,0}` -- a relabelling: entrywise `0->0, 1->2, 2->1, 3->3`.
- `{1,1,1,0}` -- not a relabelling, but rational of bidegree (1,3), formula above.

So duality IS a rational self-map of the Ptolemy variety, explicitly.  What is still not
established is that it is the SAME map as the sigma-transport.  The two are now
comparable in a way they were not before: sigma acts coordinate-wise as a field
automorphism of K, while duality acts by the explicit rational formulas above.  The next
step is a direct comparison on the exact class-1 point -- apply both and see whether they
agree -- which needs no new theory, only the sigma from the second pass and the formulas
from this one.

---

## UPDATE 2026-09-07 (fifth pass) — the direct comparison is INCONCLUSIVE, and that is the finding

With sigma explicit (pass 2) and duality's index map explicit (pass 3/4), the two maps are
directly comparable for the first time.  On {2,1,0,0} coordinates duality is the
relabelling `pi`, so agreement would mean `sigma(x_t) = x_{pi(t)}` up to gauge.

Measured (`computations/ptolemy/ptolemy_duality_vs_sigma_comparison.py`), same for both
sigma:

    c_1002_5, c_2001_5   ratio exactly 1
    c_1002_1, c_2001_1   ratio not a root of unity
    c_1002_3, c_2001_3   ratio not a root of unity
    5 of 11 coordinates had no pi-partner present

**This is not a refutation, and must not be recorded as one.**  A Ptolemy assignment is
defined only up to GAUGE: rescaling the decoration at each vertex sends
`c_t -> (prod_i lambda_{v_i}^{t_i}) c_t`, so ratios vary coordinate by coordinate and need
not be roots of unity.  Ratio 1 on tetrahedron 5 and not on 1 and 3 is exactly what a
non-trivial gauge looks like.

Three further reasons the test cannot decide:

1. the point comes from `eliminate_fixed_ptolemys=True`, which IS ALREADY a gauge choice,
   possibly a different one for `P^c` and `P^-c`;
2. only 6 of 11 `{2,1,0,0}` coordinates have their partner present;
3. the first version compared up to `+-1` -- the SL(2) gauge.  For SL(3) it is `mu_3`.

### The hazard on the other side

With per-vertex gauge freedom, ANY discrepancy can be blamed on gauge, which would make
"duality = sigma-transport" unfalsifiable.  That is not an argument for it.  The
falsifiable form: **is the observed ratio a COBOUNDARY** -- do vertex scalars `lambda`
exist with `ratio(t) = prod lambda_{v_i}^{t_i}`?  Definite yes/no; needs snappy's
vertex-incidence data, not pulled here.

### Bean stays OPEN

Not closed, and specifically not closed as refuted.  Next step is the coboundary test
above, which is a bounded piece of work: pull the vertex incidences from snappy, set up
the multiplicative linear system, solve.

Claimed 2026-09-07 by claude/stalled-agents-em-linking-jilmbv (takeover of the #7094 session, which ended after opening #7092). Child task qou-zmat runs the coboundary test.
## UPDATE 2026-09-07 (sixth pass) — RETRACTED: the coboundary test was NOT blocked at the data

> **RETRACTED 2026-09-13.**  The headline below is false twice over.  The test never
> needed the full assignment — a sibling ran it on the eliminated coordinates by the
> Z-kernel route this very section names (see the 2026-09-11 pass immediately after) —
> and the recorded artifact *can* supply the missing six coordinates anyway.  The error
> was generalising "my route cannot be verified" into "the test cannot be run".  Kept
> because the negative under it is reusable: **0 of the 112 identifications relate two
> coordinates the recorded file already knows**, so nothing propagated along them can be
> cross-checked.

Issue #7092 asks the falsifiable question: is the duality/sigma ratio a COBOUNDARY?
snappy supplies exactly the right object -- `_ptolemy_equations_action_by_decoration_change(3)`
is a **128 x 6** exponent matrix (3 cusps x 2 diagonal entries), so the gauge is
`c_p -> prod_k z_k^{M[p][k]} c_p`, and the test needs **no unknowns at all**: any integer
vector in the LEFT KERNEL of `M` forces `prod_t r_t^{n_t} = 1` whatever the gauge is.

**It cannot be run on the recorded point.**  `L6a4-c1-ptolemy-in-K.json` holds 26
coordinates from `eliminate_fixed_ptolemys=True`.  The {1,1,1,0} duality formula needs 8
coordinates per tetrahedron; measured, **at most 2 of the 8 are present on any
tetrahedron**.

### The reconstruction attempt, and why it is unverifiable

Propagating along snappy's 112 identifications takes 26 known coordinates to 98, leaving
6 unknown, constrained by 27 equations -- apparently determined.  It is not usable:

    identifications relating TWO coordinates I already know:  0

The recorded 26 are exactly **one representative per identification class** -- that is what
the elimination does.  So no propagated value can be cross-checked against the file, and
when the 6-unknown solve returns 0 solutions there is no way to attribute it: untwisted
identifications (snappy returns only `+-1`, while a nontrivial generalized obstruction
class twists by cube roots of unity), a sign-orientation convention, or something else.
An unverifiable reconstruction feeding an inconsistent solve is not evidence.

### Two bugs of my own, both surfaced by the solve returning 0

1. The first propagation **ignored the sign field** -- 8 of the 112 relations carry `-1`.
   With signs honoured all 12 fully-determined equations pass (0 non-zero); the earlier
   "10 non-zero" was contamination from setting the unknowns to 1.
2. **`u` was left in the unknowns list** -- the cube root of unity, which is KNOWN -- so it
   was solved for and substituted at the same time.  6 unknowns, not 7.

Fixing both still leaves the reconstruction unverifiable, so neither bug is the blocker.

### The fix is at the producer

Re-run the exact-point producer with `eliminate_fixed_ptolemys=False` (or record BOTH
forms) so the full assignment is on disk rather than inferred.  Then the coboundary test
is short: ratio vector, integer left-kernel of the 128 x 6 matrix, check
`prod r_t^{n_t} = 1`.  Recorded in
`computations/ptolemy/ptolemy_full_assignment_reconstruction_blocked.py`.

Bean stays OPEN.  Nothing here bears on whether duality equals the sigma-transport; it is
a statement about the recorded artifact.

---


---

## UPDATE 2026-09-11 (sixth pass) — the COBOUNDARY TEST ran (#7092): YES for sigma_b, NO for sigma_a

Probe `computations/ptolemy/ptolemy_duality_sigma_coboundary_test.py` (+ witness alongside),
PR #7183, exact in `K = Q[T]/(f)`, decided by the Z-KERNEL of the gauge exponent lattice
(unimodular column reduction; a Q-basis scaled to integers would only span a finite-index
sublattice and could miss a root-of-unity obstruction).  Inputs re-confirmed against snappy
3.3.2: same triangulation as the corpus point (isosig `ivLAPQccddfghghhoooaaaooo`, the 26
canonical variables match exactly, 34 equations), **6** coordinates eliminated by
`eliminate_fixed_ptolemys` (not 5 — `c_0012_0, c_0012_1, c_0102_1, c_0111_0, c_1002_0,
c_2001_0`), and the same 6 for `P^{-c}`, differing only by `u -> u^2`.

### Set-up that had to be settled first

- **Duality on ALL 16 index shapes with SIGNS, derived not measured.** With the dual
  decoration `g* = (v1 x v2, v1 x v3, v2 x v3)` (det g* = det(g)^2 = 1; this is `g^{-T} J`
  with `J = antidiag(1,-1,1) in SL(3)`), the `{2,1,0,0}` relabelling has sign **+1** on all
  twelve indices (`det(a x b, a x c, X) = det(a,b,c) (a . X)`), and the pass-4 (1,3) formula
  generalises to every `{1,1,1,0}` index: `D_t * x_{s(k)} = det[x_{2 at i, 1 at m}]_{i != j,
  m != k}` for ANY omitted column-vertex `k` (all four `k` agree on the point — an extra
  consistency check).  Verified exactly on 25/25 random SL(3) decorations before touching the
  point.  Different `J`'s differ by a `{+-1}`-valued torus element, i.e. a gauge, so the
  verdict is `J`-independent.
- **D(x) is a genuine `P^{-c}` point**: all 32 per-tetrahedron GGZ (5.2) relations hold, and
  the 128 face identifications hold at `u = u_1` (0 failures) and fail at `u = u_2` (16) —
  the pass-1 class negation, now at the point level and through duality's own formulas.
- **The gauge is the decoration torus, 2 parameters per cusp**, `snappy`'s
  `_ptolemy_equations_action_by_decoration_change` (128 x 6), checked row by row against
  the GGZ action.  The issue's `lambda_v^{t_i}` is the 1-parameter-per-cusp scalar sub-torus.
- **The verdict is gauge-invariant** (kernel products of `sigma(x)/D(x)` unchanged under a
  random exact gauge of `x`; a pure gauge has all 122 kernel products = 1), so treating the
  6 eliminated coordinates "as unknowns" is automatic — no representative matters.

### Result

- **`Gal(K/Q) = Z/2 x Z/2`.**  `sigma_a^2 = sigma_b^2 = 1`; `tau = sigma_a sigma_b` fixes
  `Q(zeta_3)`.  This is load-bearing: `D` is an involution (`g** = g`), so `D(x) ~ sigma(x)`
  forces `sigma^2(x) ~ x`; with `sigma` of order 4 the two verdicts below would contradict
  each other.  They do not.
- **`sigma_a`: NOT a coboundary**, for the torus (91 of 122 kernel relations fail) and for
  the scalars.  Simplest obstruction: `c_0210_0` and `c_0120_0` have IDENTICAL gauge
  exponents (vertices 1 and 2 of tet 0 both lie on cusp 1) yet
  `[sigma_a(x)/D(x)](c_0210_0) / [same](c_0120_0) = -128 T^3/113642578125 - 53507/46548`,
  not a root of unity.  Scope (a): these two explicit maps differ on this point by
  something that is not a gauge.
- **`sigma_b`: COBOUNDARY of the PGL(3) decoration gauge over K.**  All 122 torus kernel
  relations have product exactly 1, so `r = sigma_b(x)/D(x)` is a homomorphism on the row
  lattice `L = {e in Z^6 : sum e = 0 mod 3}` (every row has entry-sum 3 — the centre `mu_3`
  acts trivially).  `L` is the character lattice of `T_SL(3)/mu_3 = T_PGL(3)`, the group
  that actually acts on Ptolemy coordinates, so `r in T_PGL(3)(K)`.  Recorded on a Z-basis:
  `r(3e_0) = 256 T^3/189404296875 + 308/3879`, `r(e_1-e_0) = r(e_3-e_0) = r(e_5-e_0) =
  16315/23274 - 256 T^3/113642578125`, `r(e_2-e_0) = 1`, `r(e_4-e_0) = -256 T^3/113642578125
  - 6959/23274` (columns: `d0,d1` on cusps 0,1,2); all 128 equations re-verified from it.
  The ratio takes 4 distinct values; 48 of 128 coordinates have ratio exactly 1.
- **What `sigma_b` does NOT give: an SL(3) lift over K.**  `L` has index 3 in `Z^6`; a
  diagonal `det = 1` matrix over K needs a cube root of `w = r(3e_0)`, and `Y^3 - w` is
  IRREDUCIBLE over K (exact algebraic-field factorisation).  So an SL(3) decoration change
  exists only over `K(w^{1/3})`.  The class of `w` in `K^x/(K^x)^3 = H^1(K, mu_3)` is
  invariant under K-gauge changes of `x` and under the choice of `J`, so it is a property
  of the pair `(x, sigma_b)`.
- **Scalar ansatz (the issue as literally written): NOT a coboundary for either sigma**
  (first obstruction `c_0021_0` vs `c_0111_0`), with or without the vertex coordinates
  `c_3000 = 1` (which force `lambda_v in mu_3`).

### Where this leaves the bean — still OPEN, and sharper

"The sigma-transport" is not one map: the two automorphisms inverting `zeta_3` differ by
`tau`, and `tau(x)` is not gauge-equivalent to `x`.  On this point duality IS the
`sigma_b`-transport modulo the PGL(3) gauge and is NOT the `sigma_a`-transport modulo any
gauge.  This is a point-level fact about the class-1 point, not an identity of maps on the
variety; it says nothing yet about whether `rho -> rho^{-T}` on REPRESENTATIONS induces
`sigma_b` (the remaining content of this bean), and it selects which sigma that
identification would have to name.  Rule 13a: not closed.

---


---

## UPDATE 2026-09-13 — the falsifiable form is ANSWERED; the bean stays open

**A sibling answered issue #7092** (main \`f7fee734c3\`, session
\`01CwN2Uy1xo99iLdJgrcKYbY\`), on the exact L6a4 class-1 point over
K = Q[T]/(f), by the Z-kernel of the gauge exponent lattice — exactly in K, no
floats, no tolerances, no fitting:

* **sigma_b: IS a PGL(3)-gauge coboundary.** All 122 torus kernel relations have
  product exactly 1, so the ratio is a homomorphism on the row lattice
  L = {sum e = 0 mod 3}, i.e. an element of T_PGL(3)(K) — the group that actually
  acts on Ptolemy coordinates. It does NOT lift to a diagonal SL(3) matrix over K
  (r(3e_0) is not a cube in K, exact).
* **sigma_a: is NOT.** 91 of 122 integer relations have product != 1.
* **The scalar ansatz lambda_v^{t_i} (the issue as written): NOT a coboundary for
  either sigma.**

Gal(K/Q) = Z/2 x Z/2, both sigma involutions — which is what makes the two verdicts
consistent with D being an involution.

**The bean stays open, and the sibling says why in its own scope line:** this is a
*point-level* fact about *this point*, **not an identity of maps on the variety**.
It does not establish that rho -> rho^{-T} on representations induces sigma_b. That
identification — the thing this bean is about — is untouched. Per repo rule 13a this
bean is not closeable while that conjecture is open.

## What this session added (branch \`claude/8-fold-way-qou-derivation-qj9uzv\`)

**The FULL un-eliminated class-1 assignment, recovered exactly in K.** The six
coordinates \`eliminate_fixed_ptolemys\` drops are all **cube roots of unity**:

    c_0012_0 = c_0102_1 = c_0111_0 = c_1002_0 = c_2001_0 = 1
    c_0012_1 = u^2                    (verified exactly: x == u^2, x^3 = 1 in K)

That is **GGZ Remark 5.3 — vertex points take the value 1 — twisted by the
obstruction cocycle.** In the trivial class every fixed coordinate is 1; here the
class is non-trivial and exactly one of the six carries the mu_3 twist. It is the
same mu_3 that \`PtolemyTwist.lean\` formalises as \`zpow3\`, arriving in the one
place the recorded artifact had discarded it.

Verification: 12 equations contain no unknown and vanish *before* anything is solved
(an independent check of the recorded 26); each of the six is pinned by **6 to 10
independent single-unknown equations**, all agreeing exactly in K; all **39/39**
un-eliminated equations vanish; no recovered coordinate is zero.
Producer \`computations/ptolemy/ptolemy_class1_full_assignment.py\`, output
\`computations/ptolemy/L6a4-c1-ptolemy-FULL.json\`.

## THREE ERRORS OF MINE RETRACTED HERE, all with the same symptom

Every one presented as "0 solutions" and each had a different cause:

1. **"the coboundary test is BLOCKED at the DATA"** (my commit \`6c2f3700c8\`) —
   **false twice.** The test never needed the full assignment (the sibling ran it on
   the eliminated coordinates via the kernel route, which my own docstring had
   named), and the artifact *can* supply the full assignment. The error was
   generalising *"my route cannot be verified"* into *"the test cannot be run"*.
   File renamed \`..._superseded.py\` so the filename stops asserting it.
2. **"NO candidate satisfies all equations"** — a solver artifact. sympy's general
   nonlinear \`solve\` on all 39 returned nothing; that is not evidence of no solution.
3. **"the system is LINEAR"** — wrong, and caught by my own assertion before any
   number was produced. Degree 1 in *each* variable is not linear:
   \`c_0012_0 = c_0111_0 * c_1002_0\` is bilinear. The system is **triangular**, which
   is what makes it solvable.

One honest sub-finding survives from (1) and is reusable: **0 of the 112
identifications relate two coordinates the recorded file already knows**, because the
26 are one representative per identification class — so nothing propagated along them
can ever be cross-checked. Prefer a route whose own equations are the check.

## Next, in priority order (agent judgement, not a finding)

1. **Test whether sigma_b is the duality map ON THE VARIETY, not at a point.** The
   full assignment now makes the {1,1,1,0} duality formula evaluable directly (it
   needed 8 coordinates per tetrahedron and had at most 2). This is the bean's
   actual subject and the gap the sibling explicitly left.
2. Re-run the coboundary verdict against the FULL point, as an independent
   confirmation of the sibling's result through different data.

**Bean stays open** — the sixth pass's own scope line is the reason: a point-level fact, not
an identity of maps on the variety.


---

## UPDATE 2026-09-13b — the SL(3)-lift obstruction is a CLASS, and it is NOT the mu_3 twist

Branch `claude/8-fold-way-qou-derivation-qj9uzv`, PR #7273. Attacks the map-level gap
through the SL(3)-lift obstruction the sixth pass recorded.

**Step 1 — it is a well-defined class, not a value at one lattice vector.** The sixth
pass rules out the lift because `w := r(3 e_0)` is not a cube in K. A different `e_0`
gives a different `w`, so as stated that is not a statement about maps. Proved sorry-free
(`QOU/Eightfold/SubgroupExtensionObstruction.lean`): replacing `e_0` by `e_0 * l`
(`l in L`) multiplies the obstruction by `r(l)^n`, so its class in `A/A^n` is independent
of the witness; and an extension forces the obstruction to be an n-th power, so a
non-trivial class forbids EVERY extension — with no hypothesis on `[M : L]`. `#print
axioms` gives `propext` alone on all three declarations.

**Step 2 — what that class IS, measured exactly.** K contains `zeta_3`, so by Kummer
`K^x/(K^x)^3 = H^1(K, mu_3)`: the obstruction is mu_3-cohomological, exactly like the
representation-level class in `H^2(M, dM; Z/3)`. The tempting reading is therefore that
the non-liftability is simply the obstruction twist showing up, hence structurally
expected and no evidence about the map identity. **That reading is EXCLUDED:**

    [u]      non-trivial in K^x/(K^x)^3   -- refuted at p = 31
    [w]      NOT a cube                   -- refuted at p = 31
    [w*u]    NOT a cube                   -- refuted at p = 61
    [w*u^2]  NOT a cube                   -- refuted at p = 31

so `[w]` is **not** in `<[u]>`. The obstruction carries a class in `H^1(K, mu_3)` that is
neither the twist nor trivial — an independent datum any proof of "rho -> rho^{-T}
induces sigma_b" must account for.

Method: reduction mod primes (if `v = y^3` in K then `vbar = ybar^3` in every residue
field, so one prime refutes exactly). The prime choice is the content — `p = 1 mod 3` for
cubes to have index 3, `f` with a root mod p, and **`p != 1 mod 9`**, because an element
of order 3 is a cube in `F_p^x` exactly when `9 | p-1`, so at such a prime `[u]` is
trivial and the three candidates become indistinguishable. Controlled both ways:
`(2+T)^3` must be RECOGNISED (survives all 40 primes) and `(2+T)^3 * u` must be REFUTED
(it is) — a test that can only answer "not a cube" is indistinguishable from a broken
one, and all four verdicts are of that form.

Probe `computations/ptolemy/ptolemy_sl3_lift_obstruction_class.py`.

**A wrong turn of mine, recorded.** The first version gated a Groebner decision behind a
norm test. `N(u) = 1` is a rational cube, so the norm test is inconclusive for `u` by
construction, and the Groebner over Q on a quartic with coefficients up to 2.5e13 did not
finish. Reduction mod primes is the right algorithm and is instantaneous.

**SCOPE — this does NOT refute the map identity, and must not be read as doing so.** The
ratio does lie in the PGL(3) decoration torus, the group that actually acts on Ptolemy
coordinates, so on this point `sigma_b(x)` and `D(x)` are the same point of the variety
modulo decoration. What is measured is a finer SL(3)-level datum, at one point in one
class. **Bean stays open** (rule 13a).

**Next, agent judgement:** identify the class. The honest question is whether `[w]` is the
image of something canonical — a Ptolemy coordinate, the discriminant, a unit of `O_K` —
and that must be *derived*, not searched: picking a generator because it matches `[w]` is
selection against the target and is barred by the NO-FITTING directive.


---

## UPDATE 2026-09-13c — the obstruction class lives in Q(sqrt(-15)), a PROPER subfield of the trace field

Branch `claude/8-fold-way-qou-derivation-qj9uzv`, PR #7273. Locates the class from
update 2026-09-13b. Derived from the Galois data the witness already records — no
candidate matching, per NO-FITTING.

**The three quadratic subfields**, from `s = T + sigma(T)` and its quadratic minimal
polynomial:

    Fix(sigma_a) = Q(sqrt(-15))      Fix(sigma_b) = Q(sqrt(5))
    Fix(tau)     = Q(sqrt(-3)) = Q(zeta_3)        (tau = sigma_a sigma_b)
    => K = Q(sqrt(-3), sqrt(5)), biquadratic

`Fix(tau) = Q(zeta_3)` independently reproduces the witness's own `galois_group`
annotation — a cross-check on both, not a restatement of one.

**sigma_a FIXES w**, so

    w = 4/3 - (4/1875) s   in Q(sqrt(-15)),   8 s^2 - 11875 s + 5000000 = 0

and the degree argument applies there: `[K:F] = 2`, and `y^3 = w` in F makes `[F(y):F]`
divide both 3 and 2, so `y` is in F. Hence **w is a cube in K iff it is a cube in
Q(sqrt(-15))**.

**A negative worth recording.** The recorded trace field of this point is ALL of K
(`span_dimension 4`, `equals_ptolemy_field true`, `L6a4-c1-trace-field.json`). So
`Q(sqrt(-15))` is a **proper** subfield of the trace field — the obstruction does not
live in the trace field, it lives in one quadratic piece of it.

**Class vs element, kept apart** (the arity rule). `sigma(w)/w` being a cube is what
fixes the CLASS, and an element can move by a cube. `sigma_b` and `tau` move the element
and leave the class **unrefuted** over 40 primes — recorded as unrefuted, never proved,
since reduction cannot prove a cube. The `sigma_a` row is flagged **VACUOUS**: it fixes
`w` outright, so its ratio is 1 and "1 is a cube" is an identity, not evidence.

**A premature negative of mine, corrected one commit later.** The first version of this
probe tested membership in `Q(zeta_3)` alone, found it fails, and concluded *"the descent
does not apply"* — scoped to one subfield, stated as though general. The guard stopped the
run correctly; the sentence around it over-generalised. Three subfields exist and w is in
one of them.

Probe `computations/ptolemy/ptolemy_obstruction_class_subfield.py` (renamed from
`..._eisenstein.py`, whose name asserted the wrong subfield).

**Bean stays open.** Nothing here bears on whether `rho -> rho^{-T}` induces `sigma_b` as
a map on the variety.

**Next, agent judgement:** `h(Q(sqrt(-15))) = 2` — counted from the reduced forms
`[(1,1,4), (2,1,2)]`, not quoted — so unique factorisation fails and `[w]` cannot be read
off by factoring; the ideal class group enters. Identifying `[w]` in the cube-class group
of `Q(sqrt(-15))` is the next step, and it must stay derived.


---

## UPDATE 2026-09-13d — the point-level fact is now a VARIETY-level one, and the roast's objection is split

The priority-1 next step of this bean ("test whether `sigma_b` is the duality map ON THE
VARIETY, not at a point") has RUN.  `computations/ptolemy/ptolemy_duality_variety_level_orbit.py`,
report `L6a4-c1-duality-variety-level.json`, exact in K throughout.

### The lever: the orbit IS the variety, and that was not recorded before

Three facts already on main line up, and nobody had joined them:

- the class-1 saturated ideal is zero-dimensional of **degree 4** over Q with `u` carried
  as a VARIABLE, mod p and in characteristic zero, `degrees_agree: true`
  (`L6a4-c1-sweep.json`);
- `f` is **irreducible** of degree 4 and the Ptolemy field equals the trace field with
  `span_dimension 4`, so `x` generates `K` (`L6a4-c1-irreducibility.json`,
  `L6a4-c1-trace-field.json`);
- `Gal(K/Q) = Z/2 x Z/2` is **abelian** (#7092).

MEASURED here (G1/G2): the four conjugates are pairwise DISTINCT and each is a genuine
variety point -- 0/32 GGZ (5.2) failures and 0/128 identification failures, each at its
own cube root (`id`, `tau` at `u2`; `sigma_a`, `sigma_b` at `u1`).  Four distinct points
inside a degree-4 zero-dimensional scheme leaves no room: **the orbit is the whole
variety, and the scheme is reduced.**  This also closes `qou-47nf`'s caveat *"degree 4 is
the mod-p count; over C it may differ"* -- the char-zero run answers it and the two are
now joined.

### The result

    point      sigma_a                sigma_b
    id         NOT (91/122 fail)      coboundary, PGL3 only (0/122 fail)
    sigma_a    NOT (91/122 fail)      coboundary, PGL3 only (0/122 fail)
    sigma_b    NOT (91/122 fail)      coboundary, PGL3 only (0/122 fail)
    tau        NOT (91/122 fail)      coboundary, PGL3 only (0/122 fail)

Both columns constant down the orbit.  Guards: G3 measures that **D IS Galois-equivariant**
-- `D(sigma x) = sigma(D x)` on 128/128 coordinates at all four points, which is the
load-bearing leg and is checked rather than argued; G4 calibrates the identity row against
#7092; G5 is the refutation control (the `sigma_a` column is NO everywhere, so the test
CAN fail).

### The roast's objection, split three ways -- only one is answered

`docs/audits/2026-09-07-takeover-fronts-roast.md:102-116` anticipated this move.  It makes
three points and this result touches ONE:

- **(A) pointwise vs universal closure — ANSWERED.**  The sharp half is where the
  quantifier sits.  A per-point test can only give `for all x, exists sigma`; each point
  could a priori be self-dual up to a DIFFERENT Galois element.  The measurement gives
  `exists sigma, for all x`, with `sigma_b` exhibited and `sigma_a` excluded at every
  point.  That arity upgrade is the whole content.
- **(B) "two distinct rational self-maps can agree on a Galois orbit" — NOT ANSWERED.**
  Four points impose four conditions.  This is an identity of maps ON V, never of rational
  maps, and it carries NO implication for another obstruction class or manifold.
- **(C) whether `rho -> rho^{-T}` INDUCES `sigma_b` — NOT ANSWERED**, and it is still this
  bean's subject.  What sits between is the Ptolemy-to-representation direction: `V`
  modulo gauge corresponds to the class-1 boundary-unipotent PGL(3,C) representations
  (GGZ), and IF that correspondence is a bijection here, agreement on all of `V` modulo
  gauge is agreement of the induced maps on representations.  **The probe does not
  establish that bijection and does not assume it.**

Honest one-line form: **every point of the L6a4 class-1 variety is self-dual up to
Gal(K/Q), by one and the same element `sigma_b`.**  Strictly stronger than #7092's single
point; strictly weaker than "D = sigma_b as maps"; silent on representations.

### A cross-check that cost nothing

`w = r(3 e_0)`, whose cube-root-ness decides the SL(3) lift, transports by Galois
(`w(sigma x) = sigma(w x)`, verified) and takes exactly TWO values across the four points,
constant on the cosets of `{1, sigma_a}`.  That reproduces PR #7273 section 4 -- `sigma_a`
fixes `w`, `w` lies in `Q(sqrt(-15))` -- from the orbit side, which shares no machinery
with the subfield-descent route that found it.

### Lean

`QOU/Eightfold/GaloisOrbitTransport.lean`, sorry-free; three of its four results depend on
**no axioms at all**, the fourth on `propext`.  `eq_smul_of_transitive_orbit` is the
upgrade; `rel_of_transitive_orbit` is its version modulo an action-stable relation, stated
as an **Iff** so it propagates the `sigma_a` NO exactly as it propagates the `sigma_b`
YES; `exists_not_forall_eq_of_not_central` shows **commutativity cannot be dropped** (for
any non-central `b` in any group, right multiplication by `b` is a counterexample).  No
numbers in the Lean.

### A bug the calibration guard caught, worth keeping

The first run read the verdict off `gauge is not None` from `coboundary_test`'s second
return value.  That is a PROXY for a different fact: in the index-3 case the function
returns `None` when `w` has no cube root in `K`, meaning *"the PGL(3) gauge element does
not LIFT to SL(3)"*, NOT *"there is no gauge element"* -- the very distinction PR #7273
exists to draw.  The table printed `NOT a coboundary (0 of 122 kernel relations fail)`,
self-contradictory on its face, and it was the G4 CALIBRATION row that failed, not the
mathematics.  Same class as blindness-taxonomy rows 27-32: a structural proxy substituted
for the structural fact.  The verdict is now read from the integer kernel, which is the
definition.

### Still OPEN (rule 13a)

(B) and (C) above.  The next honest step is (C): establish, or refute, that the Ptolemy
point-to-representation correspondence is injective modulo gauge on this class, which is
what would carry the variety-level identity across to representations.


---

## UPDATE 2026-09-13e — (C) attacked DIRECTLY, on characters: only `sigma_b` survives

Pass 13d left three things open, of which (C) -- whether `rho -> rho^{-T}` INDUCES
`sigma_b` on REPRESENTATIONS -- is this bean's actual subject.  It is now attacked
directly, and the route goes AROUND the Ptolemy-to-representation gap rather than through
it: `computations/ptolemy/ptolemy_duality_is_sigma_on_characters.py` never mentions gauge,
duality formulas or coboundaries.  It compares CHARACTERS.

### The identity

If `rho^{-T} ~ sigma(rho)` as PGL(3) reps then `A sigma(rho(w)) A^-1 = lambda(w) rho(w)^-T`.
Traces give `sigma(chi(w)) = lambda(w) chi(w^-1)`; determinants give
`sigma(det w) = lambda(w)^3 / det(w)`.  Cube the first, substitute the second, `lambda`
cancels:

    sigma( chi(w)^3 / det(w) )  ==  chi(w^-1)^3 / det(w^-1)      for every w.

`I(w) = chi(w)^3/det(w)` is the PGL-invariant: a non-trivial obstruction class says the
rep does NOT lift to SL(3), so each matrix is defined only up to a scalar and `chi` alone
is not an invariant.  Same invariant, same reason, as `exact_character_selfduality.py`.

### Result -- 4686 reduced words, length <= 5, exact in K

    id       REFUTED   3504 witnesses   shortest  ac
    tau      REFUTED   3952 witnesses   shortest  ab
    sigma_a  REFUTED   4068 witnesses   shortest  ab
    sigma_b  HOLDS on every word tested

Only `sigma_b` survives.  `tau` and `id` fix `zeta_3`, so they sit at the wrong obstruction
class; `sigma_a` is refuted here exactly as it is on the Ptolemy side -- **the two levels
agree, which they were not obliged to.**

### Two EXACT calibration matches

The `id` row IS the self-duality test, and it reproduces the corpus to the digit: **94**
witnesses with shortest `ac` at length <= 3 against `L6a4-c1-character-selfduality.json`
(`pgl_witnesses` 94, `shortest_witness.word` `ac`), and **3504** at length <= 5 against
`exact_character_selfduality.py`'s own recorded figure.  It is also the REFUTATION
CONTROL: it proves the test can fail, so `sigma_b` passing is not vacuous.

### Stage 2 -- closing what the cube hides

`I(w)` is a cube, losing one cube root of unity per word.  Computing the intertwiner
scalar directly, `lambda(w) = sigma_b(chi(w))/chi(w^-1)`:

    defined on                        936 of 936 words (no chi(w^-1) vanishes)
    lambda(w)^3 == 1                  936 of 936
    lambda(vw) = lambda(v)lambda(w)  2580 of 2580 concatenations

So `lambda` is a **mu_3-valued HOMOMORPHISM** on everything tested.  This is the step worth
having, because **a mu_3 scalar is TRIVIAL IN PGL(3)** -- twisting `rho^{-T}` by `lambda`
changes nothing there.  With the rep recorded ABSOLUTELY IRREDUCIBLE (Burnside;
`L6a4-c1-irreducibility.json`, `span_rank 9 = full_rank 9`) the argument closes to:

> **IF** the character identity holds for ALL `w`, **THEN** `sigma_b(rho) ~ lambda (x)
> rho^{-T} = rho^{-T}` as PGL(3) representations.

### STILL NOT PROVED, and rule 13a keeps this bean OPEN

**"All w" versus "the 4686 tested."**  A finite sweep cannot give the full character, and
stage 2's multiplicativity is likewise measured on a finite set.  The visible route to
closing it: the image SPANS `M_3(K)` (`matrices_spanned 31`, `span_rank 9`), so a
character is determined by finitely many words -- turning that into a bound on word length
is the remaining work and is NOT done.  Also still one manifold, one obstruction class;
roast point (B) (two distinct rational self-maps can agree on an orbit) is untouched.

### (B) is BLOCKED, not untried

Obstruction class 2 was investigated.  **No exact class-2 point exists in the repo**, and
three recorded solve routes each hit a measured wall -- msolve RUR > 3000 s; GB-only mod p
> 2700 s producing 0 bytes; Singular full system > 5400 s (`qou-0y6l`) -- while the
upstream `ptolemy.unhyperbolic.org` object returns **403** from this container (re-tested).
So class-specificity is untouched.  Useful structural note: the whole blocker is ONE input
file -- `ptolemy_duality_sigma_coboundary_test.py` is already class-parameterised, and the
orbit producer hardcodes class 1 in three places, so adapting is a small edit if
`L6a4-c2-ptolemy-in-K.json` ever lands.

### Next honest step

Bound the word length at which the character is determined, using the spanning fact -- that
is what would turn the corroboration into a proof for class 1.


---

## UPDATE 2026-09-13f — (C) is PROVED for class 1.  The word-length bound is ONE.

Pass 13e ended with the honest gap *"all `w` versus the 4686 tested"* and named the route
to closing it as a word-length bound from the invariant theory of 3x3 matrices
(Procesi/Razmyslov degree `n^2`, Teranishi's sharper 6 for two generic matrices).  **That
route was not taken, because the bound is 1** and a sweep was never the right instrument.

### Why the bound is 1

Set `rho_1(w) = sigma_b(rho(w))` and `rho_2(w) = lambda(w) rho(w)^{-T}`.  **Both are
HOMOMORPHISMS**: transpose-inverse is an anti-anti-automorphism, so
`(rho(v)rho(w))^{-T} = rho(v)^{-T} rho(w)^{-T}`, and `lambda` is multiplicative (measured
in 13e).  So a single `A` with `A rho_1(g) A^{-1} = rho_2(g)` on the three GENERATORS makes
`w -> A rho_1(w) A^{-1}` and `w -> rho_2(w)` two homomorphisms agreeing on a generating
set -- hence **equal on every word**.  Not corroborated: equal.  No characters, no absolute
irreducibility, no trace algebra, no word length.

### The solve, and the result

`A rho_1(g) = lambda(g) rho(g)^{-T} A` is LINEAR in the nine entries of `A`; each
`K`-element is four rationals, so 36 unknowns and 108 rational equations over three
generators, nullspace exact over `Q`
(`computations/ptolemy/ptolemy_duality_sigma_intertwiner.py`).

    id       nullspace dim 0    no intertwiner
    tau      nullspace dim 0    no intertwiner
    sigma_a  nullspace dim 0    no intertwiner
    sigma_b  nullspace dim 4    INVERTIBLE INTERTWINER FOUND

**PROVED, for L6a4 obstruction class 1 over `K`: `sigma_b(rho)` and `rho^{-T}` are
conjugate in `PGL(3,K)`.**  `lambda` is `mu_3`-valued on every generator, and `mu_3`
scalars are TRIVIAL in `PGL(3)`, so the twist is invisible there -- the statement is
exactly *"duality induces the `sigma_b` transport on this representation"*.

### Four checks the solve had to pass

- **Controls at dim 0.**  `id`, `tau`, `sigma_a` admit **no nonzero solution at all** --
  stronger than "no invertible one".  `id` failing is independently required: a solution
  there would mean `rho` is SELF-DUAL, contradicting the recorded COMPLEX TYPE verdict.
- **Schur.**  `dim_Q = 4 = [K:Q]`, i.e. `dim_K = 1`: the intertwiner is unique up to a
  `K`-scalar, exactly as Schur forces for an absolutely irreducible `rho`.  A LARGER
  dimension would have meant the system was under-constrained -- a tripwire, not a remark.
- **Relators 2/2.**  The intertwining holds on both relators, so it descends to `pi_1`
  rather than living only on the free group.
- **Longer words 8/8**, including words with inverse letters.  These MUST hold
  automatically if multiplicativity is applied correctly.

### Lean

`QOU/Eightfold/IntertwinerFromGenerators.lean`, sorry-free, arbitrary groups, no matrices
or fields in it: `eqOn_of_eqOn_generators` (two homomorphisms agreeing on a generating set
are equal), `conjHom`, `conj_eq_of_eqOn_generators` (**the bound is one**), and
`twist_trivial_of_mem` (a twist by a homomorphism into a normal `N` vanishes in `H/N` --
with `N` the scalars, a character twist is invisible projectively).

### What is STILL open -- rule 13a keeps this bean open

- **Other obstruction classes.**  Class 2 is BLOCKED, not untried: no exact point exists in
  the repo and three solve routes have measured walls (`qou-0y6l`), with the upstream
  object 403 from this container.
- **Other manifolds.**  Nothing here generalises; L6a4 only.
- **Duality as a map on a moduli space.**  Roast point (B) -- two distinct rational
  self-maps can agree on a finite set -- is untouched, and the proof above is about ONE
  representation (up to its Galois orbit), not about a map of varieties.

The bean's title asks for the identification in general.  For the L6a4 class-1
representation it is now a theorem; in general it is open.


---

## UPDATE 2026-09-13g — the lambda class question: the twist is ABSENT, not invisible

Pass 13f closed (C) for class 1 and left one question: is `lambda`'s class canonical, or an
artifact of the decoration?  **Measured answer: `lambda == 1` on every generator, hence on
every word.  There is no twist to have a class** — and that is a stronger result, not a
null one.

### The stronger theorem

With `lambda == 1` the intertwining is

    A sigma_b(rho(w)) A^{-1} = rho(w)^{-T}        exactly, no scalar

an equality of **GL(3,K)** representations, not merely the PGL(3,K) statement of 13f.
Re-solved with `lambda` pinned to 1 (nullspace dim 4, invertible `A` found), 9/9 words
including inverse letters.  As characters: `sigma_b(chi(w)) = chi(w^{-1})` **untwisted**,
1554 words of length <= 4, **zero** skipped.

### The triviality is FORCED — this is the actual content

`lambda = 1` could have been luck of the decoration.  It is not.

- The lift is **SL(3)**: `det rho(g) = 1` on all three generators, measured.
- So det of both sides **forces** `lambda(g)^3 = 1`.  mu_3-valued is a consequence of the
  normalisation, never a discovery.
- The only freedom is the lift, `rho -> mu.rho`, under which
  `lambda' = lambda . mu . sigma_b(mu)`.  The law is **measured**, by re-solving the
  intertwiner for rescaled `rho'` against the predicted `lambda'`, with a deliberately
  wrong `lambda'.u` as control — nullspace dim 0 every time, correctly rejected.  Three
  `mu` tested: mu_3, rational, generic.
- An SL(3)-preserving redecoration has `mu` in mu_3, and since `sigma_b(zeta_3) =
  zeta_3^2` the coboundary is `N_b(mu) = mu.sigma_b(mu) = mu.mu^2 = mu^3 = 1`
  **identically**.

So `lambda' = lambda` for **every** admissible `mu`: no decoration could have made the
twist nontrivial.  Untwistedness is a property of the representation.

### Supporting measurements, none assumed

- `Gal(K/Q)` is **Klein four** — full multiplication table; every element an involution, so
  `sigma_b^2 = id`, which is what puts `N_b`'s image in the fixed field `K^sigma_b`.
- `sigma_b(zeta_3) = zeta_3^2` (and `sigma_a` too; `id` and `tau` fix it).  `sigma_b`
  **negating the obstruction class** is why it is the automorphism that works at all, and
  the same fact is what kills the coboundaries.
- `lambda` is trivial on **both relators**, so it descends to `pi_1` and "class in
  `Hom(pi_1, mu_3)`" type-checks — it is the trivial class.

### Correction to my own prior claim

Pass 13f wrote *"lambda is mu_3-valued and mu_3 scalars are TRIVIAL in PGL(3), so the twist
is invisible there"*.  True as stated and **misleading**: it implies a twist exists that
PGL(3) does not see.  Corrected in `ptolemy_duality_sigma_intertwiner.py` (docstring, the
mu_3 check — now reporting `lambda == 1` separately from `lambda^3 == 1` — and the verdict)
and in its report; it also stands in commit `e7211e61b7` (immutable) and in the PR #7290
comment, which a follow-up comment corrects.

**The sharper point: both earlier passes already held the refutation and neither read it.**
13f reported only `lambda(g)^3 == 1`; stage 2's witness records
`stage2_intertwiner_scalar.distinct_values: 1` across 936 words, which with its own
multiplicativity check forces `lambda == 1`.  The data was there; the summary word
"mu_3-valued" was chosen instead.

### Scope, and one thing that must be quoted with it

One manifold, one obstruction class, one representation up to its Galois orbit.  The
rational and generic `mu` rows **do** move `lambda`, correctly — those lifts leave SL(3),
where `lambda` need not be a cube root at all.  **The rigidity claim is scoped to SL(3)
and must be quoted that way.**  Bean stays open under rule 13a: the general identification
in the title is untouched.


---

## UPDATE 2026-09-13h — the orbit survives it; and roast point (B) is NARROWED, not closed

Two fronts, taken together.

### 1. The untwisted GL(3,K) duality is a fact about the CLASS, not the point

The prediction was written into the probe **before** the run, as an argument rather than a
guess: at `x_g = g(x)` the representation is `rho_g = g(rho)`, so `sigma(rho_g) =
(sigma.g)(rho)`; applying `g` to the base intertwining gives
`g(A).(g.sigma_b)(rho).g(A)^{-1} = rho_g^{-T}`. Matching needs `sigma = g sigma_b g^{-1}`,
which is `sigma_b` itself because **`Gal(K/Q)` is Klein four** — measured, not assumed.

Measured, 16 solves with `lambda` **pinned to 1** (so a success is untwisted GL(3,K), not
projective):

    point          id       tau   sigma_a   sigma_b
    x_id      none(0)   none(0)   none(0)  FOUND(4)
    x_tau     none(0)   none(0)   none(0)  FOUND(4)
    x_sigma_a none(0)   none(0)   none(0)  FOUND(4)
    x_sigma_b none(0)   none(0)   none(0)  FOUND(4)

Every control at **dim 0** — no nonzero solution at all. Every `sigma_b` cell at
**dim 4 = [K:Q]**, Schur at each point. And `A_g == g(A)` up to a K-scalar at all four: the
intertwiner is the Galois **transport** of the base one, not merely some matrix per point.

Since the orbit **is** the whole variety, this is the representation-level twin of §1's
variety-level *"exists sigma, for all x"*. It is also a real test of
`GaloisOrbitTransport.lean`, whose sharpness theorem says commutativity cannot be dropped —
had `sigma_b` not been uniform, either that hypothesis fails here or the Klein-four
measurement is wrong. Guards first: relator gate at all four points, and `det rho_g(g) = 1`
at all four, so the SL(3) normalisation is not an artifact of the base point.

### 2. Roast point (B): NARROWED to two hypotheses, one of them newly found

*"Two distinct rational self-maps of a variety can agree on a Galois orbit."* Splitting it:

- **(B1), as functions on the points — closed and TRIVIAL.** The orbit is all of `V(Kbar)`,
  so two functions on a four-element set agreeing at all four are equal. No algebra needed
  and none should be claimed; this reading carries no content.
- **(B2), as scheme / rational maps — the substantive one.** Pointwise agreement upgrades to
  equality exactly when (i) the points **exhaust** the space and (ii) the coordinate ring is
  **reduced**. Both are measured true for this variety in §1.

`QOU/Eightfold/PointwiseAgreementOnReduced.lean` (sorry-free, arbitrary commutative rings)
isolates (ii): `eq_of_sub_mem_all_primes`, `eq_of_apply_sub_mem_all_primes`, and the
sharpness `exists_ne_of_not_isReduced` with the concrete witness `(2 : ZMod 4)` — a nonzero
nilpotent lies in every prime, so without reducedness two genuinely different maps agree at
every point.

**The second gap, which the roast does not name and which I had not either.** Applying that
to `D` versus `sigma_b` needs them to be morphisms **in the same category**, and they are
not obviously so: `sigma_b` is a field automorphism of `K` (semilinear over `K`), while `D`
is a `K`- or `Q`-rational map. *"Equal as rational self-maps"* does not yet type-check for
this pair. So the status is:

> **(B) is NARROWED to two named hypotheses — reducedness + exhaustion, MEASURED TRUE, and
> a common category for the two maps, NOT ESTABLISHED — rather than closed.**

Attacking the objection surfaced an extra hypothesis instead of removing one. Recorded that
way deliberately; the bean stays open under rule 13a.


---

## UPDATE 2026-09-13i — costing the second manifold, and my "same wall" claim RETRACTED

### What I claimed, and why it was wrong

I told the author a second manifold *"needs the exact Ptolemy point that blocked class 2"* —
i.e. that it inherits class 2's walls (msolve RUR >3000 s, GB-only mod p >2700 s, Singular
>5400 s) and the upstream 403. **Wrong.** The class-2 wall is a **variable-count** wall, not
a wall about obstruction classes or exactness. L6a4: 8 tetrahedra, **27** variables after
elimination. `m004`: 2 tetrahedra, **7**. Gröbner cost is super-exponential in that count.

    m004 class 1    7 vars    dim 0, degree  4     0.9 s
    m003 class 1    7 vars    dim 0, degree 18     0.0 s
    5_2  class 1   11 vars    dim 0, degree 10     0.4 s
    L6a4 class 2   27 vars    ---                  >5400 s (known wall)

Nontrivial N=3 classes are **ubiquitous, not scarce** — 19 of 19 small manifolds enumerated
carry one. And `m004` class 1 is **degree 4, the same as L6a4 class 1**, so directly
comparable.

### The real cost: two of three structural conditions are NOT generic

|  | L6a4 c1 | `m004` c1 | `5_2` c1 |
|---|---|---|---|
| ζ₃ ∈ K | yes | yes | yes — generic so far |
| **Gal abelian** | yes (Klein 4) | yes (C₂) | **NO (order 12)** |
| **orbit = variety** | yes (1 orbit of 4) | **NO (2 comps of deg 2)** | — |

`5_2` c1 breaking abelian-ness is `exists_not_forall_eq_of_not_central` biting on a **real
example** rather than in principle; `m004` c1 breaking single-orbit means the "for all x"
upgrade must be redone per component. Both are findings rather than obstacles — a
non-abelian manifold where the per-point intertwiner still exists would show the transport
argument is *sufficient but not necessary*.

### An honest unknown

A naive `std()` over ℚ on **L6a4 class 1 itself** times out, yet the corpus holds its exact
point — so that point did not come from this pipeline's cheapest route and I do not know
what route produced it. Small manifolds are unaffected (elimination demonstrably works:
`m004`'s primitive-element eliminant is `x²+2x+4`, so **K = ℚ(ζ₃)**), but I cannot claim the
L6a4-scale route is reproducible here.

### A misread caught before it reached the report

sympy's `galois_group(f)` returns `(G, alt)` where the second value is *"lies in Aₙ"*, **not
"abelian"**. Reading it as abelian reported `m004`'s C₂ — an abelian group — as non-abelian.
Abelian-ness is `G.is_abelian`.

### Estimate and recommendation

Compute is free; the cost is **porting the probes**, which hardcode L6a4's field and its two
automorphism polynomials, to compute `Gal(K/ℚ)` as explicit substitutions. Roughly a
session, dominated by point-extraction plumbing.

Recommendation (agent judgement): **both, `m004` first** — `m004` gives the reproduction
check cheaply though its C₂ is a weak test of the transport; `5_2` is the sharper test and
is the same ported code with a different input.

Probe: `computations/ptolemy/ptolemy_second_manifold_cost.py`. Bean stays open under rule 13a.

## 2026-09-14 — the 5_2 wall was an algorithm choice, not the container

`5_2` class 1 is EXTRACTED on a 16 GB container. The previous record — mine —
said it needed a bigger machine on the strength of 7.9 GB RSS at 717 s. That
measured the symptom. Stage 2 was asking Singular for a LEX Groebner basis of
(eqs, T-lin, h) in a 12-variable ring over Q, and lex is where rational
coefficients explode; `stdfglm` makes the lex basis cheaper to reach but still
builds it.

Nothing downstream needs a lex basis. Where T is primitive the shape lemma gives
{1, T, ..., T^(d-1)} as a basis of the component ring, so each coordinate comes
from DEGREVLEX normal forms plus one small exact linear solve. Measured: deg-4
component 14.9 s, deg-6 component 17.9 s, Singular RSS 15 MB (sampled).

STRUCTURAL FINDING, and it constrains the arc: `5_2` class 1 has TWO genuine
Galois orbits (degrees 4 and 6), where L6a4 class 1 has one. PR #7290 section 1
upgrades per-point to for-all-x by 'four distinct points in a degree-4
zero-dimensional scheme leaves no room -- the orbit IS the whole variety'. That
argument does NOT transfer to `5_2`: a per-point result upgrades only within one
orbit, and the two orbits must be tested separately.

Also added: coordinates are now back-substituted into the Ptolemy equations mod
h(T) before a point is written. NEITHER route verified its own output before.

Corrected here too: both L6a4 classes are 27 variables / 33 equations. The
earlier note calling class 2 'a variable-count wall (27 vs 7)' was comparing
L6a4 to m004, not class 1 to class 2, so it does not explain why class 1 is
solved and class 2 is not.

Branch claude/ptolemy-lex-free-stage2-2026-09-14; issue #7346. Bean stays OPEN
(rule 13a) -- the general duality identification is still a conjecture.


### 2026-09-14 — `5_2` class 1 answered, on BOTH orbits, and the test finally SELECTS

Three things landed, in dependency order.

**1. The producer was discarding every Galois orbit but the first** (`674c2b6307`).
`ptolemy_exact_point.py` printed *"the variety is NOT a single Galois orbit, so a
per-point result does not upgrade to 'for all x' for free"* and then wrote
`to_point_json(genuine[0])` into one file. Orbit 1 of `5_2` class 1 had no
addressable artifact at all, so the one inference the NOTE forbids was the only one
a consumer could make. Each genuine orbit now gets its own point file plus a
`provenance.orbit_index`; orbit 0 keeps the unsuffixed name, so no committed
artifact moves.

**2. `Aut(K/Q)` was the reason the duality probe could not run on `5_2`**
(`350e00d152`). It solved `f(g(t)) = 0 mod f` for the `deg` coefficients of `g` —
`deg` equations of degree `deg` in `deg` unknowns, a Groebner basis inside
`sp.solve`. Two runs on the degree-4 orbit were killed at 25 and 40 minutes with no
output past the header. Factoring `f` over `K` and reading the linear factors gives
the same set: 0.025 s / 0.082 s / 0.316 s at degrees 2 / 4 / 6. Evidenced by route
agreement on `m004`, an unchanged `m004` calibration witness, `assert`ed group
axioms mod `f` on every run, and recorded element orders.

**3. The answer, per orbit — and they cannot be pooled.**

- **Orbit 0**, `[K:Q] = 4`, `|Aut| = 4`, orders `[1,2,2,2]` => `Gal(K/Q) = V_4`.
  **Exactly one of the three involutions** carries an untwisted intertwiner,
  `FOUND(4)`, lambda = 1; the other two fail untwisted *and* twisted; the identity
  control fails; Schur holds at dimension 4.
- **Orbit 1**, `[K:Q] = 6`, `|Aut| = 2` => `K/Q` **not normal**, orders `[1,2]`.
  The unique non-identity sigma carries an untwisted intertwiner, `FOUND(6)`,
  lambda = 1; control fails; Schur holds at dimension 6.

**Why orbit 0 is the first informative run.** `m004` and L6a4 class 1 both have
`|Aut| = 2`, so their single candidate succeeding is equally consistent with *"any
non-identity sigma works"*. Three involutions and one success is a genuine
selection.

**This does NOT close the bean, and the gap is sharper than before.** Two open
items, both raised BY this measurement rather than settled by it:

- **Which invariant distinguishes the winning involution in `V_4`?** The
  measurement says one of three is special; it does not say why. Until that is
  identified, "the duality sigma" is a name for something located by search.
- **Orbit 1 has an intertwiner but no transport argument.** `K/Q` is not normal
  there, so the `C_2` is not a quotient of a Galois group acting on all six roots.
  The orbit-0 upgrade route is unavailable on orbit 1 even though the conclusion
  looks the same.

Audit: `docs/audits/2026-09-14-ptolemy-lex-free-stage2-and-the-l6a4-gb-wall.md`
sections 5a-5c.


### 2026-09-14 (later) — the duality sigma is IDENTIFIED: complex conjugation of K

The open item from this morning's entry ("which invariant distinguishes the
winning involution in `V_4`?") is measured.

**The corpus already had a criterion and it does NOT select.**
`ptolemy_duality_galois_check.py` establishes that cocycle negation is
`u -> u^2`, "the nontrivial automorphism of mu_3, i.e. complex conjugation OF
THE CUBE ROOT OF UNITY". When `Gal(K/Q) = V_4`, TWO of the three involutions
invert `zeta_3`, so that criterion halves the candidates and stops. L6a4 is
where this is visible, because the older probes hardcode exactly the surviving
pair:

    sigma_a   inverts zeta_3 True   is conj(K) False   intertwiner False
    sigma_b   inverts zeta_3 True   is conj(K) True    intertwiner True

"Complex conjugation of mu_3" and "complex conjugation of K" are different
claims and only the second selects.

**Two notions, kept separate because they come apart here.** (CM) K totally
imaginary and `Fix(sigma)` totally real -- embedding-independent, decided
exactly by Sturm root counts, no tolerance. (EMB) `sigma(alpha) = conj(alpha)`
at one embedding, 60 digits. An earlier version of the probe asserted these
must agree and CRASHED on `5_2` orbit 1, whose K is totally imaginary but NOT
CM: `Fix(sigma)` has degree 3 and is not totally real, so (CM) is False while
(EMB) holds at 2 of 6 embeddings. The crash was correct.

    CM-conjugation, TESTABLE (>1 candidate) and HOLDS : 5_2-c1-orbit0, L6a4-c1
    corroborates but cannot select (|Aut| = 2)        : m004-c1
    K not CM, per-embedding statement only            : 5_2-c1-orbit1
    FAILS                                             : none

**What is NOT new, stated plainly:** the L6a4 selection itself is already in
`L6a4-c1-duality-orbit-untwisted.json` (`works_per_point` is `sigma_b` at every
point; `id`/`tau`/`sigma_a` fail) and the coboundary witness already records the
group as `Z/2 x Z/2`. New here is the IDENTIFICATION of the selected element,
and a second manifold on which the selection is exercised at all.

**Also fixed a latent regression I had introduced hours earlier.** The
factorisation route substituted `sp.rootof`'s return value, whose SHAPE varies
with f -- `ComplexRootOf` (5_2, monic), `Mul` `125*CRootOf(...)` (L6a4,
NON-monic), `Add` in radicals (m004, quadratic). It was developed against three
fields and all three were monic; the first non-monic field broke it. Both wrong
fixes were caught by the route's own guard rather than returning a wrong
automorphism count. Now uses `sp.to_number_field(r, alpha).as_poly(t)`, which is
shape-independent.

**STILL OPEN, and the bean stays open on all three:**

1. **Why should duality be realised by complex conjugation?** This is a measured
   regularity over four points, not a theorem. No mechanism is offered.
2. **Orbit 1 is weaker than it looks.** Its K is not CM, so only the
   per-embedding statement is available there, and `|Aut| = 2` means it could
   not have selected anything anyway.
3. **The transport argument still does not reach orbit 1** (K/Q not normal) --
   unchanged from this morning.

Probe: `computations/ptolemy/ptolemy_duality_sigma_is_complex_conjugation.py`.
Audit: `docs/audits/2026-09-14-ptolemy-lex-free-stage2-and-the-l6a4-gb-wall.md`
sections 5d-5e.


### 2026-09-14 (evening) — the MECHANISM, and why it cannot start from the Lagrangian

#7356 merged (46ba3c0243). Follow-up on branch
`claude/duality-sigma-hermitian-derivation-2026-09-14`.

**The mechanism.** The untwisted duality relation `A sigma(rho) A^-1 = rho^-T` is,
after one line of rearrangement, `rho^T A sigma(rho) = A` -- i.e. exactly the
invariance of the sigma-sesquilinear form `H(v,w) = v^T A sigma(w)`. The duality
intertwiner and an invariant form are THE SAME OBJECT. Schur (solution space =
[K:Q] free Q-params = one K-dimension, verified per case) makes it canonical.

It normalises Hermitian CONSTRUCTIVELY: `A^dagger = c A` by Schur, `N(c) = 1` by
applying dagger twice, and `d := x + c sigma(x)` satisfies `sigma(d) c = d` for
every x, so `A_herm := d A` is Hermitian on the nose. Hilbert 90 with a produced
witness. Measured c: -1 (5_2 orbit0), t+5 (m004), a cubic (L6a4), 1 (orbit1).

**Signature (2,1) -- i.e. PU(2,1) -- at every embedding, all four points.** Two
independent exact methods required to agree (Jacobi on the sigma-fixed leading
principal minors; roots of the characteristic polynomial at 50 dps). So these are
SPHERICAL CR representations. Corroborating detail: `A_herm[0,0] = 0` in every
case, i.e. `e_0` is a null vector, which a definite form cannot have.

**THE CAVEAT THAT MATTERS (audit section 3).** Steps 1-2 hold for ANY involution,
so they do NOT single out conjugation -- and measured, the other two involutions
on 5_2 orbit 0 admit no invariant form at all (nullspace 0). What conjugation
supplies is the SIGNATURE, an archimedean invariant that an abstract involution
does not have.

**WHY THE LAGRANGIAN ROUTE IS BLOCKED -- measured, all six grep paths.** The
corpus's reality/conjugation arc and its Lagrangian arc DO NOT TOUCH ANYWHERE:
zero matches in both directions between `QOU/Eightfold/` and any
Lagrangian/action term. Three specific gaps:

1. The only anti-structure inside `L_q` is the antipode S (`psi* = int_A o S(psi)`),
   and `def:frobenius-hopf-substrate` NOWHERE asserts `S^2 = id`. The S^2 hits in
   the corpus are all the HECKE antipode, a different object. So the involutivity
   hypothesis has no supplier upstream.
2. `L_q` is fibre-independent by `alg:categorical-action`'s own statement, while a
   signature is archimedean. Any Lagrangian route must pass THROUGH the
   archimedean specialisation, not around it.
3. `prop:categorical-self-duality` is unformalised by its own admission.

**Lean, sorry-free**: `QOU/Eightfold/DualityIntertwinerIsHermitianForm.lean` --
`invariantForm_of_intertwiner`, `hilbert90_witness`,
`hermitian_of_hilbert90_witness`, `hermitian_representative`. lean-direct exit 0
with `-DautoImplicit=false`; `#print axioms` clean on all four (propext /
Classical.choice / Quot.sound, no sorryAx). Stated over a general CommRing with an
arbitrary ring endomorphism, which localises what is algebra (all of the
formalised part) and what needs the archimedean place (the signature, NOT
formalised, and the file's Scope section says so).

**STILL OPEN — bean stays open:**
1. Why are these representations PU(2,1) at all? That is the input here, not the
   output.
2. The converse: must a duality sigma be conjugation? Nothing here shows it.
3. The Lagrangian connection, blocked on the three gaps above. `S^2 = id` for the
   QOU substrate antipode is the cheapest of the three to settle and is the one I
   would attack first.
4. Orbit 1 (not CM) still has no signature at 4 of its 6 embeddings; the probe
   asserts and aborts there rather than reporting one.

Audit: `docs/audits/2026-09-14-duality-sigma-is-conjugation-derivation.md`.


---

## 🛑 CORRECTION 2026-09-14 — my "cheapest of the three gaps" call was wrong

This bean recommended `S^2 = id` for the QOU substrate antipode as *"the
cheapest of the three to settle"* and as *"a single missing theorem in
`def:frobenius-hopf-substrate`"*. **Both halves are wrong.**

It is not a missing theorem, it is a missing **axiom**: measured, the block
carries no antipode condition at all, so `S` is free data and `S^2 = id` is
**INDEPENDENT** of the definition rather than unproved. And it is not cheap —
it is an owner decision about a central definition, not agent work.

Machine-checked: `QOU/QuantumObservableUniverse/AntipodeIndependence.lean`
(sorry-free, `lean`-direct exit 0) plus
`scripts/lean-structure-field-law-audit.py`, which gives the identical verdict
on both Lean carriers. Tracked as `qou-c64q`; write-up in
`docs/audits/2026-09-14-antipode-is-free-data-s-squared-is-independent.md`.

Consequence for THIS bean: the intrinsic route to identifying the duality with
complex conjugation (via `psi* = int_A . S(psi)` being an involution) is
**blocked on a definition the owner has not written**, not on a proof. The
archimedean signature argument of
`docs/audits/2026-09-14-duality-sigma-is-conjugation-derivation.md` is
unaffected and remains the live route.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Round 69 Formalization Progress (PR #8293)
- Formalized `QOU.Eightfold.PointwiseAgreementOnReduced.apply_eq_iff_sub_mem_all_primes` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/scale_mobius_adjoint_reduced_trefoil_probe.py`, `scriptHash: ae187b673714`, Commit 1 `9b139cda51963d9af6817b576a80c90bb2f74d00`, Commit 2 / Witness `474ee8c61ef5b687f244b6a129aeb23ef9956372`, PR `litlfred/qou#8293`).
