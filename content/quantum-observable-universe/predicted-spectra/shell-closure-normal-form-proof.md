*
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
crossing at every generator.
$\qquad\blacksquare$
