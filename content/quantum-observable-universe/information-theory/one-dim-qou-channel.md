*Lean sibling: structural, over a generic commutative ring $R$ (AGENTS.md §7c) — the carried datum is the Markov-trace value.*

**Definition.** A **one-dimensional channel** over a coefficient ring $R$ is a bounded braid carrier. Physically, it models an optical fibre as a one-dimensional waveguide (distinct from the categorical fibre functor $\tau$). It is a line along which $n$ strands, the modes of the fibre, propagate while carrying a braid word $\beta \in B_n$. Its transmitted, measurable datum is the Markov trace $\mathrm{tr}_M(\beta) \in R$. This is the same invariant that reads out particle content elsewhere in this paper.

The **cladding** is the surface of the fibre. We model it as a topological boundary condition confining $\beta$ to the strand bundle: no strand crosses the surface. A channel is thus determined by its trace value. The **vacuum channel** is the empty fibre ($\beta = \mathbf{1}$, $\mathrm{tr}_M = 1$).

The Lean sibling records this as the structure $\mathtt{OneDimChannel}\,R$ carrying its $\mathrm{trace}$. It also includes the vacuum channel and the **parallel placement** of two side-by-side fibres:

$$
  \mathcal{F}_A \parallel \mathcal{F}_B := \langle\, \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B) \,\rangle .
$$

We justify this product through the multiplicativity of the trace. The surface boundary ensures parallel fibres form a split link. We establish this in the next proposition.
