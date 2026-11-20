## Proof

By [spectral sequence collapse](#prop:spectral-sequence-collapse),
$\mathrm{HH}^k(H_3(R, q)) = 0$ for $k \geq 1$ at generic $q$, so only
$\mathrm{HH}^0 = Z(H_3) = \bigoplus_\lambda R \cdot e_\lambda$ survives.
Per [explicit $H_3$ pages](#prop:spectral-sequence-h3-explicit), the
four surviving $E_\infty^{p, *}$ classes are:

| $p$ | $E_\infty^{p, *}$ representative |
|:--:|--|
| $0$ | $[\mathbf{1}]$ |
| $1$ | $[\sigma_1 - \sigma_2]$ |
| $2$ | $[\sigma_1 \sigma_2 + \sigma_2 \sigma_1]$ |
| $3$ | $[\sigma_1 \sigma_2 \sigma_1] / d_2\text{-image}$ |

The $\alpha_k$ are extracted via the Markov-trace pairing on each class.

**Jones-Markov weights.** Solving the linear system
$\mathrm{tr}_M(\mathbf{1}) = 1$, $\mathrm{tr}_M(\sigma_i) = z$,
$\mathrm{tr}_M(\sigma_i \sigma_j) = z^2$ in the Wedderburn block
decomposition gives unique weights $y_\lambda$ on the three irreps
$\lambda \in \{(3), (2,1), (1,1,1)\}$.

**$\alpha_0 = 1$.** Trivial: $\mathrm{tr}_M([\mathbf{1}]) = 1$ by
Jones-Markov normalisation.

**$\alpha_1 = 0$.** By cyclicity of the Markov trace and equal
contributions from $\sigma_1, \sigma_2$:

$$
  \mathrm{tr}_M([\sigma_1 - \sigma_2])
  \;=\; \mathrm{tr}_M(\sigma_1) - \mathrm{tr}_M(\sigma_2)
  \;=\; z - z \;=\; 0.
$$

The vanishing is exact (verified to canonical precision $10^{-16}$ in
[explicit α_k witness](#witness:alpha-k-jones-markov-h3)). An
$\alpha_1$ value beyond zero would require a higher Hochschild
operation (Gerstenhaber bracket on $HH^*(H_3(R, q))$) — not the
direct trace pairing.

**$\alpha_2 = z^2$.** By Markov factorisation:

$$
  \mathrm{tr}_M(\sigma_1 \sigma_2)
  \;=\; \mathrm{tr}_M(\sigma_2 \sigma_1)
  \;=\; z^2,
$$

hence $\mathrm{tr}_M([\sigma_1 \sigma_2 + \sigma_2 \sigma_1]) = 2 z^2$
and $\alpha_2 = 2 z^2 / 2 = z^2$.

**$\alpha_3 = h z^2 + z$.** By cyclicity and the Hecke relation
$\sigma_1^2 = h \sigma_1 + \mathbf{1}$:

$$
  \mathrm{tr}_M(\sigma_1 \sigma_2 \sigma_1)
  \;=\; \mathrm{tr}_M(\sigma_1^2 \sigma_2)
  \;=\; h \, \mathrm{tr}_M(\sigma_1 \sigma_2) + \mathrm{tr}_M(\sigma_2)
  \;=\; h z^2 + z.
$$

Equivalently, since $hz = q^2(q^2-1)/(q^2+1)$ for $z = q^3/(q^2+1)$:

$$
  \alpha_3 \;=\; z\,(1 + hz) \;=\; \frac{q^3}{q^2+1}\Bigl(1 + \frac{q^2(q^2-1)}{q^2+1}\Bigr).
$$

(By contrast, the special factorization $z(1 + q^{1/2} - q^{-1/2})$ holds only for the Convention-C weight $z_C = \sqrt q/(q+1)$.)

$\square$

canonical evaluation at $q_0 \approx 1.110$ matches the symbolic
forms above to $\sim 10^{-16}$; values are tabulated in the witness
file
([`alpha-k-jones-markov-h3.witness.json`](https://github.com/litlfred/qou/blob/main/computations/alpha/alpha-k-jones-markov-h3.witness.json)).

## Alternative derivation via Wenzl-bridge

By [Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q)$ at $H_3$ admits the closed form
$y_\lambda = s_{\lambda, r}(Q) / \sum_\mu d_\mu s_{\mu, r}(Q)$ with
$Q = q^2$ and $X = Q^r = q^{3/2}/(1 + q - q^2 - q^3 + q^{3/2})$. The
Markov pairings $\alpha_k = \langle \mathrm{tr}_M, r_k \rangle$ on the
four $E_\infty$ classes inherit this $q$-rational structure
automatically; the per-class derivations below can be replaced by a
uniform application of the bridge formula (see also
[recipe](#prop:y-lambda-recipe-from-partition)).
