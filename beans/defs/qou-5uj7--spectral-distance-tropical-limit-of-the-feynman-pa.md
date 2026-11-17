---
# qou-5uj7
title: 'Spectral distance = tropical limit of the Feynman path sum: formalize d_Connes = minimal Reeb step count'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T12:04:33Z
updated_at: 2026-11-17T08:05:00Z
parent: b9cj
---


Branch: claude/anchor-followups-2026-08-08. From the owner's question: "can we
formalize that spectral distance is an aggregation of computational distances?
is this like the computational paths in Feynman diagrams?"

Answer: yes to both, and the corpus already holds both halves. Precise below,
with established results separated from the QOU-specific step that is NOT.

## THE STATEMENT

Connes spectral distance and the Feynman path sum are THE SAME PATH STRUCTURE
under two different semirings:

    Feynman            (C, +, x)              weight e^{iS/hbar}   coherent SUM
    Connes/Wasserstein (R u {inf}, min, +)    weight = cost        MINIMUM

related by TROPICALIZATION: Sum_paths e^{-S/hbar} -> min_paths S as hbar -> 0
(Laplace / Varadhan; Maslov dequantization). So the spectral distance is the
TROPICAL LIMIT of the path sum.

## IS IT AN AGGREGATION? Yes -- of TRANSPORT PLANS, not of paths.

Connes distance has exactly the Kantorovich-Rubinstein form:

    d_Connes(phi,psi) = sup{ |phi(a) - psi(a)| : ||[D,a]|| <= 1 }
    W_1(mu,nu)        = sup{ Int f dmu - Int f dnu : Lip(f) <= 1 }

||[D,a]|| IS the Lipschitz seminorm. So Connes distance is a NONCOMMUTATIVE
WASSERSTEIN-1 distance, i.e. an optimal-transport cost. The AGGREGATION is on
the PRIMAL side -- min over couplings pi of Int d(x,y) dpi, each coupling
aggregating mass x distance -- and the sup formula is its DUAL. On a discrete
structure each d(x,y) is itself min-over-paths of the step count.

So: aggregation yes; but a MINIMUM over transport plans, not a coherent sum over
paths. That is exactly the difference from Feynman, and it is the semiring.

## WHAT THE CORPUS ALREADY HAS

  * Path sum -> finite trace. Ch 10, QOU.FeynmanPathIntegrals:
      lem:feynman-trace-collapse   "Path integral collapses to a finite sum on
                                    the eigenbasis"
      lem:feynman-markov-identification  "Markov-weighted eigenbasis sum equals
                                    the Markov trace"
      prop:feynman-categorical-trace, prop:feynman-classical-limit
      folio/quantum-observable-universe/braids-and-knots/feynman-eigenbasis.md
    i.e. the corpus HAS ALREADY replaced Int Dphi e^{iS/hbar} with the Markov
    trace on the knot eigenbasis.
  * The algebra and trace: Hecke H_n(q) + Markov.
  * The Dirac operator: categorical-dirac-operator{,-exists,-unique}, Lean-proved
    existent AND unique. D_grad = q^-1 grad + (1-q^-1) iota_xi grad.
  * The step structure: Reeb / Planck steps (discrete-planck-step.md).

MISSING: the spectral distance itself. One construction. NCG appears in the
corpus only as ALGEBRA (the universal Kahler-differential SES,
docs/audits/2026-05-03-tau-hat-n-proton-realisation.md:81-87), never as metric
geometry -- no spectral triple is ever formed.

## THE TARGET THEOREM

    d_Connes(states) = minimal Reeb step count

Checkable in the finite case, and a theorem statement rather than a programme.
If it holds, the framework has a DERIVED metric instead of the assumed ones
(Fubini-Study on Bring's surface, round metric on P(V) = S^2) catalogued in
qou-mumr -- which would unblock the position-space density that qou-usft is
stuck on.

## ESTABLISHED vs NOT -- do not blur these

  ESTABLISHED (literature):
    - Connes distance = Kantorovich-Rubinstein form; ||[D,a]|| as Lipschitz
      seminorm (Rieffel, compact quantum metric spaces; d'Andrea-Martinetti for
      the Wasserstein identification).
    - On discrete spectral triples / graphs, Connes distance = shortest-path
      metric. Caveat: WHICH D matters; the result is sensitive to the choice.
    - Tropicalization of path sums (Maslov dequantization, Laplace method).
  NOT ESTABLISHED, and this is the actual work:
    - that QOU's REEB STEPS are the graph edges of that spectral triple. Nothing
      currently connects the categorical Dirac operator to the Reeb step count.

## THE HONEST RISK

The Feynman weight is e^{iS/hbar} -- IMAGINARY and oscillatory. Tropicalization
is clean for e^{-S/hbar} (real, Euclidean). Getting from the corpus's
oscillatory path sum to a min-plus cost needs a Wick rotation or an equivalent.
The corpus's bar-involution machinery (bar-even = cosh = retained, bar-odd =
sinh = radiated) is a PLAUSIBLE hook, since bar-even/odd is exactly a
real/imaginary split. That is a LEAD, not a step. Do not present it as one.

## RELATION TO THE OTHER OPEN BEANS

  qou-mumr  -- catalogues that all existing metrics are ASSUMED (archimedean
               specialisation). This bean is the route to a derived one.
  qou-usft  -- blocked on the absence of a position-space density. A derived
               metric is the prerequisite.
  qou-7e67  -- ruling 3, "derive the archimedean identification", is THIS.
               The hyperbolic-volume -> Euclidean-length gap and the missing
               metric are the same gap.

## TRANSPORT PLANS, in detail (owner asked)

A transport plan pi is a JOINT distribution on pairs: pi(x,y) = how much mass
moves from x to y, constrained to respect both endpoints:

    Sum_y pi(x,y) = mu(x)      everything at x goes somewhere
    Sum_x pi(x,y) = nu(y)      everything arriving at y came from somewhere

In the finite case that is literally a NON-NEGATIVE MATRIX with prescribed row
and column sums.

  PRIMAL   W_1 = min over pi of Sum_{x,y} c(x,y) pi(x,y)
           -- minimise total MASS x DISTANCE. THIS is the aggregation: each plan
           aggregates every bit of mass against how far it travels; you take the
           cheapest plan.
  DUAL     W_1 = sup over f, Lip(f) <= 1, of [ Sum f mu - Sum f nu ]
           -- f is a PRICE. A broker collects at f(x), delivers at f(y);
           competition forces f(x)-f(y) <= c(x,y). Best revenue = least cost.

MONGE vs KANTOROVICH matters here. Monge demanded a MAP (each point goes to one
destination). Kantorovich allows mass to SPLIT across destinations, which is
what makes the problem convex and gives duality -- and splitting is exactly what
superposition needs.

Connes is that dual verbatim:  measures -> states, functions -> algebra
elements, Lip(f) <= 1 -> ||[D,a]|| <= 1.

### THE CAVEAT THAT DECIDES WHERE THIS FORMALIZATION LIVES

The DUAL is clean noncommutatively; the PRIMAL is NOT. A noncommutative
"coupling" needs a joint state on A (x) A with prescribed marginals, and quantum
optimal transport is an ACTIVE RESEARCH AREA with competing, non-equivalent
definitions (Carlen-Maas; De Palma-Trevisan; Golse-Mouhot-Paul). Do not assume a
primal exists just because the dual does.

=> THEREFORE: FORMALIZE IN THE FINITE / DISCRETE CASE, where the primal is a
   finite LP and the plan is an explicit matrix. Reeb steps suggest exactly that
   setting. A continuum or genuinely noncommutative attempt would import an
   unsettled research question as a dependency.

## MACHINERY VERIFIED (scratchpad/connes_demo.py, exact rational arithmetic)

5-cycle 0-1-2-3-4-0 with a chord 1-3. For all 10 vertex pairs:
    shortest path == Connes dual == transport primal.   ALL AGREE.
Weighted variant (edge (1,3) re-weighted 1 -> 3): the dual correctly reroutes,
reproducing the WEIGHTED shortest path (d(1,3) = 2 via vertex 2, not 3).

CONSEQUENCE, and it is the sharp question for QOU:

    "WHICH D" == "WHICH STEP COSTS".

The Dirac operator supplies the EDGE COSTS. So the open QOU question is not
"can we get a metric" -- the machinery demonstrably works -- but:

    what edge costs does the CATEGORICAL DIRAC OPERATOR
    D_grad = q^-1 grad + (1 - q^-1) iota_xi grad  actually supply,
    and are they the Reeb step costs?

## FORMALIZATION PLAN (finite case)

  [ ] 1. Extract the edge/hopping structure implied by the categorical Dirac
         operator. What are its matrix elements between adjacent states?
  [ ] 2. Identify the STATE SET. Reeb steps act on what, exactly? Fibre states?
         Knot types (the Ch 10 eigenbasis)? This must be pinned before any
         distance is well-posed.
  [ ] 3. Form the finite spectral triple (A, H, D) and compute d_Connes on it.
  [ ] 4. Compare to the Reeb step count. TARGET THEOREM:
             d_Connes(states) = minimal Reeb step count.
  [ ] 5. If it holds: Lean it, finite case first.
  [ ] 6. Only then ask whether it yields a position-space density (qou-usft).

  FALSIFIER, stated up front: if the categorical Dirac operator's hopping
  structure does not connect Reeb-adjacent states, or connects them with
  non-uniform costs that do not match the step count, the identification is
  FALSE and this bean should be closed negative rather than rescued.

## STEP 1 DONE — what the categorical Dirac operator actually supplies

Definition (categorical-dirac-operator.md):

    D_grad = q^-1 grad + (1 - q^-1) iota_xi grad  :  A -> Omega^1(A)

### FINDING 1 — it is a DERIVATION, not a spectral triple. Retarget.

D_grad maps A -> Omega^1(A). That is a first-order DIFFERENTIAL CALCULUS, NOT a
self-adjoint operator on a Hilbert space. A Connes spectral triple (A, H, D)
needs H and a self-adjoint D with [D,a] bounded on H. The corpus has no H.

But this is GOOD news, because in NCG the commutator [D,a] REPRESENTS the
differential "da" -- so D_grad is already playing the role of a |-> [D,a], i.e.
exactly the object the Lipschitz seminorm is built from:

    L(a) := || D_grad(a) ||_{Omega^1}
    d(phi,psi) = sup{ |phi(a) - psi(a)| : L(a) <= 1 }

=> THE RIGHT TARGET IS RIEFFEL'S COMPACT QUANTUM METRIC SPACE, not a Connes
   spectral triple. Rieffel's framework needs a Lip-NORM (a seminorm with
   Leibniz, kernel = scalars, and the right compactness), NOT a Hilbert space.
   It is strictly weaker and it is what the corpus already has. Retarget step 3
   of the plan accordingly: build the Lip-norm, not the triple.

### FINDING 2 — the Reeb coefficient IS hbar_q, identically

    coefficient on grad        q^-1      = 0.90091828395574149216
    coefficient on Reeb part  (1 - q^-1) = 0.099081716044258507839
    hbar_q = (q-1)/q                     = 0.099081716044258507839
    difference                             4.93e-32  (round-off at 30 dps)

(1 - 1/q) = (q-1)/q is an ALGEBRAIC IDENTITY, not a numerical coincidence. So
hbar_q is structurally THE REEB-DIRECTION WEIGHT IN THE DIRAC OPERATOR -- which
is precisely a step COST in the sense the transport picture needs. And the two
coefficients form a CONVEX COMBINATION summing to exactly 1:

    q = 1     -> pure grad (undeformed covariant derivative)
    q -> inf  -> pure Reeb (contact component)
    q0        -> 90.09 % grad + 9.908 % Reeb

### BEARING ON qou-adwi (the two incompatible Planck lengths)

This is structural support for the resolution hypothesised there -- that the two
values are DIFFERENT QUANTITIES, not contradictory values for one:

    hbar_q ~ 0.0991  = the REEB SHARE of the Dirac operator, i.e. a step cost
    ell_P  == 1      = the TOTAL, i.e. the normalising unit

and the coefficients summing to exactly 1 is the reason. Under a Lipschitz
normalisation L(a) <= 1 the unit is set by the whole operator, so a Reeb step
would carry cost proportional to hbar_q within a unit-normalised total.

STATED AS SUPPORT, NOT PROOF. I have shown the coefficients sum to 1 and that
ell_P == 1; I have NOT shown these are the same 1. Do not close qou-adwi on
this. It does, however, move the likely resolution from "one of them is wrong"
to "they are the share and the total".

### REVISED PLAN

  [x] 1. Extract the edge/hopping structure -- DONE. It is a derivation into
         1-forms with a q^-1 / hbar_q split between gradient and Reeb parts.
  [ ] 2. Identify the STATE SET (fibre states? the Ch 10 knot eigenbasis?).
         Still the blocking unknown -- no distance is well-posed without it.
  [ ] 3. RETARGETED: build the Rieffel LIP-NORM L(a) = ||D_grad a||, verify the
         Lip-norm axioms (Leibniz; kernel = scalars). NOT a spectral triple.
  [ ] 4. Compute d and compare to the Reeb step count.
  [ ] 5. Lean the finite case.
  [ ] 6. Only then ask about a position-space density.

  NEW SUB-QUESTION from Finding 2: because D_grad is a CONVEX COMBINATION of a
  gradient part and a Reeb part, the induced metric is NOT purely the Reeb step
  count -- it also sees the gradient direction, at 9x the weight. So the naive
  target "d_Connes = minimal Reeb step count" is probably WRONG as stated: it
  should be the Reeb count only in the q -> infinity limit, where D_grad ->
  iota_xi grad. At q0 the metric mixes both. Revise the target theorem before
  attempting it.

## Round 77 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8270 (`6053dcb4a4cd613867cf11286810e234a6e19f69`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/DeformedVolumeParityAndDiracReebConvexSplitBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/deformed_volume_parity_and_dirac_reeb_convex_split_brick_probe.py` (`scriptCommitSha: 9d5b1ea5cef1335474ac59e8528d4646769eddc6`) and `computations/probes/deformed-volume-parity-and-dirac-reeb-convex-split-brick.witness.json` (`allPassed: true`).

