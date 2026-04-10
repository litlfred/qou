Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Planck time
$t_P(q) = q/(q-1) = 1/\hbar_q$
([Planck time](#def:planck-time)).  The **quantum temperature**
of a region $U \subset M$ is

$$
  T_q(U) \;:=\; \hbar_q \;=\; \frac{q - 1}{q},
$$

with inverse temperature $\beta_q := 1/T_q = t_P(q)$.

**Structural content.**
In classical statistical mechanics, temperature is defined
implicitly through the Boltzmann distribution
$\rho \propto e^{-\beta H}$, where $\beta = 1/(k_B T)$ is
a Lagrange multiplier enforcing energy conservation.  In the
QOU, $\beta_q$ has a direct operational meaning: it is the
**number of discrete Reeb operations** (Julia set iterations
$f_q$ on the exceptional divisor) that compose one macroscopic
time unit.  Temperature is not a statistical average over
kinetic energies — it is the **tick rate** of the quantum
substrate.

**Surface integral realisation (non-abelian Stokes).**
The entropy of a region $U$ with boundary $\partial U$ is
an integral over the boundary, not the bulk.  Let
$\mathcal{F} = \mathrm{Ad}(A)$ be the adjoint bundle and
$\Omega_{\mathcal{F}}$ its curvature 2-form.  The
measurability condition $c_1(\mathcal{F}) = 0$
([quantum observable universe](#def:quantum-observable-universe))
ensures that $\Omega_{\mathcal{F}}$ is exact in non-abelian
cohomology.  By the Yekutieli non-abelian Stokes theorem
([Yekutieli triple](#def:yekutieli-triple)), for any
2-chain $\Sigma$ bounding a loop $\gamma$ in $U$:

$$
  \mathrm{Hol}_{\mathcal{F}}(\gamma)
  \;=\; \mathcal{P}\exp\!\oint_\gamma \omega_{\mathcal{F}}
  \;=\; \mathcal{P}\exp\!\iint_\Sigma \Omega_{\mathcal{F}},
$$

where $\mathcal{P}\exp$ denotes the path-ordered exponential
and $\omega_{\mathcal{F}}$ is the adjoint connection.  The
flatness condition ($c_1 = 0$, $c_2 = 0$) makes this
independent of the choice of $\Sigma$ — the entropy
is a **boundary datum**.

The quantum entropy of $U$ is then

$$
  S_q(U) \;=\; -\,\mathrm{tr}_{\mathrm{Ad}}
  \!\oint_{\partial U}
  \omega_{\mathcal{F}} \,\wedge\, *\eta_q,
$$

where $\eta_q = (2q-1)/q^3$ is the operational entropy
density ([operational entropy](#def:operational-entropy))
and $*$ is the Hodge star on $\partial U$.  The quantum
temperature is the thermodynamic conjugate:

$$
  \frac{1}{T_q}
  \;=\; \frac{\partial S_q}{\partial \mathbf{E}_q}\bigg|_V
  \;=\; \frac{1}{\hbar_q}.
$$

**Why temperature is a surface quantity.**
The Frobenius pairing
$\langle\,\cdot\,,\,\cdot\,\rangle_A : A \otimes A \to \mathbf{1}$
([Frobenius pairing](#def:frobenius-pairing)) is non-degenerate,
so internal degrees of freedom are fully determined by boundary
data via the categorical trace.  This is the content-object
version of the holographic principle: the number of
distinguishable states in $U$ is controlled by $\partial U$,
not by $U$ itself.  Temperature, as the derivative of entropy
with respect to energy, inherits this boundary character.

**Classical limit.**
As $q \to 1$: $T_q \to 0$, $\beta_q \to \infty$, and
$S_q(U) \to S_{\mathrm{classical}}(U)$.  The non-abelian
Stokes integral degenerates to the classical Gauss law,
and the Frobenius trace becomes the ordinary matrix trace.
The Boltzmann constant emerges as
$k_B = \hbar_q / T_{\mathrm{phys}}$ in the correspondence
limit where physical temperature $T_{\mathrm{phys}}$ is
measured in SI units.
