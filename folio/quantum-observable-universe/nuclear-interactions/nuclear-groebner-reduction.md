Every nucleus $\mathcal{N}(Z, N)$ corresponds to a braid word in $B_A$; Gröbner--Shirshov reduction in $H_A(q)$ produces a unique normal form representing the lowest-energy state.

**Proposition.**
Let $R = \mathbb{Z}[q, q^{-1}]$, with $q$ a categorical invariant, not a free parameter. The Iwahori--Hecke algebra $H_A(q) = R[B_A] / I$ admits an admissible system $(B, <)$, and the Gröbner--Shirshov basis $G$ for $I$ is

$$
  G = \bigl\{\, \sigma_i^2 - (q - q^{-1})\sigma_i - 1, \;\;
  \sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1}, \;\;
  \sigma_i\sigma_j - \sigma_j\sigma_i \ (|i - j| \geq 2) \,\bigr\}
$$

(the Hecke relation, the Yang--Baxter relation, and far commutativity). The division algorithm computes the remainder, yielding the unique, path-independent normal form

$$
  \mathcal{N}(Z, N)
   := 
  r\bigl(\mathcal{N}_{\mathrm{raw}}(Z, N), G\bigr)
   \in  H_A(q).
$$

By convention, $\mathcal{N}(Z, N)$ denotes the reduced normal form unless explicitly stated.

**The nuclear braid word.**
The unreduced braid word is

$$
  \mathcal{N}(Z, N)
  = 
  \prod_{1 \leq i < j \leq A}
  \sigma_{i}^{\epsilon(i, j)}
$$

where the crossing sign $\epsilon(i, j)$ depends on nucleon types: $+1$ (protons), $-1$ (neutrons), $0$ (mixed, resolved as $\tfrac{1}{2}(\sigma_i + \sigma_i^{-1})$). Gröbner--Shirshov reduction collapses the exponential expansion into the normal form.
