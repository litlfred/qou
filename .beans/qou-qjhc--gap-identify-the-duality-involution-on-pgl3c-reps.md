---
# qou-qjhc
title: 'GAP: identify the duality involution on PGL(3,C) reps with the sigma-transport on Ptolemy coordinates'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T08:42:32Z
updated_at: 2026-09-11T15:25:52Z
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
