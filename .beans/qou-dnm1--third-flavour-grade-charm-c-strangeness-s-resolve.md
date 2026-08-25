---
# qou-dnm1
title: 'Third flavour grade (charm C / strangeness S) — resolve D-bar0 = K0 collision (qou-20sx child, from #4625). (n,T3) grades only by generation+weak-sign, so D-bar0{c-bar,u}={-5,+3} collides with K0{d-bar,s}={+3,-5} as a multiset. Needs a flavour Cartan (S,C) beyond isospin — the FLAVOUR SU(3)/SU(4) eightfold-way (DISTINCT from the excluded COLOUR SU(3) #4564; flavour is a global symmetry). Attack options: (1) extend GMN Y_f=B+S+C, derive S/C as higher Milnor/linking knot charges extending Y=B=mu-bar_123 #4597; (2) a third knot grading orthogonal to (n,T3); (3) flavour SU(3) weight lattice from Bring/icosahedral geometry (qou-d7h1 on #4600); (4) S/C as a q-graded/bar-grade flavour index. Owned partly by #4600 SU(3)/eightfold scope.'
status: todo
type: task
priority: normal
created_at: 2026-08-02T20:13:54Z
updated_at: 2026-08-25T18:06:33Z
parent: qou-20sx
---

## PREMISE VOID 2026-08-25 (qou-17mq) — no third flavour grade is missing

STATUS LEFT ALONE deliberately; closing is the author's call. But do not
start the four attack options in the title: they search for an object that
is not absent.

orderedContent_injective is proved SORRY-FREE, 'by decide', on main
(QOU/ParticleInteractions/MesonOperatorSelectionT3.lean:246):

  def gradedContent  (m) : Multiset Z := {-writhe c1, writhe c2}   -- symmetric
  def orderedContent (m) : Z x Z      := (-writhe c1, writhe c2)   -- keeps bar

  theorem graded_D_K0_collide     : gradedContent D = gradedContent K0
  theorem orderedContent_injective : Function.Injective orderedContent := by decide

This bean's own title writes the two states as D-bar0 = {-5,+3} and
K0 = {+3,-5}. Those are DIFFERENT ORDERED PAIRS. They collide only as
MULTISETS. And the ordering is not a bolted-on tiebreaker: it is the
quark/antiquark strand orientation, the same signedWrithe datum that
produces T3 — 'topological strand-orientation data, not a fit' per the
theorem's own docstring.

THE ARITY SLIP. mass_from_graded_content_cannot_separate quantifies over
f : Multiset Z -> Q, i.e. SYMMETRIC functions of the UNORDERED content. It
says no symmetric function of the multiset separates them. It does NOT say
the content cannot carry the mass — and the ordered complement is injective.
Fourth recorded instance of da-arity-conflation.

WHY IT PROPAGATED. MesonOperatorSelectionT3.lean carries the error and its
correction ADJACENT: the docstring on graded_D_K0_collide ends 'a further
flavour grading (charm number vs strangeness) is the remaining missing
datum', and the VERY NEXT THEOREM refutes it. The section heading above it
reads '### The honest remainder — residual content collision (needs a 3rd
grade)', which invites stopping exactly there.

NOT ESTABLISHED, and the distinction is the point: that the D-meson mass is
derived or derivable. Injectivity gives a FACTORISATION (an injection admits
a left inverse on its image), never a derivation of the factorising map.
Fitting through five injectively-labelled points is the per-state fit the
J/psi attack already recorded as worthless. sorry-free != derived.

WHAT ACTUALLY REMAINS: qou-qpj9 Obstruction A — a canonical, parameter-free
map from the ordered content to a hyperbolic braid word at H_3(q). The
(n,T3) content is Vol=0 torus-carrier data
(MesonFluxTubeReduction.twoStrand_winding_bijective). GEOMETRIC, and NOT
gated on 4-A / the N=3 problem — which is the ranking consequence: this
bean's front was placed behind the framework's hardest open object by a
dependency that does not exist.

RECOMMEND: re-scope onto qou-qpj9 rather than continue options (1)-(4).
qou-mesont3 reached this independently and recommended the same; that note
never reached this bean or the SM cheat sheet. Re-verified at source here,
not taken from that bean.
Audit: docs/audits/2026-08-25-4c-no-third-flavour-grade-is-missing.md
