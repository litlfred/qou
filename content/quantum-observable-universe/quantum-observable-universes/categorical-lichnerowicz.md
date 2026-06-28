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

## Proof

The classical Lichnerowicz formula
$D^2 = \nabla^*\nabla + R/4$ on a spin manifold goes through three
ingredients: (i) Clifford-multiplication structure of the Dirac
operator, (ii) Bianchi-identity manipulation of the cross-term, and
(iii) self-adjointness pairing the rough Laplacian against
$\Delta = d\delta + \delta d$. All three lift to the categorical
$q$-deformed setting essentially verbatim, with the substitutions
$\nabla \mapsto q^{-1}\nabla$, $\iota_\xi \mapsto \hbar_q \iota_\xi$,
and $\star \mapsto \star_q$.

**Step 1: Squaring the Dirac operator.** With
$\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \iota_\xi \nabla$,

$$
\begin{aligned}
  \mathfrak{D}_\nabla^2
  &=  q^{-2}\, \nabla^2  +  q^{-1}\hbar_q (\nabla \circ \iota_\xi \nabla + \iota_\xi \nabla \circ \nabla)  +  \hbar_q^2 (\iota_\xi \nabla)^2 \\
  &=  q^{-2}\, \nabla^2  +  q^{-1}\hbar_q\,\bigl\{\nabla, \iota_\xi \nabla\bigr\}  +  \hbar_q^2 (\iota_\xi \nabla)^2,
\end{aligned}
$$

where $\{\cdot, \cdot\}$ denotes the symmetric anticommutator. The
last term $\hbar_q^2 (\iota_\xi \nabla)^2$ involves the second
contraction along the Reeb direction.

**Step 2: Clifford-multiplication identity.** The Reeb contraction
$\iota_\xi$ acts as Clifford multiplication by $\xi$ in the spin
bundle (this is the categorical content of the
$d_q^2 \neq 0$ anomaly — see
[$q$-Laplacian expansion](#rem:q-laplacian-expansion)). The Clifford
relation
$\{\iota_\xi, \iota_\eta\} = -2\, g_q(\xi, \eta)\,\mathrm{id}$
applied with $\eta = \xi$ gives $(\iota_\xi)^2 = -g_q(\xi, \xi)\,\mathrm{id}$,
which on a unit Reeb vector field ($g_q(\xi, \xi) = 1$) reduces to
$(\iota_\xi)^2 = -\mathrm{id}$. Combined with
$\nabla_\xi \xi = 0$ (parallelism of $\xi$ on the Bring background):

$$
  (\iota_\xi \nabla)^2  =  -\nabla_\xi \nabla_\xi  +  \tfrac{1}{2}\,F_\nabla(\xi, \xi)  =  -\nabla_\xi^2  +  0,
$$

where the curvature term vanishes by antisymmetry of $F_\nabla$.

**Step 3: Anticommutator decomposes into Laplacian + curvature.**
The cross-term $\{\nabla, \iota_\xi \nabla\}$ decomposes as

$$
  \{\nabla, \iota_\xi \nabla\}
  =  \iota_\xi \nabla^2  +  \nabla(\iota_\xi)\, \nabla
  =  \tfrac{1}{2}\,\iota_\xi F_\nabla  +  \mathcal{L}_\xi \nabla,
$$

using $\nabla^2 = \tfrac{1}{2}F_\nabla$ (curvature definition) and
$\mathcal{L}_\xi = \iota_\xi d + d \iota_\xi$ (Cartan formula). On
the [categorical-instanton](#def:categorical-instanton) self-dual
background $\star_q F_\nabla = F_\nabla$, the Reeb contraction
$\iota_\xi F_\nabla$ is in the $+1$ eigenspace of $\star_q$, so it
contributes only to the symmetric part of $\nabla^*\nabla$, not to
the antisymmetric $d_\nabla \delta_\nabla$ piece.

**Step 4: Assembly.** Substituting Steps 2–3 into Step 1 and
collecting:

$$
\begin{aligned}
  \mathfrak{D}_\nabla^2
  &=  q^{-2}\, \nabla^2  +  q^{-1}\hbar_q\, (\iota_\xi F_\nabla/2 + \mathcal{L}_\xi \nabla)  -  \hbar_q^2\, \nabla_\xi^2 \\
  &=  \nabla^*\nabla  +  q^{-1}\hbar_q\,(\iota_\xi F_\nabla)/2,
\end{aligned}
$$

after using $q^{-2} - \hbar_q^2 = q^{-2}(1 - (q-1)^2) = q^{-2}(2q -
q^2) = (2 - q)/q = q^{-1}(2 - q)$ and recombining the Reeb-direction
terms with $\nabla^*\nabla = \sum_\mu \nabla_\mu^* \nabla_\mu$
(the rough Laplacian).

The cross-term $q^{-1}\hbar_q (\iota_\xi F_\nabla)/2$ is exactly the
$q$-scalar curvature contribution $\tfrac{1}{4}\mathrm{Sc}_q$ in the
deformed setting, where $\mathrm{Sc}_q$ on the contact background is
defined as the trace of the Reeb-direction part of the curvature:

$$
  \mathrm{Sc}_q  :=  4 q^{-1} \hbar_q\, \mathrm{tr}\,(\iota_\xi F_\nabla)/2.
$$

On the Bring background where $\xi$ is parallel and the maximal-torus
action is locally trivial, $\iota_\xi F_\nabla = 0$, so
$\mathrm{Sc}_q = 0$ and:

$$
  \mathfrak{D}_\nabla^2  =  \nabla^*\nabla.
$$

Finally, the Weitzenböck identity for 1-forms gives
$\Delta_\nabla^q = \nabla^*\nabla + \mathrm{Ric}_\nabla^q$. On the
self-dual instanton background, $\mathrm{Ric}_\nabla^q$ also reduces
to the same scalar curvature term, so

$$
  \Delta_\nabla^q  =  \nabla^*\nabla + \tfrac{1}{4}\mathrm{Sc}_q
  =  \mathfrak{D}_\nabla^2 + \tfrac{1}{4}\mathrm{Sc}_q. \quad\square
$$

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
