The nuclear ground state is the nucleon ordering that minimises
the quantum dilogarithm volume $\Phi_q = \sum_i \log|\hat{V}_i|$
of the transfer matrix chain.  The ordering is determined by
the **eigenvalue structure** of the three typed transfer matrices.

## Transfer matrix eigenvalues

The three transfer matrices
([transfer matrix](#prop:beta-decay-transfer-matrix)) have
eigenvalues determined by the typed crossing operators
([typed crossings](#def:typed-crossing-operator)):

See [Table 1](#tbl:ground-state-ordering-table1-data).

where $h = q - q^{-1}$.

**Key symmetry**: $T_{nn}$ is the $q \leftrightarrow q^{-1}$
mirror of $T_{pp}$.  Their eigenvalues are swapped:
$\lambda_\pm(T_{nn}) = \lambda_\mp(T_{pp})$.  The mixed matrix
$T_{pn}$ has **zero trace** and equal-magnitude eigenvalues
$\pm\sqrt{1 + h^2/4} \approx \pm 1.005$.

## Ground-state rule

**Proposition.**
*The nuclear ground state ordering for a nucleus with $Z$ protons
and $N$ neutrons ($A = Z + N$) is determined by:*

**(i) Interleaving.**  *Alternate protons and neutrons in adjacent
positions.  For $Z \leq N$: neutrons at even positions
($0, 2, 4, \ldots$), protons at odd positions
($1, 3, 5, \ldots$).*

**(ii) Tail packing.**  *Place excess neutrons ($N - Z$ of them)
at the highest positions ($2Z, 2Z+1, \ldots, A-1$), forming
$nn$ pairs at the high generators.*

**(iii) Boundary correction.**  *For small $A$ ($A \leq 3$), the
sorted ordering (all protons first) beats interleaving because
the chain is too short for the interleaved eigenvalue
cancellation to dominate.*

*Formally, for $Z \leq N$ and $A \geq 4$:*

$$
  \mathrm{ordering}[k]
  =
  \begin{cases}
    1 \text{ (proton)} & k \text{ odd}, \; k < 2Z \\
    0 \text{ (neutron)} & \text{otherwise}
  \end{cases}
$$

## Minimisation of $\Phi_q$ under interleaving

The vertex volume at generator $i$ is
$\hat{V}_i = z \cdot a_i + b_i$, where $(a_i, b_i)$ is the
chain-reduced transfer matrix state.  The chain at generator $i$
multiplies transfer matrices for all crossings with strands
$j > i$.

Each $T_{pp}$ contributes dominant eigenvalue $+q \approx 1.110$
(growth).  Each $T_{nn}$ contributes $+q^{-1} \approx 0.901$
(decay).  The interleaved arrangement alternates growth and
decay factors, producing destructive interference that drives
$|\hat{V}_i|$ below $1$ at most generators.

In contrast:
- **Sorted** (all protons first): generators $0, \ldots, Z-2$
  see only $T_{pp}$ crossings (pure growth), producing
  $|\hat{V}_i| > 1$ (no binding).  Generators $Z, \ldots, A-2$
  see only $T_{nn}$ (pure decay), but the accumulated growth
  from early generators limits the total binding.

- **Interleaved**: every generator sees a mix of $T_{pp}$, $T_{pn}$,
  $T_{nn}$ crossings.  The alternating $q$ and $q^{-1}$ eigenvalues
  cancel partially at each step, keeping $|\hat{V}_i|$ close to
  (and often below) $1$ throughout the chain.

The $T_{pn}$ matrix has zero trace, meaning its contributions
average to zero over many chain steps.  The interleaved
arrangement maximises the fraction of $T_{pn}$ crossings,
which act as **neutral spacers** between the binding $T_{nn}$
and anti-binding $T_{pp}$ contributions.

## Verified ground states

Exhaustive search over all $\binom{A}{Z}$ orderings confirms
the derived rule for $A \leq 14$:

See [Table 2](#tbl:ground-state-ordering-table2-data).

The sorted ordering (protons first) is optimal only for
$A \leq 3$, where the chain is too short for eigenvalue
cancellation to develop.  For $A \geq 4$, interleaving
dominates by factors of $2\text{--}10\times$ in $|\Phi_q|$.

## Connection to the Gram matrix

The transfer matrix eigenvalues are the Gram matrix entries
in disguise: $\lambda_+(T_{pp}) = q$ and $\lambda_+(T_{nn}) = q^{-1}$
are the braiding eigenvalues from the Hecke relation
$(T - q)(T + q^{-1}) = 0$.  The ground-state ordering maximises
the destructive interference between these eigenvalues,
which is equivalent to minimising the Frobenius norm
$\|\mathrm{NF}(\mathcal{N})\|_F$ of the nuclear configuration
in the Gram matrix inner product.

## Scalability

For $A > 14$, exhaustive search over $\binom{A}{Z}$ orderings is
infeasible.  The derived rule provides an $O(A)$ construction:
interleave protons at odd positions $1, 3, \ldots, 2Z-1$ and
pack excess neutrons at positions $2Z, \ldots, A-1$.  This
matches the exhaustive ground state for all verified cases
($A \leq 14$, except $A \leq 3$ where sorting wins).

For $A \leq 3$: use sorted (protons first).
For $A \geq 4$: use interleaved + tail packing.
