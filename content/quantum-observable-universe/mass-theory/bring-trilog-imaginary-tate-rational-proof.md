### Proof — via Kummer reflection formula

**Kummer reflection (Lewin 1991, Eq. 6.10):** for $z \notin (0, 1)$:

$$
  \mathrm{Li}_3(z) - \mathrm{Li}_3(1/z)
  \;=\;
  -\frac{\log^3(-z)}{6}
  - \frac{\pi^2 \log(-z)}{6}.
$$

**Apply at $z = \zeta_5 = e^{2\pi i / 5}$.**

*LHS.* $\mathrm{Li}_3(\zeta_5) - \mathrm{Li}_3(\zeta_5^{-1}) =
\mathrm{Li}_3(\zeta_5) - \overline{\mathrm{Li}_3(\zeta_5)} =
2 i\,\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = 2 i\,S_3(2\pi/5)$.

*RHS.* The principal-branch logarithm of $-\zeta_5$:

$$
  -\zeta_5 \;=\; e^{i (2\pi/5 + \pi)} \;=\; e^{i \cdot 7\pi/5}.
$$

Since $7\pi/5 > \pi$, principal logarithm reduces mod $2\pi$:

$$
  \log(-\zeta_5) \;=\; i\,(7\pi/5 - 2\pi) \;=\; -\frac{3 i \pi}{5}.
$$

Compute:

$$
  \begin{aligned}
    \log^3(-\zeta_5) &\;=\; \left(-\tfrac{3 i \pi}{5}\right)^3 \;=\; \frac{27 i \pi^3}{125}, \\
    -\frac{\log^3(-\zeta_5)}{6} - \frac{\pi^2 \log(-\zeta_5)}{6}
    &\;=\; -\frac{27 i \pi^3}{750} + \frac{3 i \pi^3}{30} \\
    &\;=\; i \pi^3 \left( -\tfrac{9}{250} + \tfrac{25}{250} \right)
    \;=\; \frac{16 i \pi^3}{250}
    \;=\; \frac{8 i \pi^3}{125}.
  \end{aligned}
$$

*Combine.* $2 i\,S_3(2\pi/5) = 8 i \pi^3 / 125$, so
$S_3(2\pi/5) = 4 \pi^3 / 125$. $\square$

### canonical structural verification at 50 dps

Verified by the canonical formalism
([witness JSON](https://github.com/litlfred/qou/blob/main/computations/kummer-reflection-zeta5.witness.json)):

| Quantity | Value (50 dps) |
|---|---|
| Direct: $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5)$ via `exact algebraic structures.polylog` | $0.9922008537\allowbreak 6959424561\allowbreak 5242082147\allowbreak 2446464712\allowbreak 0923410832\ldots$ |
| Closed form: $4 \pi^3 / 125$ | $0.9922008537\allowbreak 6959424561\allowbreak 5242082147\allowbreak 2446464712\allowbreak 0923410832\ldots$ |
| Residual | $1.34 \times 10^{-51}$ |
| Kummer formula LHS vs RHS residual | $5.35 \times 10^{-51}$ |

Both residuals are well below the working-precision $10^{-40}$
threshold — the closed form is verified to 50 digits.
