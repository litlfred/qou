## The finiteness inequality

**Proposition.**
*A nuclear configuration $\mathcal{N}(p, n)$ is stable only if the Skein polynomial is positive,*

$$
  P_{\mathcal{N}(p,n)}(q)  >  0,
$$

*equivalently, for each generator $i = 0, \ldots, A-2$ the traced volume is positive,*

$$
  \hat{V}_i(q) = 
  c_+^{(i)}\lambda_+^{k_i}
  + 
  c_-^{(i)}\lambda_-^{k_i}
   >  0
  \qquad (i = 0, \ldots, A-2),
$$

*where $\hat{V}_i = z \cdot M_{11}^{(i)} + M_{21}^{(i)}$ is the traced volume of generator $\sigma_i$ ([transfer matrix](#prop:skein-polynomial-transfer-matrix)), $P = \prod_i \hat{V}_i$, the transfer-matrix eigenvalues $\lambda_\pm$ are real and opposite in sign ($\det T < 0$), and $k_i = A-1-i$.*

Although each $\hat{V}_i > 0$ for $q > 1$, the product $P$ can flip sign through Yang--Baxter cross-terms. The sign flip is governed by the $q$-deformed finiteness bound

$$
  \boxed{[A-1]_q!  >  [2]_q^{A-1}},
  \qquad
  [n]_q! = \prod_{k=1}^{n} [k]_q,
  \quad
  [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}},
$$

first satisfied at $A = 5$ for all $q > 1$; at the aether $q_0$ the Skein-polynomial sign flip occurs at $A = 6$ (one step later, because the $(2,2)$ shell closure stabilises $A = 4$). Shell closures at the magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ re-stabilise $P > 0$, extending the physical nuclear chart to $A \sim 300$ ([shell closure](#prop:shell-closure-normal-form)).
