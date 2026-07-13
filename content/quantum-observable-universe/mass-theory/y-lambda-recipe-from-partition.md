*For any partition $\lambda \,\vdash\, n$, we determine $y_\lambda(q)$ mechanically as a rational function in $\sqrt q$.*

1. *Extract cell contents $c(i, j) = j - i$ and hook lengths $h(i, j)$. Define $n(\lambda) = \sum_i (i-1)\lambda_i$.*
2. *Compute the universal substitution:*

   $$
     \boxed{\; X \;:=\; \frac{q^{3/2}}{1 + q - q^2 - q^3 + q^{3/2}}. \;}
   $$

3. *Form the Schur principal-specialisation with $Q = q^2$:*

   $$
     \boxed{\; s_{\lambda, r}(Q) \;=\; Q^{n(\lambda)} \cdot \prod_{(i, j) \in \lambda} \frac{1 - X \cdot Q^{c(i, j)}}{1 - Q^{h(i, j)}}. \;}
   $$

4. *Normalize by $Z_n = \sum_{\mu \vdash n} f^\mu s_{\mu, r}(Q)$ to get:*

   $$
     \boxed{\; y_\lambda(q) \;=\; \frac{s_{\lambda, r}(Q)}{Z_n}. \;}
   $$

5. *Factor the result over $\mathbb{Q}(\sqrt{q})$ to isolate the cyclotomic denominator.*

This deterministic process produces the exact $y_\lambda(q)$ closed form in $O(p(n) \cdot \max \text{hooks})$ steps.
