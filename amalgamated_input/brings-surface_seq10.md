<!-- FILE_START: archimedean-condition-genus-intro.md -->
The previous sub-section identified the lepton spectrum and the
chirality assignment that the Descartes condition fixes. This
sub-section then asks: which closed-braid generators populate the
maximally-descended genus, and what makes the generation system
*complete*?

The blocks below trace the algebraic derivation. Torus-knot
generators classify the closures available at low genus;
embeddability-closure shows they are stable under composition;
genus-from-Hecke-completeness gives the necessary-and-sufficient
condition that the Hecke algebra reproduce the genus; the
Chebyshev-degree-genus identity connects the genus to a specific
polynomial degree; genus-ideal-characterisation identifies the
genus as a Hecke ideal; the Yekutieli-leading-coefficient block
extracts the leading-order behavior from that ideal; the
genus-filtration-ideal sequence interprets the filtration in
ideal-theoretic terms; and the closing blocks (torus-embeddable-
complete + generation-completeness) demonstrate that the
torus-knot generators exhaust the maximally-descended genus.
The proof-of-completeness IS the framework's anchor for the
lepton-spectrum derivation.
<!-- FILE_END: archimedean-condition-genus-intro.md -->

<!-- FILE_START: torus-knot-generators.md -->
The Euler characteristic $\chi(A) = -6$ of the Bring's surface is
the reason torus knots serve as the generators of the particle
spectrum. Because the Bring's surface has genus $g = 4$
(from $\chi = 2 - 2g = -6$), there is a hard upper bound on
which torus knots can be localized in the fibre: any $T_{m,n}$
whose Seifert genus exceeds $4$ cannot embed. This
constraint selects a finite, enumerable generator set
$\mathcal{G}$ ([knot-particle generation](#def:knot-particle-generation))
whose cardinality is entirely determined by $\chi$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\chi(A) = -6$ (Descartes universe). The torus knot $T_{m,n}$
with $\gcd(m,n) = 1$ and $m < n$ embeds into the Seifert genus-$g$
surface of $A$ only if the Seifert genus satisfies

$$
  g(T_{m,n}) =  \frac{(m-1)(n-1)}{2}  \leq  g(A) =  4.
$$

The constraint $(m-1)(n-1) \leq 8$ admits exactly six coprime pairs
with $m \geq 2$, tabulated in
[Table: Torus-knot generators](#tbl:torus-knot-generators-table-data).
Together with the unknot $T_{1,0} = 0_1$ (genus $0$), the generator
set has $|\mathcal{G}| = 7$.

**Genus bound from $\chi(A) = -6$.**
The Bring's surface $\Sigma_4$ has genus $g = 4$ and Euler
characteristic $\chi = 2 - 2g = -6$. A knot $T_{m,n}$ localized
in the fibre $\mathcal{S}_c$
([localized knot](#def:localized-knot)) inherits a Seifert surface
that must embed in the genus-$4$ handlebody provided by $\Sigma_4$.
The Seifert genus of $T_{m,n}$ is $(m-1)(n-1)/2$, so
embeddability requires $(m-1)(n-1) \leq 2g = 8$.
<!-- FILE_END: torus-knot-generators.md -->

<!-- FILE_START: torus-knot-generators-interpretation.md -->
**Remark (physical interpretation).**

1. **Lepton generations.** Charged leptons are $T_{2,3}$
 (electron), $T_{2,5}$ (muon), $T_{2,7}$ (tau) at Reeb degrees
 $\deg\alpha_V = 1, 2, 3$. Only the first two are
 $S_5$-equivariant
 ([prop:s5-equivariant-torus-knots](#prop:s5-equivariant-torus-knots));
 the tau embeds topologically but breaks its $\mathbb{Z}_7$
 symmetry. $T_{2,9}$ saturates $g = 4$ also symmetry-broken, and
 $T_{2,11}$ is genus-excluded --- so no fourth generation.

2. **Quark sector.** The $(3,n)$-family generators $T_{3,4}$ and
 $T_{3,5}$ are $H^{0,1}$ force carriers
 ([cohomological embedding](#prop:cohomological-embedding)):
 $T_{3,4}$ encodes Hopf-squared color binding, while $T_{3,5}$
 mediates the weak interaction. The three-strand meridional
 winding $m = 3$ of these torus knots resonates with the three
 color tubes
 ([color tube interpretation](#rem:color-tube-interpretation)):
 each meridional strand threads one color fiber.

3. **Saturation.** The seventh generator $T_{2,9}$ at genus $4$
 exactly saturates the Bring's surface. Beyond this, new particle
 types require either a higher-genus QOU (different $\chi$) or
 composite construction via the linking operations.

4. **Hyperbolic knots are derived.** The figure-eight $4_1$ (Higgs
 boson), the three-twist $5_2$, and all other hyperbolic
 knots in the dictionary are *not* generators. They arise from
 Skein crossing changes applied to linked torus-knot
 configurations, inheriting nonzero hyperbolic volume — and
 hence nonzero bare mass — from the linking process.

**On the cutoff.**
The bound $N(\chi) = 1 - \chi = 1 - (-6) = 7$ on the number of
nontrivial generators is not accidental: it equals the number of
handles ($g = 4$) of Bring's surface plus the three independent
Seifert genus values ($1, 2, 3$) available within those handles.
The recursive brane tower
([recursive brane tower](#def:recursive-brane-tower)) does not
increase the genus — it refines the blow-up structure within the
existing handles — so the generator count is stable across all
brane levels.
<!-- FILE_END: torus-knot-generators-interpretation.md -->

<!-- FILE_START: embeddability-closure.md -->
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

**Preservation of embeddability under each operation.**

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
<!-- FILE_END: embeddability-closure.md -->

<!-- FILE_START: embeddability-closure-interpretation.md -->
**Remark (interpretation).**
Every knot type produced by the three generation operations
([knot-particle generation](#def:knot-particle-generation)) applied
to the generator set $\mathcal{G}$
([finiteness of generators](#prop:torus-knot-generators)) remains
embeddable in the genus-$4$ fiber of the Bring's surface, and hence
admits a localized knot structure
([localized knot](#def:localized-knot)) that descends to the base
manifold via the fibre functor $\tau$.

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
<!-- FILE_END: embeddability-closure-interpretation.md -->

<!-- FILE_START: genus-from-hecke-completeness.md -->
**Lemma.**
*The minimum genus at which the torus-knot evaluations span a
$5$-dimensional Iwahori--Hecke representation
$H_2(q) \oplus H_3(q)$ is $g_{\min} = 4$.  Equivalently, the count
of embeddable torus knots $T_{r,s}$ with $r \in \{2, 3\}$ first
reaches or exceeds $5$ at genus $g = 4$.*
<!-- FILE_END: genus-from-hecke-completeness.md -->

<!-- FILE_START: chebyshev-degree-genus.md -->
**Lemma.**
*Let $a_n \in \mathbb{Z}[s]$ be the Hecke recurrence
$a_{n+1} = s\,a_n + a_{n-1}$ with $a_0 = 0$, $a_1 = 1$, and let
$u = s^2$.  For odd $n = p$, $\deg_u a_p = (p-1)/2 = g(T_{2,p})$,
and the leading coefficient of $a_p$ in $u$ is $1$.*
<!-- FILE_END: chebyshev-degree-genus.md -->

