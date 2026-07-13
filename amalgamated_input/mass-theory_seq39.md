<!-- FILE_START: intro-wenzl-bridge-cyclotomic.md -->
The Wenzl bridge converts the q-deformed Hecke trace into a Jones-polynomial evaluation at a cyclotomic root of unity. The resulting $\alpha$-coefficients are explicit polynomials in the substrate parameter.

We first construct the Wenzl bridge and prove it preserves the Hecke trace under cyclotomic specialisation. We then factor the categorical $y_\lambda$ sequence into explicit cyclotomic polynomials. Finally, we tabulate the $\alpha_k$ values for $k \leq 6$ and connect them to the six-term mass formula.
<!-- FILE_END: intro-wenzl-bridge-cyclotomic.md -->

<!-- FILE_START: y-lambda-cyclotomic-factorization.md -->
*Let $\sigma_i$ be the symmetric Hecke generators with parameter $z = 1/(q^{1/2} + q^{-1/2})$, and $\check{q} = q^{1/2}$. For every $\lambda \,\vdash\, n$ at $n \in \{2, 3, 4\}$, the Jones-Markov coefficient admits the closed form:*

$$
  y_\lambda(\check{q}) \;=\; \frac{P_\lambda(\check{q})}{D_n(\check{q})}, \qquad
  D_n(\check{q}) \;=\; \prod_{d} \Phi_d(\check{q})^{e_{n, d}},
$$

*where $P_\lambda(\check{q}) \in \mathbb{Z}[\check{q}]$ is a polynomial and $D_n(\check{q})$ is a pure product of cyclotomic polynomials $\Phi_d(\check{q})$.*

This factorisation guarantees a clean closed form for $y_\lambda$ over $\mathbb{Q}(\check{q})$. Hook-length data determines the cyclotomic denominators. The numerator is a finite-degree polynomial.
<!-- FILE_END: y-lambda-cyclotomic-factorization.md -->

<!-- FILE_START: y-lambda-recipe-from-partition.md -->
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
<!-- FILE_END: y-lambda-recipe-from-partition.md -->

<!-- FILE_START: graded-hecke-energy-truncation-bound.md -->
*Let $\hat{\beta}_K$ be the closure of $\mathcal{B}_K \in B_n$ and $\mathfrak{M}_K$ its highest-weight KLR module. The mass-spectrum generating function:*

$$
  P_K(q) \;=\; \sum_{d \in \mathbb{Z}} \dim_R \mathrm{Hom}_{\mathcal{K}_n}(P_d, \mathfrak{M}_K) \, q^d
$$

*has at most $\ell(K, q_0) + 1$ nonzero terms, where $\ell(K, q_0)$ is the confinement level at $q_0$.*

This bound drastically reduces computational cost. Canonical evaluation only needs to enumerate degrees $d \le \ell(K, q_0)$, instead of all $p(n)$ partitions. It enables stratified caching and limits combinatorial explosion.
<!-- FILE_END: graded-hecke-energy-truncation-bound.md -->

<!-- FILE_START: descent-rate-probe-sim.md -->

<!-- FILE_END: descent-rate-probe-sim.md -->

<!-- FILE_START: multi-level-jet-sum-sim.md -->

<!-- FILE_END: multi-level-jet-sum-sim.md -->

<!-- FILE_START: macdonald-hook-telescope.md -->
*Let $Q = q^2$ and $X = q\,z\,/\,(1 - Q + q\,z)$. The Wenzl-bridge normalisation $Z_n$ telescopes identically to a geometric ratio:*

$$
  \boxed{\;
    Z_n \;=\; \left(\frac{1 - X}{1 - Q}\right)^n.
  \;}
$$

*Therefore, every Jones-Markov coefficient admits a single-product closed form:*

$$
  \boxed{\;
    y_\lambda \;=\; Q^{n(\lambda)}
      \cdot \frac{(1 - Q)^n}{(1 - X)^n}
      \cdot \prod_{x \in \lambda}
        \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
  \;}
$$

This algebraic collapse removes the nested polynomial denominators entirely. It reduces evaluation cost from exponential series summation to a single $O(n)$ product over partition cells.
<!-- FILE_END: macdonald-hook-telescope.md -->

<!-- FILE_START: demazure-fiber-markov-trace.md -->
*Let $D_w(\lambda)$ be the Demazure character of the irreducible $S_n$-module $V_\lambda$. We define the Demazure-fiber functional via principal specialisation $x_i \mapsto q^{i-1}$:*

$$
  \boxed{\;
    T^{\mathrm{Dem}}(\lambda;\, w)
    \;:=\;
    y_\lambda
    \cdot
    \frac{D_w(\lambda)}{D_{w_0}(\lambda)}.
  \;}
$$

*For the longest element $w_0$, this saturates to the Jones-Markov coefficient $y_\lambda$. For $w < w_0$, it yields the structural resonance width: the fraction of $V_\lambda$ reachable from the Demazure sub-crystal cut by $w$.*

This functional structurally bounds the LP/SDP costs. It maps heuristic cutoffs to explicit Bruhat-prefix Demazure sub-crystals.
<!-- FILE_END: demazure-fiber-markov-trace.md -->

<!-- FILE_START: wenzl-bridge-applicability-qou.md -->
*Let $\mathbf{C}$ be a QOU substrate with self-dual fundamental object $A$ and fibre functor $\tau$. Then the Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ is uniquely fixed by $(\mathbf{C}, A, \tau)$ up to normalisation, and equals the Wenzl-bridge closed form.*

This ensures there is no parameter fitting. The unique Tannaka-Krein trace forces the exact Wenzl substitution at fractional rank $r$.
<!-- FILE_END: wenzl-bridge-applicability-qou.md -->

