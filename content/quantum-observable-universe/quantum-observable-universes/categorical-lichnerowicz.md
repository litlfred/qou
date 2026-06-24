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

## Consequences

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
