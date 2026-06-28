## Distance from the substrate bound

[`thm:flavor-mass-splitting-bound`](../braids-and-knots/flavor-mass-splitting-bound.md)
gives the upper bound

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;<\;
  M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q
  \;\approx\;
  3.88\,\text{MeV},
$$

The realised value $1.286\,\text{MeV}$ sits at about $33\%$ of
the bound.  Per the slack-ratio identity in
[`thm:flavor-mass-splitting-bound`](../braids-and-knots/flavor-mass-splitting-bound.md)
the closed form for this ratio is

$$
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q}
  \;=\;
  \frac{1}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left((\Delta m / M_N)^2\right),
$$

so **the dominant contribution is the explicit $1/3$** in the
substrate formula of
[`prop:flavor-split-substrate`](flavor-split-substrate.md);
the Skein-side factor $(q^{1/2} + q^{-1/2})/(q + q^{-1}) \approx
0.997$ at $q_0$ is close to $1$ and only adjusts the slack slightly.
Tightening the bound to capture the realised value remains open
(no canonical closed form is committed in this revision).
