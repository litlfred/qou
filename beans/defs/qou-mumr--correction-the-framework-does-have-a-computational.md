---
# qou-mumr
title: 'CORRECTION: the framework DOES have a computational length -- distance is a Reeb step count, ell_P == 1'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T11:02:55Z
updated_at: 2026-10-04T15:18:12Z
parent: qou-q4oa
---


Branch: claude/anchor-followups-2026-08-08.

## I WAS WRONG. Retracting a claim I made twice today.

I wrote, in qou-usft and in the coulomb_energy.py docstring, that "the framework
has never constructed a position-space geometry at all -- everything it has is
trace-space or hyperbolic-volume", and concluded that r0, A^(1/3) and the 3/5
shape factor have NO derived counterpart to wire in. The owner said that was
wrong and pointed at a computational Planck length. They are right.

`folio/quantum-observable-universe/information-theory/discrete-planck-step.md:35`

    One Planck length of flow. After one Planck step, the Reeb flow displaces a
    state by exactly one Planck length:

        ell_P(q) = hbar_q * t_P = (1 - q^-1) * q/(q-1) = 1.

    "The Planck length identically evaluates to 1 over any field."

Also `fluid-dynamics/p5-counterexample.md:4`: "The separation d is measured in
units of the Planck length ell_q = (q-1)/q."

So the framework HAS a length, and more than that it has a notion of DISTANCE:
**distance in spacetime is computational** -- it is a COUNT of Reeb/Planck
steps, with ell_P == 1 by construction and "no sub-step resolution"
(discrete-planck-step.md:33). Distance is integer-valued, not a real number.

## Why this matters, and it reframes the whole EM line

qou-usft concluded the Coulomb work was blocked because no position-space object
exists. That conclusion is WRONG as stated. What is actually true is narrower
and more useful:

  * a nuclear radius in this framework is a STEP COUNT, not a length in fm;
  * converting a step count to fm needs the unit-system map, and
    `observations/g-q-closed-form.md:64` says exactly that -- G_Newton "enters as
    a unit-system datum, not as a fit parameter on q", fixing ell_P, m_P, t_P
    onto metres;
  * so the charge "density" is a distribution over a DISCRETE step lattice, not
    a continuous rho(r). The uniform-ball / Gaussian / exponential shape factors
    computed in qou-usft are all CONTINUUM objects and may all be the wrong
    class of answer.

That last point is the live one. The 7.3 % shape spread I measured was across
three continuum profiles. If the framework's density lives on an integer step
lattice, the right calculation is a LATTICE Coulomb sum, not an integral, and
the shape factor f must be recomputed in that setting.

## Status of the sweep

A full corpus search on derived length / distance / metric recovery, and on the
computational-QFT / quantum-gravity source the owner recalls, was dispatched and
is still running at the time of writing. This bean records only what was
verified by direct grep. The sweep may find more -- in particular whether any
construction recovers a METRIC (not just a length unit), which is what a real
rho(r) would need.

## Corrections owed elsewhere

  * qou-usft "STEP 4" section and its "WHAT WOULD ACTUALLY UNBLOCK THIS" -- the
    "no position-space density exists" framing must be narrowed to "no CONTINUUM
    density; the native object is a discrete step lattice, and the continuum
    shape factors may be the wrong class".
  * computations/coulomb_energy.py -- the R0_FM comment block repeats the same
    over-claim.
Both left for the sweep's result so they are corrected once, with the full
picture, rather than twice.

## CORRECTION TO THIS BEAN (sweep returned) — I overread the source twice

The sweep confirms a derived Planck length exists, so the owner's correction of
me stands. But TWO things I wrote above are wrong.

### (a) "distance in spacetime is computational -- a COUNT of Reeb/Planck steps"

OVERREAD. `discrete-planck-step.md:55` actually says the count of Planck steps
measures dynamical distance **IN REEB TIME**, and its `N(q0,q)` is an integral
over the SUBSTRATE PARAMETER -- a cosmological-time count along the q-trajectory,
not a spatial separation between two points. "Distance is integer-valued
[spatial]" does not follow from the line I cited.

Worse, `planck-time-interpretation.md` names what `ell_P` actually is:
"After one Planck time of Reeb flow, the ANGULAR DISPLACEMENT is
ell_P(q) = hbar_q * t_P = 1." It is one circuit of the Reeb FIBRE -- a phase,
not a spatial displacement. And it is an IDENTITY: it equals 1 for every q over
every field, so it carries no scale information at all. The q-dependence lives
entirely in t_P, the step COUNT, never in the length.

### (b) I cited two mutually inconsistent Planck lengths as if they agreed

Above I quoted `ell_P = 1` (discrete-planck-step.md:39) and
`ell_q = (q-1)/q ~ 0.0991` (p5-counterexample.md:4) in adjacent paragraphs
without noticing they differ by a factor t_P ~ 10.1. That is a REAL CORPUS
DEFECT, not just my sloppiness, and nobody had flagged it:

    information-theory/discrete-planck-step.md:39-43   ell_P = hbar_q * t_P  = 1
    information-theory/planck-info-unit.md:1           ell_P(p) ~ hbar_q     ~ 0.0991
    lean/QOU/InformationTheory.lean:32-34              localPlanckLength := quantumPlanckConstant
                                                       (i.e. = hbar_q EXACTLY)
    fluid-dynamics/planck-reynolds.md:1                ell_q = (q-1)/q       ~ 0.0991

The Lean file has silently HARDENED the prose's "~" into a definitional "=".
Anyone consuming `localPlanckLength` is getting hbar_q, while the
discrete-Planck-step chapter says the Planck length is identically 1. These
cannot both be right. Needs adjudication -- own bean.

## THE OPERATIVE CONCLUSION SURVIVES

Wrong on the letter, right on the consequence. The corpus HAS:
  * a derived but DIMENSIONLESS ell_P (an angular Reeb displacement, == 1);
  * ASSUMED metrics -- Fubini-Study inherited on Bring's surface
    (briggs-klein-chart.md:1), the round metric on P(V) = S^2 and an actual
    distance function d_{P(V)} gating a force law
    (measurement-observation/torsion-knot-flow.md:19,22,29), a base manifold M
    with a smooth metric and spatial wavenumbers
    (q-heat-kernel-peter-weyl.md:13). All declared ARCHIMEDEAN SPECIALISATION,
    i.e. inputs.
  * radial coordinates -- but in SUBSTRATE/MODULI space (genus-4 surface, or the
    2-sphere), never a radius from a nuclear centre.

It does NOT have (i) any transport from algebraic/hyperbolic invariants to a
Euclidean length, or (ii) a 3-space or charge density. And the corpus says (i)
about ITSELF, which is the strongest evidence available:

  pion_radius_and_cusp_volume_gap_probe.py:56-63 --
    "there is NO categorical volume->length transport in the corpus. All corpus
     lengths arise as Compton inversions hbar c / mass."

So r0, A^(1/3), 3/5 and rho(r) still have no derived counterpart. The EM
conclusion in qou-usft stands; only its justification needed narrowing.

Also: `lean/QOU/MassTheory/RadialVolRhoMirrorTest.lean` is a MACHINE-CHECKED
REFUTATION of the nearest thing to a density ansatz, rho(K) = tr_M(K) -- it
fails the 3H/3He mirror test in DIRECTION (C_knot ratio 1.35 vs rho ratio 0.50,
straddling unity). "Radial" there is magnitude-vs-phase, not position.

## THE ONE ACTIONABLE OPENING

A categorical Dirac operator EXISTS with Lean existence and uniqueness:
`quantum-observable-universes/categorical-dirac-operator{,-exists,-unique}`,
D_grad = q^-1 grad + (1-q^-1) iota_xi grad. Connes is in references.bib. But the
corpus NEVER forms the spectral distance
    d(phi,psi) = sup{ |phi(a)-psi(a)| : ||[D,a]|| <= 1 }.
NCG appears only as ALGEBRA (the universal Kahler-differential SES,
docs/audits/2026-05-03-tau-hat-n-proton-realisation.md:81-87), never as metric
geometry. There is no spectral triple.

That is the sharpest available route to a genuine derived metric: the algebra is
there, the Dirac operator is there and is Lean-proved to exist and be unique,
and the missing step is forming the triple and the distance. NOT attempted here.

## On the owner's remembered paper

Finster's CAUSAL FERMION SYSTEMS -- the programme where spacetime itself emerges
from a measure on operators -- IS in the corpus: references.bib
(finster2021/2022/2024, dappiaggi2024) and `observations/cfs-comparison-summary.md`.
That is almost certainly the memory. But the block is a STRUCTURAL COMPARISON
only: it records agreements (both type II_1 factors, free-probability class) and
mismatches (G(1,1)=1 vs L_CFS(1,1)=0), leaves the key numerical question open,
and imports no geometry. Also present: Verlinde entropic gravity, Jacobson,
Bilson-Thompson braided QG (vendored PDF), 't Hooft Planck-scale CA (realised as
the Planck STEP, i.e. time). NO causal sets, spin foams, tensor networks, or
Ryu-Takayanagi anywhere.

## LITERATURE — actual entries, with corpus locations

Verified present in `references.bib` by the sweep. Marked with what each does
and does NOT give us.

  finster2021 / finster2022 / finster2024, dappiaggi2024
      CAUSAL FERMION SYSTEMS. Spacetime and its geometry EMERGE from a measure
      on operators on a Hilbert space -- the closest published programme to
      "distance is computational". Corpus block:
      folio/quantum-observable-universe/observations/cfs-comparison-summary.md
      STATUS: structural comparison ONLY. Records agreements (both type II_1
      factors, free-probability class) and mismatches (G(1,1)=1 vs
      L_CFS(1,1)=0), leaves the key numerical question open, imports no geometry.

  connes1994 (Noncommutative Geometry), connes1996,
  chamseddine-connes-1997 (spectral action)
      THE tool for getting a metric from an algebra: the spectral distance
      d(phi,psi) = sup{|phi(a)-psi(a)| : ||[D,a]|| <= 1} on a spectral triple
      (A, H, D). Recovers geodesic distance in the commutative case and works
      for noncommutative A.
      STATUS: cited, but used only as ALGEBRA (universal Kahler-differential
      SES, docs/audits/2026-05-03-tau-hat-n-proton-realisation.md:81-87). The
      distance formula is never formed; there is no spectral triple.
      => This is the actionable gap: the categorical Dirac operator already
         exists AND is Lean-proved existent and unique.

  verlinde2011 (entropic gravity), jacobson1995 (Einstein eq. as equation of
  state)
      Cited at information-theory/information-theory-intro.md:3.
      STATUS: emergent GRAVITY / FORCE, not emergent DISTANCE. Both presuppose
      a metric and derive dynamics on it.

  bilsonthompson2007, "Quantum gravity and the standard model"
      Braid states in background-independent QG. Vendored PDF at
      library/0603022v2/0603022v2.pdf. Directly on-theme (braids -> particles).
      STATUS: no metric construction.

  thooft2016, Planck-scale cellular automaton
      Cited at discrete-planck-step.md:68; the Planck STEP realises 't Hooft's
      tick. STATUS: discretises TIME, not space.

  Ashtekar / Rovelli LQG entropy
      gravity-spacetime/lqg-entropy-qdim-partition-pole.md:14 uses S = A/4 l_p^2
      to FIX the Immirzi parameter. STATUS: l_p enters as an EXTERNAL symbol --
      it is consuming a Planck length, not deriving one.

  ABSENT entirely, checked: causal sets (Bombelli-Lee-Meyer-Sorkin), spin foams
  as a construction, tensor networks / MERA, Ryu-Takayanagi, ER=EPR,
  It-from-Qubit. If the owner is remembering a distance-from-counting paper, it
  is Finster CFS above, not a causal-set source -- none is in the tree.

## OWNER'S INSIGHT: "spectral distance is computational distance in aggregate?"

Essentially YES, and it makes the Connes route far more concrete than the
generic "form a spectral triple" suggestion above. Stating it precisely:

  d_Connes(phi, psi) = sup{ |phi(a) - psi(a)| : a in A, ||[D, a]|| <= 1 }

is not itself a count -- it is a VARIATIONAL formula, a sup over the algebra.
But on a DISCRETE structure it REDUCES to one. This is standard: for a finite
spectral triple / a graph whose Dirac operator carries the hopping structure,
the Connes distance equals the SHORTEST-PATH distance -- the minimal number of
edges. The mechanism is exactly the owner's "in aggregate":

  * the constraint ||[D, a]|| <= 1 is a LIPSCHITZ condition -- it says the
    observable a may change by at most 1 per elementary step;
  * therefore |phi(a) - psi(a)| <= (number of steps between the two states);
  * the sup SATURATES on the observable that increments by the full 1 at every
    step, so the sup EQUALS the step count.

So the spectral distance is the algebraic dual of step-counting: it extracts the
count from the algebra WITHOUT presupposing a geometry, and it interpolates --
states not separated by a whole number of steps get a real distance.

WHY THIS MATTERS FOR QOU SPECIFICALLY. The framework already has the step
structure (Reeb/Planck steps) and already has the operator (the categorical
Dirac operator D_grad = q^-1 grad + (1-q^-1) iota_xi grad, Lean-proved existent
and unique). The missing step is not conceptual, it is: form the triple and
check that d_Connes reproduces the Reeb step count. If it does, the framework
has a DERIVED metric rather than an assumed one, and the count-vs-continuum
question in qou-usft becomes answerable.

A CONSISTENCY OBSERVATION worth testing, not yet a claim: the Lipschitz
normalisation ||[D,a]|| <= 1 is what SETS THE UNIT of the resulting distance.
The corpus's ell_P = hbar_q * t_P == 1 is dimensionless and identically 1 over
any field. Those two 1's may be the same 1 -- i.e. ell_P == 1 might be the
statement that the Reeb step IS the Lipschitz unit, which would explain why it
carries no scale and why converting it to fm needs an external datum
(g-q-closed-form.md's G_Newton). If so, the qou-adwi contradiction may resolve
as: ell_P == 1 is the METRIC UNIT, and hbar_q ~ 0.0991 is a different quantity
(an angular velocity) that was mislabelled a length. TEST THIS before adjudicating
qou-adwi either way.

## Progress (PR #8452)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PolarizationArgumentDiscardDecayWindowFractionSurprisalVolumeTermStepUnitDomainWallDilution.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_k6is_kh7e_lsvj_mumr_qjh8_probe.witness.json` (`Commit 1` = `ffa2d78ef5414a49bba12e0efccca6fbb72626d5`, `HEAD` = `078aa49b3db67c82ebbd4ebd6bd00b088ab2f9d9`).
