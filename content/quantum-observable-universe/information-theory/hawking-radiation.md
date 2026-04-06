The jet horizon ([jet horizon](#def:jet-horizon)) provides an
algebraic model of the **event horizon** of a black hole.

**Hawking radiation** \cite{hawking1975} is the prediction that
a black hole is not perfectly black: it emits thermal radiation
at temperature $T_H = \hbar c^3 / (8\pi G M k_B)$.  The
radiation carries no information about the internal state of
the black hole — it is thermal, with a Planck spectrum
determined only by the mass $M$.

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
