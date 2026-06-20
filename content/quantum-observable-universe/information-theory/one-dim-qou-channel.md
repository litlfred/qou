*Lean sibling: structural, over a generic commutative ring $R$ (AGENTS.md §7c) — the carried datum is the Markov-trace value.*

**Definition.** A **one-dimensional QOU channel** — physically an *optical fibre*, in the literal sense of a one-dimensional waveguide, **not** the categorical fibre functor $\tau$ — over a coefficient ring $R$ is a bounded braid carrier: a line along which $n$ strands, the **modes** of the fibre, propagate while carrying a braid word $\beta \in B_n$. Its transmitted, measurable datum is the Markov trace $\mathrm{tr}_M(\beta) \in R$, the same invariant that reads out particle content elsewhere in the framework.

The **cladding** is the surface of the fibre, modelled as a topological boundary condition confining $\beta$ to the strand bundle: no strand crosses the surface. A channel is thus summarised by its trace value, and the **vacuum channel** is the empty fibre ($\beta = \mathbf{1}$, $\mathrm{tr}_M = 1$).

The Lean sibling records this as the structure $\mathtt{OneDimChannel}\,R$ carrying its $\mathrm{trace}$, together with the **vacuum** channel and the **parallel placement** of two side-by-side fibres,
$$
  \mathcal{F}_A \parallel \mathcal{F}_B \;:=\; \langle\, \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B) \,\rangle .
$$
The multiplicativity of the trace that justifies this product — the surface boundary making parallel fibres a split link — is established in the next proposition.
