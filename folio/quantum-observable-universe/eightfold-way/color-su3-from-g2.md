*The discrete color symmetry $\mathrm{PSL}(2,7) \cong \mathrm{GL}(3,\mathbb{F}_2)$
and the continuous Lie stabilizer $\mathfrak{su}(3) = \ker(\mathrm{ev}_e) \subset
\mathfrak{g}_2 = \mathrm{Der}(\mathbb{O})$ of dimension $8$ arise from the octonionic
automorphism group $G_2$ via the Fano plane, whose incidence structure
encodes the octonion multiplication table.  While the Hurwitz automorphism
group $\mathrm{Aut}(\Sigma_4) \cong S_5$, first Betti number $b_1(\Sigma_4) = 8$,
and Euler characteristic $\chi_{\mathrm{eu}}(\Sigma_4) = -6$ of the genus-$4$
Bring surface are proved independently, the octonion algebra $\mathbb{O}$ enters
as an algebraic module not yet generated from the single-fibre ($N = 2$)
substrate, and the single-node non-separating pinch attempting to degenerate
Bring's surface directly onto the genus-$3$ Klein quartic via the common subgroup
$S_4 \subset S_5 \cap \mathrm{PSL}(2,7)$ is structurally excluded below.*

**The $S_4$ bridge mechanism.**
The Bring surface $\Sigma_4$ (genus 4) has automorphism group $S_5$.
The Klein quartic $\Sigma_3$ (genus 3) has automorphism group
$\mathrm{PSL}(2,7)$ of order $168 = 84(3-1)$, the Hurwitz bound.
The group $S_4$ is the maximal common subgroup:

1. $S_4 \subset S_5$ as the stabilizer of one letter (index 5).
2. $S_4 \cong \mathrm{Stab}(\mathrm{pt})$ in $\mathrm{PSL}(2,7)$
   acting on the 7 Fano points (index 7).

The point stabilizer $S_4$ preserves the *local Fano structure*
at the fixed point: the 3 lines through that point, encoding the 3
octonion multiplication triples involving the corresponding imaginary
unit.  By finite-group orbit decomposition:

- $S_4$ acts transitively on the 3 lines through the fixed point,
- $S_4$ acts transitively on the 4 lines not through the fixed point,
- $S_4$ acts transitively on the 6 remaining Fano points,
- the 3 local lines partition the 6 remaining points into 3 pairs.

**Conjectured genus degeneration.**
The derivation chain from Bring to Fano is:
$$
  \underbrace{\Sigma_4}_{g=4,\; S_5}
  \;\xrightarrow{\text{pinch}}\;
  \underbrace{\Sigma_3^{\mathrm{nod}}}_{g_{\mathrm{arith}}=4,\; S_4}
  \;\xrightarrow{\text{normalize}}\;
  \underbrace{\Sigma_3}_{g=3,\; \mathrm{PSL}(2,7)}
$$
Pinching an $S_4$-invariant 1-cycle on $\Sigma_4$ produces a nodal curve
of arithmetic genus 4 but geometric genus 3.  The $S_4$ symmetry
survives the pinch (it fixes the vanishing cycle).  On the
normalization $\Sigma_3$ of genus 3, the Hurwitz bound gives
$|\mathrm{Aut}| \leq 84(3-1) = 168$, which $\mathrm{PSL}(2,7)$ attains.

**The gap in this argument.**  The Hurwitz bound is an
*upper* bound; it does not force the automorphism group to be
$\mathrm{PSL}(2,7)$, and the generic genus-3 curve has small or trivial
automorphism group.  That $S_4$ embeds in $\mathrm{PSL}(2,7)$ as a point
stabilizer shows the enhancement is *available*, not that it
*occurs*: nothing here rules out the normalization being a genus-3
curve whose automorphism group is exactly $S_4$, or any other group
containing $S_4$.  Maximality of the enhancement does not select it.

**The $S_4$ bridge cannot select the Klein quartic.**
A stronger negative than the Hurwitz error: the $S_4$ datum has no
separating power at all.  The Fermat quartic $x^4 + y^4 + z^4 = 0$ is a
genus-3 curve whose automorphism group $(\mathbb{Z}/4)^2 \rtimes S_3$ of
order $96$ *also* contains $S_4$ --- exhibited as $V_4 \rtimes S_3$
in exact $\mathbb{Z}[i]$ arithmetic (element-order profile
$\{1{:}1,\, 2{:}9,\, 3{:}8,\, 4{:}6\}$, with $V_4$ normal and $S_3$ inducing the
full symmetric action on $V_4 \setminus \{1\}$).  So even a fully correct
argument that the normalization has genus $3$ and inherits $S_4$ stops
short of the Klein quartic, because at least one other genus-3 curve
satisfies both conditions.

**The competitor set is in fact infinite.**  Fermat is not an
isolated coincidence.  The $S_4$-invariant ternary quartics form a
two-dimensional space, so the genus-3 curves admitting $S_4$ contain an
entire *pencil*

$$
C_t : x^4 + y^4 + z^4 + t\,(x^2 y^2 + y^2 z^2 + z^2 x^2) = 0 ,
$$

with parameter $t$ (not $\lambda$, which throughout this chapter denotes a
partition), smooth --- hence of genus $3$ --- for every $t$ outside
$\{2,\, -2,\, -1\}$, with Fermat the single member $t = 0$.  The
fibres of $t \mapsto [C_t]$ in moduli are finite, so
infinitely many pairwise non-isomorphic genus-3 curves carry a faithful
$S_4$ action.  This follows in exact rational
arithmetic using only
*finiteness* of the automorphism group --- the sharp Hurwitz
bound is deliberately avoided here, for the reason given above.  The
$S_4$ bridge therefore fails not only to choose between two
candidates, but to cut a $\mathbb{P}^1$ down at all.

Identifying the normalization therefore cannot be reduced to telling
Klein and Fermat apart.  Many invariants do that --- the
automorphism-group order alone separates them, $168$ against $96$ ---
while saying nothing about the rest of the family, and nothing whatever
about which member the pinch produces.  What is required is an invariant
that the *degeneration itself determines*: read off the pinched
cycle and the nodal curve, rather than computed from a shortlist of
candidate targets.  The decisive version is the period matrix.  None has
been computed.  This is a scope-(a) negative: the degeneration itself is
not refuted, only the argument offered for it.

**The marked points obstruct the degeneration.**
There is extra data the pinch does supply, and it settles the question ---
against the conjecture.  Pinching a single *non-separating* cycle on a
genus-4 curve yields a one-node curve of arithmetic genus $4$ whose
normalization has genus $3$ *together with two marked points* --- the
two preimages of the node, consistent with $3 + 1 = 4$.  Since the pinched
cycle is $S_4$-invariant, $S_4$ preserves that pair setwise, so the object
the degeneration produces is a pair $(\Sigma_3, \{p, q\})$ with an
$S_4$-stable point pair, not a bare genus-3 curve.

No smooth plane quartic admits such a pair.  Let $\{p, q\}$ be $S_4$-stable;
permuting it gives a homomorphism $S_4 \to S_2$ whose kernel has index $1$ or
$2$, hence is $S_4$ itself or the unique index-2 subgroup $A_4$.  Either way
the line through $p$ is an invariant $1$-dimensional subspace of
$\mathbb{C}^3$.  But the $3$-dimensional representation of $S_4$ is absolutely
irreducible, and so is its restriction to $A_4$ --- each established both
by commutant dimension and by character norm.  An absolutely irreducible
representation has no invariant line over any extension field, so no such
pair exists: $S_4$ has *no orbit of size $\le 2$* on $\mathbb{P}^2$ at
all.

Consequently, under the three premises this chain itself asserts --- one
$S_4$-invariant non-separating cycle (which is what arithmetic genus $4$ and
geometric genus $3$ mean), $S_4$ acting faithfully on the normalization
(which is what "$S_4$ survives" means), and a non-hyperelliptic
normalization (which the Klein quartic is) --- the required configuration
does not exist.  This is a scope-(b) *structural exclusion*, licensed by
a proved invariant rather than by a numerical near-miss, and unlike the two
earlier failures it bears on the conjecture rather than on an argument
for it.

What remains are the escapes, named precisely.  A
*hyperelliptic* genus-3 normalization is not excluded: its canonical map
is $2$-to-$1$ onto a conic, so its automorphisms do not act through
$\mathrm{PGL}_3$ in the manner above, and such curves admitting $S_4$ do
exist.  The Klein quartic is not hyperelliptic, so that escape does not
recover it.  Nor is a pinch with several nodes or of a separating cycle
excluded --- but either is a different claim from the one made here.  What
the argument does not touch at all is the Bring surface: it constrains the
target, not the source.

**Status:** the $S_4$ incidence action on the local Fano data holds as an
exact finite-group identity, and the genus-$4$ Hurwitz and homology invariants
of $\Sigma_4$ together with the $\dim = 8$ octonionic derivation stabilizer
$\mathfrak{su}(3) = \ker(\mathrm{ev}_e) \subset \mathfrak{g}_2$ stand
unconditionally.  The single-node non-separating genus degeneration step is a
different matter: under its own three premises it is *excluded*.  A pinch of the
kind described cannot deliver a non-hyperelliptic genus-3 normalization, and
the Klein quartic is non-hyperelliptic.  Rescuing a geometric $\Sigma_4 \to \Sigma_3$
pinch therefore requires giving up one of the three premises explicitly --- a
hyperelliptic target, a multi-node or separating pinch, or a non-faithful $S_4$
--- while coupling the octonionic rank-$2$ color triple $\mathbf{3}$ to the
three-strand Hecke state space requires a multi-fibre or rank-$2$ HOMFLY-PT
$(V_2 \oplus V_3)$ extension beyond the single $\dim \Lambda^2 V = 1$ ($N = 2$)
strand.

**$\mathrm{PSL}(2,7)$ representation theory.**
The finite simple group $\mathrm{PSL}(2,7) \cong \mathrm{GL}(3, \mathbb{F}_2)$ has
6 conjugacy classes and 6 irreducible representations of dimensions

```tex
\begin{equation}\label{eq:psl27-irreps}
  \{1, 3, \bar{3}, 6, 7, 8\},
  \qquad
  \sum d_i^2 = 1 + 9 + 9 + 36 + 49 + 64 = 168 = |\mathrm{PSL}(2,7)|.
\end{equation}
```

The physical interpretation:

| $\dim$ | Representation | Physical role |
|---|---|---|
| $1$ | trivial | singlet |
| $3$ | fundamental | color triplet ($q$) |
| $\bar{3}$ | conjugate | color antitriplet ($\bar{q}$) |
| $6$ | $\mathrm{Sym}^2(\mathbf{3})$ | no singlet $\Rightarrow$ complex type |
| $7$ | natural on $\mathrm{Im}(\mathbb{O})$ | imaginary octonions |
| $8$ | adjoint of $\mathrm{SU}(3)_{\mathrm{c}}$ | gluon octet |

The 3 and $\bar{3}$ are complex conjugate (not self-dual), matching
the Günaydin--Gürsey decomposition
$\mathrm{Im}(\mathbb{O}) \cong \mathbb{R} \oplus \mathbb{C}^3$
under $\mathrm{SU}(3)_{\mathrm{c}} \subset G_2$ \cite{gunaydin-gursey1973}.
Non-self-duality is what the $\mathrm{Sym}^2$ gate consumes, so this is a
load-bearing citation rather than an attribution: a self-dual $3$ would
carry a singlet in $\mathrm{Sym}^2$ and fail the gate.
