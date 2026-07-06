**Proof sketch.**
By induction on $A$. Adding strand $A$ creates cross-terms
$\sigma_i \cdot \sigma_{A-1}$ for all $i < A - 1$. These are absorbed:

- If $|i - (A-1)| \geq 2$: far-commutativity reduces to
 $\sigma_{A-1} \cdot \sigma_i$, then I$_{9}$ absorbs (prefix $\sigma_i$
 present).
- If $|i - (A-1)| = 1$: adjacency pair, I$_{8}$ absorbs (prefix
 $\sigma_{A-1}$ present).
- If $i = A - 1$: Hecke relation $\sigma_{A-1}^2 = (q - q^{-1})\sigma_{A-1}
  + \mathbf{1}$, both terms already in basis.

The identity term $\mathbf{1}$ survives because $d \neq 0$ for nn and pn
crossings. The condition $N \geq Z - 1$ ensures at least one nn or pn
crossing at every generator. $\square$

Verified computationally for all $A \leq 8$ (14,256 terms $\to$ 8 for
${}^8\mathrm{Be}$). Formally proved in Lean (OptimalNF.lean).

**Valley of stability boundary.**
The optimality fails for $N < Z - 1$ (proton-heavy nuclei). When all
crossings are pp type ($d = 0$), the identity term vanishes: multiplying
by $(c \cdot \sigma_k + 0)$ does not preserve the identity. Without
$\mathbf{1}$ in the support, I$_{9}$ chain-stripping has no root.

See [Table 4](#tbl:shell-closure-normal-form-table4-data).

The boundary $N \geq Z - 1$ matches the nuclear valley of stability.
