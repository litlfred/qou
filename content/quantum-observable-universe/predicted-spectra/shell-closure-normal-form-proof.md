**Proof sketch.**
We proceed by induction on $A$. Adding strand $A$ creates cross-terms $\sigma_i \cdot \sigma_{A-1}$ for all $i < A - 1$. We absorb these terms as follows:

- If $|i - (A-1)| \geq 2$: Far-commutativity gives $\sigma_{A-1} \cdot \sigma_i$. Then I$_{9}$ absorbs this term since the prefix $\sigma_i$ is present.
- If $|i - (A-1)| = 1$: This forms an adjacency pair. I$_{8}$ absorbs this term since the prefix $\sigma_{A-1}$ is present.
- If $i = A - 1$: The Hecke relation yields $\sigma_{A-1}^2 = (q - q^{-1})\sigma_{A-1} + \mathbf{1}$. Both terms are already in the basis.

The identity term $\mathbf{1}$ survives because $d \neq 0$ for nn and pn crossings. The condition $N \geq Z - 1$ ensures at least one nn or pn crossing exists at every generator. $\square$

We verify this computationally for all $A \leq 8$ (reducing 14,256 terms to 8 for ${}^8\mathrm{Be}$). We formally prove this in Lean (`OptimalNF.lean`).

**Valley of stability boundary.**
The optimality fails for $N < Z - 1$ (proton-heavy nuclei). When all crossings are pp type ($d = 0$), the identity term vanishes. Multiplying by $(c \cdot \sigma_k + 0)$ does not preserve the identity. Without $\mathbf{1}$ in the support, I$_{9}$ chain-stripping lacks a root.

See [Table 4](#tbl:shell-closure-normal-form-table4-data).

The boundary $N \geq Z - 1$ matches the nuclear valley of stability.
