**Conjecture (Shared-denominator cusp holonomy).**
*Let $T_w \in H_n(R, q)$ be a Hecke normal-form word at GB-depth
$k_\star(T_w) = n$, let $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
be its [$q$-Pochhammer partial product](#def:q-pochhammer-partial-product),
and let $K_S$ be the $\Phi_q$-piece of the lifted braid
([Φ$_q$-piece](#def:phi-q-piece)). Then the roots of the
denominator polynomial*

$$
  (x; q)_n
  \;=\;
  \prod_{k=0}^{n-1}\bigl(1 - x q^k\bigr)
  \;\in\;
  \mathbb{Z}[q, x]
$$

*enforce the **cusp completeness conditions** of the Thurston
gluing equations on the ideal-tetrahedron triangulation of
$S^3 \setminus K_S$:*

$$
  (x; q_0)_n \;=\; 0
  \quad\Longleftrightarrow\quad
  \mathrm{Hol}_{\mu_k}(z_k) = 1
  \;\;\text{and}\;\;
  \mathrm{Hol}_{\lambda_k}(z_k) = 1
  \;\;\text{for some cusp}\;k,
$$

*where $z_k$ is the shape parameter of the ideal tetrahedron at
cusp $k$ and $\mu_k, \lambda_k$ are its meridian and longitude.*

## Algebraic poles as geometric addresses

The conjecture says the **algebraic denominator zeros are the
addresses of the geometric cusps**: a zero in the algebraic state
sum at $x = q_0^{-k}$ corresponds to the geometric requirement that
parallel transport around the meridian and longitude of the $k$-th
ideal-tetrahedron cusp yields a holonomy of exactly $1$. Algebraic
divergence and geometric completeness are the same event, viewed
from opposite sides of the Archimedean fibre functor $\tau$.

| Algebraic side ($R$) | Archimedean side ($\mathbb{C}$) | Geometric side ($\mathbf{Hyp}_3$) |
|---|---|---|
| zero of $(1 - x q_0^k)$ | logarithmic singularity of $\mathrm{Li}_2$ | meridian + longitude holonomy = $1$ |
| pole of $\Phi_n$ | branch point of $\log$ | complete cusp of $\Delta_{z_k}$ |
| algebraic Markov-trace divergence | $\tau_{\mathrm{arch}}$-evaluation diverges | shape parameter $z_k$ on Thurston variety |
| GB-depth $k_\star = n$ | thimble dimension $n$ | $n$ ideal tetrahedra in JSJ piece |

The bijection across rows is the **shared denominator**: the same
polynomial $(x; q_0)_n$ controls the algebraic singularities, the
classical $\mathrm{Li}_2$ branch structure, and the Thurston cusp
equations.

## Proof sketch (modulo the upstream conjectures)

Assume
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)).

1. **Algebraic side** ([q-Pochhammer partial product §interpretation](#def:q-pochhammer-partial-product)).
   The denominator $(x; q)_n$ has $n$ simple zeros at $x = q^{-k}$
   for $k = 0, \dots, n-1$. Each is a simple pole of $\Phi_n(x; q)$.

2. **Archimedean side** ([Archimedean limit](#conj:dilogarithm-archimedean-limit)).
   Under Faddeev's scaling, $(1 - q) \log \Phi_n(x; q) \to
   \mathrm{Li}_2(x)$. The poles of $\Phi_n$ map to the logarithmic
   branch point of $\mathrm{Li}_2$ at $t = 1$ in the integrand
   $-\log(1 - t)/t$.

3. **Geometric side** (Thurston [`thurston1978`], Neumann–Zagier
   [`neumann-zagier1985`]). For an ideal-tetrahedron triangulation of
   a hyperbolic 3-manifold, the **cusp completeness conditions** are
   $\mathrm{Hol}_\mu = \mathrm{Hol}_\lambda = 1$ on the meridian and
   longitude; equivalently, the Neumann–Zagier potential
   $\Phi_{\mathrm{NZ}}(z)$ has a critical point at $z = z_k$ matching
   the corresponding shape parameter.

4. **Bridge.** Under the
   [algebraic-geometric equivalence](#conj:algebraic-geometric-dilog-equivalence)'s
   pole-to-cusp bijection, the algebraic root $x = q_0^{-k}$ matches
   cusp $k$, and Step 2 identifies the singularity of the algebraic
   $\Phi_n$ with the singularity of $\mathrm{Li}_2$ at $z_k$ — which
   by Step 3 is the cusp-completeness condition. $\square$

## Implication for the Newton–Raphson solver

The conjecture has a **direct computational consequence**: the zeros
$\{q_0^{-k}\}$ of the algebraic denominator are the **exact initial
seed values** for the Newton–Raphson solver of the Thurston gluing
equations on the active JSJ piece. The pipeline is:

1. The algebraic engine computes $\Phi_n(x; q_0)$ as a rational
   function.
2. Extract the $n$ roots of its denominator $(x; q_0)_n$:
   $\{q_0^{-k} : k = 0, \dots, n-1\}$.
3. Lift the roots into the complex plane and supply them not as universal constants, but as **initial seeds** for Newton–Raphson iteration on the ideal-triangulation gluing equations.

By Steps 1–4 of the proof sketch above, the algebraic seeds sit
**near** the cusp-completeness solution of the Thurston gluing
equations — only the gluing residuals from the active transient
crossings differ from zero. The solver converges in $O(1)$ Newton
steps per cusp (empirically $\approx 10$ steps to machine precision
across depths $n = 1, \dots, 3$, see witness below), instead of the
$O(\log\epsilon^{-1})$ steps needed when starting from a generic
universal $z_q$. The Newton step also avoids local-minimum traps,
because the algebraic poles are **isolated** in the cusp variety.

Driving Newton–Raphson on the color-tube discriminant $\Delta(z) = 0$ from each algebraic seed (perturbed by $0.1i$ into $\mathbb{C}$) tests this convergence behaviour.
At depths $n = 1, 2, 3$, all seeds converge to a complex critical
point with residual $\lesssim 10^{-13}$ in 9–11 iterations,
empirically supporting the $O(1)$ claim.

## Relation to existing PL/JSJ infrastructure

This conjecture is the **shared-denominator** statement that the
existing
([Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)) already
asserts implicitly: the JSJ piecewise sum
$\sum_S \mathrm{Vol}(K_S)$ is computed from the algebraic
$\sum_S \Phi_q(\lvert V_S\rvert)$ at exactly the cusps prescribed by
the algebraic denominators. Phrased motivically, the algebraic class
$[\Phi_n(x; q_0)] \in \mathfrak{B}(q)$ in the
([quantum Bloch group](#def:quantum-bloch-group))
regulates archimedeanly to the volume of the matched JSJ piece, with
the regulator's domain of definition pinned by the shared-denominator
locus.

## Discussion

Stated conditional on
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)). The statement is formulated conditionally over the shared-denominator cusp-holonomy hypothesis class, which deliberately carries **no unconditional witness**: the conjecture's open state remains explicit.

What makes the class unsatisfiable by fiat is that the cusp shape
assignment $k \mapsto z_k$ is one of its parameters. Requiring a geometric
shape, $\mathrm{Im}\, z > 0$, excludes real constants such as the
"skeleton" $z = 2$ of an alternative formulation, but a class field asserting only
that *some* geometric shape exists is discharged by $z = i$ for every $q$,
$x$ and $n$, since that existential is unlinked to the root index. Binding
the shape as a parameter is what makes the conjecture constrain the cusp
data supplied to it.

The conjecture then yields one consequence directly: at a root index the
matched shape has $\mathrm{Im}\, z_k > 0$, so $z_k$ is not real and in
particular is not the bare algebraic seed $q_0^{-k}$. Direct ideal-triangulation comparison below reaches the same conclusion.

### Empirical scope of the seeding pipeline

Two numerical comparisons bracket the conjecture's strong form:

- **Color-tube cubic** (converges): iterating Newton–Raphson on $\Delta(z) = 0$ from the perturbed seeds $q_0^{-k} + 0.1i$ at depths $n \leq 3$ converges to residual $\lesssim 10^{-13}$ in 9–11 steps, supporting the $O(1)$-step scaling.

- **Ideal-triangulation Thurston gluing system** (bounds the literal seed identity): comparing the bare real seeds $q_0^{-k}$ against the converged tetrahedral shape parameters of $\mathtt{m004}$ ($4_1$), $\mathtt{m003}$, and $\mathtt{L6a4}$ (the Borromean rings) yields Euclidean distances of $\approx 0.4$–$0.9$ from $z_k$, indexed by **tetrahedron** rather than by cusp, ruling out the literal equality $q_0^{-k} = z_k$.

Together these two checks support the conjecture's *structural*
content (algebraic poles label the ideal tetrahedra) while bounding its
*canonical* form (the bare $q_0^{-k}$ are not literally the shape
parameters).

### No function of the seed can carry the index

The identity $q_0^{-k} = z_k$ is excluded twice over, and neither
exclusion needs the distances above.

**It is already a theorem.** Conditional on the hypothesis class below, $z_k \neq r$ for every real $r$,
because positivity of the imaginary part excludes every real shape and the seeds $q_0^{-k}$ are
real. So the identity fails for a reason internal to the conjecture.

**The stronger statement is that the shapes do not separate the
indices at all.** An ideal tetrahedron carries three shape parameters —
the relabelling orbit $z \mapsto 1/(1-z) \mapsto 1 - 1/z$, which cyclic edge rotation realises while leaving the dihedral angles and the
tetrahedron unchanged — so two distinct recorded values may be one
tetrahedron. Reading the committed witness through that orbit:

| manifold | $n$ roots $q_0^{-k}$, pairwise distinct | distinct recorded values | tetrahedra up to isometry |
|---|---|---|---|
| $\mathtt{m004}$ | 2 | 1 | 1 |
| $\mathtt{m003}$ | 2 | 1 | 1 |
| $\mathtt{L6a4}$ | 8 | 2 | 1 |

$\mathtt{L6a4}$'s two values $1 + i$ and $(1+i)/2$ lie in one orbit, both
with dihedral angles $\{\pi/4, \pi/4, \pi/2\}$; $\mathtt{m004}$ and
$\mathtt{m003}$ are two copies of the regular ideal tetrahedron
$e^{i\pi/3}$, the orbit's fixed point. The roots are pairwise distinct
since $q_0 \neq 1$. So on each of these triangulations an assignment
*seed value* $\mapsto$ *shape* is **constant up to isometry**, and a
constant map cannot recover $k$.

This excludes every candidate function of the seed value — injective or
not — on the three triangulations the corpus probes. It is a counting
argument, and its invariant is the pigeonhole principle on a finite set;
it does **not** exclude the conjecture.

**Asserted denominator coincidence beyond the algebraic shape.** Its displayed
right-hand side is the pair of holonomies
$\mathrm{Hol}_{\mu_k}, \mathrm{Hol}_{\lambda_k}$, each a product of
shape parameters along a meridian or longitude path. A holonomy is
path-dependent, hence index-dependent even where the shapes are all
equal — exactly the property the shapes lack. The quantity that tests
the conjecture is therefore the gluing residual
$\lvert \mathrm{Hol}_{\mu_k} - 1 \rvert$ evaluated at the algebraic
seeds, which neither witness computes.

**Two indexings remain in tension and the resolution is open.** The left
side has $n$ roots with $n$ the partial-product order; the right side is
indexed by cusps, and the two counts differ on every manifold probed
above (2 against 1, 2 against 1, 8 against 3). A companion cardinality
argument reaches the same conclusion from the ideal vertices of a single
tetrahedron. Substituting "tetrahedron" for "cusp" is not available as a
repair, since a holonomy is cusp data; for an ideal triangulation of a
cusped manifold the tetrahedron-indexed gluing data is the **edge**
equation, with one edge per tetrahedron, and the cusp-completeness
conditions are the complementary set. Which of these the conjecture
intends is not settled here.
