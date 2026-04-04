A stable vortex filament in the brane fluid is not merely an analogy
for a particle — it **is** one.  The precise claim is that geodesics
of the [acoustic metric](#rem:madelung-fluid) coincide with critical
points of a $q$-deformed energy functional on the space of closed
curves in the [state bundle](#def:state-bundle) $\mathcal{S}$.

**The $q$-energy functional.**
Let $\gamma \colon S^1 \to \mathcal{S}$ be a closed curve in the
state bundle, representing a candidate vortex filament.  Define the
$q$-deformed energy

$$
  \mathcal{E}_q[\gamma]
  \;=\;
  \oint_\gamma
  \Bigl(
    \tfrac{1}{2}\,\lVert\dot\gamma^H\rVert^2
    \;+\; Q_q(\gamma)
    \;+\; \lVert F_A(\dot\gamma)\rVert^2
  \Bigr)\,ds,
$$

where $\dot\gamma^H$ is the horizontal (spatial) component of the
velocity, $Q_q$ is the [quantum pressure](#rem:madelung-fluid), and
$F_A(\dot\gamma)$ is the curvature evaluated along the filament.
The three terms have distinct physical roles:

| Term | Controls | Classical limit ($q \to 1$) |
|---|---|---|
| $\frac{1}{2}\lVert\dot\gamma^H\rVert^2$ | Kinetic energy of filament motion | Biot--Savart self-induction |
| $Q_q(\gamma)$ | Quantum pressure resisting compression | Vanishes ($Q_1 = 0$) |
| $\lVert F_A(\dot\gamma)\rVert^2$ | Gauge-field energy stored in the filament | Yang--Mills action density |

**Critical points are geodesics.**
The Euler--Lagrange equation $\delta\mathcal{E}_q / \delta\gamma = 0$
yields the geodesic equation on $(\mathcal{S}, g_{\mathrm{ac}})$
with an effective potential from the quantum pressure:

$$
  \nabla_{\dot\gamma}\dot\gamma
  \;=\;
  -\nabla^\perp Q_q
  \;-\; \iota_{\dot\gamma}\,{*F_A},
$$

where $\nabla^\perp$ is the normal gradient to the filament and
$\iota_{\dot\gamma}\,{*F_A}$ is the Lorentz-type force from the
gauge curvature.  In the classical limit $q \to 1$, the quantum
pressure vanishes and the gauge contribution reduces to the
Biot--Savart law: the filament moves by local self-induction, as
in the Hasimoto soliton.

**Stability analysis.**
A critical point $\gamma_0$ is a stable vortex if the second
variation $\delta^2\mathcal{E}_q[\gamma_0]$ is positive-definite on
normal perturbations.  The second variation decomposes via the
[weight-space decomposition](#def:adjoint-weight-decomposition) of
the adjoint bundle:

- **Longitudinal modes** (Cartan subalgebra): these are the stable
  directions.  Perturbations along the Cartan weight decay
  exponentially, governed by the real part of the $q$-deformed
  stability eigenvalues $\lambda_k^{(q)} = [k]_q^2 \cdot
  \hbar_q / L_q^2$.  These are the [discrete vortex
  modes](#prop:discrete-vortex-spectrum).

- **Ladder modes** ($E_\pm$): these are the potentially unstable
  directions.  A ladder perturbation connects intensity level $j$
  to $j \pm 1$, with energy barrier
  $\Delta E = \hbar_q \cdot ([j+1]_q[j+2]_q - [j]_q[j+1]_q)
  / (2I_q)$.  For $q > 1$, this barrier is strictly positive,
  ensuring discrete jumps rather than continuous drift.

- **Gauge modes** ($F_A$-direction): pure gauge perturbations are
  quotient out by the gauge symmetry; they correspond to the
  internal colour degree of freedom and do not affect stability.

**Index theorem.**
The Morse index of a critical vortex $\gamma_0$ — the number of
negative eigenvalues of $\delta^2\mathcal{E}_q$ — equals the
number of conjugate points along the geodesic, which in turn
equals the number of ladder transitions that lower energy.  For
the fundamental vortex ($j = \frac{1}{2}$), the index is zero:
there is no lower state, and the vortex is an absolute minimum of
$\mathcal{E}_q$ in its topological class.  This is the variational
proof that the lightest fermion is stable.

**Connection to mass.**
The value of $\mathcal{E}_q$ at a critical point reproduces the
[mass identity](#def:mass-identity):

$$
  \mathcal{E}_q[\gamma_0]
  \;=\;
  \oint_{\gamma_0}
  \lVert\nabla_A q\rVert \cdot
  \lVert L \wedge F^+\rVert
  \;\propto\; m,
$$

confirming that the [geometric drag](#rem:geometric-drag) — mass as
resistance to vortex propagation through the jet bundle — is
the static limit of the $q$-energy functional.
