
$$
f(t) \;=\; \sum_{n=1}^{\infty} \Bigl(\sum_{i=1}^{2g} \alpha_i^n\Bigr) t^n
\;=\; \sum_{i=1}^{2g} \frac{\alpha_i t}{1 - \alpha_i t} .
$$

The coefficient bound forces the power series to converge absolutely on the open disc $|t| < q^{-1/2}$, so $f$ is holomorphic there. Grouping equal eigenvalues, each distinct value $\alpha$ among the $\alpha_i$, occurring with multiplicity $m_\alpha \geq 1$, contributes a simple pole of $f$ at $t = 1/\alpha$ with residue $-m_\alpha/\alpha \neq 0$; poles at distinct locations cannot cancel. Hence no $1/\alpha_i$ lies in the disc $|t| < q^{-1/2}$, i.e.

$$
|\alpha_i| \;\leq\; q^{1/2} \qquad \text{for all } i .
$$

**Step 5: The functional equation forces equality.** The zeta function of a smooth projective curve satisfies the functional equation

$$
P(t) \;=\; q^g\, t^{2g}\, P\!\Bigl(\frac{1}{qt}\Bigr),
$$

a consequence of the Riemann--Roch theorem on $\mathcal{B}$ \cite{rosen2002} (Ch. 5, Thm. 5.9). Comparing root sets on both sides, the involution $\alpha \mapsto q/\alpha$ permutes the multiset $\{\alpha_1, \ldots, \alpha_{2g}\}$. Applying Step 4 to the eigenvalue $q/\alpha_i$ gives $|q/\alpha_i| \leq q^{1/2}$, i.e. $|\alpha_i| \geq q^{1/2}$. Combined with Step 4 itself,

$$
|\alpha_i| \;=\; q^{1/2} \qquad \text{for all } i = 1, \ldots, 2g .
$$

Since $g = 4$ for Bring's curve, this is the asserted bound on all eight fundamental eigenvalues. $\square$
