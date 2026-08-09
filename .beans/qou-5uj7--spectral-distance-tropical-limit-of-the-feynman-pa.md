---
# qou-5uj7
title: 'Spectral distance = tropical limit of the Feynman path sum: formalize d_Connes = minimal Reeb step count'
status: todo
type: task
created_at: 2026-08-09T12:04:33Z
updated_at: 2026-08-09T12:04:33Z
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
      content/quantum-observable-universe/braids-and-knots/feynman-eigenbasis.md
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
