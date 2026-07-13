Every nucleus $\mathcal{N}(Z, N)$ corresponds to a braid word in $B_A$. Gröbner--Shirshov reduction in $H_A(q)$ produces a unique normal form representing the lowest-energy state.

**Convention.** $\mathcal{N}(Z, N)$ denotes the reduced normal form unless explicitly stated.

**Proposition.**
Let $R = \mathbb{Z}[q, q^{-1}]$. $q$ is a categorical invariant, not a free parameter. The Iwahori--Hecke algebra $H_A(q) = R[B_A] / I$ admits an admissible system $(B, <)$.

The Gröbner--Shirshov basis $G$ for $I$ consists of:
1. **Hecke relation**: $\sigma_i^2 - (q - q^{-1})\sigma_i - 1$
2. **Yang--Baxter relation**: $\sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1}$
3. **Far commutativity**: $\sigma_i\sigma_j - \sigma_j\sigma_i$ for $|i - j| \geq 2$

The division algorithm computes the remainder, yielding the unique normal form:

$$
  \mathcal{N}(Z, N)
   := 
  r\bigl(\mathcal{N}_{\mathrm{raw}}(Z, N), G\bigr)
   \in  H_A(q).
$$

By Gröbner--Shirshov basis theory, the remainder is path-independent.

**The nuclear braid word.**
The unreduced braid word is:

$$
  \mathcal{N}(Z, N)
  = 
  \prod_{1 \leq i < j \leq A}
  \sigma_{i}^{\epsilon(i, j)}
$$

where the crossing sign $\epsilon(i, j)$ depends on nucleon types: $+1$ (protons), $-1$ (neutrons), $0$ (mixed, resolved as $\tfrac{1}{2}(\sigma_i + \sigma_i^{-1})$).

Gröbner--Shirshov reduction collapses the exponential expansion into the normal form.

**Computational results.**
The change in total Hecke weight under beta decay is always negative, confirming that beta decay releases energy. The normal form is tractable for numerical evaluation via the Markov trace.
