*For any partition $\lambda \,\vdash\, n$, $y_\lambda(q)$ is determined mechanically as a rational function in $q$.*

1. *Extract cell contents $c(i, j) = j - i$ and hook lengths $h(i, j)$. Define $n(\lambda) = \sum_i (i-1)\lambda_i$.*
2. *Fix the universal substitution at the Wenzl level $r = 2$, with $Q = q^2$:*

   $$
     \boxed{\; X \;:=\; Q^{r} \;=\; q^{4}. \;}
   $$

   *Equivalently $X = z_W/(1 - Q + z_W)$ for the Wenzl-normalised parameter $z_W = q\,z = q^4/(q^2+1)$ at $z = q^3/(q^2+1)$ — the relation that pins the level.*
3. *Form the Schur principal-specialisation:*

   $$
     \boxed{\; s_{\lambda, r}(Q) \;=\; Q^{n(\lambda)} \cdot \prod_{(i, j) \in \lambda} \frac{1 - X \cdot Q^{c(i, j)}}{1 - Q^{h(i, j)}}. \;}
   $$

4. *Normalize by $Z_n = \sum_{\mu \vdash n} f^\mu s_{\mu, r}(Q)$ to get:*

   $$
     \boxed{\; y_\lambda(q) \;=\; \frac{s_{\lambda, r}(Q)}{Z_n}, \qquad Z_n \;=\; [r]_Q^{\,n} \;=\; (1 + q^2)^n. \;}
   $$

   *The closed form for $Z_n$ removes the sum over all $p(n)$ partitions.*
5. *Factor the result over $\mathbb{Q}(q)$ to isolate the cyclotomic denominator.*

This deterministic process produces the exact $y_\lambda(q)$ closed form in $O(|\lambda| \cdot \max h)$ steps — the cost of one Schur specialisation, the normaliser being closed-form.

**Properties at $r = 2$.** With the Markov parameter $z = q^3/(q^2+1)$, the Wenzl parameter $z_W = q\,z = q^4/(q^2+1)$ sits directly on the integer level $r = 2$ of the Wenzl lattice, yielding three structural simplifications:

- No square root: the recipe lives over $\mathbb{Q}(q)$ rather than $\mathbb{Q}(\sqrt q)$.
- $Z_n = (1 + q^2)^n$ is closed-form, so step 4 requires no partition sum.
- $y_\lambda = 0$ whenever $\lambda$ has more than $r = 2$ rows, so only the one- and two-row partitions contribute.

**Worked example** ($n = 2$, both partitions of dimension one):

$$
  y_{(2)} \;=\; \frac{(q^2 - q + 1)(q^2 + q + 1)}{(1 + q^2)^2}, \qquad
  y_{(1,1)} \;=\; \frac{q^2}{(1 + q^2)^2},
$$

whose numerators are $\Phi_6(q)\,\Phi_3(q) = q^4 + q^2 + 1$ and $q^2$, and which sum against their dimensions to $1$.
