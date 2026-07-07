<!-- FILE_START: archimedean-intro.md -->
We now specialise the categorical framework to the archimedean setting,
where the base ring is an archimedean field $K$ (e.g.
$\mathbb{Q}$, $\mathbb{R}$, or $\mathbb{C}$) and the quantum universe
is realised by CR geometry on a contact manifold. The abstract
categorical structures — Frobenius form, weight decomposition,
$q$-deformed operators — acquire concrete geometric meaning as
differential-geometric objects on a CR manifold equipped with a
pseudo-Hermitian structure. The main result
(§\ref{sec:physical-interpretation}) places gravity, gauge theory,
and quantum mechanics in a unified commutative diagram within this
setting.
<!-- FILE_END: archimedean-intro.md -->

<!-- FILE_START: c-quantum-universe.md -->
Let $K$ be an archimedean field.  A quantum universe over $K$
([quantum universe](#def:quantum-universe)) is realised by the $4$-tuple
$(\mathbf{C}, \varTheta, G, \mathcal{S})$: here
$\varTheta$ is a contact form on a CR manifold $M$ (encoding the contact
geometry and Reeb structure),
$G = \mathrm{SU}(2)$ is the gauge group, and
$\mathcal{S}$ is the state bundle carrying the quantum degrees of freedom.
The base manifold $M$ is implicit as the domain of $\varTheta$; the
principal bundle $P$ is implicit as the frame bundle of $\mathcal{S}$
under $G$.  The precise requirements are:

1. $M$ (the domain of $\varTheta$) is a CR manifold of hypersurface type
   (real dimension $2n+1$, $n \geq 1$) with non-degenerate Levi form
   of signature $(r,s)$, $r + s = n$;
2. $\varTheta$ is a pseudo-Hermitian structure (contact form) on $M$,
   determining the Levi distribution $H = \ker\varTheta$, the Reeb vector
   field $\xi$, the Webster metric $g_\varTheta$ (of signature $(2r,2s)$
   on $H$), and the Levi form $L_\varTheta$;
3. $G = \mathrm{SU}(2)$;
4. $\mathcal{S} = P \times_G \mathbb{P}^1(\mathbb{C}) \to M$ is the
   associated *state bundle*, where $P \to M$ is the principal
   $G$-bundle (with holonomy reducing to
   $\mathrm{SO}(3) \subset \mathrm{SU}(2)/\{\pm I\}$) and
   $\mathrm{SU}(2)$ acts on $\mathbb{P}^1(\mathbb{C})$ by Möbius
   transformations.

The :refterm[monoidal category]{#monoidal-category} is $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$
(the representation category of the quantum group at the substrate
parameter $q(p)$, [substrate parameter](#def:substrate-parameter)), the
Frobenius--Hopf object is
$A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the
Haar state, and the fibre functor $\tau$ is the forgetful functor
to $K\text{-}\mathrm{Mod}$.
<!-- FILE_END: c-quantum-universe.md -->

<!-- FILE_START: notation-special-cases.md -->
**Notation.** The symbol $\varTheta$ (upright capital theta, `\varTheta`) denotes
the \emph{contact form} (pseudo-Hermitian structure) in the archimedean
$4$-tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$.  It replaces the
earlier lowercase $\theta$; the upright face distinguishes the contact form
from scalar angles and phase parameters (for which plain italic $\theta$
is retained).

When the category $\mathbf{C}$ is understood from context, we abbreviate to
$(\varTheta, G, \mathcal{S})$.  The *strictly pseudoconvex* case corresponds to
signature $(n,0)$, where $L_\varTheta$ is positive definite — this is the
primary case of physical interest, giving a positive-definite Webster
metric $g_\varTheta$ and a well-defined Hodge star.  The *indefinite* case
(signature $(r,s)$ with $s > 0$) admits analogous constructions with
the Webster metric of mixed signature; see
([Levi generalisation](#rem:levi-generalisation)) for the extension.
<!-- FILE_END: notation-special-cases.md -->

<!-- FILE_START: c-quantum-observable-universe.md -->
An *archimedean quantum observable universe* is an archimedean quantum
universe $(\mathbf{C}, \varTheta, G, \mathcal{S})$
([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)) that satisfies
the vanishing conditions

$$
  H^0(M, \mathrm{Ad}(P)) = 0
  \qquad\text{and}\qquad
  \Gamma_c(M, \mathcal{S}) = 0.
$$

These analytic conditions are the archimedean realisation of the
categorical observability conditions of
[quantum observable universe](#def:quantum-observable-universe): the Frobenius
non-degeneracy of the Haar state on $\mathcal{O}_q(\mathrm{SU}(2))$,
combined with irreducibility of the instanton connection
([irreducible connection](#ex:irreducible-connection)), forces
$H^0(M, \mathrm{Ad}(P)) = 0$; the section-vanishing
$\Gamma_c(M, \mathcal{S}) = 0$ follows from the non-existence of
$A$-equivariant sections of the associated $\mathbb{P}^1(\mathbb{C})$-bundle.
<!-- FILE_END: c-quantum-observable-universe.md -->

<!-- FILE_START: archimedean-realisations.md -->
In the archimedean setting
([Examples](#ex:c-quantum-universe)--[Example](#ex:c-quantum-observable-universe)),
the categorical structures specialise to familiar geometric objects:

- **Volume constraint**
  (\ref{eq:categorical-volume-constraint}).
  The Levi form $L_\varTheta = -id\varTheta|_{H \times H}$ is non-degenerate
  on the rank-$4$ distribution $H = \ker\varTheta$, realising the
  categorical volume form
  $\epsilon \colon \Lambda^2 V \to \mathbf{1}$.  The induced Hodge star
  $*_H$ splits $\Lambda^2 H^* = \Lambda^+\!H^* \oplus \Lambda^-\!H^*$,
  forcing the structure group to be $\mathrm{SU}(2)$.

- **Involution**
  ([fibre adjoint involution](#prop:fiber-adjoint-involution)).
  The categorical involution $\sigma$ becomes the identification
  $\mathbb{P}^1(\mathbb{C}) \cong S^2 \subset \mathfrak{su}(2)$ (the unit sphere
  under the Killing form): a line $\ell \subset R^2$ maps to the
  projector $\mathrm{proj}_\ell - \tfrac12\mathrm{id}$.

- **Variational equations**
  ([variational equations](#prop:variational-equations)).
  The categorical Einstein equation reduces to
  $\mathrm{Ric}_{g_\varTheta} = T^{(q)}$
  ([GR substrate geometry](#rem:gr-substrate-geometry)); the transport equation
  reduces to the Schrodinger equation
  $J\hbar_q\iota_{\xi_q} D_A \psi = \hat{H}_q \psi$
  ([Schr\"{o}dinger jet coaction](#rem:schrodinger-jet-coaction)).
<!-- FILE_END: archimedean-realisations.md -->

<!-- FILE_START: affine-light-cone-figure.md -->
**Figure (affine light cone on Bring's brane, formal math-book style).**

*Single-panel illustration of the affine light-cone wedge over the
brane locus in the spacetime affine chart $z = x_0/x_1 \in \mathbb{CP}^1$,
re-derived from natural Bring coordinates per the the prior work redo workplan
(Phase 2).*

**Brane curve.** The thick black curve is the locus
$\{(z, X_{\mathrm{real}}(z)) : z \in [-1.5, 2.5]\}$
where $X_{\mathrm{real}}(z)$ is the real root of the canonical Bring
chiral cubic

$$
  X^3 + (z+1)\, X^2 + (z^2+z+1)\, X + (z^3 + z^2 + z + 1) = 0
$$

at the given $z$. The cubic's discriminant has six complex zeros at
$z \approx (0.119, \pm 1.054)$, $(0.106, \pm 0.937)$,
$(-0.975, \pm 0.223)$ (see [fig:bring-fibre-q0](#fig:bring-fibre-q0));
the real interval $z \in [-1.5, 2.5]$ stays well outside any
neighbourhood of those branch points, so $X_{\mathrm{real}}$ is a
single-valued smooth function on the interval.

**Affine light cone.** Two thin straight lines bound a wedge opening
from the big-bang vertex
$(-1.5, X_{\mathrm{real}}(-1.5)) \approx (-1.5, 0.811)$
toward the heat-death horizon at $z = 2.5$, with a vertical opening of
$\pm 1.5$ in the $X$ direction. No fabricated 3D surface or
exponential-profile brane — the wedge is purely a 2D bounded region
of the spacetime-affine-chart $(z, X)$-plane.

**Observer.** A small filled black circle at the substrate point
$q_0 \approx 1.1099786$ (imported from `q_parameter.Q`,
which derives $q_0$ from the CODATA 2022 $m_\mu / m_e$ ratio and the
SnapPy hyperbolic volume of the figure-eight knot complement; see
`docs/canonical-derivation-cheat-sheet.md`). The observer sits on the
brane at $(q_0, X_{\mathrm{real}}(q_0)) \approx (1.110, -1.743)$. A
vertical dotted line marks the substrate slice.

**Euler-characteristic annotation.** The corner box records
$\chi(A) = -6$, equivalently $\chi(\Sigma_4) = -6$, the
Euler-characteristic constraint of Bring's surface that fixes the
algebraic substrate's topology in the QOU framework
([archimedean-condition.md](../archimedean-universe/archimedean-condition.md)).

This figure is generated programmatically by
[`affine_light_cone_figure.py`](../../../computations/affine_light_cone_figure.py),
with the parameters and verified sample values recorded in
[`affine-light-cone-figure.witness.json`](../../../computations/affine-light-cone-figure.witness.json).
Formal math-book style (black ink on white, line styles only, no
gradient or decorative color) per author directive.
<!-- FILE_END: affine-light-cone-figure.md -->

