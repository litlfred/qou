On $H_3$ itself the Gram matrix is degenerate: $\det G = 0$ exactly, the $(1^3)$ block being the radical of the Markov trace (`MarkovGramDegenerate.lean`). Non-degeneracy therefore holds on $H_3/\mathrm{rad} \cong \mathrm{TL}_3$ and not on $H_3$.

The dual exists and is unique by non-degeneracy of $G$ on that quotient: the pairing $\langle K^\vee, b_j \rangle_F = \sum_{i,k} c_i (G^{-1})_{ik} G_{kj} = \sum_i c_i \delta_{ij} = c_j$ follows from $G^{-1} G = I$.
