**Proof.** The Hecke relation $\sigma_i^2 = h\sigma_i + 1$
(where $h = q - q^{-1}$) gives each generator eigenvalues $q$
and $-q^{-1}$ on $V_{(2,1)}$, with product $-1$; $\sigma_i^{-1}$ has
eigenvalues $q^{-1}$ and $-q$, also with product $-1$. For a word of
$n$ letters, $\det \rho_{(2,1)}(\beta) = (-1)^n$, which is $1$ for even
$n$. So $\lambda_1 \lambda_2 = 1$, and the characteristic polynomial is
$\lambda^2 - \chi\,\lambda + 1$. Its roots have modulus $1$ if and only
if $\chi$ is real with $|\chi| \le 2$. That condition can fail: $\sigma_1^2$
has eigenvalues $q^2$ and $q^{-2}$.

For the Borromean value, take the explicit model
$\rho_{(2,1)}(\sigma_1) = \mathrm{diag}(q, -q^{-1})$ and

$$
  \rho_{(2,1)}(\sigma_2) =
  \begin{pmatrix}
    -\dfrac{1}{q(q^2+1)} & 1 \\[1ex]
    \dfrac{q^4 + q^2 + 1}{(q^2+1)^2} & \dfrac{q^3}{q^2+1}
  \end{pmatrix},
$$

which satisfies the braid relation, with $\sigma_2^{-1} = \sigma_2 - h$.
Multiplying out $(\sigma_1\sigma_2^{-1})^3$ and taking the trace gives the
displayed formula. $\square$

## Values

| Operator | $(3)$ | $\chi_{(2,1)}$ | $V_{(2,1)}$ eigenvalues | $(1^3)$ |
|----------|-------|-----------------|-------------------------|---------|
| $\sigma_i$ | $q$ | $h$ | $q,\; -q^{-1}$ (real) | $-q^{-1}$ |
| $\sigma_i^2$ | $q^2$ | $q^2 + q^{-2}$ | $q^2,\; q^{-2}$ (real) | $q^{-2}$ |
| $\sigma_1\sigma_2$ | $q^2$ | $-1$ | $e^{\pm 2\pi i/3}$ for every $q$ | $q^{-2}$ |
| $\beta_{\mathrm{Bor}}$ | $1$ | $\approx 1.994$ at $q_0$ | $\approx e^{\pm 0.0763 i}$ at $q_0$ | $1$ |

At $q = q_0$ the Borromean eigenvalues lie on the unit circle close to $+1$,
at angle $\theta \approx 4.37^\circ$. At $q = 2$ the trace is $-1573/64$ and
they are real, off the unit circle.

Note that unit modulus holds specifically for the three-cycle and Borromean elements above rather than for arbitrary even words, with $\chi_{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - h^4$ and non-degenerate complex-conjugate eigenvalues on $V_{(2,1)}$.

## Rotation versus growth

On $V_{(2,1)}$ an even word has $\lambda_1\lambda_2 = 1$, so its eigenvalues are
either a conjugate pair on the unit circle (a rotation by $\theta$ with
$2\cos\theta = \chi_{(2,1)}$) or a real pair $\lambda, \lambda^{-1}$ (growth).
Which case occurs depends on the word and on $q$. The outer channels $(3)$ and
$(1^3)$ are one-dimensional and carry $q^{w}$ and $(-q)^{-w}$-type growth.

The earlier "baryon--meson duality" in this section rested on
$\theta_{\mathrm{Bor}} = \pi$. Since $\chi_{(2,1)}(\beta_{\mathrm{Bor}}) \approx +1.994$
at $q_0$, the Borromean $(2,1)$ channel contributes with positive sign there,
and the claimed origin of the factor $\dim V_{(2,1)} = 2$ in the proton
substrate identity as a subtracted channel does not hold.
