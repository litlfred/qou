Physics frequently uses an unspecified $\infty$ to denote an unrenormalised divergence ($\Lambda \to \infty$, $1/\varepsilon$, $\delta(0)$). These require a specific element in an extended number system. The blow-up calculus ([surreal blow-up calculus](#def:surreal-blowup-calculus)) makes each device literal in $\mathbf{No}$.

**Möbius energy diagonal.** The diagonal-regularised Möbius energy ([Möbius energy proof](#prf:mobius-energy)) computes
$$
  E(\varrho) = \iint_{S^1 \times S^1} \!\!\left(\frac{1}{|\varrho(s) - \varrho(t)|^2} - \frac{1}{D(\varrho(s), \varrho(t))^2}\right) \!ds\, dt.
$$
In the surreal lift, the inner integrand at $s = t$ evaluates to $1/0^2 = \omega^2$. The arc-length subtraction $1/D^2$ matches this $\omega^2$. The difference is a finite surreal, and its standard part is the renormalised energy.

**$c_q$ at $q = 1$.** The speed of light $c_q = 1/(q-1)$ at $q = 1 + \varepsilon$ is exactly $\omega \in \mathbf{No}$. The classical-limit divergence "$c_q \to \infty$ as $q \to 1$" becomes the literal identity $c_q\big|_{q = 1 + \varepsilon} = \omega$.

**Vacuum normalisation.** The empty-link Markov trace evaluates to $\mathrm{tr}_M(1) = z = q^3/(q^2+1)$. At $q = 1 + \varepsilon$, this is $1/2 + \varepsilon + O(\varepsilon^2)$. In the unnormalised convention $\mathrm{tr}_M(1) = 1$, normalisation factors become $1/0$. The named-surreal calculus makes these distinctions explicit.

The blow-up calculus respects the birthday grading. The counterterm $C(\omega)$ has the same birthday as $X(\omega)$. Their difference lives at a strictly lower birthday. The standard part collapses it to $\mathbb{R}$. This provides a birthday-graded refinement of BPHZ subtraction, where each subtraction reduces the birthday by a controlled ordinal amount.

The QOU mass formula contains no divergences. The blow-up calculus serves three secondary purposes:
1. **Möbius energy comparison**: turning the informal classical $\infty$ into a named $\omega^2$.
2. **Classical-limit $q \to 1$**: making "$c_q \to \infty$" literal.
3. **Future renormalisation work**: providing a setting for Yang--Mills or Sobolev-completion arguments requiring regularisation.
