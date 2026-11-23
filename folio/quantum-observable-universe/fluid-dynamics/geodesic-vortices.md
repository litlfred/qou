Geodesics of the [acoustic metric](#rem:madelung-fluid) exactly map to the critical points of the $q$-deformed energy functional evaluated over closed curves in the [state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$.

**The $q$-energy functional.**
For $\varrho \colon S^1 \to \mathcal{S}$:

$$
  \mathcal{E}_q[\varrho]
  = 
  \oint_\varrho
  \bigl(
    \tfrac{1}{2}\lVert\dot\varrho^H\rVert^2
    + Q_q(\varrho)
    + \lVert F_A(\dot\varrho)\rVert^2
  \bigr)ds,
$$

where $\dot\varrho^H$ specifies the horizontal velocity, $Q_q$ the [quantum pressure](#rem:madelung-fluid), and $F_A(\dot\varrho)$ the filament curvature.

**Critical points are geodesics.**
Evaluating $\delta\mathcal{E}_q / \delta\varrho = 0$ produces

$$
  \nabla_{\dot\varrho}\dot\varrho
  = -\nabla^\perp Q_q - \iota_{\dot\varrho}{*F_A}.
$$

As $q \to 1$, $Q_q \to 0$ and the gauge term simplifies into Biot--Savart self-induction (the classical Hasimoto soliton).

**Stability.**
The second variation $\delta^2\mathcal{E}_q$ resolves via the [weight-space decomposition](#def:weight-decomposition):

- **Longitudinal** (Cartan): Stable, carrying eigenvalues $[k]_q^2 \hbar_q / L_q^2$.
- **Ladder** ($E_\pm$): Protected by an energetic barrier $\Delta E = \hbar_q([j\!+\!1]_q[j\!+\!2]_q - [j]_q[j\!+\!1]_q)/(2I_q) > 0$ strictly when $q > 1$.
- **Gauge**: Trivially zero (quotiented out by symmetry).

**Index theorem.**
The Morse index of the fundamental vortex ($j = 1/2$) evaluates to zero: no subordinate energy state exists. The lightest fermion acts as the absolute minimum of $\mathcal{E}_q$ within its topological class.

**Connection to mass.**
$\mathcal{E}_q[\gamma_0] = \oint_{\gamma_0} \lVert\nabla_A q\rVert \cdot \lVert L \wedge F^+\rVert \propto m$ explicitly generates the [mass identity](#def:mass-identity). The static limit of $\mathcal{E}_q$ functions as the [geometric drag](#rem:geometric-drag).
