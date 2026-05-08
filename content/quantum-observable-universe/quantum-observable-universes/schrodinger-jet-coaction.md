The $q$-deformed Schrödinger equation governs the evolution of states
in the linearised state bundle
([linearisation convention](#sec:linearisation-convention)).

For a section $\psi \in \Gamma(\mathcal{S}_{\mathrm{lin}})$ and the $q$-deformed Reeb
vector field $\xi_q$ ([$q$-Reeb vector field](#ex:q-reeb-vector-field)), the
Schrödinger dynamics take the form

$$
  J\hbar_q(p)\iota_{\xi_q} D_A \psi =  \hat{H}_q \psi,
$$

where $\hat{H}_q = -\tfrac{1}{2}\hbar_q\Delta_q + V_q$ is the
*$q$-deformed Hamiltonian* (here $\Delta_q$ is the $q$-Laplacian of
[$q$-harmonic form](#def:q-harmonic-form) acting on sections of
$\mathcal{S}_{\mathrm{lin}}$, and $V_q$ is a potential depending on the curvature
$\Omega_q$), and:

- $\hbar_q(p) = 1 - q(p)^{-1}$: the
([quantum Planck constant](#def:quantum-planck-constant)) is a local field;
- $D_A = d + A$: the instanton connection on $P$ acts as the potential;
- $\iota_{\xi_q} D_A \psi$: the covariant derivative $D_A\psi$ is an
  $\mathcal{S}_{\mathrm{lin}}$-valued $1$-form; contracting it with $\xi_q$
  yields a section of $\mathcal{S}_{\mathrm{lin}}$, matching the right-hand side.

As $q(p) \to 1$ (classicality), the commutator
$[\hat{X}, \hat{P}]_q \to 0$ ([Heisenberg commutator](#rem:heisenberg-commutator)), the
uncertainty vanishes, and the wave-like nature of the section freezes into a
classical trajectory.

This equation provides the bottom row of the
([main commutative diagram](#prop:main-commutative-diagram)).
