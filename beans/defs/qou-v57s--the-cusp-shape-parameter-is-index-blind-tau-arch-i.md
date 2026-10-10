---
# qou-v57s
title: 'The cusp shape parameter is INDEX-BLIND: tau_arch is not a function of the algebraic seed (scope-(b), pigeonhole)'
status: in-progress
type: task
created_at: 2026-10-10T12:34:17Z
updated_at: 2026-10-10T12:34:17Z
---

Measured 2026-10-10 (PR #7586, issue #7585) while working `qou-3kni`'s cusp
leg. Parent subject: `conj:shared-denominator-cusp-holonomy`, carrier
`folio/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md`.

## The finding

The conjecture says the `n` roots `q_0^{-k}` of `(x; q_0)_n` "address" the
cusps. `snappy_cusp_seeding.py` measured `|q_0^{-k} - z_k| ~ 0.4-0.9` against
SnapPy's shapes and concluded the bijection must be of **labels**, *"with the
actual shape parameter being a non-trivial function `tau_arch(q_0^{-k})` of the
algebraic seed; the shape of that function is the subject of further work."*

**There is no such function, and showing it needs no distance -- only
counting.** From the COMMITTED witness (SnapPy not re-run):

| manifold | `n` roots, pairwise distinct | distinct shape VALUES | tetrahedra up to ISOMETRY | cusps |
|---|---|---|---|---|
| m004 | 2 | 1 | **1** | 1 |
| m003 | 2 | 1 | **1** | 1 |
| L6a4 | 8 | 2 | **1** | 3 |

The isometry column is not what the witness records. An ideal tetrahedron has
THREE shape parameters -- the edge-relabelling orbit -- so two recorded values
can be one tetrahedron, and L6a4's are: `(1+i)/2` is `rotate` twice from `1+i`
(`rotate(1+i) = i`, `rotate(i) = (1+i)/2`), both with angles
`{pi/4, pi/4, pi/2}`. m004/m003 are two copies of the REGULAR tetrahedron,
whose orbit is a FIXED POINT -- and that fixed-point property IS regularity.

So `tau_arch` (seed -> shape) is **CONSTANT** on all three: `n` distinct inputs,
one isometry class out.

**Scope: (b) structural exclusion. Invariant: pigeonhole on a finite set.** A
map from an `n`-set onto a 1-set is not injective and carries no information
about its argument. This excludes `tau_arch` AS A FUNCTION OF THE SEED VALUE,
on the three triangulations the corpus probes -- every injective candidate
(Moebius, exponential, any reparametrisation) AND every non-constant one. It
does NOT exclude the conjecture.

## 🛑 The orbit identity was ALREADY PROVED, sorry-free -- cite the Lean

`QOU/MathlibExt/IdealTriangulation.lean` (0 sorries) carries `param`,
`rotate` (docstring: *"The same tetrahedron, relabelled"*), `shape_cycle2`,
`shape_cycle3`, `rotate_angles`, `param_prod`. Its section header states the
very thing the probe re-measured: *"`z -> 1/(1-z)` does not change the
tetrahedron ... **This is not a coincidence to be checked numerically.**"*

The probe's identity section is downgraded in its own docstring to a
consistency check of its arithmetic against that proof, directing a citer to
`shape_cycle2` / `rotate_angles`. **What is genuinely new here is only the DATA
step** -- that the committed values lie in one orbit -- plus the counting
consequence. Recorded this way because the probe nearly published proved Lean
as a numerical finding.

## Why the conjecture SURVIVES, and what to measure instead

Its displayed RHS is **holonomy**: `Hol_{mu_k}(z_k) = Hol_{lambda_k}(z_k) = 1`.
A holonomy is a product of shape parameters along a meridian/longitude PATH, so
it is path-dependent and therefore index-dependent **even when every shape is
equal** -- exactly the property shapes lack. So the conjecture's EQUATION is
better than its own table row (*"pole of Phi_n <-> complete cusp"*) and better
than the witness's reading: the existing probe measured the one object in the
statement that cannot carry the index.

**The object to measure is the residual `|Hol_{mu_k} - 1|` at the algebraic
seeds, not `|q_0^{-k} - z_k|`.** `snappy_cusp_seeding.py`'s SECOND caveat
already says a genuine test needs the gluing system.

## Two smaller corrections to the recorded negative

1. **ARITY.** The equivalence ranges `k` over `n` roots on the left and over
   CUSPS on the right, and `n != c` in all three cases (2v1, 2v1, 8v3). The
   carrier's own table row already says *"n ideal tetrahedra in JSJ piece"*, so
   **the carrier is internally inconsistent**: table tetrahedron-indexed,
   equation cusp-indexed. Tetrahedron-indexing is the consistent reading and is
   what the producer pairs against (`M.tetrahedra_shapes`).
2. **The 0.4-0.9 is mostly the probe's own knob.** Seeds are lifted by a fixed
   `IM_PERTURBATION = 0.1` while the true `Im` is `sqrt(3)/2 = 0.866`. Matching
   the lift collapses m004 from `0.8646/0.9148` to `0.4009/0.5`. The knob-free
   part is the REAL part, floor **0.400918284** on m004, which no lift can
   move -- a STRONGER negative than the recorded one, since it holds for every
   lift.

## What is NOT established here

- **Whether anything in the corpus already computes the holonomy residual.**
  `IdealTriangulation.lean` has `SatisfiesEdgeEquations` /
  `SatisfiesAngleEquations` and ZERO cusp/meridian/longitude hits, but per-knot
  meridian work exists elsewhere -- `QOU/Knot/FigureEightDeformedMeridianWinding.lean`,
  `QOU/Mass/FiveTwoGluingFromFareyWord.lean`,
  `QOU/Mass/FiveTwoAPolynomialFromFareyWord.lean` -- and none was read closely.
  The six-path corpus-grep gates the claim and was NOT run to completion. A
  `corpus-grepper` pass was in flight when this was written; **read its result
  before citing any novelty here.**
- **Generality beyond these three triangulations.** SnapPy's triangulation is
  not canonical; a different one changes `n`. The conjecture ties `n` to
  GB-depth `k_star(T_w) = n`, an ALGEBRAIC quantity, so whether `n = c` is
  achievable at all is a separate question not settled here. Do not read the
  arity row as a general theorem.

## The decision this leaves with the owner

**Default if nothing is done:** nothing changes. The probe is additive, the
carrier keeps its cusp-indexed equation beside its tetrahedron-indexed table,
and the witness keeps its lift-dependent distance as the published negative.
Under AGENTS.md's ASK-THE-OWNER rule a content edit to a conjecture statement
is not an agent's call, so it has not been made.

- **Re-index the carrier** from cusps to tetrahedra in the displayed
  equivalence, matching its own table row. Costs one `.md` + `.ts` + `.lean`
  sibling edit on `shared-denominator-cusp-holonomy`; risks that the
  cusp-indexed form is the INTENDED one and the table row is the error --
  which only the author knows. Commits the conjecture to the tetrahedron
  reading.
- **Record the prune in the carrier's own §"Empirical scope"** without
  touching the equivalence: replace *"the shape of that function is the subject
  of further work"* with the counting argument. Costs one paragraph; risks
  nothing; commits to nothing, and stops the next agent spending a session
  searching for `tau_arch`.
- **Build the holonomy residual** -- the positive route. Costs a real compute
  leg (Thurston gluing system per manifold, meridian/longitude paths, mpmath);
  risks being duplicated if the corpus-grep finds it exists; commits to the
  tetrahedron/holonomy reading. This is the only option that could CLOSE
  anything.

**My recommendation, as judgement not finding:** take option 2 now (one
paragraph, no risk, and it is the thing that stops wasted search), hold option
1 until you say which indexing you meant, and schedule option 3 only after the
corpus-grep result lands -- because if `FiveTwoGluingFromFareyWord` already
carries the residual machinery, option 3 is a wiring job rather than a compute
leg.

## Status

`in-progress`, not completed. **The conjecture is open** and this bean's
subject is a constraint on it, so per AGENTS.md it does not close on the
recording being done.

