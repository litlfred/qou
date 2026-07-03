The jet horizon ([jet horizon](#def:jet-horizon)) provides an
algebraic model of the **event horizon** of a black hole.

**Hawking radiation** \cite{hawking1975} is the prediction that
a black hole is not perfectly black: it emits thermal radiation
at temperature $T_H = \hbar c^3 / (8\pi G M k_B)$.

In general terms, the effect is a statement about the restriction of a
global state to an exterior subalgebra.  The in-vacuum (regular across
the horizon) and the out-modes of a late-time exterior observer are
related by a Bogoliubov transformation with non-vanishing
mixing coefficients; consequently the global vacuum, *restricted to
the exterior algebra*, is not a pure vacuum but a thermal (KMS) state
with respect to the horizon boost flow, with Planck spectrum at $T_H$
determined only by the mass $M$ (and charge and spin).  The leading-order
radiation therefore carries no record of individual infallen states:
information-freeness is a property of the exterior *marginal*, not of
the global evolution, which remains unitary.

In the jet-horizon framework, this has a direct algebraic
interpretation:

1. **Degree-$0$ data is trapped.**  The horizon ideal
   $\mathfrak{h} \subset A_0$ blocks all zeroth-order
   sections.  No particle identity (knot type, crossing
   structure) crosses the horizon.  This is the
   **information paradox** stated algebraically: the full
   fibre data of $A_0$ is inaccessible from outside.

2. **Degree $\geq 1$ data leaks.**  The quotients
   $A_1/A_0$ and $A_2/A_0$ carry non-trivial sections
   across $\mathcal{H}$.  These are the first and second
   Taylor coefficients of the energy function — linear
   transport (winding number) and curvature (linking
   number).  This data is **thermal**: it depends on
   statistical properties (temperature $\sim \eta_q$,
   operational entropy
   ([operational entropy](#def:operational-entropy)))
   rather than individual particle states.

3. **The Bekenstein--Hawking entropy** \cite{bekenstein1973}
   $S = A / (4\ell_P^2)$ counts the number of independent
   degree $\geq 1$ sections on the horizon surface
   $\mathcal{H}$.  In the QOU framework, the area $A$ is
   the rank of $\Gamma(\mathcal{H}, A_1/A_0)$ — the
   dimension of the space of first-order jet data that the
   horizon can carry.

4. **No photons escape.**  Photons are degree-$0$ objects
   ($K = \varnothing$, step $0$ in the jet-Planck
   correspondence
   ([jet-Planck steps](#rem:jet-planck-steps))).  They
   are blocked by the horizon ideal along with all other
   degree-$0$ data.  What an external observer detects as
   "thermal photons" are degree-$1$ winding modes that
   have no knot identity — they are the Hawking quanta.

**The correspondence, stated at the level of the filtration.**  The
dictionary between the general definition and the jet-horizon model is
exact once both sides are read as filtration statements — the jet
filtration $A_0 \subset A_1 \subset \cdots$ on the bundle side, the
Gröbner--Shirshov leading-term filtration on the Hecke-algebra side:

| General (semiclassical) | QOU (filtration) |
|---|---|
| global vacuum, entangled across the horizon | the single Markov-trace GNS state on the full filtered algebra |
| event horizon | the vanishing locus $V(\mathfrak{h})$ of degree-$0$ sections — the truncation locus of the filtration |
| Bogoliubov mixing of in/out modes | the evolution is filtered-unitary but not graded-diagonal: it shifts filtration degree, so interior degree-$0$ identity re-enters the exterior as degree-$\geq 1$ graded data |
| exterior marginal is thermal (KMS) at $T_H$ | the compression of the GNS state to the degree-$0$ exterior observables retains only statistical data (temperature $\sim \eta_q$); individual knot identity does not survive the compression |
| Hawking quanta | sections of $A_1/A_0$ — degree-$1$ winding modes without knot identity |
| spectrum depends only on $M$ | the leaked graded data is determined by the Markov-trace value (the mass), not by the trapped degree-$0$ sections |

In this reading, "the radiation carries no information" is a statement
about the degree-$0$ observable marginal only.  Whether the *full*
accumulated graded record determines the trapped degree-$0$ data is
exactly the witness-completeness question
([witness completeness](#conj:witness-completeness)).
