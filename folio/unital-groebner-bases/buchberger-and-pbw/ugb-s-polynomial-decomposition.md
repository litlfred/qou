Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an
$R$-module, $(B, <)$ an admissible system on $A$. Let $\alpha \in B$ and suppose
that $f_1, \ldots, f_n \in A$ satisfy $\LM(f_i) = \alpha$ and
$\LC(f_i) \in R^\times$. Then if:

$$f := \sum_i c_i f_i \quad (c_i \in R^*)$$

satisfies $\LM(f) < \alpha$, we may write:

$$f = \sum_{i \neq j} d_{i,j} S_{i,j}$$

where the $S_{i,j}$ are the S-polynomials about $f_i$ and $f_j$ given by:

$$S_{i,j} := \frac{1}{a_i} f_i - \frac{1}{a_j} f_j, \qquad a_i := \LC(f_i),\; a_j := \LC(f_j) \in R^\times$$

*Proof.* Because we have cancellation of the terms involving $\alpha$, we have
$\sum_i c_i = 0$. Then a telescoping argument yields:

$$f = c_1 a_1 S_{1,2} + (c_1 a_1 + c_2 a_2) S_{2,3} + \cdots + (c_1 a_1 + \cdots + c_{n-1} a_{n-1}) S_{n-1,n}$$

which gives the desired result. $\square$
