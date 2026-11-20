**The meson ratio.** The mass-squared ratio is:
$$
  \frac{m_K^2}{m_\pi^2}
  \;=\;
  [3]_q \cdot [4]_q
  \;+\;
  \frac{\alpha_{\mathrm{em}}}{\pi}
  \cdot
  \bigl(1 + \log(1 + \hbar_q)\bigr).
$$
The strong fusion $[3]_q \cdot [4]_q$ is framework-derived and Lean-proved; it supplies $\approx 99.98\%$ of the ratio, and the electromagnetic term is a $\approx 203$ ppm correction.

**The electromagnetic factor is the full series, not the second-order truncation.** Reading the rational expression $\tfrac{3q^2-1}{2q^2}$ of this proposition directly as the physical electromagnetic correction would replace the full logarithmic factor $1 + \log(1+\hbar_q)$ by its quadratic Taylor polynomial $1 + \hbar_q - \hbar_q^2/2$. Where a convergent power series is truncated is an external choice; writing the truncated sum in rational closed form conceals that choice rather than deriving it.

The stopping order was chosen against the data. Evaluated at the substrate anchor, the error in $m_K/m_\pi$ against the measured value is $479.1$, $23.4$, $53.5$, $51.3$, $51.49$, $51.474$, $51.4755$ parts per billion for the series stopped at $\hbar_q^1, \dots, \hbar_q^7$, converging to $51.4754$ parts per billion. The second order is the only order that falls below the limit the series converges to, and every subsequent term moves away from the measurement. A convergent series does not produce a single outlying term; selection does.

Removing the truncation moves the prediction from $23.45$ to $51.48$ parts per billion, against a target of $263.6$. The prediction survives with a margin of $5.1$, so nothing downstream turns on the choice.

**Scope of the $\alpha_{\mathrm{em}}$ input.** The $\alpha_{\mathrm{em}}$ entering the electromagnetic term is the framework's own **derived** value — the bare force-carrier coupling dressed by the Chern--Simons tower, $\alpha_{\mathrm{em}}^{-1} \approx 137.0359351$ ([fine-structure data](#sec:fine-structure-data)). No measured constant is imported.

The distinction between the derived and the bare coupling matters. Substituting the bare coupling $q\,[9]_q\,[10]_q \approx 136.82$ (the order-zero term) degrades $m_K^2/m_\pi^2$ to $\approx 363$ parts per billion; at every order from one upward, including the exact resummation, the deviation is $\approx 47$ parts per billion. The agreement is therefore not $\alpha_{\mathrm{em}}$-anchored.

**The ratio is not, however, parameter-free.** Two inputs remain selected. The pair $(3,4)$ in $[3]_q \cdot [4]_q$ was found by scanning products of $q$-integers, and the derivation of that pair from the braid content is open. And $\alpha_{\mathrm{em}}$, though derived rather than imported, is derived conditionally: its Chern--Simons dressing rests on a Witten $\kappa$ Gram-determinant value that carries an open `sorry`. The strong core alone misses the target by a factor of $385$, so the correction that clears it inherits that condition.
