The argument is a **direct two-step peel**, one Markov move per
factor. Embed $\sigma_i\sigma_j$ in $H_{j+1}(q)$, the minimal
Hecke algebra containing both generators; higher embeddings
follow by Markov closure $\mathrm{tr}_M^{H_n} = \mathrm{tr}_M^{H_{n-1}}$
on any element of $H_{n-1}(q)$ embedded in $H_n(R, q)$.

*Peel 1 (outer generator).* In $H_{j+1}(q)$ the rightmost
generator is $\sigma_j$. Since $\sigma_i \in H_j(q)$ (it involves
only indices $\le j-1$), $\sigma_i$ commutes by definition with the
coefficient ring and is not affected by the Markov move on
$\sigma_j$:

$$
  \mathrm{tr}_M^{H_{j+1}}\!(\sigma_i\sigma_j)
  \;=\; z \cdot \mathrm{tr}_M^{H_j}\!(\sigma_i).
$$

*Peel 2 (inner generator).* The remaining element $\sigma_i$
lives in $H_j(q)$. Repeatedly apply Markov closure to reduce
to the minimal embedding $\sigma_i \in H_{i+2}(q)$:

$$
  \mathrm{tr}_M^{H_j}\!(\sigma_i)
  \;=\; \mathrm{tr}_M^{H_{j-1}}\!(\sigma_i)
  \;=\; \cdots \;=\;
  \mathrm{tr}_M^{H_{i+2}}\!(\sigma_i).
$$

In $H_{i+2}(q)$, $\sigma_i$ itself is the rightmost generator.
Apply the Markov axiom once more:

$$
  \mathrm{tr}_M^{H_{i+2}}\!(\sigma_i)
  \;=\; z \cdot \mathrm{tr}_M^{H_{i+1}}\!(1)
  \;=\; z.
$$

Combining the two peels:
$\mathrm{tr}_M(\sigma_i\sigma_j) = z \cdot z = z^2$.
$\square$
