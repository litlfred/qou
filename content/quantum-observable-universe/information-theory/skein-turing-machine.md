A Turing machine computation of $N$ gates encodes as a braid
$\beta$ on $n$ strands with $c = 3N$ crossings — three per
Toffoli gate
([q-AND](#rem\:toffoli-q-and)).  Closing the braid gives a
link $L = \hat{\beta}$ whose Skein polynomial $P_L(q)$ is
the **output** of the computation
([transfer matrix product](#prop\:skein-polynomial-transfer-matrix)).

**The Skein decomposition is the discrete path integral.**

At each crossing of $L$, the Skein relation resolves the
link into three branches:

$$
  q  L_+ -  q^{-1} L_- =  s  L_0
$$

where $s = q^{1/2} - q^{-1/2}$.  Each resolution replaces
one crossing with one of three outcomes: positive ($L_+$),
negative ($L_-$), or smoothed ($L_0$).  Iterating over all
$c$ crossings produces a **resolution tree** with $3^c$
leaves — one per discrete history of the computation.

This is the **path integral at Planck resolution**:

| Path integral                | Skein decomposition                                             |
| ---------------------------- | --------------------------------------------------------------- |
| History                      | Resolution path through the tree                                |
| Action weight $e^{iS/\hbar}$ | Skein weight $q^{\pm 1}$ or $s$ per crossing                    |
| Partition function $Z$       | Skein polynomial $P_L(q) = \sum_{\text{paths}}(\text{weights})$ |
| Path integral measure        | Markov trace $\mathrm{tr}_M$                                    |
| Planck time step             | One crossing resolution                                         |

Each resolution is one Planck step
([discrete Planck step](#rem\:discrete-planck-step)).  Each
path through the tree is one discrete history of the
universe at the resolution of one crossing.  The Skein
polynomial is the sum over all $3^c$ histories, weighted by
their crossing signs — the partition function of the
computation.

**Information before and after the trace.**

Before the Markov trace, the braid word $\beta \in H_n(q)$
retains the full fine structure: which generators, in which
order, with which crossing types.  This is $O(N \log n)$
bits — the gate addresses of the computation.

After the trace, the Skein polynomial $P_L(q)$ has degree
$\leq c^2 - 1$ but is computed in factored form:

$$
  P_L(q) = \prod_{i=0}^{n-2} \hat{V}_i(q)
$$

This compression from $3^c$ paths to $O(c)$ factors is the
**selective erasure** of internal wiring: which resolution
path was taken — which history the universe followed — is
lost.  What survives is the topological invariant: the
computation's output.

The Markov trace is observation.  It collapses $3^c$ quantum
paths to one polynomial.

**The backward flow.**

Start from a section $E \in \Gamma(M, \mathcal{S})$ — the
output state of the computation.  Resolve each crossing via
the Skein relation, one gate at a time, flowing backward
through the jet tower
([jet–Planck steps](#rem\:jet-planck-steps)):

* After $1$ resolution: the last gate is undone.
* After $3N$ resolutions: complete unwinding —
  arrival at the Big Bang initial conditions
  $\mathcal{S}_0 = \sum_i (p_i, H_i)$
  ([bundle initial conditions](#def\:bundle-initial-conditions)).

By :refterm[descent]{#descent}
([:refterm[descent]{#descent} involution](#def\:descent-involution)), all
branches of the resolution tree flow back to
$\mathcal{S}_0$.  The initial conditions **are** the
program.  The braid **is** the computation.  The Skein
polynomial **is** the output.

**Quantum computations.**

A section $E$ that factors through a finite braid word is
**computable**: it is reachable from $\mathcal{S}_0$ by a
finite number of Toffoli gates, each executing in $3$ Planck
steps.  The set of all such $E$ is the computable fragment
of the QOU — the sections that can be written as finite
products of transfer matrices.

Sections that do not factor through any finite braid require
infinite crossing number — infinite jet order — and are
**never resolvable**.  They are the non-computable bundles:
states of the universe that no finite sequence of logic
gates, however long, can produce from the Big Bang.

The distinction between computable and non-computable $E$ is
not a choice — it is a topological property of the section,
determined by whether its Skein polynomial has finite degree.
