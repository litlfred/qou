The crystal-graph realisation of Hecke normal forms and the confinement–grading correspondence provide a sharp computational mechanism. Every observable extracted by the Observation Frame $\tau$ is determined by its image at the crystal limit $q \to 0$ and transported back to the generic fibre $\mathcal{S}_p$ along the flat $q$-connection.

## Mechanism

At the crystal limit $q \to 0$, the cyclotomic KLR module category $\mathcal{K}_n$ degenerates to its associated graded, the Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$. The crystal carries no quantum corrections; Kashiwara operators $\tilde{e}_i, \tilde{f}_i$ decorate its edges, and weights are integer-graded. The graded Euler characteristic $\tau(M) = \sum_d (-1)^d \dim_R M_d$ remains invariant under flat transport from the special fibre at $q = 0$ to a generic fibre $\mathcal{S}_p$ at $q = q_0$:

$$
  \tau\bigl(\mathfrak{M}_K\bigr)\big|_{q = q_0}
  \;=\;
  \tau\bigl(\mathfrak{M}_K\bigr)\big|_{q \to 0}.
$$

Any Laurent polynomial $P_K^{(k)}(q)$ extracted at level $k$ from the crystal traversal lifts uniquely to the generic fibre via the $\mathbb{Z}$-grading of the GB spectral sequence.

## Consequence for the engine

The Gröbner–Shirshov reduction engine operates entirely on the finite, discrete crystal graph at $q = 0$. No resolution of overlapping S-polynomials at the generic fibre is required. Crystal-limit values pull back to the physically relevant $q_0$ along the flat connection. The cemetery filter acts identically on both sides. The engine replaces continuous polynomial term-rewriting with graph traversal while losing no information at the generic fibre.
