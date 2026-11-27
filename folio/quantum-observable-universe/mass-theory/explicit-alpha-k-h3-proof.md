## Proof sketch

A trace factors through the cocentre $\mathrm{HH}_0(H_3) = H_3/[H_3, H_3]$. Per
[explicit $H_3$ pages](#prop:spectral-sequence-h3-explicit), the length-filtered
cocentre has three classes $[\mathbf{1}], [\sigma_1], [\sigma_1\sigma_2]$, and the
representatives $r_k$ sit as follows:

| $k$ | $r_k$ | in the cocentre |
|:--:|--|--|
| $0$ | $\mathbf{1}$ | $[\mathbf{1}]$ |
| $1$ | $\sigma_1 - \sigma_2$ | $0$ (a sum of commutators) |
| $2$ | $\sigma_1 \sigma_2$ | $[\sigma_1\sigma_2]$ |
| $3$ | $\sigma_1 \sigma_2 \sigma_1$ | $h\,[\sigma_1\sigma_2] + [\sigma_1]$ |

(The earlier sketch listed four surviving classes in $\mathrm{HH}^0 = Z(H_3)$, which has rank $3$. The trace pairing lives on $\mathrm{HH}_0$.)

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

The vanishing is exact and holds for every trace, because
$\sigma_1 - \sigma_2 = [\sigma_1, \sigma_2\sigma_1] - [\sigma_2, \sigma_1\sigma_2] - h\,[\sigma_1, \sigma_2]$
by the Hecke and braid relations.

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


$\square$

## Alternative derivation via Wenzl-bridge

By [Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q)$ at $H_3$ admits the closed form
$y_\lambda = s_{\lambda, r}(Q) / \sum_\mu d_\mu s_{\mu, r}(Q)$ with
$Q = q^2$ and $r = 2$ ($X = Q^2 = q^4$). The
Markov pairings $\alpha_k = \langle \mathrm{tr}_M, r_k \rangle$ on the
four $E_\infty$ classes inherit this $q$-rational structure
automatically; the per-class derivations below can be replaced by a
uniform application of the bridge formula (see also
[recipe](#prop:y-lambda-recipe-from-partition)).
