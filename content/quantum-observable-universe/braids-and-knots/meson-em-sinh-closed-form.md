Let $R$ be a field and $q \in R^\times$. Writing the substrate Planck quantum $\hbar_q = (q - 1)/q$, we have:
$$
  1 + \hbar_q - \hbar_q^2/2
  \;=\;
  1 + \frac{1 - q^{-2}}{2}
  \;=\;
  \frac{3 - q^{-2}}{2}
  \;=\;
  \frac{3 q^2 - 1}{2 q^2}.
$$
Substituting this closed form into the meson mass-squared ratio gives:
$$
  \frac{m_K^2}{m_\pi^2}
  \;=\;
  [3]_q \cdot [4]_q
  \;+\;
  \frac{\alpha_{\mathrm{em}}}{\pi}
  \cdot
  \frac{3 q^2 - 1}{2 q^2}.
$$
The strong fusion $[3]_q \cdot [4]_q$ is framework-derived and Lean-proved; it supplies $\approx 99.98\%$ of the ratio (the EM term is a $\approx 203$ ppm correction).

**Scope of the EM term.** The $\alpha_{\mathrm{em}}$ entering the EM correction is the framework's own **derived** value — the bare force-carrier coupling dressed by the Chern--Simons tower, $\alpha_{\mathrm{em}}^{-1} \approx 137.0359351$ ([fine-structure data](#rem:fine-structure-data)). No measured constant is imported.

An earlier version of this caveat stated that substituting "the derived $\alpha_{\mathrm{em}}$" degrades $m_K^2/m_\pi^2$ from $\approx 47$ ppb to $\approx 363$ ppb and concluded the ratio's L2-100× pass is $\alpha_{\mathrm{em}}$-anchored rather than parameter-free. **That is incorrect and is withdrawn.** The value substituted there, $q\,[9]_q\,[10]_q \approx 136.82$, is the *bare* coupling — the order-zero term — not the derived one. An order sweep reproduces the $363$ ppb figure exactly at order zero and gives $\approx 47$ ppb at every order from one upward, including the exact resummation. The pass is not $\alpha_{\mathrm{em}}$-anchored.

What does remain a caveat: the factor $\tfrac{3q^2-1}{2q^2}$ is the leading two-term truncation of $1 + \log(1 + \hbar_q)$, and the full series fits worse.
