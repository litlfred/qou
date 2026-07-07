<!-- FILE_START: physical-elaborations-intro.md -->
The deformed operators of the previous sections have
direct physical readings; we collect the four that the rest of
the paper will refer back to. Remark: $q$-torsion leaves as $q$-curvature minima characterises a $q$-torsion leaf as a local
minimum of $\lVert \Omega_q \rVert$ restricted to the horizontal
distribution, with the leaf trapped in a $q$-curvature well by
Reeb-flow invariance. Remark: Physical meaning of $q$-harmonic forms refers back to the Reeb-decomposition reading: a
$q$-harmonic form is itself $q$-dependent and interpolates
between the Hodge Laplacian's classical harmonic forms and the
deep-quantum regime. Remark: Linearisation convention fixes
the identification of $i$ in the Schrödinger equation with the
CR complex structure $J$ on the Levi distribution and records
that the curved fibre $\mathbb{P}^1(\mathbb{C})$ of $\mathcal{S}$
is linearised by stereographic projection at a base section to
write a linear PDE for $\psi$. Remark: Schrödinger equation from jet coaction writes $J \hbar_q(p) \iota_{\xi_q} D_A \psi =
\hat{H}_q \psi$ as the bottom row of the main commutative
diagram — the $q$-deformed Schrödinger evolution on the
linearised state bundle, with $\hbar_q(p) = 1 - q(p)^{-1}$
a local field and $\hat{H}_q$ the $q$-deformed Hamiltonian.

_(draft.)_
<!-- FILE_END: physical-elaborations-intro.md -->

<!-- FILE_START: q-torsion-leaf-minimum.md -->
Let $A_q$ denote the $q$-deformed connection
([$q$-connection](#ex:q-connection)) and define the $q$-curvature

$$
  \Omega_q =  dA_q + \tfrac{1}{2}[A_q, A_q]_q,
$$

where $[\cdot,\cdot]_q$ is the $q$-deformed Lie bracket
([$q$-Lie bracket](#ex:q-lie-bracket)) extended to $\mathrm{Ad}(P)$-valued
forms. A $q$-torsion leaf $L$ ([$q$-torsion leaf](#ex:q-torsion-leaf)) is a
local minimum of $\lVert\Omega_q\rVert$ restricted to the horizontal
distribution: the invariance of $L$ under $\phi_t^q$ forces the first
variation of $\lVert\Omega_q|_L\rVert$ to vanish, so $L$ sits in a
$q$-curvature well. Physically, a $q$-torsion leaf represents a region of
the CR manifold where the gauge curvature is minimised and the $q$-deformed
dynamics are in equilibrium.
<!-- FILE_END: q-torsion-leaf-minimum.md -->

<!-- FILE_START: q-harmonic-physical.md -->
See [Reeb physical interpretation](#rem:reeb-physical) for the physical interpretation of
$q$-harmonic forms and the Reeb decomposition. In brief: the
$q$-Laplacian $\Delta_q$ interpolates between the Hodge Laplacian
($q = 1$) and the deep-quantum regime ($q \to \infty$), so a
$q$-harmonic form --- a "particle" --- is itself $q$-dependent.
<!-- FILE_END: q-harmonic-physical.md -->

<!-- FILE_START: linearisation-convention.md -->
Throughout this paper the symbol $i$ in the Schrödinger equation is
identified with the complex structure operator
$J \colon H \to H$ on the Levi distribution ($J^2 = -\mathrm{Id}$):
it acts as a geometric twisting operator on horizontal planes rather
than as an algebraic imaginary unit. This identification is canonical
on any CR manifold of hypersurface type
([archimedean quantum universe](#ex:c-quantum-universe)).

The fibre $\mathbb{P}^1(\mathbb{C})$ of the state bundle $\mathcal{S}$ is a
non-linear space, so we cannot write a linear PDE for sections of
$\mathcal{S}$ directly. We work instead with the *linearised* model: identify
a neighbourhood of a base-point in $\mathbb{P}^1(\mathbb{C})$ with
$\mathbb{C}$ via stereographic projection, and interpret $\psi$ as a
section of the line bundle $\mathcal{S}_{\mathrm{lin}}$ obtained by linearising
$\mathcal{S}$ at the chosen section. The covariant derivative
$D_A = d + A$ then acts on sections of this line bundle in the
standard way.
<!-- FILE_END: linearisation-convention.md -->

<!-- FILE_START: schrodinger-jet-coaction.md -->
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
<!-- FILE_END: schrodinger-jet-coaction.md -->

<!-- FILE_START: outro-quantum-observable-universes.md -->
This closes the Quantum Observable Universe chapter.  The
categorical setup of Chapter 1 has been promoted to its observable
form: the substrate parameter $q$ controls the
$\mathbb{G}_m$-family of differentials, the Reeb derivation $\xi$
sits as the canonical one-parameter vector field on the gauge
group $\mathrm{SU}_q(2)$, and the $q$-resolvent / $q$-special
functions assemble the spectral pairing
$(\exp_q, \log_q, \mathrm{Li}_2^q)$ that the next chapters consume.

The next chapter (lifting and descent) builds the brane tower
$\{A_n\}_{n \geq 0}$ from the QOU data assembled here: each level
$A_n$ inherits the full QOU structure (substrate parameter,
Reeb derivation, special functions) and lifts it one categorical
level up the tower.  The categorical-jet-coaction closing remark
in the elaborations section is the substrate-level prototype of
the Yekutieli cocycle data that the next chapter formalises.
<!-- FILE_END: outro-quantum-observable-universes.md -->

