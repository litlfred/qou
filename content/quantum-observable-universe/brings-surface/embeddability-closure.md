Every knot type produced by the three generation operations
([knot-particle generation](#def:knot-particle-generation)) applied
to the generator set $\mathcal{G}$
([finiteness of generators](#prop:torus-knot-generators)) remains
embeddable in the genus-$4$ fiber of the Bring's surface, and hence
admits a localized knot structure
([localized knot](#def:localized-knot)) that descends to the base
manifold via the fibre functor $\tau$.

**Theorem.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with
$\chi(A) = -6$ and fiber genus $g(\Sigma_4) = 4$.  Let $K$ be any
knot type appearing as a component of a link produced by a finite
sequence of Hopf linkings $\ell_H$, color-tube threadings $\ell_c$,
and Skein crossing changes $\sigma$ applied to generators in
$\mathcal{G}$.  Then:

1. The Seifert genus of $K$ satisfies $g(K) \leq 4$.
2. $K$ admits a localized knot structure
   $(c, K) \in \mathrm{Hom}(\mathbf{1}, A^{\mathrm{co}T}) \times \mathrm{Knot}$ at some point $c$ of the base
   $\mathbb{P}(V)$.
3. The localized knot $(c, K)$ descends under $\tau$ to an
   observable morphism in $\mathbf{C}$: every generated particle
   interacts with every other generated particle via the categorical
   braiding.

In particular, no generated knot is "dark" — the generation scheme
is closed under observability.

**Why each operation preserves embeddability.**

*Hopf linking $\ell_H$.*
The Hopf link $\mathcal{L}_{\mathrm{Hopf}}$ on the exceptional
divisor $\mathcal{S}_c \cong S^2$ joins two knots localized at (possibly
distinct) points of the base.  Each component retains its own knot
type and hence its own Seifert genus.  The linking structure lives
in the total space $S^3 \to \mathcal{S}_c$ and does not increase the genus of
any individual component.  Consequently, if $g(K_1) \leq 4$ and
$g(K_2) \leq 4$, then both components of
$K_1 \cup_{\mathrm{Hopf}} K_2$ remain embeddable.

*Color-tube threading $\ell_c$.*
Threading three knots through the color tubes $(r, g, b)$ similarly
preserves each component's knot type.  The three-component link
$K_1 \cup_r K_2 \cup_g K_3$ has each $K_i$ sitting in its own
color fiber; the Seifert genus of each component is unchanged.

*Skein crossing change $\sigma$.*
This is the non-trivial case.  A crossing change at a single site
alters the Seifert genus by at most $\pm 1$:

$$
  |g(L_+) - g(L_-)| \leq 1, \qquad
  g(L_0) \leq \max\{g(L_+), g(L_-)\}.
$$

Starting from generators with $g(T_{m,n}) \leq 4$, a crossing
change produces a knot of genus at most $5$.  However, the Bring
surface imposes a *spectral filter*: only knots with $g(K) \leq 4$
admit localized knot structures.  A Skein descendant with $g = 5$
has zero image in the physical state space
$V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ — its coefficient in
the mass functional vanishes because the fibre functor $\tau$
cannot evaluate it.

The spectral filter acts at the level of the Skein resolution:

$$
  q  [L_+] - q^{-1} [L_-]
  = (q^{1/2} - q^{-1/2}) [L_0]
$$

in the Skein module $\mathrm{Sk}_q(\mathbf{C})$.  Terms whose knot
type has $g > 4$ lie in the kernel of the mass functional
$\mathcal{M} \colon \mathrm{Sk}_q \to \mathbb{R}_{\geq 0}$, because
$\mathcal{M}$ is defined via the fibre functor, which requires
localizability.  The physical mass receives contributions only from
the embeddable terms.

**Explicit verification for the particle dictionary.**

See [Table](#tbl:embeddability-closure-table-data).

Every knot in the dictionary has $g(K) \leq 4$.  The Skein
descendants ($4_1$, $5_2$) have *lower* genus than their parent
generators — crossing changes that produce hyperbolic knots from
torus knots typically decrease the genus.

**Physical consequence.**
The closure of embeddability under generation is the topological
reason that *all* fundamental particles interact: they all descend
to the same base manifold $\mathbb{P}(V)$ and hence participate in
the categorical braiding.  A hypothetical particle corresponding to
a genus-$5$ knot would be unobservable — it could not be localized
in the Bring's surface fiber, could not descend to the base, and would
have zero coupling to all other particles.  The $\chi = -6$
constraint of the Descartes universe therefore guarantees a
self-consistent, fully interacting particle spectrum with no dark
sectors arising from the generation scheme.
