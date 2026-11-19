**Definition (Frobenius dual).**
*Let $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ be the (**convention D**: read on the quotient $H_n/\mathrm{rad}\,\mathrm{tr}_M \cong \mathrm{TL}_n$, where the induced pairing is non-degenerate; on $H_n$ itself $\det G = 0$ exactly, the $(1^3)$ block being the radical) non-degenerate
Frobenius Gram matrix on the NF basis $\{b_i\}$ of $H_3(q)$
([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). For a
state $K = \sum_i c_i b_i$ in NF, the **Frobenius dual**
is the unique element $K^\vee \in H_3(q)$ satisfying
$\langle K^\vee, b_j \rangle_F = c_j$ for all $j$.
Explicitly:*

$$
  K^\vee = \sum_{i,j} c_i (G^{-1})_{ij} b_j.
$$

*The dual exists and is unique by non-degeneracy of $G$ — which under **convention D** holds on $H_3/\mathrm{rad} \cong \mathrm{TL}_3$ and not on $H_3$, where $\det G = 0$: the pairing
$\langle K^\vee, b_j \rangle_F = \sum_{i,k} c_i (G^{-1})_{ik} G_{kj}
= \sum_i c_i \delta_{ij} = c_j$ follows from $G^{-1} G = I$.*
