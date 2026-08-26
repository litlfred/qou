---
# qou-ken6
title: Serre-Leray spectral sequence of the colour fibration — unexplored, aimed at N=3
status: completed
type: task
priority: normal
created_at: 2026-08-25T21:13:28Z
updated_at: 2026-08-25T21:53:16Z
parent: qou-8lxd
---

Owner prompt 2026-08-25: 'we have fibration and serre-leray spectral sequence - check corpus'.

CORPUS-GREP RESULT — the tool is ABSENT, and the fibrations are PRESENT.

Serre-Leray: ZERO hits for the spectral sequence of a fibration, anywhere in
content/ or docs/. Every 'Serre' hit is the q-SERRE RELATIONS of a quantum group
(fred2005, UGB Groebner-Shirshov). Every 'Leray' hit is a LERAY SELF-SIMILAR
PROFILE in the Navier-Stokes blowup chapter. Different objects sharing the names.
The corpus DOES have one spectral sequence, in mass-theory/
spectral-sequence-collapse-proof.md, but it is HOCHSCHILD (HH^k = 0 by
Whitehead for semisimple algebras), not Serre-Leray of a fibration.

Fibrations, by contrast, are everywhere:
  brings-surface/color-tube-interpretation.md  the COLOUR FIBRATION over P^1(C),
      whose fibre is a curve inside the THREE-DIMENSIONAL colour space A^3 with
      c = (c_r, c_g, c_b)
  brings-surface/t-duality-elliptic.md         elliptic fibration S -> P^1(C)
  brings-surface/radial-projection.md          fibration over the base manifold M
  klein-bring-icosahedral-bridge.md            Seifert fibration S^3/2I -> S^2(2,3,5)
  knot-particle-generation-interpretation.md   Hopf fibration S^3 -> S^2
  virtual-particles-exceptional-divisor.md     Reeb bundle U(1) -> S^3 -> S_p

WHY THIS IS AIMED AT N=3, stated as a reason to look and NOT as a result.

The Sym^2 parity exclusion (merged, b457b8ad57) is a statement about objects of
the SINGLE-FIBRE TENSOR CATEGORY: any such object passing the gate has even
vector-space dimension, so none is 3-dimensional. The corpus's own conclusion is
that N=3 must therefore come from GROUPOID-LEVEL structure -- multi-strand,
framing, or inter-fibre.

A fibration total space is assembled from base AND fibre. It is not obviously an
object of the single-fibre tensor category, so the exclusion does not obviously
apply to it. And the Serre-Leray spectral sequence is precisely the machine that
computes the total space from the two. The colour fibration already carries a
three-dimensional colour space.

That is a SHAPE MATCH, and shape matches are exactly what the anti-laundering
discipline exists to catch. NOTHING IS CLAIMED HERE. I have not computed an E_2
page, not identified what would play the role of the fibre's cohomology, and not
checked whether anything the SS produces would pass the Sym^2 gate. The honest
status is: a standard tool, never applied, pointed at a live gap, with a stated
reason it might evade an exclusion that kills the obvious routes.

FIRST CONCRETE STEP for whoever takes this: for the colour fibration over
P^1(C), identify the fibre and base cohomology the corpus can actually supply,
and write the E_2 page. If E_2 cannot even be written down from existing corpus
objects, that is the answer and it is cheap to reach.

CAUTION: 'three-dimensional colour space A^3' is an AMBIENT affine space in which
a curve sits -- it is NOT a 3-dimensional representation of anything. Reading it
as the missing flavour triple would be precisely the dimension-vs-object
conflation this epic keeps having to retract.


## CORRECTION 2026-08-25, same session — "ABSENT" WAS WRONG. Owner caught it.

Owner: "double check corpus - should be pages there already. maybe only in lean
and not exposition?" Correct on both counts; the central claim above is retracted.

MY ERROR: the grep behind "ZERO hits" did cover .md AND .lean, but I read it
through `head -15` and all fifteen lines were .md. The .lean hits sat below the
cutoff. I concluded absence from a truncated list.

WHAT ACTUALLY EXISTS — a real spectral-sequence layer, mostly in Lean:

  QOU/Mathlib/SpectralSequence.lean          29 decls, ZERO sorry, zero axiom
      Abstract E_r-page API: pages indexed by N x Z x Z, differential of bidegree
      (r, 1-r) cohomological, CollapsesAt r0, convergesTo. Its docstring states
      the gap it fills: "Mathlib has homological-algebra primitives
      (HomotopyCategory, DerivedCategory, ChainComplex) but no E_r-page
      abstraction with collapse criteria." EXPOSITION-FREE — exactly the owner's
      guess: this piece exists only in Lean.

  QOU/Machinery/SpectralSequenceBasic.lean    3 decls, 3 sorry (by design)
      Scaffold for the GB (Groebner-Shirshov) filtration SS; d_1, d_2 sorry'd,
      docstring calls the instances "the open infrastructure work".

  QOU/BraidKnot/spectral_sequence_h3_explicit.lean   2 decls, 0 sorry
  QOU/BraidKnot/e_infinity_identifications.lean      2 decls, 4 sorry (6-term E_inf)
  QOU/WedderburnMass/curvature_rank_gb_stratification.lean
  exposition: mass-theory/spectral-sequence-collapse-proof.md,
              appendix-mass-binding-algorithms/mba-step07-gb-filtration.md

WHAT SURVIVES, precisely: the corpus SS is the GB-FILTRATION / HOCHSCHILD-KLR
one, claiming CollapsesAt 2 — the Wedderburn block decomposition IS the E_2 page.
That is a filtration spectral sequence OF AN ALGEBRA. It is not the Serre-Leray
SS OF A FIBRATION, which relates H*(base), H*(fibre), H*(total). Serre-Leray in
that sense still does not appear.

BUT THE GAP IS FAR SMALLER, AND BETTER SHAPED: the E_r machinery already exists
and is sorry-free. Applying it to a fibration means INSTANTIATING AN EXISTING
API, not building one.

REVISED FIRST STEP (supersedes the one above): instantiate
QOU.Mathlib.SpectralSequence on the colour fibration over P^1(C) — identify what
plays E_2^{p,q} from base and fibre cohomology the corpus can actually supply.
If the existing API cannot be instantiated on it, that is the answer, cheaply.

CAUTIONS, both live: (1) the colour fibration's ambient A^3 is a space a curve
sits in, NOT a 3-dimensional representation; (2) the GB SS's own differentials
are sorry'd, so "the corpus has a spectral sequence" must not be read as "the
corpus has a PROVED spectral sequence".


## ANSWERED 2026-08-25 — the Serre-Leray SS of the colour fibration supplies RANK 2, not 3.

Probe: computations/eightfold/colour_fibration_leray_e2_probe.py (exact sympy over Q(z), no floats).
Audit: docs/audits/2026-08-25-colour-fibration-leray-e2.md
Commit: 01d6b1ad31

FIBRE SETTLED FIRST, because the corpus was ambiguous and the answer turns on it.
Read as a cubic in one variable the fibre would be THREE POINTS, and everything
below would collapse. It is not. t-duality-elliptic.md gives the Weierstrass
form and the fibre is an ELLIPTIC CURVE. The probe verifies both of the corpus's
own shifts symbolically -- X = c + z (color-tube-fibers.lean) leaves the X^2
coefficient NON-zero, so that shift alone does not depress the cubic; the second
shift X = t - (z+1)/3 does -- and reproduces the corpus's published

    p(z) = (2z^2 + z + 2)/3
    q(z) = 5(4z^3 + 3z^2 + 3z + 4)/27

EXACTLY (both agreement checks return True; the probe exits non-zero if either
fails). Delta(z) = -4p^3 - 27q^2 has degree 6 and is not identically zero, so the
generic fibre is a smooth genus-1 curve.

THE RANK. A genus-1 curve has H^0 = Z, H^1 = Z^2, H^2 = Z. The fibration's
representation-theoretic content is the monodromy pi_1(B0) -> SL(2,Z) on
H^1(fibre) = Z^2. RANK 2 -- the same 2 the framework already has. No 3.

DEGENERATION. Over the smooth locus B0 = P^1 minus the roots of Delta, B0 is an
open Riemann surface (cohomological dimension 1), so E_2^{p,q} is supported in
p in {0,1}. Every d_r with r >= 2 has target at p+r >= 2, where all groups
vanish. All d_r vanish for r >= 2, so E_2 = E_infinity -- degenerate for DIMENSION
reasons, before any QOU input is used. No differential, no new object.

HONEST CAVEAT, stated in the audit: that is the SERRE SS over the smooth locus.
The LERAY SS over all of P^1, with the constructible sheaves R^q f_* Z, has
H^2(P^1) nonzero and a d_2 : E_2^{0,1} -> E_2^{2,0} MAY be nonzero. That variant
is not degenerate and I do not claim it is. It changes nothing: H^1 of the fibre
is rank 2 either way, and a differential can only REDUCE what survives to
E_infinity, never manufacture a rank-3 summand absent from E_2.

THE OTHER READING IS THE ONE THIS BEAN WARNED ABOUT, AND IT IS ALREADY DEAD.
Taking r, g, b -- the three ambient coordinates, equivalently the three roots --
as the triple directly gives the S_3 PERMUTATION representation. Permutation
representations are self-dual (the permuted basis is orthonormal for an invariant
symmetric form), so FS = +1, Sym^2 carries a singlet, and it fails the Sym^2 gate
for the same reason the SU(2) adjoint does. S_3 = W(A_2) is the WEYL GROUP of the
weight lattice, not the fundamental representation. Already recorded as T3g
section 4 in docs/audits/2026-08-07-eightfold-live-surface-collapse.md.

Both readings therefore land on results the corpus already has.

SCOPE, per the (a)/(b) discipline.
  (b) STRUCTURAL, invariant named: the Serre-Leray SS of THIS fibration cannot
      supply a rank-3 object. The invariant is a rank bound -- H^1 of a genus-1
      curve has rank 2, an open Riemann surface has cohomological dimension 1.
      A bound, not a failed numerical fit.
  (a) ONLY, explicitly NOT (b): nothing here excludes fibrations in general, the
      corpus's other fibrations (Seifert S^3/2I -> S^2(2,3,5), Hopf S^3 -> S^2,
      the Reeb bundle), or groupoid-level structure as the source of N = 3. The
      bean's framing -- that the Sym^2 exclusion is about single-fibre objects
      and something built from base AND fibre might evade it -- STAYS LIVE. What
      is settled is that the COLOUR fibration, the one that looked most promising
      because it carries a visible three, does not do it.

TWO INFRASTRUCTURE FINDINGS, recorded not fixed (they touch another area's file
and neither is caused by this work). In QOU/Mathlib/SpectralSequence.lean:
  1. The structure does NOT carry the d o d = 0 requirement its docstring claims
     ("equipped with differentials d_r and the requirement d_r o d_r = 0"). There
     is no such field. Cells are bare Type u with no module structure, so the
     condition is not statable as written; trivial_d_squared_zero holds for PUnit
     by rfl and is not it.
  2. instance canonical makes GBFiltrationCollapsesAtE2 R ALWAYS INHABITED by the
     trivial PUnit sequence. Every [GBFiltrationCollapsesAtE2 R]-conditional
     theorem downstream is therefore conditional on nothing -- the AGENTS.md
     section 3b-tax failure mode. Neither undermines anything above (this work
     instantiates no Lean API; it settles geometry), but both matter to anyone
     reading CollapsesAt-conditional statements as carrying content.
