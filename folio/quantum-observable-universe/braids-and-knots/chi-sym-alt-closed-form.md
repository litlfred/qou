Let $\mathbf{H}_n(q)$ be the Iwahori–Hecke algebra with $H_A = q - q^{-1}$, and let $\beta$ be a word in the Hecke elements $c\,\sigma_g + d\cdot 1$. Write $\chi_{\mathrm{sym}}$ and $\chi_{\mathrm{alt}}$ for the characters of the two one-dimensional Wedderburn blocks, on which $\sigma \mapsto q$ and $\sigma \mapsto -q^{-1}$ respectively.

**Per-factor product.** For a single letter $\sigma + d\cdot 1$,

$$
\chi_{\mathrm{sym}}(\sigma + d)\,\chi_{\mathrm{alt}}(\sigma + d)
  = (q + d)\,(-q^{-1} + d) = d^2 - 1 + d\,H_A =: f(d).
$$

**Stationarity.** Over any commutative ring, without division,

$$
4\,f(d) = (2d + H_A)^2 - H_A^2 - 4 .
$$

All of the $d$-dependence lies inside a perfect square in the offset $2d + H_A$, which vanishes exactly at $d = -H_A/2$. Hence $f$ is stationary at the $ud$ value, and a perturbation of the offset enters the product at second order.

**Closed form.** Let the word carry $n_\sigma$ letters with $d = 0$, $n_{\sigma^{-1}}$ with $d = -H_A$, $n_{ud}$ with $d = -H_A/2$, and a set $P$ of remaining letters. Then

$$
\chi_{\mathrm{sym}}(\beta)\,\chi_{\mathrm{alt}}(\beta)
  = (-1)^{\,n_\sigma + n_{\sigma^{-1}} + n_{ud}}
    \left(1 + \tfrac{H_A^2}{4}\right)^{\,n_{ud}}
    \prod_{d \in P} f(d).
$$

**Specialisation to the atomic word.** For the canonical $A$-nucleon word, $n_{ud} = 2A$ (two per nucleon) and $P$ is the single colour-weighted p-n interface, at $d = -H_A(\tfrac12 - \tfrac{\delta}{4})$. The p-p interface is a plain $\sigma$ and the n-n a plain $\sigma^{-1}$, so exactly one letter lies outside the three colour-blind classes, independently of $A$. The count of averaged letters is therefore $n_{ud} + |P| = 2A + 1$.

**Colour-blind corollary.** If every letter of $P$ satisfies $d = -H_A/2$ (equivalently $\delta = 0$), then $\prod_{d \in P} f(d) = \bigl(-(1 + H_A^2/4)\bigr)^{|P|}$ and the closed form collapses to

$$
\chi_{\mathrm{sym}}(\beta)\,\chi_{\mathrm{alt}}(\beta)
  = (-1)^{\#\beta}\left(1 + \tfrac{H_A^2}{4}\right)^{\,n_{ud} + |P|},
$$

the exponent $2A+1$ on the atomic word. The implication runs only in this direction: setting $\delta = 0$ specialises the general statement, while the specialised one no longer records $\delta$.
