Every nucleus $\mathcal{N}(Z, N)$ corresponds to a braid word in $B_A$; Gröbner--Shirshov reduction in $H_A(q)$ produces a unique normal form representing the lowest-energy state.

**Proposition.**
Let $R = \mathbb{Z}[q, q^{-1}]$, with $q$ a categorical invariant, not a free parameter. Order the generators $\sigma_1 < \sigma_2 < \cdots < \sigma_{A-1}$ and the words in $B_A$ length-lexicographically. With respect to this admissible system $(B, <)$, the ideal $I$ of the Iwahori--Hecke algebra $H_A(q) = R[B_A] / I$ has the Gröbner--Shirshov basis

$$
  G = \bigl\{\, \sigma_i^2 - (q - q^{-1})\sigma_i - 1, \;\;
  \sigma_i\sigma_j - \sigma_j\sigma_i \ (i \geq j + 2), \;\;
  \sigma_i\sigma_{i-1}\cdots\sigma_j\sigma_i - \sigma_{i-1}\sigma_i\sigma_{i-1}\cdots\sigma_j \ (1 \leq j \leq i - 1) \,\bigr\}
$$

(the Hecke relation, far commutativity, and the Bokut--Shiao family \cite{bokut2001}, which contains the Yang--Baxter relation $\sigma_i\sigma_{i-1}\sigma_i - \sigma_{i-1}\sigma_i\sigma_{i-1}$ as its case $j = i - 1$). The three defining families alone (Hecke, Yang--Baxter, far commutativity) are **not** a Gröbner--Shirshov basis once $A \geq 4$: they are completed by the Bokut--Shiao family ([Hecke normal form](#def:hecke-normal-form)). Every element of $G$ has leading coefficient $1$, so the division algorithm computes a remainder independent of the reduction path \cite{bergman1978}, yielding the unique normal form

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
