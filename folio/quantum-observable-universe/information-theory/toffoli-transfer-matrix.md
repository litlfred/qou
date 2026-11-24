Let $P_{\mathrm{flip}}(q; k_1, k_2)$ be the target-flip amplitude on a $3$-strand nuclear braid with control types $(k_1, k_2) \in \{0,1\}^2$ and target strand $3$, constructed from the Hecke crossing coefficients. Write $\hat{V}_i = z(q)\,a_i + b_i$ for the traced volume at generator $\sigma_i$, with $(a_i, b_i)$ rational in $q$, and

$$
  P_{\mathrm{flip}} = \sum_i \Bigl[\prod_{j \neq i} \hat{V}_j^{\,\mathrm{par}}\Bigr] \bigl(\hat{V}_i^{\,\mathrm{par}} - \hat{V}_i^{\,\mathrm{dau}}\bigr),
$$

the parent context being the input state. Then:

1. **(Type-dependence of the control crossing.)** The traced volume at $\sigma_1$ is
$$
  \hat{V}_1(k_1,k_2) = z(q)\,c_{k_1k_2} + d_{k_1k_2},
$$
which is **type-dependent through $d$**, not through $c$:

| Control pair | $c_{k_1 k_2}$ | $d_{k_1 k_2}$ |
|:------------:|:--------------:|:--------------:|
| $\mathfrak{p}\mathfrak{p}$ | $1$ | $0$ |
| mixed | $1$ | $-\frac{q - q^{-1}}{2}$ |
| $\mathfrak{n}\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ |

2. **(No universal core.)** The three target-flip amplitudes are **distinct**. At $q = 111/100$,
$$
  P_{\mathrm{flip}}(\mathfrak{p}\mathfrak{p}) = -0.13061590, \qquad P_{\mathrm{flip}}(\text{mixed}) = -0.11767065, \qquad P_{\mathrm{flip}}(\mathfrak{n}\mathfrak{n}) = -0.10701099 .
$$
There is no factorisation $P_{\mathrm{flip}} = c_{k_1k_2}\,\Phi$ with a control-independent core: since $c = 1$ for every pair, such a factorisation would force the three to coincide, and the type-dependence resides in $d$.

3. **(The q-AND.)** For the all-proton control pair, with Markov parameter $z = q^3/(q^2+1)$,
$$
  P_{7,6}(q) = -\,\frac{(q-1)(q+1)\bigl(q^{6} + q^{4} + 2q^{2} + 1\bigr)}{2q\,(q^{2}+1)^{2}}.
$$

4. **(No antisymmetry.)** With each entry taken from its own input column, $P_{6,7} \neq -P_{7,6}$:
$$
  P_{6,7}(q) = \frac{(q-1)(q+1)\bigl(2q^{6} + q^{4} + q^{2} + 1\bigr)}{2q\,(q^{2}+1)^{2}} .
$$

5. **(Classical limit.)** Every target-flip amplitude vanishes as $q \to 1$: each carries the factor $(q-1)$.

6. **(Toffoli diagonals.)** The diagonal is $\hat V_0 \hat V_1$ with $\hat V_i = z\,a_i + b_i$ and $(a_i, b_i)$ rational in $q$. For the all-proton ordering every crossing has $(c,d) = (1,0)$, giving $P_{7,7}(q) = z + \hbar_\times z^2$ with $\hbar_\times = q - q^{-1}$. At $z = q^3/(q^2+1)$, the odd- and even-channel diagonal entries are
$$
  P_{7,7}(q) = \frac{q^3(q^4 + 1)}{(q^2 + 1)^2},
  \qquad
  P_{6,6}(q) = \frac{\bigl(q^{4}+1\bigr)\bigl(q^{4}+q^{2}+2\bigr)}{4q\,(q^{2}+1)^{2}},
$$
whose numerators have no positive real root. Thus **both diagonal entries are strictly positive for every $q > 0$** (whereas the golden-ratio threshold $q = 1/\varphi^2$ remains independently the root of $s^2 + s - 1$ in the Weierstrass coefficient of $\mathcal{E}_q$ in [golden ratio degeneration](#rem:golden-ratio-degeneration), which carries no $z$).
