The Rosso--Jones inner product $\langle -, - \rangle_{\mathrm{RJ}}$ ([canonical inner product](#prop:rj-canonical-inner-product)) is the archimedean :refterm[descent]{#descent} of the categorical trace $\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$ to the Iwahori--Hecke subalgebra.

The chain of identifications is:

| Level               | Object                                                                                                                                     | Role                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Categorical         | $\mathrm{tr} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes -) \circ \mathrm{coev}_A$                                                 | Integration in the action $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$ |
| Archimedean         | Markov trace $\mathrm{tr}_M$ on $H_r(q)$                                                                                                   | :refterm[Descent]{#descent} of $\mathrm{tr}$ to the Hecke algebra      |
| Representation ring | $\langle -, - \rangle_{\mathrm{RJ}} = \sum_\lambda d_\lambda(q) \cdot \mathrm{tr}_\lambda(-) \cdot \mathrm{tr}_\lambda(-)$                 | Diagonal form via Schur orthogonality                                  |
| Q-value             | $F_{\mathrm{deg2}} = \sum_\tau J(\tau) \cdot \mathrm{tr}_M(\tau \cdot \Delta_\beta) / \sum_\tau J(\tau) \cdot \mathrm{tr}_M(\Delta_\beta)$ | RJ-weighted spectral projection                                        |

The categorical action ([canonical action](#prop:qou-canonical-action)) integrates the Lagrangian via $\mathrm{tr}$. In the archimedean realization, this becomes the Markov trace on the Hecke algebra. The Markov trace decomposes via Schur orthogonality into quantum-dimension weights $d_\lambda(q)$. These are the Rosso--Jones weights. The shell correction $F_{\mathrm{deg2}}$ in the Q-value formula ([spectral decomposition](#cor:spectral-decomposition-qvalue)) uses exactly this inner product to weight the degree-$2$ torus knots $\tau(2,9)$ and $\tau(3,4)$.

Schur orthogonality leaves no freedom in the weighting ([Proposition (ii)](#prop:rj-canonical-inner-product)). The quantum dimensions are determined by $q$ alone.
