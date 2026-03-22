The $q$-deformed Schrodinger equation governs the evolution of states
in the linearised state bundle. Throughout this paper the symbol $i$ in
the Schrodinger equation is identified with the complex structure
operator $J \colon H \to H$ on the Levi distribution ($J^2 = -\mathrm{Id}$):
it acts as a geometric twisting operator on horizontal planes rather than
as an algebraic imaginary unit.

*Linearisation convention.*
The fibre $\mathbb{P}^1(\mathbb{C})$ is a non-linear space, so one cannot write a
linear PDE for sections of $E$ directly. We work instead with the
*linearised* model: identify a neighbourhood of a base-point in
$\mathbb{P}^1(\mathbb{C})$ with $\mathbb{C}$ via stereographic projection, and
interpret $\psi$ as a section of the line bundle $E_{\mathrm{lin}}$
obtained by linearising $E$ at the chosen section. The covariant
derivative $D_A = d + A$ then acts on sections of this line bundle in the
standard way.

For a section $\psi \in \Gamma(E_{\mathrm{lin}})$ and the $q$-deformed Reeb
vector field $\xi_q$ ([$q$-Reeb vector field](#def:q-reeb-vector-field)), the
Schrodinger dynamics take the form

$$
  J\,\hbar_q(p)\,\iota_{\xi_q} D_A \psi \;=\; \hat{H}_q\, \psi,
$$

where $\hat{H}_q = -\tfrac{1}{2}\hbar_q\,\Delta_q + V_q$ is the
*$q$-deformed Hamiltonian* (here $\Delta_q$ is the $q$-Laplacian of
[$q$-harmonic form](#def:q-harmonic-form) acting on sections of
$E_{\mathrm{lin}}$, and $V_q$ is a potential depending on the curvature
$\Omega_q$), and:

- $\hbar_q(p) = 1 - q(p)^{-1}$: the
([quantum planck constant](#def:quantum-planck-constant)) is a local field;
- $D_A = d + A$: the instanton connection on $P$ acts as the potential;
- $\iota_{\xi_q} D_A \psi$: the covariant derivative $D_A\psi$ is an
  $E_{\mathrm{lin}}$-valued $1$-form; contracting it with $\xi_q$
  yields a section of $E_{\mathrm{lin}}$, matching the right-hand side.

As $q(p) \to 1$ (classicality), the commutator
$[\hat{X}, \hat{P}]_q \to 0$ ([Heisenberg commutator](#rem:heisenberg-commutator)), the
uncertainty vanishes, and the wave-like nature of the section freezes into a
classical trajectory.

*Categorical role.*
Although this remark is stated as a PDE rather than in categorical language,
it is essential to the paper's structure: the Schrodinger equation
provides the bottom row of the
([main commutative diagram](#prop:main-commutative-diagram)). Categorically, the
$q$-deformed Hamiltonian $\hat{H}_q$ defines an endomorphism of the
module category $\mathrm{Mod}_{E_{\mathrm{lin}}}$ over the jet algebra
$\Gamma(J^1 E)$, and the Schrodinger equation is the condition that
$\psi$ lies in the kernel of $\hat{H}_q - J\hbar_q\,\iota_{\xi_q}D_A$.
In the base-field-independent setting of
[quantum universe](#def:quantum-universe)
and [](#def:quantum-observable-universe), this extends to arbitrary base
rings $R$ by replacing $\Gamma(E_{\mathrm{lin}})$ with the appropriate
$R$-linear category of sections.
