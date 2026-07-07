**Proposition.** Let $P_{\mathrm{flip}}(q; k_1, k_2)$ be the target-flip amplitude on a $3$-strand nuclear braid with control types $(k_1, k_2) \in \{0,1\}^2$ and target strand $3$, constructed from the Hecke crossing coefficients. Then:

1. **(Universal factorization.)** Every target-flip amplitude factors as
$$
  P_{\mathrm{flip}}(q; k_1, k_2) = c_{k_1 k_2}(q) \cdot \Phi(q)
$$
where $c_{k_1 k_2}$ is the crossing coefficient of the control–control pair (the non-flipping strands) and $\Phi(q)$ is the **universal core amplitude** independent of the control types:
$$
  \Phi(q) = \frac{(q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1)}{2(q + 1)^2}
$$

| Control pair | $c_{k_1 k_2}$ | $d_{k_1 k_2}$ |
|:------------:|:--------------:|:--------------:|
| $\mathfrak{p}\mathfrak{p}$ | $1$ | $0$ |
| mixed | $1$ | $-\frac{q - q^{-1}}{2}$ |
| $\mathfrak{n}\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ |

2. **(Target-flip blindness of the control crossing.)** The generator $\sigma_1$ constitutes the single control–control crossing. Its traced volume $\hat{V}_1 = z(q)\,c + d$ is type-dependent. A target-flip leaves the control crossing unchanged. Consequently, $\Delta_1 = 0$ for every target-flip transition. The entire target-flip amplitude concentrates at generator $\sigma_0$.

3. **(The q-AND.)** The Toffoli gate selects the target strand whose control–control pair has $c = 1$ ($\mathfrak{p}\mathfrak{p}$ crossing). In the exceptional divisor, this choice provides the governor basis with unit prefactor:
$$
  P_{7,6}(q) = 1 \cdot \Phi(q) = \frac{(q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1)}{2(q+1)^2}
$$

4. **(Antisymmetry.)** $P_{6,7}(q) = -P_{7,6}(q)$.

5. **(Classical limit.)** All target-flip amplitudes vanish as $q \to 1$ because the core $\Phi(q)$ contains the factor $(q - 1)$.

6. **(Toffoli diagonal.)** The diagonal entry is
$$
  P_{7,7}(q) = \frac{q + q^{1/2} - 1}{q + 1}
$$
This all-proton amplitude vanishes exactly at the golden ratio threshold $q = 1/\varphi^2$.
