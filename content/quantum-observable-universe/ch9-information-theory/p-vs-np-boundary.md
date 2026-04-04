**Conjecture ($\mathrm{P} \neq \mathrm{NP}$ as boundary condition).**
*There exist decision problems whose braid encodings
$L = \hat{\beta}$ possess computational horizons
([computational horizon](#def:computational-horizon)) — jet
horizons in the resolution tree $\mathcal{R}(L)$ across which
the degree-$0$ answer $P_L(q_0)$ cannot be extracted in
$\mathrm{poly}(c)$ Planck steps.*

*Equivalently: $\mathrm{P} \neq \mathrm{NP}$ if and only if
there exist braids whose Skein resolution trees have
**irreducible exponential weight** — resolution trees where the
$3^c$ histories do not destructively interfere down to
polynomial effective size.*

**Reformulation as a boundary condition.**

The classical statement of $\mathrm{P}$ vs $\mathrm{NP}$ asks
whether every problem whose solutions can be verified quickly
can also be solved quickly \cite{cook1971}.  In the QOU
framework, this becomes a question about the **permeability of
the jet horizon** applied to computation:

$$
  \boxed{
    \mathrm{P} = \mathrm{NP}
    \;\;\Longleftrightarrow\;\;
    \text{every computational horizon is transparent}
  }
$$

where "transparent" means the degree-$0$ observable (the answer)
can be reconstructed from a polynomial-depth sample of the
degree $\geq 1$ data (the witnesses).

**The three equivalent viewpoints.**

1. **Information-theoretic.**  $\mathrm{P} \neq \mathrm{NP}$
   means there exist computations whose information content
   exceeds the polynomial bandwidth budget
   ([bandwidth bound](#prop:p-bandwidth-bound)).  The $3^c$
   resolution paths carry $c \cdot \log 3$ nats of raw
   information; in NP-complete problems, this information does
   not compress below exponential size under the Markov trace.
   The degree-$0$ answer requires aggregating exponentially many
   degree $\geq 1$ witnesses.

2. **Topological.**  $\mathrm{P} \neq \mathrm{NP}$ means there
   exist braid closures $L$ whose Skein polynomials $P_L(q)$ do
   not factor into $\mathrm{poly}(c)$ terms.  The factored form
   $\prod_i \hat{V}_i(q)$ requires $\omega(\mathrm{poly}(c))$
   factors — the link $L$ has irreducible topological complexity
   that no polynomial-time process can decompose.

3. **Gravitational (boundary condition).**  $\mathrm{P} \neq
   \mathrm{NP}$ means the computational horizon is a genuine
   event horizon: the exponential interior of the resolution
   tree is **causally disconnected** from the polynomial
   exterior.  The degree-$0$ answer is behind the horizon.  A
   polynomial-time observer can sample degree $\geq 1$ data
   (verify witnesses), but cannot reconstruct the degree-$0$
   observable — exactly as a Schwarzschild observer receives
   Hawking radiation (degree $\geq 1$ thermal data) but cannot
   recover the infalling state (degree-$0$ particle identity).

**The Planck step argument.**

Consider a braid $\beta$ with $c$ crossings encoding an
NP-complete problem (e.g., Hamiltonian path encoded as a
link \cite{freedman2003}).  At each Planck step, the
$q$-connection $\nabla_q$ resolves one crossing, branching
the resolution tree into three sub-histories.  After $c$
steps, the tree has $3^c$ leaves.

A polynomial-time algorithm would need to evaluate $P_L(q_0)$
using only $\mathrm{poly}(c)$ of the $3^c$ paths.  This
requires that the remaining $3^c - \mathrm{poly}(c)$ paths
have cancelling contributions — that destructive interference
in the Skein relation eliminates all but polynomially many
surviving terms.

The conjecture asserts that for NP-complete problems, this
cancellation does not occur.  The $3^c$ paths carry
**irreducible weight**: every exponential-size subtree
contributes non-trivially to $P_L(q_0)$.  No polynomial
sample suffices.

**Connection to quantum computation.**

The descent involution $\hat{\tau}$
([quantum universality](#conj:quantum-computational-universality))
decomposes the computation at a root of unity $q_k$:

$$
  \mathrm{End}(V^{\otimes n})
  \;=\;
  \mathcal{A}^{\mathrm{desc}} \;\oplus\; \mathcal{A}^{\mathrm{trans}}
$$

The descended part $\mathcal{A}^{\mathrm{desc}}$ is the
classical computation (P if polynomial, NP-hard if not).  The
transient part $\mathcal{A}^{\mathrm{trans}}$ is the quantum
parallelism — the exponentially many interfering paths.

$\mathrm{BQP}$ (bounded-error quantum polynomial time) is the
class where quantum parallelism at $q_k$ collapses the
transient modes efficiently — where the lift to the root of
unity and descent back to real $q$ can be done in polynomial
depth.  The standard belief $\mathrm{P} \subsetneq
\mathrm{BQP} \subseteq \mathrm{NP}$ translates to:

- **$\mathrm{P} \subsetneq \mathrm{BQP}$**: Quantum
  interference (lift to $q_k$) can penetrate some computational
  horizons that are opaque to classical (real $q$) computation.
- **$\mathrm{BQP} \subseteq \mathrm{NP}$**: Even quantum
  interference cannot penetrate **all** computational horizons.
  Some NP-complete problems have horizons that are opaque even
  at roots of unity.

The computational horizon is the universal obstruction: it is
the information-theoretic barrier that separates efficient from
inefficient computation, and its opacity is the content of
$\mathrm{P} \neq \mathrm{NP}$.
