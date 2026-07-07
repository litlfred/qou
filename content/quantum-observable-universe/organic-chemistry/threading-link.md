**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms arranged in a cycle. The **threading link** of the ring is the torus link

$$
  \mathcal{T}_N =  T(2, N),
$$

whose closure in the braid group $B_N$ is

$$
  \hat{\beta}_N
  = 
  (\sigma_1  \sigma_2  \cdots  \sigma_{N-1})^2.
$$

The threading link winds **twice** around the torus defined by the $N$ atoms, passing through every atom on each winding. It has $2(N-1)$ crossings.

**Component structure.**
The number of components of $T(2,N)$ is $\gcd(2,N)$. For even $N$, the threading link is a 2-component link. These two components are the topological realisation of the two delocalised $\pi$ electrons.

**Alexander polynomial.**
The Alexander polynomial of $T(2,N)$ for even $N = 2m$ is

$$
  \Delta_{T(2,2m)}(t)
  = 
  \frac{t^m - t^{-m}}{t - t^{-1}}.
$$

Evaluated at the substrate parameter $t = q$:

| Threading | $m$ | $\Delta(q)$ |
|-----------|:---:|-------------|
| $T(2,2)$ (Hopf) | 1 | $1$ |
| $T(2,4)$ | 2 | $q + q^{-1}$ |
| $T(2,6)$ | 3 | $q^2 + 1 + q^{-2}$ |
| $T(2,8)$ | 4 | $q^3 + q + q^{-1} + q^{-3}$ |
