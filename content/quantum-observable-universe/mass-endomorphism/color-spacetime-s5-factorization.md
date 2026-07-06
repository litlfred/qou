**Proposition (color and spacetime are orthogonal factors of the Bring Galois group).**
*Let $K$ be a Bring-embeddable knot, evaluated through the categorical
Markov trace $\mathrm{tr}_M$ on the Hecke algebra
$H_2(q)\oplus H_3(q)$, whose $2+3=5$ irreducible representations are the
Bring fivefold. Bring's five homogeneous coordinates split as
$\underbrace{(x_0,x_1)}_{\text{spacetime}}$ and
$\underbrace{(x_2,x_3,x_4)}_{\text{color}}$, and the substrate Galois group
$S_5$ contains the block-diagonal product $S_2\times S_3$. Then:*

1. *the factorization $S_2\times S_3\hookrightarrow S_5$ is **faithful**;*
2. *the color factor $S_3$ fixes every spacetime coordinate and the
   spacetime factor $S_2$ fixes every color coordinate — the two sectors are
   **orthogonal**;*
3. *every additive homomorphism from the connected phase parameter
   $\mathbb{R}$ to a finite group is trivial.*

## The one trace object, two sectors

The embeddable strand counts give a single trace algebra
$H_2(q)\oplus H_3(q)$ with $2+3=5$ irreducible representations
([`prop:cohomological-embedding`](#prop:cohomological-embedding)); these five
match Bring's five homogeneous coordinates, split into a rank-two
*spacetime* block $(x_0,x_1)$ and a rank-three *color* block
$(x_2,x_3,x_4)$ ([`brings-qou-4tuple`](../brings-surface/brings-qou-4tuple.md)).
The color content of an embedded photon is recorded literally as an element
of $H_3(q)$, with the two generators $\sigma_0,\sigma_1$ the color axes
([`knot-basis-color-content`](../brings-surface/knot-basis-color-content.md)),
so color is a grading **on the trace algebra**, not on a separate object.

The substrate symmetry $S_5$ acts on all five coordinates. Its block-diagonal
subgroup $S_2\times S_3$ permutes spacetime and color **separately**: the
$S_3$ permutes the three color sheets while holding spacetime fixed (the
three copies of $S_3\subset S_5$ of
[`color-sector-coords`](../brings-surface/color-sector-coords.md),
[`rem:chirality-trefoil`](#rem:chirality-trefoil)), and the $S_2$ permutes the
two spacetime coordinates while holding color fixed. Parts (1)–(2) make this
precise: the product embeds faithfully and each factor fixes the other
sector pointwise. Color and the spacetime sector are therefore **independent
coordinates on one object** — coupled only by the $S_5$ elements *outside*
$S_2\times S_3$, which rotate spacetime indices into color indices.

## Discreteness

Part (3) is a rigidity statement about the *continuous* sector. The
connected group $\mathbb{R}$ is divisible, so any homomorphism to a finite
group $G$ vanishes: for each $x$, $f(x)=f\big(\lvert G\rvert\cdot
\tfrac{x}{\lvert G\rvert}\big)=\lvert G\rvert\cdot f(\tfrac{x}{\lvert
G\rvert})=0$, since $\lvert G\rvert\cdot g=0$ for every $g\in G$. A
continuous winding parameter thus cannot carry a finite-group (e.g.
$\mu_5$) character. Its consequence for the physical reading — that the
continuous trace phase is not the discrete color charge — is recorded in
[`rem:mass-modulus-em-phase-color-grading`](#rem:mass-modulus-em-phase-color-grading).

## Lean

Formalized sorry-free in
[`QOU.MassEndomorphism`](color-spacetime-s5-factorization.lean):
`spacetime_color_card` ($2+3=5$), `colorSpacetimeEmbed_injective` (1),
`color_fixes_spacetime` and `spacetime_fixes_color` (2), and
`winding_hom_to_finite_trivial` (3). The construction is generic: the
embedding and the divisibility argument hold over the bare combinatorial
data, with no archimedean input.
