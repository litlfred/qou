**$\mathfrak{Q}_\beta$ cos-resummation theorem (conditional on [`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix)).**
*The single-wrap Form A closed-form prediction $\mathfrak{Q}_\beta^A$ admits a tighter symbolic refinement. We obtain this refinement by replacing the linear bridge correction $(z-1)h/2$ from [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge) with the classical cosine of half-argument:*

$$
  \mathfrak{Q}_\beta^{A,\mathrm{cos}}
  \;:=\;
  \mathfrak{Q}_\beta^A \cdot \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr),
  \qquad
  z = \tfrac{1}{\sqrt q + 1/\sqrt q},
  \quad
  h = q - q^{-1}.
$$

*This refinement tightens the CODATA residual from $+1677.5$ ppm (Form A bare) to $+305.7$ ppm, improving accuracy by a factor of $5.49$ at $q_0 \approx 1.110$.*

## Structural origin

The transfer-matrix $M_\beta$ from [`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix) has spectrum $\{e^{+i\alpha},\, e^{-i\alpha}\}$ on the $2$-dimensional irrep $V_{(2,1)}$ of $H_3(q)$, with eigenphase $\alpha = (z-1) h / 2$ at the single-wrap order. The Markov trace $\tau_M$ symmetrizes the two eigenphases:

$$
  \tau_M(M_\beta)
  \;=\;
  \tfrac{1}{2}\bigl(e^{+i\alpha} + e^{-i\alpha}\bigr)
  \;=\;
  \cos\alpha
  \;=\;
  \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr).
$$

Two structural constraints enforce this form:

1. **Markov cyclicity.** The trace is cyclic, $\tau_M(xy) = \tau_M(yx)$. It is therefore invariant under the bar involution $q \mapsto q^{-1}$, which maps $\sigma_i \mapsto \sigma_i^{-1}$ and consequently $\alpha \mapsto -\alpha$. The resummation must be even in $\alpha$; only $\alpha^{2k}$ powers survive. The minimal even-power resummation that matches the linear bridge at the perturbative level is the cosine, $\cos\alpha = 1 - \alpha^2/2! + \alpha^4/4! - \cdots$.
2. **Classical decategorification.** The mass observable lives in the classical limit (Pauli/Bose–Einstein statistics), not in the q-deformed quantum group. Empirical comparison confirms this classical nature:

   | resummation | residual at $q_0$ |
   |---|---:|
   | $\cos((z-1)h/2)$ (classical) | $+305.7$ ppm |
   | $\cos_q((z-1)h/2)$ (q-deformed) | $+313.4$ ppm |

   The classical cosine is more accurate by $\approx 7$ ppm, consistent with the classical limit of the mass observable.

## Numerical reduction

At $q_0$:

See [Table](#tbl:q-beta-cos-resummation-table-data).
