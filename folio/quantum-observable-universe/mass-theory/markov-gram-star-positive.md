*Let $T_w^{*} = T_{w^{-1}}$ be the Hecke star and let*

$$
  S_{ij} \;=\; \mathrm{tr}_M\!\bigl(b_i\,b_j^{*}\bigr)
$$

*be the Gram matrix of the Markov trace on the normal-form basis
$b \in \{\gamma,\, \sigma_0,\, \sigma_1,\, L_+,\, L_-,\, e^{-}\}$ of $H_3(q)$. Then
$S$ is positive semidefinite whenever every Wedderburn weight satisfies
$y_\lambda \ge 0$, and its kernel is spanned by the blocks with $y_\lambda = 0$.*

## Positivity is a block computation, not a measurement

Wedderburn decomposes $H_3(q)$ into matrix algebras, one per partition, and the
Markov trace acts on the block of $\lambda$ as $y_\lambda$ times the matrix trace.
The star form therefore splits as

$$
  \mathrm{tr}_M(a\,a^{*}) \;=\; \sum_{\lambda \vdash 3} y_\lambda \cdot
  \mathrm{tr}\!\bigl(A_\lambda A_\lambda^{*}\bigr),
$$

and on each $M_d$ the sesquilinear trace $\mathrm{tr}(AA^{*})$ is the sum of the
squares of the matrix entries. A nonnegative combination of sums of squares is
nonnegative, and it vanishes only when every block with $y_\lambda > 0$ vanishes.
Positivity of the whole form is thus equivalent to nonnegativity of the weights, and
the degeneracy locus is exactly the set of blocks the trace kills.

Two consequences follow for $H_3(q)$ without any numerical input.

- Under convention C every weight is strictly positive, so $S$ is positive definite:
  signature $(6,0,0)$.
- Under convention D the weight of $(1^{3})$ is zero, so $S$ acquires a
  one-dimensional kernel and nothing else: signature $(5,0,1)$.

The kernel under convention D is the row cap seen through the pairing. Quotienting by
it leaves a genuine inner product, which is what a Rieffel Lipschitz seminorm
requires.

## The star is what makes the form positive

Positivity is a statement about the *star* pairing and about no other. The Hecke star
sends the basis element of a word to the basis element of its inverse, which on the
normal-form basis swaps $L_+ \leftrightarrow L_-$ and fixes the remaining four
vectors. That single swap flips the sign of the one antisymmetric direction in the
mixed-symmetry block, and the sign it flips is the whole difference between the two
pairings. No signature
claim about the Markov--Gram form is meaningful until the pairing is named.

**Archimedean specialisation.** What follows sits on the archimedean side of the
substrate wall: it invokes real- or complex-analytic constructs --- real-valued
physical observables, real-analytic bounds, transcendental constants, or numerical
evaluation at the substrate parameter $q_0$. Any generic categorical or
$q$-deformation identities it draws on remain valid over an abstract coefficient ring;
only their archimedean realisation is specialised here. At $q_0$ the star form has
eigenvalues $0.855067$ (fourfold), $0.101797$ and $3.476950$ under convention C, and
$0$, $0.752702$ (threefold) and $4.230339$ under convention D. The repeated magnitude
under convention D is $\mu_+ = 0.75270211325196540159$, the $T = 1$ isospin projector
scalar; the isolated $0.101797$ under convention C is the $(1^{3})$ block, small
because $y_{(1^{3})} = 0.0227449$ is small.
