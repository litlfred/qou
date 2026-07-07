<!-- FILE_START: q-deformed-operators-intro.md -->
The categorical $q$-deformed operators of the previous
section live abstractly on $\Omega^\bullet(A)$; we now specialise
them to a concrete CR manifold $M$ and read the resulting
formulas in classical differential-geometric language. Each operator inherits a uniform interpolation pattern
$q^{-1}(\text{classical}) + (1 - q^{-1})(\text{Reeb correction})$.

Example: $q$-deformed exterior derivative writes $d_q = q^{-1}d
+ (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi$ on $\Omega^k(M)$
and reads off the archimedean $d_q^2 = q^{-1}(1-q^{-1})
d\varTheta \wedge \mathcal{L}_\xi$. Example: $q$-deformed Lie bracket writes $[V, W]_q = q^{-1}[V, W] + (1 - q^{-1})(\varTheta(V)
\mathcal{L}_\xi W - \varTheta(W)\mathcal{L}_\xi V)$ on
$\mathfrak{X}(M)$. Example: $q$-deformed connection gives
$A_q = q^{-1}A + (1 - q^{-1})\iota_\xi A \varTheta$ on
sections of the gauge bundle. Example: $q$-deformed Reeb vector field acts on $C^\infty(M)$ by $\xi_q(f) = q^{-1}\xi(f) +
(1 - q^{-1})[\xi, X_f]_q$, with $X_f$ the horizontal lift of
$\mathrm{grad}_{g_\varTheta} f$.

Example: $q$-deformed Reeb flow integrates $\xi_q$ to the
one-parameter family $\phi_t^q \colon M \to M$. Example: $q$-torsion leaf names the maximal integral submanifolds of the
horizontal distribution $H = \ker\varTheta$ invariant under
$\phi_t^q$; Remark: Existence of $q$-torsion leaves explains
why they are Legendrian (the Levi form forces the dimension
bound) and notes the KAM-type subtleties for $q > 1$.
Remark: $\mathrm{SU}(2)$ action as quantum torsion closes the
section by recasting the substrate parameter as a torsion index
on the categorical algebra itself: $q$ measures the failure of
the algebra of states to commute, and the spinor sign rule
emerges as the $720°$ unwinding of this twist. The next
section, **$q$-Harmonic analysis: heat equation, Laplace,
Fourier**, takes these operators and builds the spectral
analysis on top of them.

_(draft.)_
<!-- FILE_END: q-deformed-operators-intro.md -->

<!-- FILE_START: q-ext-deriv.md -->
In the archimedean realisation, the categorical $d_q$
([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)) specialises to
$d_q \colon \Omega^k(M) \to \Omega^{k+1}(M)$:

$$
  d_q\alpha
  = q^{-1}d\alpha
        + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi\alpha.
$$

The vertical projection $\pi_V \circ d$ becomes
$\varTheta \wedge \mathcal{L}_\xi$ via the
([Reeb decomposition](#ex:reeb-decomposition)), and
$d_q^2 = q^{-1}(1-q^{-1})d\varTheta \wedge \mathcal{L}_\xi$
([categorical $d_q^2 = 0$](#prop:categorical-dq-squared)) specialises via
$\omega_V = d\varTheta$.
<!-- FILE_END: q-ext-deriv.md -->

<!-- FILE_START: q-lie-bracket.md -->
In the archimedean realisation, the categorical Reeb derivation
([categorical Reeb derivation](#def:categorical-reeb)) induces the *$q$-deformed
Lie bracket* on smooth vector fields $V, W \in \mathfrak{X}(M)$:

$$
  [V, W]_q
  = q^{-1}[V, W]
        + (1 - q^{-1})\bigl(\varTheta(V)\mathcal{L}_\xi W
                              - \varTheta(W)\mathcal{L}_\xi V\bigr).
$$
<!-- FILE_END: q-lie-bracket.md -->

<!-- FILE_START: q-connection.md -->
In the archimedean realisation, the categorical $q$-connection
([categorical $q$-connection](#def:categorical-q-connection)) specialises
to $A_q = q^{-1}A + (1 - q^{-1})\iota_\xiA\varTheta$,
where $q$ is the substrate parameter
([substrate parameter](#def:substrate-parameter)).
At $q = 1$ this recovers the full instanton connection $A$; as
$q \to \infty$, the connection reduces to its Reeb component
$\iota_\xi A\varTheta$, retaining only the vertical (internal spin)
part of the gauge potential.
<!-- FILE_END: q-connection.md -->

<!-- FILE_START: q-reeb-vector-field.md -->
The categorical Reeb derivation $\xi$
([categorical Reeb derivation](#def:categorical-reeb)) deforms in the archimedean
setting to $\xi_q$, acting on smooth functions $f \in C^\infty(M)$ by

$$
  \xi_q(f) =  q^{-1}\xi(f) + (1 - q^{-1})[\xi, X_f]_q,
$$

where $X_f$ is the horizontal lift of $\mathrm{grad}_{g_\varTheta}f$ to
$H = \ker\varTheta$ and $[\cdot,\cdot]_q$ is the $q$-deformed Lie
bracket ([$q$-Lie bracket](#ex:q-lie-bracket)).
<!-- FILE_END: q-reeb-vector-field.md -->

<!-- FILE_START: q-reeb-flow.md -->
In the archimedean realisation, the categorical $q$-Reeb derivation
([categorical $q$-Reeb flow](#def:categorical-q-reeb-flow)) specialises to
the $q$-deformed Reeb vector field $\xi_q$
([$q$-Reeb vector field](#ex:q-reeb-vector-field)), which generates a
one-parameter family of diffeomorphisms
$\phi_t^q \colon M \to M$, $t \in \mathbb{R}$:

$$
  \frac{d}{dt}\phi_t^q =  \xi_q \circ \phi_t^q,
  \qquad \phi_0^q = \mathrm{id}_M.
$$
<!-- FILE_END: q-reeb-flow.md -->

<!-- FILE_START: q-torsion-leaf.md -->
Let $H = \ker\varTheta \subset TM$ be the horizontal distribution on the
CR manifold $M$.  A *$q$-torsion leaf* is a maximal integral
submanifold $L \hookrightarrow M$ of $H$ that is invariant under the
$q$-deformed Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)):

$$
  T_p L \subset H_p
  \quad\text{for all } p \in L,
  \qquad\text{and}\qquad
  \phi_t^q(L) = L
  \quad\text{for all } t \in \mathbb{R}.
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-torsion-leaf.md -->

<!-- FILE_START: q-torsion-existence.md -->
The horizontal distribution $H = \ker\varTheta$ on a contact manifold is
maximally non-integrable: $d\varTheta|_{H \times H}$ is non-degenerate.
By the Frobenius theorem, maximal integral submanifolds of $H$ have
dimension at most $n$ (half the rank of $H$); these are the
*Legendrian submanifolds*.  [$q$-torsion leaf](#ex:q-torsion-leaf)
therefore requires $L$ to be a Legendrian submanifold invariant under the
$q$-deformed Reeb flow.

Existence is not automatic: it depends on the dynamics of $\xi_q$.
When $q \to 1$ and $\xi_q \to \xi$, invariant Legendrian submanifolds
exist whenever the Reeb flow is periodic or integrable (e.g. on
$S^3/\Gamma$).  For $q > 1$, the deformation generically breaks
periodicity, and one must appeal to KAM-type persistence results.

In the category of Lie algebroids over $M$, the Frobenius integrability
condition is equivalent to $H$ carrying a Frobenius structure
([quantum universe](#def:quantum-universe)).  Since the Levi form
$d\varTheta|_{H \times H}$ is non-degenerate, this Frobenius structure
*fails* --- and it is precisely this failure that forces the
dimension bound on integral submanifolds and gives $q$-torsion leaves
their rigidity.
<!-- FILE_END: q-torsion-existence.md -->

<!-- FILE_START: quantum-torsion-motivation.md -->
In classical differential geometry, torsion measures the failure of
infinitesimal parallelograms to close: transport a vector around a
small loop, and the gap between its starting and ending positions is
the torsion of the connection. In the categorical framework developed
here, a parallel phenomenon appears at the algebraic level, and its
source is the $\mathrm{SU}(2)$ action itself.

The $\mathrm{SU}(2)$ action on the Frobenius–Hopf object $A$ is not a
symmetry being passively twisted by an ambient manifold — it *is* the
twist. Every $\mathrm{SU}(2)$ representation (every particle state)
introduces a topological torsion into the categorical substrate. This
is the content of **quantum torsion**: the non-commutativity of the
algebra of states, measured by the $q$-deformation.

The distinction is sharp:

1. **Classical torsion** ($\nabla$): space-time fails to close a
 parallelogram — a defect in the connection on the tangent bundle.

2. **Quantum torsion** ($\mathrm{SU}_q(2)$): the algebra of states
 fails to commute — a defect baked into the algebraic operations
 themselves.

The substrate parameter $q$ therefore serves as a **torsion index**.
When $q = 1$, the quantum torsion vanishes: the $\mathrm{SU}(2)$
action is perfectly smooth and the algebra is commutative. As $q$
departs from $1$, the quantum torsion increases — the non-commutativity
tightens the algebraic structure, forcing the $q$-deformed Reeb flow
and its invariant leaves ([q-torsion leaf](#ex:q-torsion-leaf)) into
progressively more rigid configurations.

This perspective also explains the spinor sign rule. A spinor requires
a $720°$ rotation to return to its initial state. In the quantum
torsion picture, the first $360°$ is the physical rotation of the state
in space; the second $360°$ is the **quantum torsion reset** — the
unwinding of the twist that the $\mathrm{SU}(2)$ action has placed on
the vortex-tube fibre of the state bundle $\mathcal{S}$. The double
cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ is thus not only a
topological accident but a direct manifestation of the quantum torsion
carried by fermionic states.
<!-- FILE_END: quantum-torsion-motivation.md -->

