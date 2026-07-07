**Definition (Habiro ring).**
*Let $R = \mathbb{Z}[q]$. The **$q$-Habiro ring** $\widehat{\mathbb{Z}[q]}_q$ is the inverse limit of the polynomial rings $R / ( (q; q)_n )$ as $n \to \infty$, where $(q; q)_n = \prod_{k=1}^n (1 - q^k)$ is the $q$-Pochhammer symbol:*

$$
  \widehat{\mathbb{Z}[q]}_q
  \;:=\;
  \varprojlim_n \frac{\mathbb{Z}[q]}{((q; q)_n)}.
$$

*Elements of the $q$-Habiro ring are formal power series of the form $\sum_{n=0}^\infty c_n(q) \, (q; q)_n$ with $c_n \in \mathbb{Z}[q]$.*

The Habiro ring completes the polynomial ring $\mathbb{Z}[q]$ at the cyclotomic ideals. It forms the natural home for quantum topological invariants evaluated at roots of unity, where the terms $(q; q)_n$ vanish for $n$ large enough, truncating the infinite series to a finite sum.

**Application to QOU.** The algebraic quantum volume evaluates as a finite sum precisely because its components belong to a generalized Habiro ring where the truncation depth connects to the physical shell structure.
