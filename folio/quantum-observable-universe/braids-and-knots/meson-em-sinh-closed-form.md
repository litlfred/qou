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

**What this proposition claims, and what it does not.** The displayed chain is an exact identity of rational functions over $R$, and that is its entire content. It says that two spellings of one quantity agree. It does **not** identify that quantity with any physical correction, and it must not be cited as though it did.

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

**The electromagnetic factor is the full series, not the truncation above.** Through 2026-08-22 the second term of the ratio was written with $\tfrac{3q^2-1}{2q^2}$ in place of $1 + \log(1+\hbar_q)$ — that is, with the identity of this proposition read as the physical correction. It is not. The quantity $\tfrac{3q^2-1}{2q^2}$ is exactly $1 + \hbar_q - \hbar_q^2/2$, the series stopped after two terms, and where a series is stopped is a choice. Writing the truncated sum in closed form makes the choice invisible; it does not derive it.

The stopping order was chosen against the data. Evaluated at the substrate anchor, the error in $m_K/m_\pi$ against the measured value is $479.1$, $23.4$, $53.5$, $51.3$, $51.49$, $51.474$, $51.4755$ parts per billion for the series stopped at $\hbar_q^1, \dots, \hbar_q^7$, converging to $51.4754$ parts per billion. The second order is the only order that falls below the limit the series converges to, and every subsequent term moves away from the measurement. A convergent series does not produce a single outlying term; selection does.

Removing the truncation moves the prediction from $23.45$ to $51.48$ parts per billion, against a target of $263.6$. The prediction survives with a margin of $5.1$, so nothing downstream turns on the choice.

**Scope of the $\alpha_{\mathrm{em}}$ input.** The $\alpha_{\mathrm{em}}$ entering the electromagnetic term is the framework's own **derived** value — the bare force-carrier coupling dressed by the Chern--Simons tower, $\alpha_{\mathrm{em}}^{-1} \approx 137.0359351$ ([fine-structure data](#sec:fine-structure-data)). No measured constant is imported.

An earlier version of this caveat stated that substituting "the derived $\alpha_{\mathrm{em}}$" degrades $m_K^2/m_\pi^2$ from $\approx 47$ to $\approx 363$ parts per billion, and concluded that the ratio's agreement is $\alpha_{\mathrm{em}}$-anchored rather than parameter-free. **That is incorrect and is withdrawn.** The value substituted there, $q\,[9]_q\,[10]_q \approx 136.82$, is the *bare* coupling — the order-zero term — not the derived one. An order sweep reproduces the $363$ figure exactly at order zero and gives $\approx 47$ at every order from one upward, including the exact resummation. The agreement is not $\alpha_{\mathrm{em}}$-anchored.

**The ratio is not, however, parameter-free.** Two inputs remain selected. The pair $(3,4)$ in $[3]_q \cdot [4]_q$ was found by scanning products of $q$-integers, and the derivation of that pair from the braid content is open. And $\alpha_{\mathrm{em}}$, though derived rather than imported, is derived conditionally: its Chern--Simons dressing rests on a Witten $\kappa$ Gram-determinant value that carries an open `sorry`. The strong core alone misses the target by a factor of $385$, so the correction that clears it inherits that condition.
