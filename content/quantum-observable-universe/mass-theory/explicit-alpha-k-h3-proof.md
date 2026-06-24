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

The vanishing is exact (verified to numerical precision $10^{-16}$ in
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

Equivalently, using $h / (q^{1/2} + q^{-1/2}) = q^{1/2} - q^{-1/2}$:

$$
  \alpha_3 \;=\; z \bigl(1 + q^{1/2} - q^{-1/2}\bigr).
$$

$\square$

Numerical evaluation at $q_0 \approx 1.110$ matches the symbolic
forms above to $\sim 10^{-16}$; values are tabulated in the witness
file
([`alpha-k-jones-markov-h3.witness.json`](https://github.com/litlfred/qou/blob/main/computations/alpha-k-jones-markov-h3.witness.json)).
