**Proposition (unit-modulus eigenvalues and the Borromean fixed point).**
*For any braid word $\beta$ of even length in $H_3(q)$, the
eigenvalues of the standard representation $\rho_{(2,1)}(\beta)$
lie on the unit circle $|\lambda| = 1$. The Borromean braid
$\beta_{\mathrm{Bor}} = (\sigma_1\sigma_2^{-1})^3$ has the
degenerate eigenvalue $\lambda = -1$.*

**Proof.** The Hecke relation $\sigma_i^2 = h\sigma_i + 1$
(where $h = q - q^{-1}$) gives each generator eigenvalues $q$
and $-q^{-1}$ on $V_{(2,1)}$, with product
$q \cdot (-q^{-1}) = -1$. For a product of $n$ generators,
$\det\bigl(\rho_{(2,1)}(\beta)\bigr) = (-1)^n$. When $n$ is
even, $\det = 1$, so the eigenvalues satisfy $\lambda_1\lambda_2 = 1$.
Combined with $|\mathrm{tr}| \le 2$ (which holds for real traces
of $2 \times 2$ matrices with unit determinant), both eigenvalues
lie on the unit circle.

For the Borromean braid ($n = 6$ generators):
$\det = 1$ and the Lean-proved closed form
([`thm:borromean-markov-trace-closed-form`](borromean-markov-trace-closed-form.md))
together with the Wedderburn decomposition yield
$\chi_{(2,1)}(\beta_{\mathrm{Bor}}) = -2$. The characteristic
polynomial is then $\lambda^2 + 2\lambda + 1 = (\lambda + 1)^2 = 0$,
giving the degenerate eigenvalue $\lambda = -1$.  $\square$

## Eigenvalue table

| Operator | $(3)$ | $V_{(2,1)}$ eigenvalues | $(1^3)$ |
|----------|-------|-------------------------|---------|
| $\sigma_i$ | $q$ | $q,\; -q^{-1}$ (real) | $-q^{-1}$ |
| $L_+ = \sigma_1\sigma_2$ | $q^2$ | $e^{\pm i\theta_L}$, $\lvert\lambda\rvert = 1$ | $q^{-2}$ |
| $\mathfrak{M}_+$ (meson) | $q^6$ | $e^{\pm i\theta_M}$, $\lvert\lambda\rvert = 1$ | $q^{-6}$ |
| $\beta_{\mathrm{Bor}}$ (proton) | $1$ | $-1$ (degenerate) | $1$ |

At $q = q_0$: the Hopf link has phase
$\theta_L \approx 59°$; the meson braid has
$\theta_M \approx 54°$; the Borromean braid has $\theta = 180°$
(the unique fixed point on the unit circle where $\lambda = -1$).

## The baryon--meson duality

The sign of the $(2,1)$ contribution to the Markov trace distinguishes
the two sectors:

- **Baryons** ($\theta = \pi$, $\cos\pi = -1$): the standard
  representation contributes **negatively**.  This is the structural
  origin of the factor $\dim V_{(2,1)} = 2$ appearing as a multiplier
  in the proton substrate identity — the $(2,1)$ channel is
  *subtracted* from the symmetric channel.

- **Mesons** ($\theta \approx 54°$, $\cos\theta > 0$): the standard
  representation contributes **positively**.  All-positive-crossing
  braids force the symmetric eigenvalue $q$ to dominate, but the
  $(2,1)$ channel *adds* rather than subtracts.

The unit-modulus constraint means the $(2,1)$ channel carries
**phase information** (the angle $\theta$) but no amplitude growth —
only the $(3)$ and $(1^3)$ channels exhibit geometric growth ($q^n$
and $q^{-n}$).  Mass ratios between different braids therefore arise
from the interplay of real geometric growth on the outer channels and
oscillatory phase rotation on the standard representation.
