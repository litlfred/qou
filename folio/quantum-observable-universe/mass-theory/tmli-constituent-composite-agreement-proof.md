**Proof.**
Under the hypothesis, $\beta_{\mathfrak{H}}$ is (up to cyclic rotation)
a product $w_0 w_1 \cdots w_{N-2}$ with $w_i$ a word in
$\sigma_i^{\pm 1}$, and the letters grouped at generator $\sigma_i$ are
exactly $w_i$, with Hecke reduction $\rho(w_i) = a_i\sigma_i + b_i$.
The [Markov trace product](#thm:markov-trace-product) then gives
$\mathrm{tr}_M(\rho(\beta_{\mathfrak{H}})) = \prod_i (z\,a_i + b_i)
= \prod_i \hat{V}_i^{\mathrm{const}}$, and cyclicity of
$\mathrm{tr}_M$ covers the rotations.

For the counterexample, $\sigma_0\sigma_1\sigma_0\sigma_1 =
h\,\sigma_0\sigma_1\sigma_0 + \sigma_1\sigma_0$ by the braid and Hecke
relations, so its trace is $h(hz^2 + z) + z^2$, while the grouped
product is $(hz + 1)^2$; these differ by
$z^2 - hz - 1 = -(q^4+q^2+1)/(q^2+1)^2$. $\square$
