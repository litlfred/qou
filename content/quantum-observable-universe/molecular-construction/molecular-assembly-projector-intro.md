A molecule is a composite braid: $k$ sub-units (atoms, or smaller
fragments) assembled into a single word in $H_N(q)$, where $N$ is the
total strand count.  Before specialising to any one molecule, we record
the *general* algebraic structure that the assembly forces — structure
that does not depend on knowing the chemistry in advance.

The $k$ sub-units determine a **strand-partition** $\lambda =
(n_1,\dots,n_k)$ with $\sum_i n_i = N$, and the assembly factors through
the **parabolic (Young) subalgebra** $H_\lambda(q) = H_{n_1}(q) \otimes
\cdots \otimes H_{n_k}(q) \hookrightarrow H_N(q)$.  Every such
factorisation carries canonical **assembly projectors** onto the
Wedderburn blocks of $H_N(q)$; projection onto the *symmetric* block is
delocalisation.

Three things must be kept strictly distinct — conflating them is the
"post-justification" trap:

1. **Existence** of the projector is pure algebra — true for every
   $\lambda$, carrying no energy claim.
2. **Optimality** (which block the molecule actually occupies) is the
   *physics*, selected by the binding LP/SDP.
3. **Energetics**: the binding energy is the trace-weight *gap* between
   the selected block and the next configuration.

Benzene is recovered as the special case $\lambda = (2,2,2)$ (three
acetylene sub-units on six carbons), but the definitions below are
stated for arbitrary $\lambda$, and the same machinery applies to
$\mathrm{CH_4}$, $\mathrm{CO_2}$, and the other molecules of this
chapter.
