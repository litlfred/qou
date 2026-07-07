<!-- FILE_START: geometric-interpretations-intro.md -->
The categorical $d_q$, $\delta_q$, $\Delta_q$, and
the fermion--boson decomposition are now in hand; we read them
through the dictionary of classical vector calculus to make their
geometric content visible to a reader more comfortable with
$\mathbb{R}^3$ than with rigid monoidal categories.

Remark: Differential forms and the classical vector calculus operators recalls the bridge: $df$ as gradient,
$d\alpha$ as curl, $\delta$ as $-\mathrm{div}$, and $\Delta =
d\delta + \delta d$ as the Hodge Laplacian. Remark: Quantum-twisted neighbourhoods and the $q$-Laplacian reads $\Delta_q
\alpha = 0$ as the statement that $\alpha$ has found
equilibrium between its spatial environment and its internal
quantum spin, with $q$ tuning the relative weight.
Proposition: Closed form of $\delta_q$ and its archimedean
specialisation (rem) deliver the adjoint formula $\delta_q =
q^{-1}\delta + (1-q^{-1}) \mathcal{L}_\xi^* \circ \iota_\xi$. Remark: Three-term expansion of the $q$-Laplacian decomposes $\Delta_q = q^{-2}\Delta
+ q^{-1}(1-q^{-1})[\text{Coriolis}] + (1-q^{-1})^2 \Delta_\xi$
into classical diffusion, Coriolis cross-coupling, and pure
spin diffusion.

Remark: Self-adjointness of $\Delta_q$ and Remark: A particle is a $q$-harmonic form make the equivalence $\Delta_q
\alpha = 0 \Leftrightarrow d_q \alpha = 0$ and $\delta_q
\alpha = 0$ explicit: a particle is simultaneously $q$-closed
and $q$-coclosed. Remark: A concrete geometric realisation
refers ahead to a later chapter: on a suitable genus-$4$
curve, $\xi$, $\varTheta$, and $q$ are explicit formulas and
the boson--fermion split becomes a Hodge decomposition of the
harmonic space.
Remark: Complex substrate parameter and the observability constraint records what changes if $q$ is allowed to
acquire a phase: the imaginary part of $\hbar_q$ destroys
positivity of the Haar functional and so is excluded by the
observability axiom, but the algebraic sector ($q$ a root of
unity, modular tensor categories) remains internally
consistent. The next section, **Categorical instanton and
self-duality**, returns to the connection $\nabla$ and the
$q$-Hodge star $\star_q$ to read the gauge sector of the
action.

_(draft.)_
<!-- FILE_END: geometric-interpretations-intro.md -->

<!-- FILE_START: vector-calculus-bridge.md -->
For readers more familiar with vector calculus than differential
geometry, we briefly recall how the classical operators appear in the
language of differential forms on a smooth Riemannian manifold
$(M, g)$.

**Forms by degree.** A $0$-form is a scalar field $f \colon M \to \mathbb{R}$ (temperature, electrostatic potential). A $1$-form
$\alpha$ assigns to each tangent vector a number — it is the
geometric version of a vector field (velocity, force, the gradient
of a potential). A $2$-form $\beta$ measures oriented flux through
an infinitesimal parallelogram (magnetic field strength, vorticity).

**The exterior derivative $d$.**
- On a $0$-form: $df$ is the *gradient*. In coordinates,
  $df = \partial_i f dx^i$.
- On a $1$-form: $d\alpha$ is the *curl*. If
  $\alpha = Pdx + Qdy + Rdz$ in $\mathbb{R}^3$, then
  $d\alpha = (\partial_y R - \partial_z Q)dy \wedge dz + \cdots$
- The identity $d^2 = 0$ encodes both $\nabla \times (\nabla f) = 0$
  and $\nabla \cdot (\nabla \times \mathbf{F}) = 0$.

**The Hodge star $\star$.**
On an $n$-dimensional manifold, $\star$ maps $k$-forms to
$(n{-}k)$-forms by "complementing" directions:
$\star(dx) = dy \wedge dz$ in $\mathbb{R}^3$. It converts between
the two natural duals of a differential form.

**The codifferential $\delta$ and divergence.**
The codifferential $\delta = (-1)^{nk+n+1}\star d\star$ is the
formal adjoint of $d$. On $1$-forms in $\mathbb{R}^3$,
$\delta\alpha = -\mathrm{div}(\alpha^{\sharp})$, where
$\alpha^{\sharp}$ is the vector field dual to $\alpha$.

**The Laplacian.**
The Hodge Laplacian is $\Delta = d\delta + \delta d$. On $0$-forms,
$\Delta f = \delta df$, which equals $-\nabla^2 f$ (the negative
of the analyst's Laplacian). A function $f$ is *harmonic*
($\Delta f = 0$) precisely when it has no sources or sinks: its
value at each point equals the average over any small sphere
centered there.
<!-- FILE_END: vector-calculus-bridge.md -->

<!-- FILE_START: q-laplacian-interpretation.md -->
The classical Laplacian $\Delta f = 0$ says: the value of $f$ at a
point equals the average over any small neighbourhood. The
$q$-Laplacian $\Delta_q = d_q\delta_q + \delta_qd_q$ replaces
"small neighbourhood" with a *quantum-twisted neighbourhood* that
weights the horizontal (spatial) and vertical (Reeb/spin) directions
differently.

Setting $\Delta_q \alpha = 0$ means the field $\alpha$ has found a
perfect equilibrium between its spatial environment and its internal
quantum spin. The geometric twist (measured by the substrate
parameter $q$) precisely counterbalances the spatial diffusion:

- **At $q = 1$** (classical limit): $d_q = d$, and $\Delta_q$
  reduces to the Hodge Laplacian $\Delta$. The "quantum twist"
  vanishes, and $q$-harmonic forms are ordinary harmonic forms.

- **At $q \to \infty$** (deep-quantum regime): $d_q$ projects
  onto $\pi_V \circ d$, so only the Reeb (spin) direction
  contributes. A $q$-harmonic form in this limit is one that
  is "averaged" purely along the internal fibre.

A $q$-harmonic form ($\Delta_q \alpha = 0$) is therefore a
"particle" — a field configuration that is in perfect $q$-equilibrium
with its twisted geometric environment. The substrate parameter $q$
([substrate parameter](#def:substrate-parameter)) tunes the relative
weight of spatial diffusion versus internal spin in this balancing act.
<!-- FILE_END: q-laplacian-interpretation.md -->

<!-- FILE_START: q-codifferential-formula-prop.md -->
Let $d_q = q^{-1}d + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi$ be
the $q$-exterior derivative
([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)).
The formal adjoint of $d_q$ with respect to the Webster inner product
$\langle \cdot, \cdot \rangle_\varTheta$ is

$$
  \delta_q =  q^{-1}\delta
  +  (1 - q^{-1})\mathcal{L}_\xi^* \circ \iota_\xi,
$$

characterised uniquely by the adjoint relation

$$
  \langle d_q\alpha, \beta \rangle_\varTheta
  = 
  \langle \alpha, \delta_q\beta \rangle_\varTheta
$$

for all compactly supported forms $\alpha, \beta$.
<!-- FILE_END: q-codifferential-formula-prop.md -->

<!-- FILE_START: q-codifferential-formula.md -->
In the archimedean realisation, the $q$-exterior derivative is
$d_q = q^{-1}d + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi$
([archimedean $d_q$](#ex:q-ext-deriv)). To find the formal adjoint
$\delta_q$ with respect to the Webster inner product
$\langle \cdot, \cdot \rangle_\varTheta$, every operation in $d_q$ is
replaced by its geometric mirror:

- The classical derivative $d$ becomes the classical codifferential
  $\delta$.
- Wedging with the contact form ($\varTheta \wedge$) becomes
  contraction with the Reeb vector field ($\iota_\xi$), because
  $\xi$ is the metric dual to $\varTheta$: $\varTheta(X) = \langle \xi, X \rangle_\varTheta$ for all $X$.
- The Lie derivative $\mathcal{L}_\xi$ becomes its formal adjoint
  $\mathcal{L}_\xi^*$.

The resulting closed formula is:

$$
  \delta_q =  q^{-1}\delta
  +  (1 - q^{-1})\mathcal{L}_\xi^* \circ \iota_\xi.
$$

In words: where $d_q$ uses the Reeb vector field to *add* a vertical
spin twist to a form (via $\varTheta \wedge \mathcal{L}_\xi$), the
codifferential $\delta_q$ uses contraction with $\xi$ (via
$\iota_\xi$) to *extract* and step down that vertical spin. They are
exact geometric duals under the Webster metric.

The $q$-codifferential is uniquely characterised by the
adjoint relation:

$$
  \langle d_q\alpha, \beta \rangle_\varTheta
  = 
  \langle \alpha, \delta_q\beta \rangle_\varTheta
$$

for all compactly supported forms $\alpha, \beta$.
<!-- FILE_END: q-codifferential-formula.md -->

<!-- FILE_START: q-laplacian-expansion.md -->
Expanding $\Delta_q = d_q\delta_q + \delta_qd_q$ using
$d_q = q^{-1}d + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi$
and
$\delta_q = q^{-1}\delta + (1 - q^{-1})\mathcal{L}_\xi^* \circ \iota_\xi$
([expanded $\delta_q$](#rem:q-codifferential-formula)), the
$q$-Laplacian separates into three distinct types of terms:

1. **Classical core** ($\propto q^{-2}$): terms proportional to
   $q^{-2}\Delta$, where $\Delta = d\delta + \delta d$ is the
   standard Hodge Laplacian. This is the ordinary spatial diffusion
   operator, measuring how the field value at a point compares to
   its spatial neighbours.

2. **Quantum spin core** ($\propto (1 - q^{-1})^2$): terms involving
   only Reeb operations
   ($\varTheta \wedge \mathcal{L}_\xi$ and
   $\mathcal{L}_\xi^* \circ \iota_\xi$). These represent pure
   internal Reeb dynamics — how the field twists along the internal
   spin direction, independent of macroscopic spatial motion.

3. **Cross-coupling terms** ($\propto q^{-1}(1 - q^{-1})$): mixed
   terms combining spatial derivatives ($d, \delta$) with Reeb
   operations ($\varTheta \wedge \mathcal{L}_\xi$,
   $\mathcal{L}_\xi^* \circ \iota_\xi$). These "Coriolis" terms
   measure the interference between moving through macroscopic
   space and spinning in the internal dimension.

In summary:

$$
  \Delta_q = q^{-2}\Delta
  +  q^{-1}(1 - q^{-1})\bigl[
    d(\mathcal{L}_\xi^* \iota_\xi)
    + (\varTheta \wedge \mathcal{L}_\xi)\delta
    + \delta(\varTheta \wedge \mathcal{L}_\xi)
    + (\mathcal{L}_\xi^* \iota_\xi)d
  \bigr]
  +  (1 - q^{-1})^2\Delta_{\xi},
$$

where $\Delta_\xi = (\varTheta \wedge \mathcal{L}_\xi) (\mathcal{L}_\xi^* \iota_\xi) + (\mathcal{L}_\xi^* \iota_\xi) (\varTheta \wedge \mathcal{L}_\xi)$ is the pure spin Laplacian.

At $q = 1$ the spin-core and cross-coupling terms vanish, recovering
$\Delta_1 = \Delta$. As $q \to \infty$, the classical core is
suppressed and the spin core dominates.
<!-- FILE_END: q-laplacian-expansion.md -->

<!-- FILE_START: q-laplacian-spectral-tower.md -->
**Proposition (the $q$-Laplacian spectral tower).** *The $q$-Laplacian
$\Delta_q = d_q\delta_q + \delta_qd_q$
([particle / $q$-harmonic form](#def:q-harmonic-form)) has eigenvalues
given by the $q$-integer tower*
$$
  [k]_q^2, \qquad [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}}
  \quad (k = 1, 2, 3, \ldots).
$$
*At a primitive root of unity $q = e^{i\pi/\kappa}$ the $q$-integer
$[\kappa]_q$ **vanishes**, and the spectrum truncates to the finite set*
$$
  \{\,[1]_q^2, [2]_q^2, \ldots, [\kappa-1]_q^2\,\},
$$
*the **Verlinde / ADE quantum-dimension** data of the truncated
representation category.*

**Proof.** The vanishing $[\kappa]_q = 0$ at $q = e^{i\pi/\kappa}$ is
elementary: the numerator $q^\kappa - q^{-\kappa}$ vanishes because
$q^\kappa = e^{i\pi} = -1$, hence $q^{-\kappa} = -1$ as well and the
difference is $0$. By the **Verlinde formula** \cite{verlinde1988} the
fusion coefficients are diagonalised by the modular $S$-matrix and the
surviving simple objects are $j = 0, \tfrac12, \ldots,
\tfrac{\kappa-2}{2}$ — the **Reshetikhin–Turaev** truncation
\cite{reshetikhin1991}. The surviving quantum dimensions are exact
algebraic numbers in the cyclotomic field $\mathbb{Q}(\zeta_\kappa)$.
$\blacksquare$

## Lean structure

`truncRoot κ := exp(iπ/κ)` over $\mathbb{C}$;
`truncRoot_pow` proves $\zeta_\kappa^{\,\kappa} = -1$ (hence
$\zeta_\kappa^{\,2\kappa} = 1$), and
`qIntegerNumerator_vanishes_at_truncRoot` proves the numerator
$q^\kappa - q^{-\kappa} = 0$ at $q = \zeta_\kappa$ — the level-$\kappa$
truncation. The statement lives over $\mathbb{C}$ because the
truncation root is genuinely complex; no reality is assumed.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-laplacian-spectral-tower.md -->

<!-- FILE_START: q-laplacian-consumers.md -->
The $q$-Laplacian spectral tower
([$q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower)) is the
organizing observation behind several $q$-deformed structures in the
framework: rather than treat each one's spectral content separately, they
all read off the *same* tower $[k]_q^2$.

## One tower, four consumers

| Structure | How it uses $[k]_q^2$ |
|---|---|
| $q$-heat equation $\partial_t u = -\Delta_q u$ | mode $k$ decays as $e^{-[k]_q^2 t}$ |
| $q$-Navier–Stokes ($\Delta_q$ dissipation) | eigenvalues $[k]_q^2 \sim q^{2k}$ |
| Markov trace / Gram / Wenzl blocks | block quantum dimensions $[2j+1]_q$ |
| Yekutieli lifting obstruction tower | level capped at $\kappa-1$ by truncation |

Because the tower is established in the proposition, each consumer refers
**back** to it rather than re-introducing $[k]_q$ locally.

## Concrete truncation values

The surviving quantum dimensions are exact algebraic numbers: for example
$[3]_q$ at $\kappa = 5$ is the golden ratio $\varphi = \tfrac{1+\sqrt5}{2}$
(the Fibonacci-anyon dimension), and $[2]_q$ at $\kappa = 8$ is
$\sqrt{2+\sqrt2}$. The practical payoff is **exactness**: at a root of
unity the spectrum is *finite*, so any spectral computation built on it
(the $q$-heat kernel, a $q$-NS truncation, a Gram block) is a finite exact
sum with **no series-truncation error** — the compute-accuracy benefit of
the root-of-unity viewpoint.

## Fibre vs observable level

The tower and its truncation are **fibre-level** statements: $q$ is a
formal (or complex) variable with $\mathrm{Im}(q)$ unconstrained,
and the operative symmetry is the root of unity / bar involution
$q \mapsto q^{-1}$ — *not* a reality assumption. Only the *observable*
component, obtained by evaluating at the real archimedean substrate
value $q_0$, is real. The root-of-unity spectra and quantum dimensions
are exact identities in the relevant cyclotomic field, independent of
the eventual archimedean realisation (cf. the front-matter
fibre-versus-observable distinction).
<!-- FILE_END: q-laplacian-consumers.md -->

<!-- FILE_START: hodge-laplacian-relation.md -->
The relationship between the Hodge star and the Laplacian carries over
to the $q$-deformed setting. Classically, the codifferential is
$\delta = (-1)^{nk+n+1}\star d\star$, so the Hodge star mediates
between differentiation and its adjoint. In the $q$-deformed theory,
the $q$-Hodge star $\star_q$ ([q-Hodge star](#def:q-hodge-star))
rescales the inner product by the substrate parameter $q$, and the
$q$-codifferential $\delta_q$ inherits this deformation.

The $q$-Laplacian $\Delta_q = d_q\delta_q + \delta_qd_q$ is
formally self-adjoint with respect to the Webster inner product.
By the defining property $\langle d_q \alpha, \beta \rangle_\varTheta = \langle \alpha, \delta_q \beta \rangle_\varTheta$
([codifferential formula](#rem:q-codifferential-formula)):

$$
  \langle \Delta_q\alpha, \beta \rangle_\varTheta
  = \langle \delta_q\alpha, \delta_q\beta \rangle_\varTheta
  + \langle d_q\alpha, d_q\beta \rangle_\varTheta
  = \langle \alpha, \Delta_q\beta \rangle_\varTheta.
$$

Self-adjointness guarantees real eigenvalues and orthogonal
eigenspaces. In particular, $\ker \Delta_q$ (the space of particles)
is a well-defined subspace with a canonical complement.
<!-- FILE_END: hodge-laplacian-relation.md -->

<!-- FILE_START: categorical-lichnerowicz.md -->
**Proposition (categorical Lichnerowicz formula).**
Let $\nabla$ be a categorical connection on an adjoint bundle over the
[contact affine chart](#def:contact-affine-chart) with
[categorical Reeb derivation](#thm:categorical-reeb-exists) $\xi$ and
$q$-Hodge star $\star_q$
([$q$-Hodge star](#def:q-hodge-star)). Let $\mathfrak{D}_\nabla =
q^{-1}\nabla + \hbar_q \, \iota_\xi \nabla$ be the
[categorical Dirac operator](#def:categorical-dirac-operator), and let
$\Delta_\nabla^q = d_\nabla^*\, d_\nabla + d_\nabla\, d_\nabla^*$ be
the categorical $q$-Laplacian on $\Omega^1(\mathrm{End}\,V)$
([Hodge–Laplacian relation](#rem:hodge-laplacian-relation)). Then on
the [categorical-instanton](#def:categorical-instanton) saddle
$\star_q F_\nabla = F_\nabla$:

$$
  \boxed{\;
  \Delta_\nabla^q  =  \mathfrak{D}_\nabla^2  +  \tfrac{1}{4}\,\mathrm{Sc}_q,
  \;}
$$

where $\mathrm{Sc}_q$ is the $q$-scalar curvature of the contact
affine chart. On the
[constructive Bring background](#ex:categorical-reeb-brings) the
Reeb generator $\xi = e_3$ is parallel (it is the maximal-torus
generator of $\mathrm{SU}_q(2)$ acting on the homogeneous space
$\mathbb{P}(V) = G_q/T_q$), so $\mathrm{Sc}_q = 0$ and the
identity simplifies to $\Delta_\nabla^q = \mathfrak{D}_\nabla^2$.
<!-- FILE_END: categorical-lichnerowicz.md -->

<!-- FILE_START: lichnerowicz-wkb-corollary.md -->
## Corollaries

The identity is the categorical input needed by
[next Faddeev-WKB order](#conj:phi-q-wkb-greens-function) Step 3b:
the gauge Hessian at the categorical-instanton saddle is the
$q$-Laplacian $\Delta_\nabla^q$, which by this proposition equals
$\mathfrak{D}_\nabla^2$ on the parallel-Reeb background. The
Pfaffian structure on chiral spinors (Atiyah–Singer index theorem
for the self-dual Dirac) then converts
$-\tfrac{1}{2}\log \det \Delta_\nabla^q = -\log \det |\mathfrak{D}_\nabla|
= -\tfrac{1}{2}\log \det \mathfrak{D}_\nabla$, recovering the WKB
$S_1$ formula.

In particular, the WKB conjecture is reduced to:

1. This proposition (now proved up to the routine Bianchi /
   Weitzenböck manipulations of Step 4).
2. The parent
   [archimedean limit conjecture](#conj:dilogarithm-archimedean-limit)
   for the $S_0$ term.
3. Mathlib infrastructure for heat-kernel zeta regularisation.

(1) is no longer the bottleneck; (2)–(3) are the residual gaps.
<!-- FILE_END: lichnerowicz-wkb-corollary.md -->

<!-- FILE_START: lichnerowicz-q-correction.md -->
## A note on the $q$-correction term

The classical Lichnerowicz identity has $R/4$ where $R$ is scalar
curvature. The categorical version has $\tfrac{1}{4}\mathrm{Sc}_q$
where $\mathrm{Sc}_q = R + O(\hbar_q)$ encodes both the classical
scalar curvature *and* the $q$-anomaly contribution from
$d_q^2 \neq 0$. The $O(\hbar_q)$ correction comes from the
non-vanishing $d_q^2$ identity (see
[$q$-Laplacian expansion](#rem:q-laplacian-expansion)), which on a
non-flat substrate adds a contact-curvature term to the otherwise
classical scalar curvature.

On the contact-flat Bring background — where the maximal torus
acts transitively on $\mathbb{P}(V) = G_q/T_q$ — both contributions
vanish, giving the clean identity
$\Delta_\nabla^q = \mathfrak{D}_\nabla^2$ used by
[`conj:phi-q-wkb-greens-function`](#conj:phi-q-wkb-greens-function).
<!-- FILE_END: lichnerowicz-q-correction.md -->

<!-- FILE_START: q-harmonic-particle.md -->
We now make explicit the logical chain leading from the QOU axioms to
the particle concept, before the fermion--boson decomposition that
follows.

By the self-adjointness and positive-definiteness of $\Delta_q$
([self-adjointness](#rem:hodge-laplacian-relation)), a form
$\alpha$ is $q$-harmonic ($\Delta_q \alpha = 0$) if and only if it
is simultaneously $q$-closed and $q$-coclosed:

$$
  \Delta_q\alpha = 0
  \quad\Longleftrightarrow\quad
  d_q\alpha = 0
   \text{and} 
  \delta_q\alpha = 0.
$$

This equivalence follows from $\langle \Delta_q \alpha, \alpha \rangle_\varTheta = \|d_q \alpha\|^2 + \|\delta_q \alpha\|^2$, which
vanishes only when both norms are zero.

Physically:
- $d_q \alpha = 0$ means $\alpha$ is *closed* under $q$-deformed
  differentiation — it has no "sources" in the twisted sense.
- $\delta_q \alpha = 0$ means $\alpha$ is *coclosed* under
  $q$-deformed contraction — it has no "sinks" in the twisted sense.

This is the formal definition of a *particle*: a field configuration
that is in perfect equilibrium with respect to the $q$-deformed
geometry. The [fermion--boson decomposition](#def:fermion-boson-decomposition)
then classifies particles by their vertical component under the
[weight decomposition](#def:weight-decomposition): bosons are purely
horizontal ($\alpha_V = 0$), fermions have non-trivial vertical part.

The complete logical chain is:

$$
  \text{QOU} \xrightarrow{d_q}
  \text{$q$-exterior derivative}
  \xrightarrow{\delta_q}
  \text{$q$-codifferential}
  \xrightarrow{\Delta_q}
  \text{$q$-Laplacian}
  \xrightarrow{\ker}
  \text{particle}
  \xrightarrow{\pi_H \oplus \pi_V}
  \text{boson $\oplus$ fermion.}
$$
<!-- FILE_END: q-harmonic-particle.md -->

<!-- FILE_START: brings-geometric-connection.md -->
The geometric structures developed above — the $q$-Laplacian, the
fermion--boson decomposition, the three-term expansion, and the
contact affine chart — become concrete on the
[Brings surface](#ex:brings-surface) studied in [Chapter 4](#chap:brings-surface).
There, the contact structure $\varTheta$, the Reeb vector field $\xi$,
and the substrate parameter $q$ are given by explicit formulas on
a genus-$4$ Riemann surface with $S_5$ symmetry.
The "abstract" balancing act $\Delta_q \alpha = 0$ reduces to
computable eigenvalue problems, and the boson--fermion split becomes
a visible decomposition of the harmonic space into horizontal and
vertical eigenspaces of the Reeb flow.
<!-- FILE_END: brings-geometric-connection.md -->

<!-- FILE_START: complex-substrate-interpretation.md -->
The [substrate parameter](#def:substrate-parameter) is defined over an
arbitrary base field $k$, so $q \in \mathrm{End}(\mathbf{1}) \cong k^\times$.
Nothing in the *algebraic* definition of $d_q$ requires $q$ to be real.
Over $k = \mathbb{C}$, write $q$ in polar form:

$$
  q =  |q|e^{i\varTheta}, \qquad |q| \geq 1,\quad \varTheta \in (-\pi, \pi].
$$

The deformed differential becomes

$$
  d_q =  |q|^{-1} e^{-i\varTheta}d
  +  \bigl(1 - |q|^{-1} e^{-i\varTheta}\bigr)\pi_V \circ d,
$$

and the quantum Planck constant generalises to

$$
  \hbar_q =  1 - q^{-1}
  =  1 - |q|^{-1} e^{-i\varTheta}.
$$

When $\varTheta \neq 0$, $\hbar_q$ acquires an imaginary part
$\mathrm{Im}(\hbar_q) = |q|^{-1}\sin\varTheta$, so the
$q$-equilibrium of the
[$q$-Laplacian](#rem:q-laplacian-interpretation) is no longer
self-adjoint — it mixes amplitudes with phases.

**Observability forces $\varTheta = 0$.**
A [quantum observable universe](#def:quantum-observable-universe) carries
a dagger structure $\dagger$ and a fibre functor $\tau$ satisfying
positive-definiteness: $h_q(a^\dagger a) > 0$ for all $a \neq 0$.
For the Haar functional $h_q$ to be positive-definite, the inner product
$\langle \alpha, \beta \rangle_q = h_q(\alpha^\dagger \wedge_q \beta)$
on $\Omega^\bullet(A)$ must be Hermitian.  This requires $d_q^\dagger$
to be the formal adjoint of $d_q$, which holds if and only if

$$
  \overline{q^{-1}} = q^{-1},
$$

i.e. $q \in \mathbb{R}_{>0}$.  The positivity axiom $q \geq 1$ then
gives the Lean constraint `field_ge_one`.

**Interpretation of the imaginary part.**
If one relaxes the observability axiom — passing to the "pre-observable"
or algebraic sector — the phase $\varTheta$ has a geometric interpretation:

1. **Phase in crossing energy.** In the skein relation
   $qL_+ - q^{-1}L_- = (q - q^{-1})L_0$, complex $q$
   contributes a relative phase $e^{2i\varTheta}$ between over-
   and under-crossings.  This phase distinguishes a knot from
   its mirror image *continuously*, rather than by discrete
   crossing reversal.

2. **Continuous chirality.**  The operator
   $\sigma_\varTheta \colon q \mapsto |q|e^{i(\varTheta + \pi)}$
   acts as chirality reversal.  For real $q$ ($\varTheta = 0$),
   this is the discrete flip $q \mapsto -q$ (ill-defined for
   $q > 0$).  For complex $q$, chirality reversal becomes a
   continuous rotation in the $\varTheta$-circle, and the
   electron/positron distinction is a $\pi$-rotation rather
   than a discontinuous mirror.

3. **Non-Hermitian $q$-Laplacian.**  When $\varTheta \neq 0$,
   $\Delta_q$ has complex eigenvalues.  The real part still
   controls spatial diffusion, but the imaginary part generates
   a *probability current* along the Reeb fibre — a persistent
   phase rotation of the internal quantum state.

**Relation to root-of-unity specialisations.**  The
[$\mathrm{SU}(2)$ specialisation](#def:substrate-parameter) at
$q_0 = e^{\pi i / \kappa}$ has $|q_0| = 1$ and
$\varTheta = \pi / \kappa$ — it is genuinely complex.  This does not
contradict the observability constraint because root-of-unity
categories carry a *modified* trace (the quantum trace $\mathrm{tr}_q$)
that restores a non-degenerate pairing without requiring
positive-definiteness in the Hilbert-space sense.  The finite
modular tensor category at roots of unity is the prototype of a
"non-observable but algebraically consistent" sector.
<!-- FILE_END: complex-substrate-interpretation.md -->

